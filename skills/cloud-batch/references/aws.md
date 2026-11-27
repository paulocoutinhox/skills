# AWS: Linux batch machines, GPU machines and cloud Macs

Read this when the plan uses EC2. Everything here ran in practice, and the commands were rechecked on **2026-11-26** against the EC2 docs and AWS CLI reference (see [sources](sources.md)). Prices are us-east-1 list prices seen that day. Check them again before a plan. Credentials and the IAM policy are in [controller setup](controller-setup.md). Cleanup is in [safety and cleanup](safety-and-cleanup.md).

## The Linux batch machine

**Machine type:** compute-optimized with enough memory for the link pool. An example that worked: `c8i.8xlarge`, 32 vCPU and 64 GiB, about US$1.50 an hour on-demand, spot in us-east-1 well under that. A day with about 10 machine-hours of spot batches cost about US$6.30 in all.

**Nested virtualization** lets the Android emulator run on KVM inside the VM. Turn it on at launch with `--cpu-options NestedVirtualization=enabled`. It works on the Intel families of the 7th and 8th generations, such as C7i, M7i, R7i, C8i, M8i and R8i and their `-flex` and `d` variants. It does not work on Graviton. List the supported types with `aws ec2 describe-instance-types --filters Name=processor-info.supported-features,Values=nested-virtualization`. AWS recommends bare metal for work that is sensitive to latency.

**Disk:** gp3 with raised throughput and IOPS, such as 500 MiB/s and 6000 IOPS, deleted with the instance and tagged. The gp3 baseline is 3000 IOPS and 125 MiB/s, and storage was US$0.08 per GB-month, with extra IOPS and throughput billed on top.

**A launch,** with placeholders for the session values:

```bash
aws ec2 run-instances --region us-east-1 --placement AvailabilityZone=us-east-1b --image-id resolve:ssm:/aws/service/canonical/ubuntu/server/24.04/stable/current/amd64/hvm/ebs-gp3/ami-id --instance-type c8i.8xlarge --key-name <project>-batch-<session> --security-group-ids <group> --instance-market-options 'MarketType=spot,SpotOptions={SpotInstanceType=one-time,InstanceInterruptionBehavior=terminate}' --instance-initiated-shutdown-behavior terminate --cpu-options NestedVirtualization=enabled --block-device-mappings 'DeviceName=/dev/sda1,Ebs={VolumeSize=200,VolumeType=gp3,Iops=6000,Throughput=500,DeleteOnTermination=true}' --user-data file://user-data.sh --tag-specifications 'ResourceType=instance,Tags=[{Key=<project>-batch,Value=<session>}]' 'ResourceType=volume,Tags=[{Key=<project>-batch,Value=<session>}]'
```

Use the prepared image's id in place of the stock Ubuntu parameter once the image exists. Current Ubuntu releases use `ebs-gp3` in the parameter path.

## Spot first

1. Sort the zones by price with `aws ec2 describe-spot-price-history --instance-types c8i.8xlarge --product-descriptions "Linux/UNIX" --start-time <now in UTC>` and try the cheapest first.
2. On `InsufficientInstanceCapacity`, move to the next zone.
3. On `MaxSpotInstanceCountExceeded`, `VcpuLimitExceeded` or `SpotMaxPriceTooLow`, fall back to on-demand only if the new estimate still fits the daily allowance. Otherwise send the new estimate and wait for a go.
4. Use `SpotInstanceType=one-time` with `InstanceInterruptionBehavior=terminate`. A persistent request would bring the machine back after the batch ended.
5. Set no maximum price. AWS advises against it because it raises interruptions.

