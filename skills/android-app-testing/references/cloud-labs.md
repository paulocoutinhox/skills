# Cloud labs and provider procedures

Read this when selecting a provider, preparing an authorized upload or interpreting a cloud run. Baseline: **2026-11-05**. Prices, devices, preview capabilities and account access can change. Only the user requests updates to this stored guidance.

## Choose the required service surface

Interactive remote access reproduces a problem on a selected physical device. A managed run executes a supplied suite across a matrix. A crawler explores reachable UI without proving business assertions. A CI runner builds and orchestrates work. These surfaces can cooperate but are not interchangeable.

Before uploading, establish the account/project, approved artifact, synthetic credentials/data, backend reachability, allowed region, retention and spending scope. A debug artifact may embed internal endpoints. Screenshots, video and logs can contain sensitive data even when the application binary is public.

## AWS Device Farm

### Managed runs

Device Farm provides physical Android devices. The researched mobile service endpoint is `us-west-2`. Use the authorized AWS profile and confirm identity before selecting an existing project or creating one. Query current devices/pools and choose the actual OS, model and capability rather than relying on a remembered ARN.

The native control sequence is:

1. Select a project through `list-projects`, or use `create-project` if creating one was requested.
2. Call `create-upload` for the application, with type `ANDROID_APP`, and retain its upload ARN and presigned URL.
3. PUT the exact APK bytes to that URL using the required headers. Creating an upload record does not transfer the file. Treat the presigned URL as sensitive.
4. Read `get-upload` until processing is terminal. Continue only after `SUCCEEDED`. Diagnose rejection before scheduling.
5. Upload the actual instrumentation test APK as `INSTRUMENTATION_TEST_PACKAGE`, or the provider-compatible Appium Python package for an existing Python suite. Verify processing for every upload.
6. For custom execution, select the current provider test specification, host and supported software. Upload the reviewed specification and retain its ARN. Custom mode is the provider's recommended path, not an assumption that every host has the same dependencies.
7. Submit `schedule-run` with application, pool/device selection, test type/package and the selected test specification. Record its run ARN before doing anything that could submit another run.
8. Inspect `get-run`, then per-device jobs/suites/tests. `COMPLETED` is a lifecycle state. Inspect the separate result, counters and actual executed cases.
9. Retrieve `list-artifacts` for the appropriate run/job/test with `LOG`, `FILE` or `SCREENSHOT`. Download authorized evidence before its links expire and inspect the files.

An illustrative custom instrumentation submission, after the placeholders have been replaced by successful uploads and a selected pool:

```text
aws devicefarm schedule-run --region us-west-2 --project-arn PROJECT_ARN --app-arn APP_UPLOAD_ARN --device-pool-arn POOL_ARN --name profile-regression --test type=INSTRUMENTATION,testPackageArn=TEST_UPLOAD_ARN,testSpecArn=SPEC_UPLOAD_ARN
```

Inspect it with the returned ARN:

```text
aws devicefarm get-run --region us-west-2 --arn RUN_ARN
aws devicefarm list-artifacts --region us-west-2 --arn RUN_ARN --type LOG
```

These are native-tool examples, not an included runner. Do not copy an old test-host specification blindly. The general framework index contains outdated Appium-version wording, while the dedicated current Appium page makes support dependent on host/device and documents newer environments. Use the exact selected host and server/driver/client compatibility. An API enum alone does not establish working execution on every host.

### Interactive reproduction

Create a remote access session for the selected device, install the approved uploaded app and reproduce the recorded steps through the browser. Capture the relevant screen/video and stop the session when finished. Remote sessions can also expose a managed Appium endpoint for a local client or Inspector.

A local workstation filesystem path is not a valid remote `appium:app`. Use the documented upload, approved HTTPS/S3 artifact or installed package. Do not disclose a managed endpoint or session token in a public report. Deleting an Appium client session and stopping the enclosing remote-access reservation are separate cleanup responsibilities.

Private-backend access depends on the actual fleet and provider network configuration. Review that capability before renting devices. Do not assume the device and its test host have identical connectivity. Keep run timeouts and device count finite, inspect applicable quotas and stop abandoned work after an interrupted client.

## Google Cloud Developer Device Platform

### New cloud workflows

Device Run and Device Streaming are the relevant services. At the baseline, Developer Device Platform is **Preview**. Confirm that the project's support/compliance requirements accept that stage. Do not present a beta CLI as a generally available product guarantee.

Prepare an authorized Google Cloud project, billing, current gcloud installation and appropriate IAM. The quickstart names Device Run, Device Streaming and Cloud Testing APIs during Preview. Enable only the required documented services through an authorized setup action. Follow its local authentication/ADC requirements or the selected federated workload identity for CI. Never commit a service-account key or copy interactive credentials into a job.

The combined quickstart lists `roles/devicerun.admin`, `roles/devicestreaming.admin`, `roles/serviceusage.serviceUsageConsumer` and viewer access. API enablement needs its own `serviceusage.services.enable` permission. Select roles for the actual used surfaces or a reviewed narrower role, without defaulting to project Owner. A caller's permissions and the service's access to an existing artifact bucket are different checks.

