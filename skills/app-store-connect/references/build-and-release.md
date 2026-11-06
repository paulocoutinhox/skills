# Build, sign, upload, and number releases

## Establish the build matrix

Read the repository's own build commands and CI. Inspect `xcodebuild -version`, `xcodebuild -list -json`, `xcodebuild -showBuildSettings`, and `xcodebuild -showdestinations` for the selected project or workspace and shared scheme. Resolve dependencies with the project's lockfiles. Confirm the current required Xcode/SDK versions on Apple's submission requirements page before selecting a runner.

Verified submission baseline on **2026-11-05**: Apple's current requirements require Xcode 26 or
later with the applicable iOS/iPadOS/tvOS/visionOS/watchOS 26 SDK since April 28, 2026.
iOS/iPadOS uploads must target iOS 13 or later since September 9, 2026. These are submission floors,
not a recommendation to add old-target compatibility code. Use the actual project's supported
deployment policy and latest compatible production toolchain. Do not infer a native Mac SDK floor
from an iOS-only condition. Confirm current native-Mac requirements separately.

Current age-rating answers must be complete under the updated system. Inspect macOS packages for
unintended `com.apple.quarantine` attributes and actual signing/upload validation. SDK/toolchain,
privacy/required-reason declarations and age/compliance tasks can independently block an upload.

| Store platform | Connect enum | Archive destination | SDK | Validation focus |
| --- | --- | --- | --- | --- |
| iPhone and iPad | `IOS` | `generic/platform=iOS` | `iphoneos` | Device families, orientation, permission strings, all screen layouts |
| Mac | `MAC_OS` | `generic/platform=macOS` | `macosx` | App Sandbox, signing, entitlements, Intel/Apple silicon policy |
| Apple TV | `TV_OS` | `generic/platform=tvOS` | `appletvos` | Remote focus, safe areas, TV assets and playback |
| Apple Vision Pro | `VISION_OS` | `generic/platform=visionOS` | `xros` | Windows/volumes/immersion, input, comfort and motion declaration |

Mac Catalyst is a distinct build destination/variant of the actual Xcode project. Do not substitute a native macOS archive blindly. iOS compatibility on Mac or Vision Pro is a separate availability choice from shipping a native platform build. A watchOS companion is archived with its containing app according to the target graph. There is no `WATCH_OS` Connect platform enum in this snapshot.

## Allocate a new build for every upload

Marketing version (`CFBundleShortVersionString`) and build number (`CFBundleVersion`) are different. For each upload, query all relevant app builds/pre-release versions and current upload records, paginate completely, include pending/in-flight and locally reserved builds, and acquire the project's CI allocation lock. Use a monotonically increasing team policy, even when a narrower platform/version scope would technically allow reuse.

For a selected numeric build policy, compare one-to-three-component values numerically, not lexically. For example, 1.9.99 precedes 1.10.0. Respect the actual Apple component constraints and project policy. Read all remote/pending/reserved values under the existing allocation lock and reserve the selected candidate durably. No candidate calculator is bundled.

Reserve the candidate atomically in the CI allocation store before starting a build. Write it to the actual build configuration, not just a text manifest. Propagate the intended version/build to embedded extensions and companion targets. Inspect the built bundle metadata and re-read pending remote state before upload. A local numeric comparison is not a concurrency lock. Failed or uncertain uploads remain reserved until reconciled. A new upload gets a new reserved value. To continue an existing resumable upload, use its recorded upload ID rather than starting another one under the same number.

## Signing and archive

Use the team's distribution signing identity and provisioning strategy. Automatic signing requires configured credentials and explicit permission for provisioning updates. Manual signing requires matching profiles for every bundle. Never log certificate passwords, export private keys into the repository, or replace the team's established signing setup gratuitously.

Template for an already configured workspace and scheme:

```bash
xcodebuild \
  -workspace "$WORKSPACE" \
  -scheme "$SCHEME" \
  -configuration Release \
  -destination "$ARCHIVE_DESTINATION" \
  -archivePath "$ARCHIVE_PATH" \
  MARKETING_VERSION="$RELEASE_VERSION" \
  CURRENT_PROJECT_VERSION="$NEXT_BUILD" \
  archive

xcodebuild \
  -exportArchive \
  -archivePath "$ARCHIVE_PATH" \
  -exportPath "$EXPORT_PATH" \
  -exportOptionsPlist "$EXPORT_OPTIONS"
```

Use `-project` instead of `-workspace` when appropriate. Set all quoted variables from validated paths and discovered project settings. Run applicable unit, integration, UI, accessibility, entitlement, and release-mode tests. Validate privacy manifests and required-reason APIs, embedded frameworks, symbol files, asset catalogs, encryption declarations, and permission-purpose strings. Test the signed app on representative devices. A simulator binary cannot be uploaded as a release binary.

`assets/export-options.plist` uses `method: app-store-connect` and disables exporter-managed version changes. Replace its team placeholder and choose the actual signing settings. Inspect the installed Xcode's supported export keys instead of assuming the template is sufficient for every target.

## Diagnose export credentials before rebuilding

