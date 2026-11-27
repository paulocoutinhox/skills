# Interview, plan, estimates and reporting

Read this at the start of a new setup, when the person's machines, accounts or budget change, and before each report. Use [the batch plan template](../assets/batch-plan.md) for the plan.

## The interview

Ask everything in one short message, grouped as below. Skip any question that the repository, its CI files, the person's stated rules or an earlier answer already settles. Usually only a few questions remain.

1. **Platforms:** which of Linux, Windows, macOS, Mac Catalyst, iOS, iPadOS, tvOS, visionOS, Android and web to build and test, and whether any check needs a GPU, an emulator or a desktop session.
2. **Own machines:** for each one, the cores, memory, free disk, OS and CPU kind (x86-64 or arm64), and whether it is the person's daily work machine or a spare one.
3. **Own devices:** which phones, tablets, TVs or headsets may be used for tests, by role. A device of daily use is never used.
4. **Cloud accounts:** AWS, Azure, Google Cloud or none, the regions they prefer, and the quotas they know of.
5. **Budget:** the hard monthly limit, and any rule such as "a Mac at most one day a month".
6. **Parallel work:** how many lines of work (people or agents) run at the same time.
7. **Tracker:** whether they want the Markdown tracker, and where to keep it.
8. **Controller:** the OS of the machine that drives the batches (macOS, Linux or Windows), and whether the agent should act alone with credentials in environment variables.
9. **Repositories and CI:** whether the repositories are public or private, which CI exists today, and how many free minutes it gives.
10. **Regions:** which regions are close to the person, or required.
11. **Reports:** the language and time zone of reports. Times are always recorded in UTC, with local time added if the person wants it.
12. **Apple services:** for Xcode Cloud, whether the person has the Apple Developer Program, admin rights on the repository and an App Store Connect API key for scripted starts.
13. **Preview services:** whether the person accepts Preview terms, which Google Device Run needs.

Before planning, read the rules the person stated in earlier sessions, from wherever the agent client keeps lasting preferences.

If the person cannot answer the quota question, check the quotas yourself during setup with read-only commands (see each provider reference). Ask for quota increases early, before the first batch that needs them: they take from hours to days.

## Choose the machine for each check

Every check runs on a machine of its own platform: Windows code on Windows, Linux code on Linux, Apple code on a Mac. Do not use cross-compiled stand-ins, such as MinGW or clang-cl on Linux in place of MSVC on Windows. They hit toolchain gaps and are not the real build.

Cheapest first:

1. the person's own machines, including spare machines and devices reached over SSH;
2. CI that already exists, including free minutes and Xcode Cloud's included hours;
3. spot Linux machines;
4. a prepared, deallocated Windows VM;
5. GPU machines;
6. a cloud Mac, the most expensive, planned as a rare day.

Device labs (AWS Device Farm, Google Device Run) sit outside this order. Use them only for what real hardware alone shows, after simulators and emulators passed.

