# AWS Device Farm

Read this when a check needs real phones or tablets. Device Farm also rents Android emulators and iOS simulators, but local ones come first and cost nothing. Docs checked on **2026-11-26**. Prices, devices and hosts change, so check the [pricing page](https://aws.amazon.com/device-farm/pricing/) and run `list-devices` before every run you pay for.

## Where it fits and what it costs

- Device Farm runs only in `us-west-2` (Oregon). Every command passes `--region us-west-2`.
- It offers Android and iOS devices only, physical and virtual (Android emulators and iOS simulators). One run or device pool cannot mix physical and virtual devices. It has no Apple TV, Apple Vision Pro or Apple Watch, and no other researched cloud rents them, so tvOS and visionOS stay on local simulators and the person's own devices.
- Prices seen on 2026-11-26:
  - pay as you go, US$0.17 per device minute;
  - an unmetered device slot, US$250 per slot per month, for heavy use;
  - a one-time free trial, normally 250 device minutes, 1,000 during a promotion shown that day;
  - desktop browser testing through Selenium, US$0.005 per instance minute.
- Runs bill as `METERED` unless the run sets `billingMethod` to `UNMETERED` in `--configuration` and the account owns slots.
- Limits that shape a plan:
  - 5 metered automation devices at once and 2 metered remote access devices, both adjustable by request;
  - 150 minutes at most per device for a run and for a remote access session, not adjustable;
  - uploads up to 4 GB, and `.aab` files are not accepted;
  - uploaded apps and test packages are kept 30 days, logs and videos 400 days.

Use Device Farm for what simulators and emulators cannot show: real GPUs from several vendors, real performance, real sensors and signing. Everything else runs locally first.

## Cover GPU vendors and OS versions

A small physical set can cover the main mobile GPU families: Qualcomm Adreno, ARM Mali, Imagination PowerVR and Samsung Xclipse, with old and new Android versions. A set used in practice was a Galaxy S25 (Adreno 830), a Pixel 9 (Mali-G715), a Pixel 10 (PowerVR D-Series) and a Redmi Note 13 (Mali-G57): three GPU families, with a new and a budget Mali. Add a Samsung phone with an Xclipse GPU for the fourth family. The public docs do not list device models, so confirm each one with `list-devices` on the day.

Hardware limits seen in practice:

- A Mali-G57 had no OpenGL ES timer queries and no usable Vulkan timestamps, so GPU time showed as "Not measured". A test must report that, not fail or invent a number.
- A test cannot rotate a physical device. That test skips there with a sentence and runs on the emulator.
- Real performance differs widely between phones. Record numbers per device, such as frames per second and the mean frame time of stress scenes.

## Choose devices

1. `aws devicefarm list-devices --region us-west-2 --filters '[{"attribute":"PLATFORM","operator":"EQUALS","values":["ANDROID"]}]'`. Add a `DEVICE_TYPE` filter (`PHYSICAL` or `VIRTUAL`) when it matters.
2. Match the exact device name the plan asks for.
3. Take only devices whose `availability` is `HIGHLY_AVAILABLE` or `AVAILABLE`. Skip `BUSY` and `TEMPORARY_NOT_AVAILABLE`.
4. Among several devices with the same name, take the newest OS.
5. For a name that is not on offer, fail and list the names that are on offer in the error.

Before you pay, check which devices accept the app. Create a pool inside the run's project, so it goes away with the project: `aws devicefarm create-device-pool --region us-west-2 --project-arn <project> --name <name> --rules file://pool-rules.json`. The rule's `value` is a string that holds a JSON list, so a file avoids shell escaping:

```json
[{"attribute": "ARN", "operator": "IN", "value": "[\"<device arn 1>\",\"<device arn 2>\"]"}]
```

Then run `aws devicefarm get-device-pool-compatibility --region us-west-2 --device-pool-arn <pool> --app-arn <app upload> --test-type <test type>`, with the test type from the table below. It returns compatible and incompatible devices with the reasons. The docs state no price for this call, so do not tell the person it is free.

## A run that cleans up after itself

Every run creates its own project and deletes it at the end. Write the orchestration in Python with uv and call the AWS CLI directly.

1. **Project:** `aws devicefarm create-project --region us-west-2 --name <project>-batch-<session>-<UTC timestamp>`. The name prefix plays the role of the session tag, so listings find it. Keep its ARN in the orchestrator, not in the tracker, since the ARN holds the account id.
2. **Uploads:** for each file, `aws devicefarm create-upload --region us-west-2 --project-arn <project> --name <file name> --type <type>`. It returns a presigned `url` and the status `INITIALIZED`. Send the bytes with a PUT from the Python orchestrator (`urllib.request.Request(url, data=file_bytes, method="PUT")`), so the presigned URL never appears in a command line or a log. Poll `aws devicefarm get-upload --region us-west-2 --arn <upload>` until the status is `SUCCEEDED`, with a bound such as 15 minutes. A `FAILED` upload gives its reason in `message`. Stop there and fix the package.
3. **Schedule:** `aws devicefarm schedule-run` with:
   - `--region us-west-2 --project-arn <project> --app-arn <app upload> --name <name>`;
   - `--device-selection-configuration '{"filters":[{"attribute":"ARN","operator":"IN","values":["<device arn>"]}],"maxDevices":4}'`, where both `filters` and `maxDevices` are required;
   - `--test '{"type":"INSTRUMENTATION","testPackageArn":"<test upload>"}'`, plus `"testSpecArn"` for a custom environment;
   - `--execution-configuration '{"jobTimeoutMinutes":30}'`, or shorter. The default and the maximum are both 150 minutes, so a hang without this bills up to 150 minutes per device.

   Keep the returned run ARN. If `schedule-run` times out or its answer is lost, run `aws devicefarm list-runs --region us-west-2 --arn <project>` before scheduling again, so the devices are not booked twice.
4. **Wait:** poll `aws devicefarm get-run --region us-west-2 --arn <run>` until the status is `COMPLETED`, with a deadline of about jobs × job timeout. Past the deadline, call `aws devicefarm stop-run --region us-west-2 --arn <run>`. Devices that have not started stop at once and do not bill. Devices that started still finish setup and teardown, and those minutes bill.
5. **Read the result:** the run status is separate from its result. The result is `PASSED`, `WARNED`, `FAILED`, `SKIPPED`, `ERRORED` or `STOPPED`. A `SKIPPED` result with `resultCode` `PARSING_FAILED` means the test package was not parsed and no test ran. Then `list-jobs --arn <run>`, `list-suites --arn <job>` and `list-tests --arn <suite>`, to name every test that did not pass.
6. **Collect:** `aws devicefarm list-artifacts --region us-west-2 --arn <job or test> --type FILE` (also `LOG` and `SCREENSHOT`), for the job and for each failed test, and download them: logs, video and screenshots. Put the artifacts of each failed test in a folder of its own. In practice, a job's files held only the output of its last test, so job-level files alone do not explain earlier failures.
7. **Delete, in a `finally`:** `aws devicefarm delete-project --region us-west-2 --arn <project>`, then `aws devicefarm list-projects --region us-west-2` to prove it is gone. Fail the run if it is not. A project with an active run cannot be deleted, so stop the run first.

## Upload and test types

| Platform | App upload | Test upload | Test type |
| --- | --- | --- | --- |
| Android | `ANDROID_APP` (`.apk`) | `INSTRUMENTATION_TEST_PACKAGE` (`.apk`) | `INSTRUMENTATION` |
| iOS | `IOS_APP` (`.ipa`) | `XCTEST_UI_TEST_PACKAGE` | `XCTEST_UI` |

iOS details:

- The app goes as an IPA: a zip with the `.app` under `Payload/`. The UI test runner goes as its own IPA with `Payload/<name>UITests-Runner.app`, or as a `.zip` holding the runner and an `.xctestrun` file, with no `Payload` folder inside.
- Build both for a generic iOS device: `xcodebuild build-for-testing -scheme <scheme> -sdk iphoneos -destination "generic/platform=iOS"`, signed with the person's own development team.
- Device Farm re-signs device builds with its own profile, which removes entitlements such as App Groups, Associated Domains, Push Notifications and In-App Purchase. A test that needs one of them cannot pass there.
- iOS simulators on Device Farm need an `.ipa` or `.zip` with an arm64 simulator build, and they always bill as metered.

## Custom test environment, for full control

The custom environment runs a YAML test spec (`version: 0.1`, phases `install`, `pre_test`, `test`, `post_test`, then `artifacts`) on a host that reaches the device:

- The host reaches the device with `adb -s "$DEVICEFARM_DEVICE_UDID"`. `$DEVICEFARM_APP_PATH` and `$DEVICEFARM_TEST_PACKAGE_PATH` point at the uploads.
- Everything the script writes into `$DEVICEFARM_LOG_DIR` is kept as a zipped artifact, up to 1 GB in total.
- A non-zero exit in `test` marks the test failed. `post_test` runs either way, so collect logs there.
- Hosts seen on 2026-11-26: `amazon_linux_2023` and `amazon_linux_2` for Android, set with `android_test_host`, and `macos_tahoe` and `macos_sequoia` for iOS, set with `ios_test_host`. Pick one on purpose instead of an old default.
- The host's `adb` refused `logcat -v raw` in practice. Use another format, such as `logcat -v threadtime`.

Use it to start an app with launch arguments in an intent extra, run an "every test" mode of the app and collect logcat into the log folder. The standard environment reports each test case. The custom environment reports per-test results only through its "test insights" option, which works on the `macos_sequoia` iOS host and later. Choose with that in mind.

## Credentials

The AWS CLI reads the batch user's keys from the environment only (see [controller setup](controller-setup.md)). The IAM policy needs only the Device Farm actions the run uses. Presigned upload URLs and artifact URLs are secrets for their lifetime, so keep them out of logs, trackers and chat.

## Sources

Checked on 2026-11-26: [Device Farm developer guide](https://docs.aws.amazon.com/devicefarm/latest/developerguide/welcome.html), [endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/devicefarm.html), [pricing](https://aws.amazon.com/device-farm/pricing/), [create a run](https://docs.aws.amazon.com/devicefarm/latest/developerguide/how-to-create-test-run.html), [schedule-run](https://docs.aws.amazon.com/cli/latest/reference/devicefarm/schedule-run.html), [Upload](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_Upload.html), [Run](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_Run.html), [StopRun](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_StopRun.html), [ListDevices](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ListDevices.html), [XCTest UI](https://docs.aws.amazon.com/devicefarm/latest/developerguide/test-types-ios-xctest-ui.html), [custom environment hosts](https://docs.aws.amazon.com/devicefarm/latest/developerguide/custom-test-environments-hosts.html) and [custom environment variables](https://docs.aws.amazon.com/devicefarm/latest/developerguide/custom-test-environment-variables.html). The device models and hardware limits come from practice. See [sources](sources.md) for the full record.
