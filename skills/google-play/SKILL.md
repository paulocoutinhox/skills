---
name: google-play
description: Create, update and administer Google Play releases through supported API/CLI workflows, including core fields, ASO, media, prices/countries, products/plans/offers, policy declarations, review conflicts, rejection recovery and controlled rollout.
license: MIT
---

# Google Play

Treat developer setup, signed build, uploaded artifact, committed edit, review approval and production availability as separate states. Explain the complete route to the requested endpoint without bundling scripts, generated schemas or automatic information refresh.

## Brief, identity and account setup

Identify repository, developer account, permanent package name, actual Gradle variant, signing, versionName, devices, locales, countries, audience, app/game type, free/paid model, products and authorized track/release scope. Use [the brief template](assets/release-brief.json) as a document, not an API payload.

Start [the field/release evidence record](assets/release-evidence.md). Inventory current and intended values, owning API/console surface, locale/device/country, editability, requiredness, readback and test status. Preserve unrequested settings and mark unknown owner facts BLOCKED. Do not populate every optional feature speculatively.

Confirm owner verification, account standing, agreements, payments/tax/trader facts and appropriate permissions. Initial app creation uses the current Play Console workflow. The researched Publisher contract has no general `applications.insert` creation operation. An edit is a transaction on an existing app, not a new app record.

Package identity is permanent and must match the actual artifact. App signing and upload keys are different under Play App Signing. Keep recovery and certificate fingerprints clear. Do not assume a free-to-paid change is freely reversible.

Enable the Android Publisher API in the selected Cloud project and grant the service identity the necessary Play Console app access. The current setup no longer requires the obsolete developer-account/Cloud-project linkage step. Use OAuth scope `https://www.googleapis.com/auth/androidpublisher`, preferably through the supported short-lived identity mechanism. Never use a browser cookie as an API credential or commit service-account/signing secrets.

## API model and resource map

Base service is `https://androidpublisher.googleapis.com/androidpublisher/v3/`. Use the exact official method/path, request model, scopes, pagination and media-upload protocol. An update mask or regions version is part of the contract when specified. Do not extrapolate fields from a similarly named endpoint.

| Domain | Publisher families | Contract distinction |
| --- | --- | --- |
| Listing/builds/tracks | edits, details, listings, images, bundles/APKs, deobfuscation, tracks/testers/countries | Explicit edit/validate/commit lifecycle |
| Data safety | applications.dataSafety | Available API operation, truthful declaration payload required |
| One-time catalog | monetization.onetimeproducts, purchaseOptions and offers | Product/option/offer lifecycle outside listing edits |
| Subscriptions | monetization.subscriptions, basePlans and offers | Product, active plan and eligible offer are separate |
| Existing older catalog | inappproducts | Inspect actual migration state rather than introducing legacy structure for new work |
| Transactions | purchases.products/productsv2/subscriptions/subscriptionsv2 | Customer purchase state, not product configuration |
| Financial correction | orders, voided purchases and supported refund/revoke operations | Customer-affecting actions with explicit scope |
| Other administration | Reviews, generated APKs, internal sharing, signing/recovery/users/grants and current documented resources | Per-method eligibility and effect |

The [complete functional API map](references/api-coverage.md) covers every resource family in the researched Publisher snapshot, with actual methods, workflow and boundaries. It includes program-specific `appstoreappsreview` and app-store catalog operations, which are distinct from ordinary Google Play app creation/review. Use those only for the actual eligible app-store-hosted program, not as a missing `applications.insert` workaround.

Reporting, Play Integrity, Pub/Sub and client Billing have separate APIs. This guide does not turn one Publisher schema into every Google service. Use their exact official contracts for the relevant integration.

Read all required pages when selecting maximum version/state or reconciling catalog changes. Handle 401/403 by actual token/scope/app permissions, 400/422 by exact fields, and 409 by edit/state conflicts. Bound transient retries and reconcile uncertain writes. [API detail](references/api-and-bootstrap.md) expands these decisions.

## Compile and allocate version codes

Inspect the committed wrapper, AGP/Kotlin/JDK/SDK, product flavors, native libraries and actual application ID. Use existing coherent commands and lockfiles. Native compilation uses the project's real toolchain, not a generic wrapper created by this skill.

