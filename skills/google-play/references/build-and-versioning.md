# Compile, sign, and increment the bundle

## Current submission baseline

Verified on **2026-11-05** against the current target-API and Billing policy pages:

| Actual new/update target | Current submission target API floor |
| --- | --- |
| Ordinary mobile app | Android 16 / API 36 |
| Wear OS | Android 15 / API 35 |
| Android TV | Android 14 / API 34 |
| Android Automotive OS | Android 15 / API 35 |
| Android XR | Android 14 / API 34 |

The listed 2026 extension deadline was November 1, 2026, which has passed at this verification
date. Do not present a deadline extension as still available without actual account evidence.
Existing-app discoverability floors are a different rule from new/update submission floors.
Check the real form factor and release date before implementation.

For apps using Play Billing, version 7's extension expired November 1, 2026. The current supported
timeline includes Billing 8 through its August 31, 2027 ordinary deadline and Billing 9 through
August 31, 2028. Prefer the latest compatible maintained client/SDK, with its actual manifest and
integration verified. These are eligibility limits, not a reason to add deprecated-client branches.
Native libraries must also satisfy the applicable page-size/ABI requirements and real device tests.

## Inspect the actual project

Read build instructions, `gradle-wrapper.properties`, Android Gradle Plugin, Kotlin/Java versions, product flavors, application IDs/suffixes, build types, dependency lockfiles, NDK/native libraries, and CI signing. Use the committed Gradle wrapper. Respect the project toolchain rather than replacing it with an arbitrary globally installed Gradle.

Check current target API submission deadlines, supported SDK levels, Billing Library deadlines, 64-bit/native-library requirements, and 16 KB page-size requirements where applicable. These depend on release date and form factor. Record the exact active requirement and source rather than hardcoding an obsolete target level into the skill.

## Version allocation

`versionCode` is a positive integer with Play maximum **2,100,000,000**. `versionName` is the human-readable release version. Every new artifact upload uses a fresh code according to this skill's strict monotonic policy, including internal testing and a newly rebuilt retry.

Under a CI concurrency lock keyed by package, read all tracks and their version codes, uploaded bundles/APKs available through the current edit/API, the console's historical maximum if API visibility is incomplete, pending uploads, and CI reservations. Paginate fully and preserve allocation records beyond individual workflow runs. Do not derive the next code solely from the current production release.

After the complete remote/pending/reserved inventory, choose the next positive integer above the known maximum and within Play's supported range. Reserve it atomically under the existing allocation lock and write the real build source. A local calculation alone is not a lock, and no version-code script is bundled.

## Explicit Gradle integration

Passing `-PversionCode` does nothing unless the project reads that property. A Kotlin DSL example for a project deliberately adopting these names:

```kotlin
val releaseVersionCode = providers.gradleProperty("releaseVersionCode")
    .map(String::toInt)

val releaseVersionName = providers.gradleProperty("releaseVersionName")

android {
    defaultConfig {
        versionCode = releaseVersionCode.get()
        versionName = releaseVersionName.get()
    }
}
```

Integrate with the existing version source and debug workflow rather than pasting a second `android` block. Validate range before building and account for variant overrides. For Flutter, React Native, Unity, or another build system, use its documented version propagation and inspect the final Android manifest rather than assuming a platform-neutral version field was applied.

```bash
./gradlew test lint bundleRelease \
  -PreleaseVersionCode="$NEXT_VERSION_CODE" \
  -PreleaseVersionName="$RELEASE_VERSION"
```

Both properties are required by the example's configuration-time `get()` calls, even for a test-only
invocation. Supply them to each separate Gradle invocation using this configuration. Do not add an
invented version fallback to conceal a missing release input. Validate and set the two shell values
before running the command.

Choose the actual flavored task, such as the project's release variant, instead of assuming every project has `bundleRelease`. Avoid blanket task names if they would test unrelated unsupported variants. Android App Bundles are the normal new-app release format. Use APK only for a specifically supported legacy/distribution case.

## Signing and verification

Use a release upload keystore from the approved secret store and the correct alias/certificate. Configure passwords through the project's secure mechanism without printing them. Debug signing is not release signing. With Play App Signing, verify that the upload certificate registered with Play matches CI and that API restrictions such as OAuth fingerprints use the distributed app signing certificate when appropriate.

Run the official `bundletool validate --bundle=<path>` with a pinned compatible tool. Inspect bundle manifest package, versionCode, versionName, min/target SDK, permissions, exported components, debuggable flag, supported ABIs, device features, and delivery modules. Inspect signing with appropriate Java signing tools for the AAB and APK tooling for APKs. Preserve SHA-256, mapping files, native symbols, and version metadata.

Test release mode on representative phone, tablet, foldable, and each selected special form factor. Include cold start, offline/error states actually specified by the product, login/deletion, accessibility, background behavior, billing/restore, deep links, permissions, and backend environments. Verify large-screen/resizable behavior without stretching or disabling it to hide layout failures.

## CI release structure

Use restricted short-lived credentials, a pinned wrapper/toolchain, dependency caches keyed by lockfiles, an allocation lock, protected release inputs, and secret-free logs. Keep build/sign/upload and track-promotion separate enough to identify failure states. Retain restricted artifacts with clear expiration. Publish only the requested package/track/countries/rollout.

A failed edit commit does not prove the binary was never accepted. Re-read artifact/track state before allocating the next attempt. A resumable upload continuation uses the same upload session. A new artifact upload reserves a new code. To recover a bad public build, halt the staged rollout where supported and create a forward-fix build with a higher code. Do not try to replace an uploaded bundle in place or distribute an older code as a rollback.
