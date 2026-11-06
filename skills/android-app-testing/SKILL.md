---
name: android-app-testing
description: Plan, execute and investigate Android app tests from Windows, macOS or Linux using emulators, physical devices and researched cloud labs. Use for forms, inputs, screens, accessibility, lifecycle, compatibility and evidence-based QA. Includes AWS, Google Cloud and Azure integration boundaries.
license: MIT
---

# Android App Testing

Test observable user outcomes and their durable effects. A successful build, a sequence of taps and a crash-free crawl are different forms of evidence. This descriptive skill provides the procedure without bundled test programs, generated flows, collectors or automatic updates.

## Establish the test contract

Inspect the repository instructions, changed behavior, build files, existing tests and supported devices. Collect the source revision or supplied APK, package/application ID, build variant, framework, minimum/target SDK, supported ABIs, backend environment, test accounts, expected journeys and known defects. Identify source access versus black-box APK access.

Ask only for missing facts that change execution: actual acceptance rules, staging access, destructive operations, required device coverage, cloud account/project, permitted uploads and spending. Use synthetic accounts and controlled data. Do not charge real cards, send messages to customers, publish a release or upload a private APK merely because testing was requested.

Record a case as preconditions → exact input/actions → expected UI and backend outcome → cleanup → evidence. Distinguish product defects, test defects, unavailable infrastructure and cases not run. Use [the report template](assets/test-report.md) to keep these distinctions visible.

## Choose coverage before choosing devices

Use fast component tests for validation rules, integration tests for persistence/API behavior and a focused set of device journeys for actual interaction. Add manual exploration for keyboard behavior, accessibility and device-specific presentation. Follow Android's [testing strategy](https://developer.android.com/training/testing/fundamentals/strategies), adapted to actual risk rather than a fixed coverage percentage.

Select the minimum supported API, the principal production API/device, the newest supported Android behavior and relevant permission/storage/target-SDK boundaries. Include compact phone, tablet/foldable or resizable window only where supported. Add representative OEM hardware and low-memory conditions when the product depends on them. Explain each matrix dimension and avoid an unbounded Cartesian product.

Host OS tests toolchain portability. Guest API, image, ABI, device, locale and settings test Android behavior. Running an identical image on three hosts does not establish three Android compatibility profiles.

## Prepare Windows, macOS or Linux

Install the supported Android Studio/SDK toolchain and the JDK compatible with the project's Gradle wrapper and Android Gradle Plugin. Identify the real SDK location, platform tools, installed images and emulator version. Do not silently upgrade the project to make a test command work.

| Host | Local emulator setup | Important boundary |
| --- | --- | --- |
| Windows | Supported x86-64 host, firmware virtualization enabled and Windows Hypervisor Platform | Windows on ARM is not supported by the researched Studio requirements. Prefer PowerShell and the checked-in `gradlew.bat` |
| macOS | Native Apple silicon tools with ARM64 images and Hypervisor.Framework. Intel hosts need compatible x86 images/tool support | Do not assume Rosetta translates the app's missing native libraries |
| Linux | Supported x86-64 host, firmware virtualization and working KVM access for the current user | Containers/VM runners need a documented virtualization capability. Ordinary container availability does not prove emulator acceleration |

Use Device Manager → Create Virtual Device to select hardware, API, ABI, image, orientation and storage. A Google APIs image includes Play services. A Google Play image additionally supplies the Play Store. Select based on the actual feature, not convenience. Match image ABI to host acceleration and application native libraries.

