# Execution, evidence and CI decisions

Read this when running a selected case, investigating a failure, comparing images or integrating an existing suite with CI. It describes a workflow and contains no bundled execution code.

## Establish one reproducible execution

Record source revision, artifact identity/hash, package/version, variant, signing identity relevant to installation, backend revision/fixtures and selected test suite. Record tool versions and the actual device model, OS/API, ABI, image, screen configuration, language, theme, keyboard mode and data state. “Android emulator” is not enough to reproduce a failure.

Create a disposable account/data namespace for each parallel worker. Separate tests that require a clean install from tests of preserved application data. Check actual fixture creation succeeded before opening the UI. Do not interpret an empty account after failed seeding as the product's intended empty state.

Run the narrow changed behavior first, then affected regression paths and justified device boundaries. Keep a small startup/authentication/navigation smoke set for every selected device. Expand only when a risk or failure supports the added work, and record excluded coverage rather than inventing a complete-device guarantee.

Local JVM tests, instrumented UI tests, black-box exploration and cloud crawling provide different evidence. AndroidJUnitRunner must target the actual application package and selected build. App and test APKs should come from the same reviewed build. Inspect the framework/provider's compatible test discovery, not just whether it accepted an upload.

## Observe, act and verify

Before interacting, inspect the current screen/semantic tree and confirm the intended package, user and state. Select one specific target, perform the action and wait for the meaningful observable outcome. Reinspect after navigation, animation, keyboard appearance or scrolling.

For agent-guided capture with current Android CLI:

```text
android screen capture --device=SERIAL --output=profile-before.png
```

Use a distinct filename for the error/after state. `--annotate` produces targeting aids. Keep an ordinary screenshot as visual evidence because numbered boxes alter the image. Do not reuse a bounding-box label from a previous frame after the layout moved.

Capture screenshots through the tool's output option rather than assuming that every shell preserves redirected binary output. If using the device screenshot path with ADB, write a PNG on the controlled device and pull the file. Do not bypass a secure-window screenshot restriction or claim a blank protected screenshot proves a rendering defect.

Device input APIs may replace a complete field value instead of simulating incremental keystrokes. Test real keyboard editing separately when cursor, masks or IME composition are the requirement. A click/input command returning success proves that interaction was accepted, not that the expected screen or durable record exists.

## Collect enough evidence to explain failure

Preserve the exact failing case, expected/actual result, first occurrence, device and relevant screenshots. Include bounded logs around the event, the Java/Kotlin or native crash details when available, and an ANR trace or bugreport only when useful and permitted. Symbolication requires the matching mapping/native symbols from the tested artifact.

`adb -s SERIAL logcat -d` reads the device's available log buffer. Its contents may include other applications or sensitive values. Prefer project/PID/time filtering where applicable, remembering that a crash can change the PID. Do not clear the buffer before preserving the evidence you need. Avoid attaching full raw logs or bugreports to a public issue without review.

JUnit XML/HTML reports describe executed tests. Screenshots/video show interaction and appearance. An authorized backend trace establishes actual persistence or deduplication. Keep these linked by case/run identity. A screenshot of a success banner cannot alone prove correct tenant, record count or payment fulfillment.

Keep evidence in the target project's ignored artifact directory or approved report storage. Preserve filenames, actual file types, capture times and relevant identifiers. Redact credentials, customer data, session URLs and payment details without altering the behavior needed for diagnosis.

## Visual and accessibility evidence

Compare a screenshot only against a reference with the intended rendering profile. Fix locale, theme, font scale, density, window and fixture data. Freeze only irrelevant volatile content when the project deliberately provides that capability. Keep a separate test for real animation/interaction behavior.

Review every changed reference image as a product change. A broad pixel tolerance can hide clipping or missing controls. Classify an expected antialiasing difference separately from a shifted layout, wrong text or missing state. Remote video compression is not a reliable pixel-perfect source.

Confirm accessible reading/focus order and labels on a real interaction path, including errors and dialogs. Automated scanners and semantic assertions complement manual assistive-technology use. Report which method ran instead of labeling the screen universally accessible.

## Performance evidence

Use a dedicated performance plan for startup, frame timing or memory. Macrobenchmark measures whole-app performance with a suitable non-debuggable, release-like target and controlled physical device conditions. A debug emulator on a busy host cannot establish production speed or fair Windows/macOS/Linux performance rankings.

Record device state, build/compilation setup, workload, repeated measurements and relevant trace. Separate first/cold startup from warm behavior. Diagnose regressions against a comparable baseline and user-facing threshold. Do not suppress benchmark configuration errors simply to produce a number. Avoid presenting cloud-farm timings as equivalent to a controlled benchmark environment.

## CI design without adding automation to the skill

Use the application's existing test configuration and checked-in wrapper. A justified pipeline can run fast local checks first, then a bounded emulator/device smoke suite, with broader compatibility before release. Define matrix/shard limits so the job cannot multiply into unintended cloud spending.

Give each parallel worker a distinct device, ports, account/data and artifact path. Never share a writable AVD or one mutable profile among workers. Orchestrator can isolate instrumentation instances, but cannot isolate a shared backend. Record data resets so they do not invalidate an upgrade/restoration case.

Keep cloud credentials in approved identity/secret mechanisms and out of logs. Untrusted pull requests must not receive privileged test-account access or unrestricted cloud identity. Upload only approved artifacts. Persist run IDs so cancellation or runner termination can be reconciled with provider state.

Fail the job for the actual required suite failure or missing required execution. Publish the permitted reports on failure, cancel unfinished sessions and keep the original outcome. Bounded diagnostic reruns should be labeled as reruns. A suite that eventually passes after silent retries has not demonstrated first-attempt reliability.

If the user explicitly asks for automation glue for a separate task, use Python with uv and declared dependencies. Existing Gradle tasks and native framework test source are their own tool/application surfaces. Do not create shell wrappers, generated Appium clients, polling utilities or refreshers merely to demonstrate this skill.

## Classify and report

| Result | Evidence needed | Consequence |
| --- | --- | --- |
| Passed | Executed case and both required UI/durable assertions succeeded | Supports only the tested configuration and behavior |
| Failed | Reproducible difference from the agreed contract | Report trigger, impact, evidence and affected paths |
| Blocked | Missing account/tool/device/fixture or unavailable prerequisite | Name the exact dependency and complete independent preparation |
| Infrastructure error | Device boot/install/provider/network setup prevented meaningful execution | Diagnose that stage without labeling an untested product defective |
| Skipped/not run | Case intentionally excluded or never reached | Keep it out of the passed denominator and explain why |
| Flaky/inconclusive | Different outcomes without an established product/test/environment cause | Preserve all attempts and investigate, without rewriting the first failure |

Use severity based on impact and likelihood, separate from scheduling priority. A finding should identify exact build/device, preconditions, minimal steps, expected/actual result, frequency, artifact links and cleanup. Re-run the affected case after a fix and the surrounding regression paths. Do not claim store approval, complete security assessment or absence of every defect.

Use [the report template](../assets/test-report.md). [Source notes](sources.md) link Android execution/performance guidance and the selected professional testing chapters.
