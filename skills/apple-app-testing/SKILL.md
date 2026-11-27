---
name: apple-app-testing
description: Plan, run and investigate iOS, iPadOS, tvOS, macOS, visionOS and watchOS app tests from macOS. Use for forms, inputs, screens, accessibility, app lifecycle and compatibility with Xcode, simulators, real devices and researched cloud services, with clear automation limits for each platform.
license: MIT
---

# Apple App Testing

Check what the user actually gets on the right Apple platform, not just a passing build or a replayed gesture. This descriptive skill holds researched steps, native-tool examples and a report template. It does not include test programs, generated flows, cloud runners or automatic updates.

## Find the real product and test contract

Look at the project instructions, source revision, existing tests, workspace/project, schemes, test targets/plans, dependencies and supported deployment targets. Treat SwiftUI/UIKit/AppKit, Catalyst, compatible iPad apps, native spatial apps, independent Watch apps and phone companions as separate cases. A shared Swift package does not show that the UI works on every platform.

Collect bundle IDs, build/configuration, entitlements/signing needs, expected user journeys, the real field rules, a safe backend/fixtures and test identities. When the user gives only a binary, find out its platform, distribution channel and architecture. You cannot turn an arbitrary App Store IPA into a simulator build or get the original tests from it.

Ask only for missing facts that change how you run the tests: acceptance criteria, required devices/OS versions, pairing/account access, cloud uploads and a fixed spending limit. Use synthetic data. Permission to test the app is not permission to publish builds, enroll devices, expose private services or buy production products.

For each case, write down preconditions, input/actions, the expected UI and lasting effect, cleanup and evidence. Use [the report template](assets/test-report.md). When a device, tool or account is missing, mark the case as not run instead of making up results.

## Select the correct execution surface

| Platform | Local route on macOS | Interaction that must be tested | Important boundary |
| --- | --- | --- | --- |
| iOS/iPadOS | Simulator in Device Hub and real iPhone/iPad | Touch, keyboard, focus, navigation, sheets, resize and supported posture changes | Simulator does not prove camera, radio, thermal, purchase or hardware behavior |
| tvOS | Apple TV simulator and real Apple TV | Directional focus, Select/Back, long press, text entry and playback controls | Mouse clicks that skip moving focus cannot show that the remote is usable |
| macOS | Native Mac app on the host or another controlled Mac/VM | Keyboard, pointer, menus, windows, dialogs, documents and permissions | There is no macOS destination in the mobile Simulator. Catalyst is a separate build mode |
| visionOS | visionOS simulator and Apple Vision Pro | Spatial window/volume/immersive transitions, gaze/pinch, depth and comfort | Native visionOS SDK apps do not support XCUIAutomation UI testing in the researched contract |
| watchOS | Watch simulator, with a compatible phone where needed, and real Apple Watch | Crown, scrolling, text-entry choices, wrist/scene changes and phone connectivity | A standalone app and a companion workflow need different fixtures and device combinations |

Apple supports unit and UI test targets for watchOS. For visionOS, XCUIAutomation supports compatible iPhone/iPad apps built with the iOS SDK, not native visionOS SDK apps. Keep component/render checks and manual spatial acceptance separate. See [platform scenarios](references/platform-scenarios.md).

Pick cases by how likely a behavior is to break: minimum supported OS, main production device/OS, newest supported behavior, compact/large layouts and the features that really depend on hardware. Write down display, input, language/region, appearance and accessibility settings. Do not promise every combination from one shared simulator image. Do not use Mac hardware timings in place of handheld performance.

## Prepare the Mac, runtimes and devices

Use full Xcode that works with the Mac, SDKs and deployment targets. Command Line Tools alone do not give you the simulator/testing environment. Under the current Xcode requirements, visionOS development needs Apple silicon. Write down the selected developer directory and toolchain. Do not quietly change the machine-wide selection:

```text
xcode-select -p
xcodebuild -version
```

