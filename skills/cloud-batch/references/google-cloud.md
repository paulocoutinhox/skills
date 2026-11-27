# Google Cloud Compute Engine

**This reference comes from the docs only.** The projects behind this skill never ran a batch on Google Cloud, so nothing here is a lesson from practice. Tell the person so, and treat the first Google Cloud batch as a trial: small, short and checked step by step. Commands and prices were checked on **2026-11-26** against the Compute Engine docs, the gcloud reference and Google's price pages (see [sources](sources.md)). Sign-in and roles are in [controller setup](controller-setup.md).

The general rules of this skill apply unchanged: batches, fresh trees, honest exit status, a timer, tags (labels here) and proven cleanup.

## Spot VM with a time limit

```bash
gcloud compute instances create <project>-batch-<session> --zone=us-central1-a --machine-type=c3-standard-8 --provisioning-model=SPOT --instance-termination-action=DELETE --max-run-duration=4h --image-family=ubuntu-2404-lts-amd64 --image-project=ubuntu-os-cloud --boot-disk-size=200GB --labels=<project>-batch=<session> --tags=<project>-batch-<session> --metadata=enable-oslogin=TRUE --metadata-from-file=startup-script=startup.sh --no-service-account --no-scopes
```

- `--max-run-duration` (30 seconds to 120 days) is the timer: at the end, the VM is deleted. Use either it or `--termination-time`, not both.
- `--instance-termination-action=DELETE` deletes the VM when Google reclaims it or the time runs out. The default for Spot VMs is `STOP`, which would leave a stopped VM and its disk billing.
- The boot disk auto-deletes by default. Check any extra disk's auto-delete setting.
- Spot VMs get no notice by default, plus up to 30 seconds for a shutdown script. A 120-second notice can be set with `--preemption-notice-duration=120s`. Detect a reclaim from inside with the metadata key `instance/preempted`. Sync results every minute anyway.
- Spot prices can change up to once a day. Seen in us-central1: `c3-standard-8` US$0.403 an hour on-demand and US$0.143 spot, `n2-standard-32` US$1.554 on-demand and US$0.932 spot.
- Billing is per second with a 1-minute minimum. An in-use external IPv4 address costs US$0.0025 an hour on a Spot VM, and a reserved static IP that sits unused costs US$0.01 an hour.
- A startup script runs as root on every boot, up to 256 KB.
- `--no-service-account --no-scopes` keeps cloud credentials off the machine. Without them, Google attaches the default Compute Engine service account, whose token any process on the VM can read.

## GPUs

- G2 machine types include NVIDIA L4 GPUs: `--machine-type=g2-standard-4 --maintenance-policy=TERMINATE`, with a boot disk of at least 40 GB.
- Prefer G2 with L4 for new plans. N1 machines with attached T4 or P4 GPUs (`--accelerator=type=nvidia-tesla-t4,count=1`) reach end of support on August 1, 2027, so do not plan new work on them.
- GPU VMs need `--maintenance-policy=TERMINATE`, since the default `MIGRATE` does not work with GPUs.
- Spot GPUs exist. Check the GPU quotas per model and region, the spot (preemptible) GPU quota and the global GPU quota first (see [budget and quotas](budget-and-quotas.md#quotas-ask-early)).

## Nested virtualization, for the Android emulator

- Add `--enable-nested-virtualization` at creation.
- It works on Intel machine series from Haswell on. It does not work on E2, Arm, most AMD series (N4D is the exception) or most memory-optimized series.
- The hypervisor inside the VM must be Linux KVM.
- An organization policy can turn it off, and it costs about 10 % or more in CPU speed.

## Prepared image

- Prepare a VM as in [AWS](aws.md#the-prepared-image-ami), stop it, then `gcloud compute images create <project>-batch-<date> --source-disk=<disk> --source-disk-zone=<zone> --family=<project>-batch`.
- Launch from the family (`--image-family=<project>-batch --image-project=<project id>`), which points at the newest image.
- Delete older images with `gcloud compute images delete <name>`, so one stays. Image storage was about US$0.05 per GiB-month.

## SSH access

- Firewall rule from the caller's address, with the session in its name, since firewall rules take no labels:

```bash
gcloud compute firewall-rules create <project>-batch-<session>-ssh --network=default --direction=INGRESS --action=ALLOW --rules=tcp:22 --source-ranges=<caller ip>/32 --target-tags=<project>-batch-<session>
```

- The create command above gives the VM the matching network tag (`--tags`) and turns on OS Login (`enable-oslogin=TRUE`).
- For keys, OS Login with an expiry is the closest match to per-session keys: `gcloud compute os-login ssh-keys add --key-file=$HOME/.ssh/<project>-batch-<session>.pub --ttl=6h`. Keys that `gcloud compute ssh` creates have no expiry.

## Delete and prove

```bash
gcloud compute instances delete <name> --zone=<zone> --delete-disks=all --quiet
gcloud compute firewall-rules delete <project>-batch-<session>-ssh --quiet
gcloud compute instances list --filter="labels.<project>-batch=<session>"
gcloud compute disks list --filter="labels.<project>-batch=<session>"
gcloud compute firewall-rules list --filter="name~^<project>-batch-<session>"
```

The three listings must be empty. Remove the session's OS Login key with `gcloud compute os-login ssh-keys remove --key-file=$HOME/.ssh/<project>-batch-<session>.pub` if its expiry is far away, and delete the key files in `~/.ssh`.

Label keys and values take only lowercase letters, digits, `_` and `-`, and a key starts with a letter, so keep the project part of the tag in lowercase.

## What Google Cloud does not offer

- No macOS machines. Apple work stays on the local Mac, CI, Xcode Cloud or an AWS Mac host.
- No Windows client images. Windows 10 or 11 needs bring-your-own-license on sole-tenant nodes, so use Windows Server images.

## Budgets and spend

A Cloud Billing budget with alert thresholds, created with the person's go (see [budget and quotas](budget-and-quotas.md#budget-alerts)), and the billing export to BigQuery for spend queries. Budgets do not cap spending.

## Sources

Checked on 2026-11-26: [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot), [limit VM run time](https://docs.cloud.google.com/compute/docs/instances/limit-vm-runtime), [instances create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create), [G-series GPU VMs](https://docs.cloud.google.com/compute/docs/gpus/create-gpu-vm-g-series), [N1 GPU VMs](https://docs.cloud.google.com/compute/docs/gpus/create-gpu-vm-general-purpose), [nested virtualization](https://docs.cloud.google.com/compute/docs/instances/nested-virtualization/overview), [custom images](https://docs.cloud.google.com/compute/docs/images/create-custom), [firewall rules create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create), [OS Login](https://docs.cloud.google.com/compute/docs/oslogin/set-up-oslogin), [labels](https://docs.cloud.google.com/compute/docs/labeling-resources), [OS details](https://docs.cloud.google.com/compute/docs/images/os-details), [VM pricing](https://cloud.google.com/compute/vm-instance-pricing), [Spot pricing](https://cloud.google.com/spot-vms/pricing) and [network pricing](https://cloud.google.com/vpc/network-pricing). See [sources](sources.md) for the full record.
