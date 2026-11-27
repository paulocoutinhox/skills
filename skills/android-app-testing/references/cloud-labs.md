# Cloud labs and provider procedures

Read this when you choose a provider, prepare an approved upload or read a cloud run. Baseline: **2026-11-05**. Prices, devices, preview features and account access can change. Only the user asks for updates to this stored guidance.

## Choose the required service surface

Interactive remote access reproduces a problem on a chosen physical device. A managed run runs a supplied suite across a matrix. A crawler explores the UI it can reach, without proving business assertions. A CI runner builds and coordinates work. These surfaces can work together, but one cannot replace another.

Before you upload, settle the account/project, approved artifact, synthetic credentials/data, backend reachability, allowed region, retention and spending limit. A debug artifact may contain internal endpoints. Screenshots, video and logs can contain sensitive data even when the app binary is public.

## AWS Device Farm

### Managed runs

Device Farm offers physical Android devices. The researched mobile service endpoint is `us-west-2`. Use the approved AWS profile and confirm identity before you pick an existing project or create one. Query current devices/pools and choose the real OS, model and capability instead of relying on an ARN from memory.

The native control steps are:

1. Pick a project through `list-projects`, or use `create-project` if creating one was requested.
2. Call `create-upload` for the app, with type `ANDROID_APP`, and keep its upload ARN and presigned URL.
3. Send the exact APK bytes to that URL, for example with `curl -T app.apk "PRESIGNED_URL"`. Creating an upload record does not send the file. Treat the presigned URL as sensitive and keep it out of logs.
4. Read `get-upload` until processing leaves `INITIALIZED`/`PROCESSING`. Continue only after `SUCCEEDED`. On `FAILED`, read its metadata/message and find the cause of the rejection before scheduling.
5. Upload the real instrumentation test APK as `INSTRUMENTATION_TEST_PACKAGE`, or the provider-compatible Appium Python package for an existing Python suite. Check processing for every upload.
6. For custom execution, find the default specification for the test type with `list-uploads --arn PROJECT_ARN`, download it through `get-upload` and review its host and supported software. Upload the reviewed file with the matching specification type, such as `INSTRUMENTATION_TEST_SPEC`, and keep its ARN. Custom mode is the path the provider recommends. Do not assume every host has the same dependencies.
7. Submit `schedule-run` with the app, pool/device selection, test type/package and the chosen test specification. Write down its run ARN before you do anything that could submit another run.
8. Check `get-run`, then the jobs/suites/tests for each device. `COMPLETED` is a lifecycle state. Check the separate result (`PASSED`, `WARNED`, `FAILED`, `SKIPPED`, `ERRORED` or `STOPPED`), counters and the cases that really ran. A `SKIPPED` result with `resultCode` `PARSING_FAILED` means the test package was not parsed and no case ran.
9. Get `list-artifacts` for the right run/job/test with `LOG`, `FILE` or `SCREENSHOT`. Download approved evidence before its links expire, and look at the files.

A sample custom instrumentation submission, after the placeholders have been replaced by successful uploads and a chosen pool:

```text
aws devicefarm schedule-run --region us-west-2 --project-arn PROJECT_ARN --app-arn APP_UPLOAD_ARN --device-pool-arn POOL_ARN --name profile-regression --test type=INSTRUMENTATION,testPackageArn=TEST_UPLOAD_ARN,testSpecArn=SPEC_UPLOAD_ARN
```

Check it with the returned ARN:

```text
aws devicefarm get-run --region us-west-2 --arn RUN_ARN
aws devicefarm list-artifacts --region us-west-2 --arn RUN_ARN --type LOG
```

To end approved unfinished work, use `aws devicefarm stop-run --region us-west-2 --arn RUN_ARN`. Devices that have not started stop at once. Devices that already started still finish setup/teardown, and you still pay for that work. These are native-tool examples, not an included runner. Do not copy an old test-host specification blindly. The general framework index has outdated Appium-version wording, while the dedicated current Appium page ties support to host/device and documents newer environments. Use the exact chosen host and server/driver/client compatibility. An API enum alone does not show that a run works on every host.

### Interactive reproduction

Create a remote access session for the chosen device, install the approved uploaded app and reproduce the recorded steps through the browser. Capture the screen/video you need and stop the session when you finish. Remote sessions can also offer a managed Appium endpoint for a local client or Inspector.

A local workstation file path is not a valid remote `appium:app`. Use the documented upload, an approved HTTPS/S3 artifact or an installed package. Do not reveal a managed endpoint or session token in a public report. Deleting an Appium client session and stopping the remote-access reservation around it are separate cleanup jobs.

Access to a private backend depends on the real fleet and the provider's network setup. Check that capability before you rent devices. Do not assume the device and its test host have the same connectivity. Keep run timeouts and device count fixed, check the quotas that apply and stop abandoned work after an interrupted client.

## Google Cloud Developer Device Platform

### Device Run

