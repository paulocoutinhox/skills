# Execution, artifacts, accessibility and performance

Read this when running an existing suite, collecting evidence, diagnosing a failure or defining app-project CI. This package provides the procedure, not an execution framework.

## Freeze a reproducible run identity

Record revision, artifact hashes, bundle IDs, app version/build, configuration, entitlements relevant to behavior, selected scheme/plan and its enabled test targets. Include dependencies, Xcode/macOS build, simulator/device runtime, architecture, model and input/settings profile. For Watch companion tests, record both endpoints. For visionOS, record native versus compatible app mode and spatial presentation.

Select the subset justified by the changed contract, then affected regression paths. Separate logic, integration, supported UI automation and manual/hardware acceptance. A passed shared Swift package test is evidence for that package on the executed destination, not for all of the product's windows and devices.

Keep fixtures and output paths unique per worker. Parallel tests must not share mutable accounts, the same document, one simulator or a single writable result path. Serializing one suite can be appropriate for an unavoidable shared resource, but should not hide unknown global-state dependencies throughout the project.

## Build and test products are different states

Use `xcodebuild test` for a coherent local build/run, or an intentional build-for-testing and test-without-building workflow. The second form needs matching app/test products, `.xctestrun`, resources, SDK/platform and architecture. Inspect test discovery and enabled tests before interpreting exit status.

Do not count an archive action, successful signing, accepted upload or completed provider allocation as an executed test. An unavailable destination, runner installation failure or entitlement mismatch can stop the suite before any business assertion ran.

Swift Testing is appropriate for current unit/component work, while XCTest remains the UI/performance surface described by Apple. Frameworks and provider parsers have distinct supported contracts. Do not assume a provider that accepts XCTest ZIPs automatically discovers every Swift Testing suite or a different platform's runner.

## Observe the actual process and UI

Confirm package, window/scene, account and current state before acting. On supported XCUIAutomation destinations, inspect the accessible query and wait for the action's true precondition. On native visionOS, use supported simulator/device interaction and explicit manual acceptance, without inventing a UI-test target.

For asynchronous effects, use bounded condition waits, an actual response indicator and authorized durable evidence as appropriate. Do not add sleeps until timing happens to work. Preserve the first failure before any diagnostic rerun.

Use real device/app screenshots and video, not generated mockups. Include the keyboard, focused item, error, active window or spatial mode when relevant. Keep an unannotated capture alongside any explanatory annotations and retain original proportions. A flattened spatial video does not prove binocular depth or physical comfort.

## Inspect modern result bundles

Open the `.xcresult` in Xcode for tests, failures, logs, coverage and available media. Use the selected installation's current `xcresulttool` help for structured inspection. Examples checked against local Xcode 27.2 help are:

```text
xcrun xcresulttool get test-results summary --path artifacts/ios-smoke.xcresult
xcrun xcresulttool export attachments --path artifacts/ios-smoke.xcresult --output-path artifacts/failed-attachments --only-failures
```

Substitute an actual result bundle and fresh output path. These are documented examples, not evidence that an app suite ran during skill creation. Prefer current result-report commands instead of adding deprecated object-graph or legacy JSON compatibility code.

Inspect what actually executed per destination, configuration and attempt. Passed, failed, expected failure, skipped and mixed outcomes are different. Keep excluded targets and zero-case execution visible. A green aggregate with skipped cases cannot support claims about those cases.

Attach bounded logs around the failed event and matching crash/hang details. Use the artifact's matching dSYMs for symbolication. Avoid collecting entire simulator directories, full private documents or account databases when a smaller relevant artifact explains the failure. Review screenshots, payloads and logs for credentials or customer data before sharing.

## Accessibility and visual evidence

Accessibility Inspector audits the chosen screen and exposes platform-specific checks. Run the relevant checks on loading/error/content variants and inspect reported context. Combine them with real VoiceOver, keyboard/focus and other supported assistive-technology journeys. A clean audit is not complete accessibility certification.

Fix runtime, device/window, scale, language/region, font, appearance and fixture for screenshot comparisons. Separate expected rendering variation from missing or overlapping content. Review changed reference images as a product decision. Do not broaden thresholds or accept all new images merely to remove failures.

Mac pointer/focus behavior, Apple TV remote traversal, Watch entry and Vision Pro gaze/pinch each need the appropriate interaction evidence. An element visible in a capture may be unreachable, unlabeled or behind another active surface.

## Performance and diagnostics

Use a distinct performance plan based on the user-visible requirement: launch, scrolling/frame behavior, memory growth, export time or another actual workload. Apple's guidance calls for release-like tests without a debugger and without coverage/sanitizers when collecting realistic metrics. Keep diagnostic sanitizer runs as separate evidence.

Measure comparable device/build/fixture/compilation conditions, repeat the workload and state the baseline/tolerance. A debug simulator running on a busy Mac cannot establish real Watch battery use, phone thermal behavior, Apple TV rendering or Vision Pro comfort/frame delivery.

Use Instruments or the relevant Xcode diagnostic to explain a regression instead of asserting one from an isolated elapsed time. Thread, memory, actor or sanitizer findings require the relevant execution/configuration and do not prove absence of every race or leak when the run is clean. Never disable distribution security features simply to make a performance or UI job start.

## App-project CI and cleanup

Define fast component checks, a bounded supported UI smoke set and justified broader/hardware coverage. Select a concrete macOS image/Xcode/runtime, shared scheme and plan. Preserve the real command exit status, publish permitted failure artifacts and prevent skipped required execution from becoming success.

A macOS UI job needs its actual graphical-session/permission model. A build agent is not a remote accessory lab. Do not assume an SSH shell, VM image or a provider's “macOS” label establishes usable UI access, attached Watch/TV/headset or a supported simulator runtime.

Use approved workload identity or secrets, and keep privileged accounts away from untrusted changes. Record cloud run/session IDs before waiting. After an interruption, query/cancel the known session rather than blindly submitting another billable run.

Stop only owned devices/reservations, close temporary documents, remove only owned fixture data and restore deliberate settings/mappings. Account for retained cloud artifacts and temporary credentials separately from device reset. Do not delete a shared project or wipe a user's Mac/Keychain as test cleanup.

This collection contains no CI implementation or helper script. If the user separately requests automation glue, write Python with uv and declared dependencies. Native Swift test source, Xcode actions and direct vendor commands remain their proper application/tool surfaces.

## Report an actionable result

Provide exact build/platform/configuration, preconditions, minimal steps, expected/actual result, observed frequency, impact/severity, separate priority and sanitized evidence. Distinguish product failure, test failure, infrastructure error, blocked, unsupported, skipped and flaky/inconclusive work.

Retest a requested fix and surrounding affected paths. Report all attempts without rewriting the first failure as a pass. Explain which simulator, device and service prerequisites remain for the requested coverage. Use [the report template](../assets/test-report.md) and [source notes](sources.md).
