# Sources, applicability and authoring evidence

Research baseline: **2026-11-05**. Sources below were inspected for the stated decision. Stored guidance changes only when the user requests maintenance. No collected manuals, generated API archives, execution helpers or autonomous updates are included.

## Frameworks and professional testing foundations

| Source | Decision supported |
| --- | --- |
| [Apple testing overview](https://developer.apple.com/documentation/xcode/testing) and its [official Markdown body](https://developer.apple.com/documentation/xcode/testing.md) | Combine focused unit, integration, supported UI and performance evidence |
| [XCUIAutomation](https://developer.apple.com/documentation/xcuiautomation) and [Markdown body](https://developer.apple.com/documentation/xcuiautomation.md) | XCTest UI role and the explicit native visionOS SDK exclusion, while compatible iOS SDK apps can be tested in visionOS |
| [UI recording](https://developer.apple.com/documentation/xcuiautomation/recording-ui-automation-for-testing) and [Markdown body](https://developer.apple.com/documentation/xcuiautomation/recording-ui-automation-for-testing.md) | Review queries, Accessibility authorization and the need for assertions beyond replay |
| [Running tests/results](https://developer.apple.com/documentation/xcode/running-tests-and-interpreting-results) and [Markdown body](https://developer.apple.com/documentation/xcode/running-tests-and-interpreting-results.md) | Plan/scheme execution, filtered runs and different result states |
| [WWDC25 UI automation session](https://developer.apple.com/videos/play/wwdc2025/344/) | Inspected transcript sections on platform coverage, identifiers and hardware inputs. “Designed for iPad” is a consequential visionOS qualification |
| [ISTQB CTFL v4.0.1 syllabus](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf), selected sections 4.2 and 5.5 | Partition/boundary/condition/state cases and actionable defect evidence. This skill applies these ideas independently, not as copied training material or certification |
| Adam Bender, [Testing Overview](https://abseil.io/resources/swe-book/html/ch11.html), in *Software Engineering at Google* | Match scope and resources to fast, useful feedback |
| Joseph Graves, [Larger Testing](https://abseil.io/resources/swe-book/html/ch14.html), in *Software Engineering at Google* | Balance integration fidelity, setup dependencies, repeatability and diagnosis |

Selected public chapters, relevant transcript sections and syllabus sections were inspected. No claim is made that a complete commercial book or every linked platform manual was read. The worked product examples are original illustrative acceptance rules, not observed results from an actual app.

## Mac, simulators and platform interaction

| Official source | Decision supported |
| --- | --- |
| [Xcode system requirements](https://developer.apple.com/xcode/system-requirements) | Separate host, SDK, deployment, physical-device and simulator ranges. visionOS development requires Apple silicon |
| [Xcode command-line reference](https://developer.apple.com/documentation/xcode/xcode-command-line-tool-reference) | Use the selected full Xcode's native tool help/manual instead of invented wrappers |
| [Device Hub](https://developer.apple.com/documentation/xcode/device-hub) | Current integrated device/simulator management and execution surface |
| [Manage devices](https://developer.apple.com/documentation/xcode/managing-your-simulated-and-physical-devices-in-device-hub) and [Markdown body](https://developer.apple.com/documentation/xcode/managing-your-simulated-and-physical-devices-in-device-hub.md) | Runtime creation, pairing/trust, Watch companion and current wireless prerequisites |
| [Simulated-device environment](https://developer.apple.com/documentation/xcode/configuring-the-environment-of-a-simulated-device) and [Markdown body](https://developer.apple.com/documentation/xcode/configuring-the-environment-of-a-simulated-device.md) | Appearance/text/environment, canvas versus logical size and restart versus erase |
| [visionOS interaction in Device Hub](https://developer.apple.com/documentation/xcode/interacting-with-your-visionos-app-in-device-hub) and [Markdown body](https://developer.apple.com/documentation/xcode/interacting-with-your-visionos-app-in-device-hub.md) | Simulated pointer/gaze, pinch/drag, viewpoint and room settings with physical acceptance kept separate |
| [watchOS test setup](https://developer.apple.com/documentation/watchos-apps/setting-up-tests-for-your-watchos-app) and [Markdown body](https://developer.apple.com/documentation/watchos-apps/setting-up-tests-for-your-watchos-app.md) | Watch unit/UI target support. Historical WatchKit target names are not imposed on a current project's architecture |
| [XCUIRemote](https://developer.apple.com/documentation/xcuiautomation/xcuiremote) and [Markdown body](https://developer.apple.com/documentation/xcuiautomation/xcuiremote.md) | Actual tvOS remote button and press-and-hold interface |
| [macOS virtualization on Apple silicon](https://developer.apple.com/documentation/virtualization/running-macos-in-a-virtual-machine-on-apple-silicon) | Controlled guest OS testing is distinct from mobile simulation and physical hardware coverage |
| [Accessibility audits](https://developer.apple.com/documentation/accessibility/performing-accessibility-audits-for-your-app) and [Markdown body](https://developer.apple.com/documentation/accessibility/performing-accessibility-audits-for-your-app.md) | Screen/platform-specific checks plus assistive-technology testing, without a full-accessibility guarantee |
| [Performance tests](https://developer.apple.com/documentation/xcode/writing-and-running-performance-tests) and [Markdown body](https://developer.apple.com/documentation/xcode/writing-and-running-performance-tests.md) | Release-like metric conditions, separate diagnostics and baseline interpretation |
| [StoreKit test setup](https://developer.apple.com/documentation/xcode/setting-up-storekit-testing-in-xcode) and [Markdown body](https://developer.apple.com/documentation/xcode/setting-up-storekit-testing-in-xcode.md) | Local configuration/transactions differ from App Store sandbox and production evidence |

## Cloud contracts

| Official source | Decision supported |
| --- | --- |
| [First Xcode Cloud workflow](https://developer.apple.com/documentation/xcode/configuring-your-first-xcode-cloud-workflow) and [Markdown body](https://developer.apple.com/documentation/xcode/configuring-your-first-xcode-cloud-workflow.md) | Onboarding, selected products/environment and result artifacts |
| [Xcode Cloud actions](https://developer.apple.com/documentation/xcode/configuring-your-xcode-cloud-workflow-s-actions) and [Markdown body](https://developer.apple.com/documentation/xcode/configuring-your-xcode-cloud-workflow-s-actions.md) | Required test action, two build/run phases and source unavailable during the run phase |
| [Xcode Cloud release notes](https://developer.apple.com/xcode-cloud/release-notes/) and [CiAction schema](https://developer.apple.com/documentation/appstoreconnectapi/ciaction) | Distinguish historical known issues and schema values from actually available action destinations |
| [AWS XCTest UI integration](https://docs.aws.amazon.com/devicefarm/latest/developerguide/test-types-ios-xctest-ui.html) | Application versus runner packages and the different IPA/ZIP layouts |
| [AWS iOS hosts](https://docs.aws.amazon.com/devicefarm/latest/developerguide/custom-test-environments-hosts-ios.html) | Explicit supported host selection, avoiding an implicit legacy host |
| [AWS run creation](https://docs.aws.amazon.com/devicefarm/latest/developerguide/how-to-create-test-run.html), [CreateUpload](https://docs.aws.amazon.com/cli/latest/reference/devicefarm/create-upload.html) and [ScheduleRun](https://docs.aws.amazon.com/cli/latest/reference/devicefarm/schedule-run.html) | Upload transfer/processing, typed packages, test specification and run identity |
| [AWS endpoints](https://docs.aws.amazon.com/general/latest/gr/devicefarm.html), [remote access](https://docs.aws.amazon.com/devicefarm/latest/developerguide/remote-access.html) and [managed Appium endpoint](https://docs.aws.amazon.com/devicefarm/latest/developerguide/appium-endpoint-interaction.html) | Regional mobile service, interactive sessions and remote artifact handling |
| [EC2 Mac](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-mac-instances.html) | Mac infrastructure versus device lab, compatible host selection and minimum Dedicated Host allocation period |
| [Developer Device Platform setup](https://docs.cloud.google.com/developer-device-platform/quickstart), [iOS XCTest guide](https://docs.cloud.google.com/developer-device-platform/device-run/ios) and [alpha CLI](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/device-run/sessions/submit/xctest) | Preview scope, signed device products, ZIP root layout, iOS command surface and result/session lifecycle |
| [Firebase Test Lab migration](https://firebase.google.com/docs/test-lab/migrate) and [existing iOS XCTest guide](https://firebase.google.com/docs/test-lab/ios/run-xctest) | Announced shutdown and explicit migration instead of a permanent new dependency |
| [Azure Xcode pipelines](https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/xcode?view=azure-devops) | macOS CI orchestration and actual build versus test configuration. Historical sample Xcode numbers are not current requirements |
| [App Center retirement](https://learn.microsoft.com/en-us/appcenter/retirement) | Retired Test product is separate from extended Analytics/Diagnostics, with BrowserStack migration guidance |
| [BrowserStack App Live](https://www.browserstack.com/docs/app-live) | Interactive iOS mobile product, without inferring native Mac or accessory coverage |

## Access limits, conflicts and local verification

Availability check on 2026-11-05: the Developer Device Platform overview still labels
iOS forthcoming, while the dedicated iOS guide and alpha CLI document execution. Treat actual project
access and returned device availability as prerequisites. Neither page establishes a successful run.

Apple's JavaScript documentation frontends did not expose substantive text through the web reader. The official `.md` bodies linked above were retrieved directly and read where used. Older guessed article paths returned errors and were not used as evidence. Only the successful current destinations support the guide. Microsoft articles displayed authorization banners but exposed the substantive public article.

The live Google iOS alpha CLI reference was readable. A beta iOS result appeared in search indexing but its live reference returned 404. The skill follows the actual iOS guide/alpha reference and does not silently borrow Android's beta command. Xcode Cloud's historical visionOS issue and a schema enum do not establish an independently verified current runtime destination.

Local `xcodebuild -version` reported **Xcode 27.2 (27B52)**. Native `xcodebuild -help` and `xcresulttool` help confirmed the documented plan/destination/result options and modern summary/attachment commands. A `simctl help` attempt could not connect to CoreSimulator under the execution sandbox. It was not used to claim available runtimes, working simulator interaction or application execution.

No app source, test bundle, real device or provider account was exercised during authoring. No paid session, pairing change, cloud setup, purchase or release was performed. Structural validation and editorial case inspection do not certify an application, spatial comfort, hardware performance or complete provider availability.

## Native-screen and display procedure verification

Checked **2026-11-05** with installed Xcode **27.2** `simctl help io` and the previously exercised
native UI/capture workflow. [XCUIAutomation](https://developer.apple.com/documentation/xcuiautomation)
and [XCUIApplication](https://developer.apple.com/documentation/xcuiautomation/xcuiapplication) govern
the external-app native runner. Activation, control existence/hittability and genuine transactions
are separate evidence. The new Swift example is a worked fixture, not a newly executed test run.

Display enumeration and screenshot selection were confirmed from native help. Specific Duo screen
IDs and host-window behavior are observed environment details. Discover them for the actual runtime.
This revision did not boot/reset a device, change macOS privacy settings or rerun a store transaction.
