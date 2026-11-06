---
name: app-store-connect
description: Create, update and administer Apple store releases for iOS/iPadOS, macOS, tvOS and visionOS through supported API/CLI workflows, including all core fields, ASO, media, pricing, availability, products, rejection recovery, review and release controls.
license: MIT
---

# App Store Connect

Operate a release as a sequence of verified states: prepared source, signed artifact, transferred upload, processed build, complete listing/products, submitted review, approved version and actual storefront availability. These are not interchangeable success states.

This skill is descriptive. Its researched procedures and limits are written here. Do not create refresh scripts, counters, converters or generated API catalogs. Stored information is updated only when the user requests maintenance. Native Apple tools and supported API calls remain the execution surfaces for an explicitly requested app task.

## Brief and platform matrix

Identify team/account role, numeric app ID, stable bundle IDs, SKU, marketing version, source revision, build schemes, signing, locales, territories, actual features and release endpoint. Obtain truthful privacy/encryption/content/age/accessibility answers from implementation and owner. Do not invent declarations or reviewer credentials.

| Target | Connect platform | Archive destination | SDK and main concerns |
| --- | --- | --- | --- |
| iPhone/iPad | `IOS` | `generic/platform=iOS` | `iphoneos`, actual device families and adapted layouts |
| Native Mac | `MAC_OS` | `generic/platform=macOS` | `macosx`, sandbox, signing, entitlements and architectures |
| Apple TV | `TV_OS` | `generic/platform=tvOS` | `appletvos`, focus/remote, safe areas and TV assets |
| Apple Vision Pro | `VISION_OS` | `generic/platform=visionOS` | `xros`, windows/volumes/immersion, input and motion |

Mac Catalyst is the project's actual separate destination/variant. iOS compatibility availability on Mac/Vision Pro is not a native release. A watchOS companion follows the containing app/target graph, without inventing a `WATCH_OS` Connect enum.

Keep platform, version, build, locale, device slot, asset and review relationships explicit. Use [the brief](assets/release-brief.json) as a document template, not an API payload.

Start a field/change inventory in [the release evidence template](assets/release-evidence.md): current value, desired value, owning API/console surface, locale/platform/territory, requiredness, editability, readback and execution status. Preserve intentional existing values. Unknown owner facts remain blocked. Do not fill an optional field merely to make the form look complete.

## Account bootstrap and authentication

Confirm active membership, app access, agreements, paid-app eligibility, bank/tax status and legal distribution authority. Enrollment, agreement signatures and owner attestations require the actual owner. API credentials, distribution signing identities and IAP server credentials serve different purposes.

Provision supported bundle IDs, capabilities, certificates, devices and profiles through the appropriate API resources. Match team/platform/entitlements and all extension IDs. Do not enable every capability speculatively.

The researched `/v1/apps` collection reads app records and has no general POST creation operation. Prepare name, SKU, bundle ID, primary language and platforms, then create the initial record through Apps → New App. Retrieve the resulting app by bundle ID. Creating `/v1/appStoreVersions` is not creating the app itself.

Connect base is `https://api.appstoreconnect.apple.com`. JWTs use ES256, actual `kid`, `typ: JWT`, Unix `iat`/`exp` and `aud: appstoreconnect-v1`. Team keys use the actual issuer in `iss`. Individual keys use `sub: user` and omit `iss`. Ordinary release requests use short lifetimes of at most 20 minutes. Do not generalize special scoped GET lifetime exceptions to writes.

Keep `.p8` keys in the approved secret mechanism, not source/history/logs. A Connect token is not automatically an App Store Server API token. Use the current documented signing library/tool for the selected credential profile instead of inventing cryptography or a wrapper script.

## Supported API resource map and request method

| Domain | Resource families | Critical dependency |
| --- | --- | --- |
| Team/signing | users, invitations, bundle IDs/capabilities, certificates, profiles, devices | Correct identity/role before provisioning |
| App information | apps, appInfos, appInfoLocalizations, appCategories, appTags | App-level information is separate from a version localization |
| Version/build | appStoreVersions, preReleaseVersions, builds, buildUploads, buildUploadFiles | Processed compatible build before version selection |
| Listing media | appAssetLibraries, library images/videos/reference data, placements and ordering requests | Discover specification → reserve/upload/commit → verify → place → order |
| Compliance | ageRatingDeclarations, appEncryptionDeclarations, accessibilityDeclarations | Actual owner/implementation facts |
| Review/release | appStoreReviewDetails, reviewSubmissions/items, release requests, phased releases | Eligible item/state before submit/release |
| Commercial | Territories, app availability, price points/schedules, tax configuration | Intended countries/base territory and actual price model |
| Products | inAppPurchases and current product-version/localization/price/availability resources | Product parent before draft version and review |
| Subscriptions | Groups, subscriptions, group/product versions, offers, prices and availability | Correct service grouping, current version and eligibility |
| Beta/diagnostics | TestFlight groups/testers, beta review/feedback and diagnostics | Correct audience, review and processed build |
| Growth/games/reporting | Custom product pages, experiments, events, nominations, Game Center, analytics and sales/finance reports | Feature/role/platform eligibility |

