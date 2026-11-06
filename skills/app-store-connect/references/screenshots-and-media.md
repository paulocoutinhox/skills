# Screenshots, icons, previews, and uploaded assets

Verified baseline: 2026-11-05. Fetch the current [screenshot specification](https://developer.apple.com/help/app-store-connect/reference/app-information/screenshot-specifications/) before exporting. Device requirements change independently of API enums.

## Required capture plan

Create a matrix of platform, supported device family, display slot, orientation, locale, screenshot order, source capture, export path, dimensions, file format, byte size, and upload resource ID/state. Apple accepts 1–10 screenshots per device size in JPEG/JPG/PNG. Images must have no alpha channel. Use actual product UI in a stable test state without private customer data.

| Slot | Verified pixel examples | Operational rule |
| --- | --- | --- |
| iPhone Dynamic Island, medium | 1179×2556 or 1206×2622, and transposed landscape | Current main required iPhone family. Check the live table's alternative/scaling rules |
| iPhone Dynamic Island, large | 1260×2736, 1290×2796, 1320×2868, and transposed landscape | Optional/alternative family according to current supported layout |
| iPhone Duo outer display | 1398×2034 or 2034×1398 | Capture the actual outer-display layout |
| iPhone Duo inner display | 2007×2853 or 2853×2007 | Capture the actual unfolded layout, not an enlarged phone screenshot |
| iPad 13-inch | 2064×2752 or 2048×2732, and transposed landscape | Required when the app supports iPadOS |
| Mac | 1280×800, 1440×900, 2560×1600, 2880×1800 | Match the specified 16:10 canvas and actual Mac UI |
| Apple TV | 1920×1080 or 3840×2160 | Show TV UI and focus states without clipped safe areas |
| Apple Vision Pro | 3840×2160 | Use supported spatial capture tooling and actual app presentation |
| Apple Watch, when included | Current examples include 422×514 and 410×502 | Select the actual supported watch slot from the live table |

The specification announces Duo screenshots as required starting **April 2027 for apps using iOS
27.1 SDK or later**. The [October 5 announcement](https://developer.apple.com/news/?id=kkphp5qo)
uses broader submission wording. Prepare for the stated SDK condition and verify the actual release
rule at submission. Apple does not give an exact day in these inspected notices. Do not invent one.
Use the current Asset Library's reference data for actual Duo placement groups and specifications.
Those identifiers are dynamic strings, so a device absent from the deprecated `ScreenshotDisplayType`
enum is not proof that the current API cannot target it. Never map Duo to a guessed phone group.
If the required group is genuinely unavailable to the account/API, report the exact gap and use the
documented console handoff rather than inventing support.

### Required assets and Duo capture procedure

Before upload, mark each applicable platform/device family as required, supplied, validated, and
delivered. Include the required iPhone/iPad slots, the applicable April 2027 Duo requirement, and
each selected native platform. A missing required family is an incomplete release, even when the
binary upload succeeds. Do not upload only the easiest phone capture or stretch it into another family.

1. Install/select the Xcode/SDK with actual Duo support, discover its simulator in Device Hub, and
   use the release-equivalent app layout with stable harmless demo content.
2. Select the outer/closed display and intended orientation, navigate the actual app, and capture
   the visible UI. Select the inner/unfolded presentation and capture its actual adapted layout.
3. Inspect transition/reflow, safe areas, text, controls, and absence of private/debug content.
   Device Hub's canvas scale is not the app's logical display geometry.
4. Verify the outer 1398×2034 or landscape transpose and inner 2007×2853 or transpose against the
   live specification. Preserve proportional UI and opaque output. A black or wrong-display capture
   is a capture failure to diagnose, not permission to fabricate or resize an unrelated screen.
5. Repeat the meaningful localized journeys, retain source captures and editable compositions, and
   upload to the actual matching slot. Validate delivered state, ordering, and the product-page preview.

Generic `simctl` capture below is usable only if it captures the intended display correctly in the
selected runtime. Do not invent a display/hinge command flag. Use the supported Device Hub capture
controls and actual local tool help when the default screenshot does not represent the selected pose.

## Capture and design

Use `xcrun simctl list devices available` to discover installed simulators. Boot the intended device and capture with `xcrun simctl io "$DEVICE_UDID" screenshot "$OUTPUT_PATH"` after navigating the actual app. Use platform-appropriate Mac, TV, and Vision Pro capture workflows and inspect their output dimensions. Discover Duo simulators from the installed SDK rather than inventing device names or UDIDs.

Seed reproducible demo content. Hide notifications, personal identities, debug overlays, and test payment details. Show each platform's real layout, controls, typography, and permission behavior. Test folded/unfolded and orientation transitions where supported. Keep titles, captions, device frames, and UI proportionate. Never let a frame conceal the app or crop critical controls.

Create an editable composition master. Generative image tools may create supporting backgrounds or illustrations, not fictional product evidence. Composite genuine captures, concise localized benefit captions, and licensed artwork. Export exact accepted dimensions without stretching. Preserve white/transparent handling required by the actual asset type. Flatten screenshot alpha into the intended opaque background.

Inspect full-size and storefront-size previews for readable type, text overflow, clipped edges, incorrect device frames, distorted UI, misleading claims, and image-to-image consistency. Use a deterministic image inspector such as Pillow or ImageMagick for width, height, format, color mode, alpha, and bytes. Visual review is still required. A file extension does not prove the actual encoding.

## Icons and previews

App icons are built into the platform's asset catalog and validated by Xcode. Use the correct modern icon pipeline for the installed Xcode, including layered/platform-specific assets when required. Do not upload a single arbitrary 1024px PNG as a substitute for all macOS, tvOS, and visionOS icon requirements. Inspect the current icon guide and export validation for the actual target.

App previews are separate video assets with their own orientation, resolution, length, codec/audio, and size requirements. Recheck the current [preview specification](https://developer.apple.com/help/app-store-connect/reference/app-information/app-preview-specifications/). Use real captured experience, accurate localized overlays, licensed sound, and readable thumbnails/poster times. Do not claim one video encoding fits every platform or substitute a promotional trailer for actual app footage without checking policy.

The researched baseline allows up to three previews, 15–30 seconds each, at most 500 MB, maximum 30 fps, with H.264 or ProRes 422 HQ and the specified stereo audio. Mac/TV previews use landscape. Resolve exact device resolution, container, audio sample rate/bit depth, and poster-frame requirements from the current table. Use `ffprobe` or equivalent to inspect actual streams, duration, dimensions, frame rate, rotation, codecs, audio layout, and bytes. A `.mp4` extension alone is insufficient evidence of compliance. Capture the real app experience and verify silent-autoplay readability.

## Current Asset Library workflow

Use the [App Asset Library](https://developer.apple.com/documentation/appstoreconnectapi/app-asset-library) for new screenshots, previews and in-app event media. Set-based screenshot/preview and event-media resources are deprecated. Do not add compatibility code around them or copy their checksum/state contract into the current API.

### Discover specifications and limits

1. Read `GET /v1/apps/{id}/assetLibrary` for the actual library ID.
2. Read `GET /v1/appAssetLibraryRefData`. Inspect `features`, `placementProfileGroups`, `imageSpecs`, `videoSpecs`, `placementTypes` and `displayClasses`. Supported filters/fields can narrow the response for the actual task.
3. Start with the actual feature, such as `APP_STORE_VERSIONS`. Its placement policies describe allowed types and per-group limits. Resolve the target platform/device's group, then that type/group's specification IDs, then the actual image/video specification.
4. Validate dimensions, aspect, extension/MIME, bytes, alpha, video frame rate/duration/audio and accepted asset category. IDs are returned strings, not a permanent locally copied device catalog. A feature absent from the returned catalog is unavailable even if a broader enum names it.

The current App Store version policy permits up to ten screenshots, three previews and one product-page header asset per applicable group. Custom pages, events and experiments have their own limits. The screenshot/preview specification above is editorial planning guidance. Use actual reference data and required-device rules together for the real operation.

### Reserve, transfer, commit and inspect

Reserve with `POST /v1/appAssetLibraryImages` or `POST /v1/appAssetLibraryVideos`. Required attributes are `fileName`, exact `fileSize` and `category`, with the actual `assetLibrary` relationship. Optional `referenceName` helps identify purpose/locale. Videos additionally accept `previewFrameTimeCode`.

Use `APP_SCREENSHOTS_AND_PREVIEWS` for actual app captures/previews and `CREATIVE_ASSETS` only for eligible creative placements. Category is selected at reservation and cannot be changed later. A marketing illustration is not an acceptable substitute for captured screenshot evidence.

Execute every returned upload operation with exact method, URL, headers, byte offset and length. Upload parts only while their reservation/URLs remain valid. Do not send Connect JWTs to the temporary upload host. Reconcile uncertain transfers before resending, and commit only when all parts have succeeded.

Commit with `PATCH /v1/appAssetLibraryImages/{id}` or the video equivalent, setting `uploaded: true`. **The current library request has no `sourceFileChecksum` attribute.** Preserve a local artifact hash for evidence, but do not send the deprecated screenshot request's MD5 field.

Poll the resource: `AWAITING_UPLOAD` is not committed, `UPLOAD_COMPLETE` is processing, `PREPARE_FOR_SUBMISSION` means processing succeeded, and `FAILED` needs actual `stateDetails` investigation and a corrected reservation. Read the returned `specId`, processed image/video and preview-frame status. Never send a fabricated `specId`. A successfully uploaded asset is not yet a visible placement or approved content.

### Place and order media

Create `POST /v1/appAssetLibraryPlacements` with actual `placementType`, returned `placementGroup`, exactly one image/video relationship and exactly one target surface. The normal targets are `appStoreVersionLocalization`, `appCustomProductPageLocalization`, `appEventLocalization` and `appStoreVersionExperimentTreatmentLocalization`. Retention media has its own supported version relationship.

For example, an actual screenshot on an existing editable localization uses this shape:

```json
{
  "data": {
    "type": "appAssetLibraryPlacements",
    "attributes": {
      "placementType": "APP_SCREENSHOT",
      "placementGroup": "<group-returned-by-reference-data>"
    },
    "relationships": {
      "image": {"data": {"type": "appAssetLibraryImages", "id": "<processed-image-id>"}},
      "appStoreVersionLocalization": {
        "data": {"type": "appStoreVersionLocalizations", "id": "<editable-localization-id>"}
      }
    }
  }
}
```

Read the localization's `placements`, filtered to type/group and sorted by `placementGroupPosition`. That is a supported sort key, not a writable/readable position attribute. Set the intended complete order using `POST /v1/appAssetLibraryPlacementOrderingRequests`, with `placementGroup`, ordered `orderedPlacements` relationship IDs and the one target localization. Re-read sorted placements to confirm sequence. Events are not orderable like screenshot galleries because their individual placement types have a single-asset limit.

Placement state follows parent review, including processing, preparation and approval. Submit the actual version/custom-page/event parent as required. Eligible creative assets can also have supported independent review items. A library upload alone is not submission.

### Replacement and shared-asset effects

Asset bytes and placement links/type/group/target are immutable after their relevant creation/commit. To replace artwork, upload/process the new asset, inspect every existing placement using the old asset, then recreate only the intended placement links and reorder that group. Placement deletion leaves the library asset intact. Deleting a library asset while placements still reference it fails.

Preserve the current live assets until the replacement is validated. If a group is already at its cap, plan the minimal remove/create sequence on the editable parent and verify completeness afterward. There is no generic PATCH-placement or atomic gallery-swap operation to invent. A partially completed sequence must remain identified as incomplete.

An approved asset can be archived through `archived: true`, subject to the actual state restriction. A draft is not made archivable by pretending it is approved. Updating a video's preview frame affects every placement of that shared video and regenerates the frame asynchronously. Verify nested frame state and the actual still image before concluding success.

## Other asset contracts

IAP/subscription review screenshots, App Review attachments, encryption documents, App Clip header/advanced-experience images, Game Center images, routing coverage and binary/hosted-asset uploads retain their specific contracts. For applicable dedicated attachment endpoints, the reservation/update model may require a whole-file MD5 checksum. Resolve that endpoint's request instead of applying the Asset Library commit universally.

Store icon assets remain part of the actual target build pipeline. Custom pages, experiments, product-page headers, search/ad creative, event cards/details and retention surfaces have separate placement eligibility, categories, limits and review. Reuse a master only when the resulting file and actual feature satisfy the matching specification. Public marketing art, capture evidence and private review attachments are different deliverables.

## Worked Duo capture-to-delivery reconciliation

For four journeys in three locales, capturing both outer and inner layouts produces 24 images.
That count is an example, not Apple's minimum. Build a row for every locale/journey/display with
source capture, output dimensions/hash, library asset ID, detected `specId`, target localization,
placement group/ID and intended order. Opaque JPEG export is one way to avoid accidental PNG alpha.
Keep real UI proportions. Uploading all files without placing them does not complete delivery.

Use the selected toolchain's actual commands to discover and capture displays:

```text
xcrun simctl help io
xcrun simctl io "$SIMULATOR_UDID" enumerate
xcrun simctl io "$SIMULATOR_UDID" screenshot --display="$OUTER_DISPLAY_ID" "$OUTER_CAPTURE"
xcrun simctl io "$SIMULATOR_UDID" screenshot --display="$INNER_DISPLAY_ID" "$INNER_CAPTURE"
```

These operations are present in the inspected Xcode 27.2 help. Populate display variables from
`enumerate`. One exercised Duo runtime used IDs `1` and `3`, but these are not universal assignments.
Use Device Hub to choose closed/open posture and the actual orientation. Selecting a display for
capture does not switch posture. Screen power/geometry operations are not a substitute for the
folding interaction. If capture is black, inspect posture, powered display, app state and enumeration
before retrying. Do not fabricate a hinge flag or stretch a different screenshot to fit.

In the exercised Asset Library, outer and inner specifications resolved to one Duo placement group.
Always use current reference data to determine whether this applies to the actual account/version.
Two display specifications do not necessarily mean two independent gallery limits. In that example,
four journeys interleaved outer/inner gave eight placements in one group per locale, within its
returned ten-image cap. Preserve the existing other-device groups and their ordering.

After every image reaches its successful processing state, compare its detected specification with
the intended display. Create the correct locale placements, then send the complete ordered group.
For two example placements, the ordering request body is:

```json
{
  "data": {
    "type": "appAssetLibraryPlacementOrderingRequests",
    "attributes": {"placementGroup": "<returned-group>"},
    "relationships": {
      "orderedPlacements": {"data": [
        {"type": "appAssetLibraryPlacements", "id": "<first-placement>"},
        {"type": "appAssetLibraryPlacements", "id": "<second-placement>"}
      ]},
      "appStoreVersionLocalization": {"data": {
        "type": "appStoreVersionLocalizations", "id": "<target-localization>"
      }}
    }
  }
}
```

Use every intended placement ID, including retained images in that group. Read sorted placements
back per localization/group and compare IDs and media relationships, not just counts. Resume a
partial run from confirmed IDs/hashes. Do not blindly reserve/upload a second copy of each image
because a process was interrupted. Keep shared-asset deletion and the parent's editable/review state
separate from capture success. Retain final screenshots and sanitized receipts, then remove temporary
capture runners, private logs and intermediate copies that are no longer needed.
