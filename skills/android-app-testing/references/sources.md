# Sources, applicability and research limits

Checked **2026-11-05** against the official public material linked below. The dates mark this editorial research. They do not promise the services will always be available. Only maintenance the user asks for changes stored facts. No collector, runnable suite, generated provider schema or automatic refresh is included.

## Test design and professional foundations

| Source inspected | Decision supported |
| --- | --- |
| [Android testing strategies](https://developer.android.com/training/testing/fundamentals/strategies) | Choose test scope and how close to real it is by risk, instead of putting every check into a slow device journey |
| [ISTQB CTFL syllabus v4.0.1](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf), selected sections 4.2 and 5.5 | Find partitions/boundaries/conditions that affect each other, and report bugs others can reproduce. This skill is an original practical use, not a certification course or a copy of the syllabus |
| Adam Bender, [Testing Overview](https://abseil.io/resources/swe-book/html/ch11.html), in *Software Engineering at Google* | Keep fast feedback, test intent and meaningful outcomes visible |
| Joseph Graves, [Larger Testing](https://abseil.io/resources/swe-book/html/ch14.html), in *Software Engineering at Google* | Balance how real an integration is against setup complexity, environment dependencies and failure diagnosis |

Only the cited public chapters and selected syllabus sections were checked for these principles. The examples are sample product contracts, not claims that a specific app or model was tested.

## Host, emulator and execution contracts

| Official source | Applied knowledge |
| --- | --- |
| [Install Android Studio](https://developer.android.com/studio/install) | Host support, architecture and real workstation requirements. Windows/Linux ARM exclusions refer to this Studio distribution, not every cloud ARM environment |
| [Emulator acceleration](https://developer.android.com/studio/run/emulator-acceleration) | WHPX, Hypervisor.Framework, KVM, image/host matching and AEHD's announced end date |
| [Manage AVDs](https://developer.android.com/studio/run/managing-avds) | Device Manager workflow, hardware/image properties and Google APIs versus Play Store images |
| [Android CLI](https://developer.android.com/tools/agents) and [SDK command](https://developer.android.com/tools/agents/android-cli/commands/sdk) | Current native management surface and slash-delimited package names |
| [SDK manager notice](https://developer.android.com/tools/sdkmanager), [AVD manager notice](https://developer.android.com/tools/avdmanager) and [emulator management notice](https://developer.android.com/studio/run/emulator-commandline) | Deprecation notices clearly point new management to Android CLI. The acceleration guide still documents the runtime's diagnostic flag |
| [Create an emulator](https://developer.android.com/tools/agents/android-cli/commands/emulator_create) and [start it](https://developer.android.com/tools/agents/android-cli/commands/emulator_start) | Real profile listing, listed device names, cold/headless startup and return-when-ready behavior |
| [ADB](https://developer.android.com/tools/adb) and [physical device setup](https://developer.android.com/studio/run/device) | Device selection, install/diagnostic surfaces and USB approval/host setup |
| [Emulator network address space](https://developer.android.com/studio/run/emulator-networking-address) | Emulator-specific host-loopback alias and network limits |
| [Command-line testing](https://developer.android.com/studio/test/command-line) | Real Gradle test/build difference, module/variant tasks and report locations |
| [Build-managed devices](https://developer.android.com/studio/test/managed-devices) | Configured device lifecycle/tasks and virtualization requirements. The researched managed-device feature starts at API 27, not every possible app minimum SDK |

## UI, accessibility, lifecycle and performance

| Official source | Applied knowledge |
| --- | --- |
| [Compose testing APIs](https://developer.android.com/develop/ui/compose/testing/apis) | Semantic selection, actions and assertions |
| [Compose synchronization](https://developer.android.com/develop/ui/compose/testing/synchronization) | Test-clock/idle behavior and async limits |
| [Compose common testing patterns](https://developer.android.com/develop/ui/compose/testing/common-patterns) | Component saved-state tests and scoped configuration overrides |
| [Espresso](https://developer.android.com/training/testing/espresso) and [idling resources](https://developer.android.com/training/testing/espresso/idling-resource) | View interactions and syncing the async work that matters |
| [Modern UI Automator](https://developer.android.com/training/testing/other-components/ui-automator) | System/cross-app interaction and the 2.4 API's in-development status |
| [Appium quickstart](https://appium.io/docs/en/latest/quickstart/) and [UiAutomator2 driver](https://github.com/appium/appium-uiautomator2-driver) | Server/driver/client separation, host support, capabilities and explicit compatibility choice |
| [Android input](https://developer.android.com/tools/agents/android-cli/commands/input), [text](https://developer.android.com/tools/agents/android-cli/commands/input_text) and [capture](https://developer.android.com/tools/agents/android-cli/commands/screen_capture) | Native exploration, selector-based text replacement and device-specific PNG output |
| [Save UI state](https://developer.android.com/topic/libraries/architecture/saving-states) | Different state lifetimes and who restores what |
| [Screen/window testing](https://developer.android.com/training/testing/different-screens) | Real layout/configuration changes and the difference between visual and behavior tests |
| [Accessibility testing](https://developer.android.com/guide/topics/ui/accessibility/testing) | Combine assistive-technology use with available automated checks |
| [Macrobenchmark](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview) | Release-like measured target, suitable physical hardware and honest measurement conditions |

Native AndroidX UI Automator and Appium's UiAutomator2 driver have separate versioning and run contracts. Do not assume compatibility from similar names. The Appium repository's current top-level compatibility notice and older kept README wording differ. Check the real chosen release's contract instead of taking the first version number from a search excerpt.

## Cloud services

| Official source | Applied knowledge |
| --- | --- |
| [AWS service endpoints/quotas](https://docs.aws.amazon.com/general/latest/gr/devicefarm.html) | Device Farm's researched mobile region and fixed service limits |
| [Create a Device Farm run](https://docs.aws.amazon.com/devicefarm/latest/developerguide/how-to-create-test-run.html) | Project → upload record → byte transfer/processing → schedule → inspect |
| [CreateUpload CLI](https://docs.aws.amazon.com/cli/latest/reference/devicefarm/create-upload.html), [ScheduleRun CLI](https://docs.aws.amazon.com/cli/latest/reference/devicefarm/schedule-run.html), [GetRun CLI](https://docs.aws.amazon.com/cli/latest/reference/devicefarm/get-run.html) and [ListArtifacts CLI](https://docs.aws.amazon.com/cli/latest/reference/devicefarm/list-artifacts.html) | Real identifiers, test types, lifecycle/result separation and getting evidence |
| [Custom environments](https://docs.aws.amazon.com/devicefarm/latest/developerguide/custom-test-environments.html), [Appium environments](https://docs.aws.amazon.com/devicefarm/latest/developerguide/test-types-appium.html) and [instrumentation](https://docs.aws.amazon.com/devicefarm/latest/developerguide/test-types-android-instrumentation.html) | Chosen host/software and test discovery. Old framework-index wording is not a universal Appium version rule |
| [Remote access](https://docs.aws.amazon.com/devicefarm/latest/developerguide/remote-access.html) and [managed Appium endpoint](https://docs.aws.amazon.com/devicefarm/latest/developerguide/appium-endpoint-interaction.html) | Interactive devices, remote artifact location and session cleanup |
| [Developer Device Platform quickstart](https://docs.cloud.google.com/developer-device-platform/quickstart) | Billing, APIs, identity and setup requirements during Preview |
| [Device Run](https://docs.cloud.google.com/developer-device-platform/device-run), [device catalog](https://docs.cloud.google.com/developer-device-platform/device-catalog), [Android instrumentation](https://docs.cloud.google.com/developer-device-platform/device-run/android-instrument) and [results](https://docs.cloud.google.com/developer-device-platform/device-run/find-logs) | Real submission, device IDs, attempts, orchestration and Cloud Storage evidence |
| [Test Lab deprecation notice](https://firebase.google.com/docs/test-lab/migrate) and [FAQ](https://firebase.google.com/docs/test-lab/migrate-faq) | September 30, 2027 shutdown and Device Streaming staying available |
| [Device Streaming in Studio](https://developer.android.com/studio/run/android-device-streaming) | Interactive remote physical devices and explicit session lifecycle |
| [Developer Device Platform billing](https://docs.cloud.google.com/developer-device-platform/pricing) | Check the current plan instead of copying another product's allowance |
| [Play pre-launch report](https://support.google.com/googleplay/android-developer/answer/9844487?hl=en) | Extra release-adjacent evidence with clearly incomplete coverage |
| [App Center retirement](https://learn.microsoft.com/en-us/appcenter/retirement) | Test retirement date. The page names BrowserStack App Automate for device testing |
| [Azure Android pipelines](https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/android?view=azure-devops) | Build/test orchestration, hosted macOS emulator guidance and hosted Ubuntu acceleration limit |
| [BrowserStack App Live](https://www.browserstack.com/docs/app-live) and [Local Testing](https://www.browserstack.com/docs/local-testing/overview) | Interactive product and documented private-backend connection |

## Access and verification limits

Some older Android/AWS URLs redirected or returned no readable body. They were not used as evidence of current behavior. The current linked pages above gave the contracts that matter. Microsoft pages showed a sign-in banner but still showed the full public article, which was read.

No provider account, billing setup, emulator, physical device, real APK or app suite was used while writing. Commands are researched native-tool examples with clear placeholders, not recorded successful runs. No paid service is described as set up or as available everywhere. Preview features, account-specific capabilities, real network access and app-specific acceptance rules are still requirements before a run.

## Exact-release and isolated-device verification

Checked **2026-11-05** against [bundletool](https://developer.android.com/tools/bundletool),
[emulator runtime options](https://developer.android.com/studio/run/emulator-commandline) and
[Play Billing testing](https://developer.android.com/google/play/billing/test). These set the rules for
AAB-to-APK origin, explicit APK signing, writable-disk/snapshot choices and suitable store test accounts.
Local upload signing and Play-distributed app signing can differ. License testers can use allowed
sideload testing paths, while ordinary test-track purchases can still charge real money.

The procedure keeps release UI smoke checks apart from real purchase evidence. The research
checked commands without creating an emulator or running a billing transaction. Runtime disk
overrides are advanced options of a checked installed runtime. AVD creation and management go
through Device Manager or `android emulator`.

## Command details rechecked

Checked **2026-11-18** against [ADB](https://developer.android.com/tools/adb) for `install -r`, `am start -W -n`, `am kill` and the `screencap`/`pull` sequence, [build-managed devices](https://developer.android.com/studio/test/managed-devices) for device and group task names, [Android CLI input](https://developer.android.com/tools/agents/android-cli/commands/input) for `--match` behavior, substring and slash-delimited regular-expression selectors and `android layout`, [Device Run Android instrumentation](https://docs.cloud.google.com/developer-device-platform/device-run/android-instrument) for `--apps`, the timeout range and what total attempts per job/shard means, [Create a Device Farm run](https://docs.aws.amazon.com/devicefarm/latest/developerguide/how-to-create-test-run.html) for `curl -T` upload transfer and downloading the default test specification, and [StopRun CLI](https://docs.aws.amazon.com/cli/latest/reference/devicefarm/stop-run.html) for how stopping is billed, result values and `PARSING_FAILED`. These are documentation checks, not device or provider runs.

## Deprecation and provider notices rechecked

Checked **2026-11-18**. The [SDK manager page](https://developer.android.com/tools/sdkmanager) says that `sdkmanager` is deprecated in favor of `android sdk`. The [AVD manager page](https://developer.android.com/tools/avdmanager) points AVD creation to `android emulator`. The [emulator command-line page](https://developer.android.com/studio/run/emulator-commandline) says that the `emulator` tool is deprecated in favor of `android emulator` and documents runtime options such as `-data`, `-cache`, `-no-snapshot` and `-accel-check`. The [emulator create](https://developer.android.com/tools/agents/android-cli/commands/emulator_create), [emulator start](https://developer.android.com/tools/agents/android-cli/commands/emulator_start), [screen capture](https://developer.android.com/tools/agents/android-cli/commands/screen_capture) and [input text](https://developer.android.com/tools/agents/android-cli/commands/input_text) references confirm the profile, `--cold`/`--headless`, `--output`/`--annotate`, `--match`/`--wait` and escaped regular-expression selector syntax used here.

The [Firebase release notes](https://firebase.google.com/support/releases) place the Test Lab deprecation entry under September 30, 2026, and the [deprecation page](https://firebase.google.com/docs/test-lab/migrate) and [FAQ](https://firebase.google.com/docs/test-lab/migrate-faq) give the September 30, 2027 shutdown and continued Android Device Streaming support. The [Developer Device Platform release notes](https://docs.cloud.google.com/developer-device-platform/release-notes) describe the platform as Preview. The [Azure Android pipeline guide](https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/android?view=azure-devops) says that Microsoft-hosted emulator tests should use the macOS image because hosted Ubuntu agents do not support the needed hardware acceleration. The [App Center retirement page](https://learn.microsoft.com/en-us/appcenter/retirement) confirms the March 31, 2025 retirement. The [CreateUpload API reference](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_CreateUpload.html) lists `INSTRUMENTATION_TEST_SPEC`, `INSTRUMENTATION_TEST_PACKAGE` and `APPIUM_PYTHON_TEST_PACKAGE`. These are documentation checks, not test runs.