A positive `versionCode` is separate from display `versionName`. The Play maximum is 2,100,000,000. Under the project's allocation lock, inspect all relevant tracks, uploaded artifacts/historical maximum and pending CI reservations. Reserve a fresh higher code before each new artifact upload. A local comparison without a lock does not prevent two jobs choosing the same value.

Write the code into the actual Gradle/version source. Passing a `-P` property has no effect unless the build reads it. Confirm flavor overrides and inspect the final manifest. A new failed/rebuilt upload needs a new reservation. A resumable continuation uses the same recorded upload session rather than creating a duplicate.

Use a real release signing/upload key, not a debug certificate. Build the actual release AAB, run relevant lint/tests and release-mode device checks, validate with the supported bundletool, and inspect package/version, SDK levels, permissions, exported components, ABIs, debug flags, modules and signature. Preserve hashes, mappings and native symbols.

Target API/Billing deadlines and 16 KB native page support depend on actual release date/form factor. Identify the applicable rule rather than hardcoding an obsolete SDK floor. Test phone/tablet/foldable and every actually claimed watch/TV/automotive/PC/XR capability. [Build detail](references/build-and-versioning.md) explains propagation and recovery.

## Listing, ASO, categories and links

Research baseline: 2026-11-05. Title allows 30 characters, short description 80, full description 4,000 and release notes 500 Unicode characters per locale. The listing's `video` is an eligible YouTube link. AppDetails contains supported contact fields, not invented subtitle/keywords/promotional text/category/tag properties.

First recommendation: use as much of the title and short-description capacity as possible for meaningful, natural and relevant language. Aim near 30/80 where that improves the message. Google has no ordinary subtitle field. Explain each term's actual intent/feature fit and remove filler/duplication. This is the owner's editorial preference where practical, not a store minimum or a promise of ranking gains.

Identify the real problem or core game loop, target audience and demonstrated benefit. Make title, short description, icon and opening screenshots communicate the same promise. Use relevant localized language naturally. Do not repeat keywords mechanically, fabricate ranking/price badges or promise features/countries the app lacks. Store search and web landing-page SEO are different systems.

Choose a clear primary task for the title and a complementary benefit/differentiator for the short description. The full description explains verified workflows, features, compatibility and account/payment conditions, rather than repeating a word list. Google's discovery guidance includes metadata, relevance, quality and user response. Exact ranking weights and keyword-density formulas are not published guarantees. Measure actual qualified conversion/retention by source/locale and keep campaign effects separate.

Choose app/game and current primary category by actual purpose. Up to five approved tags describe real functionality/mechanics, not arbitrary hashtags. The researched listing schema lacks category/tag writes, so prepare precise console selections. Do not send invented JSON fields and mistake ignored values for success.

Verify real support/privacy/terms/deletion links and actual contact details. Data safety must account for app/backend/SDK collection/sharing, purposes, required/optional behavior, encryption and deletion. Use `applications.dataSafety` where appropriate to the actual declaration contract. Other content-rating, ads, audience, access and sensitive-permission tasks may require console forms. Never answer “no collection” just because one analytics flag is off.

The current Data safety request carries official CSV contents in the `safetyLabels` string, outside the edit. It is not an invented nested JSON questionnaire. Ordinary AppDetails owns only default language/contact fields. Listing owns language/title/short/full description/video. TrackRelease owns release name, version codes, notes, status, fraction, country targeting and update priority. [The field and ASO guide](references/listing-and-marketing.md) explains every core field, limits, request example, preservation and actual console tasks.

## Pricing and availability

App-download price/free-paid status, IAP option price, subscription price/offer and customer entitlement are separate. Read current country/currency/tax decisions, catalog and subscriber cohorts first. Ordinary Listing/AppDetails has no download-price field. Use the actual App pricing console flow where no documented method exists. A published free app cannot become paid, so paid-to-free is not a reversible temporary workaround.

Use supported Money units/nanos, current region versions and precise update masks. One-time products have purchase-option regional pricing/availability, future-region choices and dedicated activation. Subscriptions have base-plan prices, new-subscriber/future-region availability and separately authorized existing-cohort migrations. A regional price does not distribute the app there, and an active offer cannot override an inactive parent.

