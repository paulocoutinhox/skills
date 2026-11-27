# Safety, timers and proven cleanup

Read this before you write a launch or delete script and before every session. Each rule has its reason. Provider commands were checked on **2026-11-26** (see [sources](sources.md)). Where keys live and how each CLI signs in is in [controller setup](controller-setup.md).

## Access to the machine

- **SSH key login only.** A password can be guessed and leaks into logs.
  - **AWS:** each session creates a fresh key pair, `aws ec2 create-key-pair --key-name <project>-batch-<session> --key-type ed25519 --tag-specifications 'ResourceType=key-pair,Tags=[{Key=<project>-batch,Value=<session>}]' --query KeyMaterial --output text`, saved to `~/.ssh/<project>-batch-<session>` with mode 600 and deleted with the session. ed25519 key pairs work for Linux instances only. Windows instances on AWS need an RSA key pair.
  - **Azure:** one ed25519 key in `~/.ssh` for the persistent VM. The admin password at creation is random (`openssl rand -base64 30`) and is unset right after. The setup script then gives the batch user a new random password that is stored only as the Windows LSA secret that autologon reads, so no copy leaves the machine. Set `PasswordAuthentication no` in `C:\ProgramData\ssh\sshd_config`.
  - **The person's own machine:** install their public key once, then `ssh -o BatchMode=yes <user>@<host>`. If they gave a password in the chat, never write it anywhere, and ask them to install the key.
- **The firewall opens SSH only from the caller's current address.** Get it with `curl -fsS https://checkip.amazonaws.com` and allow `<ip>/32`. Remove the rule when the batch ends, so only the controller can ever reach SSH.
- **Use one known_hosts file per session,** next to the session key: `-o UserKnownHostsFile=~/.ssh/<project>-batch-<session>.known_hosts -o StrictHostKeyChecking=accept-new`. Cloud providers reuse public IPs, and a reused IP with an old host key in `~/.ssh/known_hosts` makes `BatchMode` SSH fail. Delete the file with the session.
- **The caller's address can change** during a long session, such as on home internet. SSH then fails while the machine still runs. Authorize the new `/32` and remove the old one.
- **The batch machine holds no cloud keys.** What it needs comes through stdin of the SSH command or as a short-lived presigned URL, such as `aws s3 presign <url> --expires-in 600`. A machine with keys is a leak waiting to happen.
- **Cache credentials go through stdin,** read with `IFS= read -r` and kept only in the job's environment, never written to disk (see [CI and caches](ci-and-cache.md)).
- **Never weaken a machine's security to make a batch faster,** such as antivirus exclusions or turning off Defender. On Windows 11, a Dev Drive (ReFS, with Defender's performance mode on a trusted drive) is the supported way to speed up builds.

## Tags and protected resources

- Tag every resource with one key, such as `<project>-batch=<session>`. Listings and deletions use the tag, and nothing else is touched, so a deletion can never reach another project's resources.
- Write down the resource groups, images and buckets that are never touched, and check deletions against that list.
- AWS: `run-instances --tag-specifications` can tag the instance, its volumes, the spot request and the network interface at launch. Tag the security group at `create-security-group` with `ResourceType=security-group`, and the key pair at `create-key-pair` with `ResourceType=key-pair`.
- Google Cloud labels work on instances, disks, images and snapshots, not on firewall rules. Give firewall rules a name prefix of the session instead.
- Azure: put the batch resources in a resource group of their own, tagged.

## Account resources need the person's go

Never create secrets, buckets, tokens, budgets, quota requests, service accounts or accounts before the person says to. Secrets were once created in the wrong project because nobody waited. Each project has its own credentials and buckets and never shares them.

## The self-destruct timer

Every rented machine has a timer, so a forgotten machine ends by itself. The cloud Mac host is the one exception:

