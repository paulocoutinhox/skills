---
name: cloud-batch
description: Plan and run builds and tests on the right machines, fast and within a budget, across the person's own machines, CI, Xcode Cloud, AWS, Azure, Google Cloud, AWS Device Farm and Google Device Run, with simulators, emulators and real devices for Android, iOS, iPadOS, tvOS, visionOS, macOS, Mac Catalyst, Windows, Linux GPUs and browsers. Use to choose machines, group work from several people or agents into shared batches, set up caches and credentials, estimate and track spend, run batches with honest results, delete every cloud resource and prove it, and keep an optional Markdown tracker.
license: MIT
---

# Cloud Batch

Run every build and test on a machine of its own platform, in shared batches, at the lowest cost that still gives real evidence. Most rules here came from real problems in long multi-platform projects, so each rule keeps its reason, which helps with edge cases. The parts that come from the docs only are marked.

This skill is descriptive. It explains how to plan, which native commands to use, and how to write the person's launch, batch, sync and cleanup scripts. It bundles no runnable helper. Scripts written for the person use Python run with uv, so the same scripts work on macOS, Linux and Windows controllers. Commands that must run in a shell, such as Xcode Cloud's `ci_scripts`, stay short native commands.

Terms used throughout:

- A **line of work** is one person or agent working on one task.
- The **coordinator** is the one person or agent who owns the plan, the batches, the spend and the cloud credentials.
- The **controller** is the machine the coordinator drives batches from, usually the person's own computer.
- The **batch line** is the coordinator's regular run of shared batches, once or twice a day.
- A **gate** is a check that must pass before work lands.
- A **block of work** is a set of related changes that land together, such as a feature.
- **The lock** is the single build slot of the person's daily machine (see [local machines](references/local-machines.md)).

This skill decides where and how builds and tests run, what they cost, and how the machines are cleaned up. It is not for:

- deciding which test cases to write, which belongs to test design;
- store release, TestFlight distribution or publishing;
- production deployment or long-running servers;
- a single quick check that the local machine can run in minutes, which needs no batch.

## What the person decides

The person decides spending beyond the plan, credentials, account resources (budgets, buckets, secrets, quotas, service accounts), renting a cloud Mac, anything that cannot be undone and how to respond to real platform limits. For those, give simple options, each with its cost.

Within an agreed plan, the agent does the rest alone: launch, run, collect, report and delete. It also decides technical defaults by following how the leading tools do it, such as the machine size, the zone, the order of steps or the fix of a script bug, and states its choice.

Never create secrets, buckets, tokens, budgets or accounts before the person says to. Secrets were once created in the wrong project because nobody waited for that go. Each project has its own credentials and buckets and never shares them.

## Workflow

1. **Interview.** Read the person's stated rules, then ask the open questions of [the interview](references/interview-and-plan.md#the-interview) in one message: platforms, own machines and devices, cloud accounts and quotas, budget and hard limits, lines of work in parallel, tracker, controller OS, public or private repositories and CI minutes, regions, report language and time zone, Apple services for Xcode Cloud, and Preview terms for Google Device Run.
2. **Check the controller.** Install the tools and check every credential with read-only commands, following [the controller setup](references/controller-setup.md). Stop until every check passes. No batch starts with an unchecked credential.
3. **Plan.** Fill [the batch plan](assets/batch-plan.md): which machine runs what, the device matrix, the batch schedule, the caches, the credentials, the cost per batch and per month, the quota requests and the cleanup checks. If the person wants the tracker, create it now from [the template](assets/cloud-tracker.md), so every later event lands in it.
4. **Write the scripts.** Launch, batch runner, sync and delete scripts for the chosen providers, following [batches](references/batches.md), [safety and cleanup](references/safety-and-cleanup.md) and the provider reference.
5. **Prepare before renting.** Build bundles and dry-run them locally. A paid machine never waits while someone writes a script.
6. **Estimate and check the budget.** Price per hour × hours × machines, plus storage, public IPs, transfer and per-call charges. Check the month's spend. Above the daily allowance, send the estimate and wait for a go.
7. **Run.** Launch with a self-destruct timer, run all jobs in parallel where memory allows, and sync results every minute.
8. **Collect and report.** Read the logs, not only the summary. Send each line of work its own findings.
9. **Delete and prove.** Delete everything the session created, then list by tag and fail if anything is left.
10. **Track.** Keep the tracker, created at step 3, titled `# ☁️ Cloud Tracker` with every section title as the template writes it (each word capitalized), the 📊 Overview right under the title and the 📋 Rules and 🚦 Legend at the end, and follow [the tracker procedure](references/tracker.md). Every change of state (a launch, a timer extension, an attach, a run or build that starts or ends, a spend check, a quota answer, a deletion, a leftover) updates the file right after the action, before the report and before the next action. Start every row of a table with a Status column with its status emoji from the legend (🟢 good, 🟡 waiting, 🟠 attention, 🔴 problem, ⚪ idle, 🔵 planned), mark each service's cost by how much of its share is spent, and keep one section per service and one row per platform. Never write sensitive data in the tracker: no credentials, IPs, host names, signed URLs, device serials, personal data, account ids or private paths.

