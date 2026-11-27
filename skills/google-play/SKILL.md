---
name: google-play
description: Create, update and manage Google Play releases through supported API/CLI workflows, including core fields, ASO, media, prices and countries, products, plans and offers, policy declarations, review conflicts, fixing rejections and controlled rollout.
license: MIT
---

# Google Play

Treat these as separate states: developer setup, signed build, uploaded artifact, committed edit, review approval and production availability. Explain the full route to the requested endpoint. Do not bundle scripts, generated schemas or automatic information refresh.

## Brief, identity and account setup

Identify the repository, developer account, permanent package name, actual Gradle variant, signing, versionName, devices, locales, countries, audience, app or game type, free or paid model, products and the authorized track and release scope. Use [the brief template](assets/release-brief.json) as a document, not an API payload.

Start [the field/release evidence record](assets/release-evidence.md). List current and intended values, the API or console surface that owns each one, locale/device/country, whether it can be edited, whether it is required, the readback and the test status. Keep settings nobody asked to change, and mark unknown owner facts BLOCKED. Do not fill in every optional feature just in case.

Record the authorized endpoint as `prepare`, an internal/test upload, review submission, production rollout or limited administration, matching the brief's `authorized-endpoint`. Do the ordinary prerequisites inside that endpoint without asking again, then stop. Report the next step you did not run, whether a commit, Console action or rollout change, with its effect on customers. Do not move on to a later state.

Confirm owner verification, account standing, agreements, payments/tax/trader facts and the right permissions. You create a new app through the current Play Console workflow. The Publisher API we researched has no general `applications.insert` operation for creating apps. An edit is a transaction on an existing app, not a new app record.

The package name is permanent and must match the actual artifact. Under Play App Signing, the app signing key and the upload key are different keys. Keep recovery details and certificate fingerprints clear. Do not assume you can freely undo a change from free to paid.

Enable the Android Publisher API in the chosen Cloud project and give the service identity the Play Console app access it needs. The current setup guide does not require linking the developer account to a Cloud project. Use OAuth scope `https://www.googleapis.com/auth/androidpublisher`, preferably through the supported short-lived identity method. Before asking the user for a service-account key, check the environment variable `GOOGLE_STORE_CERTIFICATES_PATH` (the folder that holds the key files). Read only the file names and paths you need. Never print a key's contents. Ask the user only for what is missing. Never use a browser cookie as an API credential, and never commit service-account or signing secrets.

## API model and resource map

The base service is `https://androidpublisher.googleapis.com/androidpublisher/v3/`. Use the exact official method and path, request model, scopes, pagination and media-upload protocol. When the docs specify an update mask or regions version, it is part of the contract. Do not guess fields from an endpoint with a similar name.

| Domain | Publisher families | How they differ |
| --- | --- | --- |
| Listing/builds/tracks | edits, details, listings, images, bundles/APKs, deobfuscation, tracks/testers/countries | Explicit edit, validate and commit lifecycle |
| Data safety | applications.dataSafety | Available API operation, needs an honest declaration payload |
| One-time catalog | monetization.onetimeproducts, purchaseOptions and offers | Product, option and offer lifecycle outside listing edits |
| Subscriptions | monetization.subscriptions, basePlans and offers | Product, active plan and eligible offer are separate |
| Transactions | purchases.products/productsv2/subscriptions/subscriptionsv2 | Customer purchase state, not product setup |
| Financial correction | orders, voided purchases and supported refund/revoke operations | Actions that affect customers, with an explicit scope |
| Other administration | Reviews, generated APKs, internal sharing, signing/recovery/users/grants and current documented resources | Eligibility and effect differ per method |

The [complete functional API map](references/api-coverage.md) covers every resource family in the Publisher snapshot we researched, with the real methods, workflow and limits. It includes the program-specific `appstoreappsreview` and app-store catalog operations, which are not the same as ordinary Google Play app creation or review. Use those only for an app that really is in the eligible app-store-hosted program, not as a way around the missing `applications.insert`.

Reporting, Play Integrity, Pub/Sub and the client Billing library each have their own APIs. This guide does not treat one Publisher schema as every Google service. Use each one's exact official contract for the integration at hand.

Read all the pages you need when you pick the highest version or state, or when you match up catalog changes. Handle 401/403 by checking the real token, scope and app permissions, 400/422 by checking the exact fields, and 409 as an edit or state conflict. Limit retries for temporary errors, and check the real result of any write whose outcome is unclear. [API detail](references/api-and-bootstrap.md) explains these decisions further.

## Compile and allocate version codes

