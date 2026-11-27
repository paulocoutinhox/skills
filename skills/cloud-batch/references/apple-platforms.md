# Apple platforms: simulators, devices, macOS and Mac Catalyst

Read this for iOS, iPadOS, tvOS and visionOS simulators, Apple devices reached from a Mac, and macOS or Mac Catalyst UI tests. Follow [device testing](device-testing.md) first. Commands and API names were checked on **2026-11-26** against the help text, man pages and SDK headers of Xcode 27.2. The behavior notes come from real runs, and the sources say which is which.

## Run UI tests on a simulator

1. Pick a simulator that already exists, has no apps of other projects, and belongs to this line of work alone. Note its UDID.
2. Boot it without a window: `xcrun simctl boot <udid>`. Do not open Simulator.app.
3. Wait until it is really ready (see the notification center below).
4. Build the runner once with `xcodebuild build-for-testing`, then run it with `xcodebuild test-without-building -xctestrun <file> -destination 'platform=iOS Simulator,id=<udid>'`.
5. Give each test a time limit: `-test-timeouts-enabled YES -maximum-test-execution-time-allowance 600` for 10 minutes.
6. Shut the simulator down with `xcrun simctl shutdown <udid>` and uninstall what the run installed.

Generate the runner project, for example with XcodeGen, with an Info.plist that names the app it drives and the screenshot folder.

## Wait for the notification center

A freshly booted iOS simulator accepts an app before SpringBoard has loaded the notification sources. An app installed before that never shows notifications, and its permission requests hang.

- `xcrun simctl bootstatus <udid>` returns minutes too early for this.
- The reliable signal seen in practice is the SpringBoard log record `notificationSourcesDidInstall` with `initialLoad=1`, under the subsystem `com.apple.UserNotifications`, read with `xcrun simctl spawn <udid> log show --predicate 'subsystem == "com.apple.UserNotifications"'`. It is not an API, so the text may change with a new iOS.
- Give the wait a bound, such as 15 minutes, and fail with the reason.
- A busy Mac or a CI runner delays it by minutes.

## The software keyboard

- A simulator reports the Mac's keyboard as a hardware keyboard, so iOS shrinks its own keyboard to a bar, and a test that taps keys finds none. Turn off `AutomaticMinimizationEnabled` in the domain `com.apple.keyboard.preferences` of the simulator during the run, and restore it after.
- The first time the keyboard shows on a new simulator, it covers the keys with the slide-to-type introduction (`UIContinuousPathIntroductionView`). Tap its one button first.
- XCUITest never sees the keyboard animation go idle when a field takes the keyboard back while it is still hiding. End the editing with a tap elsewhere, and wait until the keyboard is gone before the next tap.

## Recordings, logs and screenshots

- Ask for screenshots on failure, not a screen recording. The iOS 17 test manager ended when Xcode asked it for a recording.
- Stream the app's log during the run, and fail the run when the app logged an error, even if every test passed.
- The unified log has no type for a warning and gives it the type of an error. Classify by the level the app writes in its own message text.
- On failure, keep the whole simulator log next to the result bundle.
- Capture the app window only, never the whole screen.

## Simulator settings and inputs

- **External display:** the simulator's external display exists but is off. Power it on with `xcrun simctl io <udid> screenConfig --display=external power on` in Xcode versions that have `screenConfig` (Xcode 27 does). No simctl command adds a display.
- **Location:** set `XCUIDevice.shared.location = XCUILocation(location: <CLLocation>)` in the test (iOS 16.4 and later), or `xcrun simctl location <udid> set <lat>,<lon>`. Reset it after, because the device keeps the place and its time zone.
- **Authorizations:** reset them per test with `app.resetAuthorizationStatus(for: .camera)` and the other protected resources, or `xcrun simctl privacy <udid> reset <service> <bundle id>`. The notification authorization resets only with a reinstall.
- **System alerts:** tap the buttons by position, not by text, because the device writes the buttons in its own language.
- **tvOS remote:** `XCUIRemote.shared.press(.up)` and the other buttons, tvOS only.
- **Gamepads:** `GCVirtualController` exists on iOS and iPadOS 15 and later, not on tvOS, macOS or visionOS, and an app can connect one at a time. Test several gamepads in engine-level tests instead.
- **GPU:** a simulator or a virtual Mac has a paravirtual GPU, not a real one. GPU results count only from real Macs and real devices.
- **visionOS:** install the platform with `xcodebuild -downloadPlatform visionOS`, and ask the person before creating its simulator.
- **iPad multitasking:** tests can switch between Full Screen Apps, Windowed Apps and Stage Manager, tile and resize windows, and must restore the mode after.

