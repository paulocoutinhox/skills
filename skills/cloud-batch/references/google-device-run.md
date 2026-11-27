# Google Developer Device Platform: Device Run

Read this when the plan considers Google's device lab for Android or iOS tests. **This reference comes from the docs only, and the service was in Preview when checked on 2026-11-26.** The projects behind this skill used AWS Device Farm, not this service. Preview means pre-release terms, so ask the person whether that is acceptable before planning on it. Firebase Test Lab is deprecated and shuts down on September 30, 2027, so new work goes here or to [Device Farm](device-farm.md).

## Setup, once, with the person's go

- A Google Cloud project with a paid billing account (see [controller setup](controller-setup.md#google-cloud)).
- The roles from Google's quickstart for the person or service account: `roles/devicerun.admin`, `roles/viewer` and `roles/serviceusage.serviceUsageConsumer`, plus `roles/storage.objectViewer` on input buckets and `roles/storage.objectUser` on the output bucket. Add `roles/devicestreaming.admin` only for interactive Device Streaming.
- Enable the APIs that the quickstart lists for the surfaces you use.

## Android instrumentation tests

```bash
gcloud beta device-run devices list
gcloud beta device-run sessions submit instrumentation --device=<device id> --target-app=app.apk --test=app-androidTest.apk --instrumentation-timeout=30m --async
```

- Take the device id from `devices list`. Never guess one.
- `--instrumentation-timeout` accepts 1 minute to 3 hours. Set it, so a hang does not bill long.
- Use `--target-app` for the app. Do not use the deprecated `--apps` flag.
- Other flags: `--pre-target-apps`, `--post-target-apps`, `--bucket-name`, `--orchestrator-version`, `--flaky-test-attempts` (keep it at 1, so a flaky test is not retried into a pass), `--video` and `--sharding-option`.

## iOS XCTest on physical devices

```bash
gcloud alpha device-run sessions submit xctest --device=<device id> --test=./MyTests.zip --xctest-timeout=30m --async
```

- iOS runs only on the `alpha` track. It runs on physical iPhones and iPads, which the lab re-signs.
- Build with `xcodebuild build-for-testing -scheme <scheme> -destination "generic/platform=iOS"`, then zip the `Debug-iphoneos` folder and the `.xctestrun` file at the root of the zip.
- Only XCTest `test` methods are found. Swift Testing `@Test` functions are not.
- `--xctest-timeout` accepts 1 minute to 1 hour.

## Watch, cancel and collect

- `gcloud beta device-run sessions describe <session id> --full`, `sessions wait <session id>`, `sessions list` and `sessions cancel <session id>`, on the same track as the submission.
- If a submission times out, run `sessions list` before submitting again.
- Results go to Cloud Storage, by default `gs://<project id>-devicerun/automation/sessions/<session id>/`. Download what the report needs, then delete the session folder once the batch is recorded, since storage bills: `gcloud storage rm --recursive gs://<project id>-devicerun/automation/sessions/<session id>/`. Prove it with `gcloud storage ls gs://<project id>-devicerun/automation/sessions/`, which must not list that session.

## Price

Google bills per second with a 1-minute minimum, or per monthly device slot. Rates seen in search extracts of Google's product page, which did not render for the check, so read them in a browser before a plan:

| Item | Preview rate | From April 2027 |
| --- | --- | --- |
| Device Run, physical device | US$0.083 a minute | US$0.20 a minute |
| Emulator | US$0.017 a minute | US$0.06 a minute |
| Device slot | Not listed | US$250 a month physical, US$200 emulator |

## Sources

Checked on 2026-11-26: [Device Run Android instrumentation](https://docs.cloud.google.com/developer-device-platform/device-run/android-instrument), [Device Run iOS](https://docs.cloud.google.com/developer-device-platform/device-run/ios), [quickstart](https://docs.cloud.google.com/developer-device-platform/quickstart), [release notes](https://docs.cloud.google.com/developer-device-platform/release-notes), [submit instrumentation](https://docs.cloud.google.com/sdk/gcloud/reference/beta/device-run/sessions/submit/instrumentation), [submit xctest](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/device-run/sessions/submit/xctest), [gcloud release notes](https://docs.cloud.google.com/sdk/docs/release-notes), [product page](https://cloud.google.com/products/developer-device-platform) and the [Test Lab deprecation FAQ](https://firebase.google.com/docs/test-lab/migrate-faq). See [sources](sources.md) for the full record.
