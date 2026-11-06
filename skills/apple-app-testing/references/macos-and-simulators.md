# Mac, simulator and physical-device setup

Read this for toolchain selection, destinations, app/test artifacts and failures before meaningful app execution. Current Xcode documentation calls the integrated simulated/physical-device interface Device Hub.

## Establish the development environment

Record macOS, Mac architecture, selected full Xcode version/build and the project's actual SDK/deployment requirements. Compare them with Apple's Xcode system-requirements table, including the simulator runtime range. A deployment target lower than the available simulator range still needs an appropriate device/environment for that boundary.

Use `xcode-select -p` and `xcodebuild -version` to inspect selection. The SDK and developer tools must belong to the intended installation. If multiple versions exist, choose the project's documented developer-directory configuration for the operation rather than silently changing system-wide selection. Resolve Xcode's initial setup/license requirements through the authorized user, without automatically accepting agreements.

Developing for visionOS requires Apple silicon under the researched Apple requirements. An Intel Mac is not an equivalent visionOS environment. Likewise, an arm64 simulator product and an arm64 physical-device product have different platform targets. Check both platform and architecture for every executable dependency.

Full Xcode supplies `xcodebuild`, `simctl`, `devicectl`, `xcresulttool` and Instruments tooling. The command-line reference directs users to the selected installation's help/manual. Do not assume a command copied from a different Xcode is available or fabricate a simulator input API.

## Configure runtimes and simulated devices

Open Device Hub from Xcode → Open Developer Tool → Device Hub or Manage Devices in the destination menu. Add the actual platform, model and runtime. If the runtime is missing, install the required Xcode platform component first. Record the device identifier, OS build and settings.

For native command-line discovery on a working simulator host:

```text
xcrun simctl list runtimes
xcrun simctl list devices available
```

Choose a concrete device identifier instead of `booted`, which becomes ambiguous when multiple workers/devices are active. A conventional explicit boot and readiness check is:

```text
xcrun simctl boot SIMULATOR_UDID
xcrun simctl bootstatus SIMULATOR_UDID -b
```

Run boot only for the selected shutdown device, not as a blind retry against an already booted instance. Confirm that the device and application UI are ready after boot. A successful command does not complete a first-run wizard, grant permissions or establish backend readiness.

Use actual simulator `.app` products when manually installing:

```text
xcrun simctl install SIMULATOR_UDID /path/to/SimulatorApp.app
xcrun simctl launch SIMULATOR_UDID com.example.app
```

Replace both paths and bundle ID with inspected values. The app's original XCTest runner is a separate artifact. Installing a product is not executing its tests. An App Store/device IPA cannot be installed as a simulator product simply by extracting or renaming it.

## Distinguish reset operations

Restart preserves the simulator's existing data. Reset Content and Settings erases it. Fresh install, reinstall with preserved data and upgrade from a supported previous artifact are separate scenarios. Removing the app does not by itself prove every Keychain, shared container, cloud or backend value was reset.

Keep a device owned by one worker and write artifacts to a distinct directory. Shut down only owned devices. Do not erase all simulators, reset global privacy preferences, delete all DerivedData or kill shared services as a first response to one test failure.

Use Device Hub's appearance/text/environment controls for supported variations. Canvas zoom changes how the Mac displays the simulator. Changing logical device/window size changes the app's layout. Keep those operations distinct in evidence.

## Pair physical devices deliberately

Use Device Hub's current pairing flow, required trust prompts and Developer Mode for the selected platform. Confirm device OS and Xcode device support, selected team, provisioning and test-runner installation.

The current wireless pairing guide requires iOS/iPadOS 27 or later for that specific direct pairing flow and otherwise directs users to a cable. Do not generalize an older wireless workflow to every current device/toolchain combination. Use the actual supported flow for the selected destination.

For Apple TV and Vision Pro, the current guide requires IPv6 on the Wi-Fi network and device discoverability through the relevant Remote App and Devices or Remote Devices setting. Authorize the PIN/trust flow on the actual device. A corporate network that blocks discovery can fail before signing or app code is involved.

For a companion Watch, establish the intended phone/watch pair and developer authorization on both. Independent Watch application architecture does not guarantee every development/pairing step avoids a phone. Confirm the real scheme and watch test host instead of hardcoding historical WatchKit Extension names into a current project.

Signing must match the exact artifact, entitlements, registered-device/distribution path and provider requirements. Simulator runs do not validate device provisioning. A runner installation error is infrastructure evidence, not a passing or failing business case.

## Native Mac and other macOS versions

Run native Mac apps/tests on the selected Mac destination. Check native AppKit/SwiftUI, Catalyst and iPad-on-Mac identities separately. Record the app path and bundle ID so a previously installed copy is not mistaken for the just-built artifact.

A controlled macOS VM can provide a different OS/user-state environment. Apple's Virtualization framework documents macOS guests on Apple silicon. Record host/guest OS, architecture, graphical session and supported virtual hardware. A VM or Rosetta execution cannot certify a missing physical Intel/device/hardware profile.

UI control needs the relevant graphical session and system authorization. Xcode's recorder documents an Accessibility permission prompt for Xcode Helper. Grant the requested runner/tool permission deliberately through the actual UI. Screen capture or automation may require separate permissions for the chosen tool. Do not edit the privacy database or disable system protections to avoid those boundaries.

Use disposable test accounts/users for sandbox file permissions, document access and first-run prompts. Do not clear the developer's real Keychain, privacy decisions or document history. Inspect the actual signed/distributed variant when Gatekeeper, sandbox or entitlements affect the requirement.

## Diagnose in stage order

Distinguish toolchain selection, runtime availability, simulator service access, pairing, signing, installation, test discovery, application launch, backend connectivity and assertion failure. Preserve the first error and identify the stage before changing anything.

A sandbox can prevent a command from contacting CoreSimulator even when Xcode is installed. Record unavailable access instead of claiming that no runtimes exist or that the application crashed. Complete the plan, artifact inspection and other independent checks without inventing execution.

See [sources](sources.md) for current Apple toolchain, Device Hub, pairing and native manual evidence.

## Multi-display and host-control diagnostics

Use `xcrun simctl help io` from the selected Xcode before choosing capture options. In inspected
Xcode 27.2, `io <device> enumerate` lists screens and `screenshot --display=<id>` selects one.
Do not equate that selection with a Device Hub posture change. Diagnose the powered/visible display
and actual window before retrying a black image. See [native UI and multi-display procedures](native-ui-and-multidisplay.md)
for the concrete sequence and environment-specific GUI-control diagnosis.
