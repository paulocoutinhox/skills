# Cloud services and their real Apple-platform coverage

Read this before you choose a provider or upload a private artifact. Baseline: **2026-11-05**. For a real run, the current catalog and the selected account's capabilities decide. Only the user asks for maintenance of this stored knowledge.

## Match the service to the question

| Requirement | Checked route | Required evidence |
| --- | --- | --- |
| iPhone/iPad physical compatibility or remote reproduction | AWS Device Farm, Google Device Run for iOS or a documented iOS provider | Real device/OS, accepted artifact, cases that ran and result |
| Native macOS UI/document behavior | Controlled local/remote Mac with a usable graphical session, or a suitable native Mac CI test destination | Native app identity, macOS/architecture, permissions and interaction |
| tvOS/Watch simulator checks | Local Xcode or a selected Mac runner with the real runtime/scheme/test support | Returned destination and cases that really ran |
| Physical Watch/Apple TV behavior | Controlled physical hardware or a provider that clearly documents that device/capability | Real pairing/input/hardware journey |
| Native visionOS spatial acceptance | Apple-silicon simulator host plus a real Vision Pro where needed | Component checks and clear simulator/manual physical evidence |

The reviewed AWS and Google mobile-lab documents describe iOS devices and tests, not a full farm for every Apple platform. Do not turn “iOS support,” “macOS host,” a build enum or an Appium driver capability into a reservation that a provider has not documented.

For every provider, find out the account/project, which binary/source uploads are allowed, synthetic accounts, whether staging is reachable, region/data retention, a fixed device/time/attempt limit and who owns cleanup. A remote device cannot reach the developer's local service through the workstation's loopback address.

## Xcode Cloud

Use Xcode for first onboarding and the repository connection. Check the right product, shared schemes and dependencies before you turn on a workflow. Later workflow/build operations and artifacts are available through Xcode, App Store Connect and its documented Xcode Cloud API resources. Researching this skill does not create those resources or send build notifications.

Select the real Xcode/macOS environment, Test action, scheme, existing test plan and the destinations available for that environment. Mark a required suite Required To Pass. Build, Test, Analyze and Archive actions each have their own purpose. An archive or finished build does not show that a test action ran.

A Test action first builds products with `build-for-testing`, then runs them with `test-without-building`. The second phase does not have the source checkout. Put runtime fixtures in suitable test resources instead of assuming a file next to the source can be read then. Do not assume one action's local artifacts exist in another action's temporary environment.

Check the platform/action combination in the selected environment. The App Store Connect action schema includes several Apple platform/destination values, but the schema accepting a value does not prove every product/runtime/test combination works. Native visionOS UI automation is still limited by XCUIAutomation's clear SDK restriction.

Check outcomes for each action, destination and case. Then download the result bundle, the logs you need and matching symbols before artifact retention runs out. Do not quietly turn on TestFlight distribution, notarization or release post-actions for a QA request. You can set up native test actions without adding custom shell hooks to this descriptive collection.

## AWS Device Farm: physical iOS

### Prepare the correct artifacts

Choose the approved AWS identity and Device Farm project in the researched mobile region, `us-west-2`. Select real available iPhone/iPad devices and a supported iOS test host/software combination. The provider warns that leaving out host selection on older devices can pick legacy infrastructure. Choose the supported host on purpose instead of taking that default.

The app upload is a signed device `.ipa`. XCTest UI needs the matching Runner product and test bundle built to run on a device. Simulator products, unrelated test runners and a ZIP of source alone do not meet that contract.

AWS documents two test-package layouts:

- A runner `.ipa` contains `Payload/YourUITests-Runner.app`. It is not the same artifact as the app under test.
- A test `.zip` can contain the runner `.app` or runner `.ipa` and optional `.xctestrun`/test-plan support. AWS clearly says not to put a `Payload` folder inside this ZIP layout. If you include project/workspace and plans, check the exact requirements of the selected test spec.

Keep app/runner/test dependencies and signing/entitlement expectations consistent. Check any provider re-signing limits against capabilities such as sign-in, Keychain groups or app groups. An artifact the provider changed is not automatically the same as production distribution.

### Submit, inspect and match up results

1. Select an existing project and device pool, or create only the resources that were requested.
2. Create the app upload record with type `IOS_APP`. Send the exact IPA bytes to the returned presigned URL, for example with `curl -T app.ipa "PRESIGNED_URL"`, and keep its upload ARN. Keep the presigned URL out of logs.
3. Read `get-upload` until processing leaves `INITIALIZED`/`PROCESSING`. Continue only after `SUCCEEDED`. On `FAILED`, read its metadata/message and diagnose the package before scheduling.
4. Upload/process the prepared test package as `XCTEST_UI_TEST_PACKAGE` and, for chosen custom execution, the real `XCTEST_UI_TEST_SPEC`.
5. Find the default specification with `list-uploads --arn PROJECT_ARN`, download it through `get-upload` and review its current host and software before you upload the reviewed copy. Do not copy an unreviewed host/Appium recipe or turn off signing errors across the board.
6. Schedule the selected run and save the returned run ARN before you wait.
7. Check `get-run` and the jobs/suites/tests for each device. The `COMPLETED` state is separate from `PASSED`, `WARNED`, `FAILED`, `SKIPPED`, `ERRORED` or `STOPPED` results. A `SKIPPED` result with `resultCode` `PARSING_FAILED` means the package was not parsed and no case ran.
8. Get the `list-artifacts` outputs you need for logs, files and screenshots. Check which tests ran and open the real evidence.