Use Xcode → Open Developer Tool → Device Hub, or Manage Devices from the run-destination menu. Add the model/runtime you need, and install platform support through Xcode when it is missing. Select a supported simulator or paired physical device. Native Mac tests select the real Mac destination.

Follow the current Device Hub pairing instructions for trust, Developer Mode and networking. A physical Watch may need its companion phone and approval on both devices. Check the tvOS/visionOS discovery requirements and the real paired state. Do not assume one cable, one pairing flow or one device identity works for all platforms.

Keep these apart: fresh install, upgrade that keeps data, relaunch, simulator restart and simulator erase. A restart does not clear data. An uninstall does not prove that every credential or server record is gone. Erasing a shared simulator destroys evidence. [Mac/simulator setup](references/macos-and-simulators.md) covers exact discovery and diagnosis.

## Build and run the intended suite

Find the real workspace or project and shared scheme. Look at plans and destinations before you build a command:

```text
xcodebuild -list -workspace Example.xcworkspace
xcodebuild -showTestPlans -workspace Example.xcworkspace -scheme Example
xcodebuild -showdestinations -workspace Example.xcworkspace -scheme Example
```

Replace the names with the values you found in the project. Use `-project` instead of `-workspace` when that fits, never both. Choose a real destination from the output. A generic build-only destination is not a device where tests ran.

For a normal iOS simulator suite with an existing `Smoke` plan:

```text
xcodebuild test -workspace Example.xcworkspace -scheme Example -testPlan Smoke -destination 'platform=iOS Simulator,id=SIMULATOR_UDID' -derivedDataPath artifacts/derived-data -resultBundlePath artifacts/ios-smoke.xcresult
```

Create the parent artifact folder with the available file tool. Use a fresh result path so nobody mistakes an earlier bundle for this run. Put in the real plan and UDID. Check each plan's enabled targets/configurations so an empty or skipped suite does not look like a pass. For other platforms, use the real scheme/destination from discovery. Native macOS can use `platform=macOS` for the intended native scheme. Catalyst needs its own reported variant, such as `platform=macOS,variant=Mac Catalyst`.

To run only the changed behavior first, add `-only-testing:TARGET/CLASS/METHOD` with identifiers from the real test target. After any run, read the result bundle summary described in [execution/evidence](references/execution-and-evidence.md). Confirm that the expected tests ran on the intended destination. `-retry-tests-on-failure` and `-test-iterations` are for diagnosis. Report their attempts separately so a later pass does not hide the first failure.

Use `build-for-testing` to prepare matching app/test products. Use `test-without-building` to run those reviewed products where supported. Keep `.xctestrun`, runner, host app and resource paths together. Building simulator arm64 is not the same as building device arm64. Native Swift package tests can use `swift test` for package logic, but that does not run the app UI or cover all deployment destinations.

Use existing Swift Testing for suitable unit/component work. Use XCTest plus XCUIAutomation for supported UI tests. When you package a cloud suite, select the framework the provider really supports. Any extra automation script the user asks for is written in Python and run with uv.

For engine/canvas apps and native SDK sheets, choose how to observe each requirement. Use the
existing UI target where you can. A throwaway XCTest runner can open an installed app by bundle
ID without touching shipping source, but it must run real assertions on a supported destination.
Being able to reach a native control is not the same as a verified purchase/restore. See
[native UI and multi-display procedures](references/native-ui-and-multidisplay.md) for the worked
runner, display listing, posture/capture diagnosis and host-automation limits.

## Test forms, inputs and asynchronous work

Take values from the real rules: required/optional, normalization, format, range/length and cross-field rules. Do not make up a password policy, a valid name alphabet or a universal postal-code pattern.

