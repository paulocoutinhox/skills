# The Cloud Tracker

Read this when the person wants the tracker, and before every change to it. The tracker is one Markdown file, usually `CLOUD.md`, that shows at a glance what runs, what it costs, how each platform stands and what is left to clean up. It is also the coordinator's handoff file for the next session.

## Create it

1. Ask where to keep it. The default is outside the repository, such as next to the person's other planning files, because it changes many times a day. Put it in the repository only if the person wants that.
2. Copy [the tracker template](../assets/cloud-tracker.md) to that path. Keep its layout, the same idea as a Kanban board, with the most important information first: the title and the 📊 Overview, a summary of what happens in each service, open the file with nothing above them. Then come 🏃 Running Now, 🧹 Open Cleanup Items, 💰 Budget, 🗓️ Planned, 🧩 Platforms, 📜 Batch Log, 🗄️ Persistent Resources, 📏 Quotas and ⏱️ Measured Durations, and the 📋 Rules and the 🚦 Legend close it. Keep its title, `# ☁️ Cloud Tracker`, and every section title exactly as the template writes them: with their emoji and each word starting with a capital letter, such as `## 🏃 Running Now`. Never rename or translate them, since the next session and the links find the sections by those titles. Row text can use the person's language.
3. Remove the rows and sections of the services and platforms the plan does not use. Fill the monthly limit, the shares, the month, the quotas and the persistent resources from the plan. Replace every `<placeholder>`.
4. Record the path in the plan, so every later session finds it.

## Who writes it

Only the coordinator writes the tracker. Lines of work keep their own short state files and send results to the coordinator, who records them. Two writers would overwrite each other's rows.

## The one rule: every change updates the file at once

Every action that changes the state of a machine, a run, a build, a cost, a quota, a decision or a result updates the tracker **right after the action, before the report to the person and before the next action**. Never collect changes to write later. A batch that ends while the file still says "running" misleads the next session, and a forgotten machine bills every hour.

Each update also:

- sets `Last updated` to the current UTC time;
- changes the status emoji of every row it touches;
- brings the 📊 Overview row of that service in line with its section.

## Resume a session from it

A session that starts, or resumes after a crash or a lost context, reads the tracker first, then checks it against the real state before acting:

- machines and their tags: `aws ec2 describe-instances --filters Name=tag:<project>-batch,Values=*`, `aws ec2 describe-hosts --filter Name=tag-key,Values=<project>-batch` (hosts filter by tag key only), `az vm list -g <group> -d -o table`, `gcloud compute instances list --filter="labels.<project>-batch:*"`;
- device labs: `aws devicefarm list-projects --region us-west-2`, keeping the projects whose name starts with `<project>-batch-`, then `aws devicefarm list-runs --region us-west-2 --arn <project arn>` for each, and `gcloud beta device-run sessions list` plus `gcloud alpha device-run sessions list` when iOS runs are planned;
- Xcode Cloud: `GET /v1/ciWorkflows/{id}/buildRuns`;
- CI: `gh run list --limit 10`;
- own machines: who holds the lock, and which simulators and emulators are booted;
- for every 🏃 or 📜 row whose cleanup is not proven, the provider's full tag listing from [safety and cleanup](safety-and-cleanup.md#delete-everything-and-prove-it), such as the AWS proof script, so a security group, key pair, public IP or firewall rule left by a crash is found.

Fix every row that does not match, with a 🔴 row in 🧹 Open Cleanup Items for anything running that the file did not know. Then continue.

## What each event changes

