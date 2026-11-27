---
name: app-store-connect
description: Create, update and manage Apple store releases for iOS/iPadOS, macOS, tvOS and visionOS through supported API/CLI workflows, including all core fields, ASO, media, pricing, availability, products, fixing rejections, review and release controls.
license: MIT
---

# App Store Connect

Run a release as a series of checked states: prepared source, signed file, finished upload, processed build, complete listing and products, submitted review, approved version and real availability in the store. Each state is a different kind of success. One does not stand in for another.

This skill is descriptive. Its researched steps and limits are written here. Do not create refresh scripts, counters, converters or generated API catalogs. Stored information changes only when the user asks for maintenance. Apple's own tools and supported API calls are still how you carry out an app task the user clearly asked for.

## Brief and platform matrix

Find the team/account role, numeric app ID, stable bundle IDs, SKU, marketing version, source revision, build schemes, signing, locales, territories, real features and release endpoint. Get honest privacy/encryption/content/age/accessibility answers from the code and the owner. Do not make up declarations or reviewer credentials.

| Target | Connect platform | Archive destination | SDK and main concerns |
| --- | --- | --- | --- |
| iPhone/iPad | `IOS` | `generic/platform=iOS` | `iphoneos`, real device families and adapted layouts |
| Native Mac | `MAC_OS` | `generic/platform=macOS` | `macosx`, sandbox, signing, entitlements and architectures |
| Mac Catalyst | `MAC_OS`, on the same app record as the iOS app | `generic/platform=macOS,variant=Mac Catalyst` | `macosx` with the Catalyst variant, Mac layout, menus, sandbox and signing |
| Apple TV | `TV_OS` | `generic/platform=tvOS` | `appletvos`, focus/remote, safe areas and TV assets |
| Apple Vision Pro | `VISION_OS` | `generic/platform=visionOS` | `xros`, windows/volumes/immersion, input and motion |
| Apple Watch | None. It ships inside the iOS app record (`IOS`) | Part of the iOS app's archive | `watchos`, the watch target inside the iOS app, small screens and Digital Crown |

Mac Catalyst is its own destination or variant in the project. An iOS app that is also available on Mac or Vision Pro is not a native release for those devices. A watchOS companion follows the app and target structure that contains it. Do not make up a `WATCH_OS` Connect enum.

Keep the links between platform, version, build, locale, device slot, asset and review clear. Use [the brief](assets/release-brief.json) as a document template, not an API payload.

Start a list of fields and changes in [the release evidence template](assets/release-evidence.md). For each one, record the current value, desired value, which API or console screen owns it, locale/platform/territory, whether it is required, whether it can be edited, the read-back value and whether it has been done. Keep existing values that are there on purpose. Facts only the owner knows stay blocked until the owner gives them. Do not fill an optional field just to make the form look complete.

Record the allowed endpoint as `prepare`, `upload`, `beta`, `submit` or `release`, matching the brief's `authorized-endpoint`. Do the normal steps needed to reach that endpoint without asking again, then stop. Report the next change you have not made as its resource, operation and effect on customers. Do not move on to a later state.

## Account bootstrap and authentication

Confirm active membership, app access, agreements, paid-app eligibility, bank/tax status and the legal right to distribute. Enrollment, signing agreements and owner statements need the real owner. API credentials, distribution signing identities and IAP server credentials each do a different job.

Set up supported bundle IDs, capabilities, certificates, devices and profiles through the matching API resources. Match the team, platform, entitlements and all extension IDs. Do not turn on every capability just in case.

The researched `/v1/apps` collection reads app records. It has no general POST operation to create an app. Prepare the name, SKU, bundle ID, primary language and platforms, then create the first record in Apps → New App. Find the new app by bundle ID. Creating `/v1/appStoreVersions` does not create the app itself.

The Connect base URL is `https://api.appstoreconnect.apple.com`. JWTs use ES256, the real `kid`, `typ: JWT`, Unix `iat`/`exp` and `aud: appstoreconnect-v1`. Team keys put the real issuer in `iss`. Individual keys use `sub: user` and leave out `iss`. Normal release requests use short lifetimes of at most 20 minutes. Special longer lifetimes for some scoped GET requests do not apply to writes.

