# Build, sign, upload, and number releases

## Establish the build matrix

Read the repository's own build commands and CI. Run `xcodebuild -version`, `xcodebuild -list -json`, `xcodebuild -showBuildSettings`, and `xcodebuild -showdestinations` for the chosen project or workspace and shared scheme. Resolve dependencies with the project's lockfiles. Check the current required Xcode and SDK versions on Apple's submission requirements page before you choose a runner.

Submission baseline checked on **2026-11-05**: Apple's current rules require Xcode 26 or later with
the matching iOS/iPadOS/tvOS/visionOS/watchOS 26 SDK since April 28, 2026. iOS/iPadOS uploads must
target iOS 13 or later since September 9, 2026. These are minimums for submission, not advice to add
code for old targets. Use the project's real deployment policy and the latest compatible production
toolchain. Do not take a native Mac SDK minimum from a rule that is only about iOS. Check current
native Mac requirements on their own.

Current age-rating answers must be complete under the updated system. Check macOS packages for
unwanted `com.apple.quarantine` attributes and run real signing and upload validation. SDK and
toolchain, privacy and required-reason declarations and age and compliance tasks can each block an
upload on their own.

| Store platform | Connect enum | Archive destination | SDK | Validation focus |
| --- | --- | --- | --- | --- |
| iPhone and iPad | `IOS` | `generic/platform=iOS` | `iphoneos` | Device families, orientation, permission strings, all screen layouts |
| Mac | `MAC_OS` | `generic/platform=macOS` | `macosx` | App Sandbox, signing, entitlements, Intel/Apple silicon policy |
| Apple TV | `TV_OS` | `generic/platform=tvOS` | `appletvos` | Remote focus, safe areas, TV assets and playback |
| Apple Vision Pro | `VISION_OS` | `generic/platform=visionOS` | `xros` | Windows/volumes/immersion, input, comfort and motion declaration |

Mac Catalyst is its own build destination or variant in the real Xcode project. Do not swap in a native macOS archive without checking. Making an iOS app available on Mac or Vision Pro is a separate availability choice from shipping a native build for that platform. A watchOS companion is archived with the app that contains it, following the target structure. There is no `WATCH_OS` Connect platform enum in this snapshot.

## Allocate a new build for every upload

The marketing version (`CFBundleShortVersionString`) and the build number (`CFBundleVersion`) are different. For each upload, query all relevant app builds, pre-release versions and current upload records, read every page, include pending, in-progress and locally reserved builds, and take the project's CI allocation lock. Use an always-increasing team policy, even when a narrower platform or version scope would technically allow reuse.

For a numeric build policy, compare values with one to three parts as numbers, not as text. For example, 1.9.99 comes before 1.10.0. Follow Apple's real limits on each part and the project policy. Read all remote, pending and reserved values while holding the existing allocation lock, and save the chosen number so the reservation lasts. No number calculator is included.

Reserve the number in one step in the CI allocation store before you start a build. Write it to the real build configuration, not only to a text manifest. Pass the intended version and build to embedded extensions and companion targets. Check the built bundle's metadata and read the pending remote state again before uploading. A local number comparison is not a lock against parallel runs. Failed or uncertain uploads keep their number reserved until you have checked what happened. A new upload gets a new reserved number. To continue an existing resumable upload, use its recorded upload ID instead of starting another one with the same number.

## Signing and archive

Use the team's distribution signing identity and provisioning approach. Automatic signing needs set-up credentials and clear permission to update provisioning. Manual signing needs matching profiles for every bundle. Never log certificate passwords, export private keys into the repository, or replace the team's existing signing setup without a reason.

Template for a workspace and scheme that are already set up:

```bash
xcodebuild -workspace "$WORKSPACE" -scheme "$SCHEME" -configuration Release -destination "$ARCHIVE_DESTINATION" -archivePath "$ARCHIVE_PATH" MARKETING_VERSION="$RELEASE_VERSION" CURRENT_PROJECT_VERSION="$NEXT_BUILD" archive
xcodebuild -exportArchive -archivePath "$ARCHIVE_PATH" -exportPath "$EXPORT_PATH" -exportOptionsPlist "$EXPORT_OPTIONS"
```

Use `-project` instead of `-workspace` when that fits. Set all quoted variables from checked paths and the project settings you found. Run the unit, integration, UI, accessibility, entitlement, and release-mode tests that apply. Check privacy manifests and required-reason APIs, embedded frameworks, symbol files, asset catalogs, encryption declarations, and permission-purpose strings. Test the signed app on typical devices. A simulator binary cannot be uploaded as a release binary.

`assets/export-options.plist` uses `method: app-store-connect` and turns off version changes by the exporter. Replace its team placeholder and choose the real signing settings. Check which export keys the installed Xcode supports instead of assuming the template is enough for every target.

## Diagnose export credentials before rebuilding

