---
name: apple-app-testing
description: Plan, execute and investigate iOS, iPadOS, tvOS, macOS, visionOS and watchOS app tests from macOS. Use for forms, inputs, screens, accessibility, lifecycle and compatibility using Xcode, simulators, physical hardware and researched cloud services, with explicit per-platform automation limits.
license: MIT
---

# Apple App Testing

Verify user outcomes on the correct Apple platform, not just a successful build or replayed gesture. This descriptive skill contains researched procedures, native-tool examples and a report template. It does not bundle test programs, generated flows, cloud runners or automatic updates.

## Establish the actual product and test contract

Inspect project instructions, source revision, existing tests, workspace/project, schemes, test targets/plans, dependencies and supported deployment targets. Identify SwiftUI/UIKit/AppKit, Catalyst, compatible iPad apps, native spatial apps, independent Watch apps and phone companions separately. A shared Swift package does not establish a working UI on every platform.

Collect bundle IDs, build/configuration, entitlements/signing requirements, expected journeys, actual field rules, safe backend/fixtures and test identities. For a binary-only request, identify the artifact's platform, distribution channel and architecture. An arbitrary App Store IPA cannot become a simulator build or supply the original tests.

Ask only for missing facts that affect execution: acceptance criteria, required devices/OS versions, pairing/account access, cloud uploads and finite spending scope. Use synthetic data. App testing does not authorize publishing builds, enrolling devices, exposing private services or purchasing production products.

Record preconditions, input/actions, expected UI and durable effect, cleanup and evidence. Use [the report template](assets/test-report.md). Mark missing-device/tool/account cases as unexecuted rather than inventing results.

## Select the correct execution surface

| Platform | Local route on macOS | Interaction that must be tested | Important boundary |
| --- | --- | --- | --- |
| iOS/iPadOS | Simulator in Device Hub and real iPhone/iPad | Touch, keyboard, focus, navigation, sheets, resize and supported posture changes | Simulator is not proof of camera, radio, thermal, purchase or hardware behavior |
| tvOS | Apple TV simulator and real Apple TV | Directional focus, Select/Back, long press, text entry and playback controls | Mouse clicks that skip focus traversal cannot establish remote usability |
| macOS | Native Mac app on the host or another controlled Mac/VM | Keyboard, pointer, menus, windows, dialogs, documents and permissions | There is no macOS destination in the mobile Simulator. Catalyst is a separate build mode |
| visionOS | visionOS simulator and Apple Vision Pro | Spatial window/volume/immersive transitions, gaze/pinch, depth and comfort | Native visionOS SDK apps do not support XCUIAutomation UI testing in the researched contract |
| watchOS | Watch simulator, with a compatible phone where needed, and real Apple Watch | Crown, scrolling, text-entry choices, wrist/scene changes and phone connectivity | A standalone app and a companion workflow need different fixtures and device combinations |

Apple supports unit and UI test targets for watchOS. Do not repeat the obsolete blanket claim that Watch apps cannot have UI tests. For visionOS, XCUIAutomation supports compatible iPhone/iPad apps built with the iOS SDK, not native visionOS SDK apps. Keep component/render checks and manual spatial acceptance separate. See [platform scenarios](references/platform-scenarios.md).

Choose cases by behavioral risk: minimum supported OS, principal production device/OS, newest supported behavior, compact/large layouts and actual hardware-dependent features. Record display, input, language/region, appearance and accessibility settings. Do not promise all combinations from one shared simulator image or substitute Mac hardware timings for handheld performance.

## Prepare the Mac, runtimes and devices

Use full Xcode compatible with the Mac, SDKs and deployment targets. Command Line Tools alone do not provide the simulator/testing environment. Developing for visionOS requires Apple silicon under the current Xcode requirements. Record the selected developer directory and toolchain without silently changing the machine-wide selection:

```text
xcode-select -p
xcodebuild -version
```

