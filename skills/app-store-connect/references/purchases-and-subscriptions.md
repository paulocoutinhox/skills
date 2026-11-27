# Purchases and subscriptions

## Product design and intake

Make a catalog table with the product ID that cannot change, reference name, type, entitlement/consumption behavior, subscription group and level, period, display name and description per locale, territories, base territory, price points, tax category, Family Sharing choice, introductory/promotional/win-back offers, review notes, review screenshot, and where the app offers the feature.

Keep consumables, non-consumables, non-renewing subscriptions, and auto-renewable subscriptions apart. Consumable credit balances need a ledger that is safe to repeat. Non-consumables need restore. A non-renewing subscription is not a recurring auto-renewable plan. Use one subscription group for plans that replace each other for the same service. Set levels on purpose to control upgrade and downgrade behavior. Do not create unrelated groups just to show monthly versus annual billing.

Product identifiers are stable deployment identifiers. Map them exactly across app source, backend, store, and any entitlement service. Check whether an existing ID can be edited or reused before you plan a rename. Do not delete and recreate products to hide a setup mistake.

## Configuration order

1. Confirm the paid-app agreement, banking and tax eligibility, product permissions, app identity, and store availability.
2. For a normal IAP, create the parent with the current `/v2/inAppPurchases` contract. For subscriptions, create the group and parent subscription through their documented contracts. Look up the required attributes instead of using a payload from memory.
3. Use current draft-version resources: `inAppPurchaseVersions`, `subscriptionVersions`, and `subscriptionGroupVersions`. Check parent relationships and the latest or draft state before you create another version.
4. Add localized content and images to the correct current version. The new version-based API includes v2 localization and image resources for subscriptions and groups. Do not attach localized changes to deprecated older relationships.
5. Get the allowed territories and price points. Set the base territory, automatic or manual price schedules, start dates, regional availability, and currency behavior. A decimal price string is not always the price-point resource ID Apple needs.
6. Set up the intended offers and eligibility, including duration, payment mode, region, customer eligibility, redemption limits, and dates. Check price-consent rules before increases. Do not quietly remove older prices that existing customers keep.
7. Upload the required review screenshot with the documented reserve/upload/commit flow and give notes that show how reviewers reach the paid feature.
8. Read the parent and draft version resources back, and check all localizations, prices, territory availability, review state, and the link to the app.

## Review in the current version-based API

### Fields and exact metadata ownership

| Resource/model | Current inputs and decision |
| --- | --- |
| `/v2/inAppPurchases` create | Required `name` reference name, `productId` that cannot change, the real `inAppPurchaseType` and the `app` relationship. Optional `reviewNote` and `familySharable` are real review and sharing decisions. |
| IAP parent update | `name`, `reviewNote`, `familySharable`. Do not send product ID or type as editable just because they appeared in a create or response model. |
| `/v1/subscriptionGroups` | Create with `referenceName` and the app relationship. The parent update edits the supported reference name, not any localization or review state. |
| `/v1/subscriptions` create | Required reference `name`, `productId` that cannot change and `group`, with the chosen `subscriptionPeriod`, `groupLevel`, review note and Family Sharing. |
| Subscription parent update | Supported name, sharing, period, review and level, and eligible `multiSeatStatus` / `marketSettings` with their real models. Offer, price and retention relationships also have their own supported contracts. Check state and sharing or product decisions that cannot be undone first. |
| Version creation | `POST /v1/inAppPurchaseVersions`, `/v1/subscriptionVersions`, `/v1/subscriptionGroupVersions`, each linked to its real parent. These versions hold items for review. They are not renamed product IDs. |
| Current product localizations | `POST /v2/inAppPurchaseLocalizations` or `/v2/subscriptionLocalizations`, with required `locale`, `name`, optional description and the `version` relationship. PATCH the real v2 child for an editable draft. |
| Current group localization | `/v2/subscriptionGroupLocalizations`, required locale and name, optional `customAppName` and the group-version relationship. |
| Public product images | `/v2/inAppPurchaseImages` or `/v2/subscriptionImages` attach to a version. Use their real reserve and commit contract, not normal public screenshot placement fields. |
| Private review screenshots | `/v1/inAppPurchaseAppStoreReviewScreenshots` links to `inAppPurchaseV2`. `/v1/subscriptionAppStoreReviewScreenshots` links to the parent subscription. They do not become linked to a version just because public product images are. |