For an operation, inspect its actual official method, path, required parameters, request/response models and state restrictions. JSON:API uses `data.type`, attributes and relationships with provider resource IDs. A product's display name or store identifier is not necessarily its relationship ID. Omitted/null/deleted are distinct. Do not infer a PATCH contract from a create model.

Follow pagination `links.next` to completion when completeness matters. For uploads, reserve with actual filename/bytes/parent, use each returned method/URL/header/byte range exactly and commit the actual resource's request. Current library assets use the uploaded flag without a checksum field, while dedicated attachments can require their documented checksum. Poll the actual processing state. Do not leak an account bearer header to another upload host. Reconcile uncertain creates/uploads before retrying.

The [functional API map](references/api-coverage.md) covers current core and specialized families: testing, optimization, events, retention, Game Center, hosted assets, alternative distribution, reporting, signing/access, Xcode Cloud/SCM and webhooks. It explains their use and boundaries. New work uses current APIs rather than deprecated set-based media or old submission endpoints. Each operation still requires its actual model and eligibility, not guessed parameters.

For 401 inspect token/time/key, for 403 role/app access/agreements, and for 409/422 exact state and field errors. Respect 429/transient retry guidance with bounded attempts. An unfamiliar state remains unresolved, not success. [API detail](references/api-and-bootstrap.md) expands the resource/request decisions.

## Build numbers and signed release artifacts

Marketing version and `CFBundleVersion` are different. Before every new upload, read all relevant remote builds/pre-release versions and pending uploads, include local/CI reservations, and acquire the project's existing allocation lock. Choose a fresh monotonically increasing supported number, reserve it durably, then build. A local `max + 1` calculation alone cannot prevent two runners choosing the same value.

Apply the number to actual build settings and intended embedded targets. Inspect the final artifact's metadata. A failed/uncertain upload remains reserved until reconciled. A resumable continuation uses its existing upload identity. A new rebuilt/restarted upload gets a new allocation. Never silently enable exporter-managed renumbering.

Inspect the real workspace/project, shared scheme, Xcode, SDK, settings and destinations. Resolve dependencies from the project's lockfiles. Archive the selected Release destination with `xcodebuild`, then export with project-appropriate signing/export options. [The export-options document](assets/export-options.plist) needs the real team and installed-Xcode-supported keys.

Validate entitlements, profiles, signatures, assets, privacy manifests/reason APIs, permission strings, encryption and release-mode behavior. Simulator binaries are not release artifacts. Use supported Xcode/Transporter/altool upload paths for the actual platform/file type. Do not invent platform flags or POST an IPA to `/v1/builds`. The documented buildUploads/buildUploadFiles API has a complete package/asset protocol, not a generic arbitrary-byte shortcut.

Wait for processing and inspect terminal errors. Select the build by actual app/platform/version/number/state. Preserve source/toolchain/artifact hash and symbols. Mac App Store distribution is distinct from external Developer ID notarization. See [build detail](references/build-and-release.md).

