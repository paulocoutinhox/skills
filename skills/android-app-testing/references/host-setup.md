# Host setup and device readiness

Read this for workstation setup, image choice, connectivity and install diagnosis. The host operating system runs the tools. The Android guest/device runs the app.

## Set up the real toolchain

Open the project's Gradle wrapper, Android Gradle Plugin configuration, Java toolchain and SDK declarations. Write down the selected versions and check their documented compatibility before you build. A globally installed Gradle or a random JDK cannot stand in for the project's toolchain. Use Studio's real SDK location instead of assuming every workstation has the default path.

Install Android Studio and the SDK components for the selected platform/image through the setup wizard and SDK Manager. Keep platform tools, the emulator runtime, the platform and any needed build tools easy to identify. The Android CLI can list packages with `android sdk list`. Its package paths use slash-separated names. Choose exact packages through current help or the IDE. Do not copy old command-line-tool layouts or guess an image revision.

Common SDK locations are `%LOCALAPPDATA%\Android\Sdk`, `~/Library/Android/sdk` and `~/Android/Sdk`. These are hints for finding the SDK, not facts about a given host. Make the selected SDK tools findable in that terminal, and check the real executable/version when Studio and the terminal disagree.

## Acceleration and host-specific checks

| Host | Establish before boot | Failure to investigate |
| --- | --- | --- |
| Windows | Supported x86-64 machine, firmware virtualization, Windows Hypervisor Platform turned on and a restart done if needed | Firmware support turned off, hypervisor not available, clashing host virtualization setup or graphics driver |
| macOS | Matching native Studio/runtime, Hypervisor.Framework and a guest architecture that matches the host | Wrong image ABI, unsupported runtime/OS or not enough resources |
| Linux | Supported x86-64 machine, KVM installed, `/dev/kvm` present and usable by the current user | Missing virtualization, wrong group/session permissions or a runner that does not expose KVM |

The official acceleration guide documents this emulator-runtime check. At the common default paths, run the right command after you confirm the path:

```powershell
& "$env:LOCALAPPDATA\Android\Sdk\emulator\emulator.exe" -accel-check
```

```bash
"$HOME/Library/Android/sdk/emulator/emulator" -accel-check
```

```bash
"$HOME/Android/Sdk/emulator/emulator" -accel-check
```

Use its result as a diagnostic, not proof that the guest booted or the GPU works. The baseline Windows recommendation is WHPX. The separate AEHD driver has an announced end date of December 31, 2026, so do not build a new setup around it. Do not suggest turning off host security controls as a general emulator fix.

Use the distro's documented KVM setup, and log in again if a group membership change needs it. Do not fix permissions with KVM devices anyone can write to, or by running the whole development environment with full privileges. Check the real runner's supported virtualization instead of assuming that a cloud VM, Docker or WSL setup is the same as the native host.

## Create a repeatable device

Use Device Manager to pick the required API/image/ABI, and write down the hardware profile, density, resolution, memory/storage, navigation mode and locale. Host-native accelerated images are x86-family on Intel/AMD and ARM64 on Apple silicon. An image that boots fine can still lack the ABI the app's native libraries need.

For current Android CLI management:

```text
android --version
android emulator create --list-profiles
android emulator create medium_phone
android emulator list
```

`medium_phone` is a documented example profile. Read the real output and pick the new AVD name before you start it:

```text
android emulator start --cold AVD_NAME
```

Replace `AVD_NAME` with that listed name. `--headless` is available for a prepared host with no user present. Cold start skips the saved boot snapshot. It does not wipe the app or choose the Android API you want. Use the IDE's exact image selection when the documented profile interface cannot express the requested matrix.

Do not run two workers against one writable AVD. Give each worker its own device and artifact folder. Build-managed devices can handle the lifecycle of a test device already set up in a project. The researched feature starts at API 27, so on its own it cannot cover a lower app minimum. Its task name joins the declared device or group with the variant, such as `pixel2api30DebugAndroidTest` or `phoneAndTabletGroupDebugAndroidTest`. Find the real declared names instead of assuming a profile name creates a task. Do not use build-managed Firebase Test Lab devices.

## Identify and prepare the target

```text
adb devices -l
adb -s SERIAL get-state
adb -s SERIAL shell getprop sys.boot_completed
```

Put in the serial you found. Expect `device` from `get-state` and `1` from `sys.boot_completed`. An empty value means boot is still running, so wait with a time limit instead of installing. Confirm Android reports that boot finished, get past any setup/lock screen and check that the real app can start. The transport state `device` is needed, but it does not mean the UI is ready. Fix `offline`, `unauthorized` or unclear multiple-device cases before you install.

For physical USB devices, use a cable that carries data, approved USB debugging and the needed Windows OEM drivers or Linux USB rules. macOS usually needs no extra USB driver. A USB approval prompt needs the device owner to act. Prefer the documented paired wireless-debugging flow where it fits, and remove access after you test a borrowed device.

Install the right APK or the full split set. `INSTALL_FAILED_NO_MATCHING_ABIS` points to native libraries. Signature conflicts need the matching signing identity or a separately planned clean install. A clean install cannot check migration of kept data. Check free storage and API support when installation fails. Do not hide these failures by accepting an install command that returned an error.

## Connect to the real backend

The emulator's `127.0.0.1` is its own loopback. The standard Android Emulator offers `10.0.2.2` as an alias for the workstation's loopback. This is not a universal address for physical devices or remote clouds. Check the listener, firewall, DNS, proxy and TLS separately from app validation.

For a controlled local test backend on TCP 8080, an ADB reverse mapping is another clear option:

```text
adb -s SERIAL reverse tcp:8080 tcp:8080
adb -s SERIAL reverse --list
```

Check the intended mapping, and when you finish, remove only that mapping with `adb -s SERIAL reverse --remove tcp:8080`. A remote lab needs its own documented network path. Do not make a private service public or turn off release TLS checks to make a test pass.

## Diagnose the first failed stage

Keep these apart: host acceleration, guest boot, ADB, installation, app startup, backend reachability and assertion failure. Write down the first real error, the selected device and the logs that matter. Choose a fix for that stage. Repeated full wipes can erase the state you need to reproduce the bug while leaving a host or network problem in place.

See [source notes](sources.md) for official setup, acceleration, ADB, networking and managed-device contracts.

## Disposable writable data and stale AVD references

Check the selected AVD's real data path when it points to a scratch folder that no longer exists. A
stale reference is not an acceleration or app bug. Create a test device you own with the current
management tools, and keep other devices. Advanced runtime disk overrides need the installed emulator's
real help. Separate writable images and snapshots on purpose. Cold boot alone does not clear
or isolate saved user data. See [release-device isolation](release-bundle-testing.md#own-the-emulators-writable-data).
