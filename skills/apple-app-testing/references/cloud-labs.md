# Cloud services and their real Apple-platform coverage

Read this before choosing a provider or uploading a private artifact. Baseline: **2026-11-05**. A current catalog and the selected account's capabilities govern an actual run. Only the user requests maintenance of this stored knowledge.

## Match the service to the question

| Requirement | Appropriate researched route | Required evidence |
| --- | --- | --- |
| iPhone/iPad physical compatibility or remote reproduction | AWS Device Farm, Google Device Run for iOS or a documented iOS provider | Actual device/OS, accepted artifact, executed cases and result |
| Native macOS UI/document behavior | Controlled local/remote Mac with a usable graphical session, or a suitable native Mac CI test destination | Native app identity, macOS/architecture, permissions and interaction |
| tvOS/Watch simulator checks | Local Xcode or a selected Mac runner with the actual runtime/scheme/test support | Returned destination and cases that actually ran |
| Physical Watch/Apple TV behavior | Controlled physical hardware or a provider explicitly documenting that device/capability | Real pairing/input/hardware journey |
| Native visionOS spatial acceptance | Apple-silicon simulator host plus actual Vision Pro where needed | Component checks and explicit simulator/manual physical evidence |

The reviewed AWS and Google mobile-lab documents describe iOS devices and tests, not a complete farm for every Apple platform. Do not translate “iOS support,” “macOS host,” a build enum or an Appium driver capability into a reservation that a provider has not documented.

For every provider, identify account/project, permitted binary/source uploads, synthetic accounts, staging reachability, region/data retention, finite device/time/attempt scope and who owns cleanup. A remote device cannot reach the developer's local service by assuming the same loopback address as the workstation.

## Xcode Cloud

Use Xcode for the initial onboarding and repository connection. Inspect the correct product, shared schemes and dependencies before enabling a workflow. Later workflow/build operations and artifacts are available through Xcode, App Store Connect and its documented Xcode Cloud API resources. Researching this skill does not create those resources or send build notifications.

Select the actual Xcode/macOS environment, Test action, scheme, existing test plan and destinations available for that environment. Make a required suite Required To Pass. Build, Test, Analyze and Archive actions have separate purposes. An archive or completed build is not evidence that a test action executed.

A Test action first builds products with `build-for-testing`, then runs them with `test-without-building`. The second phase does not have the source checkout available. Put runtime fixtures in appropriate test resources rather than assuming a source-relative file can be read then. Do not assume one action's local artifacts are present in another action's temporary environment.

Verify the platform/action combination in the selected environment. The App Store Connect action schema includes multiple Apple platform/destination values, but schema acceptance is not proof that every product/runtime/test combination works. The release-note page still contains an older visionOS test-action limitation. Do not turn that historical entry into a universal current guarantee in either direction. Native visionOS UI automation remains bounded by XCUIAutomation's explicit SDK restriction.

Inspect per-action, destination and case outcomes, then download the result bundle, relevant logs and matching symbols before artifact retention expires. Do not silently enable TestFlight distribution, notarization or release post-actions for a QA request. Native test actions can be configured without adding custom shell hooks to this descriptive collection.

## AWS Device Farm: physical iOS

### Prepare the correct artifacts

Choose the authorized AWS identity and Device Farm project in the researched mobile region, `us-west-2`. Select actual available iPhone/iPad devices and a supported iOS test host/software combination. The provider warns that omitted host selection on older devices can select legacy infrastructure. Explicitly choose the supported host instead of inheriting that behavior.

The application upload is a signed device `.ipa`. XCTest UI needs the matching Runner product and test bundle built for device execution. Simulator products, unrelated test runners and a ZIP of source alone do not satisfy that contract.

AWS documents two test-package layouts:

- A runner `.ipa` contains `Payload/YourUITests-Runner.app`. It is not the same artifact as the application under test.
- A test `.zip` can contain the runner `.app` or runner `.ipa` and optional `.xctestrun`/test-plan support. AWS explicitly says not to put a `Payload` directory inside this ZIP layout. Inspect the exact selected test-spec requirements if including project/workspace and plans.

Keep app/runner/test dependencies and signing/entitlement expectations coherent. Check any provider re-signing constraints against capabilities such as authentication, Keychain groups or app groups. A provider-modified artifact is not automatically equivalent to production distribution.

### Submit, inspect and reconcile

1. Select an existing project and device pool, or create only the resources requested.
2. Create the app upload record with type `IOS_APP`. PUT the exact IPA bytes to the returned presigned URL and keep its upload ARN.
3. Read `get-upload` until terminal processing. Continue only after `SUCCEEDED`.
4. Upload/process the prepared test package as `XCTEST_UI_TEST_PACKAGE` and, for selected custom execution, the actual `XCTEST_UI_TEST_SPEC`.
5. Review the provider's current custom test specification and supported host. Do not copy a historical host/Appium recipe or disable signing errors indiscriminately.
6. Schedule the selected run and preserve the returned run ARN before waiting.
7. Inspect `get-run` and per-device jobs/suites/tests. The `COMPLETED` state is separate from `PASSED`, `FAILED`, `ERRORED` or other actual results.
8. Retrieve relevant `list-artifacts` outputs for logs, files and screenshots. Verify which tests executed and open the actual evidence.

An illustrative native submission after all upload ARNs and the pool are real and ready:

