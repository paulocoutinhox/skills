# Screenshot and media production

Baseline: 2026-11-05. Recheck the current [preview asset guide](https://support.google.com/googleplay/android-developer/answer/9866151?hl=en), including form-factor-specific sections and featuring eligibility.

| Asset | Baseline specification | Check |
| --- | --- | --- |
| Store icon | 512×512, 32-bit PNG, at most 1,024 KB | Actual encoding, no pre-added store masking or misleading badges |
| Feature graphic | 1024×500, JPEG or 24-bit PNG without alpha | Safe composition, no tiny UI/text, no false ranking or discount claims |
| General screenshots | JPEG or 24-bit PNG without alpha, min dimension 320px, max 3840px, largest dimension no more than twice the smallest | At least two overall, up to eight per supported device family/type |
| Common phone recommendation | 1080×1920 portrait or 1920×1080 landscape | Recommendation, not the only accepted dimensions |
| Android TV banner | 1280×720, eligible JPEG/24-bit PNG | Actual TV branding and readable safe areas |
| Android TV screenshots | At least one required for a TV listing, with current 16:9 guidance | Use actual TV UI, verify resolution/current featuring rules |
| Tablet/Chromebook | Current large-screen guidance: at least four, 1080–7680px, 16:9 or 9:16 | Core UI, no extra caption overlays in these specialized captures |
| Wear OS app/watch face | At least one, 1:1, minimum 384×384 | Interface only, no device frames, added text/backgrounds, transparency or masking |
| Android Automotive OS | When provided, at least two 800×1280 portrait and two 1024×768 landscape | Generic system/emulator UI, no OEM-specific screenshots. Category affects whether required |
| Android XR | Four to eight, PNG/JPEG, at most 8 MB each, 8:5 | Minimum 1920×1200, recommended 3840×2400 |
| Preview video | Eligible public/unlisted YouTube video link | Verify accessibility, advertising/age restrictions, and gameplay/content rules |

Featuring recommendations can be stricter than basic upload validity. A generic two-screenshot minimum is not proof a game or form-factor promotion qualifies. Check the current required number, orientation, resolution, and proportion of gameplay footage for the intended surface.

The current same help page lists a general 3840px maximum and specialized large-screen guidance up to 7680px. Preserve this distinction and validate against the actual target surface. A 1920×1080 or 1080×1920 large-screen export meets both ranges when appropriate. Do not apply a generic maximum to reject a separately supported high-resolution slot, or assume its high-resolution allowance applies to phone screenshots. Current screenshot-based recommendation eligibility calls for at least four qualifying app screenshots or three qualifying gameplay screenshots for games, with the stated high-resolution aspect ratios.

## Capture workflow

Create a device matrix for phone, 7-inch tablet, 10-inch tablet, foldable, Chromebook/PC, Wear OS, TV, automotive, and XR targets actually supported. Do not upload every type merely because the API enumerates it. Capture representative real UI and document tested device/OS/locale. Foldable and large-screen images must show adapted layouts rather than stretched phone content.

Use Android Studio emulator/device tooling or `adb -s "$DEVICE_SERIAL" exec-out screencap -p > "$OUTPUT_PATH"` on a selected stable app state. Populate harmless demo data and remove notifications, personal identifiers, debug overlays, and payment information. Keep original captures as source assets.

For store compositions, use one clear benefit per image, short localized captions, readable contrast, consistent typography, and proportional device frames when useful. Keep important content inside safe areas and account for storefront cropping. Use AI-generated supporting artwork only when it truthfully represents the product and licensing is clear. Never fabricate app screens, endorsements, UI features, or before/after outcomes.

Export exact intended dimensions and real image formats. Inspect bytes, orientation, aspect ratio, alpha/color mode, text clipping, content cutoffs, layout on small previews, and privacy. Use Pillow/ImageMagick or equivalent deterministic inspection plus actual visual review. Do not transform a square image into landscape by stretching.

## API upload and ordering

Within the current edit, query supported `edits.images` methods and their `imageType` parameter enum. Upload to the correct locale and image type using the method's media-upload protocol. Do not send a local file path as JSON image data. Check the response hash/URL and read the remote inventory back. If a newer console media type is absent from the refreshed API enum, use its supported console upload surface instead of inventing an enum value.

The researched valid ordinary image types are `phoneScreenshots`, `sevenInchScreenshots`, `tenInchScreenshots`, `tvScreenshots`, `wearScreenshots`, `icon`, `featureGraphic` and `tvBanner`. Do not use the unspecified sentinel. Automotive/XR and newer promotional UI surfaces are not represented by a guessed extra enum.

The upload method accepts real media, with supported simple/multipart or resumable upload protocols. Its ordinary path is `/upload/androidpublisher/v3/applications/{packageName}/edits/{editId}/listings/{language}/{imageType}`. The Discovery also describes the distinct resumable path. Use that actual protocol and upload-session identity, especially after an interrupted transfer.

The upload-level ceiling is 15,728,640 bytes in this researched contract. Individual store surfaces can impose smaller limits, so apply both. `aiGeneratedState` is an optional supported upload query parameter. Set the actual non-AI or developer-attested AI state truthfully when applicable. It is not a reason to fabricate UI or claim artwork was captured from the app. The result includes actual image ID, preview URL and available SHA-1/SHA-256 hashes.

Order screenshots intentionally. Avoid indiscriminate `deleteall` before replacement assets are validated. If the API requires delete/reupload to reorder, prepare the exact desired set, preserve source copies, and execute it within the authorized listing change. Each supported locale needs accurate images or an intentional, documented default-language behavior.

There is no ordinary `images.reorder` method in this snapshot. For a gallery replacement, prepare/validate all files first, preserve the old sources/order, perform the intended delete/upload sequence within one serialized edit, then inspect the returned gallery and actual preview before commit. If any upload fails, fix the staged gallery or discard the edit rather than committing a partial asset set. A standalone product mutation is not discarded with it.

## Additional console media and promotional surfaces

The current [Play Asset Library](https://support.google.com/googleplay/android-developer/answer/16386748?hl=en) can manage/reuse eligible store-listing, experiment and event graphics in Play Console. This UI library is not Apple's placement API and does not add unlisted Publisher endpoints. Prepare the exact creative, localization, rights and intended destination, then use the supported console workflow when no ordinary API exists.

Custom store listings, experiments, promotional/event content, newer form-factor assets and short-video programs have their actual account/format/review eligibility. Do not use `Listing.video` as a generic upload field for any video program. It is a supported YouTube URL for the ordinary listing, and a single URL must satisfy that surface's requirements.

The adaptive launcher icon inside the Android app is distinct from the store icon. TV banners and specialized in-app assets also have Android resource requirements beyond listing uploads. Verify both the built application and storefront asset inventories.
