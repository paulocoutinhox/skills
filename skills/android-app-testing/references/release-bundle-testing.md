# Test the exact release bundle on an isolated device

Read this when the deliverable is a signed AAB or an app-store release, rather than a Debug APK.
A separately assembled APK can differ from the uploaded bundle. Preserve the AAB hash and generate
its test APKs with the project's supported bundletool version. Installation is not a billing test.

## Verify provenance, package and signing

1. Record the final AAB path/hash, source revision, version name/code, toolchain and signing evidence.
   Confirm these values from the artifact, not only Gradle arguments or a release manifest.
2. Use the selected bundletool's `validate`, `dump manifest` and `build-apks` help. Validate the AAB
   and inspect its application ID, version, SDK levels, native ABIs, debuggable state and permissions.
3. Generate a device-compatible split set or an intentional universal APK set from that exact AAB.
   Use explicit signing inputs for release-equivalent checks. If omitted, bundletool can select a
   debug key. A valid AAB upload signature does not establish the generated APK signing identity.
4. Install with bundletool's selected-device path or the complete compatible split set. Record the
   APK set and installed package version. Preserve existing data only when signatures permit it.

One native example, after the variables below have been resolved from approved inputs:

```text
java -jar "$BUNDLETOOL_JAR" validate --bundle="$AAB_PATH"
java -jar "$BUNDLETOOL_JAR" dump manifest --bundle="$AAB_PATH" --module=base
java -jar "$BUNDLETOOL_JAR" build-apks --bundle="$AAB_PATH" --output="$APKS_PATH" --mode=universal --ks="$KEYSTORE_PATH" --ks-key-alias="$KEY_ALIAS" --ks-pass=file:"$STORE_PASSWORD_FILE" --key-pass=file:"$KEY_PASSWORD_FILE"
java -jar "$BUNDLETOOL_JAR" install-apks --apks="$APKS_PATH" --device-id="$DEVICE_SERIAL"
```

`APKS_PATH` is a new `.apks` file, not a source-project ZIP deliverable. Password references point to
approved temporary protected files or the project's established secret mechanism. Do not put actual
passwords in argv, print them or commit those files. Preserve original keystores and remove temporary
secret copies after use. A universal APK is convenient for smoke tests, but cannot prove every
Play-delivered dynamic module or device-specific split combination. Inspect the actual installed set.

App signing and upload keys can differ under Play App Signing. A locally generated APK signed with
an upload key need not update a Play-installed app signed by Google's app-signing key. Use a separate
controlled device/profile for that fresh-install test, or install through the intended Play track for
real update/distribution evidence. Do not uninstall the user's app to hide a signature mismatch.

## Own the emulator's writable data

Prefer a dedicated disposable device created through current Device Manager/Android CLI. Discover
and record the actual API, image, ABI and Play capabilities. Do not run two writers against one AVD.
An existing AVD's data-path entry can refer to a deleted scratch directory. Inspect that path before
calling it a guest boot failure. Create a new owned device instead of erasing an unrelated one.

If an installed emulator runtime is deliberately reused with separate writable disk images, verify
its current `-help` for `-data`, `-cache`, `-no-snapshot` and headless options. Use unique task-owned
paths for both writable data/cache and avoid loading/saving the original AVD's snapshots. Never
repurpose `HOME` or overwrite its default `userdata-qemu.img`. A cold boot or `-no-snapshot` alone
does not isolate existing user data. Follow the runtime's current image-initialization contract.

Select the actual serial from `adb devices -l`. Wait for completed boot, an unlocked usable UI,
package manager and target app startup. Keep the instance process/session identifiable. An ADB
transport becoming available is not a ready device. Preserve any initialization or installation error
before a diagnostic retry. Use current management commands rather than inventing an agent CLI flag.

## Exercise the real release and diagnose billing separately

Launch the installed package's actual launcher component. Discover it from package/manifest tooling
instead of assuming a framework Activity name. Verify startup, free/inactive boundaries, core flows,
permission/consent handling, native SDK screens, offline/error states and background/resume behavior.
Record genuine UI captures and relevant bounded logs after each meaningful state transition.

For Play billing, establish a supported Play image/account, correct store account, configured license
tester, eligible release/install path, region, active product/base plan and actual backend credentials.
License testers can use the documented sideload testing path when its package/account requirements
are met. An ordinary test-track user can still incur real charges, so confirm the actual test account
and payment method before testing a transaction. Read the SDK's full diagnostic context.
A device/user-not-allowed error on an unsigned-in isolated
emulator does not prove a bad product mapping. It also does not establish a successful purchase flow.
Report the error and unexecuted transaction cases. Do not enable a fake entitlement to pass the test.

A visible paywall can be a fallback or show no store products. Inspect the actual packages, localized
prices and entitlement refresh. Test purchase/restore with a suitable account when available. Keep
native button reachability, an initiated billing sheet and a verified transaction as separate evidence.

## Cleanup without discarding release evidence

Stop the owned emulator, wait for its disk writes to end and remove only its disposable images,
fixtures and temporary secret files. Remove only task-created ADB reverse mappings. Keep final signed
artifacts, hashes, matching symbols/mappings and a sanitized test receipt as needed. Do not erase a
shared AVD, user login/profile, global SDK cache or original signing files as routine cleanup.