```text
aws devicefarm schedule-run --region us-west-2 --project-arn PROJECT_ARN --app-arn APP_UPLOAD_ARN --device-pool-arn POOL_ARN --name ios-profile-regression --test type=XCTEST_UI,testPackageArn=TEST_UPLOAD_ARN,testSpecArn=SPEC_UPLOAD_ARN
```

On a client timeout, inspect the known run before submitting again. Do not interpret a lost response as proof that no billable work started. Standard non-UI XCTest and UI tests have different package/type contracts. Choose the documented type for an existing suite rather than renaming one into the other.

### Interactive devices

Remote access lets an authorized user reproduce a case on a selected iOS device. Install the approved app, capture the relevant interaction and stop the enclosing remote session when finished. A managed Appium endpoint can support an existing compatible client/Inspector, but does not create support for an unlisted Watch/TV/headset.

Use an uploaded/approved remote artifact rather than a local filesystem path in remote app capabilities. Keep endpoints/presigned URLs private. Device cleanup does not remove backend records or revoke test-account tokens.

## AWS EC2 Mac: a separate infrastructure choice

EC2 Mac provides native Mac infrastructure on Dedicated Hosts. The team must establish the AMI/macOS, Xcode, runtimes, architecture, graphical session, permissions and test-agent isolation. It is useful for a controlled Mac execution environment, not a ready-made physical Apple accessory lab.

Select an Apple-silicon host where visionOS development is required and confirm the host's supported macOS image. The researched allocation has a minimum **24-hour Dedicated Host period** before release, so a short test session is not necessarily a short bill. Stopping the instance is different from releasing the host and removing retained storage. Inspect the actual approved lifecycle and costs before allocation.

## Google Cloud Developer Device Platform: iOS XCTest

The researched service is Preview. Its current iOS guide and live CLI reference use **`gcloud alpha device-run`**, while Android documentation uses a beta surface. A beta iOS search result did not have a retrievable current reference. Use the inspected iOS contract and installed CLI help rather than substituting Android commands.

The general platform overview still says iOS support is forthcoming, despite the dedicated iOS
guide and alpha CLI. Confirm access against the actual project and returned device catalog before
committing to this route. Documented syntax is not verified account availability. If unavailable,
report the limitation and choose another authorized supported provider explicitly.

Prepare an authorized project with billing, required APIs, identity/IAM and artifact-bucket access. The common quickstart names Device Run, Device Streaming and Cloud Testing setup during Preview. Enable the actual required surfaces within authorized setup. A caller's permissions and the service's read/write permissions on an existing bucket are separate.

List current iOS devices and supported software versions, then select real catalog IDs and an Xcode compatible with the built suite. Do not copy a catalog example's device availability or default Xcode as a permanent guarantee.

Build matching device test products. The iOS guide requires the actual products directory, such as `Debug-iphoneos`, and matching `.xctestrun` directly at the root of the ZIP. Do not wrap them inside an extra `build/` or `Products/` directory. Inspect host-app and UI-runner signatures where applicable. This layout is different from AWS's runner packaging.

An illustrative submission with verified placeholders:

```text
gcloud alpha device-run sessions submit xctest --project=PROJECT_ID --device=IOS_DEVICE_ID --test=ios-tests.zip --xcode-version=XCODE_VERSION --xctest-timeout=10m --flaky-test-attempts=1 --async
gcloud alpha device-run sessions describe SESSION_ID --project=PROJECT_ID --full
```

Ten minutes is an example selected timeout. One flaky-test attempt means one total attempt. Preserve the returned session ID, inspect each job and use the documented wait/cancel lifecycle when needed. Successful submission is not a passing test.

Read the actual Cloud Storage paths in the result and retrieve the required evidence. Select video/attachment collection deliberately, including any OS and UI-versus-unit limitations. Stored artifacts remain after device release. Pin scope and account for device/shard/attempt multiplication, storage and the active plan. A budget alert is not a cap.

Firebase Test Lab is deprecated with announced shutdown on **September 30, 2027**. Do not select it for new runs. Discuss existing XCTest migration only when requested. Device IDs, flags, attempts and package/feature contracts need explicit translation. Android Device Streaming does not imply an iPhone streaming product.

## Azure Pipelines and other mobile labs

Azure Pipelines can build/test Xcode projects on macOS agents and can submit approved artifacts to another lab. Select an explicit image/Xcode from the actual software manifest, compatible SDK/runtime and a shared scheme/plan. Use a Test action or existing `xcodebuild test` invocation, not an iOS build-only starter task labeled as QA success.

Native Mac UI tests need the actual graphical session and authorization. tvOS/watchOS simulator tests need real installed runtimes and working destinations. A hosted Mac label does not promise physical Watch/Apple TV/Vision Pro hardware. Use an appropriately prepared self-hosted Mac or explicit external device service when required.

App Center Test retired on **March 31, 2025**. Extensions for Analytics & Diagnostics do not restore it. Microsoft recommends BrowserStack App Automate as a device-testing migration route. App Live is the interactive product, and App Automate executes its supported suites. Verify selected iOS capability, account, signing and private-network access. A desktop macOS browser product is not evidence of native Mac-app coverage.

Keep actual app-project CI implementations separate from this descriptive skill. Preparing a test plan does not authorize a new workflow with source/account uploads, paid jobs or release actions. See [execution/evidence](execution-and-evidence.md) and [sources](sources.md).
