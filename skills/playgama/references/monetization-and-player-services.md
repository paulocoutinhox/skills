# Ads, purchases, storage, and leaderboards

## Advertising

Integrate through Bridge's supported advertisement module and current engine binding. Interstitial integration is required where supported. Offer opportunities at real breaks such as completed levels, game over or an appropriate return to menu after play. A first Start press does not by itself establish a natural break. No game-owned show request belongs in initialization/loading, readiness, initial menu entry or focus restoration.

Bridge controls actual display timing and caps. Its currently documented configurable minimum defaults to 60 seconds. Do not turn this default into a universal first-ad deadline or add competing timers/every-N-rounds counters. Request once per real opportunity and let the SDK skip when inappropriate. Check actual support before interstitial logic, and never force an ad into active play to meet a count.

Review explicit show calls, event handlers, custom platform messages and `advertisement.interstitial.autoShow` configuration. A custom message can trigger an ad even when no direct call appears in the game code. SDK preloading is not display. Partner-managed initial advertising is distinct from a game-owned request, but requires correct pause/audio handling too. Read the actual binding's config instead of guessing unsupported fields.

Prevent overlapping requests, double clicks and stale callbacks from showing an ad after play has resumed. Keep the relevant transition under one owner until the documented completion/error path resolves. Do not invent a cancellation API or queue a deferred ad to fire during combat. An ad close clears its own pause reason and cannot unmute a player preference or resume an independently paused scene.

Test first launch without interaction, initial Start, first completed loop, later natural breaks, no-fill, error, closure and focus changes during an ad. Record request time, actual display and gameplay phase separately. A mocked successful response is not proof of host behavior.

## Rewarded advertising and banners

Disclose the exact benefit and that watching an ad is required on the opt-in control, for example “Watch an ad for 50 coins”. Provide a decline path and ordinary play without the bonus. A revive/extra-life/continue/time recovery offer appears at most once per attempt. Track the attempt identity so re-opening a dialog or changing scenes cannot reset the limit.

Grant only on the documented `rewarded` state, once for the actual request and promised placement/amount. Closing alone is not completion. Repeated or stale callbacks cannot grant twice or credit a different run. Cancellation/failure/no-fill grants nothing and leaves an actionable continuation. Pause gameplay/audio during fullscreen advertising and preserve progress.

Use explicit capability checks to hide unsupported rewarded/payment UI. Banners must not cover gameplay, controls, dialogs, or purchase disclosures. Use current platform-specific requirements and real ad events rather than simulated success callbacks. Do not add external ad SDKs or external checkout contrary to platform rules.

Sticky and advanced banners use Bridge-supported placements only. Recompute usable layout after showing/hiding a banner or rotating the device. Inspect actual hit areas, not only the canvas's nominal dimensions.

## Catalog configuration

Read `list_in_app_products` first. Preserve its exact checksum and all existing products. Construct the complete desired array and pass `expectedChecksum` to `replace_in_app_products`. A product omitted from that array is removed. An empty array clears the catalog. The provider requires asking before product removals. A 409 stale checksum requires a fresh read and reapplication of the intended change, not overwriting another editor's work.

Each current product uses `productId`, `title`, optional `description`, `type: consumable|non_consumable`, and `priceUsd` with at most two decimal places and a nonnegative value. Keep IDs unique/stable and mapped to the same Bridge config product IDs. `hasInGamePurchases` follows the documented catalog/flag rules. Do not enable purchases with an empty catalog or mistake a zero price for a general monetization recommendation.

The researched catalog/SDK exposes one-time consumable and permanent products. It does not document a recurring auto-renewing subscription type. Do not emulate subscriptions through repeated charges, claim unsupported APIs, or sell prohibited real-world/external benefits. If the user requests subscriptions, report that capability gap and recheck current official support before proposing a different authorized product model.

## Purchase flow and verification

Populate the `payments` product ID entries in `playgama-bridge-config.json` and describe matching products in the actual target platform dashboards. Store-specific ID overrides use the current config contract. Check `bridge.payments.isSupported` or the engine equivalent before showing purchase controls. Platform payment support differs across distribution destinations.

Call the supported purchase function from a direct player action. For plain JavaScript, the researched methods include `bridge.payments.purchase(productId)`, `getPurchases()`, and `consumePurchase(productId)`. The consume argument in the current JS examples is the configured product ID, not an invented order token. Read the exact engine/platform contract before implementation.

Verify valuable purchases on a trusted backend before granting benefits. The researched documented verification endpoint is `POST https://playgama.com/api/bridge/v1/verify` with JSON `platform`, `type: purchase`, and `data` containing the returned purchase object. Current supported verification destinations are `playgama`, `msn`, and `microsoft_store`. Read current response fields and match successful product/order/user binding as applicable. Other destinations require their documented platform verification. Do not claim this endpoint verifies every Bridge platform or use a client-only success flag as proof.

Persist idempotent delivery using the actual stable purchase identity available on that platform. Grant the benefit durably, then consume a consumable through the documented method. On launch, inspect unconsumed purchases and reconcile interrupted delivery without awarding twice. Do not consume permanent products. Recheck permanent ownership on launch/restore using supported purchase listing.

Show current platform product price/availability and accurate item benefits. Handle cancellation, pending/error states, unavailable payments, duplicate callbacks, failed consumption, reload, and account changes. A failed consume after durable fulfillment must be retried/reconciled, not granted again. Store purchase fields vary by platform.

## Functional shops and repeated transactions

Separate three models: an internal-currency exchange, a platform consumable purchase and permanent platform ownership. Test each by its actual contract. An ordinary repeatable consumable must be purchasable again when eligible. Permanent ownership must restore and prevent repurchase. Explicit stock, daily or resource limits need a visible reason and a valid recovery path.

For each supported item, verify price, available currency, required unlocks, displayed benefit and actual resulting inventory. Start a single transaction from an enabled control, prevent duplicate in-flight delivery, and refresh balance/stock/eligibility after completion. Release the temporary in-flight state on every terminal success, cancel and error path. A button that works once and remains disabled forever is a functional defect unless the product is intentionally permanent or exhausted.

Run two eligible purchases, rapid repeated input, insufficient funds, leave/re-enter shop, scene change, reload and failure followed by retry. Observe the real deduction and benefit, not just a success toast. Failed purchases cannot deduct currency or grant an item. Keep internal-currency updates consistent under the actual storage/backend guarantees. Do not claim Bridge Storage provides a transaction spanning arbitrary keys or devices.

Action-point/energy gates need the same clarity: show remaining capacity, cost, unmet condition and how the player continues. Hidden rules do not excuse apparently dead combat, shop or progression controls. Review all visible areas with a first-time player flow.

## Player services

Use Bridge Storage as required for progress, settings, ownership-related state, and crash recovery. Player-controlled local state is not sufficient proof for valuable server-side entitlements or protected leaderboard scores. Sign-in must follow capability and UX rules without forcing an unsupported/blocking launch flow.

Configure leaderboards through list/create/update tools. Tags are immutable, unique per game, and must match SDK identifiers. Choose numeric/time and ascending/descending semantics deliberately. Scores are stored as whole numbers in the current contract, so display decimals do not create arbitrary fractional score storage. Inspect existing score-protection settings. Deleting leaderboards/scores is a console-only destructive action in this surface.

Test all claimed monetization/player services on the actual distribution destinations. Keep a support matrix for ads, payments, verification, storage, auth, and leaderboards. A green result on one portal does not prove all partner platforms support the same feature.
