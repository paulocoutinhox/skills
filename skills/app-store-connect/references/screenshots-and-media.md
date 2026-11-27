# Screenshots, icons, previews, and uploaded assets

Checked baseline: 2026-11-05. Fetch the current [screenshot specification](https://developer.apple.com/help/app-store-connect/reference/app-information/screenshot-specifications/) before exporting. Device requirements change separately from API enums.

## Required capture plan

Make a table of platform, supported device family, display slot, orientation, locale, screenshot order, source capture, export path, dimensions, file format, byte size, and upload resource ID and state. Apple accepts 1–10 screenshots per device size in JPEG/JPG/PNG. Images must have no alpha channel. Use the real product UI in a stable test state without private customer data.

| Slot | Verified pixel examples | Operational rule |
| --- | --- | --- |
| iPhone Dynamic Island, medium | 1179×2556 or 1206×2622, and transposed landscape | The main required iPhone family today. Check the live table's alternative and scaling rules |
| iPhone Dynamic Island, large | 1260×2736, 1290×2796, 1320×2868, and transposed landscape | Not required by itself. Giving it fills the large-display slot |
| iPhone Face ID, large | 1284×2778 or 1242×2688, and transposed landscape | Required for an iPhone app when no Dynamic Island large screenshots are given |
| iPhone Duo outer display | 1398×2034 or 2034×1398 | Capture the real outer-display layout |
| iPhone Duo inner display | 2007×2853 or 2853×2007 | Capture the real unfolded layout, not an enlarged phone screenshot |
| iPad 13-inch | 2064×2752 or 2048×2732, and transposed landscape | Required when the app supports iPadOS |
| Mac | 1280×800, 1440×900, 2560×1600, 2880×1800 | Match the specified 16:10 canvas and the real Mac UI |
| Apple TV | 1920×1080 or 3840×2160 | Show TV UI and focus states without cut-off safe areas |
| Apple Vision Pro | 3840×2160 | Use supported spatial capture tools and the real app presentation |
| Apple Watch, when included | Current examples include 422×514 and 410×502 | Pick the real supported watch slot from the live table |

The specification says Duo screenshots are required starting **April 2027 for any app using the
iOS 27.1 SDK or later**. The [October 5 announcement](https://developer.apple.com/news/?id=kkphp5qo)
says that from April 2027 any app or game submitted needs iPhone Duo screenshots, without the SDK
condition. Prepare outer and inner Duo screenshots for every iPhone submission from April 2027, which
meets both statements, and check the real rule shown at submission. Apple does not give an exact day
in the notices we checked. Do not make one up.
Use the current Asset Library's reference data for the real Duo placement groups and specifications.
Those identifiers are dynamic strings, so a device missing from the deprecated `ScreenshotDisplayType`
enum does not prove that the current API cannot target it. Never map Duo to a guessed phone group.
If the required group is really not available to the account or API, report the exact gap and use the
documented console handoff instead of making up support.

### Required assets and Duo capture procedure

Before upload, mark each platform and device family that applies as required, supplied, validated,
and delivered. Include the required iPhone and iPad slots, the April 2027 Duo requirement where it
applies, and each chosen native platform. A missing required family means the release is incomplete,
even when the binary upload works. Do not upload only the easiest phone capture or stretch it to fit
another family.

1. Install or select the Xcode and SDK with real Duo support, find its simulator in Device Hub, and
   use the same app layout as the release with stable, harmless demo content.
2. Select the outer (closed) display and the intended orientation, move through the real app, and
   capture the visible UI. Select the inner (unfolded) display and capture its real adapted layout.
3. Check the transition and reflow, safe areas, text, controls, and that no private or debug content
   shows. Device Hub's canvas scale is not the app's logical display size.
4. Check the outer 1398×2034 or its landscape transpose and the inner 2007×2853 or its transpose
   against the live specification. Keep the UI in proportion and the output opaque. A black or
   wrong-display capture is a capture failure to look into. It does not allow faking an image or
   resizing an unrelated screen.
5. Repeat the meaningful localized journeys, keep the source captures and editable compositions, and
   upload to the real matching slot. Check the delivered state, the order, and the product-page
   preview.

The generic `simctl` capture below works only if it captures the intended display correctly in the
chosen runtime. Choose the posture in Device Hub, then select each display with the documented
`xcrun simctl io "$SIMULATOR_UDID" enumerate` and `screenshot --display=` steps in
[the worked Duo reconciliation](#worked-duo-capture-to-delivery-reconciliation). Do not make up a
hinge flag.

## Capture and design

Use `xcrun simctl list devices available` to find installed simulators. Boot the intended device and capture with `xcrun simctl io "$DEVICE_UDID" screenshot "$OUTPUT_PATH"` after moving through the real app. Use the right capture workflows for Mac, TV, and Vision Pro and check their output dimensions. Find Duo simulators from the installed SDK instead of making up device names or UDIDs.

Seed demo content you can reproduce. Hide notifications, personal identities, debug overlays, and test payment details. Show each platform's real layout, controls, typography, and permission behavior. Test folded and unfolded states and orientation changes where supported. Keep titles, captions, device frames, and UI in proportion. Never let a frame hide the app or cut off important controls.

Create an editable master composition. Image generation tools may create supporting backgrounds or illustrations, not fake product evidence. Combine real captures, short localized benefit captions, and licensed artwork. Captions and overlays describe the product benefit. They never describe how the image was made or mention AI, agents or tools. Export the exact accepted dimensions without stretching. Keep the white or transparent handling that the real asset type requires. Flatten screenshot alpha onto the intended opaque background.

Check full-size and store-size previews for readable type, text overflow, cut-off edges, wrong device frames, distorted UI, misleading claims, and consistency between images. Use a reliable image inspector such as Pillow or ImageMagick for width, height, format, color mode, alpha, and bytes. You still need to look at the images. A file extension does not prove the real encoding.

## Icons and previews

App icons are built into the platform's asset catalog and checked by Xcode. Use the correct modern icon pipeline for the installed Xcode, including layered or platform-specific assets when required. Do not upload one random 1024px PNG in place of all macOS, tvOS, and visionOS icon requirements. Check the current icon guide and export validation for the real target.

App previews are separate video assets with their own orientation, resolution, length, codec and audio, and size rules. Check the current [preview specification](https://developer.apple.com/help/app-store-connect/reference/app-information/app-preview-specifications/) again. Use the real captured experience, accurate localized overlays, licensed sound, and readable thumbnails and poster times. Do not claim one video encoding fits every platform, or use a promotional trailer in place of real app footage without checking policy.

The researched baseline allows up to three previews, 15–30 seconds each, at most 500 MB, at most 30 fps, with H.264 or ProRes 422 HQ and the specified stereo audio. Mac and TV previews are landscape. Get the exact device resolution, container, audio sample rate and bit depth, and poster-frame rules from the current table. Use `ffprobe` or a similar tool to check the real streams, duration, dimensions, frame rate, rotation, codecs, audio layout, and bytes. A `.mp4` extension alone does not show the file meets the rules. Capture the real app experience and check that it reads well when it autoplays without sound.

## Current Asset Library workflow

Use the [App Asset Library](https://developer.apple.com/documentation/appstoreconnectapi/app-asset-library) for new screenshots, previews and in-app event media. Set-based screenshot, preview and event-media resources are deprecated. Do not add compatibility code around them or copy their checksum and state contract into the current API.

### Discover specifications and limits

1. Read `GET /v1/apps/{id}/assetLibrary` for the real library ID.
2. Read `GET /v1/appAssetLibraryRefData`. Look at `features`, `placementProfileGroups`, `imageSpecs`, `videoSpecs`, `placementTypes` and `displayClasses`. Supported filters and fields can narrow the response for the task.
3. Start with the real feature, such as `APP_STORE_VERSIONS`. Its placement policies describe the allowed types and the limits for each group. Find the target platform or device's group, then that type and group's specification IDs, then the real image or video specification.
4. Check dimensions, aspect, extension/MIME, bytes, alpha, video frame rate, duration and audio, and the accepted asset category. IDs are strings the API returns, not a fixed device catalog copied locally. A feature missing from the returned catalog is not available, even if a broader enum names it.

The current App Store version policy allows up to ten screenshots, three previews and one product-page header asset per group that applies. Custom pages, events and experiments have their own limits. The screenshot and preview specification above is for planning. Use the real reference data and the required-device rules together for the real operation.

### Reserve, transfer, commit and inspect

Reserve with `POST /v1/appAssetLibraryImages` or `POST /v1/appAssetLibraryVideos`. Required attributes are `fileName`, the exact `fileSize` and `category`, with the real `assetLibrary` relationship. The optional `referenceName` helps show purpose or locale. Videos also accept `previewFrameTimeCode`.

Use `APP_SCREENSHOTS_AND_PREVIEWS` for real app captures and previews, and `CREATIVE_ASSETS` only for eligible creative placements. You choose the category when you reserve, and you cannot change it later. A marketing illustration cannot stand in for a captured screenshot.

Run every returned upload operation with its exact method, URL, headers, byte offset and length. Upload parts only while their reservation and URLs are still valid. Do not send Connect JWTs to the temporary upload host. When a transfer might or might not have worked, check before sending again, and commit only when all parts have succeeded.

Commit with `PATCH /v1/appAssetLibraryImages/{id}` or the video version, setting `uploaded: true`. **The current library request has no `sourceFileChecksum` attribute.** Keep a local file hash as evidence, but do not send the MD5 field from the deprecated screenshot request.

Poll the resource: `AWAITING_UPLOAD` is not committed, `UPLOAD_COMPLETE` is processing, `PREPARE_FOR_SUBMISSION` means processing worked, and `FAILED` needs a look at the real `stateDetails` and a corrected reservation. Read the returned `specId`, the processed image or video and the preview-frame status. Never send a made-up `specId`. An uploaded asset is not yet a visible placement or approved content.

### Place and order media

Create `POST /v1/appAssetLibraryPlacements` with the real `placementType`, the returned `placementGroup`, exactly one image or video relationship and exactly one target surface. The normal targets are `appStoreVersionLocalization`, `appCustomProductPageLocalization`, `appEventLocalization` and `appStoreVersionExperimentTreatmentLocalization`. Retention media has its own supported version relationship.

For example, a real screenshot on an existing editable localization uses this shape:

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

Read the localization's `placements`, filtered by type and group and sorted by `placementGroupPosition`. That is a supported sort key, not a position attribute you can read or write. Set the full intended order with `POST /v1/appAssetLibraryPlacementOrderingRequests`, using `placementGroup`, the ordered `orderedPlacements` relationship IDs and the one target localization. Read the sorted placements again to confirm the order. Events cannot be ordered like screenshot galleries, because each of their placement types allows only one asset.

Placement state follows the parent's review, including processing, preparation and approval. Submit the real version, custom page or event parent as required. Eligible creative assets can also have their own supported review items. Uploading to the library alone is not a submission.

### Replacement and shared-asset effects

Asset bytes and placement links, type, group and target cannot change after they are created or committed. To replace artwork, upload and process the new asset, check every existing placement that uses the old asset, then recreate only the intended placement links and reorder that group. Deleting a placement leaves the library asset in place. Deleting a library asset fails while placements still point to it.

Keep the current live assets until the replacement is checked. If a group is already full, plan the smallest remove and create sequence on the editable parent and check afterward that nothing is missing. There is no general PATCH-placement or one-step gallery-swap operation, so do not make one up. A sequence that is only partly done must stay marked as incomplete.

An approved asset can be archived with `archived: true`, within the real state limits. Pretending a draft is approved does not make it archivable. Changing a video's preview frame affects every placement of that shared video and rebuilds the frame in the background. Check the nested frame state and the real still image before you call it done.

## Other asset contracts

IAP and subscription review screenshots, App Review attachments, encryption documents, App Clip header and advanced-experience images, Game Center images, routing coverage and binary or hosted-asset uploads keep their own contracts. For dedicated attachment endpoints that apply, the reservation or update model may need an MD5 checksum of the whole file. Look up that endpoint's request instead of using the Asset Library commit everywhere.

Store icon assets stay part of the real target build pipeline. Custom pages, experiments, product-page headers, search and ad creative, event cards and details, and retention screens each have their own placement eligibility, categories, limits and review. Reuse a master only when the resulting file and the real feature meet the matching specification. Public marketing art, capture evidence and private review attachments are different deliverables.

## Worked Duo capture-to-delivery reconciliation

For four journeys in three locales, capturing both outer and inner layouts gives 24 images.
That count is an example, not Apple's minimum. Make a row for every locale, journey and display with
the source capture, output dimensions and hash, library asset ID, detected `specId`, target
localization, placement group and ID and intended order. Opaque JPEG export is one way to avoid
accidental PNG alpha. Keep real UI proportions. Uploading all files without placing them does not
finish delivery.

Use the chosen toolchain's real commands to find and capture displays:

```text
xcrun simctl help io
xcrun simctl io "$SIMULATOR_UDID" enumerate
xcrun simctl io "$SIMULATOR_UDID" screenshot --display="$OUTER_DISPLAY_ID" "$OUTER_CAPTURE"
xcrun simctl io "$SIMULATOR_UDID" screenshot --display="$INNER_DISPLAY_ID" "$INNER_CAPTURE"
```

These operations appear in the Xcode 27.2 help we checked. Fill the display variables from
`enumerate`. One Duo runtime we observed used IDs `1` and `3`, but these are not fixed for every
runtime. Use Device Hub to choose the closed or open posture and the real orientation. Selecting a
display for capture does not change the posture. Screen power and geometry operations do not replace
the folding action. If the capture is black, check the posture, the powered display, the app state and
the enumeration before you retry. Do not make up a hinge flag or stretch a different screenshot to fit.

In one Asset Library we observed, the outer and inner specifications belonged to one Duo placement
group. Always use current reference data to find out whether this applies to the real account and
version. Two display specifications do not always mean two separate gallery limits. In that example,
four journeys with outer and inner images alternating gave eight placements in one group per locale,
within its returned limit of ten images. Keep the existing groups for other devices and their order.

After every image reaches its successful processing state, compare its detected specification with
the intended display. Create the correct placements for each locale, then send the complete ordered
group. For two example placements, the ordering request body is:

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

Use every intended placement ID, including images you keep in that group. Read the sorted placements
back for each localization and group and compare IDs and media relationships, not just counts. Resume
a partial run from confirmed IDs and hashes. Do not reserve and upload a second copy of each image
without checking just because a process was interrupted. Keep shared-asset deletion and the parent's
editable and review state separate from capture success. Keep the final screenshots and cleaned
receipts, then remove temporary capture runners, private logs and in-between copies you no longer
need.