Inspect the committed wrapper, AGP/Kotlin/JDK/SDK, product flavors, native libraries and the actual application ID. Use the existing commands and lockfiles when they fit together. Native builds use the project's real toolchain, not a generic wrapper made by this skill.

A positive `versionCode` is separate from the display `versionName`. The Play maximum is 2,100,000,000. While holding the project's allocation lock, check all relevant tracks, uploaded artifacts and the highest code ever used, and pending CI reservations. Reserve a fresh, higher code before each new artifact upload. A local comparison without a lock does not stop two jobs from picking the same value.

Write the code into the real Gradle or version source. A `-P` property does nothing unless the build reads it. Confirm flavor overrides and inspect the final manifest. A new upload after a failure or rebuild needs a new reservation. Continuing a resumable upload uses the same recorded upload session instead of creating a duplicate.

Use a real release signing or upload key, not a debug certificate. Build the actual release AAB, run the relevant lint and tests and the release-mode device checks, and validate it with the supported bundletool. Inspect the package and version, SDK levels, permissions, exported components, ABIs, debug flags, modules and signature. Keep the hashes, mappings and native symbols.

Target API and Billing deadlines, and 16 KB native page support, depend on the actual release date and form factor. Find the rule that applies instead of hardcoding an outdated SDK floor. Test phone, tablet and foldable, and every watch, TV, automotive, PC or XR feature the app really claims. [Build detail](references/build-and-versioning.md) explains how values flow through the build and how to recover.

## Listing, ASO, categories and links

Listing limits were checked on 2026-11-05. The title allows 30 characters, the short description 80, the full description 4,000 and release notes 500 Unicode characters per locale. The listing's `video` is an eligible YouTube link. AppDetails holds the supported contact fields. It has no subtitle, keywords, promotional text, category or tag properties, so do not invent them.

First recommendation: use as much of the title and short description space as you can for meaningful, natural and relevant words. Aim near 30/80 where that makes the message better. Google has no ordinary subtitle field. Explain how each term fits a real user intent or feature, and remove filler and repeats. This is the owner's editorial preference where it is practical, not a store minimum or a promise of better ranking.

Identify the real problem or core game loop, the target audience and the benefit the app shows. Make the title, short description, icon and first screenshots tell the same promise. Use relevant local language naturally. Do not repeat keywords mechanically, make up ranking or price badges, or promise features or countries the app does not have. Store search and web landing-page SEO are different systems.

Pick one clear main task for the title and a benefit or difference that adds to it for the short description. The full description explains real, checked workflows, features, compatibility and account or payment conditions, instead of repeating a list of words. Google's discovery guidance covers metadata, relevance, quality and how users respond. Exact ranking weights and keyword-density formulas are not published guarantees. Measure real qualified conversion and retention by source and locale, and keep campaign effects separate.

Choose app or game and the current main category by the app's real purpose. Up to five approved tags describe real features or game mechanics, not random hashtags. The listing schema we researched cannot write category or tags, so prepare exact console choices. Do not send made-up JSON fields and then mistake ignored values for success.

The title, descriptions, release notes, screenshot captions and feature graphics are product content that customers see. Describe only the app and its changes. Never say how the copy or artwork was made, and never mention AI, agents, tools or prompts in it unless the owner clearly asks. Record required disclosures in the declaration that owns them, such as the image upload's `aiGeneratedState` attestation or Data safety, not in listing copy.

Check that the support, privacy, terms and deletion links work and that the contact details are real. Data safety must cover what the app, backend and SDKs collect and share, the purposes, required or optional behavior, encryption and deletion. Use `applications.dataSafety` where it fits the real declaration contract. Other tasks, such as content rating, ads, audience, access and sensitive permissions, may need console forms. Never answer “no collection” just because one analytics flag is off.

The current Data safety request sends the official CSV contents in the `safetyLabels` string, outside the edit. It is not a made-up nested JSON questionnaire. Ordinary AppDetails owns only the default language and contact fields. Listing owns language, title, short and full description, and video. TrackRelease owns release name, version codes, notes, status, fraction, country targeting and update priority. [The field and ASO guide](references/listing-and-marketing.md) explains every core field, the limits, a request example, how to keep existing values and the real console tasks.

## Pricing and availability

App download price and free or paid status, the IAP option price, the subscription price and offer, and customer entitlement are separate things. First read the current country, currency and tax decisions, the catalog and the subscriber groups. Ordinary Listing/AppDetails has no download-price field. Use the real App pricing console flow where no documented method exists. Read the intended free or paid model from the owner's plan, the brief and the other stores before you touch App pricing, and check it again right before Send changes for review. The first submission of a free app locks it as free, even before it is published (checked on 2026-11-24). The only way back is a deletion the owner authorizes and a new app. The package name comes back after the seven-day hold only when the app had zero installs ever. Otherwise it is lost, and the new app needs a new package name. Never choose Free as a default just to clear the dashboard.

