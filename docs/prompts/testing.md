# Testing prompts

Testing for web, Android and Apple apps, and the machines and batches they run on. Read [how to use the prompts](../task-prompts.md) before
you copy one.

## Web testing

```text
Use web-app-testing from paulocoutinhox/skills.
Read [SKILLS_ROOT]/web-app-testing/SKILL.md and name the path really loaded. If it is missing, say so.

Test [WEB_APP] at [AUTHORIZED_LOCAL_OR_STAGING_URLS] for [JOURNEYS_BROWSERS_AND_ROLES].
Start/build commands, fixtures, and limits: [CONTEXT]. Cloud scope/budget: [AUTHORIZATION_OR_NONE].
Use local Playwright and the test suites and tools already in place. Cover forms, keyboard and
focus, navigation, errors, responsive behavior, and tenant separation where it applies. For the
requested remote coverage, pick an AWS, Azure or Google service that is really current. Keep
managed browsers, CI containers, monitoring, and real device coverage apart. Use Python/uv for any
new scripts that are asked for, and add no test runner nobody asked for.
Run only within scope, keep evidence for each case, close the sessions you opened, and report
failures, blocked or planned coverage, and real limits. Do not use retired services or claim runs
that did not happen.
Keep saved browser login state in a path that is clearly ignored and out of shared files.
```

## Android testing

```text
Use android-app-testing from paulocoutinhox/skills.
First read [SKILLS_ROOT]/android-app-testing/SKILL.md and the matching host, device and lab references.
Briefly list the skill path you found. If it is missing, say so.

Test [APP_OR_REPOSITORY] from [WINDOWS_MACOS_OR_LINUX].
Build/install inputs, supported Android versions, and key user journeys: [CONTEXT].
Test accounts and test-data setup that gives the same result every time: [NON_SECRET_DETAILS].
Available local devices and allowed cloud provider/budget: [RESOURCES_OR_NONE].

Look at the app and choose a set of emulators and physical devices, with a reason for each. Cover
forms, input checks, keyboard and focus, navigation, permissions, accessibility, rotation and
resizing, lifecycle and restore, network failures, and purchase or deep-link flows where they
apply. Run the allowed checks you can with the native tools and test frameworks already in place.
Before any cloud run, explain what build files and frameworks it needs. Do not claim that every
provider offers the same devices or services.
Deliver evidence, failures that can be reproduced, coverage, and a clear split between cases run,
planned, and blocked. Do not create test runners nobody asked for, or upload private builds without
permission.
If you test a release AAB, read references/release-bundle-testing.md. Build and install the exact
APK set made from the bundle, record where the signing came from, keep writable device data
separate, and do not treat a billing-account limit as a successful purchase.
```

## Apple testing

```text
Use apple-app-testing from paulocoutinhox/skills.
First read [SKILLS_ROOT]/apple-app-testing/SKILL.md and the matching platform, tool and lab references.
Briefly list the skill path you found. If it is missing, say so.

Test [APP_OR_REPOSITORY] on macOS for [IOS_IPADOS_TVOS_MACOS_VISIONOS_WATCHOS_SELECTION].
Project/schemes, Xcode/toolchain, supported OS versions, and key journeys: [CONTEXT].
Test-data setup, available hardware, and allowed cloud resources/budget: [NON_SECRET_DETAILS].

Look at the real destinations. Choose a set of simulators, native Macs, and physical devices, with
a reason for each. Cover forms, keyboard and focus, remote, Crown or spatial input where it applies,
navigation, accessibility, permissions, resizing and lifecycle, restore, and the purchase flows that
matter. Use supported test frameworks and name the automation limits of each platform. Keep native
macOS, Catalyst, compatible iOS apps, and native spatial apps apart. Check which devices and build
files the cloud service really supports.
Run the allowed checks you can. Deliver evidence that can be reproduced, coverage, and blocked or
planned cases. Do not present simulator checks as hardware proof, make up automation that is not
supported, create test runners nobody asked for, or upload private build files without permission.
For engine and native SDK boundaries or multiple displays, read
references/native-ui-and-multidisplay.md. Check the active app or sheet, the native assertions that
really ran, the listed displays and postures, and real screen captures. Being able to reach a
control is not the same as a finished purchase.
```

## Cloud batch

```text
Use cloud-batch from paulocoutinhox/skills.
First read [SKILLS_ROOT]/cloud-batch/SKILL.md, then the interview, controller setup and safety
references, the tracker procedure if a tracker is wanted, and the reference of each provider,
service and platform the plan uses, such as Xcode Cloud, Device Farm or Google Device Run.
Briefly list the skill path you found. If it is missing, say so.

Plan and run builds and tests for [REPOSITORY] on [PLATFORMS].
Existing CI and Apple services: [CI_XCODE_CLOUD_OR_NONE].
Own machines and devices that may be used: [MACHINES_AND_DEVICES_BY_ROLE].
Cloud accounts, regions and known quotas: [ACCOUNTS_OR_NONE].
Monthly limit and hard rules: [BUDGET_AND_RULES]. Tracker: [YES_WITH_PATH_OR_NO].

Ask only the interview questions that the repository does not answer. Check the controller's tools
and sign-ins with read-only commands and stop until they pass. Write the plan with the machine for
each check, the device matrix, the batch schedule, caches, credentials by name only, the cost per
batch and per month, quota requests and cleanup checks. Write any scripts in Python run with uv.
Before each launch, show the estimate and the month's spend, and wait for a go above the daily
allowance. Run each check on its own platform from a fresh tree, keep every step's real status,
delete every resource the session created and prove it with a listing. If there is a tracker,
update it with its status emojis right after every change of state, before each report.
Do not create budgets, buckets, secrets or quota requests, or rent a cloud Mac, without an explicit
go. Never use a phone of daily use. Deliver the plan, the per-job results with log paths, the cost, the cache
hit rate and the deletion proof, and say which checks were not run.
```