Before asking the user for API credentials, check these environment variables: `APPLE_STORE_CERTIFICATES_PATH` (the folder that holds the `.p8` key files) and `APPLE_STORE_ISSUER_ID` (the issuer ID). Read only the names and paths you need. Never print a key's contents. Ask the user only for what is missing. Keep `.p8` keys in the approved secret store, not in source, history or logs. A Connect token is not automatically an App Store Server API token. Use the current documented signing library or tool for the chosen credential type. Do not write your own cryptography or a wrapper script.

## Supported API resource map and request method

| Domain | Resource families | Critical dependency |
| --- | --- | --- |
| Team/signing | users, invitations, bundle IDs/capabilities, certificates, profiles, devices | Correct identity/role before setup |
| App information | apps, appInfos, appInfoLocalizations, appCategories, appTags | App-level information is separate from a version localization |
| Version/build | appStoreVersions, preReleaseVersions, builds, buildUploads, buildUploadFiles | Processed compatible build before you select it for a version |
| Listing media | appAssetLibraries, library images/videos/reference data, placements and ordering requests | Find specification → reserve/upload/commit → verify → place → order |
| Compliance | ageRatingDeclarations, appEncryptionDeclarations, accessibilityDeclarations | Real facts from the owner and the code |
| Review/release | appStoreReviewDetails, reviewSubmissions/items, release requests, phased releases | Item is eligible and in the right state before submit/release |
| Commercial | Territories, app availability, price points/schedules, tax configuration | Intended countries/base territory and the real price model |
| Products | inAppPurchases and current product-version/localization/price/availability resources | Parent product before draft version and review |
| Subscriptions | Groups, subscriptions, group/product versions, offers, prices and availability | Correct service grouping, current version and eligibility |
| Beta/diagnostics | TestFlight groups/testers, beta review/feedback and diagnostics | Correct audience, review and processed build |
| Growth/games/reporting | Custom product pages, experiments, events, nominations, Game Center, analytics and sales/finance reports | Feature/role/platform eligibility |

For each operation, check its official method, path, required parameters, request and response models and state limits. JSON:API uses `data.type`, attributes and relationships with the provider's resource IDs. A product's display name or store identifier is not always its relationship ID. Omitted, null and deleted mean different things. Do not guess a PATCH contract from a create model.

Follow pagination `links.next` to the end when you need the full list. For uploads, reserve with the real filename, byte size and parent. Use each returned method, URL, header and byte range exactly, then commit with the request for that resource. Current library assets use the uploaded flag with no checksum field. Dedicated attachments can need their documented checksum. Poll the real processing state. Do not send an account bearer header to a different upload host. When a create or upload might or might not have worked, check what exists before you retry.

The [functional API map](references/api-coverage.md) covers current core and specialized families: testing, optimization, events, retention, Game Center, hosted assets, alternative distribution, reporting, signing/access, Xcode Cloud/SCM and webhooks. It explains what each is for and where it stops. New work uses current APIs, not deprecated set-based media or old submission endpoints. Each operation still needs its real model and eligibility, not guessed parameters.

For a 401, check the token, clock and key. For a 403, check the role, app access and agreements. For a 409/422, check the exact state and field errors. Follow 429 and temporary-error retry guidance with a limited number of attempts. A state you do not recognize stays unresolved. It is not success. [API detail](references/api-and-bootstrap.md) goes deeper into resource and request choices.

## Build numbers and signed release artifacts

The marketing version and `CFBundleVersion` are different. Before every new upload, read all relevant remote builds, pre-release versions and pending uploads. Include numbers already reserved locally or in CI, and take the project's existing allocation lock. Pick a fresh, always-increasing, supported number, save the reservation so it lasts, then build. Working out `max + 1` locally is not enough by itself to stop two runners from picking the same number.