Treat these as separate permissions: App Store Connect metadata and upload access, Certificates,
Identifiers & Profiles access, and permission to use cloud-managed distribution certificates.
An App Manager role or a working JWT request does not prove by itself that Xcode has the signing
permission it needs. Read the first export error and the archive's real team and signing settings.

| Observation | Next check/action | Avoid |
| --- | --- | --- |
| Archive succeeded, export failed on cloud signing | Check the Xcode credential in use and the cloud-signing permission | Rebuilding unchanged source or removing push entitlements |
| API-key flags were supplied | `-authenticationKeyPath`, ID and issuer select that key for provisioning | Assuming the owner account that is already signed in is used instead |
| A suitable owner/team account is already set up in Xcode | Within the allowed signing operation, export the same archive again with that account, without the API-key override | Exporting a private key or creating a replacement certificate without need |
| Profiles or entitlements differ | Compare every bundle ID, team, profile and distribution entitlement | Accepting a development profile for production push |
| No credential has the required permission | Keep the archive and report the specific owner or permission handoff | Treating a code change as a fix for the signing account |

`xcodebuild -help` in Xcode 27.2 says `-allowProvisioningUpdates` allows profile, app-ID and
certificate operations with the set-up account or the supplied authentication key. Use it only in
the intended provisioning scope. It is not a general fix for every export error. Keep automatic and
manual signing choices consistent with the archive. Exporting the same unchanged archive again after
fixing sign-in does not by itself require building a new binary.

Check the exported IPA, not only the archive: real version and build, code signature, team,
embedded provisioning profile, `get-task-allow`, distribution entitlements and relevant SDK
resources. Keep the matching dSYMs and file hashes. A successful exit from the exporter does not show
that purchases, notifications or other hardware or service features work.

### Keep keys at their original location

The Xcode 27.2 `altool --help` lists `--api-key`, `--api-issuer` and an `API_PRIVATE_KEYS_DIR`
lookup for `AuthKey_<Key-ID>.p8`. Set that environment variable to the existing approved folder for
this run, with a correctly quoted path. Do not copy the key into the repository's `private_keys`
folder just to match the default lookup. Record the uploader and the supported options you really
used. Private key lookup, account identity and app/binary identity each need their own check.

### Fix an upload reserved during export

Before you reserve another number after an uncertain upload, read the app's builds and
`GET /v1/apps/{id}/buildUploads`, following all pages. Look at a specific upload through
`GET /v1/buildUploads/{id}` and its files when needed. The 4.6 contract has no collection-wide
`GET /v1/buildUploads` operation. Match the app, platform, marketing version, build number and the
returned upload identity, not just a recent timestamp.

A preflight can leave a record that is waiting for upload. Find out whether the documented uploader
is continuing that recorded upload or starting a really new transfer. Do not delete the pending
record, reuse a used number for a new file or assume a waiting record is a valid processed build.
Keep the evidence for reservation, transfer, processing and selected build together. Final
processing errors need their real details. A lost local stdout log does not prove that Apple received
nothing.

## Upload and processing

Prefer the supported Xcode distribution workflow, Transporter, or an installed `altool` workflow whose help confirms platform support. An iOS example is:

```bash
xcrun altool --upload-app -f "$IPA_PATH" --api-key "$ASC_KEY_ID" --api-issuer "$ASC_ISSUER_ID"
```

Provide the private key through the tool's documented secure lookup. Check supported file types and platform options for macOS, tvOS, and visionOS in the current tool help. Do not make up an `altool --type visionos` flag or apply iOS packaging assumptions to a Mac package.

The 4.6 API also documents `/v1/buildUploads` and `/v1/buildUploadFiles`. Read their create and update schemas before choosing a direct upload integration. A build upload names the app, platform, marketing version, and build number. File uploads describe the real filename, size, UTI, and asset type and return upload operations. Follow the required asset-description and package protocol. A generic POST of an IPA to `/v1/builds` is not a documented upload method. Do not claim a direct upload works until the full protocol is built and tested.

Poll upload and build processing at limited intervals. Tell apart transfer success, validation failure, processing, valid build, missing export compliance, beta eligibility, and version eligibility. Record provider messages and stop on final failures. After processing, link the correct build to the correct platform's editable store version. Never pick the first returned build without checking version, platform, number, and processing state.

## CI design

Use a supported macOS runner and the chosen Xcode version, a dependency cache keyed by lockfiles, a separate temporary keychain, short-lived signing material, limited credentials, and a concurrency group keyed by app identity. Hide secrets in signing and release logs. Keep cleaned build receipts, hashes, dSYMs, and validation summaries as restricted artifacts with retention limits.

Keep verification, build, upload, review submission, and public release as separate jobs. Tie each stage to the release scope the user set, instead of sending every branch push to production by default. Remove temporary credentials after the job. Mac App Store distribution and outside Developer ID notarization are different release paths. Do not add notarization steps in place of Mac App Store review.