## Apple devices reached from the Mac

- `xcrun devicectl list devices` lists them. `xcrun devicectl device install app --device <udid> <path>` installs, and `xcrun devicectl device process launch --device <udid> <bundle id> <arguments>` launches with launch arguments.
- The Mac reaches a device over the CoreDevice tunnel, whose address `devicectl` reports. It is not a broadcast network, so a development server reached that way needs no local-network permission on the device.
- **iPhone and iPad:** keep them unlocked during the run. iOS runs UI tests on a device only after the person turns on **Settings > Developer > Enable UI Automation** once, with the passcode. No tool can do it. Tell the person once, and make a run that iOS stops for it say so.
- **Apple TV:** pair it with Xcode first. tvOS launches no app while the Apple TV sleeps. The test presses an arrow of the remote before it launches the app, which wakes the Apple TV and only moves the focus. Do not use the Home button to wake it: tvOS acts on Home a moment later and sends the freshly launched app to the background.
- **Signing:** the person's own development team, from a variable such as `APPLE_TEAM`.
- No researched cloud rents an Apple TV or an Apple Vision Pro. AWS Device Farm covers iPhone and iPad (see [Device Farm](device-farm.md)).

## macOS and Mac Catalyst UI tests

- XCUITest drives Mac apps only in the automation mode of macOS. A CI machine or a dedicated Mac enables it once without a password: `sudo automationmodetool enable-automationmode-without-authentication`. Running `automationmodetool` with no argument prints the current state.
- On a person's Mac, automation mode asks for the password, and the clicks go to the app in front. So Mac UI tests run on CI runners or a dedicated Mac, never on a Mac someone is using.
- A Mac installs no app for the tests: launch it with `XCUIApplication(url:)` from the built bundle. That initializer exists on macOS and Mac Catalyst only.
- **Held keys and input methods:** XCUITest presses a key once and types characters without the input method. To hold a key or type through an input method, the test asks the run, through a line of its output, to post the events with `CGEventPost`. That needs the test-running app in **Privacy & Security > Accessibility**.
- **Input sources:** the runner's sandbox keeps input sources per process. The run selects the input source with the Carbon Text Input Sources API and relaunches the app, since an app keeps the source it had when it came to the front.
- **Screenshots:** the runner can only write inside its container, so screenshots are attachments of the `.xcresult`. Export them with `xcrun xcresulttool`, also when tests failed.
- **Input-method settings:** the runner keeps them too. For example, Japanese live conversion is on by default, and the run turns it off with the key `JIMPrefLiveConversionKey` of `com.apple.inputmethod.Kotoeri`. Restore every setting after.

## Xcode Cloud

When the local Mac is busy, Xcode Cloud runs Apple builds and simulator tests in Apple's CI, with fresh simulators for every test run and no physical devices. Its setup, workflow design, scripts and API are in [Xcode Cloud](xcode-cloud.md).

## Cloud Mac day

A cloud Mac is the most expensive machine. Its dedicated host bills at least 24 hours, so plan it as one day a month at most and fill it (see [AWS](aws.md#cloud-mac-ec2-mac-dedicated-host)). Prepare the day before: the batch list, the bundles, the Xcode and tool setup scripts, and the collection and release scripts. Fill the day with heavy Apple work that can wait: UI tests on many simulators at once, every Apple slice, benchmarks and long investigations.

## Sources

Checked on 2026-11-26 against the help text, man pages and SDK headers of Xcode 27.2 (`xcrun simctl help`, `xcrun devicectl help`, `man xcodebuild`, `man automationmodetool`), plus [XCUIAutomation](https://developer.apple.com/documentation/xcuiautomation), [GCVirtualController](https://developer.apple.com/documentation/gamecontroller/gcvirtualcontroller) and [EC2 Mac instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-mac-instances.html). The notification-center signal, the keyboard settings and the input-method details come from practice. See [sources](sources.md) for the full record.