For an export failure, distinguish Connect API access from cloud-signing permission and the selected
Xcode credential. Preserve a valid archive and repair authentication/provisioning at the failed stage
before rebuilding. Keep keys at their original approved paths. The [export and upload diagnostics](references/build-and-release.md#diagnose-export-credentials-before-rebuilding)
cover role differences, uploader flags, pending-upload reconciliation and final signed-artifact checks.

## Listing, ASO and links

Research baseline: 2026-11-05. App name and subtitle each allow 30 characters, description 4,000, promotional text 170 and release notes 4,000. Detailed help limits keywords to 100 UTF-8 bytes, despite a marketing overview using character wording. Use the byte ceiling conservatively, including separators.

First recommendation: use as much of the available name/subtitle capacity as possible with meaningful, natural, product-relevant language. Prefer useful near-capacity candidates, explain what each term contributes, and remove filler or duplication. Filling every character is the owner's editorial preference where practical, not a store minimum or ranking guarantee.

Identify the audience's actual task/core game loop, credible differentiator and paid/free boundary. Write brand/purpose in the name where natural, a complementary subtitle and a description opening that explains a concrete benefit. Follow with demonstrated features, compatibility and truthful account/purchase requirements. Promotional text communicates a real current message, not keyword stuffing. Do not promise ranking improvements.

Choose relevant localized search terms with evidence, not invented volumes. Avoid repeated app/company names, unauthorized competitor names and irrelevant terms. Localize intent, examples and UI terminology. Do not assume web SEO metadata and App Store indexing are the same system.

Apple identifies title, subtitle, keywords and categories as text-relevance inputs alongside user behavior. Allocate a clear primary task to the name, complementary value to the subtitle and additional relevant terms to keywords without repeating covered words. Promotional text explicitly does not affect search ranking. The description's first sentence should explain concrete value, followed by verifiable features and transparent account/purchase conditions. Do not stuff it with terms or freeze regional prices into copy.

Choose current primary/secondary category IDs and allowed game subcategories from the actual category hierarchy. Apple app tags are generated/managed through a separate supported visibility surface, not arbitrary hashtags. AppInfo relationships and version metadata belong to different resources.

Verify support/privacy/marketing/terms links and actual contact/access information. Provide factual review notes, working reviewer access, content rights and the required declarations. [Metadata detail](references/metadata-and-marketing.md) gives further field distinctions.

Use [the complete core-field guide](references/store-fields-and-localizations.md) for every app/AppInfo/version/localization/reviewer attribute and compliance decision. Name/subtitle/privacy fields belong to AppInfo localizations. Description/keywords/promotional text/support/marketing/what's-new belong to version localizations. Release strategy/build linkage belong to the platform version. API-optional and review-optional are different concepts. Read changed values back under the actual parent and locale.

## Pricing, territories and commercial changes

Treat download price, IAP price, subscription price/offer and entitlement as separate configurations. Read actual territory-specific price points and existing schedules before mutation. Choose base territory, automatic equalization, deliberate country overrides, effective dates, tax category and future-territory behavior. Never substitute a decimal string for an Apple price-point resource ID.

Use `appPriceSchedules` for app-download pricing and current v2 `appAvailabilities` / `territoryAvailabilities` for sale countries, dates and preorders. IAP uses its own price schedule/availability resources. Subscriptions use prices, product/plan availability and offer contracts. Preserve intended scheduled prices and existing-customer price decisions. Changing a base territory can delete scheduled changes and affect inherited IAP pricing.

Price increases require the actual cohort/country notification or consent rules. Do not migrate preserved subscribers as an incidental catalog edit. App tax-category and owner financial/legal tasks use their documented console surfaces. [Commercial instructions](references/pricing-and-availability.md) provide exact resource versions, request shape, sequence, readback and customer verification. Price and availability changes can take effect independently of binary review.

## Screenshots and previews

Use real app captures with harmless demo data. Decorative image-model artwork must not fabricate product UI. Preserve exact proportions, localized text and platform-specific layout. Inspect full size and storefront size for overlapping text, clipped controls, distorted frames and unreadable captions.

Apple's baseline accepts 1–10 opaque JPEG/JPG/PNG screenshots per device slot. Required/current examples include:

| Slot | Pixel dimensions |
| --- | --- |
| iPhone medium Dynamic Island | 1179×2556 or 1206×2622, plus supported landscape transposes |
| iPad 13-inch | 2064×2752 or 2048×2732, plus supported landscape transposes |
| Duo outer | 1398×2034 or 2034×1398 |
| Duo inner | 2007×2853 or 2853×2007 |
| Mac | 1280×800, 1440×900, 2560×1600 or 2880×1800 |
| Apple TV | 1920×1080 or 3840×2160 |
| Apple Vision Pro | 3840×2160, actual supported spatial capture |

Duo screenshots become a required release input in April 2027 under the screenshot specification's
iOS 27.1 SDK-or-later condition. Apple's October 5 announcement uses broader submission wording.
For an applicable iPhone release, prepare real outer/inner captures now and include them in the
required-device checklist, not an optional polish backlog. Confirm the current rule at submission
and do not invent an exact day within April. Native Mac/TV/spatial assets remain their own platforms.
Use current Asset Library reference data for real Duo placement groups/specifications. Its dynamic
identifiers support device discovery without an old screenshot enum. An absent deprecated enum is
not proof that the current API cannot upload a required device family. Never guess group IDs.

Previews are separate device-specific videos: researched baseline up to three, 15–30 seconds, at most 500 MB and 30 fps with the specified codecs/audio. Mac/TV are landscape. Icons, previews, public screenshots and IAP review screenshots have different contracts. See [media detail](references/screenshots-and-media.md).

For current public media, read the app's library and `appAssetLibraryRefData`, resolve feature/type/group/specification/category and reserve an image/video. Transfer exact returned parts, commit `uploaded: true` without a deprecated checksum field and await `PREPARE_FOR_SUBMISSION`. Then create a placement on the correct editable localization and order its group. Inspect processed `specId`, actual media, placement review state and final order. Shared-video poster changes affect all placements. Replacing immutable bytes requires a new asset and deliberate placement replacement, not a guessed PATCH-placement operation.

## Purchases and subscriptions

Model immutable product IDs, type, service entitlement, group/level, period, locales, countries, tax, price points, offers, review note/screenshot and app entrypoint. Separate consumables, non-consumables, non-renewing and auto-renewable subscriptions. Monthly/annual alternatives for the same service usually belong to the appropriate shared group, not unrelated groups merely for duration.

Create the parent product/group/subscription, then the current draft version/localizations/media, prices/availability and eligible offers. Current version-based resources include inAppPurchaseVersions, subscriptionVersions and subscriptionGroupVersions. Use the current reviewSubmissions/items relationships, not deprecated pre-version submission paths. The researched first combined subscription/binary submission requires the documented console flow.

Use StoreKit-supported localized prices/eligibility and disclose period, trial, full renewal price, restoration, privacy and terms. Verify transactions and process updates under one transaction owner. For direct application-owned processing, deliver benefits durably and idempotently before finishing. Standard RevenueCat processing completes transactions automatically. Reconcile custom benefit delivery independently through its verified records/webhooks and do not finish a second time.

For a direct backend, use the separate App Store Server API/library and Notifications V2 contracts. Verify signed data against the intended trust/app/environment and reconcile duplicate/out-of-order events. Cancellation can retain access until expiration. Grace, billing retry, refund/revocation and replacement have distinct effects.

Test local StoreKit, real sandbox and TestFlight as separate evidence. Cover every plan, restore/account switch, pending approval, renewal, upgrade/downgrade, grace, expiration, refund and duplicate delivery. [Purchase detail](references/purchases-and-subscriptions.md) expands these states.

## Review, launch and evidence

Complete platform version/localizations, processed build association, review details, declarations, media delivery, commercial availability and product readiness. Test the actual release UI/backends and reviewer path. TestFlight eligibility is not App Store approval.

Apply [all relevant review guideline families](references/policy-and-review-checklist.md): safety/UGC/children, completeness and accurate metadata, hardware/software behavior, payments/business models, originality/login/services, privacy/data-sharing/deletion and legal/IP requirements. Include third-party SDK behavior and applicable AI-data disclosure/permission. Fill factual forms and test the implementation. Missing evidence remains BLOCKED.

Submit only within the user's endpoint scope. Track waiting, in-review, rejected/unresolved, approved/pending-release and actual availability. Release using the chosen manual/scheduled/automatic/phased strategy. A pause does not uninstall already downloaded builds. Recovery normally requires a higher-build forward fix and appropriate review.

Create the current review submission and eligible version/product items, then set the actual submission `submitted` flag. Inspect item states separately from submission completion. Use eligible cancellation and resolved/removed-item operations deliberately. Metadata-only rejection can reuse the same build where allowed, while a binary correction needs a newly reserved build. App Review correspondence/appeals use the actual console/support surface, not customer-review response APIs. Current phased updates follow seven days with a total 30-day pause allowance and do not prevent manual downloads.

For replacing a queued submission, inventory the entire app/product/group item graph, wait for the
authorized cancellation, apply editable changes and recreate the intended eligible graph before
resubmission. Verify the replacement submission and selected build. See [the replacement procedure](references/review-and-operations.md#replace-a-queued-submission-without-losing-its-items)
and [Duo capture-to-placement reconciliation](references/screenshots-and-media.md#worked-duo-capture-to-delivery-reconciliation).

Verify the actual storefront/version and production purchase/restore path. Report app/platform/version/build IDs, source/artifact evidence, metadata/assets, products/offers, submission/release state, checks and exact remaining console actions. [Operations detail](references/review-and-operations.md) supports this record.

Professional context comes from [Apple's API](https://developer.apple.com/documentation/appstoreconnectapi), [review guidelines](https://developer.apple.com/app-store/review/guidelines/), [product-page guidance](https://developer.apple.com/app-store/product-page/) and the release/monitoring chapters of [Site Reliability Engineering](https://sre.google/sre-book/). Product positioning can use Dunford's [Obviously Awesome](https://www.aprildunford.com/books) as further reading, with its context limits. See [sources](references/sources.md) and [license](LICENSE.md).