| Dimension | Exercise | Required observation |
| --- | --- | --- |
| Presence | Untouched, empty, whitespace, cleared and optional fields | Correct submit state, linked error and kept valid data |
| Boundaries | Just outside and exactly at accepted limits | UI/API/storage agree with no hidden truncation |
| Text | Accents, combining characters, emoji, supported scripts and long paste | Value saves and reloads correctly, in the stated grapheme/code-point/UTF-16/byte unit |
| Editing | Cursor movement, middle replacement, paste, delete, masks and undo where offered | Formatting and the submitted canonical value stay consistent |
| Credentials | Secure field, visibility, autofill/password manager, invalid login and expiry | Correct accessible state and recovery without showing secret values |
| Input method | Software/hardware keyboard, return action, Tab/Shift-Tab, dictation or supported platform method | Correct focus, submission, scrolling and visible error/action |
| Numeric/date | Locale separators, sign/zero/bounds, time zone and calendar boundary | The shown value maps to the intended saved value |
| Choices/files | Required selection, cancellation, disabled values, denied file/photo access | Honest selection/upload state and a deliberate access scope |
| Remote validation | Delayed response, changed value and out-of-order completion | A response for A cannot validate or reject current value B |
| Submission | Double activation, slow success, timeout, offline, retry and server field error | One intended saved operation and a state the user can recover from |

Test one invalid category at a time before you combine conditions. Check the error text, which field it belongs to and focus, not just that a red border exists. A screenshot with the keyboard showing and the data actually submitted reveal different bugs.

On Apple TV, reach and submit the form through the remote focus path. On Watch, use supported text entry and Crown interaction on the selected model/language. On Mac, check first responder, default/cancel actions, keyboard shortcuts and menus. In visionOS, check focus and text entry in the right spatial presentation. [Forms and UI technique](references/forms-and-ui.md) covers these cases and synchronization in more detail.

## Inspect screens and platform lifecycle

Cover initial/loading/content/empty/error/offline states and the moves between them, including cancellation. Enter through normal navigation and supported deep links, document open or notification paths. Check modal dismissal, Back/Up equivalents, selected tab/sidebar, scroll position and repeated entry. After a user switch, a signed-in app must not show the previous account's cached records.

Check long translations, supported RTL, larger text, light/dark, increased contrast and reduced motion. Check safe areas, system overlays, keyboard covering content and the real touch/focus/selection targets. Zooming the canvas is not the same as changing the app's logical window size.

Keep these apart: background/foreground, OS termination, user termination, device restart, upgrade and state restoration. Ending the app from a test does not prove real background suspension, memory-pressure termination or Watch wrist-down behavior. On Mac, closing the last window may leave the app running. Reopening a document is not the same as relaunching the process.

Test permission grant, deny, limited selection and later revocation only where the platform/feature supports them. Include interrupted pickers, sign-in callbacks and lost connectivity. Cover paired-phone disconnect/reconnect for Watch and immersive-space cancel/re-entry for native visionOS. Write down checks that need real hardware, such as sensors, haptics, real remote behavior, accessibility use and spatial comfort.

When purchases are in scope, keep local StoreKit configuration, store sandbox/TestFlight and production apart. Test cancellation, pending/success/failure, restore and entitlement changes in the intended environment. Local transactions do not prove production receipt/server processing. A cloud device may not have the store/account state you need. Check the real benefit without making a real charge as a testing shortcut.

## Use reliable observation and evidence

Look at the accessible hierarchy, limit queries to the real screen/window and use stable accessibility identifiers while keeping meaningful labels for users. Wait for the right element/state with time-limited XCTest waits. Existence, visibility, hittability, enabled state, focus and successful saving are different assertions.

A recorder suggests interactions. It does not give you complete acceptance. When the user asked for implementation, add real postconditions to existing tests. UI automation does not look directly at the app process's models. Check lasting effects through approved fixture/backend evidence. Find elements again after the screen changes, and do not keep tapping a remembered coordinate.

For native visionOS, do not invent an XCUITest target or an Appium workaround that gets around unsupported SDK automation. Use the component tests you have, real simulator interaction and acceptance on a physical device. State clearly what is not covered.

Capture a plain, unmarked screenshot/video around important transitions. For failures, keep the `.xcresult`, chosen logs and matching symbols. Use Accessibility Inspector and test by hand with assistive technology. An automated audit covers only its chosen screen/rules, not full accessibility. [Execution/evidence](references/execution-and-evidence.md) explains modern result inspection, performance conditions and CI isolation.