Preserve existing scheduled/commercial choices and distinguish customer price from tax/proceeds. Product changes are outside edit transactions and can take effect independently. [Commercial instructions](references/pricing-and-availability.md) provide actual request shapes, paths, activation/cohort decisions and verification. Do not use retired pricing templates or invent a universal float price/app-country endpoint.

For a worked ASO direction, a genuine local reading-notes app can emphasize organizing/finding notes without upload. It must not promise cloud sync or measured time savings absent from the product evidence. Localize the value and examples, not just the words. [Listing detail](references/listing-and-marketing.md) expands the editorial procedure.

## Media and device-specific truth

Capture actual UI with harmless data. Decorative image-model artwork must not fabricate app functionality. Check proportion, readable type, safe crop, permission content, privacy and overlays at both full and storefront size. Recompose for tablet/foldable/TV/XR instead of stretching phone content.

| Asset/surface | Researched baseline |
| --- | --- |
| Store icon | 512×512, 32-bit PNG, at most 1,024 KB |
| Feature graphic | 1024×500, JPEG/24-bit opaque PNG |
| General screenshots | At least two overall, up to eight per device type, 320–3840px with largest dimension at most twice smallest |
| Phone high-resolution example | 1080×1920 portrait or 1920×1080 landscape |
| Tablet/Chromebook | Specialized guidance: at least four, 1080–7680px, 16:9 or 9:16, core UI |
| Wear OS | At least one 1:1 minimum 384×384, interface-only, no added device frame/text/background |
| Android TV | At least one screenshot and a 1280×720 eligible banner |
| Automotive when provided | At least two 800×1280 portrait and two 1024×768 landscape, generic system UI |
| Android XR | Four to eight PNG/JPEG, at most 8 MB each, 8:5, minimum 1920×1200, recommended 3840×2400 |

The same official page has general and specialized large-screen ranges. Apply the actual target slot and expose that distinction. Basic upload validity and featuring eligibility differ. Qualifying screenshot-based recommendations have additional app/game count/resolution/aspect conditions.

Upload images to the correct locale/type within the intended edit, using supported media protocols and actual parameter enums. Preserve ordering and existing source assets until replacements are verified. A newer console-only type is not permission to invent an API enum. [Media detail](references/screenshots-and-media.md) covers the surface distinctions.

Inspect actual bytes, returned image IDs/hashes and gallery order before committing. The current image upload supports truthful `aiGeneratedState` attestation. It does not permit fabricated UI. Ordinary image methods have no reorder endpoint. Prepare a complete validated replacement and perform any necessary delete/upload sequence in the serialized edit. Newer Asset Library/experiment/event/form-factor console surfaces do not imply an unlisted Publisher API.

## Billing graph and customer access

Choose immutable IDs, benefits, type, regions, price/tax model and restoration behavior. For current one-time products, configure the actual purchase options/offers. For subscriptions, distinguish product, base plan and offer. Monthly/annual, auto-renewing/prepaid and installment options have different schemas and lifecycle rules.

Read existing state before mutation. Configure exact regional prices, regionsVersion/update masks, eligibility and effective dates. Activate the intended purchasable plan/option/offer and verify client-visible results. Catalog writes are outside edit transactions. A failed listing commit does not roll back a price change.

Use the current compatible Billing client/SDK, current product details and eligible offer tokens. Show localized full price, interval, trial/discount phases, renewal and cancellation/restoration terms. Verify purchases on the trusted backend, including package/product/token/state and line items. Do not trust a client success flag.

Grant only completed purchases. With direct application-owned processing, persist idempotent delivery before acknowledgment/consumption. The ordinary acknowledgment window is three days after completion, with pending timing and current exceptions checked. Standard RevenueCat processing owns automatic completion. Reconcile custom delivery from its verified records/webhooks and never acknowledge independently a second time.

Configure authenticated RTDN/Pub/Sub delivery and reconcile authoritative purchase state. Handle duplicates/out-of-order events, renewal, pending completion, prepaid top-up, replacement/linked tokens, cancellation, grace, account hold, pause, expiry, refund and revocation. Cancellation can preserve paid access until expiration. Consumables require a durable balance/delivery policy. See [billing detail](references/products-and-subscriptions.md).