List devices using `gcloud beta device-run devices list --project=PROJECT_ID` and inspect the catalog's platform, hardware type, OS and supported product. A streaming-capable entry need not provide the requested automation surface. Choose an actual returned ID, not an assumed combination of model and API.

After building matching application and instrumentation APKs, an illustrative submission is:

```text
gcloud beta device-run sessions submit instrumentation --project=PROJECT_ID --device=DEVICE_ID --apps=app.apk --test=app-androidTest.apk --instrumentation-timeout=5m --flaky-test-attempts=1 --async
```

The five-minute timeout is a chosen example, not a suggested budget for every suite. `--flaky-test-attempts=1` means one total attempt. Record the returned session identity and query it:

```text
gcloud beta device-run sessions describe SESSION_ID --project=PROJECT_ID --full
```

Use `sessions wait` when a blocking wait is appropriate and `sessions cancel` to stop authorized unfinished work. Read each device/job outcome and selected suite, not only the successful submission. Inspect the documented artifact paths in the result and download only needed logs, reports and media.

Inputs and outputs use Cloud Storage. The default bucket is `PROJECT_ID-devicerun`, or use an approved explicit bucket. Verify service access for existing buckets, object retention and who can read screenshots. Device release does not delete stored artifacts. Select `--paths-to-pull`, video, dumpsys and bugreport collection deliberately to avoid collecting unrelated device/user data.

Use `software-versions list` before selecting an Orchestrator version. Device Run does not enable Orchestrator by default. Its isolation does not reset shared backend accounts, and clearing package data is inappropriate for a preserved-data upgrade scenario. Sharding increases simultaneous work and requires independent fixtures.

### Excluded new target: Firebase Test Lab

The official November 3, 2026 notice deprecates Test Lab and announces complete shutdown on **September 30, 2027**. Existing executions remain supported until then, but this collection does not select it for new testing workflows. The following distinctions are migration context only. Android Device Streaming is not deprecated.

For an existing account still using Test Lab, the documented test types are instrumentation, Robo and Game Loop. Console, gcloud and Testing/ToolResults APIs provide different submission/results surfaces. A Robo crawl can expose crashes or layout problems without a handwritten suite, but custom-drawn UI, authentication and unvisited business paths limit coverage. A supplied test login must be synthetic. A passed crawl is not a verified purchase/profile workflow.

Migration needs actual command/flag translation and feature assessment. Device Run uses `--apps`, combined catalog IDs and total attempt counts rather than Test Lab's retry count. Do not translate a Robo or Game Loop job into an instrumentation command and claim equivalent coverage. Review the supported destination for that feature instead of introducing silent fallback behavior.

Test Lab's no-cost quotas and Developer Device Platform's billing requirements are different. Do not copy one service's allowance into the other. Consult the active account and current pricing, including storage. A budget alert reports spending and does not stop it.

### Interactive devices and release-adjacent evidence

Android Studio's Device Manager can reserve a supported Android Device Streaming device after project/authentication setup. Deploy the selected APK, interact with its UI and finish the session explicitly. Device reset at the provider does not revoke a test account's backend tokens or delete backend records.

Google Play pre-launch reports can add crash, compatibility and accessibility evidence for uploaded test releases. They are a separate Play workflow and do not guarantee complete coverage. App Distribution provides builds to testers and can support feedback, but distributing an APK alone does not execute its acceptance tests. None of these services is permission to publish production.

## Azure and Microsoft

App Center Test retired on **March 31, 2025**. Later Analytics & Diagnostics extensions do not restore the testing product. Do not recommend new `appcenter test run` jobs or the obsolete test service as an available Azure device farm.

Use Azure Pipelines to build, execute existing tests on an appropriate agent or submit artifacts to an authorized device lab. The current Microsoft Android guide calls for a **macOS Microsoft-hosted agent** for accelerated emulator tests and states that hosted Ubuntu agents do not provide the required acceleration. Check the actual agent-image software manifest before choosing an image. Self-hosted Windows/macOS/Linux agents need their own verified SDK, hardware and device isolation.

The conceptual pipeline is checkout → compatible toolchain → unit/build checks → device readiness → existing suite → results/artifacts → device/session cleanup. Preserve failing exit statuses and publish evidence even when the suite fails. A task that builds an APK is not an instrumented test run. Do not paste the guide's historical SDK/AVD Bash recipe as a new maintained script.

Microsoft's migration notice points to BrowserStack App Automate for device testing. BrowserStack App Live is the interactive product, while App Automate executes supported suites. Use the selected product's real account/capabilities and documented Local Testing connection for private backends. Record tunnel/session termination and redact access credentials. Do not assume that purchasing Azure capacity includes either subscription.

## Bound execution and reconcile interruptions

Record provider/project, source/artifact hash, selected devices, timeout, attempts, labels and run/session ID. On a client timeout, query the known run before submitting again. If creation response was lost, inspect recent account runs by identity/time/artifact evidence rather than assuming nothing happened.

Cancellation, stopped work, infrastructure failure, skipped tests and passing assertions are distinct. Report the actual executed denominator. Stop reservations and revoke temporary access within the agreed scope. Do not delete an entire shared cloud project as a cleanup shortcut. See [sources](sources.md) for the exact provider documents and [execution/evidence](execution-and-evidence.md) for report semantics.