Use the supported Money units/nanos, current region versions and exact update masks. One-time products have purchase-option regional pricing and availability, choices for future regions and their own activation. Subscriptions have base-plan prices, availability for new subscribers and future regions, and price moves for existing subscriber groups, which need separate authorization. A regional price does not make the app available in that region, and an active offer cannot override an inactive parent.

Keep existing scheduled and commercial choices, and tell customer price apart from tax and proceeds. Product changes happen outside edit transactions and can take effect on their own. [Commercial instructions](references/pricing-and-availability.md) give the real request shapes, paths, activation and subscriber-group decisions and checks. Do not use retired pricing templates or invent a single float price or app-country endpoint.

As a worked ASO example, a real local reading-notes app can stress organizing and finding notes without uploading them. It must not promise cloud sync or measured time savings that the product evidence does not show. Localize the value and the examples, not just the words. [Listing detail](references/listing-and-marketing.md) explains the editorial steps further.

## Media and device-specific truth

Capture the real UI with harmless data. Decorative artwork from an image model must not fake app features. Check proportions, readable text, safe crop, permission content, privacy and overlays at both full size and store size. Rebuild the layout for tablet, foldable, TV and XR instead of stretching phone content.

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

The same official page has general and specialized ranges for large screens. Use the range for the real target slot and say which one applies. Basic upload validity and featuring eligibility are different. To qualify for screenshot-based recommendations, an app or game must meet extra count, resolution and aspect-ratio conditions.

Upload images to the right locale and type inside the intended edit, using the supported media protocols and the real parameter enums. Keep the order and the existing source assets until the replacements are checked. A newer image type that only the console offers does not let you invent an API enum. [Media detail](references/screenshots-and-media.md) covers how the surfaces differ.

Before committing, inspect the real bytes, the returned image IDs and hashes, and the gallery order. The current image upload supports an honest `aiGeneratedState` attestation. It does not allow fake UI. The ordinary image methods have no reorder endpoint. Prepare a complete, checked replacement and run any needed delete and upload steps one at a time in the edit. Newer console areas such as Asset Library, experiments, events and form factors do not mean an unlisted Publisher API exists.

## Billing graph and customer access

Choose IDs that never change, the benefits, type, regions, price and tax model and restore behavior. For current one-time products, set up the real purchase options and offers. For subscriptions, tell apart the product, the base plan and the offer. Monthly or annual, auto-renewing or prepaid, and installment options have different schemas and lifecycle rules.

Read the existing state before you change it. Set exact regional prices, regionsVersion/update masks, eligibility and effective dates. Activate the plan, option or offer that should be buyable, and check what the client really sees. Catalog writes happen outside edit transactions. A failed listing commit does not undo a price change.

Use the current compatible Billing client or SDK, current product details and eligible offer tokens. Show the localized full price, interval, trial and discount phases, renewal, and cancel and restore terms. Verify purchases on the trusted backend, including package, product, token, state and line items. Do not trust a success flag from the client.

Grant only completed purchases. When the app processes purchases itself, save an idempotent delivery record (one that is safe to repeat) before you acknowledge or consume. The normal acknowledgment window is three days after completion. Check pending timing and current exceptions. Standard RevenueCat processing handles completion automatically. With custom delivery, compare your delivery records with the verified purchase records and webhooks, and never acknowledge a purchase a second time.

Set up authenticated RTDN/Pub/Sub delivery and match it against the purchase state from the source of truth. Handle duplicate and out-of-order events, renewal, pending completion, prepaid top-up, replacement and linked tokens, cancellation, grace, account hold, pause, expiry, refund and revocation. A cancellation can keep paid access until it expires. Consumables need a lasting balance and delivery policy. See [billing detail](references/products-and-subscriptions.md).

## First production app and console prerequisites

If the app is still a draft, an uploaded or committed production draft may need its first Console
confirmation. Follow [the complete first-production sequence](references/first-production-release.md)
from the real dashboard prerequisites through exact build confirmation, countries, Publishing overview
and the acknowledged submission. Reuse the uploaded AAB. Do not use internal testing in place of the
requested production review, and do not report a `completed` track status as public availability.

Inspect the saved declarations and the final merged manifest. Contains ads, Advertising ID use,
consent, target audience and IARC content ratings are separate answers. A child dialog's Add or Save
can be separate from saving its parent. Find the validation, focus or scroll problem before you
repeat failed clicks.