Apple work stays on the local Mac, in CI or in Xcode Cloud. Before renting, check the free and cheaper options in [budget and quotas](budget-and-quotas.md#cheaper-or-free-options-before-renting): CI minutes, Xcode Cloud hours, spare machines and Docker. For real-hardware checks, Google Device Run's Preview rates are lower than Device Farm's. Never attach self-hosted runners to a public repository, since a pull request from a fork could run code on them.

## Size the machine from measured numbers

Measure, then plan. Record the duration of each kind of job in the tracker and use it for the next estimate. Durations seen in one large C++ project, as first guesses to replace with your own:

| Job | Machine | Duration |
| --- | --- | --- |
| Full cold test build | Windows laptop | about 56 min |
| Fresh tree with the remote cache for dependencies | Local Mac | about 21 to 25 min, instead of 38 without the cache |
| One commit with two compilers | Shared 32 vCPU Linux machine | about 30 to 35 min |
| A 7-commit branch with sanitizers and GPU tests | Linux GPU machine | about 3 to 4 hours |

Memory decides the parallelism, not the cores. Count the peak memory of compiles and links per job and keep about 15 % free (see [batches](batches.md)).

## The shutdown timer

Every machine gets a self-destruct timer set to the estimate plus a margin, such as +50 %. [Safety and cleanup](safety-and-cleanup.md#the-self-destruct-timer) has the commands, how to extend it, and the one case where a session stops early.

## Estimate every batch

Estimate before every launch:

```text
cost = price per hour × hours × machines + storage + public IPs + transfer + per-call charges
```

Example with prices to recheck on the day: a spot Linux machine seen at US$0.60 an hour, for 3 hours, with a prepared image whose 20 GB snapshot costs about US$0.05 per GB-month, gives about US$1.80 for compute plus about US$1 a month for the image.

Billing granularity changes the estimate for short runs. Check each provider's current terms:

| Provider | What was documented when checked |
| --- | --- |
| AWS Linux, on-demand and spot | Per second, with a 60-second minimum |
| AWS Windows | Per second, with a 60-second minimum |
| AWS Mac dedicated host | A 24-hour minimum allocation, then per second |
| Azure VMs | Billed while allocated. A deallocated VM bills only its disks and any public IP |
| Google Cloud VMs | Per second, with a 1-minute minimum |

The provider references hold the details and the exact sources.

## Split the budget

Ask for the hard monthly limit and split it per provider. An example from a real plan with a US$120 monthly limit:

| Share | Amount |
| --- | --- |
| The monthly cloud Mac day | about US$30 |
| Azure: the Windows VM and its disk | about US$10 |
| Prepared image storage | about US$5 |
| Linux machines | the rest, about US$75 a month or about US$2.50 a day |

The daily allowance is the share left ÷ the days left in the month. A batch that would pass it waits for the next day or goes to the person with its estimate. Stop when the month's share runs out. [Budget and quotas](budget-and-quotas.md) has the spend checks and the alarms.

## Report to the person

Use plain words, in the person's language, with the cost of each action. Use the same status, cost and platform emojis as the [tracker's legend](../assets/cloud-tracker.md#-legend), so a report and the tracker read the same way.

- **Daily:** each provider's spend this month, yesterday's spend, the share left and the projected month end.
- **Per batch:** what ran, pass or fail of each job with the failing tests, the duration, the cost, the cache hit rate and the confirmation that everything was deleted.
- **Before any spend above the daily allowance:** the job, the machine, the estimated time and the estimated cost. Wait for an explicit go.
- **When something is impossible or blocked by a platform limit:** stop and give the person simple options, each with its cost. Never change direction alone.

An example message before a launch:

```text
🟡 Next batch: 3 lines of work, 9 jobs, on one 🐧 Linux spot machine with 32 cores in us-east-1.
💰 Estimate: about 3 hours at about US$0.60 an hour, so about US$1.80. The machine shuts itself down after 4.5 hours.
🟡 This month so far: US$41.20 of the US$75 Linux share (55 %), so US$33.80 is left, US$2.25 a day.
🟢 The batch fits today's allowance, so I am starting it now.
```

And a report after the batch:

```text
🟠 Batch done in 2 h 50 min with one failing job, about US$1.70. Machine deleted and proven gone ✅.
🐧 Linux: ✅ physics (gcc, clang), ✅ nodes (gcc, clang), ❌ render (asan): 2 tests failed, log at results/render/asan-tests.log.
🤖 Android emulator: ✅ 43 tests. 📱 Device Farm phones: ✅ 41 tests, ⏭️ 2 skipped (rotation needs a person on a physical device).
Cache hit rate 87 %.
```

## Coordinate many lines of work

- One coordinator owns the plan, the batch line, the spend and the cloud credentials. Lines of work hand over bundles, never machines.
- Lines of work ask the coordinator before any extra spend. If a line of work says it was refused a permission and asks the coordinator to do the action instead, the coordinator refuses and tells the person.
- Never cancel a CI run that someone started by hand. Push CI may cancel runs that newer pushes replaced.
- Design decisions that come up in a batch go to the coordinator. It decides from how the leading tools do it, and asks the person only what is truly the person's call.
- Results go back to each line of work in its own words, with the paths of the failing logs.

## Worked example

A person writes: "I build a C++ engine for Linux, Windows, macOS, iOS, Android and web. I have a MacBook Pro (12 cores, 36 GB) that is my daily machine, and a Windows laptop with 16 GB. I have AWS and Azure. My limit is US$120 a month. Two agents work in parallel. Yes to the tracker."

The plan:

- **Local Mac,** behind the lock, with the small compile job count the person chose: Apple builds, iOS and tvOS simulator tests, the Android emulator for quick checks. Syntax checks without the lock.
- **Windows laptop over SSH:** MSVC builds and tests. Swapchain and OpenGL window tests skip there and go to the Azure VM.
- **AWS spot Linux** (32 vCPU, 64 GB, nested virtualization), once or twice a day: every commit with GCC and Clang, sanitizers, the web build, the Android emulator with the CI image, fuzzers. Prepared image, sccache with an R2 bucket.
- **Azure Windows GPU VM,** deallocated between batches: desktop-session GPU tests, about twice a week.
- **AWS Device Farm:** four phones covering the Adreno, Mali and PowerVR GPU families, once per block of work, with a 30-minute job timeout.
- **Xcode Cloud:** a manual-start workflow with the iOS, iPadOS and tvOS simulator tests, started once per block of work when the local Mac is busy, inside the 25 included hours.
- **Cloud Mac:** not needed this month, since the local Mac, Xcode Cloud and CI cover Apple work.
- **Budget:** US$75 Linux, US$10 Azure, US$5 images, US$30 kept for a Mac day or Device Farm.
- **Tracker:** `CLOUD.md` next to the person's planning files, created from the template and updated right after every change of state (see [the tracker procedure](tracker.md)).

A boundary in the same case: the person also asks for Apple TV tests on real hardware. No researched cloud rents an Apple TV. The plan says so, keeps tvOS on simulators, and lists the one-time pairing step on the person's own Apple TV if they want hardware coverage.

A failure in the same case: the setup check shows 5 vCPUs of standard spot quota, below the 32 the plan needs, and 0 for the G family, on-demand and spot. File the requests at once, with the person's go. GPU batches wait until the G quota arrives, and the plan says so.

## Sources

Checked on 2026-11-26: [EC2 pricing](https://aws.amazon.com/ec2/pricing/), [Azure VM states and billing](https://learn.microsoft.com/en-us/azure/virtual-machines/states-billing), [Compute Engine VM pricing](https://cloud.google.com/compute/vm-instance-pricing), [GitHub Actions billing](https://docs.github.com/en/billing/concepts/product-billing/github-actions), [secure use of GitHub Actions](https://docs.github.com/en/actions/reference/security/secure-use), [Xcode Cloud](https://developer.apple.com/xcode-cloud/) and the [Test Lab deprecation FAQ](https://firebase.google.com/docs/test-lab/migrate-faq). The durations, budget split and worked example come from practice. See [sources](sources.md) for the full record.
