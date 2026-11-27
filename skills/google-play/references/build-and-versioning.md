# Compile, sign, and increment the bundle

## Current submission baseline

Checked on **2026-11-05** against the current target-API and Billing policy pages:

| Actual new/update target | Current submission target API floor |
| --- | --- |
| Ordinary mobile app | Android 16 / API 36 |
| Wear OS | Android 15 / API 35 |
| Android TV | Android 14 / API 34 |
| Android Automotive OS | Android 15 / API 35 |
| Android XR | Android 14 / API 34 |

The listed 2026 extension deadline was November 1, 2026, which had already passed on the check
date. Do not say a deadline extension is still available unless the account really shows it.
The minimum levels for existing apps to stay discoverable are a different rule from the minimum
levels for new apps and updates. Check the real form factor and release date before you build.

For apps that use Play Billing, the extension for version 7 ended on November 1, 2026. The current
supported timeline includes Billing 8 up to its normal deadline of August 31, 2027, and Billing 9 up
to August 31, 2028. Prefer the latest compatible, maintained client or SDK, and check its real
manifest and integration. These are eligibility limits, not a reason to add code paths for
deprecated clients. Native libraries must also meet the page-size and ABI rules that apply and pass
real device tests.

## Inspect the actual project

Read the build instructions, `gradle-wrapper.properties`, Android Gradle Plugin, Kotlin/Java versions, product flavors, application IDs and suffixes, build types, dependency lockfiles, NDK and native libraries, and CI signing. Use the committed Gradle wrapper. Respect the project toolchain instead of swapping in some globally installed Gradle.

Check the current target API submission deadlines, supported SDK levels, Billing Library deadlines, 64-bit and native-library rules, and 16 KB page-size rules where they apply. These depend on release date and form factor. Record the exact rule in force and its source instead of hardcoding an outdated target level into the skill.

## Version allocation

`versionCode` is a positive integer with a Play maximum of **2,100,000,000**. `versionName` is the release version people read. Under this skill's strict always-increasing policy, every new artifact upload uses a fresh code, including internal testing and a newly rebuilt retry.

While holding a CI lock for the package, read all tracks and their version codes, the uploaded bundles and APKs you can see through the current edit or API, the console's highest code ever used if the API does not show everything, pending uploads and CI reservations. Read every page, and keep allocation records beyond single workflow runs. Do not work out the next code only from the current production release.

After you have the full list of remote, pending and reserved codes, choose the next positive integer above the known maximum and within Play's supported range. Reserve it in one step under the existing allocation lock and write it into the real build source. A local calculation alone is not a lock, and no version-code script is included.

## Explicit Gradle integration

Passing `-PversionCode` does nothing unless the project reads that property. Here is a Kotlin DSL example for a project that chooses to use these names:

```kotlin
val releaseVersionCode = providers.gradleProperty("releaseVersionCode").map(String::toInt)

val releaseVersionName = providers.gradleProperty("releaseVersionName")

android {
    defaultConfig {
        versionCode = releaseVersionCode.get()
        versionName = releaseVersionName.get()
    }
}
```

Fit this into the existing version source and debug workflow instead of pasting a second `android` block. Check the range before building, and allow for variant overrides. For Flutter, React Native, Unity or another build system, use its documented way of passing the version, and inspect the final Android manifest instead of assuming a platform-neutral version field was applied.

```bash
./gradlew test lint bundleRelease -PreleaseVersionCode="$NEXT_VERSION_CODE" -PreleaseVersionName="$RELEASE_VERSION"
```

The example's `get()` calls run at configuration time, so both properties are required, even when
you only run tests. Pass them to every separate Gradle run that uses this configuration. Do not add
a made-up version fallback to hide a missing release input. Check and set the two shell values
before you run the command.

Choose the real flavored task, such as the project's release variant, instead of assuming every project has `bundleRelease`. Avoid catch-all task names if they would test unrelated, unsupported variants. Android App Bundles are the release format. Use an APK only for a distribution channel that requires one.

## Signing and verification

Use a release upload keystore from the approved secret store, with the right alias and certificate. Set passwords through the project's secure method without printing them. Debug signing is not release signing. With Play App Signing, check that the upload certificate registered with Play matches CI, and that API restrictions such as OAuth fingerprints use the distributed app signing certificate when that is the right one.

Run the official `bundletool validate --bundle=<path>` with a pinned, compatible tool. Inspect the bundle manifest's package, versionCode, versionName, min and target SDK, permissions, exported components, debuggable flag, supported ABIs, device features and delivery modules. Check signing with the right Java signing tools for the AAB, and APK tools for APKs. Keep the SHA-256, mapping files, native symbols and version metadata.

Test release mode on typical phone, tablet and foldable devices, and on each chosen special form factor. Include cold start, the offline and error states the product really defines, login and deletion, accessibility, background behavior, billing and restore, deep links, permissions and backend environments. Check large-screen and resizable behavior without stretching the layout or turning resizing off to hide layout bugs.

## CI release structure

Use limited short-lived credentials, a pinned wrapper and toolchain, dependency caches keyed by lockfiles, an allocation lock, protected release inputs and logs with no secrets. Keep build, sign and upload separate enough from track promotion that you can tell where a failure happened. Keep restricted artifacts with a clear expiry. Publish only the requested package, track, countries and rollout.

A failed edit commit does not prove the binary was never accepted. Read the artifact and track state again before you pick a code for the next attempt. Continuing a resumable upload uses the same upload session. A new artifact upload reserves a new code. To recover from a bad public build, halt the staged rollout where supported and make a forward-fix build with a higher code. Do not try to replace an uploaded bundle in place, or ship an older code as a rollback.
