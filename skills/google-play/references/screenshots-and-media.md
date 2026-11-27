# Screenshot and media production

Baseline: 2026-11-05. Check the current [preview asset guide](https://support.google.com/googleplay/android-developer/answer/9866151?hl=en) again, including the form-factor sections and featuring eligibility.

| Asset | Baseline specification | Check |
| --- | --- | --- |
| Store icon | 512×512, 32-bit PNG, at most 1,024 KB | Real encoding, no store masking added beforehand and no misleading badges |
| Feature graphic | 1024×500, JPEG or 24-bit PNG without alpha | Safe layout, no tiny UI or text, no false ranking or discount claims |
| General screenshots | JPEG or 24-bit PNG without alpha, min dimension 320px, max 3840px, largest dimension no more than twice the smallest | At least two overall, up to eight per supported device family/type |
| Common phone recommendation | 1080×1920 portrait or 1920×1080 landscape | A recommendation, not the only accepted size |
| Android TV banner | 1280×720, eligible JPEG/24-bit PNG | Real TV branding and readable safe areas |
| Android TV screenshots | At least one required for a TV listing, with current 16:9 guidance | Use real TV UI, check resolution and current featuring rules |
| Tablet/Chromebook | Current large-screen guidance: at least four, 1080–7680px, 16:9 or 9:16 | Core UI, no extra caption overlays in these special captures |
| Wear OS app/watch face | At least one, 1:1, minimum 384×384 | Interface only, no device frames, added text or backgrounds, transparency or masking |
| Android Automotive OS | When provided, at least two 800×1280 portrait and two 1024×768 landscape | Generic system or emulator UI, no OEM-specific screenshots. The category affects whether they are required |
| Android XR | Four to eight, PNG/JPEG, at most 8 MB each, 8:5 | Minimum 1920×1200, recommended 3840×2400 |
| Preview video | Eligible public/unlisted YouTube video link | Check accessibility, advertising and age limits, and gameplay and content rules |

Featuring recommendations can be stricter than basic upload validity. A general two-screenshot minimum does not prove that a game or form-factor promotion qualifies. Check the current required count, orientation, resolution and share of gameplay footage for the intended surface.

The same current help page lists a general 3840px maximum and special large-screen guidance up to 7680px. Keep these apart and check against the real target surface. A 1920×1080 or 1080×1920 large-screen export meets both ranges when that fits. Do not use the general maximum to reject a separately supported high-resolution slot, and do not assume its high-resolution allowance applies to phone screenshots. Current eligibility for screenshot-based recommendations asks for at least four qualifying app screenshots, or three qualifying gameplay screenshots for games, with the stated high-resolution aspect ratios.

## Capture workflow

Make a device list for the phone, 7-inch tablet, 10-inch tablet, foldable, Chromebook/PC, Wear OS, TV, automotive and XR targets the app really supports. Do not upload every type just because the API lists it. Capture typical real UI and note the tested device, OS and locale. Foldable and large-screen images must show adapted layouts, not stretched phone content.

Use Android Studio emulator or device tools, or `adb -s "$DEVICE_SERIAL" exec-out screencap -p > "$OUTPUT_PATH"`, on a chosen stable app state. Fill in harmless demo data, and remove notifications, personal details, debug overlays and payment information. Keep the original captures as source assets.

For store layouts, use one clear benefit per image, short localized captions, readable contrast, consistent fonts and device frames in the right proportions when useful. Keep important content inside safe areas and allow for cropping on the store page. Use AI-generated supporting artwork only when it honestly shows the product and the licensing is clear. Never fake app screens, endorsements, UI features or before-and-after results. Captions describe the product benefit and never say how the image was made or that AI, agents or tools were involved. Record AI generation only through the honest `aiGeneratedState` upload attestation.

Export the exact intended sizes and real image formats. Inspect the bytes, orientation, aspect ratio, alpha and color mode, cut-off text, cut-off content, layout in small previews and privacy. Use Pillow/ImageMagick or a similar repeatable check, plus a real visual review. Do not turn a square image into landscape by stretching it.

## API upload and ordering

Inside the current edit, look up the supported `edits.images` methods and their `imageType` parameter enum. Upload to the right locale and image type using the method's media-upload protocol. Do not send a local file path as JSON image data. Check the response hash and URL, and read the remote list back. If a newer console media type is missing from the refreshed API enum, use its supported console upload page instead of inventing an enum value. The agent uploads there in the owner's signed-in browser when browser use is authorized for this task, and otherwise prepares an exact owner handoff.

The valid ordinary image types we researched are `phoneScreenshots`, `sevenInchScreenshots`, `tenInchScreenshots`, `tvScreenshots`, `wearScreenshots`, `icon`, `featureGraphic` and `tvBanner`. Do not use the unspecified placeholder value. Automotive, XR and newer promotion surfaces do not have a guessed extra enum.

The upload method takes real media, with the supported simple, multipart or resumable upload protocols. Its ordinary path is `/upload/androidpublisher/v3/applications/{packageName}/edits/{editId}/listings/{language}/{imageType}`. The Discovery also describes the separate resumable path. Use that real protocol and upload-session identity, especially after a transfer was interrupted.

The upload limit is 15,728,640 bytes in this researched contract. Single store surfaces can set smaller limits, so apply both. `aiGeneratedState` is an optional supported upload query parameter. Set the real non-AI or developer-attested AI state honestly when it applies. It is not a reason to fake UI or to claim artwork was captured from the app. The result includes the real image ID, preview URL and available SHA-1/SHA-256 hashes.

Order screenshots on purpose. Do not run a careless `deleteall` before the replacement assets are checked. If the API needs a delete and reupload to change the order, prepare the exact set you want, keep source copies, and run it within the authorized listing change. Each supported locale needs accurate images, or a deliberate and documented fallback to the default language.

There is no ordinary `images.reorder` method in this snapshot. To replace a gallery, prepare and check all files first, keep the old sources and order, run the intended delete and upload steps one at a time within one edit, then inspect the returned gallery and the real preview before commit. If any upload fails, fix the staged gallery or throw away the edit instead of committing a partial set of assets. A standalone product change is not thrown away with it.

## Additional console media and promotional surfaces

The current [Play Asset Library](https://support.google.com/googleplay/android-developer/answer/16386748?hl=en) can manage and reuse eligible store-listing, experiment and event graphics in Play Console. This UI library is not Apple's placement API and does not add unlisted Publisher endpoints. Prepare the exact creative, localization, rights and intended destination. When no ordinary API exists, do the supported console workflow in the owner's signed-in browser if browser use is authorized for this task, and otherwise hand that exact step to the owner.

Custom store listings, experiments, promotion and event content, newer form-factor assets and short-video programs each have their own real account, format and review eligibility. Do not use `Listing.video` as a general upload field for any video program. It is a supported YouTube URL for the ordinary listing, and one URL must meet that surface's requirements.

The adaptive launcher icon inside the Android app is not the store icon. TV banners and special in-app assets also have Android resource requirements beyond listing uploads. Check both the built app and the store asset lists.