Use Xcode → Open Developer Tool → Device Hub, or Manage Devices from the run-destination menu. Add the required model/runtime, installing platform support through Xcode when missing. Select a supported simulator or paired physical device. Native Mac tests select the actual Mac destination.

Use the current Device Hub pairing instructions for trust, Developer Mode and networking. A physical Watch may require its companion phone and authorization on both devices. Verify tvOS/visionOS discovery prerequisites and actual paired state. Do not assume one cable, one pairing flow or one device identity applies to all platforms.

Separate fresh installation, preserved-data upgrade, relaunch, simulator restart and simulator erase. A restart does not clear data, uninstall does not prove every credential/server record disappeared, and erasing a shared simulator destroys evidence. [Mac/simulator setup](references/macos-and-simulators.md) covers exact discovery and diagnosis.

## Build and run the intended suite

Find the real workspace or project and shared scheme. Inspect plans and destinations before constructing a command:

```text
xcodebuild -list -workspace Example.xcworkspace
xcodebuild -showTestPlans -workspace Example.xcworkspace -scheme Example
xcodebuild -showdestinations -workspace Example.xcworkspace -scheme Example
```

Replace names with inspected project values. Use `-project` instead of `-workspace` when appropriate, not both. Choose a real returned destination. A generic build-only destination is not a device on which tests executed.

For a conventional iOS simulator suite with an existing `Smoke` plan:

```text
xcodebuild test -workspace Example.xcworkspace -scheme Example -testPlan Smoke -destination 'platform=iOS Simulator,id=SIMULATOR_UDID' -derivedDataPath artifacts/derived-data -resultBundlePath artifacts/ios-smoke.xcresult
```

Create the parent artifact directory through the available file tool and use a fresh result path. Substitute actual plan and UDID. Inspect plans' enabled targets/configurations so an empty or skipped suite does not look successful. For other platforms, use the actual scheme/destination from discovery. Native macOS can use `platform=macOS` for the intended native scheme, while Catalyst needs its own reported variant.

Use `build-for-testing` to prepare compatible app/test products and `test-without-building` to execute those reviewed products where supported. Keep `.xctestrun`, runner, host app and resource paths together. Building simulator arm64 is different from building device arm64. Native Swift package tests can use `swift test` for package logic, but that does not execute application UI or all deployment destinations.

Use existing Swift Testing for suitable unit/component work and XCTest plus XCUIAutomation for supported UI tests. Select the actual provider-supported framework when packaging a cloud suite. Source language is independent of the rule that separately requested automation glue must be Python with uv.

For engine/canvas apps and native SDK sheets, select the observation surface per requirement. Use
the existing UI target where possible. A disposable XCTest runner can activate an installed app by
bundle ID without entering shipping source, but it must execute real assertions on a supported
destination. Keep native control reachability separate from a verified purchase/restore. See
[native UI and multi-display procedures](references/native-ui-and-multidisplay.md) for the worked
runner, display enumeration, posture/capture diagnosis and host-automation boundaries.

## Test forms, inputs and asynchronous work

Derive values from the real required/optional, normalization, format, range/length and cross-field rules. Do not invent a password policy, valid name alphabet or universal postal-code pattern.

| Dimension | Exercise | Required observation |
| --- | --- | --- |
| Presence | Untouched, empty, whitespace, cleared and optional fields | Correct submit state, associated error and retained valid data |
| Boundaries | Just outside and exactly at accepted limits | UI/API/storage agree without hidden truncation |
| Text | Accents, combining characters, emoji, supported scripts and long paste | Correct stored round-trip and declared grapheme/code-point/UTF-16/byte unit |
| Editing | Cursor movement, middle replacement, paste, delete, masks and undo where offered | Formatting and submitted canonical value stay consistent |
| Credentials | Secure field, visibility, autofill/password manager, invalid login and expiry | Correct accessible state and recovery without exposing secret values |
| Input method | Software/hardware keyboard, return action, Tab/Shift-Tab, dictation or supported platform method | Correct focus, submission, scrolling and visible error/action |
| Numeric/date | Locale separators, sign/zero/bounds, time zone and calendar boundary | The displayed value maps to the intended durable value |
| Choices/files | Required selection, cancellation, disabled values, denied file/photo access | Honest selection/upload state and deliberate access scope |
| Remote validation | Delayed response, changed value and out-of-order completion | A response for A cannot validate or reject current value B |
| Submission | Double activation, slow success, timeout, offline, retry and server field error | One intended durable operation and a recoverable state |

