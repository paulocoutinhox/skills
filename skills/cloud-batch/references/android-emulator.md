# Android emulator, local and in the cloud

Read this for Android emulator runs on the local machine or a cloud batch machine. Follow [device testing](device-testing.md) first. Documented commands were checked on **2026-11-26** against the Android developer docs and AOSP sources. Some useful shell commands are not in the public docs. Those are marked, so check them with `adb shell am help`, `adb shell cmd appops help` or the device's own help text on the Android version you run.

## KVM first

The emulator needs hardware acceleration, which is KVM on Linux. On a cloud machine, use a type with nested virtualization, or the emulator crawls or does not start:

- AWS: the Intel families of the 7th and 8th generations, such as c7i and c8i, with nested virtualization turned on (see [AWS](aws.md)), or a `.metal` instance;
- Azure: sizes whose page lists nested virtualization as supported, such as Dv5 and Ev5 (see [Azure](azure.md));
- Google Cloud: machine series that support nested virtualization (see [Google Cloud](google-cloud.md)).

Check with `ls -l /dev/kvm` and add the batch user to the `kvm` group.

## Start, wait, stop

Create and list virtual devices with the Android CLI (`android emulator create`, `android emulator list`). For a headless run with a chosen GPU mode, start the emulator runtime with its documented options:

```bash
emulator -avd <name> -no-window -no-audio -no-boot-anim -gpu swiftshader
```

Pick the GPU mode the check needs: `swiftshader` or `software` for software rendering, `lavapipe` for software Vulkan, `host` for a real GPU. Do not use `swiftshader_indirect`, which is deprecated.

Wait until `adb -s <serial> shell getprop sys.boot_completed` prints `1`, with a bound. Run the tests. Then stop it with `adb -s <serial> emu kill`.

## Emulator images differ in GPU translation

Different system images translate OpenGL ES differently. A defect showed up only on the CI emulator image, whose translator ran on SwiftShader 4. The local Mac's emulator drew through ANGLE on SwiftShader 5, where the defect did not show. Reproduce on the exact image that failed. A cloud batch machine can run the CI's image.

## Rotation

An app that follows the sensor turns only with the accelerometer, not with UI Automator's rotation. Set the accelerometer through the emulator console: `adb -s <serial> emu sensor set acceleration <x>:<y>:<z>`. Read the value before, and restore it after. A physical device turns only in a person's hands, so that test skips there with a sentence.

## Keyboard

- Android hides the soft keyboard while a hardware keyboard is attached, and the emulator reports the host's keyboard. Turn on `adb -s <serial> shell settings put secure show_ime_with_hard_keyboard 1`, and restore the old value after. The setting is per user, so add `--user <id>` on a device with several users.
- Whether the keyboard shows: `adb shell dumpsys input_method` prints `mInputShown`. It is not a public API, so fail with the API level in the message when the field is missing.
- The accessibility tree of the keyboard window reads as empty for a moment while the screen turns. Wait for it.

## Immersive mode

Set the secure setting `immersive_mode_confirmations` to `confirmed` before the first start (`adb shell settings put secure immersive_mode_confirmations confirmed`), or the system hint covers the app. This key comes from AOSP code, not the public docs.

## Permission dialogs

- Tap the buttons by resource id, which holds in every language: `permission_allow_foreground_only_button`, `permission_allow_button`, `permission_allow_one_time_button`, `permission_deny_button` and `permission_deny_and_dont_ask_again_button`, in the permission controller's package. The package name differs between AOSP and devices with Google services, so read it from the dialog's window.
- Android 10 shows `permission_allow_button` for the camera, where later versions show "while in use", so list every id of an answer.
- In landscape, scroll toward the button.
- Wait until the dialog window has the input focus before the tap, or the tap reaches the activity below.
- Revoke runtime permissions before each test with `adb shell pm revoke <package> <permission>`, so the prompts show again.

## Notifications

Open the shade, tap the notification and wait until the app is in front. Never change Do Not Disturb, which belongs to the person. Fail with that reason if it hides the notifications.

## Recents and process death

- `adb shell am kill <package>` ends the process once it holds no activity, as the system does under memory pressure. It only ends processes that are safe to kill, so confirm in the process list that it really ended.
- Removing the task, as a swipe away in Recents does, worked in practice with `adb shell am stack remove <id>`. It is not in the public docs, so check `am help` on the device first. UI Automator can swipe the task away in the Recents screen instead.

## Location, fresh start and results

- **Location:** test providers of GPS and network need the app op `android:mock_location` for the runner, set in practice with `adb shell appops set <runner package> android:mock_location allow`. It is not in the public docs, so check `cmd appops help` on the device.
- **Fresh start:** `adb shell pm clear <package>` before a start gives a first-start state.
- **Results:** the app's own files come out with `adb exec-out run-as <package> tar -c -C files <folder>`. The app must be debuggable.

## The runner

Use a test APK that instruments itself, so it drives the app from outside. Run it with `adb shell am instrument -w <test package>/<runner class>`, and bound the time until the first test starts. On failure, keep `logcat.txt` and a picture of the app window.

## GPU programs and focus navigation

- A program that `adb shell` starts finds no Vulkan GPU on many devices. Run GPU tests from an installed test app.
- `adb shell input keyevent` with D-pad keys moves the focus, which suits TV and focus navigation tests.

## Physical Android phones

- Always name the device with `adb -s <serial>` or `ANDROID_SERIAL`. A phone of daily use is off-limits.
- Turn off the maker's "confirm installs over USB" option once, or every install waits for a tap.
- Real-hardware checks across GPU vendors go to [AWS Device Farm](device-farm.md).

## Sources

Checked on 2026-11-26: [emulator command line](https://developer.android.com/studio/run/emulator-commandline), [emulator console](https://developer.android.com/studio/run/emulator-console), [emulator acceleration](https://developer.android.com/studio/run/emulator-acceleration), [ADB](https://developer.android.com/tools/adb), [AOSP boot properties](https://source.android.com/docs/core/perf/boot-times) and the [permission controller layout](https://android.googlesource.com/platform/packages/modules/Permission/+/refs/heads/main/PermissionController/res/layout/grant_permissions.xml). The commands marked as not in the docs come from practice. See [sources](sources.md) for the full record.