Treat these as separate capabilities: App Store Connect metadata/upload access, Certificates,
Identifiers & Profiles access, and permission to use cloud-managed distribution certificates.
An App Manager role or successful JWT request does not by itself prove the signing grant needed by
Xcode. Read the first export error and the archive's actual team/signing settings.

| Observation | Next check/action | Avoid |
| --- | --- | --- |
| Archive succeeded, export failed on cloud signing | Inspect the selected Xcode credential and cloud-signing permission | Rebuilding unchanged source or removing push entitlements |
| API-key flags were supplied | `-authenticationKeyPath`, ID and issuer select that key for provisioning | Assuming an already signed-in owner account is used instead |
| A suitable owner/team account is already configured in Xcode | Within the authorized signing operation, retry export of the same archive using that account, without the API-key override | Exporting a private key or creating a replacement certificate unnecessarily |
| Profiles or entitlements differ | Compare every bundle ID, team, profile and distribution entitlement | Accepting a development profile for production push |
| No credential has the required permission | Preserve the archive and report the specific owner/permission handoff | Treating a code change as a signing-account repair |

`xcodebuild -help` in Xcode 27.2 documents `-allowProvisioningUpdates` as allowing profile/app-ID/
certificate operations with the configured account or supplied authentication key. Use it only in
the intended provisioning scope. It is not a generic fix for every export error. Keep automatic and
manual signing choices consistent with the archive. Re-exporting the same unchanged archive after
an authentication repair does not itself require compiling a new binary.

Inspect the exported IPA, not only the archive: actual version/build, code signature, team,
embedded provisioning profile, `get-task-allow`, distribution entitlements and relevant SDK resources.
Retain matching dSYMs and artifact hashes. A successful exporter exit does not demonstrate purchase,
notification or other hardware/service behavior.

### Keep keys at their original location

The Xcode 27.2 `altool --help` advertises `--api-key`, `--api-issuer` and an `API_PRIVATE_KEYS_DIR`
lookup for `AuthKey_<Key-ID>.p8`. Set that environment variable to the existing approved directory for
this invocation, with a correctly quoted path. Do not copy the key into the repository's `private_keys`
folder just to satisfy default lookup. Record the uploader and supported options actually used.
Private key lookup, account identity and app/binary identity need separate verification.

### Reconcile an upload reserved during export

Before allocating another number after an uncertain upload, read the app's builds and
`GET /v1/apps/{id}/buildUploads`, following all pages. Inspect an exact upload through
`GET /v1/buildUploads/{id}` and its files when needed. The 4.6 contract has no collection-wide
`GET /v1/buildUploads` operation. Match app, platform, marketing version, build number and returned
upload identity, not just a recent timestamp.

A preflight can leave an awaiting-upload record. Determine whether the documented uploader is
continuing that recorded upload or a genuinely new transfer. Do not delete the pending record,
reuse a consumed number for a new artifact or assume an awaiting record is a valid processed build.
Keep reservation, transfer, processing and selected-build evidence together. Terminal processing
errors need their actual details. A lost local stdout log is not evidence that Apple received nothing.

## Upload and processing

Prefer the supported Xcode distribution workflow, Transporter, or an installed `altool` workflow whose help confirms platform support. An iOS example is:

```bash
xcrun altool --upload-app \
  -f "$IPA_PATH" \
  --api-key "$ASC_KEY_ID" \
  --api-issuer "$ASC_ISSUER_ID"
```

Arrange the private key through the tool's documented secure lookup. Confirm supported file types and platform options for macOS, tvOS, and visionOS using current tool help. Do not invent an `altool --type visionos` flag or use iOS packaging assumptions for a Mac package.

The 4.6 API also documents `/v1/buildUploads` and `/v1/buildUploadFiles`. Query their create/update schemas before choosing a direct upload integration. A build upload identifies the app, platform, marketing version, and build number. File uploads describe the actual filename, size, UTI, and asset type and return upload operations. Respect the required asset-description/package protocol. A generic POST of an IPA to `/v1/builds` is not a documented upload method. Do not claim a direct-upload implementation exists until the complete protocol is implemented and tested.

Poll upload and build processing with bounded intervals. Distinguish transfer success, validation failure, processing, valid build, missing export compliance, beta eligibility, and version eligibility. Record provider messages and stop on terminal failures. After processing, associate the correct build to the correct platform's editable store version. Never choose the first returned build without checking version, platform, number, and processing state.

## CI design

Use a supported macOS runner and the chosen Xcode version, dependency cache keyed by lockfiles, isolated temporary keychain, ephemeral signing material, restricted credentials, and a concurrency group keyed by app identity. Keep signing and release logs redacted. Retain sanitized build receipts, hashes, dSYMs, and validation summaries in restricted artifacts with retention limits.

Separate verification, build, upload, review submission, and public release jobs. Connect each stage to the explicit release scope rather than defaulting every branch push to production. Clean up temporary credentials after the job. Mac App Store distribution and external Developer ID notarization are distinct release paths. Do not add notarization steps as a substitute for Mac App Store review.