Read localizations and images through `/v1/inAppPurchaseVersions/{id}/localizations` or `/images` and the matching subscription and group-version relationships. Avoid deprecated direct-parent localization and image paths for new work. The version resources allow create and read, not a general PATCH to reset review state. Fix supported child metadata, or use the real review or support path for a state that is truly stuck.

The current IAP display name is 2–30 characters and the description at most 45. The reference name is an internal value with a different limit and purpose. Check each product type's current limits and locale rules, keep the benefit customers buy apart from an internal plan label, and never stuff unrelated search terms into paywall copy.

For promoted products, use the real promotional-image screen and the [official promotion specification](https://developer.apple.com/app-store/promoting-in-app-purchases/): a 1024×1024 PNG or high-quality JPEG that shows the benefit, separate from a screenshot or app icon, readable at small size and clear of framing and overlaid app-icon areas. Promotion eligibility and ranking depend on product type. Do not assume consumables appear in search or that every reviewed product is promoted automatically.

The researched official guide uses `/v1/reviewSubmissions` and `/v1/reviewSubmissionItems` with `subscriptionVersion`, `subscriptionGroupVersion`, and related current version relationships. Look up the real create schemas and supported item types. Mark the submission as submitted only after all items are ready. Old subscription and group submission endpoints are deprecated in this snapshot.

The current guide says the first subscription must be submitted together with an app binary through App Store Connect. Prepare all resources the API supports, then complete that first combined submission in the console. Later eligible changes use the documented version-review flow. For other first IAP combinations, follow the real current review guide and status. Never claim that approving a product on its own removes the required app review.

## App and backend integration

Use StoreKit 2 where the real deployment targets support it. Fetch localized products and prices from the store. Show the plan name, period, full recurring price, trial or introductory length, renewal terms, restore, privacy, and terms before purchase. Do not hardcode a price that can differ by territory or offer eligibility.

Handle purchase success, verified and unverified results, pending approval, cancellation, a dropped network, revoked purchases, restore, account switch, and expired, grace and billing-retry subscriptions. Process verified transaction updates while the app runs. When the app processes StoreKit directly, finish the transaction only after the benefit is delivered in a lasting way that is safe to repeat. A standard RevenueCat setup finishes transactions automatically. Check custom consumable delivery from its verified transaction records or webhooks. Do not assume the app can delay that automatic finish or finish again on its own.

For your own backend, use the official App Store Server Library/API and Server Notifications V2. These are separate from the Connect API contract researched for this guide. Fetch their current documentation and schemas. Check signed transaction and notification JWS against the official trust chain, the expected bundle, app and environment, and replay and repeat-safety rules. Keep production and sandbox environments apart. Check the server status instead of trusting an active flag sent by the client. Notifications can repeat or arrive out of order.

Model access by the real effective status and expiration. Cancellation stops future renewal and may leave access until expiration. A refund or revocation can remove access sooner. Billing retry and grace period are different. Upgrades, downgrades and linked replacement transactions need to be matched up. Never handle all events as one on/off switch.

## Test matrix

Test the local StoreKit configuration, sandbox store products, and TestFlight as separate environments. Local StoreKit success does not prove the store-side product setup. Test every plan and locale, duplicate consumable delivery, interrupted purchase, pending/Ask to Buy, restore on another device, login and logout, upgrade, downgrade, trial eligibility, renewal, cancellation, expiration, grace, billing retry, refund, revocation, and webhook replay and out-of-order handling.

Check platform SDK support across iOS/iPadOS, macOS, tvOS, and visionOS. The shared app record does not automatically give every target its purchase UI and backend integration. Record real sandbox transaction evidence without storing full receipts or customer identifiers in public files.