## Right machine for each check

Windows code builds on Windows, Linux on Linux, Apple code on a Mac. No cross-compiled stand-ins, such as MinGW or clang-cl on Linux in place of MSVC, because they hit toolchain gaps and are not the real build.

Cheapest first: the person's own machines, existing CI and Xcode Cloud's included hours, spot Linux, a prepared deallocated Windows VM, GPU machines, and a cloud Mac last. Device labs are only for what real hardware alone shows. Apple work stays on the local Mac, in CI or in Xcode Cloud. A cloud Mac is a rare, planned day, because its host bills at least 24 hours. Consider free options first: CI minutes, Xcode Cloud hours, spare machines and Docker. [Interview and plan](references/interview-and-plan.md) has the full order, sizing, estimates and a worked example.

## Batches, never one task per machine

Never rent a machine for one check. Gather everything that needs that kind of machine and run it in one session: every commit alone and the head, both compilers, sanitizers, GPU tests, web and Android builds, fuzzers and benchmarks. Startup overhead is minutes per launch, so one large shared machine beats several small ones.

Lines of work never rent machines. Each one leaves a bundle folder (a git bundle, a `run.py` with every step and [a README](assets/bundle-readme.md) with the exact command), and one coordinator runs the shared batch line once or twice a day. Lines of work keep working while a batch runs.

The rules that keep batch results true:

- **Fresh trees.** Each commit builds in a fresh worktree, clone or archive, in a build folder only that commit used. An `rsync -a` onto an old build folder keeps old timestamps, Ninja rebuilds nothing, and the gate passes on old objects.
- **Absolute bundle paths.** `git -C repo fetch <relative path>` resolves the path inside `repo` and fails. It cost one line of work a whole batch.
- **Honest exit status.** The runner exits non-zero when any step failed. A script that ended with `echo` or `grep` reported failures as PASS twice.
- **Every error in one run.** Keep going after a failed step and build with `ninja -k 0`, so one paid run reports everything.
- **Memory decides parallelism.** Too many compile jobs, or sanitizer links in parallel, ran machines out of memory. Size a link pool from measured peaks.
- **Sync every minute.** A spot machine was reclaimed after 67 minutes, and every unsynced result was lost.
- **No early delete.** A launching batch deleted its machine while four attached runs still used it. Wait until no runner is left, or launch with a keep option and let the coordinator delete.
- **Strict tests.** Never loosen a test, change its workload, retry it until it passes or skip it to get a pass. Fix the root cause, and prove a flaky test's cause under load.

[Batches](references/batches.md) has the runner example, link pools, attaching work, flaky tests, benchmarks and watching a batch. [CI and caches](references/ci-and-cache.md) covers keeping CI small and the remote compiler cache.

## Safety, credentials and cleanup

These rules are not negotiable:

- Keys live where they normally live: environment variables in the shell profile (`~/.zshrc`, `~/.bashrc`, or the user environment variables on Windows), SSH keys in `~/.ssh`, and the standard `gcloud auth login` and `az login`. They go nowhere else: no script, log, repository, image, tracker, memory or chat message. The agent loads the profile inside each command, because an agent's shell snapshot can hold stale keys. That happened and gave expired credentials.
- Login is by SSH key. AWS sessions use a fresh key pair (ed25519 for Linux, RSA for Windows), saved in `~/.ssh` under the session's name and deleted with the session. A password is a last resort for a machine that cannot take a key, and it never goes on a command line. The one exception is the random, single-use admin password that `az vm create` takes, which the setup replaces at once.
- The firewall opens SSH only from the caller's current address as a `/32`, and the rule goes when the batch ends.
- Every resource carries one tag or label, such as `<project>-batch=<session>`. Listings and deletions use that tag, and nothing else is touched.
- Every rented machine has a self-destruct timer sized to the batch with a margin. A cloud Mac host is the one exception: its planned release goes in the tracker, and the release is proven.
- Every session ends with a deletion and a listing that proves nothing is left. The cleanup script exits non-zero if anything remains.
- When the AWS CLI uses keys from the environment, `unset AWS_PROFILE`, because an empty value fails with "The config profile () could not be found".
- Never weaken a machine's security to make a batch faster, such as by turning off Defender.