The Publisher API has no operation for app creation, most App content declarations, IARC rating,
target audience, category and tags, app pricing, production countries, Publishing overview
submission or app deletion. When the owner authorized browser use for this task, the agent does
these console-only steps itself in the owner's signed-in Chrome. Start Chrome normally with a
remote-debugging port and attach over the DevTools Protocol, because Google refuses sign-in in
browsers launched by automation. Otherwise each step becomes an exact owner handoff with the console
path, values and expected evidence. Send changes for review runs only within the authorized
endpoint. Remove changes, Unpublish, Delete app and reading the owner's Gmail or Google Payments
each need explicit authorization for that exact action. Without it, record the action as a BLOCKED
owner step. Follow [the Console browser procedure](references/play-console-browser.md)
for launching Chrome on macOS, Windows and Linux, talking to its tabs, every form, the Advertising
ID quick-check blocker, submission, and deleting an app with its transaction ID and seven-day
package-name hold.

## Edit, review and rollout sequence

1. Make package release changes one at a time, and create an edit, recording its ID and expiry.
2. Read the existing details, listings, images, tracks and artifacts, and keep the intended release graph.
3. Upload the signed AAB through the documented media path, check the returned code and attach the relevant mappings and symbols.
4. Apply the intended listing and media changes, and update only the chosen track with the real version codes, localized notes and an explicit status.
5. Validate the edit, fix errors and commit when it is within scope. Read the remote track and review state again.
6. Finish any open app content or review actions and the right managed-publishing step where eligible.
7. Check real release availability, installability, vitals, backend and billing behavior, and rollout impact.

Choose the commit's review-conflict behavior on purpose. Current `changesInReviewBehavior` defaults to `CANCEL_IN_REVIEW_AND_SUBMIT`, which can cancel a review in progress. Use `ERROR_IF_IN_REVIEW` when that review should stay as it is, and handle the returned conflict without quietly changing the intent. The rejection-specific `changesNotSentForReview` contract is separate from managed publishing and approval. Commit has an empty request body.

`draft`, `inProgress`, `halted` and `completed` have different effects. An in-progress rollout needs the intended supported fraction. Do not switch to completed to get around validation errors. `tracks.update` describes the release graph you want. It is not an excuse to throw away retained versions.

Set the in-app update priority within 0–5 before rollout. Country targeting is allowed only for eligible production in-progress releases and is not general app distribution. Respect the real form-factor track IDs, edit expiry and changes made at the same time in the console or API. After commit, check through a valid current read context. Do not treat the finished edit as still editable.

Managed publishing cannot hold back an app's first publication, and some changes take effect right away anyway. Internal sharing is separate from an internal test track. Personal accounts created after November 13, 2023 have the researched closed-test requirement of 12 testers for 14 days in a row before they can apply for production access. Do not fake engagement or suggest that an API upload skips eligibility.

Apply [the policy/readiness checklist](references/policy-and-review-checklist.md) to the real binary, backend and SDKs: content and audience, UGC and AI, privacy and deletion, permissions, billing and ads, rights, stable features and claimed device programs. Complete the real App content and reviewer tasks and keep access working. Keep app, update and item status separate. A live app can have a rejected pending update.

A committed edit is not review approval or public availability. Reproduce each rejection, fix the metadata, access, declaration or binary that caused it, test again and resubmit through the real supported API or console path. Metadata-only fixes can keep an eligible binary. Code changes need a newly reserved higher code. Customer `reviews.reply` is not a policy appeal API.

Halt eligible staged or fully rolled-out releases only within scope and real eligibility. Halting a full release does not apply to internal tracks or a track's first release, and it needs an eligible earlier version. It changes what is served from now on, not apps that are already installed. Prepare a forward fix with a higher code. Report the package, version and artifact, signing evidence, all fields, assets and prices, the edit, track, countries and fraction, policy and product state, the real checks and exact handoffs. [Release detail](references/edits-review-and-rollout.md) gives concrete steps.

The official [Publisher API](https://developers.google.com/android-publisher/api-ref/rest), [asset guidance](https://support.google.com/googleplay/android-developer/answer/9866151?hl=en), [Billing guidance](https://developer.android.com/google/play/billing/integrate) and [managed-publishing help](https://support.google.com/googleplay/android-developer/answer/9859654?hl=en) are the rules for their own areas. The [SRE release-engineering](https://sre.google/sre-book/release-engineering/) chapter and Dunford's [positioning book](https://www.aprildunford.com/books) give professional context, not store-approval guarantees. See [sources](references/sources.md) and [license](LICENSE.md).
