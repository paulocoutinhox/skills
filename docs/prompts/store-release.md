# Store release and monetization prompts

App Store Connect, Google Play, RevenueCat and Playgama delivery. Read
[how to use the prompts](../task-prompts.md) before you copy one.

## Apple app delivery

```text
Use app-store-connect from paulocoutinhox/skills.
First read [SKILLS_ROOT]/app-store-connect/SKILL.md and the references for the chosen platforms and stage.
Briefly list the skill path you found. If it is missing, say so.

Deliver [APP] from [REPOSITORY] for [IOS_MACOS_TVOS_VISIONOS_SELECTION].
Allowed final stage (the brief's `authorized-endpoint`): [PREPARE_UPLOAD_BETA_SUBMIT_OR_RELEASE].
Account/app IDs, signing setup, current version/builds, and locales: [NON_SECRET_CONTEXT].
Audience, positioning, categories, monetization/products, and assets: [BRIEF].

List the current and requested fields by the API or console resource that owns them, platform,
locale and territory. Keep values nobody asked to change. Name the exact steps the owner or a
lawyer must do. Build and sign the real targets. Reserve a new build number for each new upload,
and allow for CI jobs that pick numbers at the same time.
Use name and subtitle text that fills most of the space with real meaning, keywords that add to it
and honest descriptions. Explain how each phrase fits the user's intent and the app's features.
Keep listing copy, captions and release notes about the app, with no notes on how they were made.
Prepare the real required screenshots and the current Asset Library uploads, placements and order,
URLs, privacy and reviewer access, and the product, version and offer links that apply.
Check download and product prices, base and manual schedules, sale countries and the policy for
current subscribers. Use the current review checklist. Submit only the eligible version and items,
and only up to the allowed final stage. Handle rejection, cancellation and resubmission with exact
build and resource evidence.
Fill in assets/release-evidence.md with what you read back, the real tests, blocked checks and
console actions. Report IDs and the real review, release and storefront states. Keep credentials out
of the output.
Look into export credential and cloud-signing permission problems apart from metadata API access.
Match up pending uploads before you retry. To replace a queued version, keep the whole app, product
and group review set, and check the replacement submission and the full media placement order.
```

## Google Play delivery

```text
Use google-play from paulocoutinhox/skills.
First read [SKILLS_ROOT]/google-play/SKILL.md and the references for the requested stage.
Briefly list the skill path you found. If it is missing, say so.

Deliver [APP] from [REPOSITORY] to [TRACK_AND_REQUESTED_RELEASE_STAGE].
Allowed final stage (the brief's `authorized-endpoint`): [PREPARE_INTERNAL_REVIEW_PRODUCTION_OR_ADMIN].
Play Console browser use in my signed-in Chrome: [AUTHORIZED_OR_HANDOFF_ONLY].
Account/package IDs, signing, current releases/version codes, and locales: [NON_SECRET_CONTEXT].
Audience, positioning, categories/tags, monetization/products, and assets: [BRIEF].

Before you change anything, list the current and requested fields, assets, products and review and
publishing state. Build and inspect the correctly signed bundle. Reserve a new version code under
CI number control.
Use the title and short-description space with real meaning, within the real limits. Give a reason
for each term, and write honest localized descriptions and images. Google has no normal App Store
style subtitle or keywords field. Keep notes on how the copy was made out of the listing, and record
AI statements in their declarations.
Check paid or free download choices, regional Money prices, option, plan and offer activation,
region versions, update masks, countries and the policy for current subscribers. Keep settings
nobody asked to change.
Use the policy and reviewer checklist and the supported Data safety CSV flow. Do console-only steps
in my signed-in browser only when browser use is allowed above. Otherwise give them to me as exact
owner steps. Removing changes, unpublishing, deleting the app and reading my Gmail or Google
Payments each need my clear permission for that exact action. Otherwise record them as BLOCKED owner
steps.
Choose on purpose how the commit handles review conflicts, and keep the current review unless you
mean to replace it. Handle metadata-only fixes and binary fixes differently, along with the real
resubmission and release controls.
Fill in assets/release-evidence.md with what you read back, the real tests, blockers and the
separate app, update and item states. Do only the allowed final stage and report the results without
showing credentials.
For a first draft app, follow references/first-production-release.md through the saved
prerequisites, the exact production draft confirmation, countries and the full Publishing overview
change set. Record the submission receipt, pending quick checks and real availability separately.
```

## RevenueCat