Apply the number to the real build settings and the embedded targets you intend. Check the final file's metadata. A failed or uncertain upload keeps its number reserved until you have checked what happened. A resumed upload keeps its existing upload identity. A new rebuild or restarted upload gets a new number. Never quietly turn on renumbering by the exporter.

Check the real workspace/project, shared scheme, Xcode, SDK, settings and destinations. Resolve dependencies from the project's lockfiles. Archive the chosen Release destination with `xcodebuild`, then export with signing and export options that fit the project. [The export-options document](assets/export-options.plist) needs the real team and keys that the installed Xcode supports.

Check entitlements, profiles, signatures, assets, privacy manifests/reason APIs, permission strings, encryption and behavior in release mode. Simulator binaries are not release files. Use supported Xcode/Transporter/altool upload paths for the real platform and file type. Do not make up platform flags or POST an IPA to `/v1/builds`. The documented buildUploads/buildUploadFiles API has a full package and asset protocol. It is not a shortcut for sending any bytes you like.

Wait for processing and check final errors. Select the build by its real app, platform, version, number and state. Keep the source, toolchain, file hash and symbols. Mac App Store distribution is different from outside Developer ID notarization. See [build detail](references/build-and-release.md).

When an export fails, tell apart Connect API access, cloud-signing permission and the Xcode credential
in use. Keep a valid archive and fix sign-in or provisioning at the step that failed before
rebuilding. Keep keys at their original approved paths. The [export and upload diagnostics](references/build-and-release.md#diagnose-export-credentials-before-rebuilding)
cover role differences, uploader flags, checking pending uploads and final checks of the signed file.

## Listing, ASO and links

Research baseline: 2026-11-05. App name and subtitle each allow 30 characters, description 4,000, promotional text 170 and release notes 4,000. The detailed help pages limit keywords to 100 UTF-8 bytes, even though a marketing overview talks about characters. Stay safely within the byte limit, counting separators.

First recommendation: use as much of the name and subtitle space as you can with meaningful, natural words about the product. Prefer useful candidates that come close to the limit, explain what each term adds, and remove filler or repeats. Filling every character is the owner's writing preference where it works. It is not a store minimum or a ranking promise.

Find the audience's real task or core game loop, a believable difference from other apps and the line between free and paid. Put the brand or purpose in the name where it reads naturally, a subtitle that adds to it, and a description opening that explains a concrete benefit. Then cover the features you can show, compatibility and honest account or purchase requirements. Promotional text shares a real current message. It is not for stuffing keywords. Do not promise better rankings.

Choose relevant local search terms backed by evidence, not made-up search volumes. Avoid repeating app or company names, competitor names you have no right to use and terms that do not fit. Localize the intent, examples and UI words. Do not assume web SEO metadata and App Store search work the same way.

Apple names the title, subtitle, keywords and categories as text inputs for search relevance, along with user behavior. Give the name a clear main task, the subtitle extra value and the keywords other relevant terms, without repeating words already covered. Apple says promotional text does not affect search ranking. The description's first sentence should explain concrete value, followed by features that can be checked and clear account or purchase conditions. Do not stuff it with terms or fix regional prices in the copy.

Choose current primary and secondary category IDs and allowed game subcategories from the real category tree. Apple app tags are created and managed through a separate supported visibility screen. They are not free-form hashtags. AppInfo relationships and version metadata belong to different resources.

Listing text, release notes, promotional text, screenshot captions and preview overlays are product content that customers see. Describe only the app and its changes. Never describe how the copy or media was made, and never mention AI, agents, tools or prompts in it unless the owner clearly asks. When a store policy requires a disclosure, such as sharing data with a third-party AI, record it in the place that owns the declaration (App Privacy, age rating or the in-app consent flow), not in listing copy.

Check support, privacy, marketing and terms links and the real contact and access details. Give factual review notes, working reviewer access, content rights and the required declarations. [Metadata detail](references/metadata-and-marketing.md) explains more field differences.

Use [the complete core-field guide](references/store-fields-and-localizations.md) for every app, AppInfo, version, localization and reviewer field and for every compliance choice. Name, subtitle and privacy fields belong to AppInfo localizations. Description, keywords, promotional text, support, marketing and what's-new belong to version localizations. Release strategy and build link belong to the platform version. Optional in the API and optional for review are different things. Read changed values back under the real parent and locale.

## Pricing, territories and commercial changes

Treat download price, IAP price, subscription price/offer and entitlement as separate settings. Read the real price points for each territory and the existing schedules before changing anything. Choose the base territory, automatic equalization, intended country overrides, start dates, tax category and how future territories behave. Never use a decimal string in place of an Apple price-point resource ID.

Use `appPriceSchedules` for app download pricing and the current v2 `appAvailabilities` / `territoryAvailabilities` for sale countries, dates and preorders. IAP uses its own price schedule and availability resources. Subscriptions use prices, product/plan availability and offer contracts. Keep scheduled prices and decisions for existing customers that are there on purpose. Changing a base territory can delete scheduled changes and change inherited IAP pricing.

Price increases need the real notice or consent rules for each group of customers and country. Do not move preserved subscribers to a new price as a side effect of a catalog edit. App tax category and the owner's financial and legal tasks use their documented console screens. [Commercial instructions](references/pricing-and-availability.md) give the exact resource versions, request shape, order, read-back and customer checks. Price and availability changes can take effect without binary review.

## Screenshots and previews

Use real app captures with harmless demo data. Decorative artwork from an image model must not fake product UI. Keep exact proportions, localized text and layout for each platform. Check at full size and at store size for overlapping text, cut-off controls, stretched frames and captions that are hard to read.

Apple's baseline accepts 1–10 opaque JPEG/JPG/PNG screenshots per device slot. Required and current examples include:

| Slot | Pixel dimensions |
| --- | --- |
| iPhone medium Dynamic Island | 1179×2556 or 1206×2622, plus supported landscape transposes |
| iPhone large display | Dynamic Island 1260×2736, 1290×2796 or 1320×2868, otherwise required Face ID 1284×2778 or 1242×2688, plus transposes |
| iPad 13-inch | 2064×2752 or 2048×2732, plus supported landscape transposes |
| Duo outer | 1398×2034 or 2034×1398 |
| Duo inner | 2007×2853 or 2853×2007 |
| Mac | 1280×800, 1440×900, 2560×1600 or 2880×1800 |
| Apple TV | 1920×1080 or 3840×2160 |
| Apple Vision Pro | 3840×2160, real supported spatial capture |

Duo screenshots become a required release input in April 2027. The screenshot specification limits
the rule to apps using the iOS 27.1 SDK or later, while Apple's October 5 announcement says any app or
game submitted. Because the sources differ, treat Duo screenshots as required for every iPhone
submission from April 2027 unless the live submission flow shows otherwise. For an iPhone release,
prepare real outer and inner captures for the release and include them in the required-device
checklist, not in a list of optional extras. Confirm the current rule at submission and do not make
up an exact day in April. Native Mac, TV and spatial assets stay on their own platforms.
Use current Asset Library reference data for real Duo placement groups and specifications. Use its
dynamic identifiers to find device groups. Never guess group IDs.

Previews are separate videos for each device. Researched baseline: up to three, 15–30 seconds, at most 500 MB and 30 fps with the specified codecs and audio. Mac and TV are landscape. Icons, previews, public screenshots and IAP review screenshots each have different contracts. See [media detail](references/screenshots-and-media.md).

For current public media, read the app's library and `appAssetLibraryRefData`, work out the feature, type, group, specification and category, and reserve an image or video. Send exactly the returned parts, commit `uploaded: true` without a deprecated checksum field and wait for `PREPARE_FOR_SUBMISSION`. Then create a placement on the correct editable localization and order its group. Check the processed `specId`, the real media, the placement review state and the final order. Changing a shared video's poster affects all its placements. Replacing bytes that cannot change needs a new asset and a planned placement replacement, not a guessed PATCH-placement operation.

## Purchases and subscriptions

Model product IDs that cannot change, type, service entitlement, group/level, period, locales, countries, tax, price points, offers, review note/screenshot and where the app offers the purchase. Keep consumables, non-consumables, non-renewing and auto-renewable subscriptions separate. Monthly and annual choices for the same service usually belong in the right shared group, not in unrelated groups just because the length differs.

Create the parent product, group or subscription first. Then create the current draft version, localizations, media, prices, availability and eligible offers. Current version-based resources include inAppPurchaseVersions, subscriptionVersions and subscriptionGroupVersions. Use the current reviewSubmissions/items relationships, not deprecated older submission paths. The first submission that sends a subscription together with an app binary must use the documented console flow.

Use the localized prices and eligibility that StoreKit supports, and show the period, trial, full renewal price, restore, privacy and terms. Check transactions and process updates under one transaction owner. When the app processes purchases directly, deliver benefits in a lasting way that is safe to repeat before finishing the transaction. Standard RevenueCat processing finishes transactions automatically. Check custom benefit delivery on its own through its verified records or webhooks, and do not finish the transaction a second time.

For your own backend, use the separate App Store Server API/library and Notifications V2 contracts. Check signed data against the intended trust root, app and environment, and handle duplicate and out-of-order events. A cancelled subscription can keep access until it expires. Grace, billing retry, refund/revocation and replacement each have different effects.

Test local StoreKit, real sandbox and TestFlight as separate evidence. Cover every plan, restore and account switch, pending approval, renewal, upgrade/downgrade, grace, expiration, refund and duplicate delivery. [Purchase detail](references/purchases-and-subscriptions.md) explains these states further.

## Review, launch and evidence

Complete the platform version, localizations, link to a processed build, review details, declarations, media delivery, sale availability and product readiness. Test the real release UI and backends and the reviewer's path. Being eligible for TestFlight is not App Store approval.

Apply [all relevant review guideline families](references/policy-and-review-checklist.md): safety/UGC/children, completeness and accurate metadata, hardware/software behavior, payments/business models, originality/login/services, privacy/data-sharing/deletion and legal/IP requirements. Include how third-party SDKs behave and any AI-data disclosure or permission that applies. Fill in forms with facts and test the code. Anything without evidence stays BLOCKED.

Submit only within the endpoint the user allowed. Track waiting, in review, rejected/unresolved, approved/pending release and real availability. Release with the chosen manual, scheduled, automatic or phased strategy. A pause does not remove builds people have already downloaded. Recovery usually needs a fix in a higher build and the right review.

Create the current review submission and its eligible version and product items, then set the submission's `submitted` flag. Check item states separately from whether the submission finished. Use eligible cancellation and resolved/removed-item operations on purpose. A rejection for metadata only can reuse the same build where allowed. A binary fix needs a newly reserved build. App Review messages and appeals use the real console or support channel, not customer-review response APIs. Current phased updates run over seven days, allow 30 days of pauses in total and do not block manual downloads.

To replace a queued submission, list the whole set of app, product and group items, wait for the
allowed cancellation, make the editable changes and recreate the intended eligible items before
resubmitting. Check the replacement submission and the selected build. See [the replacement procedure](references/review-and-operations.md#replace-a-queued-submission-without-losing-its-items)
and [Duo capture-to-placement reconciliation](references/screenshots-and-media.md#worked-duo-capture-to-delivery-reconciliation).

Check the real store page and version and the production purchase and restore path. Report app, platform, version and build IDs, source and file evidence, metadata and assets, products and offers, submission and release state, checks and the exact console actions still left. [Operations detail](references/review-and-operations.md) supports this record.

Professional background comes from [Apple's API](https://developer.apple.com/documentation/appstoreconnectapi), [review guidelines](https://developer.apple.com/app-store/review/guidelines/), [product-page guidance](https://developer.apple.com/app-store/product-page/) and the release and monitoring chapters of [Site Reliability Engineering](https://sre.google/sre-book/). Product positioning can use Dunford's [Obviously Awesome](https://www.aprildunford.com/books) as further reading, within its limits. See [sources](references/sources.md) and [license](LICENSE.md).
