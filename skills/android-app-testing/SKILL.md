---
name: android-app-testing
description: Plan, run and investigate Android app tests from Windows, macOS or Linux with emulators, real devices and researched cloud labs. Use for forms, inputs, screens, accessibility, app lifecycle, compatibility and evidence-based QA. Covers what AWS, Google Cloud and Azure can and cannot do.
license: MIT
---

# Android App Testing

Test what the user can see happen and what it saves or changes. A passing build, a series of taps and a crawl with no crashes are different kinds of evidence. This descriptive skill gives the procedure. It does not include test programs, generated flows, collectors or automatic updates.

## Establish the test contract

Read the repository instructions, changed behavior, build files, existing tests and supported devices. Collect the source revision or supplied APK, package/application ID, build variant, framework, minimum/target SDK, supported ABIs, backend environment, test accounts, expected journeys and known bugs. Find out whether you have source access or only a black-box APK.

Ask only for missing facts that change how you run the tests: the real acceptance rules, staging access, destructive operations, required device coverage, cloud account/project, allowed uploads and spending. Use synthetic accounts and controlled data. A request to test is not permission to charge real cards, message customers, publish a release or upload a private APK.

Write each case as preconditions → exact input/actions → expected UI and backend outcome → cleanup → evidence. Tell product bugs, test bugs, unavailable infrastructure and cases not run apart. Use [the report template](assets/test-report.md) to keep these differences visible.

## Choose coverage before choosing devices

Use fast component tests for validation rules, integration tests for saving/API behavior and a small set of device journeys for real interaction. Add manual exploration for keyboard behavior, accessibility and device-specific display. Follow Android's [testing strategy](https://developer.android.com/training/testing/fundamentals/strategies), adjusted to the real risk instead of a fixed coverage percentage.

Pick the minimum supported API, the main production API/device, the newest supported Android behavior and the permission/storage/target-SDK limits that matter. Include a compact phone, tablet/foldable or resizable window only where supported. Add typical OEM hardware and low-memory conditions when the product depends on them. Explain each matrix dimension, and do not test every possible combination without limit.

The host OS tests whether the toolchain works on that host. The guest API, image, ABI, device, locale and settings test Android behavior. Running the same image on three hosts does not give you three Android compatibility profiles.

## Prepare Windows, macOS or Linux

Install the supported Android Studio/SDK toolchain and the JDK that works with the project's Gradle wrapper and Android Gradle Plugin. Find the real SDK location, platform tools, installed images and emulator version. Do not quietly upgrade the project to make a test command work.

| Host | Local emulator setup | Important boundary |
| --- | --- | --- |
| Windows | Supported x86-64 host, firmware virtualization turned on and Windows Hypervisor Platform | The researched Studio requirements do not support Windows on ARM. Prefer PowerShell and the checked-in `gradlew.bat` |
| macOS | Native Apple silicon tools with ARM64 images and Hypervisor.Framework. Intel hosts need matching x86 images/tool support | Do not assume Rosetta translates the app's missing native libraries |
| Linux | Supported x86-64 host, firmware virtualization and working KVM access for the current user | Containers/VM runners need documented virtualization support. Having a normal container does not prove emulator acceleration |

Use Device Manager → Create Virtual Device to pick hardware, API, ABI, image, orientation and storage. A Google APIs image includes Play services. A Google Play image also includes the Play Store. Choose based on the real feature, not on what is easiest. Match the image ABI to host acceleration and the app's native libraries.