## Choose cloud services by real platform coverage

Research baseline: **2026-11-05**. Only maintenance that the user asks for changes stored facts. Before an approved run, confirm live account capabilities and cost.

| Service | Useful surface | Do not infer |
| --- | --- | --- |
| Xcode Cloud | Apple build/test actions, selected schemes/plans/destinations and result artifacts | An SDK/build enum does not prove a working test destination or native visionOS UI support |
| AWS Device Farm | Managed physical iOS XCTest/XCTest UI/Appium and interactive mobile sessions | A macOS test host does not mean the farm offers native Mac/Watch/Apple TV/Vision Pro coverage |
| AWS EC2 Mac | A Mac on managed infrastructure where the team sets up Xcode/desktop tests | A Mac host does not come with a physical accessory fleet or automatic test setup |
| Google Developer Device Platform | Preview Device Run for physical iOS XCTest with reviewed ZIP/Xcode/device configuration | Android Device Streaming is not an Apple device stream, and iOS coverage is not all Apple platforms |
| Azure Pipelines | macOS build/test orchestration or submission to a selected lab | A pipeline is not a phone/accessory farm |
| BrowserStack App Live / App Automate | Interactive or framework-based iOS device testing | A macOS browser session is not a native Mac-app test |

Use local or controlled physical hardware when a cloud catalog does not document the platform or feature you need. A physical iPhone lab cannot stand in for a Watch companion session, Siri Remote focus, native Mac document behavior or Vision Pro comfort.

Do not use Firebase Test Lab or App Center Test. Google's iOS guide documents an alpha/Preview
path while its overview says iOS is coming later.
Treat that mismatch as a reason to check availability: require real account/device/CLI support
before you plan a run. A published command page alone does not prove the account can run it.

Read [cloud procedures](references/cloud-labs.md) before uploads. It covers each provider's package layout, current iOS alpha CLI versus Android beta assumptions, host choice, matching runs/sessions to your records, getting results and spending/cleanup. Do not submit a simulator app as a physical iOS artifact. Do not quietly swap a failed upload for a different build.

## Worked cross-platform acceptance case

Say the real requirement is a profile name of 2–40 user-perceived characters, one saved change and a draft-keeping policy. These are example rules, not universal name validation.

1. Seed a synthetic account. Test length limits and accented/combined/emoji text in that unit. Check the submitted and reloaded values.
2. Start validation for A, change to B, then let A finish last. Current validation must still describe B.
3. Delay Save and press it twice with the platform's normal input. Confirm one saved update, the right loading/error state and a safe retry after a lost response.
4. On iOS, show the soft keyboard and resize supported layouts. On tvOS, reach the action through directional focus. On Mac, cover Tab/Return and separate windows. On Watch, cover Crown and the real phone/offline mode. On native visionOS, do the matching spatial journey by hand instead of calling it an XCUITest pass.
5. Test the stated draft/scene restoration contract separately from a fresh install. Check cleanup and the account-switch regression path.
6. Report which platform/device/input combinations really ran, with artifacts and any hardware coverage still missing. One shared model test cannot certify all six user interfaces.

## Completion and foundations

Deliver the matrix and reasons, exact artifacts/environment, cases run, expected/actual results, findings someone can reproduce, cleaned evidence and coverage that did not run. Keep failures, skips, expected failures, infrastructure errors and diagnostic reruns separate. Do not claim store approval or a bug-free app.

Apple's [testing guidance](https://developer.apple.com/documentation/xcode/testing) and [XCUIAutomation contract](https://developer.apple.com/documentation/xcuiautomation) set the framework scope. Selected [Testing Overview](https://abseil.io/resources/swe-book/html/ch11.html) and [Larger Testing](https://abseil.io/resources/swe-book/html/ch14.html) chapters from *Software Engineering at Google*, and selected [ISTQB CTFL sections](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf), guide case design and diagnosis. See [sources and access limits](references/sources.md) and [license](LICENSE.md).
