# Test the exact release bundle on an isolated device

Read this when the deliverable is a signed AAB or an app-store release, not a Debug APK.
An APK built on its own can differ from the uploaded bundle. Keep the AAB hash and generate
its test APKs with the project's supported bundletool version. Installing is not a billing test.

## Check origin, package and signing

1. Write down the final AAB path/hash, source revision, version name/code, toolchain and signing evidence.
   Confirm these values from the artifact itself, not only from Gradle arguments or a release manifest.
2. Use the chosen bundletool's `validate`, `dump manifest` and `build-apks` help. Validate the AAB
   and check its application ID, version, SDK levels, native ABIs, debuggable state and permissions.
3. Generate a split set that fits the device, or a universal APK set on purpose, from that exact AAB.
   Use explicit signing inputs for release-equal checks. If you leave them out, bundletool can pick a
   debug key. A valid AAB upload signature does not show the signing identity of the generated APK.
4. Install with bundletool's selected-device path or the full matching split set. Write down the
   APK set and installed package version. Keep existing data only when signatures allow it.

One native example, after you have filled in the variables below from approved inputs:

```text
java -jar "$BUNDLETOOL_JAR" validate --bundle="$AAB_PATH"
java -jar "$BUNDLETOOL_JAR" dump manifest --bundle="$AAB_PATH" --module=base
java -jar "$BUNDLETOOL_JAR" build-apks --bundle="$AAB_PATH" --output="$APKS_PATH" --mode=universal --ks="$KEYSTORE_PATH" --ks-key-alias="$KEY_ALIAS" --ks-pass=file:"$STORE_PASSWORD_FILE" --key-pass=file:"$KEY_PASSWORD_FILE"
java -jar "$BUNDLETOOL_JAR" install-apks --apks="$APKS_PATH" --device-id="$DEVICE_SERIAL"
```

`APKS_PATH` is a new `.apks` file, not a source-project ZIP deliverable. Password references point to
approved temporary protected files or the project's existing secret system. Do not put real
passwords in argv, print them or commit those files. Keep the original keystores, and remove temporary
secret copies after use. A universal APK is handy for smoke tests, but it cannot prove every
Play-delivered dynamic module or device-specific split combination. Check the set that was really installed.

App signing and upload keys can differ under Play App Signing. A locally generated APK signed with
an upload key may not update a Play-installed app signed by Google's app-signing key. Use a separate
controlled device/profile for that fresh-install test, or install through the intended Play track for
real update/distribution evidence. Do not uninstall the user's app to hide a signature mismatch.

## Own the emulator's writable data

Prefer a separate throwaway device created through current Device Manager/Android CLI. Find
and write down the real API, image, ABI and Play capabilities. Do not run two writers against one AVD.
An existing AVD's data-path entry can point to a deleted scratch folder. Check that path before
you call it a guest boot failure. Create a new device you own instead of erasing an unrelated one.

If you reuse an installed emulator runtime on purpose with separate writable disk images, check
its current `-help` for `-data`, `-cache`, `-no-snapshot` and headless options. Use unique paths owned
by the task for both writable data and cache, and do not load or save the original AVD's snapshots. Never
reuse `HOME` for this or overwrite its default `userdata-qemu.img`. A cold boot or `-no-snapshot` alone
does not isolate existing user data. Follow the runtime's current image-setup contract.

Pick the real serial from `adb devices -l`. Wait for boot to finish, an unlocked usable UI,
the package manager and target app startup. Keep the instance process/session easy to identify. An ADB
connection becoming available does not mean the device is ready. Keep any setup or install error
before a diagnostic retry. Use current management commands instead of making up an agent CLI flag.

## Exercise the real release and diagnose billing separately

Launch the installed package's real launcher component. Find the activity whose intent filter has
`android.intent.action.MAIN` and `android.intent.category.LAUNCHER` in the `dump manifest` output,
then start it with `adb -s SERIAL shell am start -W -n PACKAGE/ACTIVITY`. Do not guess a framework
Activity name. Check startup, free/inactive limits, core flows, permission/consent handling,
native SDK screens, offline/error states and background/resume behavior.
After each meaningful state change, record real UI captures and short relevant logs.

For Play billing, set up a supported Play image/account, the right store account, a configured license
tester, an eligible release/install path, region, active product/base plan and real backend credentials.
License testers can use the documented sideload testing path when its package/account requirements
are met. An ordinary test-track user can still be charged real money, so confirm the real test account
and payment method before you test a transaction. Read the SDK's full diagnostic context. A
device/user-not-allowed error on an isolated emulator with no signed-in account does not prove a
bad product mapping. It also does not show a successful purchase flow.
Report the error and the transaction cases that did not run. Do not turn on a fake entitlement to
pass the test.

A visible paywall can be a fallback or show no store products. Check the real packages, localized
prices and entitlement refresh. Test purchase/restore with a suitable account when you have one. Keep
native button reachability, an opened billing sheet and a verified transaction as separate evidence.

## Cleanup without discarding release evidence

Stop the emulator you own, wait for its disk writes to finish and remove only its throwaway images,
fixtures and temporary secret files. Remove only ADB reverse mappings the task created. Keep the
final signed artifacts, hashes, matching symbols/mappings and a cleaned test receipt as needed. Do
not erase a shared AVD, user login/profile, global SDK cache or original signing files as routine cleanup.