Manage SDK packages and AVDs through Device Manager or the [Android CLI](https://developer.android.com/tools/agents) `android sdk` / `android emulator` commands. Use the emulator runtime's documented options, such as `-accel-check`, `-data`, `-cache` and `-no-snapshot`, only to diagnose acceleration and for isolated runs. List profiles first, create the chosen profile, list the new device name and start that exact device. The profile's defaults do not give you the requested API matrix. [Host setup and native commands](references/host-setup.md) covers shell differences and diagnosis.

Do not reuse snapshots as evidence of a clean install. Keep fresh install, upgrade that keeps data, cold boot and saved-state tests apart. Wiping data needs a throwaway test device and destroys evidence. A cold boot alone does not clear app data.

## Build, install and establish readiness

Use the checked-in wrapper and the real module/variant. A normal `app` debug variant can use:

```bash
./gradlew :app:testDebugUnitTest :app:assembleDebug :app:assembleDebugAndroidTest
```

On Windows PowerShell:

```powershell
.\gradlew.bat :app:testDebugUnitTest :app:assembleDebug :app:assembleDebugAndroidTest
```

Find the real tasks and output paths before you adapt this to another project. Building the test APK does not run it. An APK without source cannot give you the app's original instrumentation suite. You cannot install an AAB directly with `adb install`. Split APKs need a full matching set or the proper bundletool/store install path.

List devices with `adb devices -l`, pick the intended serial and confirm that boot has finished, the screen is unlocked, the package manager works and the app starts. A working connection alone does not mean the device is ready. Install the real APK with `adb -s SERIAL install PATH_TO_APK` for a fresh install, or `adb -s SERIAL install -r PATH_TO_APK` to replace an installed build while keeping its data for an upgrade case. Launch the real launcher activity, found from the manifest, and wait for it to finish starting:

```text
adb -s SERIAL shell am start -W -n PACKAGE/ACTIVITY
```

Expect a launch status with no error, then check the real screen. Install/signature/ABI errors need diagnosis. Do not keep retrying blindly or uninstall test data you meant to keep.

For an emulator that is already set up, a normal instrumentation run is `./gradlew :app:connectedDebugAndroidTest`, or `.\gradlew.bat :app:connectedDebugAndroidTest` on Windows. That task can target several connected devices. Disconnect unrelated devices or use the project's documented device selection. Build-managed device tasks join the configured device or group name with the variant, such as `./gradlew pixel2api30DebugAndroidTest` for a device declared as `pixel2api30`. Read the project's declared names instead of making up a universal task. Gradle reports test results and the HTML report path. A task that ends without running any tests is not a pass.

When you test a store delivery, generate the test APK set from the exact final signed AAB and write
down its hash/signing/install origin. Do not use a separately built Debug APK to back that claim.
Use a device/data path you own and have isolated, find the real launcher and keep store-account billing
errors apart from catalog bugs. Follow [release-bundle testing](references/release-bundle-testing.md) for
native bundletool commands, signature limits, device isolation and cleanup.

## Test forms and inputs as contracts

Find each field's type, required/optional status, accepted values, normalization, length unit, cross-field rules and server error mapping. Do not make up a password, postal-code, email or age policy. Take the values below from the real contract.

| Area | What to exercise | What to verify |
| --- | --- | --- |
| Presence | Untouched, empty, whitespace-only, cleared and optional fields | Correct submit eligibility, field-specific errors and focus. Optional is not the same as invalid |
| Length/range | Just below, exactly at and just above real limits | The UI/API/storage enforce the same rule with no silent truncation or overflow |
| Text | Accents, emoji, combined characters, non-Latin names and multiline paste where it applies | Value saves and reloads correctly, with correct cursor/selection and the stated byte/code-unit/grapheme counting |
| Keyboard | The right email/number/password IME, Next/Done, hardware Tab/Enter and Back | Correct focus order, action behavior, scrolling and visible errors/submit controls |
| Editing | Selection, replacement, paste, autofill, deletion and mask formatting | Shown value and submitted canonical value agree. Formatting keeps the field editable |
| Numeric/date | Decimal/group separators, sign, zero, limits, time zone and date edges | Locale-aware display with a clear saved value and the real business rules |
| Credentials | Password visibility, allowed paste/autofill, invalid login, expiry and logout | No credential leaks. Correct error and recovery with no state from another account |
| Choices | Checkbox/radio/dropdown/date picker, disabled choice and required consent | The real selection is submitted. Defaults and consent follow the product contract |
| Remote validation | Existing value, delayed answer, validation failure and changed input | Old responses do not mark the new value valid or invalid |
| Submission | Double tap, loading, timeout, retry, offline and server field errors | No duplicate saved operation. Inputs can be recovered as specified |
| Attachments | Cancel picker, denied permission, allowed/disallowed type, oversized/corrupt file | Honest preview/upload state and correct cleanup without broad access nobody asked for |
| Accessibility | Labels, role/value/error announcements, TalkBack and focus movement | The user can find, fix and submit the form without relying on color |

Test one invalid partition at a time before meaningful combinations, so an early error does not hide another. Add decision cases for rules that affect each other and state changes for async work. [Detailed test design](references/test-design.md) gives worked cases and ways to observe them with each tool.

## Exercise screens, navigation and lifecycle

For every affected screen, check initial/loading/content/empty/error/offline states. Enter through the normal flow and supported deep link or notification. Check system Back versus toolbar Up, where the back stack goes, tab state, dialogs, bottom sheets, cancel, scroll position and repeated navigation. Check signed-in and signed-out entry without showing another account's cached data.

Look at real screenshots at small/large window sizes, portrait/landscape, light/dark, supported languages, RTL and larger fonts/display settings. Check cutouts, system bars, edge-to-edge insets and the open keyboard. Text must stay readable, and key actions must stay reachable with no overlapping or clipped content. A screenshot comparison does not show that tap targets or navigation work.

Keep these apart: rotation/activity recreation, saved-state restoration, background process death, user force-stop and clean relaunch. Fill a draft, press Home, end only the controlled background process with `adb -s SERIAL shell am kill PACKAGE` and return through Recents to the existing task to test the intended restoration contract. `am kill` only ends processes that are safe to kill, so confirm in the device process list that the package process really ended before you read the result. If it did not end, record the case as not run instead of using force-stop. Rotation and “Don't keep activities” are not full process-death tests. Check that secrets are not restored into the wrong fields and that finished operations are not repeated.

Test permission allow/deny, dismissal, later revocation and limited access where supported. Cover interrupted pickers, app switching and connection changes. Test push, camera, Bluetooth, biometrics, DRM and billing on suitable hardware/store environments. Emulator simulation or a remote lab may not reproduce all their production conditions.

## Choose the interaction tool on purpose

| Tool/surface | Appropriate use | Evidence boundary |
| --- | --- | --- |
| Compose UI tests | Semantics-driven actions/assertions on Compose screens | Check merged/unmerged semantics. An idle UI does not mean remote work finished |
| Espresso | View-based app interactions and assertions | Register the async idling resources that matter. Avoid random sleeps |
| UI Automator | Permission dialogs, system UI, cross-app flows and interaction with an outside release app | The newer UI Automator API is still in development. Pin the exact dependency version you choose |
| Appium + UiAutomator2 | Black-box/native/hybrid journeys on emulators or remote devices | Pin a matching server, driver, client, Java/SDK and device API combination |
| Android CLI / device UI | Agent-guided or manual exploration with live selectors/screens | Check after each state change. A successful tap is not a successful case |
| Screenshot tests | Visual changes under a controlled rendering setup | Review reference-image changes. Preview rendering does not run the whole app |

Use stable resource IDs, semantic roles/labels or scoped tags. Do not replace accessibility labels users rely on with test identifiers. Native selectors do not automatically see WebView DOM or Flutter/canvas internals. Use the app's existing framework test surface, and switch to the WebView context on purpose when needed.

Wait for the right visible condition with a time limit. Capture the state when it fails. Compose's test clock does not finish outside I/O, and an unchanged accessibility tree does not prove the backend is done. Keep the first failure before any diagnostic rerun. [Execution and evidence](references/execution-and-evidence.md) covers device isolation, artifacts, visual checks and CI.

## Choose a cloud lab with current service facts

Research baseline: **2026-11-05**. Stored guidance changes only when the user asks for maintenance. Before an approved run, confirm the selected account's current catalog, permissions, pricing, retention and service availability.

| Service | Use | Important difference |
| --- | --- | --- |
| AWS Device Farm | Physical Android compatibility, instrumentation/Appium runs, interactive remote access | Regional service, uploaded artifacts and remote session/run lifecycle |
| Google Cloud Developer Device Platform | Device Run instrumentation sessions and Device Streaming | Preview at baseline. Billing, APIs, IAM and artifacts need explicit setup |
| Azure Pipelines | Build/test orchestration on a suitable agent or submission to a device lab | A CI runner is not a managed phone farm |
| BrowserStack App Live / App Automate | Interactive real-device testing / framework-based suites | Separate products and entitlements |

Check Device Run's Preview contract against the project's needs. Android Device Streaming is a separate interactive service. Microsoft currently documents macOS hosted agents for emulator tests and says its hosted Ubuntu agents lack the needed acceleration. Do not apply that limit to unrelated Linux runners.

Do not use Firebase Test Lab or App Center Test. If the project cannot accept Google's Preview
contract, choose another supported, approved route from the table.

Cloud devices cannot reach your workstation's `localhost` just because local tests could. Set up an approved staging backend they can reach, or use the provider's documented private-network path. Estimate the chosen devices × duration × shards × attempts, plus any storage/host costs. Set a fixed scope and stop sessions. Do not treat budget alerts as a spending cap.

Read [cloud procedures](references/cloud-labs.md) for exact AWS/GCP request steps, Azure limits, matching uploads to your records and reading results before you choose or run a provider.

## Worked acceptance case

Say the given contract states that a profile display name has 2–40 Unicode code points, the server returns a field error for a reserved name, and saving creates one profile update. These are example rules, not a suggested global name policy.

1. Seed a synthetic account and open the profile form on a compact phone with the soft keyboard on. Check existing values and labels.
2. Test lengths 1, 2, 40 and 41 one at a time. Try an accented name and a name with emoji, counted as that contract says. Confirm the saved and reloaded value and the real error state.
3. Start a delayed remote name check for value A, replace it with B and return A's result last. The validation state must still describe B.
4. Return a reserved-name error, fix the field and retry. Double-tap Save during a slow response. Check one saved update and consistent loading/navigation.
5. Rotate with an unsaved draft, then separately test background process restoration. Compare each outcome with the stated retention policy.
6. Repeat the critical path on typical physical hardware. Capture the keyboard/error screen and cleaned request/result evidence. A crawler reaching the success screen cannot replace these assertions.

If there is no device or cloud access, deliver these cases written out so they can be run later, and mark the run as blocked by that specific missing requirement. Do not make up screenshots, runs, pass rates or performance numbers.

## Completion and foundations

Deliver the chosen matrix and the reasons, exact build identity, cases run, expected/actual results, bugs someone can reproduce, cleaned artifacts and coverage that did not run. Confirm the affected regression paths after fixes. A diagnostic rerun that passes does not erase the first failure. End with the real decision the evidence supports, not “everything is bug-free.”

The [ISTQB CTFL syllabus](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf), selected sections 4.2 and 5.5, guides case design and reporting. Selected [Testing Overview](https://abseil.io/resources/swe-book/html/ch11.html) and [Larger Testing](https://abseil.io/resources/swe-book/html/ch14.html) chapters from *Software Engineering at Google* guide test scope, cost and diagnosis. Android and provider contracts set the rules for their tools. See [annotated sources and limitations](references/sources.md) and [license](LICENSE.md).