Current official SDK/AVD pages mark the standalone `sdkmanager`, `avdmanager` and emulator management CLI as deprecated in favor of [Android CLI](https://developer.android.com/tools/agents). Use Device Manager or the current `android sdk` / `android emulator` commands. List profiles first, create the chosen profile, list the resulting device name and start that exact device. The profile's defaults do not establish the requested API matrix. [Host setup and native commands](references/host-setup.md) cover shell differences and diagnosis.

Do not reuse snapshots as evidence of clean installation. Separate fresh install, preserved-data upgrade, cold boot and saved-state tests. Wiping data requires a disposable test device and destroys evidence. A cold boot alone does not clear application data.

## Build, install and establish readiness

Use the checked-in wrapper and actual module/variant. A conventional `app` debug variant can use:

```bash
./gradlew :app:testDebugUnitTest :app:assembleDebug :app:assembleDebugAndroidTest
```

On Windows PowerShell:

```powershell
.\gradlew.bat :app:testDebugUnitTest :app:assembleDebug :app:assembleDebugAndroidTest
```

Discover actual tasks and output paths before substituting another project. Building the test APK does not execute it. A source-less APK cannot provide the application's original instrumentation suite. An AAB is not directly installable with `adb install`, and split APKs require a complete compatible set or the proper bundletool/store installation path.

List devices with `adb devices -l`, select the intended serial and confirm completed boot, unlocked screen, package manager and app startup. Do not interpret transport availability alone as readiness. Install the actual APK with `adb -s SERIAL install PATH_TO_APK`, then launch its real activity or launcher entry. Installation/signature/ABI errors need diagnosis, not repeated blind attempts or uninstalling preserved test data.

For an already configured emulator, a conventional instrumentation run is `./gradlew :app:connectedDebugAndroidTest`, or `.\gradlew.bat :app:connectedDebugAndroidTest` on Windows. That task can target multiple connected devices. Disconnect unrelated devices or use the project's documented device selection. Build-managed device tasks use the configured device name and variant, not an invented universal task.

When testing a store delivery, generate the test APK set from the exact final signed AAB and record
its hash/signing/install provenance. Do not substitute a separately built Debug APK for that claim.
Use an owned isolated device/data path, discover the real launcher and separate store-account billing
errors from catalog defects. Follow [release-bundle testing](references/release-bundle-testing.md) for
native bundletool commands, signature boundaries, device isolation and cleanup.

## Test forms and inputs as contracts

Identify each field's type, required/optional status, accepted values, normalization, length unit, cross-field dependencies and server error mapping. Do not invent a password, postal-code, email or age policy. Derive the values below from the actual contract.

| Area | What to exercise | What to verify |
| --- | --- | --- |
| Presence | Untouched, empty, whitespace-only, cleared and optional fields | Correct submit eligibility, field-specific errors and focus. Optional is different from invalid |
| Length/range | Just below, exactly at and just above real boundaries | Consistent UI/API/storage enforcement without silent truncation or overflow |
| Text | Accents, emoji, combined characters, non-Latin names and multiline paste where relevant | Correct round-trip, cursor/selection and declared byte/code-unit/grapheme counting |
| Keyboard | Appropriate email/number/password IME, Next/Done, hardware Tab/Enter and Back | Correct focus order, action behavior, scrolling and visible errors/submit controls |
| Editing | Selection, replacement, paste, autofill, deletion and mask formatting | Display value and submitted canonical value agree. Formatting preserves editability |
| Numeric/date | Decimal/group separators, sign, zero, bounds, timezone and date boundaries | Locale-aware display with an unambiguous stored value and actual business rules |
| Credentials | Password visibility, allowed paste/autofill, invalid login, expiry and logout | No credential disclosure. Correct error and recovery without cross-account state |
| Choices | Checkbox/radio/dropdown/date picker, disabled choice and required consent | Actual selection submitted. Defaults and consent reflect the product contract |
| Remote validation | Existing value, delayed answer, validation failure and changed input | Obsolete responses do not mark the new value valid or invalid |
| Submission | Double tap, loading, timeout, retry, offline and server field errors | No duplicate durable operation. Inputs remain recoverable as specified |
| Attachments | Cancel picker, denied permission, allowed/disallowed type, oversized/corrupt file | Honest preview/upload state and correct cleanup without unrequested broad access |
| Accessibility | Labels, role/value/error announcements, TalkBack and focus movement | The user can identify, correct and submit the form without relying on color |

Test one invalid partition at a time before meaningful combinations, so an early error does not hide another. Add decision cases for interacting rules and state transitions for asynchronous work. [Detailed test design](references/test-design.md) gives worked cases and tool-specific observation techniques.

## Exercise screens, navigation and lifecycle

For every affected screen, inspect initial/loading/content/empty/error/offline states. Enter through the normal flow and supported deep link or notification. Check system Back versus toolbar Up, back-stack destination, tab preservation, dialogs, bottom sheets, cancel, scroll position and repeated navigation. Check authenticated and unauthenticated entry without exposing another account's cached data.

Inspect actual screenshots at small/large window sizes, portrait/landscape, light/dark, supported languages, RTL and enlarged fonts/display settings. Check cutouts, system bars, edge-to-edge insets and the open keyboard. Text must remain readable and essential actions reachable without overlapping or clipped content. A screenshot comparison does not establish working hit targets or navigation.

Distinguish rotation/activity recreation, saved-state restoration, background process death, user force-stop and clean relaunch. Fill a draft, background the app, end only the controlled background process and return through the existing task to test the intended restoration contract. Rotation and “Don't keep activities” are not complete process-death tests. Check that secrets are not restored into inappropriate fields and completed operations are not replayed.

Exercise permission allow/deny, dismissal, later revocation and limited access where supported. Cover interrupted pickers, app switching and connection changes. Test push, camera, Bluetooth, biometrics, DRM and billing on appropriate hardware/store environments. Emulator simulation or a remote lab may not reproduce their full production conditions.

## Select the interaction tool deliberately

| Tool/surface | Appropriate use | Evidence boundary |
| --- | --- | --- |
| Compose UI tests | Semantics-driven actions/assertions on Compose screens | Inspect merged/unmerged semantics. UI idle does not guarantee remote work finished |
| Espresso | View-based application interactions and assertions | Register relevant asynchronous idling resources. Avoid arbitrary sleeps |
| UI Automator | Permission dialogs, system UI, cross-app flows and external release-app interaction | Current modern API is under development. Use a compatible selected dependency |
| Appium + UiAutomator2 | Black-box/native/hybrid journeys on emulators or remote devices | Pin a compatible server, driver, client, Java/SDK and device API combination |
| Android CLI / device UI | Agent-guided or manual exploration using live selectors/screens | Inspect after each state change. A successful tap is not a successful case |
| Screenshot tests | Visual changes under a controlled rendering configuration | Review reference-image changes. Preview rendering does not exercise the whole app |

Use stable resource IDs, semantic roles/labels or scoped tags. Do not replace user-facing accessibility labels with testing identifiers. Native selectors do not automatically expose WebView DOM or Flutter/canvas internals. Use the application's existing framework test surface and deliberate WebView context switching when needed.

Wait for the relevant observable condition with a bounded timeout. Capture state when it fails. Compose's test clock does not complete external I/O, and an unchanged accessibility tree does not prove backend completion. Preserve the first failure before any diagnostic rerun. [Execution and evidence](references/execution-and-evidence.md) covers device isolation, artifacts, visual checks and CI.

## Choose a cloud lab with current service facts

Research baseline: **2026-11-05**. Stored guidance changes only when the user requests maintenance. Confirm the selected account's current catalog, permissions, pricing, retention and service availability before an authorized run.

| Service | Use | Consequential distinction |
| --- | --- | --- |
| AWS Device Farm | Physical Android compatibility, instrumentation/Appium runs, interactive remote access | Regional service, uploaded artifacts and remote session/run lifecycle |
| Google Cloud Developer Device Platform | Device Run instrumentation matrices and Device Streaming | Preview at baseline. Billing, APIs, IAM and artifacts need explicit setup |
| Azure Pipelines | Build/test orchestration on an appropriate agent or submission to a device lab | CI runner is not a managed phone farm. App Center Test retired March 31, 2025 |
| BrowserStack App Live / App Automate | Interactive real-device testing / framework-based suites | Separate products and entitlements. Microsoft names App Automate as a migration option |

For new Google cloud suites, evaluate Device Run's supported preview against project requirements. It is not a drop-in rename: device IDs, flags, attempts, storage and feature support differ. Android Device Streaming remains supported. Microsoft currently documents macOS hosted agents for emulator tests and states that its hosted Ubuntu agents lack the necessary acceleration. Do not copy that limitation to unrelated Linux runners.

Do not select deprecated Firebase Test Lab for a new testing workflow. Its announced September 30,
2027 shutdown is documented only to explain migration of an existing setup. App Center Test is
already retired and must not be used. If the project cannot accept Google's Preview contract,
select an actually supported authorized route rather than silently using a retired/deprecated service.

Cloud devices cannot reach your workstation's `localhost` merely because local tests did. Establish an authorized reachable staging backend or the provider's documented private-network path. Estimate the selected devices × duration × shards × attempts, plus applicable storage/host costs. Set a finite scope and stop sessions. Do not treat budget alerts as a spending cap.

Read [cloud procedures](references/cloud-labs.md) for concrete AWS/GCP request sequences, Azure constraints, upload reconciliation and result inspection before choosing or running a provider.

## Worked acceptance case

Assume the supplied contract says a profile display name contains 2–40 Unicode code points, the server returns a field error for a reserved name, and saving creates one profile update. These are example rules, not a proposed global name policy.

1. Seed a synthetic account and open the profile form on a compact phone with the soft keyboard enabled. Verify existing values and labels.
2. Exercise lengths 1, 2, 40 and 41 independently. Try an accented name and an emoji-containing name with values counted according to that contract. Confirm the stored round-trip and actual error state.
3. Start a delayed remote name check for value A, replace it with B and deliver A's result last. The validation state must still describe B.
4. Return a reserved-name error, correct the field and retry. Double-tap Save during a delayed response. Verify one durable update and consistent loading/navigation.
5. Rotate with an unsaved draft, then separately exercise background process restoration. Compare each outcome with the stated retention policy.
6. Repeat the critical path on representative physical hardware. Capture the keyboard/error screen and sanitized request/result evidence. A crawler reaching the success screen cannot replace these assertions.

If no device or cloud access exists, deliver these executable-in-prose cases and mark execution blocked by that specific prerequisite. Do not invent screenshots, runs, pass rates or performance measurements.

## Completion and foundations

Deliver the selected matrix and rationale, exact build identity, executed cases, expected/actual results, reproducible defects, sanitized artifacts and unexecuted coverage. Confirm affected regression paths after fixes. A diagnostic rerun passing does not erase the original failure. End with the actual decision supported by evidence, not “everything is bug-free.”

The [ISTQB CTFL syllabus](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf), selected sections 4.2 and 5.5, informs case design and reporting. Selected [Testing Overview](https://abseil.io/resources/swe-book/html/ch11.html) and [Larger Testing](https://abseil.io/resources/swe-book/html/ch14.html) chapters from *Software Engineering at Google* inform test scope, cost and diagnosis. Android and provider contracts govern their tools. See [annotated sources and limitations](references/sources.md) and [license](LICENSE.md).
