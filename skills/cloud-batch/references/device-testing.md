# Device testing rules

Read this before any run on a simulator, an emulator, a browser, a person's own device or a device farm. These rules come from long device test sessions across iPhone, iPad, Apple TV, Mac, Android phones, Windows and Linux. Platform details are in [Apple platforms](apple-platforms.md), [Xcode Cloud](xcode-cloud.md), [Android emulator](android-emulator.md), [AWS Device Farm](device-farm.md), [Google Device Run](google-device-run.md), [Windows desktop tests](windows-desktop.md) and [Linux GPU and browsers](linux-gpu-and-browsers.md).

## Every check is automatic

No step asks the person to tap, answer a prompt, wake a device or report what they saw. A person once had to answer instruction cards on an iPhone, an Android phone and an Apple TV during a long guided session. Afterwards they said they never wanted manual testing again.

Automate prompts, notifications, Home, Back, Recents, rotation, the TV remote and sensors with:

| Platform | Tool |
| --- | --- |
| iOS, iPadOS, tvOS, visionOS, macOS | XCUITest (XCUIAutomation) |
| Android | UI Automator, run from an instrumentation test APK |
| Windows | UI Automation for finding elements, `SendInput` for input |
| Web | A headless browser or Selenium/WebDriver |

## Simulators, emulators and browsers carry the checks

A physical device runs only what they cannot show:

- hardware they lack, such as the camera, a real microphone, haptics, motion sensors and Bluetooth;
- real GPU behavior and performance;
- signing and store delivery.

A check that passed on a simulator is not repeated on a device. A check is never left open waiting for the person's device.

The one check no API drives is the fold posture of the iPhone Duo simulator. Only the controls of Xcode's Device Hub set it (Xcode 27.1 and later), and `xcrun simctl` has no posture command. Keep it out of routine runs. Only a person does it, when a fold change truly needs it.

## How tests find, start and capture

- **Find elements through the accessibility tree:** the accessibility label on Apple, the content description on Android, the name of the UI Automation element on Windows. So the app must expose its UI to screen readers, which also makes it accessible.
- **Start the app again for each test** with launch arguments that open the screen it checks, such as `--test <code>`. The test never navigates a long way through the app.
- **Capture the app window only,** never the whole screen.
- **Skip only for a missing capability,** with a sentence that names it, such as "turning a physical device needs a person, so this runs on the emulator". The suite then stays green on a real device and in a device farm.
- **Bound every wait:** a simulator boot, an upload, a device farm run, a test. When the bound runs out, fail with a sentence.

## The person's own devices

- **Always name the device:** `--device <udid or name>`, `adb -s <serial>`, `ANDROID_SERIAL`. Never rely on "the only connected device". An agent once ran tests on the person's personal phone because it was the only device connected. Since then, a USB phone of daily use is off-limits: nothing installs on it, and nothing is sent to it.
- **Use only simulators and emulators that already exist.** Never create or delete one without permission. Shut down the ones a run booted.
- **Other projects share the simulators.** A booted simulator looks free to every session. Another project once launched its app on the simulator where a UI test ran, and the test failed. So:
  - always pass `--device <udid>`;
  - pick a simulator with no apps of other projects installed (look at `data/Containers/Bundle/Application/*/*.app` under each device folder in `~/Library/Developer/CoreSimulator/Devices/`);
  - give each line of work its own simulator;
  - check that the app in front is yours before you trust a capture.
- **Uninstall** every app and test runner a run installed, at the end.
- **Never open app windows on the person's screen.** Use headless players, simulators booted without Simulator.app, the emulator with `-no-window`, headless browsers or the cloud.
- **Signing:** use the person's own development team, from a variable such as `APPLE_TEAM`. Never use a distribution identity of an employer or a client.
- **Clean up after the device:** a device keeps a simulated location after the run, with the time zone that the place sets, unless the test resets it.

### One-time setup the person must do

Some steps need the person's hands once. Ask for them once, in one message, before the first device run:

| Device | One-time step | What happens without it |
| --- | --- | --- |
| Android phone | Turn off the maker's "confirm installs over USB" option (Xiaomi has one, for example) | Every install waits for a tap on the phone |
| iPhone, iPad | **Settings > Developer > Enable UI Automation**, with the passcode | iOS stops the UI test run. The run must say so in a sentence |
| iPhone, iPad | Keep the device unlocked during the run | Tests cannot launch the app |
| Apple TV | Pair it with Xcode | The Mac cannot install or launch |
| Mac | Add the test-running app to **Privacy & Security > Accessibility**, only when tests post events with `CGEventPost` | Held keys and input-method typing do nothing |

No tool can do these for the person.

## The plan's device matrix

For each person, build one row per platform to cover:

| Column | Content |
| --- | --- |
| Platform | Such as Android phone, iPad, Apple TV, Windows desktop, Linux GPU, browser |
| Cheapest place that shows it | Simulator, emulator, browser, own device, CI (Xcode Cloud included), cloud VM or device farm |
| What only real hardware shows | And where to rent it, if anywhere |
| One-time setup | Pairing, Enable UI Automation, automation mode, USB install confirmation off, quotas, drivers |
| Per-run steps | Boot, install, run, collect |
| Cleanup | Uninstall, shut down, reset settings, delete projects |
| Cost | Per run and per month |

Mark what no cloud rents: Apple TV, Apple Vision Pro and Apple Watch hardware are not offered by AWS Device Farm or the other researched services, so tvOS and visionOS stay on simulators and the person's own devices. Mark also what needs the person's own device. Use [the batch plan template](../assets/batch-plan.md).

## Sources

Checked on 2026-11-26: [Preparing your app for iPhone Duo](https://developer.apple.com/documentation/technologyoverviews/preparing-your-app-for-iphone-duo), [XCUIAutomation](https://developer.apple.com/documentation/xcuiautomation), [UI Automator](https://developer.android.com/training/testing/other-components/ui-automator), [UI Automation](https://learn.microsoft.com/en-us/windows/win32/winauto/entry-uiauto-win32) and [Device Farm devices](https://docs.aws.amazon.com/devicefarm/latest/developerguide/devices.html). The rules about named devices, shared simulators and one-time setup come from practice. See [sources](sources.md) for the full record.
