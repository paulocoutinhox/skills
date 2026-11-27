# Ads, purchases, storage, and leaderboards

## Advertising

Integrate through Bridge's supported advertisement module and the current engine binding. Interstitial integration is required where supported. Offer ad opportunities at real breaks such as finished levels, game over or a suitable return to the menu after play. Pressing Start for the first time is not, by itself, a natural break. No show request from the game belongs in initialization or loading, readiness, the first entry to the menu or the return of focus.

Bridge controls when ads really show and how often. Its currently documented configurable minimum defaults to 60 seconds. Do not turn this default into a universal deadline for the first ad, or add competing timers or every-N-rounds counters. Request once per real opportunity and let the SDK skip when the time is wrong. Check real support before adding interstitial logic, and never force an ad into active play to reach a count.

Check direct show calls, event handlers, custom platform messages and the `advertisement.interstitial.autoShow` setting. A custom message can trigger an ad even when no direct call appears in the game code. SDK preloading is not the same as showing. Opening ads that the partner manages are different from a request the game makes, but they also need correct pause and audio handling. Read the binding's real config instead of guessing fields it does not support.

Stop overlapping requests, double clicks and late callbacks from showing an ad after play has resumed. Keep the transition under one owner until the documented completion or error path finishes. Do not invent a cancel API or queue a delayed ad that fires during combat. Closing an ad clears its own pause reason. It cannot unmute a player's choice or resume a scene that is paused for another reason.

Test first launch without any input, the first Start, the first finished loop, later natural breaks, no-fill, error, closing and focus changes during an ad. Record the request time, the real display and the gameplay phase separately. A faked successful response does not prove how the host behaves.

## Rewarded advertising and banners

On the opt-in control, state the exact benefit and that the player must watch an ad, for example “Watch an ad for 50 coins”. Give a way to decline and keep normal play without the bonus. A revive, extra-life, continue or extra-time offer appears at most once per attempt. Track which attempt it is, so reopening a dialog or changing scenes cannot reset the limit.

Grant only on the documented `rewarded` state, once for that request and for the promised placement and amount. Closing alone is not completion. Repeated or late callbacks cannot grant twice or reward a different run. Cancel, failure or no-fill grants nothing and leaves a way to continue. Pause gameplay and audio during fullscreen ads and keep progress.

Use the explicit capability checks to hide rewarded and payment UI that is not supported. Banners must not cover gameplay, controls, dialogs, or purchase details. Use the current platform-specific requirements and real ad events, not faked success callbacks. Do not add external ad SDKs or external checkout against the platform rules.

Sticky and advanced banners use only placements that Bridge supports. Work out the usable layout again after showing or hiding a banner or rotating the device. Check the real tap areas, not only the canvas's stated size.

## Catalog configuration

Read `list_in_app_products` first. Keep its exact checksum and all existing products. Build the complete list you want and pass `expectedChecksum` to `replace_in_app_products`. A product left out of that list is removed. An empty list clears the catalog. The provider requires asking before removing products. A 409 outdated checksum means you must read again and reapply the change you meant, not overwrite another editor's work.

Each current product uses `productId`, `title`, optional `description`, `type: consumable|non_consumable`, and `priceUsd`, which is not negative and has at most two decimal places. Keep IDs unique and stable and mapped to the same Bridge config product IDs. `hasInGamePurchases` follows the documented catalog and flag rules. Do not turn on purchases with an empty catalog, or read a zero price as a general pricing suggestion.

The catalog and SDK checked offer one-time consumable and permanent products. They do not document a recurring, auto-renewing subscription type. Do not fake subscriptions with repeated charges, claim APIs that do not exist, or sell banned real-world or external benefits. If the user asks for subscriptions, report that missing feature and check current official support again before you suggest a different authorized product model.

## Purchase flow and verification

Fill the `payments` product ID entries in `playgama-bridge-config.json` and set up matching products in the real target platform dashboards. Store-specific ID overrides follow the current config contract. Check `bridge.payments.isSupported` or the engine equivalent before showing purchase controls. Payment support differs between distribution destinations.

Call the supported purchase function from a direct player action. For plain JavaScript, the methods checked include `bridge.payments.purchase(productId)`, `getPurchases()`, and `consumePurchase(productId)`. In the current JS examples, the consume argument is the configured product ID, not an invented order token. Read the exact engine and platform contract before you build it.

Verify valuable purchases on a trusted backend before granting benefits. The documented verification endpoint checked is `POST https://playgama.com/api/bridge/v1/verify` with JSON `platform`, `type: purchase`, and `data` holding the returned purchase object. Current supported verification destinations are `playgama`, `msn`, and `microsoft_store`. Read the current response fields and match a successful product, order and user link where it applies. Other destinations need their own documented platform verification. Do not claim this endpoint verifies every Bridge platform, or use a success flag from the client alone as proof.

Save delivery idempotently, which means doing it again has no extra effect, using the stable purchase identity that the platform really provides. Grant the benefit in a lasting way, then consume a consumable through the documented method. On launch, look for unconsumed purchases and finish interrupted delivery without granting twice. Do not consume permanent products. Check permanent ownership again on launch or restore with the supported purchase list.

Show the current platform product price and availability and accurate item benefits. Handle cancel, pending and error states, unavailable payments, duplicate callbacks, failed consumption, reload, and account changes. If consuming fails after the benefit was saved, retry or finish the consume. Do not grant the benefit again. Store purchase fields differ by platform.

## Functional shops and repeated transactions

Keep three models apart: an exchange using in-game currency, a platform consumable purchase and permanent platform ownership. Test each one against its real contract. A normal repeatable consumable must be possible to buy again when allowed. Permanent ownership must restore and block a second purchase. Explicit stock, daily or resource limits need a visible reason and a valid way to recover.

For each supported item, check the price, available currency, required unlocks, shown benefit and the real inventory you end up with. Start a single transaction from an enabled control, stop duplicate delivery while one is in progress, and refresh balance, stock and eligibility after it finishes. Clear the temporary in-progress state on every final success, cancel and error path. A button that works once and then stays disabled forever is a bug, unless the product is meant to be permanent or is sold out.

Run two allowed purchases, fast repeated taps, not enough funds, leaving and re-entering the shop, a scene change, a reload and a failure followed by a retry. Watch the real deduction and benefit, not just a success message. Failed purchases cannot take currency or grant an item. Keep in-game currency updates consistent within the real storage or backend guarantees. Do not claim that Bridge Storage offers a transaction across any keys or devices.

Action-point or energy gates need the same clarity: show the remaining amount, the cost, the unmet condition and how the player can go on. Hidden rules do not excuse combat, shop or progress controls that seem dead. Review every visible area with the flow of a first-time player.

## Player services

Use Bridge Storage as required for progress, settings, ownership-related state, and crash recovery. Local state the player controls is not enough proof for valuable server-side entitlements or protected leaderboard scores. Sign-in must follow the capability and UX rules without forcing a launch flow that is unsupported or blocks play.

Set up leaderboards through the list, create and update tools. Tags are fixed, unique per game, and must match SDK identifiers. Choose numeric or time scoring and ascending or descending order on purpose. Scores are stored as whole numbers in the current contract, so showing decimals does not create storage for any fraction. Check the existing score-protection settings. Deleting leaderboards or scores is a destructive action available only in the console here.

Test every monetization and player service you claim on the real distribution destinations. Keep a support table for ads, payments, verification, storage, sign-in, and leaderboards. A green result on one portal does not prove that all partner platforms support the same feature.