Device Run and Device Streaming are the services that matter here. At the baseline, Developer Device Platform is **Preview**. Confirm that the project's support/compliance rules accept that stage. Do not present a beta CLI as a promise of a generally available product.

Prepare an approved Google Cloud project, billing, a current gcloud install and suitable IAM. The quickstart names Device Run, Device Streaming and Cloud Testing APIs during Preview. Turn on only the documented services you need, through an approved setup action. Follow its local sign-in/ADC requirements, or the chosen federated workload identity for CI. Never commit a service-account key or copy interactive credentials into a job.

The combined quickstart lists `roles/devicerun.admin`, `roles/devicestreaming.admin`, `roles/serviceusage.serviceUsageConsumer` and viewer access. Turning on an API needs its own `serviceusage.services.enable` permission. Choose roles for the surfaces you really use, or a reviewed narrower role. Do not default to project Owner. A caller's permissions and the service's access to an existing artifact bucket are separate checks.

List devices with `gcloud beta device-run devices list --project=PROJECT_ID` and check the catalog's platform, hardware type, OS and supported product. An entry that supports streaming may not offer the automation surface you need. Choose a real returned ID, not a guessed combination of model and API.

After you build matching app and instrumentation APKs, a sample submission is:

```text
gcloud beta device-run sessions submit instrumentation --project=PROJECT_ID --device=DEVICE_ID --apps=app.apk --test=app-androidTest.apk --instrumentation-timeout=5m --flaky-test-attempts=1 --async
```

The five-minute timeout is a sample value within the documented 1m–3h range, not a suggested budget for every suite. `--apps` installs the listed APK/AAB/APKS files before the tests run. `--flaky-test-attempts` sets the maximum total attempts per job or shard, so `1` means no retry. Write down the returned session identity and query it:

```text
gcloud beta device-run sessions describe SESSION_ID --project=PROJECT_ID --full
```

Use `sessions wait` when a blocking wait fits, and `sessions cancel` to stop approved unfinished work. Read each device/job outcome and the chosen suite, not only the successful submission. Check the documented artifact paths in the result and download only the logs, reports and media you need.

Inputs and outputs use Cloud Storage. The default bucket is `PROJECT_ID-devicerun`, or use an approved bucket you name. Check service access for existing buckets, object retention and who can read screenshots. Releasing the device does not delete stored artifacts. Choose `--paths-to-pull`, video, dumpsys and bugreport collection on purpose, so you do not collect unrelated device/user data.

Use `software-versions list` before you choose an Orchestrator version. Device Run does not turn on Orchestrator by default. Its isolation does not reset shared backend accounts, and clearing package data is wrong for an upgrade case that keeps data. Sharding adds work running at the same time and needs independent fixtures.

### Interactive devices and release-adjacent evidence

Android Studio's Device Manager can reserve a supported Android Device Streaming device after project/sign-in setup. Deploy the chosen APK, use its UI and end the session yourself. A device reset at the provider does not revoke a test account's backend tokens or delete backend records.

Google Play pre-launch reports can add crash, compatibility and accessibility evidence for uploaded test releases. They are a separate Play workflow and do not promise full coverage. App Distribution gives builds to testers and can help with feedback, but handing out an APK does not run its acceptance tests. None of these services is permission to publish to production.

## Azure and Microsoft

Azure has no managed Android device farm. Do not use App Center Test.

Use Azure Pipelines to build, run existing tests on a suitable agent or submit artifacts to an approved device lab. The current Microsoft Android guide calls for a **macOS Microsoft-hosted agent** for accelerated emulator tests and says hosted Ubuntu agents do not provide the needed acceleration. Check the real agent-image software manifest before you choose an image. Self-hosted Windows/macOS/Linux agents need their own checked SDK, hardware and device isolation.

The basic pipeline is checkout → matching toolchain → unit/build checks → device readiness → existing suite → results/artifacts → device/session cleanup. Keep failing exit statuses and publish evidence even when the suite fails. A task that builds an APK is not an instrumented test run. Do not paste a guide's SDK/AVD Bash recipe as a maintained script.

BrowserStack App Live is the interactive real-device product, while App Automate runs supported suites. Use the chosen product's real account/capabilities and the documented Local Testing connection for private backends. Write down tunnel/session shutdown and hide access credentials. Do not assume that buying Azure capacity includes either subscription.

## Limit runs and sort out interruptions

Write down provider/project, source/artifact hash, chosen devices, timeout, attempts, labels and run/session ID. On a client timeout, query the known run before you submit again. If the creation response was lost, check recent account runs by identity/time/artifact evidence instead of assuming nothing happened.

Cancellation, stopped work, infrastructure failure, skipped tests and passing assertions are all different. Report the real number of cases that ran. Stop reservations and revoke temporary access within the agreed scope. Do not delete a whole shared cloud project as a cleanup shortcut. See [sources](sources.md) for the exact provider documents and [execution/evidence](execution-and-evidence.md) for what report results mean.
