# Execution, evidence and CI decisions

Read this when you run a chosen case, look into a failure, compare images or connect an existing suite to CI. It describes a workflow and has no bundled code that runs tests.

## Establish one reproducible execution

Write down the source revision, artifact identity/hash, package/version, variant, the signing identity that matters for install, backend revision/fixtures and the chosen test suite. Write down tool versions and the real device model, OS/API, ABI, image, screen setup, language, theme, keyboard mode and data state. “Android emulator” is not enough to reproduce a failure.

Create a throwaway account/data namespace for each parallel worker. Keep tests that need a clean install apart from tests of kept app data. Check that fixture creation really worked before you open the UI. Do not read an empty account after failed seeding as the product's intended empty state.

Run the narrow changed behavior first, then the affected regression paths and the device limits you can justify. Keep a small startup/sign-in/navigation smoke set for every chosen device. Expand only when a risk or failure justifies the extra work. Write down what you left out instead of making up a promise that covers every device.

Local JVM tests, instrumented UI tests, black-box exploration and cloud crawling give different evidence. AndroidJUnitRunner must target the real app package and the chosen build. App and test APKs should come from the same reviewed build. Check that the framework/provider can really find your tests, not just that it accepted an upload.

## Observe, act and verify

Before you interact, check the current screen/semantic tree and confirm the intended package, user and state. Choose one specific target, do the action and wait for the meaningful visible outcome. Check again after navigation, animation, the keyboard appearing or scrolling.

For agent-guided capture with current Android CLI:

```text
android screen capture --device=SERIAL --output=profile-before.png
```

Use a different filename for the error/after state. `--annotate` adds targeting aids. Keep a plain screenshot as visual evidence, because numbered boxes change the image. Do not reuse a bounding-box label from an earlier frame after the layout moved.

Capture screenshots through the tool's output option instead of assuming every shell keeps redirected binary output intact. If you use ADB, write a PNG on the controlled device, pull it and remove only that device file:

```text
adb -s SERIAL shell screencap /sdcard/profile-error.png
adb -s SERIAL pull /sdcard/profile-error.png artifacts/profile-error.png
adb -s SERIAL shell rm /sdcard/profile-error.png
```

Open the pulled file and confirm it shows the intended state before you cite it. Do not get around a secure-window screenshot block, and do not claim that a blank protected screenshot proves a rendering bug.

Device input APIs may replace a whole field value instead of simulating keystrokes one by one. Test real keyboard editing separately when cursor, masks or IME composition are the requirement. A click/input command that returns success proves the interaction was accepted. It does not prove the expected screen or saved record exists.

## Collect enough evidence to explain failure

Keep the exact failing case, expected/actual result, first time it happened, device and the screenshots that matter. Include short logs around the event, the Java/Kotlin or native crash details when you have them, and an ANR trace or bugreport only when useful and allowed. Symbolication needs the matching mapping/native symbols from the tested artifact.

`adb -s SERIAL logcat -d` reads the device's available log buffer. It may include other apps or sensitive values. Prefer filtering by project/PID/time where it applies, and remember that a crash can change the PID. Do not clear the buffer before you save the evidence you need. Do not attach full raw logs or bugreports to a public issue without review.

JUnit XML/HTML reports describe the tests that ran. Screenshots/video show interaction and appearance. An approved backend trace shows real saving or deduplication. Link these by case/run identity. A screenshot of a success banner cannot alone prove the right tenant, record count or payment fulfillment.

Keep evidence in the target project's ignored artifact folder or approved report storage. Keep filenames, real file types, capture times and the identifiers that matter. Remove credentials, customer data, session URLs and payment details without changing the behavior needed for diagnosis.

## Visual and accessibility evidence

Compare a screenshot only against a reference with the intended rendering profile. Fix locale, theme, font scale, density, window and fixture data. Freeze only unimportant changing content when the project offers that on purpose. Keep a separate test for real animation/interaction behavior.

Review every changed reference image as a product change. A wide pixel tolerance can hide clipping or missing controls. Keep an expected antialiasing difference apart from a shifted layout, wrong text or missing state. Remote video compression is not a reliable pixel-perfect source.

Confirm accessible reading/focus order and labels on a real interaction path, including errors and dialogs. Automated scanners and semantic assertions add to manual assistive-technology use. They do not replace it. Report which method ran instead of calling the screen accessible for everyone.

## Performance evidence

Use a separate performance plan for startup, frame timing or memory. Macrobenchmark measures whole-app performance with a suitable non-debuggable, release-like target and controlled physical device conditions. A debug emulator on a busy host cannot show production speed or fair Windows/macOS/Linux performance rankings.

Write down device state, build/compilation setup, workload, repeated measurements and the trace that matters. Keep first/cold startup apart from warm behavior. Diagnose regressions against a matching baseline and a threshold that users would notice. Do not hide benchmark configuration errors just to get a number. Do not present cloud-farm timings as equal to a controlled benchmark environment.

## CI design without adding automation to the skill

Use the app's existing test configuration and checked-in wrapper. A pipeline you can justify can run fast local checks first, then a limited emulator/device smoke suite, with broader compatibility before release. Set matrix/shard limits so the job cannot grow into cloud spending nobody intended.

Give each parallel worker its own device, ports, account/data and artifact path. Never share a writable AVD or one changeable profile among workers. Orchestrator can isolate instrumentation instances, but it cannot isolate a shared backend. Write down data resets so they do not spoil an upgrade/restoration case.

Keep cloud credentials in approved identity/secret systems and out of logs. Untrusted pull requests must not get privileged test-account access or unlimited cloud identity. Upload only approved artifacts. Save run IDs so a cancellation or a runner that stops can be matched up with provider state.

Fail the job when the real required suite fails or a required run is missing. Publish the allowed reports on failure, cancel unfinished sessions and keep the original outcome. Label limited diagnostic reruns as reruns. A suite that passes in the end after silent retries has not shown first-attempt reliability.

If the user clearly asks for automation glue for a separate task, use Python with uv and declared dependencies. Existing Gradle tasks and native framework test source are their own tool/app surfaces. Do not create shell wrappers, generated Appium clients, polling utilities or refreshers just to show off this skill.

## Classify and report

| Result | Evidence needed | Consequence |
| --- | --- | --- |
| Passed | The case ran and both required UI/saved-state assertions succeeded | Supports only the tested configuration and behavior |
| Failed | A difference from the agreed contract that you can reproduce | Report trigger, impact, evidence and affected paths |
| Blocked | Missing account/tool/device/fixture or a requirement that is not available | Name the exact dependency and finish independent preparation |
| Infrastructure error | Device boot/install/provider/network setup stopped a real run | Diagnose that stage without calling an untested product broken |
| Skipped/not run | Case left out on purpose or never reached | Keep it out of the passed total and explain why |
| Flaky/inconclusive | Different outcomes with no known product/test/environment cause | Keep all attempts and investigate, without rewriting the first failure |

Set severity by impact and likelihood, separately from scheduling priority. A finding should name the exact build/device, preconditions, shortest steps, expected/actual result, how often it happens, artifact links and cleanup. Run the affected case again after a fix, plus the regression paths around it. Do not claim store approval, a full security review or that no bugs exist.

Use [the report template](../assets/test-report.md). [Source notes](sources.md) link Android execution/performance guidance and the selected professional testing chapters.