## First production app and console prerequisites

If the app is still a draft, an uploaded/committed production draft may require the first Console
confirmation. Follow [the complete first-production sequence](references/first-production-release.md)
from the real dashboard prerequisites through exact build confirmation, countries, Publishing overview
and acknowledged submission. Reuse the uploaded AAB. Do not substitute internal testing for requested
production review or report `completed` track status as public availability.

Inspect saved declarations and the final merged manifest. Contains ads, Advertising ID use, consent,
target audience and IARC content ratings are independent answers. A child dialog's Add/Save can be
separate from saving its parent. Diagnose validation/focus/scroll state before repeating failed clicks.

## Edit, review and rollout sequence

1. Serialize package release changes and create an edit with its ID/expiry recorded.
2. Read existing details/listings/images/tracks/artifacts and preserve the intended release graph.
3. Upload the signed AAB through the documented media path, verify returned code and attach relevant mappings/symbols.
4. Apply intended listing/media changes and update only the selected track with actual version codes, localized notes and explicit status.
5. Validate the edit, resolve errors and commit when within scope. Re-read remote track and review state.
6. Complete outstanding app content/review actions and the correct managed-publishing step where eligible.
7. Verify actual release availability, installability, vital/backend/billing behavior and rollout impact.

Choose commit review-conflict behavior explicitly. Current `changesInReviewBehavior` defaults to `CANCEL_IN_REVIEW_AND_SUBMIT`, which can cancel an ongoing review. Use `ERROR_IF_IN_REVIEW` when that review should remain intact and handle the returned conflict without silently changing intent. The rejection-specific `changesNotSentForReview` contract is separate from managed publishing and approval. Commit has an empty request body.

`draft`, `inProgress`, `halted` and `completed` have different effects. An in-progress rollout needs the intended supported fraction. Do not change to completed as a workaround for validation errors. `tracks.update` concerns the desired release graph, not an excuse to discard retained versions.

Set in-app update priority within 0–5 before rollout. Country targeting is permitted only for applicable production in-progress releases and is not general app distribution. Respect real form-factor track IDs, edit expiry and concurrent console/API changes. After commit, verify through a valid current read context rather than treating the finalized edit as editable.

Managed publishing cannot hold an app's first publication and has immediate-effect exceptions. Internal sharing is separate from an internal test track. Personal accounts created after November 13, 2023 have the researched 12-testers/14-continuous-days closed-test requirement before applying for production access. Do not fake engagement or imply API upload bypasses eligibility.

Apply [the policy/readiness checklist](references/policy-and-review-checklist.md) to the actual binary/backend/SDKs: content/audience, UGC/AI, privacy/deletion, permissions, billing/ads, rights, stable functionality and claimed device programs. Complete real App content/reviewer tasks and maintain working access. Separate app, update and item status. A live app can have a rejected pending update.

A committed edit is not review approval or public availability. Reproduce each rejection, correct the responsible metadata/access/declaration or binary, retest and resubmit through the actual supported API/console path. Metadata-only fixes can retain an eligible binary. Code changes require a newly reserved higher code. Customer `reviews.reply` is not a policy appeal API.

Halt eligible staged or fully rolled-out releases only within scope and actual eligibility. Full-release halting excludes internal tracks/first track releases and requires an eligible prior version. It changes future serving, not already installed apps. Prepare a higher-code forward fix. Report package/version/artifact, signing evidence, complete fields/assets/prices, edit/track/countries/fraction, policy/product state, actual checks and exact handoffs. [Release detail](references/edits-review-and-rollout.md) provides concrete steps.

Official [Publisher API](https://developers.google.com/android-publisher/api-ref/rest), [asset guidance](https://support.google.com/googleplay/android-developer/answer/9866151?hl=en), [Billing guidance](https://developer.android.com/google/play/billing/integrate) and [managed-publishing help](https://support.google.com/googleplay/android-developer/answer/9859654?hl=en) govern their respective surfaces. The [SRE release-engineering](https://sre.google/sre-book/release-engineering/) chapter and Dunford's [positioning book](https://www.aprildunford.com/books) offer professional context, not store-approval guarantees. See [sources](references/sources.md) and [license](LICENSE.md).