| Event | Sections to change |
| --- | --- |
| Plan agreed or changed | 💰 shares, 📏 needed quotas, 🗄️ Persistent Resources, 🗓️ Planned, and the 📊 and 🧩 rows of the services and platforms in use. For a newly used service, copy its 🏃 section and its 💰 row back from the template |
| New month | 💰 month, days left, spent (US$0, 0 hours, 0 minutes) and cost status. 📊 this month. 🗓️ cost status of each planned batch against the new daily allowance. Keep the old month's 📜 rows |
| Spend checked (before each batch and daily) | 💰 spent, figure date, left, days left, daily allowance, projected month end, cost status. 📊 this month and cost status |
| Quota checked, requested, granted or refused | 📏 limit, needed, request date, status |
| Batch estimated | 🗓️ new row 🔵 with the estimate and its cost status against the daily allowance |
| Person's go asked | 🗓️ row 🟡 "waiting for go". Go given: 🔵 or launch. Refused: row removed, reason in the report |
| Machine launched, or a persistent VM started | 🏃 row 🟡 starting, with zone, market, price seen and "ends at". 🗄️ VM row 🟢. 📊 🟡 |
| SSH up and jobs started | 🏃 row 🟢 with what it runs. 🗓️ that batch removed |
| Spot fell back to on-demand, or the zone changed | 🏃 row 🟠 with the new market and price |
| Work attached, a bundle replaced or the timer extended | 🏃 "what it runs" and "ends at". If the new estimate passes the batch's estimate, row 🟠 and the next report says so. If it passes the daily allowance, ask for a go first |
| Cost refreshed (at every progress check and report) | 🏃 "cost so far". Row 🟠 when it passes the estimate |
| Timer close while jobs remain | 🏃 row 🟠 until the timer is extended |
| Credential failure | Affected 🏃 or 🗓️ row 🔴 "credential", until the person renews it |
| Machine lost or spot reclaimed | 🏃 row 🔴 with the steps lost, then the batch-finished event with what did finish |
| Cloud Mac host allocated | 🔶 row 🟡 with market "dedicated host" and "ends at" set to the planned release. "Next cloud Mac day" cleared |
| Device Farm or Device Run run scheduled or running | Its 🏃 section: devices, physical or virtual, timeout, tests, device minutes, cost, status |
| Xcode Cloud build started or running | 🛠️ row: workflow, actions, status. Compute hours estimated from the actions' start and finish times until the usage page confirms them |
| CI run started by hand or running | ⚙️ row: workflow, ref, who started it, minutes, status |
| A local build takes or frees the lock | 🏠 row: lock held, what it runs, free disk |
| **Any batch, run or build finished** (any service, own machines included) | 🏃 row out. 📜 new row with the session name, results per job, status 🟡 until its cleanup is proven, or at once 🟢 or 🟠 with "Deleted and proven" set to `not needed` for runs that leave nothing to delete, such as CI and Xcode Cloud. Same row: duration, cost (0 on own machines) and cache hit rate. 🧩 last result per platform. ⏱️ measured durations. 💰 estimate added |
| Deletion proven, persistent VM deallocated or Mac host released | 📜 "Deleted and proven" ✅, and status 🟢 or 🟠 by the test results, or 🔴 if the run was lost. 🗄️ VM row ⚪. 📊 ⚪ when nothing else runs |
| Listing shows a leftover | 🧹 new 🔴 row. 📜 "Deleted and proven" ❌ and status 🔴. 📊 row of that service 🔴 until it is removed |
| Leftover removed | 🧹 row ⚪ with "Removed on" filled, kept until the next report, then removed. 📊 row ⚪, or the state of what still runs. 📜 "Deleted and proven" ✅ with the date, and status 🟢 or 🟠 by the test results, or 🔴 if the run was lost |
| Persistent resource created, kept or removed | 🗄️ row added, changed or removed, with its monthly cost |
| Billing data arrives | 📜: replace the estimate with the billed figure and write `billed`. 💰 changes only when the batch belongs to the current month |
| Cloud Mac day planned | "Next cloud Mac day" set, and its batches in 🗓️ |

## Choose the emoji

