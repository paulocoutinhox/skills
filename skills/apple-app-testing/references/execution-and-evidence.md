# Execution, artifacts, accessibility and performance

Read this when you run an existing suite, collect evidence, diagnose a failure or define app-project CI. This package gives the procedure, not a framework that runs tests.

## Freeze a reproducible run identity

Write down the revision, artifact hashes, bundle IDs, app version/build, configuration, entitlements that affect behavior, the selected scheme/plan and its enabled test targets. Include dependencies, Xcode/macOS build, simulator/device runtime, architecture, model and input/settings profile. For Watch companion tests, record both ends. For visionOS, record native versus compatible app mode and the spatial presentation.

Pick the subset the changed contract calls for, then the affected regression paths. Keep logic, integration, supported UI automation and manual/hardware acceptance separate. A passing shared Swift package test is evidence for that package on the destination where it ran, not for all of the product's windows and devices.

Keep fixtures and output paths unique to each worker. Parallel tests must not share changeable accounts, the same document, one simulator or one writable result path. Running one suite in series can be right for a shared resource you cannot avoid, but it should not hide unknown global-state dependencies across the project.

## Build and test products are different states

Use `xcodebuild test` for one local build and run, or a deliberate build-for-testing and test-without-building workflow. The second form needs matching app/test products, `.xctestrun`, resources, SDK/platform and architecture. Check test discovery and enabled tests before you read meaning into the exit status.

Do not count an archive action, successful signing, accepted upload or finished provider allocation as a test that ran. An unavailable destination, runner installation failure or entitlement mismatch can stop the suite before any business assertion runs.

Swift Testing fits current unit/component work, while XCTest is still the UI/performance surface Apple describes. Frameworks and provider parsers each support different contracts. Do not assume a provider that accepts XCTest ZIPs will find every Swift Testing suite or another platform's runner on its own.

## Watch the real process and UI

Confirm the package, window/scene, account and current state before you act. On supported XCUIAutomation destinations, check the accessible query and wait for the action's real precondition. On native visionOS, use supported simulator/device interaction and clear manual acceptance, without inventing a UI-test target.

For async effects, use time-limited condition waits, a real response indicator and approved saved-state evidence as fits. Do not add sleeps until the timing happens to work. Keep the first failure before any diagnostic rerun.

Use real device/app screenshots and video, not generated mockups. Include the keyboard, focused item, error, active window or spatial mode when they matter. Keep a plain, unmarked capture next to any marked-up version, and keep the original proportions. A flattened spatial video does not prove two-eye depth or physical comfort.

## Inspect modern result bundles

Open the `.xcresult` in Xcode for tests, failures, logs, coverage and available media. Use the selected installation's current `xcresulttool` help for structured inspection. Examples checked against local Xcode 27.2 help are:

```text
xcrun xcresulttool get test-results summary --path artifacts/ios-smoke.xcresult
xcrun xcresulttool get test-results tests --path artifacts/ios-smoke.xcresult
xcrun xcresulttool export attachments --path artifacts/ios-smoke.xcresult --output-path artifacts/failed-attachments --only-failures
```

Put in a real result bundle and a fresh output path. `summary` reports the destinations and failures, `tests` lists every test with its result, and `export attachments` writes the files plus a `manifest.json` that maps them to tests. These are documented examples, not evidence that an app suite ran while the skill was written. Use the current result-report commands. Do not add code that supports the deprecated object-graph or old JSON formats.

Check what really ran for each destination, configuration and attempt. Passed, failed, expected failure, skipped and mixed outcomes are different. Keep excluded targets and runs with zero cases visible. A green total that includes skipped cases cannot back claims about those cases.

Attach short logs around the failed event and the matching crash/hang details. Use the artifact's matching dSYMs for symbolication. Do not collect whole simulator folders, full private documents or account databases when a smaller relevant artifact explains the failure. Check screenshots, payloads and logs for credentials or customer data before you share them.

## Accessibility and visual evidence