| Provider | Timer |
| --- | --- |
| AWS | User data runs `shutdown -h +<minutes>`, and the launch sets `--instance-initiated-shutdown-behavior terminate`. A shutdown from inside the OS then terminates the instance. `halt` does not: the instance keeps running and billing |
| Azure | `az vm auto-shutdown -g <group> -n <vm> --time <UTC HHMM>`. The docs do not say whether it deallocates, so the batch script still deallocates and checks the power state |
| AWS Windows | User data `<powershell>shutdown /s /t <seconds></powershell>`, with the same `--instance-initiated-shutdown-behavior terminate` |
| AWS Mac host | No timer, since the host bills 24 hours anyway. The planned release goes in the tracker, and the release is proven with `describe-hosts` (see [AWS](aws.md#cloud-mac-ec2-mac-dedicated-host)) |
| Google Cloud | `--max-run-duration=<hours>h` with `--instance-termination-action=DELETE` at creation. From the docs only |

- Size the timer to the estimate plus a margin, such as +50 %.
- To extend it, run `sudo shutdown -h +<minutes>` on the machine (a new `shutdown` replaces the old one) and record the new time in the tracker. A timer was once too short for work added later.
- After any reboot, confirm the timer is armed again. On Ubuntu, arm it from a systemd unit (see [AWS](aws.md#the-self-destruct-timer-on-ubuntu)).
- Never stop a session early unless the person asks. Losing hours of tests costs more than the extra time. The one exception: the run of a bundle that a newer bundle of the same line of work replaced. Stop that job alone to free the machine, and the session goes on.

## Delete everything, and prove it

Every session ends by deleting what it created, then listing by tag to prove nothing is left. The script exits non-zero if anything remains. A forgotten volume or public IP bills every hour.

| Provider | Delete | Proof |
| --- | --- | --- |
| AWS | Instance, volumes, security group, key pair (in AWS and in `~/.ssh`), any Elastic IP, and on a Mac day the dedicated host | `describe-instances` shows `terminated`, 0 volumes, security groups, key pairs and Elastic IPs carry the tag, and `describe-hosts` shows the host `released` |
| Azure, kept VM | Build folders and temporary files, then `az vm deallocate`, then the public IP and the NSG rule | Power state `PowerState/deallocated`, no public IP, and the resource group holds only the expected resources |
| Google Cloud | Instance with its disks, firewall rules, session SSH keys | `instances list`, `disks list` and `firewall-rules list` show nothing for the session |
| Device Farm | The run's project | `list-projects` no longer shows it |
| Google Device Run | The session's result folder, after its files are saved | `gcloud storage ls` no longer lists the session |
| Own machines | Worktrees, build folders, bundles, booted simulators and emulators, installed test apps | `git worktree list`, `xcrun simctl list devices booted`, `adb devices`, free disk reported |

A security group cannot be deleted while an instance that is not yet terminated still uses it, so wait until the instance state is `terminated` first.

An example proof step for AWS, in Python with uv. It takes the tag key and the session, calls the CLI directly and fails loudly. It also checks the session's Elastic IPs and dedicated hosts, and that its key and known_hosts files in `~/.ssh` are gone. `describe-hosts` takes `--filter`, not `--filters`, and filters by `tag-key` only, so the script compares the tag value itself:

```python
# /// script
# requires-python = ">=3.11"
# ///

import json
import subprocess
import sys
from pathlib import Path


def aws_json(arguments: list[str]) -> dict:
    result = subprocess.run(["aws", *arguments, "--output", "json"], capture_output=True, text=True, check=True)
    return json.loads(result.stdout)


def leftovers(tag_filter: str) -> list[str]:
    found = []
    reservations = aws_json(["ec2", "describe-instances", "--filters", tag_filter])["Reservations"]

    for reservation in reservations:
        for instance in reservation["Instances"]:
            if instance["State"]["Name"] != "terminated":
                found.append(f"instance {instance['InstanceId']} is {instance['State']['Name']}")

    volumes = aws_json(["ec2", "describe-volumes", "--filters", tag_filter])["Volumes"]
    found.extend(f"volume {volume['VolumeId']}" for volume in volumes)
    groups = aws_json(["ec2", "describe-security-groups", "--filters", tag_filter])["SecurityGroups"]
    found.extend(f"security group {group['GroupId']}" for group in groups)
    key_pairs = aws_json(["ec2", "describe-key-pairs", "--filters", tag_filter])["KeyPairs"]
    found.extend(f"key pair {key_pair['KeyName']}" for key_pair in key_pairs)
    addresses = aws_json(["ec2", "describe-addresses", "--filters", tag_filter])["Addresses"]
    found.extend(f"Elastic IP {address['AllocationId']}" for address in addresses)
    return found


def hosts_left(tag_key: str, session: str) -> list[str]:
    hosts = aws_json(["ec2", "describe-hosts", "--filter", f"Name=tag-key,Values={tag_key}"])["Hosts"]
    session_hosts = [host for host in hosts if {"Key": tag_key, "Value": session} in host.get("Tags", [])]
    return [f"host {host['HostId']} is {host['State']}" for host in session_hosts if not host["State"].startswith("released")]


def main() -> int:
    tag_key = sys.argv[1]
    session = sys.argv[2]
    tag_filter = f"Name=tag:{tag_key},Values={session}"
    found = leftovers(tag_filter) + hosts_left(tag_key, session)
    ssh_folder = Path.home() / ".ssh"
    session_files = [ssh_folder / f"{tag_key}-{session}", ssh_folder / f"{tag_key}-{session}.known_hosts"]
    found.extend(f"file {path}" for path in session_files if path.exists())

    if found:
        print("Left over after cleanup: " + ", ".join(found))
        return 1

    print(f"Session {session}: nothing left.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

When a listing is not empty, retry the deletion of what is left, record it in the tracker's 🧹 Open Cleanup Items, and tell the person until it is gone.

## A kept, prepared machine is cleaned instead

A persistent VM, such as the Azure Windows GPU VM, is cleaned and deallocated so that only its disk bills:

- its build folders and temporary files go;
- its public IP and its SSH rule go;
- it is deallocated, not only stopped. A stopped Azure VM still bills compute.

## Hidden costs to look for in every cleanup

- **AWS:** volumes that outlive their instance (set `DeleteOnTermination=true`), snapshots and AMIs that pile up (keep one image), every public IPv4 address (US$0.005 an hour each, attached or idle, Elastic IPs included), NAT gateways (a batch never needs one: use the default VPC and a public subnet), data transfer out, CloudWatch log storage, S3 buckets, Device Farm projects.
- **Azure:** managed disks bill while the VM is deallocated (use Standard HDD for a disk that waits), Standard public IPs bill while they exist (US$0.005 an hour), snapshots, and Bastion (a batch never needs it). Network Watcher, which Azure creates by itself in `NetworkWatcherRG`, adds no charge. Leave it there.
- **Google Cloud:** persistent disks after the VM is deleted, unless they auto-delete (boot disks do by default), reserved static external IPs that sit unused (US$0.01 an hour), images and snapshots.
- **Cache buckets:** storage per GB-month plus operations. Set lifecycle expiry.

Prices were seen on 2026-11-26. Check them again before a plan.

## Sources

Checked on 2026-11-26: [key pairs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-key-pairs.html), [authorize-security-group-ingress](https://docs.aws.amazon.com/cli/latest/reference/ec2/authorize-security-group-ingress.html), [instance-initiated shutdown](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_ChangingInstanceInitiatedShutdownBehavior.html), [az vm auto-shutdown](https://learn.microsoft.com/en-us/cli/azure/vm), [Azure states and billing](https://learn.microsoft.com/en-us/azure/virtual-machines/states-billing), [limit VM run time on Google Cloud](https://docs.cloud.google.com/compute/docs/instances/limit-vm-runtime), [Google Cloud labels](https://docs.cloud.google.com/compute/docs/labeling-resources), [VPC pricing](https://aws.amazon.com/vpc/pricing/), [Azure IP pricing](https://azure.microsoft.com/en-us/pricing/details/ip-addresses/), [Google Cloud network pricing](https://cloud.google.com/vpc/network-pricing), [Sysinternals Autologon](https://learn.microsoft.com/en-us/sysinternals/downloads/autologon) and [Dev Drive](https://learn.microsoft.com/en-us/windows/dev-drive/). See [sources](sources.md) for the full record.
