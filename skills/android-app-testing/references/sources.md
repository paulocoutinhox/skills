# Sources, applicability and research limits

Verified **2026-11-05** against the official public material linked below. Dates identify this editorial research, not a promise of permanent service availability. Only user-requested maintenance changes stored facts. No collector, executable suite, generated provider schema or automatic refresh is included.

## Test design and professional foundations

| Source inspected | Decision supported |
| --- | --- |
| [Android testing strategies](https://developer.android.com/training/testing/fundamentals/strategies) | Select test scope and fidelity by risk instead of putting every check into a slow device journey |
| [ISTQB CTFL syllabus v4.0.1](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf), selected sections 4.2 and 5.5 | Derive partitions/boundaries/interacting conditions and report reproducible defects. This skill is an original practical application, not a certification course or reproduction of the syllabus |
| Adam Bender, [Testing Overview](https://abseil.io/resources/swe-book/html/ch11.html), in *Software Engineering at Google* | Keep fast feedback, test intent and meaningful outcomes visible |
| Joseph Graves, [Larger Testing](https://abseil.io/resources/swe-book/html/ch14.html), in *Software Engineering at Google* | Balance integration fidelity against setup complexity, environmental dependencies and failure diagnosis |

Only the cited public chapters and selected syllabus sections were inspected for these principles. The examples are illustrative product contracts, not claims that a particular app or model was exercised.

## Host, emulator and execution contracts

| Official source | Applied knowledge |
| --- | --- |
| [Install Android Studio](https://developer.android.com/studio/install) | Host support, architecture and actual workstation requirements. Windows/Linux ARM exclusions refer to this Studio distribution, not every cloud ARM environment |
| [Emulator acceleration](https://developer.android.com/studio/run/emulator-acceleration) | WHPX, Hypervisor.Framework, KVM, image/host matching and AEHD's announced sunset |
| [Manage AVDs](https://developer.android.com/studio/run/managing-avds) | Device Manager workflow, hardware/image properties and Google APIs versus Play Store images |
| [Android CLI](https://developer.android.com/tools/agents) and [SDK command](https://developer.android.com/tools/agents/android-cli/commands/sdk) | Current native management surface and slash-delimited package names |
| [SDK manager notice](https://developer.android.com/tools/sdkmanager), [AVD manager notice](https://developer.android.com/tools/avdmanager) and [emulator management notice](https://developer.android.com/studio/run/emulator-commandline) | Deprecation notices explicitly direct new management to Android CLI. The acceleration guide still documents the runtime's diagnostic flag |
| [Create an emulator](https://developer.android.com/tools/agents/android-cli/commands/emulator_create) and [start it](https://developer.android.com/tools/agents/android-cli/commands/emulator_start) | Real profile enumeration, listed device names, cold/headless startup and ready-return behavior |
| [ADB](https://developer.android.com/tools/adb) and [physical device setup](https://developer.android.com/studio/run/device) | Device selection, install/diagnostic surfaces and USB authorization/host setup |
| [Emulator network address space](https://developer.android.com/studio/run/emulator-networking-address) | Emulator-specific host-loopback alias and network boundaries |
| [Command-line testing](https://developer.android.com/studio/test/command-line) | Actual Gradle test/build distinction, module/variant tasks and report locations |
| [Build-managed devices](https://developer.android.com/studio/test/managed-devices) | Configured device lifecycle/tasks and virtualization prerequisites. The researched managed-device feature starts at API 27, not every possible application minimum SDK |

## UI, accessibility, lifecycle and performance

| Official source | Applied knowledge |
| --- | --- |
| [Compose testing APIs](https://developer.android.com/develop/ui/compose/testing/apis) | Semantic selection, actions and assertions |
| [Compose synchronization](https://developer.android.com/develop/ui/compose/testing/synchronization) | Test-clock/idle behavior and asynchronous boundaries |
| [Compose common testing patterns](https://developer.android.com/develop/ui/compose/testing/common-patterns) | Component saved-state tests and scoped configuration overrides |
| [Espresso](https://developer.android.com/training/testing/espresso) and [idling resources](https://developer.android.com/training/testing/espresso/idling-resource) | View interactions and synchronization of relevant asynchronous work |
| [Modern UI Automator](https://developer.android.com/training/testing/other-components/ui-automator) | System/cross-app interaction and the 2.4 API's under-development status |
| [Appium quickstart](https://appium.io/docs/en/latest/quickstart/) and [UiAutomator2 driver](https://github.com/appium/appium-uiautomator2-driver) | Server/driver/client separation, host support, capabilities and explicit compatibility selection |
| [Android input](https://developer.android.com/tools/agents/android-cli/commands/input), [text](https://developer.android.com/tools/agents/android-cli/commands/input_text) and [capture](https://developer.android.com/tools/agents/android-cli/commands/screen_capture) | Native exploration, selector-based text replacement and device-specific PNG output |
| [Save UI state](https://developer.android.com/topic/libraries/architecture/saving-states) | Different state lifetimes and restoration responsibilities |
| [Screen/window testing](https://developer.android.com/training/testing/different-screens) | Real layout/configuration transitions and distinction between visual and behavior tests |
| [Accessibility testing](https://developer.android.com/guide/topics/ui/accessibility/testing) | Combine assistive-technology use with available automated checks |
| [Macrobenchmark](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview) | Release-like measured target, appropriate physical hardware and honest measurement conditions |

Native AndroidX UI Automator and Appium's UiAutomator2 driver have separate versioning and execution contracts. Do not infer compatibility from similar names. The Appium repository's current top-level compatibility notice and older retained README wording differ. Inspect the actual chosen release's contract instead of taking the first version number from a search excerpt.

## Cloud services

| Official source | Applied knowledge |
| --- | --- |
| [AWS service endpoints/quotas](https://docs.aws.amazon.com/general/latest/gr/devicefarm.html) | Device Farm's researched mobile region and finite service limits |
| [Create a Device Farm run](https://docs.aws.amazon.com/devicefarm/latest/developerguide/how-to-create-test-run.html) | Project → upload record → byte transfer/processing → schedule → inspect |
| [CreateUpload CLI](https://docs.aws.amazon.com/cli/latest/reference/devicefarm/create-upload.html), [ScheduleRun CLI](https://docs.aws.amazon.com/cli/latest/reference/devicefarm/schedule-run.html), [GetRun CLI](https://docs.aws.amazon.com/cli/latest/reference/devicefarm/get-run.html) and [ListArtifacts CLI](https://docs.aws.amazon.com/cli/latest/reference/devicefarm/list-artifacts.html) | Actual identifiers, test types, lifecycle/result separation and evidence retrieval |
| [Custom environments](https://docs.aws.amazon.com/devicefarm/latest/developerguide/custom-test-environments.html), [Appium environments](https://docs.aws.amazon.com/devicefarm/latest/developerguide/test-types-appium.html) and [instrumentation](https://docs.aws.amazon.com/devicefarm/latest/developerguide/test-types-android-instrumentation.html) | Selected host/software and test discovery. Old framework-index wording is not a universal Appium version rule |
| [Remote access](https://docs.aws.amazon.com/devicefarm/latest/developerguide/remote-access.html) and [managed Appium endpoint](https://docs.aws.amazon.com/devicefarm/latest/developerguide/appium-endpoint-interaction.html) | Interactive devices, remote artifact location and session cleanup |
| [Developer Device Platform quickstart](https://docs.cloud.google.com/developer-device-platform/quickstart) | Billing, APIs, identity and setup requirements during Preview |
| [Device Run](https://docs.cloud.google.com/developer-device-platform/device-run), [device catalog](https://docs.cloud.google.com/developer-device-platform/device-catalog), [Android instrumentation](https://docs.cloud.google.com/developer-device-platform/device-run/android-instrument) and [results](https://docs.cloud.google.com/developer-device-platform/device-run/find-logs) | Actual submission, device IDs, attempts, orchestration and Cloud Storage evidence |
| [Test Lab deprecation notice](https://firebase.google.com/docs/test-lab/migrate), [FAQ](https://firebase.google.com/docs/test-lab/migrate-faq) and [command translation](https://docs.cloud.google.com/developer-device-platform/migrate/flag-command-translation) | September 30, 2027 shutdown, surviving Device Streaming and nonequivalent migration flags/features |
| [Existing Test Lab CLI](https://firebase.google.com/docs/test-lab/android/command-line), [Robo](https://firebase.google.com/docs/test-lab/android/robo-ux-test) and [quotas/billing](https://firebase.google.com/docs/test-lab/usage-quotas-pricing) | Existing test types, exploratory limits, synthetic sign-in and budget-alert semantics |
| [Device Streaming in Studio](https://developer.android.com/studio/run/android-device-streaming) | Interactive remote physical devices and explicit session lifecycle |
| [Developer Device Platform billing](https://docs.cloud.google.com/developer-device-platform/pricing) | Current plan verification instead of copying another product's allowance |
| [Play pre-launch report](https://support.google.com/googleplay/android-developer/answer/9844487?hl=en) | Additional release-adjacent evidence with explicitly incomplete coverage |
| [App Center retirement](https://learn.microsoft.com/en-us/appcenter/retirement) | Test retirement date and Microsoft-recommended device-testing migration |
| [Azure Android pipelines](https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/android?view=azure-devops) | Build/test orchestration, hosted macOS emulator guidance and hosted Ubuntu acceleration limitation |
| [BrowserStack App Live](https://www.browserstack.com/docs/app-live) and [Local Testing](https://www.browserstack.com/docs/local-testing/overview) | Interactive product and documented private-backend connection. App Automate is identified by Microsoft's migration recommendation |

## Access and verification limits

Some older Android/AWS URLs redirected or returned no readable body. They were not used as evidence of current behavior. The linked current destinations above supplied the relevant contracts. Microsoft pages displayed an authorization banner while still exposing the substantive public article, which was read.

No provider account, billing configuration, emulator, physical device, real APK or application suite was exercised during authoring. Commands are researched native-tool examples with explicit placeholders, not recorded successful runs. No paid service is described as configured or universally available. Preview features, account-specific capabilities, actual network access and app-specific acceptance rules remain operational prerequisites.

## Exact-release and isolated-device verification

Checked **2026-11-05** against [bundletool](https://developer.android.com/tools/bundletool),
[emulator runtime options](https://developer.android.com/studio/run/emulator-commandline) and
[Play Billing testing](https://developer.android.com/google/play/billing/test). These govern AAB-to-APK
provenance, explicit APK signing, writable-disk/snapshot choices and suitable store test accounts.
Local upload signing and Play-distributed app signing can differ. License testers can use permitted
sideload testing paths, while ordinary test-track purchases can still charge real money.

The procedure distinguishes release UI smoke checks from genuine purchase evidence. This authoring
pass researched commands and reviewed the prior workflow without creating a new emulator or executing
another billing transaction. Runtime disk overrides are advanced operations on an inspected installed
runtime, not a replacement recommendation for deprecated device-management tooling.