```text
Use revenuecat from paulocoutinhox/skills.
First read [SKILLS_ROOT]/revenuecat/SKILL.md and the matching store, SDK, and API references.
Briefly list the skill path you found. If it is missing, say so.

Prepare or configure [REQUESTED_SCOPE] for [APP_AND_PLATFORMS].
Current or missing account/project/platform apps, store records and product IDs: [NON_SECRET_CONTEXT].
Products, billing periods, access rights, paywall goals, and user identity model: [BRIEF].
Allowed environment and changes: [SANDBOX_OR_PRODUCTION_AND_SCOPE].

If the app is not in RevenueCat yet, follow references/first-app-setup.md: sign in, look at or
create the project and a separate app for each platform, get the public SDK keys, and connect the
allowed store credentials through their original protected paths. This is not the same as creating
store app records.
Map store products to entitlements, offerings, packages, and paywalls, and keep their roles apart.
Explain what the stores need first and where the supported sync stops. Use the supported APIs/CLI
for the allowed setup and the existing SDK and tools for the app code. Define what happens on
purchase, restore, account switch, cancellation, refund, expiration, pending payment, and offline
or error states, as they apply.
Cover backend checks, webhook authentication and safe repeats, and keeping secret and public keys
apart. Keep automatic store completion apart from your own consumable delivery, and stop duplicate
credits.
Keep one paywall editing session. Check localized previews and native prices and controls. Publish
the reviewed design only within the allowed scope. Paywall copy never tells how it was made. Check
the setup the SDK sees for each app.
Test sandbox behavior. Report the real state and evidence, cases not run, and the owner steps still
open. Do not claim that setup alone publishes store products or an app release.
For a partial setup, use the step-by-step layer check in references/testing-and-operations.md.
Record store notifications and app webhook status separately, with real native UI and transaction
evidence.
```

## Mobile release with subscriptions

```text
Use app-store-connect, google-play and revenuecat from paulocoutinhox/skills.
Read their real SKILL.md files and the matching references under [SKILLS_ROOT].
Use apple-app-testing/android-app-testing for the requested native checks, and haylen-app only when
[APP_REPOSITORY] really uses Haylen. Report a missing skill. Do not make up its tools.

Deliver [APP_REPOSITORY] to [PREPARE_UPLOAD_REVIEW_OR_PUBLIC_RELEASE] on [PLATFORMS].
App/store identities, account access and approved credential references: [NON_SECRET_CONTEXT].
Plans, entitlement, prices, countries, locales and reviewer access: [APPROVED_PRODUCT_SCOPE].

List the store and RevenueCat resources that already exist before you create missing ones. Reuse
the original approved credentials and put the public SDK keys in the right clients. Finish the
products, entitlement, packages and the reviewed localized paywall. Then check the setup the SDK
sees for each app.
Build the final native files with reserved whole-number build numbers. Inspect the real signatures,
versions and packaged settings. Test the real UI and the store-backed purchases that fit, and
clearly mark cases blocked by missing accounts or hardware. Capture real localized layouts and check
delivery.
For Apple, keep the full set of review items through any allowed replacement. For a first Google
release, finish the production draft and Console prerequisites before you send the whole set.
Keep each store's rules: Google Play console steps follow the google-play browser model (my
signed-in browser when allowed, otherwise exact owner steps). App Store Connect steps use only its
supported API/CLI and exact owner steps, never a logged-in browser session.
Report final build hashes, the real remote states, pending checks and the remaining gates
separately.
Keep private credentials and temporary tools out of the app source. Approval to publish covers its
normal prerequisites. It does not allow unrelated commercial or account changes.
```

## Playgama

```text
Use playgama from paulocoutinhox/skills.
Read [SKILLS_ROOT]/playgama/SKILL.md and the matching review, Bridge, tool, media and publication references.
Briefly list the skill path you found. If it is missing, say so.

Prepare [GAME] from [REPOSITORY_OR_EXPORT] for [REQUESTED_PLATFORM_STAGE].
Engine/export details, target devices, languages, and account/game IDs: [NON_SECRET_CONTEXT].
Gameplay promise, audience, monetization, saves, achievements, and assets: [BRIEF].

Review every numbered technical, ads/payments, UX, content and engine requirement that applies,
plus the real destination limits and where the game can be distributed.
Check host detection, startup and error states, restored Bridge saves and the exact game-ready
timing. Check that the game does not start an ad on opening, that ads run at natural breaks or when
the SDK schedules them, that rewarded ads are opt-in and that each reward is given once.
Check mute in the menu and pause, the host's starting mute, focus, ad and pause states that overlap,
and the saved setting.
Test full progress, clear limits on actions and resources, repeated consumable purchases, permanent
ownership and purchase recovery. Include desktop and mobile layouts, inputs, translations and
rights.
Prepare honest localized metadata, covers, screenshots, links, and required artwork. Player-facing
text and art never tell how they were made.
Use the supported API/CLI/MCP tools when you have them. Explain the exact steps they cannot do or
that a person must do by hand.
Fill in assets/review-report.md with the exact archive and hash, requirement IDs, real test
evidence, FAILED defects, BLOCKED checks that were not run and NOT APPLICABLE items with a reason.
For fixes, reproduce each finding and test the related flows again against the new archive.
Do only the requested and allowed upload, sandbox, moderation, or publication stage, and check its
real state. Report files, evidence, IDs, open decisions, and tool limits.
```