Test one invalid category at a time before interacting conditions. Assert error content, field association and focus, not just existence of a red border. A keyboard-visible screenshot and actual submitted data expose different defects.

On Apple TV, reach and submit the form using the remote focus path. On Watch, use supported text entry and Crown interaction on the selected model/language. On Mac, check first responder, default/cancel actions, keyboard shortcuts and menus. In visionOS, verify focus and text entry in the correct spatial presentation. [Forms and UI technique](references/forms-and-ui.md) expands these cases and synchronization.

## Inspect screens and platform lifecycle

Cover initial/loading/content/empty/error/offline states and transitions, including cancellation. Enter through normal navigation and supported deep links, document open or notification paths. Check modal dismissal, Back/Up equivalents, selected tab/sidebar, scroll position and repeated entry. An authenticated app must not show the previous account's cached records after switching users.

Inspect long translations, supported RTL, enlarged text, light/dark, increased contrast and reduced motion. Check safe areas, system overlays, keyboard occlusion and actual touch/focus/selection targets. Resizing the canvas zoom is different from changing the app's logical window size.

Separate background/foreground, OS termination, user termination, device restart, upgrade and state restoration. An explicit test termination is not proof of real background suspension, memory-pressure termination or Watch wrist-down behavior. On Mac, closing the final window may leave the app running, and reopening a document differs from relaunching the process.

Test permission grant, deny, limited selection and later revocation only where the platform/feature supports them. Include interrupted pickers, authentication callbacks and lost connectivity. Cover paired-phone disconnection/reconnection for Watch and immersive-space cancellation/re-entry for native visionOS. Document hardware-only checks such as sensors, haptics, real remote characteristics, accessibility use and spatial comfort.

When purchases are in scope, distinguish local StoreKit configuration, store sandbox/TestFlight and production. Exercise cancellation, pending/success/failure, restore and entitlement changes using the intended environment. Local transactions do not prove production receipt/server processing, and a cloud device may not provide the required store/account state. Verify the actual benefit without making a real charge as a testing shortcut.

## Use reliable observation and evidence

Inspect the accessible hierarchy, scope queries to the actual screen/window and use stable accessibility identifiers while retaining meaningful user-facing labels. Wait for the relevant element/state with bounded XCTest waits. Existence, visibility, hittability, enabled state, focus and successful persistence are different assertions.

A recorder proposes interactions, not complete acceptance. Add actual postconditions to existing tests when implementation was requested. UI automation does not directly inspect application-process models. Verify durable effects through authorized fixture/backend evidence. Reacquire handles after changing screens and do not keep tapping a remembered coordinate.

For native visionOS, do not invent an XCUITest target or an Appium workaround that bypasses unsupported SDK automation. Use available component tests, actual simulator interaction and physical-device acceptance. Keep unsupported coverage explicit.

Capture an unannotated screenshot/video around meaningful transitions and retain the `.xcresult`, selected logs and matching symbols for failures. Use Accessibility Inspector and manual assistive-technology testing. An automated audit covers its selected screen/rules, not complete accessibility. [Execution/evidence](references/execution-and-evidence.md) explains modern result inspection, performance conditions and CI isolation.

## Select cloud services by actual platform coverage

Research baseline: **2026-11-05**. Only user-requested maintenance changes stored facts. Confirm live account capabilities and cost before an authorized run.