A sample native submission, once all upload ARNs and the pool are real and ready:

```text
aws devicefarm schedule-run --region us-west-2 --project-arn PROJECT_ARN --app-arn APP_UPLOAD_ARN --device-pool-arn POOL_ARN --name ios-profile-regression --test type=XCTEST_UI,testPackageArn=TEST_UPLOAD_ARN,testSpecArn=SPEC_UPLOAD_ARN
```

On a client timeout, check the known run before you submit again. Stop approved unfinished work with `aws devicefarm stop-run --region us-west-2 --arn RUN_ARN`. Devices that already started still finish setup/teardown and you pay for it. Do not read a lost response as proof that no paid work started. Standard non-UI XCTest and UI tests have different package/type contracts. Choose the documented type for an existing suite instead of renaming one into the other.

### Interactive devices

Remote access lets an approved user reproduce a case on a selected iOS device. Install the approved app, capture the interaction you need and stop the remote session when you finish. A managed Appium endpoint can work with an existing compatible client/Inspector, but it does not add support for an unlisted Watch/TV/headset.

Use an uploaded/approved remote artifact, not a local file path, in remote app capabilities. Keep endpoints/presigned URLs private. Device cleanup does not remove backend records or revoke test-account tokens.

## AWS EC2 Mac: a separate infrastructure choice

EC2 Mac gives native Mac infrastructure on Dedicated Hosts. The team must set up the AMI/macOS, Xcode, runtimes, architecture, graphical session, permissions and test-agent isolation. It is useful for a controlled Mac test environment, not a ready-made physical Apple accessory lab.

Select an Apple-silicon host where visionOS development is needed, and confirm the host's supported macOS image. The researched allocation has a minimum **24-hour Dedicated Host period** before release, so a short test session does not always mean a short bill. Stopping the instance is not the same as releasing the host and removing kept storage. Check the real approved lifecycle and costs before allocation.

## Google Cloud Developer Device Platform: iOS XCTest

The researched service is Preview. Its current iOS guide and live CLI reference use **`gcloud alpha device-run`**, while the Android documentation uses a beta surface. Use the checked iOS contract and installed CLI help. Do not swap in Android commands.

The general platform overview says iOS support is coming later, while the dedicated iOS guide,
the release notes and the alpha CLI document iOS XCTest runs. Confirm access against the real
project and returned device catalog before you commit to this route. Documented syntax does not
prove the account has access. If it is not available, report the limit and clearly choose another
approved, supported provider.

Prepare an approved project with billing, required APIs, identity/IAM and access to the artifact bucket. The common quickstart names Device Run, Device Streaming and Cloud Testing setup during Preview. Turn on the surfaces you really need within the approved setup. A caller's permissions and the service's read/write permissions on an existing bucket are separate.

List current iOS devices and supported software versions. Then select real catalog IDs and an Xcode that matches the built suite. Do not treat a catalog example's device availability or default Xcode as a permanent promise.

Build matching device test products. The iOS guide needs the real products folder, such as `Debug-iphoneos`, and the matching `.xctestrun` directly at the root of the ZIP. Do not wrap them inside an extra `build/` or `Products/` folder. Check host-app and UI-runner signatures where they apply. This layout is not the same as AWS's runner packaging.

A sample submission with checked placeholders:

```text
gcloud alpha device-run sessions submit xctest --project=PROJECT_ID --device=IOS_DEVICE_ID --test=ios-tests.zip --xcode-version=XCODE_VERSION --xctest-timeout=10m --flaky-test-attempts=1 --async
gcloud alpha device-run sessions describe SESSION_ID --project=PROJECT_ID --full
```

Ten minutes is a sample timeout within the documented 1m–1h range. `--flaky-test-attempts` is the maximum number of run attempts per test shard, so `1` means no retry. Save the returned session ID, check each job and use the documented wait/cancel lifecycle when needed. A successful submission is not a passing test.

Read the real Cloud Storage paths in the result and get the evidence you need. Choose video/attachment collection on purpose, including any OS and UI-versus-unit limits. Stored artifacts stay after the device is released. Fix the scope and account for how devices, shards and attempts multiply, plus storage and the active plan. A budget alert is not a spending cap.

Do not use Firebase Test Lab. Android Device Streaming does not mean there is an iPhone streaming product.

## Azure Pipelines and other mobile labs

Azure Pipelines can build/test Xcode projects on macOS agents and can submit approved artifacts to another lab. Select a specific image/Xcode from the real software manifest, a matching SDK/runtime and a shared scheme/plan. Use a Test action or an existing `xcodebuild test` command, not an iOS build-only starter task labeled as QA success.

Native Mac UI tests need the real graphical session and permission. tvOS/watchOS simulator tests need real installed runtimes and working destinations. A hosted Mac label does not promise physical Watch/Apple TV/Vision Pro hardware. Use a properly prepared self-hosted Mac or a clearly named outside device service when needed.

Do not use App Center Test. BrowserStack App Live is the interactive product, and App Automate runs its supported suites. Check the selected iOS capability, account, signing and private-network access. A desktop macOS browser product does not show native Mac-app coverage.

Keep real app-project CI setups separate from this descriptive skill. Preparing a test plan is not permission for a new workflow with source/account uploads, paid jobs or release actions. See [execution/evidence](execution-and-evidence.md) and [sources](sources.md).