- **Status:** 🟢 runs or ended as planned with every test passing, 🟡 waits (starting, queued, uploading, waiting for a go), 🟠 needs attention soon (timer close, fallback, cost above its estimate, failed tests), 🔴 failed to run, lost, over budget or left something, ⚪ idle, deallocated or released, 🔵 planned.
- **📜 Batch Log status** covers the run and its cleanup: 🟡 the run ended and its cleanup is not proven yet (runs that leave nothing to delete skip this), 🟢 every test passed and cleanup is proven, 🟠 some tests failed but the run and cleanup are fine, 🔴 the run was lost or something was left. The results column shows the tests.
- **Cost of a share:** spent ÷ share. 🟢 under 50 %, 🟡 50 % to under 80 %, 🟠 80 % to 100 %, 🔴 over 100 %.
- **Cost of a batch:** 🟢 inside the daily allowance, 🟠 needs the person's go, 🔴 started above it.
- **Results:** ✅ passed, ❌ failed, ⏭️ skipped for a missing capability, ⏳ running. A skipped test is never shown as passed.
- **Platforms:** 🐧 Linux, 🪟 Windows, 🍎 Apple, 🤖 Android, 🌐 Web, 🎮 GPU work.

## Compute the cost

Use one formula everywhere: **price per hour × hours × machines, plus storage, public IPs, transfer and per-call charges**. A 200 GB gp3 disk with raised IOPS and a public IPv4 add roughly 10 % to a US$0.60 spot machine, so leave them out only when they are truly small.

- **Machines:** the price seen at launch, since spot prices change. Mark the figure `estimate`.
- **Device farms:** device minutes × price per device minute, for physical or virtual devices as billed.
- **Xcode Cloud:** compute hours from the usage page, against the hours included or bought.
- **CI:** minutes from the billing page, against the included amount.
- **The month:** the provider's billing figure with its date, plus the estimates of what ran after that date.

## Keep it short

- Rows leave 🏃 Running Now when their machine, run or build ends, and their result moves to 📜 Batch Log.
- A section in use that becomes empty keeps its `None` row, with ⚪ where the table has a Status column, as in the template.
- Keep the 📜 Batch Log of the current and the previous month. Move older rows out, or delete them if the person agrees.
- Keep one row per platform in 🧩 Platforms, with only the latest result.

## No sensitive data

The tracker never holds credentials, keys, tokens, passwords, connection strings, IP addresses, host names, presigned or expiring URLs, device serials or UDIDs, personal or customer data, e-mail addresses, account or subscription ids, or private absolute paths. Name devices by role, such as "test phone, Android 15", accounts by provider, and credentials by variable name only. Session names and tagged resource names such as `<project>-batch-<session>` are fine. Reread the changed text for such data before saving, and remove anything found at once.

## Example: one machine through a day

| Time (UTC) | Action | What the file shows |
| --- | --- | --- |
| 09:58 | Spend checked, batch estimated at 3 hours, US$1.80 | 🗓️ 🔵 batch-1, US$1.80, cost status 🟢 |
| 10:02 | Spot launch in us-east-1b | 🔶 🟡 batch-1, 🐧 Linux, c8i.8xlarge, spot, US$0.60, ends at 14:32 |
| 10:06 | SSH up, 3 bundles running | 🔶 🟢 running "physics (2 commits), render (1), nodes (3)". 🗓️ row removed |
| 12:40 | A fixed bundle replaces render's old one, timer extended, new estimate US$2.55, above US$1.80 but inside the daily allowance | 🔶 🟠 "render (new bundle)", ends at 15:30, new estimate noted for the report |
| 14:10 | Last job ends | 🔶 row out. 📜 🟡 results ✅ physics ✅ nodes ❌ render, US$2.48 estimate, "Deleted and proven" empty. 🧩 🐧 Linux 🟠 |
| 14:14 | Instance, volumes, group and key deleted and listed | 📜 "Deleted and proven" ✅ and status 🟠, since render failed. 📊 AWS EC2 ⚪ |
| Next day | Billing data for the day arrives | 📜 US$2.51 billed. 💰 spent updated |

Each line of that table is one update of the file, made right after its action. Each line also makes every other change its event lists in the table above, such as 💰 and 📊 on a spend check and ⏱️ and 💰 when a batch ends.

## Sources

This procedure follows the tracker that the coordinator of the projects behind this skill kept for its batches, with the owner's request that every change update it at once. The prices and limits it uses are in the provider references, checked on the dates in [sources](sources.md).