| Service | Useful surface | Do not infer |
| --- | --- | --- |
| Xcode Cloud | Apple build/test actions, selected schemes/plans/destinations and result artifacts | An SDK/build enum does not prove a working test destination or native visionOS UI support |
| AWS Device Farm | Managed physical iOS XCTest/XCTest UI/Appium and interactive mobile sessions | A macOS test host is not advertised native Mac/Watch/Apple TV/Vision Pro farm coverage |
| AWS EC2 Mac | A managed-infrastructure Mac on which the team configures Xcode/desktop tests | A Mac host does not include a physical accessory fleet or automatic test setup |
| Google Developer Device Platform | Preview Device Run for physical iOS XCTest with reviewed ZIP/Xcode/device configuration | Android Device Streaming is not an Apple device stream, and iOS coverage is not all Apple platforms |
| Azure Pipelines | macOS build/test orchestration or submission to a selected lab | App Center Test retired March 31, 2025. A pipeline is not a phone/accessory farm |
| BrowserStack App Live / App Automate | Interactive or framework-based iOS device testing | A macOS browser session is not a native Mac-app test |

Choose local/controlled physical hardware where a cloud catalog does not document the requested platform or capability. A physical iPhone lab cannot validate a Watch companion session, Siri Remote focus, native Mac document behavior or Vision Pro comfort by proxy.

Exclude deprecated Firebase Test Lab from new execution plans. Its shutdown date belongs only to
an explicitly requested migration discussion. Do not use retired App Center Test. Google's iOS
guide documents an alpha/Preview path while its overview still describes iOS as forthcoming.
Treat that inconsistency as an availability check: require actual account/device/CLI support before
planning an execution. A published command page alone is not proof the account can run it.

Read [cloud procedures](references/cloud-labs.md) before uploads. It covers provider-specific package layouts, current iOS alpha CLI versus Android beta assumptions, host selection, run/session reconciliation, result retrieval and spending/cleanup. Do not submit a simulator app as a physical iOS artifact or replace a failed upload with a different build silently.

## Worked cross-platform acceptance case

Assume the actual requirement is a profile name of 2–40 user-perceived characters, one saved change and a draft-retention policy. These are example rules, not universal name validation.

1. Seed a synthetic account. Exercise length boundaries and accented/combined/emoji text according to that unit. Inspect submitted and reloaded values.
2. Start validation for A, change to B, then finish A last. Current validation must still describe B.
3. Delay Save and activate it twice using the platform's normal input. Confirm one durable update, correct loading/error state and safe retry after a lost response.
4. On iOS, expose the soft keyboard and resize supported layouts. On tvOS, reach the action through directional focus. On Mac, cover Tab/Return and separate windows. On Watch, cover Crown and the actual phone/offline mode. On native visionOS, perform the corresponding spatial journey manually, rather than labeling it an XCUITest pass.
5. Exercise the stated draft/scene restoration contract separately from a fresh install. Verify cleanup and the account-switch regression path.
6. Report which platform/device/input combinations actually ran, with artifacts and unresolved hardware coverage. One shared model test cannot certify all six user interfaces.

## Completion and foundations

Deliver matrix/rationale, exact artifacts/environment, executed cases, expected/actual results, reproducible findings, sanitized evidence and not-run coverage. Keep failures, skips, expected failures, infrastructure errors and diagnostic reruns distinct. Do not claim store approval or a bug-free app.

Apple's [testing guidance](https://developer.apple.com/documentation/xcode/testing) and [XCUIAutomation contract](https://developer.apple.com/documentation/xcuiautomation) govern framework scope. Selected [Testing Overview](https://abseil.io/resources/swe-book/html/ch11.html) and [Larger Testing](https://abseil.io/resources/swe-book/html/ch14.html) chapters from *Software Engineering at Google*, and selected [ISTQB CTFL sections](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf), inform case design and diagnosis. See [sources and access limits](references/sources.md) and [license](LICENSE.md).