A new account starts with 5 vCPUs of standard spot quota and 0 for the G family (on-demand and spot), so even the 32-vCPU example machine cannot launch, and no GPU machine at all, until an increase arrives. Compare `L-34B43A08` (standard spot) and `L-1216C47A` (standard on-demand) with the planned vCPUs during setup, and request increases before the first batch (see [budget and quotas](budget-and-quotas.md#quotas-ask-early)).

AWS warns two minutes before it reclaims a spot machine. Sync results every minute anyway, because the warning is best effort and a step in flight is lost either way. A spot machine was once reclaimed after 67 minutes, and every unsynced result was lost.

## Security group and key

```bash
aws ec2 create-security-group --group-name <project>-batch-<session> --description "Batch SSH" --tag-specifications 'ResourceType=security-group,Tags=[{Key=<project>-batch,Value=<session>}]'
aws ec2 authorize-security-group-ingress --group-id <group> --protocol tcp --port 22 --cidr <caller ip>/32
aws ec2 create-key-pair --key-name <project>-batch-<session> --key-type ed25519 --tag-specifications 'ResourceType=key-pair,Tags=[{Key=<project>-batch,Value=<session>}]' --query KeyMaterial --output text
```

Write the key material to `~/.ssh/<project>-batch-<session>` with mode 600. Use the default VPC and a public subnet. A batch never needs a NAT gateway.

## The prepared image (AMI)

1. Launch from the stock Ubuntu image.
2. Install every toolchain with a setup script, clone the repository and warm its dependency caches. The setup script also creates the `batch` user that the examples connect as. At each launch, user data copies the session key from `/home/ubuntu/.ssh/authorized_keys` to `/home/batch/.ssh/authorized_keys`. On a stock image without that user, connect as `ubuntu`.
3. Clean it before imaging: build folders, logs, temporary files, `~/.ssh/authorized_keys`, `sudo cloud-init clean --logs --machine-id --seed` and `sudo journalctl --vacuum-time=1s`. A dirty image carries old keys and an old machine id into every launch.
4. Create the image with `aws ec2 create-image --instance-id <id> --name <project>-batch-<date>`, tagged.
5. Remove older images with `aws ec2 deregister-image --image-id <old> --delete-associated-snapshots`, so one image stays. Without that option, the snapshots stay and keep billing. Snapshot storage was US$0.05 per GB-month, so one image cost about US$1 a month.

Helpers that change often are copied at every launch, so a change to them needs no new image. Never bake a credential into an image.

## Results and lost machines

- Sync results to the controller every minute with `rsync -az` (see [batches](batches.md#sync-results-every-minute)).
- When SSH fails, check the state with `aws ec2 describe-instances --instance-ids <id> --query 'Reservations[0].Instances[0].State.Name'`. A `terminated` spot machine lost its in-flight steps. If the machine still runs after 10 minutes without SSH, report it, after checking that the caller's IP did not change.

## The self-destruct timer on Ubuntu

- User data runs `shutdown -h +<minutes>` at first boot, and the launch sets `--instance-initiated-shutdown-behavior terminate`, so the shutdown terminates the instance. `halt` does not terminate it, and the instance keeps billing.
- A `shutdown` in cloud-init `bootcmd` ran before systemd took over and was lost. Arm the timer from user data or from a systemd unit that runs after `multi-user.target`, which also re-arms it after a reboot:

```ini
[Unit]
Description=Batch self-destruct timer
After=multi-user.target

[Service]
Type=oneshot
ExecStart=/sbin/shutdown -h +240

[Install]
WantedBy=multi-user.target
```

- Ubuntu empties `/tmp` at each boot, so keep downloads in the home folder.
- Stop unattended upgrades during a batch with `sudo systemctl stop unattended-upgrades`, or bake updates into the image.
- For GCC ThreadSanitizer, set `sudo sysctl vm.mmap_rnd_bits=28` first. EC2 kernels use a larger address randomization that can overlap TSan's fixed shadow memory ("unexpected memory mapping").

## GPU machines

- **Linux, NVIDIA T4:** `g4dn.xlarge` was about US$0.53 an hour on-demand. Driver and display setup are in [Linux GPU and browsers](linux-gpu-and-browsers.md).
- **Windows, NVIDIA:** about US$0.71 an hour for the same type was seen in practice, with the Windows license included. That price was not rechecked, so read the current Windows price. Give it at least 80 GB of disk for the driver installer. Windows instances need an RSA key pair, not ed25519. Its timer is user data `<powershell>shutdown /s /t <seconds></powershell>` with `--instance-initiated-shutdown-behavior terminate`. Desktop-session setup is in [Windows desktop tests](windows-desktop.md).

## Cloud Mac (EC2 Mac dedicated host)

- A Mac runs on a dedicated host that bills **at least 24 hours**, then per second. One instance per host, on-demand only, no spot.
- Families seen in us-east-1, price per host-hour: mac2 US$0.65, mac2-m2 US$0.878, mac1 US$1.083, **mac-m4 US$1.23** (about US$30 a day), mac2-m2pro US$1.56, mac-m4pro US$1.97, mac2-m1ultra US$5.00, mac-m4max US$6.25, mac-m3ultra US$12.50.
- The host quota starts at 0 and needs a request, per family and region, such as "Running Dedicated mac-m4 Hosts" (`L-2CBA8B92`).
- Allocate with `aws ec2 allocate-hosts --instance-type mac-m4.metal --availability-zone us-east-1a --quantity 1 --tag-specifications 'ResourceType=dedicated-host,Tags=[{Key=<project>-batch,Value=<session>}]'`. Launch the Mac on it with `aws ec2 run-instances --instance-type mac-m4.metal --placement HostId=<host id> --image-id <macOS AMI id> --key-name <key> --security-group-ids <group> --tag-specifications 'ResourceType=instance,Tags=[{Key=<project>-batch,Value=<session>}]' 'ResourceType=volume,Tags=[{Key=<project>-batch,Value=<session>}]'`. Release the host with `aws ec2 release-hosts --host-ids <id>` after at least 24 hours.
- After a stop or terminate, AWS scrubs the Mac, which takes up to 4.5 hours on Apple silicon. The host is not billed during scrubbing and cannot take a new instance until it ends. Plan the day so the last batch does not need a restart.
- A Mac host has no self-destruct timer, since it bills its 24 hours anyway. Record the planned release time in the tracker when you allocate it. At the end, terminate the instance, release the host, and prove it with `aws ec2 describe-hosts --host-ids <id> --query 'Hosts[0].State'`, which must show `released`.
- Plan it as one day a month at most. Prepare the day before (batch list, bundles, Xcode and tool setup scripts, collection and release scripts), fill the day with heavy Apple work that can wait, release the host at the end, and record the cost.

## Device Farm

AWS Device Farm runs tests on real phones and tablets, and on Android emulators and iOS simulators, in `us-west-2` only. See [Device Farm](device-farm.md).

## Sources

Checked on 2026-11-26: [nested virtualization](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/amazon-ec2-nested-virtualization.html), [spot market options](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SpotMarketOptions.html), [EC2 error codes](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/errors-overview.html), [spot interruption notices](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-instance-termination-notices.html), [instance-initiated shutdown](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_ChangingInstanceInitiatedShutdownBehavior.html), [key pairs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-key-pairs.html), [Ubuntu images on AWS](https://ubuntu.com/aws/docs/aws-how-to/instances/find-ubuntu-images/), [gp3 volumes](https://docs.aws.amazon.com/ebs/latest/userguide/general-purpose.html), [deregister an AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/deregister-ami.html), [EC2 Mac instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-mac-instances.html), [NVIDIA GRID drivers](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/nvidia-GRID-driver.html), [EC2 pricing](https://aws.amazon.com/ec2/pricing/) and the [sanitizer workaround issue](https://github.com/actions/runner-images/issues/9491). See [sources](sources.md) for the full record.