[Safety and cleanup](references/safety-and-cleanup.md) has the details and a cleanup-proof example. [Controller setup](references/controller-setup.md) has where variables live, the tools to install on macOS, Linux and Windows, least-privilege roles and the check commands for each provider.

## Budget

Ask for the hard monthly limit, split it per provider, and check the month's spend before every batch. Report the spend each day. Stop when a share runs out. Every batch has an estimate before it starts. Budget alerts only warn, and they arrive late, so the check before every batch is what keeps spend inside the limit. Each AWS Cost Explorer API call costs money, so call it a few times a day at most. Without a monthly limit from the person, plan and estimate, but launch nothing paid. [Budget and quotas](references/budget-and-quotas.md) has the spend commands, hidden costs, alarms, quotas and licensing.

## Providers

| Provider | Reference | Experience behind it |
| --- | --- | --- |
| AWS EC2: spot Linux, GPU Linux and Windows, Mac hosts | [AWS](references/aws.md) | Run in practice, commands rechecked in the docs |
| AWS Device Farm: real phones, emulators, simulators | [Device Farm](references/device-farm.md) | Run in practice, rechecked in the docs |
| Azure: persistent Windows GPU VM, Linux GPU, spot | [Azure](references/azure.md) | Run in practice, rechecked in the docs |
| Google Cloud Compute Engine | [Google Cloud](references/google-cloud.md) | **From the docs only.** Never run in the projects behind this skill |
| Xcode Cloud: Apple builds and simulator tests | [Xcode Cloud](references/xcode-cloud.md) | **From the docs only** |
| GitHub-hosted runners | [CI and caches](references/ci-and-cache.md#github-hosted-runners) | Run in practice, prices rechecked in the docs |
| Google Device Run: Android and iOS devices, Preview | [Google Device Run](references/google-device-run.md) | **From the docs only** |
| The person's own machines | [Local machines](references/local-machines.md) | Run in practice |

## Devices, simulators, emulators and browsers

Every check is automatic: no step asks the person to tap, wake a device or report what they saw. Simulators, emulators and browsers carry the checks. A physical device runs only what they cannot show, such as real sensors, real GPU behavior and signing. Always name the device (`--device <udid>`, `adb -s <serial>`). An agent once ran tests on the person's personal phone because it was the only device connected.

Read [device testing](references/device-testing.md) first, then the platform reference:

- [Apple platforms](references/apple-platforms.md): iOS, iPadOS, tvOS and visionOS simulators, real devices, macOS and Mac Catalyst UI tests.
- [Android emulator](references/android-emulator.md): KVM, headless start, rotation, keyboard, permission dialogs, process death.
- [AWS Device Farm](references/device-farm.md): GPU vendor coverage, self-cleaning runs, custom environments.
- [Google Device Run](references/google-device-run.md): Google's device lab, from the docs only.
- [Xcode Cloud](references/xcode-cloud.md): Apple simulator tests in Apple's CI, with no physical devices.
- [Windows desktop tests](references/windows-desktop.md): autologon, scheduled tasks in the signed-in session, input methods, GPU drivers.
- [Linux GPU and browsers](references/linux-gpu-and-browsers.md): NVIDIA and AMD drivers, Wayland, software rasterizers, headless Chrome.

No researched cloud rents an Apple TV, an Apple Vision Pro or an Apple Watch. Mark that in the plan.

## Other mistakes that really happened

Every incident told in the rules above happened. These did too, and every plan keeps their fixes:

| Mistake | Fix |
| --- | --- |
| The shutdown timer was too short for work added later | Extend it with every attach, and record it |
| The local disk filled up with finished build folders | Delete them, and check 30 GB free before big builds |
| The local lock queue was full of work that could run in the cloud | Keep the lock for work only that machine can do |

## Work that outlives one session

Long work outlives an agent's context. Keep state in files outside the repository, so a new session resumes without redoing work:

- Each line of work keeps a short state file: its commits and their hashes, what passed and where with log paths, what is open and the next step.
- The coordinator keeps one handoff file: the running machines, the pending batches and the spend. The tracker can serve as that file.
- A new session reads these files first, then checks the tracker against the real state with read-only listings before acting (see [the tracker procedure](references/tracker.md#resume-a-session-from-it)).

Record every rule the person states, such as the budget, "a Mac one day a month" or "never touch my phone", where the agent client keeps lasting preferences, and read those rules before planning.

## Errors and partial work

- **Expired or refused credentials** ("ExpiredToken", "AuthorizationFailed", "invalid_grant"): stop the batch, tell the person which variable or sign-in to renew, and never retry in a loop or ask for the secret in the chat.
- **No capacity or no quota:** move to the next zone. Fall back to on-demand only if the new estimate still fits the daily allowance, and otherwise send the new estimate and wait for a go. File a quota request when the person agrees.
- **An interrupted create:** when a launch, an upload or a scheduled run times out or its answer is lost, list by the session tag (or the project's runs) before trying again. The first request may have worked, and a second one would bill twice.
- **A lost machine:** check its state with the provider. Report the finished steps and rerun the rest.
- **A tool or account that is missing:** write the plan, the scripts and the estimates, mark the runs as not done, and name the exact missing tool, sign-in or quota. Never report a run that did not happen.
- **A cleanup listing that is not empty:** retry the deletion of what is left, record it in the tracker's 🧹 Open Cleanup Items, and tell the person until it is gone.
- **A platform limit, such as no rentable Apple TV:** stop and give the person simple options, each with its cost. Never change direction alone.

## Done means

- Each check ran on its own platform, from a fresh tree, with every step's real status.
- The coordinator read the logs and sent each line of work its findings, with log paths.
- Every cloud resource of the session is deleted and a listing proved it, or the open items are in the report.
- The spend, the share left and the cache hit rate are reported.
- The tracker, if used, matches the real state: its `Last updated` time comes after the last action, nothing ended still shows as running, and its Overview agrees with its sections.

Do not claim that a run happened, that a device was used or that something was deleted without the command output that shows it.

## Resources

| Read | When |
| --- | --- |
| [Interview and plan](references/interview-and-plan.md) | Starting a setup: questions, machine order, sizing, estimates, budget split, reports, worked example |
| [Controller setup](references/controller-setup.md) | First run on a controller, or a credential failure: tools, keys, roles and checks per OS and provider |
| [Batches](references/batches.md) | Designing a batch: bundles, dry runs, fresh trees, the step runner, memory, sync, attaching work, flaky tests, benchmarks |
| [Safety and cleanup](references/safety-and-cleanup.md) | Writing launch and delete scripts: SSH access, tags, timers, proof of deletion, hidden costs |
| [Budget and quotas](references/budget-and-quotas.md) | Before every batch and when asking for quotas: spend checks, alerts, billing terms, spot, licensing, free options |
| [CI and caches](references/ci-and-cache.md) | Setting up sccache and keeping CI small |
| [Xcode Cloud](references/xcode-cloud.md) | Apple builds and simulator tests in Apple's own CI, started by hand or through the App Store Connect API |
| [Google Device Run](references/google-device-run.md) | Google's device lab for Android and iOS, in Preview |
| [AWS](references/aws.md), [Azure](references/azure.md), [Google Cloud](references/google-cloud.md) | Using that provider's machines |
| [Local machines](references/local-machines.md) | Using the person's daily machine, a laptop or a spare machine |
| [Device testing](references/device-testing.md) | Before any run on a simulator, emulator, browser or device |
| [Apple platforms](references/apple-platforms.md), [Android emulator](references/android-emulator.md), [Device Farm](references/device-farm.md), [Windows desktop tests](references/windows-desktop.md), [Linux GPU and browsers](references/linux-gpu-and-browsers.md) | The platform the run targets |
| [Tracker](references/tracker.md) | Creating the tracker, and before every change to it: which event changes which section, emojis, cost, example day |
| [Sources](references/sources.md) | Where each fact comes from, its date and the open limits |
| [Batch Plan](assets/batch-plan.md), [Bundle README](assets/bundle-readme.md), [Cloud Tracker](assets/cloud-tracker.md) | Templates to copy and fill |

Prices and limits in the references were checked on the dates in [the sources](references/sources.md). Check them again before a real spend. See the [license](LICENSE.md).
