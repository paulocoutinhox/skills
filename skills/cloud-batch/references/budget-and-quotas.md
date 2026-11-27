# Budget, spend checks, quotas and licensing

Read this when you split a budget, check the spend before a batch, set up alerts, request quotas or choose a licensed image. Prices and terms were checked on **2026-11-26** (see [sources](sources.md)). They change, so check them again before a plan.

## The budget routine

1. Ask for the hard monthly limit and split it per provider (an example split is in [interview and plan](interview-and-plan.md#split-the-budget)).
2. Before every batch, check the month's spend and estimate the batch: price per hour × hours × machines, plus storage, public IPs, transfer and per-call charges.
3. The daily allowance is the share left ÷ the days left in the month. A batch that would pass it waits for the next day, or goes to the person with its estimate.
4. Report the spend each day. Stop when a share runs out.
5. Keep your own estimate in the tracker from machine-hours × the price seen at launch, and reconcile it with the billing data later. Billing data arrives late.

Cut cost first with spot capacity, prepared images, a remote compiler cache so sessions are short, and the person's own machines.

## Spend checks

**AWS:** Cost Explorer must be turned on once by the person, in the Billing and Cost Management console, and its first data takes about a day to appear. Until then, `ce` calls fail, so use the tracker's estimates and say so in the report.

```bash
aws ce get-cost-and-usage --time-period Start=2026-11-01,End=2026-11-26 --granularity MONTHLY --metrics UnblendedCost
aws ce get-cost-and-usage --time-period Start=2026-11-25,End=2026-11-26 --granularity DAILY --metrics UnblendedCost
```

- `End` is exclusive, so the first line covers November 1 to 25.
- **Each Cost Explorer API call costs US$0.01.** Call it a few times a day at most, never in a loop.
- Cost Explorer reflects usage up to the previous day, and some data arrives later than 24 hours.

**Azure:**

- `az consumption usage list` lists usage. The whole `az consumption` group is in Preview.
- There is no `az costmanagement query` command. For a cost query, call the Cost Management Query REST API with `az rest --method post --url "https://management.azure.com/subscriptions/<id>/providers/Microsoft.CostManagement/query?api-version=<current version>" --body @query.json`, taking the current API version from its reference page.
- The Cost analysis page of the portal shows the same numbers for the person.

**Google Cloud** (from the docs only):

- Cloud Billing export to BigQuery, then a query per month. Data loads throughout the day, and the first backfill can take up to 5 days.
- The Billing reports page of the console for the person.

## Budget alerts

Offer one monthly budget alert per provider, created only with the person's go, since it is an account resource. Use alerts at 50 %, 80 % and 100 % of the provider's share, unless the person wants other levels:

| Provider | How | Cost |
| --- | --- | --- |
| AWS | AWS Budgets: `aws budgets create-budget --account-id <id> --budget file://budget.json --notifications-with-subscribers file://notifications.json`, with e-mail alerts | Budgets and their alerts are free. Budgets update up to three times a day |
| Azure | A Cost Management budget with e-mail alerts, in the portal or through the Budgets REST API. `az consumption budget create` is in Preview and has no notification option at subscription level | Free |
| Google Cloud | `gcloud billing budgets create --billing-account=<id> --display-name=<name> --budget-amount=100USD --threshold-rule=percent=0.5 --threshold-rule=percent=0.8 --threshold-rule=percent=1.0` | Free |

Alerts only warn. They arrive late and do not stop spending. The plan's own check before every batch is what keeps spend inside the limit.

## Billing granularity

| Provider | Documented terms |
| --- | --- |
| AWS Linux and Windows instances, on-demand and spot | Per second, with a 60-second minimum |
| AWS Mac dedicated host | A 24-hour minimum allocation, then per second |
| Azure VMs | Billed while allocated. A deallocated VM bills only its disks and any public IP. The docs checked do not state a per-second rule for current sizes |
| Google Cloud VMs | Per second, with a 1-minute minimum |

## Spot capacity

| Provider | How it works |
| --- | --- |
| AWS spot | A two-minute interruption notice, best effort, in instance metadata (`/latest/meta-data/spot/instance-action`) and as an EventBridge event. Pick the cheapest zone, then the next zone, then on-demand ([AWS](aws.md#spot-first)) |
| Azure Spot VMs | `az vm create --priority Spot --eviction-policy Deallocate --max-price -1`. With `-1`, the VM is never evicted for price and never billed above the standard rate. Eviction comes with up to 30 seconds of notice. Suits Linux batches |
| Google Cloud Spot VMs | `--provisioning-model=SPOT`. The default notice is 0 seconds plus up to 30 seconds for a shutdown script. Spot prices can change up to once a day |

The persistent Windows GPU VM on Azure stays a regular VM, because it keeps a prepared disk and must not vanish in the middle of a batch.

Long jobs on spot capacity need checkpoints: split them into steps whose results sync as each ends.

## Quotas: ask early

Quota requests take from hours to days. Check the quotas during the interview with read-only commands, and file requests before the first batch that needs them, with the person's go.

**AWS** quotas count vCPUs, and spot quotas are separate from on-demand quotas:

| Quota | Code | Default seen |
| --- | --- | --- |
| Running On-Demand Standard (A, C, D, H, I, M, R, T, Z) instances | `L-1216C47A` | 5 |
| Running On-Demand G and VT instances | `L-DB2E81BA` | 0 |
| All Standard (A, C, D, H, I, M, R, T, Z) Spot Instance Requests | `L-34B43A08` | 5 |
| All G and VT Spot Instance Requests | `L-3819A6DF` | 0 |
| Running Dedicated mac-m4 Hosts | `L-2CBA8B92` | 0 |

Read one with `aws service-quotas get-service-quota --service-code ec2 --quota-code <code>`. Request with `aws service-quotas request-service-quota-increase --service-code ec2 --quota-code <code> --desired-value <n>`. A new account starts with 0 for both G and VT quotas, on-demand and spot, so GPU batches wait until an increase arrives. Request both early.

**Azure** quotas count vCPUs per VM family per region, and GPU families often start at 0. Read them with `az vm list-usage --location <region> -o table`. Find the family name of a size with `az vm list-skus --location <region> --size <size> --query "[].family" -o tsv`. Raise one with `az quota update --resource-name <family> --scope /subscriptions/<id>/providers/Microsoft.Compute/locations/<region> --limit-object value=<n> --resource-type dedicated`, after registering `Microsoft.Quota`. A quota of 8 vCPUs holds one 8-vCPU GPU machine at a time, so Linux and Windows GPU runs go one after the other.

**Google Cloud** (from the docs only): regional CPU quotas, GPU quotas per model and region (such as `GPU_FAMILY:NVIDIA_L4`, and `PREEMPTIBLE_NVIDIA_L4_GPUS` for spot) and a global "GPUs (all regions)" quota. Read them in the Quotas page, with `gcloud compute regions describe <region>`, or with Cloud Quotas.

**Device Farm:** 5 metered automation devices at once and 2 remote access devices by default, both adjustable.

## Licensing

- **Windows 11 on Azure** with `--license-type Windows_Client` states that the person holds eligible rights: Microsoft 365 E3, E5, A3, A5, F3 or Business Premium, Windows Enterprise E3 or E5, Windows VDA E3 or E5, or Windows Education A3 or A5. Ask. Without those rights, use a Windows Server image, whose license is in the hourly price (the Windows price of a size is higher than its Linux price).
- **Windows on AWS:** license-included Windows Server instances cost more per hour than Linux.
- **Windows client on Google Cloud:** Google provides no Windows client images, only bring-your-own-license on sole-tenant nodes. Use Windows Server images there.
- **macOS:** Apple's license allows macOS only on Apple hardware, with up to two extra virtual copies per Mac, and leasing for at least 24 consecutive hours. That is why cloud Macs are dedicated hosts with a 24-hour minimum.
- **Device Farm and the stores:** test builds are signed with the person's own team, and the store terms apply.

## Cheaper or free options before renting

- **CI the person already has.** Standard GitHub-hosted runners are free for public repositories. For private repositories, GitHub bills per minute: macOS minutes cost about 10 times Linux minutes (US$0.062 against US$0.006 seen), so use macOS runners only for Apple jobs.
- **Xcode Cloud:** 25 compute hours a month are included with the Apple Developer Program, counted per task, not wall time (see [Xcode Cloud](xcode-cloud.md#compute-hours-and-budget)).
- **Google's Developer Device Platform** (Device Run), in Preview when checked: a cheaper device lab for real-hardware checks on Android and iOS, not a replacement for local simulators and emulators (see [Google Device Run](google-device-run.md)). Firebase Test Lab is deprecated and shuts down on September 30, 2027, so do not plan new work on it.
- **Third-party device clouds,** with their own prices. List them for the person to evaluate, and do not sign up for them.
- **Spare machines and devices** of the person: no hourly cost.
- **Docker on the local machine** for Linux reproduction.

## Sources

Checked on 2026-11-26: [GetCostAndUsage](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetCostAndUsage.html), [Cost Explorer pricing](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/pricing/), [AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html), [EC2 instance quotas](https://docs.aws.amazon.com/ec2/latest/instancetypes/ec2-instance-quotas.html), [Azure Cost Management Query API](https://learn.microsoft.com/en-us/rest/api/cost-management/query/usage), [Azure budgets](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets), [az quota](https://learn.microsoft.com/en-us/cli/azure/quota), [Azure Spot VMs](https://learn.microsoft.com/en-us/azure/virtual-machines/spot-vms), [Google Cloud budgets](https://docs.cloud.google.com/billing/docs/how-to/budgets), [Google Cloud Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot), [Windows 11 multitenant hosting rights](https://learn.microsoft.com/en-us/azure/virtual-machines/windows/windows-desktop-multitenant-hosting-deployment), [macOS Tahoe license](https://www.apple.com/legal/sla/docs/macOSTahoe.pdf), [GitHub Actions billing](https://docs.github.com/en/billing/concepts/product-billing/github-actions), [Xcode Cloud](https://developer.apple.com/xcode-cloud/) and the [Test Lab deprecation FAQ](https://firebase.google.com/docs/test-lab/migrate-faq). See [sources](sources.md) for the full record.