Accessibility Inspector audits the chosen screen and shows platform-specific checks. Run the right checks on loading/error/content variants and read the context it reports. Combine them with real VoiceOver, keyboard/focus and other supported assistive-technology journeys. A clean audit does not certify full accessibility.

For screenshot comparisons, fix the runtime, device/window, scale, language/region, font, appearance and fixture. Tell expected rendering differences apart from missing or overlapping content. Treat a changed reference image as a product decision. Do not widen thresholds or accept all new images just to remove failures.

Mac pointer/focus behavior, Apple TV remote movement, Watch entry and Vision Pro gaze/pinch each need the right interaction evidence. An element you can see in a capture may be unreachable, unlabeled or behind another active surface.

## Performance and diagnostics

Use a separate performance plan based on what the user sees: launch, scrolling/frame behavior, memory growth, export time or another real workload. Apple's guidance says to collect realistic metrics with release-like tests, no debugger and no coverage/sanitizers. Keep diagnostic sanitizer runs as separate evidence.

Measure under matching device/build/fixture/compilation conditions, repeat the workload and state the baseline/tolerance. A debug simulator on a busy Mac cannot show real Watch battery use, phone thermal behavior, Apple TV rendering or Vision Pro comfort/frame delivery.

Use Instruments or the right Xcode diagnostic to explain a regression instead of claiming one from a single elapsed time. Thread, memory, actor or sanitizer findings need the matching run/configuration. A clean run does not prove there is no race or leak anywhere. Never turn off distribution security features just to make a performance or UI job start.

## App-project CI and cleanup

Define fast component checks, a limited supported UI smoke set and broader/hardware coverage only where you can justify it. Choose a specific macOS image/Xcode/runtime, shared scheme and plan. Keep the real command exit status, publish allowed failure artifacts and stop skipped required runs from counting as success.

A macOS UI job needs its real graphical-session/permission model. A build agent is not a remote accessory lab. Do not assume an SSH shell, VM image or a provider's “macOS” label gives you usable UI access, an attached Watch/TV/headset or a supported simulator runtime.

Use approved workload identity or secrets, and keep privileged accounts away from untrusted changes. Write down cloud run/session IDs before you wait. After an interruption, query/cancel the known session instead of blindly submitting another paid run.

Stop only devices/reservations you own, close temporary documents, remove only your own fixture data and restore settings/mappings you changed on purpose. Track kept cloud artifacts and temporary credentials separately from device reset. Do not delete a shared project or wipe a user's Mac/Keychain as test cleanup.

This collection has no CI implementation or helper script. If the user separately asks for automation glue, write Python with uv and declared dependencies. Native Swift test source, Xcode actions and direct vendor commands stay in their proper app/tool places.

## Report an actionable result

Give the exact build/platform/configuration, preconditions, shortest steps, expected/actual result, how often it happened, impact/severity, a separate priority and cleaned evidence. Give each case one status:

| Status | Evidence needed | Consequence |
| --- | --- | --- |
| Passed | The case ran and its UI and saved-state assertions succeeded | Supports only the tested destination, input method and behavior |
| Failed | A difference from the agreed contract that you can reproduce | Report trigger, impact, evidence and affected paths |
| Expected failure | XCTest recorded a known issue that the suite clearly expects | Keep it visible and out of the passed count |
| Unsupported | The platform or tool cannot run this method, such as XCUIAutomation on a native visionOS app | Name the limit and the manual or other evidence used instead |
| Blocked | Missing account, device, pairing, runtime or fixture | Name the exact dependency and finish independent preparation |
| Infrastructure error | Toolchain, destination, signing, runner installation or provider failure stopped a real run | Diagnose that stage without calling the product broken |
| Skipped/not run | Left out on purpose, skipped by the suite or never reached | Keep it out of the passed total and explain why |
| Flaky/inconclusive | Different outcomes with no known cause | Keep every attempt and investigate without rewriting the first failure |

Retest a requested fix and the affected paths around it. Report all attempts without rewriting the first failure as a pass. Explain which simulator, device and service requirements are still needed for the requested coverage. Use [the report template](../assets/test-report.md) and [source notes](sources.md).
