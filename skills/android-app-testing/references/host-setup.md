# Host setup and device readiness

Read this for workstation setup, image selection, connectivity and installation diagnosis. The host operating system runs the tools. The Android guest/device runs the application.

## Establish the actual toolchain

Open the project's Gradle wrapper, Android Gradle Plugin configuration, Java toolchain and SDK declarations. Record the selected versions and resolve their documented compatibility before building. A globally installed Gradle or arbitrary JDK is not a substitute for the project's toolchain. Use Studio's actual SDK location rather than assuming that every workstation has the default path.

Install Android Studio and the SDK components for the selected platform/image through the setup wizard and SDK Manager. Keep platform tools, the emulator runtime, the platform and any required build tools identifiable. The Android CLI can inspect packages with `android sdk list`. Its package paths use slash-separated names. Select exact packages through current help or the IDE, without copying old command-line-tool layouts or guessing an image revision.

Common SDK locations are `%LOCALAPPDATA%\Android\Sdk`, `~/Library/Android/sdk` and `~/Android/Sdk`. These are discovery hints, not facts about a particular host. Make the selected SDK tools discoverable in that terminal and check the actual executable/version when Studio and terminal disagree.

## Acceleration and host-specific checks

| Host | Establish before boot | Failure to investigate |
| --- | --- | --- |
| Windows | Supported x86-64 machine, firmware virtualization, Windows Hypervisor Platform enabled and restart completed if needed | Disabled firmware support, unavailable hypervisor, conflicting host virtualization configuration or graphics driver |
| macOS | Compatible native Studio/runtime, Hypervisor.Framework and guest architecture matching the host | Wrong image ABI, unsupported runtime/OS or insufficient resources |
| Linux | Supported x86-64 machine, KVM installed, `/dev/kvm` present and accessible to the current user | Missing virtualization, incorrect group/session permissions or runner without exposed KVM |

The official acceleration guide still documents this emulator-runtime diagnostic. At the common default paths, run the appropriate command after confirming the path:

```powershell
& "$env:LOCALAPPDATA\Android\Sdk\emulator\emulator.exe" -accel-check
```

```bash
"$HOME/Library/Android/sdk/emulator/emulator" -accel-check
```

```bash
"$HOME/Android/Sdk/emulator/emulator" -accel-check
```

Use its result as a diagnostic, not proof that the guest booted or the GPU works. The baseline Windows recommendation is WHPX. The separate AEHD driver has an announced December 31, 2026 sunset, so do not build a new setup around it. Do not recommend disabling host security controls as a generic emulator repair.

Use the distro's documented KVM setup and log in again if group membership changes require it. Do not solve permissions with globally writable KVM devices or privileged execution of the whole development environment. Check the actual runner's supported virtualization instead of assuming that a cloud VM, Docker or WSL configuration is equivalent to the native host.

## Create a repeatable device

Use Device Manager to select the required API/image/ABI and record the hardware profile, density, resolution, memory/storage, navigation mode and locale. Host-native accelerated images are x86-family on Intel/AMD and ARM64 on Apple silicon. A successfully booted image can still lack the application's native-library ABI.

For current Android CLI management:

```text
android --version
android emulator create --list-profiles
android emulator create medium_phone
android emulator list
```

`medium_phone` is a documented example profile. Read the actual output and select the resulting AVD name before starting it:

```text
android emulator start --cold AVD_NAME
```

Replace `AVD_NAME` with that listed name. `--headless` is available for a prepared noninteractive host. Cold start skips the saved boot snapshot. It does not wipe the application or choose the desired Android API for you. Use the IDE's exact image selection when the requested matrix cannot be expressed through the documented profile interface.

Do not launch two workers against one writable AVD. Give each worker its own device and artifact directory. Build-managed devices can manage an existing project's configured test device lifecycle. The researched feature starts at API 27, so it cannot by itself cover a lower application minimum. Discover the real task name rather than assuming the device/profile name creates a Gradle task automatically.

## Identify and prepare the target

```text
adb devices -l
adb -s SERIAL get-state
adb -s SERIAL shell getprop sys.boot_completed
```

Substitute the inspected serial. Confirm Android reports completed boot, finish any setup/lock screen and check the actual application can start. The transport state `device` is necessary but does not establish UI readiness. Resolve `offline`, `unauthorized` or multiple-device ambiguity before installation.

For physical USB devices, use a data-capable cable, authorized USB debugging and required Windows OEM drivers or Linux USB rules. macOS normally needs no additional USB driver. A USB authorization prompt needs the device owner's action. Prefer the documented paired wireless-debugging flow where appropriate and remove access after testing a borrowed device.

Install the correct APK or complete split set. `INSTALL_FAILED_NO_MATCHING_ABIS` points to native libraries. Signature conflicts need matching signing identity or a separately planned clean install. A clean install cannot validate preserved-data migration. Check free storage and API support when installation fails. Do not hide these failures by accepting an install command that returned an error.

## Connect to the actual backend

The emulator's `127.0.0.1` is its own loopback. The standard Android Emulator provides `10.0.2.2` as an alias to the workstation's loopback. This is not a universal physical-device or remote-cloud address. Check listener, firewall, DNS, proxy and TLS separately from application validation.

For a controlled local test backend on TCP 8080, an ADB reverse mapping is another explicit option:

```text
adb -s SERIAL reverse tcp:8080 tcp:8080
adb -s SERIAL reverse --list
```

Verify the intended mapping and remove only that mapping when finished with `adb -s SERIAL reverse --remove tcp:8080`. A remote lab requires its own documented network path. Do not expose a private service publicly or disable release TLS verification to make a test pass.

## Diagnose the first failed stage

Separate host acceleration, guest boot, ADB, installation, app startup, backend reachability and assertion failure. Record the first actual error, selected device and relevant logs. Choose a repair for that stage. Repeated full wipes can erase reproduction state while leaving a host or network problem untouched.

See [source notes](sources.md) for official setup, acceleration, ADB, networking and managed-device contracts.

## Disposable writable data and stale AVD references

Inspect the selected AVD's real data path when it points to a missing scratch directory. A stale
reference is not an acceleration or app defect. Create an owned test device through current management
tools, preserving other devices. Advanced runtime disk overrides require the installed emulator's
actual help. Separate writable images and snapshots deliberately. Cold boot alone does not clear
or isolate saved user data. See [release-device isolation](release-bundle-testing.md#own-the-emulators-writable-data).
