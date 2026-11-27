# Mac, simulator and physical-device setup

Read this for toolchain choice, destinations, app/test artifacts and failures before you run the app for real. Current Xcode documentation calls the combined simulated/physical-device interface Device Hub.

## Establish the development environment

Write down macOS, Mac architecture, the selected full Xcode version/build and the project's real SDK/deployment needs. Compare them with Apple's Xcode system-requirements table, including the simulator runtime range. A deployment target below the available simulator range still needs a suitable device/environment to test that limit.

Use `xcode-select -p` and `xcodebuild -version` to check the selection. The SDK and developer tools must come from the intended installation. If several versions exist, use the project's documented developer-directory setup for the task instead of quietly changing the system-wide selection. Handle Xcode's first-run setup/license steps through the approved user. Do not accept agreements automatically.

Under the researched Apple requirements, visionOS development needs Apple silicon. An Intel Mac is not an equal visionOS environment. In the same way, an arm64 simulator product and an arm64 physical-device product have different platform targets. Check both platform and architecture for every executable dependency.

Full Xcode provides `xcodebuild`, `simctl`, `devicectl`, `xcresulttool` and Instruments tooling. The command-line reference points users to the selected installation's help/manual. Do not assume a command copied from a different Xcode is available, and do not make up a simulator input API.

## Configure runtimes and simulated devices

Open Device Hub from Xcode → Open Developer Tool → Device Hub, or Manage Devices in the destination menu. Add the real platform, model and runtime. If the runtime is missing, install the needed Xcode platform component first. Write down the device identifier, OS build and settings.

For native command-line discovery on a working simulator host:

```text
xcrun simctl list runtimes
xcrun simctl list devices available
```

Choose a specific device identifier instead of `booted`, which becomes unclear when several workers/devices are active. A normal explicit boot and readiness check is:

```text
xcrun simctl boot SIMULATOR_UDID
xcrun simctl bootstatus SIMULATOR_UDID -b
```

Run boot only for the selected device that is shut down. Do not use it as a blind retry on a device that is already booted. `bootstatus` waits until boot finishes, and its `-b` option boots the device itself when it is not already booted. After boot, confirm that the device and app UI are ready. A successful command does not finish a first-run wizard, grant permissions or make the backend ready.

Use real simulator `.app` products when you install by hand:

```text
xcrun simctl install SIMULATOR_UDID /path/to/SimulatorApp.app
xcrun simctl launch SIMULATOR_UDID com.example.app
```

Replace both paths and the bundle ID with the values you found. Capture a plain simulator screenshot with `xcrun simctl io SIMULATOR_UDID screenshot artifacts/profile-error.png`, and open it before you cite it. The app's original XCTest runner is a separate artifact. Installing a product is not running its tests. You cannot install an App Store/device IPA as a simulator product just by extracting or renaming it.

## Distinguish reset operations

Restart keeps the simulator's existing data. Reset Content and Settings erases it. Fresh install, reinstall that keeps data and upgrade from a supported earlier artifact are separate scenarios. Removing the app does not, on its own, prove that every Keychain, shared container, cloud or backend value was reset.

Give each device to one worker and write artifacts to a separate folder. Shut down only devices you own. Do not erase all simulators, reset global privacy settings, delete all DerivedData or kill shared services as a first reaction to one test failure.

Use Device Hub's appearance/text/environment controls for supported variations. Canvas zoom changes how the Mac shows the simulator. Changing the logical device/window size changes the app's layout. Keep those actions separate in evidence.

## Pair physical devices with care

Use Device Hub's current pairing flow, the required trust prompts and Developer Mode for the selected platform. Confirm the device OS and Xcode device support, the selected team, provisioning and test-runner installation.

The current wireless pairing guide needs iOS/iPadOS 27 or later for that direct pairing flow, and otherwise tells users to use a cable. Use a cable for devices that do not meet that requirement. Use the real supported flow for the selected destination.

For Apple TV and Vision Pro, the current guide needs IPv6 on the Wi-Fi network and device discovery turned on through the Remote App and Devices or Remote Devices setting. Approve the PIN/trust flow on the real device. A device paired wirelessly must be paired again after its operating system is upgraded. A company network that blocks discovery can fail before signing or app code is involved.

For a companion Watch, set up the intended phone/watch pair and developer approval on both. An independent Watch app design does not promise that every development/pairing step works without a phone. Confirm the real scheme and watch test host instead of hardcoding WatchKit Extension target names.

For a paired physical device, the selected Xcode's `devicectl` lists, installs and launches device builds:

```text
xcrun devicectl list devices
xcrun devicectl device install app --device DEVICE_ID /path/to/DeviceApp.app
xcrun devicectl device process launch --device DEVICE_ID com.example.app
```

Use an identifier from the listing and a signed device product. Its standard output is meant for people, so use `--json-output PATH` when a later step needs to read the result. Check `xcrun devicectl help` on the selected installation before you rely on other subcommands.

Signing must match the exact artifact, entitlements, registered-device/distribution path and provider requirements. Simulator runs do not check device provisioning. A runner installation error is infrastructure evidence, not a passing or failing business case.

## Native Mac and other macOS versions

Run native Mac apps/tests on the selected Mac destination. Check native AppKit/SwiftUI, Catalyst and iPad-on-Mac identities separately. Write down the app path and bundle ID so nobody mistakes an earlier installed copy for the artifact you just built.

A controlled macOS VM can give a different OS/user-state environment. Apple's Virtualization framework documents macOS guests on Apple silicon. Write down host/guest OS, architecture, graphical session and supported virtual hardware. A VM or Rosetta run cannot certify a missing physical Intel/device/hardware profile.

UI control needs the right graphical session and system permission. Xcode's recorder documents an Accessibility permission prompt for Xcode Helper. Grant the requested runner/tool permission on purpose through the real UI. Screen capture or automation may need separate permissions for the chosen tool. Do not edit the privacy database or turn off system protections to get around those limits.

Use throwaway test accounts/users for sandbox file permissions, document access and first-run prompts. Do not clear the developer's real Keychain, privacy choices or document history. Check the real signed/distributed variant when Gatekeeper, sandbox or entitlements affect the requirement.

## Diagnose in stage order

Tell apart toolchain choice, runtime availability, simulator service access, pairing, signing, installation, test discovery, app launch, backend connectivity and assertion failure. Keep the first error and find its stage before you change anything.

A sandbox can stop a command from reaching CoreSimulator even when Xcode is installed. Record that access is not available instead of claiming that no runtimes exist or that the app crashed. Finish the plan, artifact checks and other independent checks without inventing a run.

See [sources](sources.md) for current Apple toolchain, Device Hub, pairing and native manual evidence.

## Multi-display and host-control diagnostics

Use `xcrun simctl help io` from the selected Xcode before you choose capture options. In the
checked Xcode 27.2, `io <device> enumerate` lists screens and `screenshot --display=<id>` selects one.
Do not treat that selection as a Device Hub posture change. Check the powered/visible display
and the real window before you retry a black image. See [native UI and multi-display procedures](native-ui-and-multidisplay.md)
for the exact sequence and diagnosis of GUI control in each environment.
