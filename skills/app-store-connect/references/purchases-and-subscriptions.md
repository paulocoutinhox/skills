# Purchases and subscriptions

## Product design and intake

Create a catalog table containing immutable product ID, reference name, type, entitlement/consumption behavior, subscription group and level, period, display name/description per locale, territories, base territory, price points, tax category, family sharing choice, introductory/promotional/win-back offers, review notes, review screenshot, and app feature entry point.

Distinguish consumables, non-consumables, non-renewing subscriptions, and auto-renewable subscriptions. Consumable credit balances require an idempotent ledger. Non-consumables need restoration. A non-renewing subscription is not a recurring auto-renewable plan. Select one subscription group for mutually exclusive alternatives to the same service. Set levels deliberately to control upgrade/downgrade behavior. Do not create unrelated groups simply to represent monthly versus annual billing.

Product identifiers are stable deployment identifiers. Map them exactly across app source, backend, store, and any entitlement service. Verify whether an existing ID is editable or reusable before planning a rename. Do not delete/recreate products to hide a configuration error.

## Configuration order

1. Confirm paid-app agreement, banking/tax eligibility, product permissions, app identity, and storefront availability.
2. For an ordinary IAP, create the parent via the current `/v2/inAppPurchases` contract. For subscriptions, create the group and parent subscription through their documented contracts. Query required attributes rather than using a memorized payload.
3. Use current draft-version resources: `inAppPurchaseVersions`, `subscriptionVersions`, and `subscriptionGroupVersions`. Inspect parent relationships and latest/draft state before creating another version.
4. Add localized content and images to the correct current version. The new version-based API includes v2 localization/image resources for subscriptions and groups. Do not attach new localized changes to deprecated pre-version relationships without checking the current contract.
5. Retrieve allowed territories and price points. Configure base territory, automatic/manual price schedules, start dates, regional availability, and currency behavior. A decimal price string is not necessarily the price-point resource ID required by Apple.
6. Configure intended offers and eligibility, including duration, payment mode, region, customer eligibility, redemption limits, and dates. Verify price-consent rules before increases. Do not silently remove grandfathered customer pricing.
7. Upload the required review screenshot with the documented reservation/upload/commit flow and provide notes showing how reviewers access the paid feature.
8. Read parent and draft version resources back, verify all localizations, prices, territory availability, review state, and app association.

## Review in the current version-based API

### Fields and exact metadata ownership

| Resource/model | Current inputs and decision |
| --- | --- |
| `/v2/inAppPurchases` create | Required `name` reference name, immutable `productId`, actual `inAppPurchaseType` and `app` relationship. Optional `reviewNote` and `familySharable` are real review/sharing decisions. |
| IAP parent update | `name`, `reviewNote`, `familySharable`. Do not send product ID/type as editable because they appeared in a create/response model. |
| `/v1/subscriptionGroups` | Create with `referenceName` and app relationship. Parent update edits supported reference name, not arbitrary localization or review state. |
| `/v1/subscriptions` create | Required reference `name`, immutable `productId` and `group`, with selected `subscriptionPeriod`, `groupLevel`, review note and Family Sharing. |
| Subscription parent update | Supported name/sharing/period/review/level and eligible `multiSeatStatus` / `marketSettings` with their actual models. Offer/price/retention relationships also have specific supported contracts. Check state and irreversible sharing/product decisions first. |
| Version creation | `POST /v1/inAppPurchaseVersions`, `/v1/subscriptionVersions`, `/v1/subscriptionGroupVersions`, each related to its actual parent. These versions are review containers, not renamed immutable product IDs. |
| Current product localizations | `POST /v2/inAppPurchaseLocalizations` or `/v2/subscriptionLocalizations`, with required `locale`, `name`, optional description and the `version` relationship. PATCH the actual v2 child for an editable draft. |
| Current group localization | `/v2/subscriptionGroupLocalizations`, required locale/name, optional `customAppName` and group-version relationship. |
| Public product images | `/v2/inAppPurchaseImages` or `/v2/subscriptionImages` attach to a version. Use their actual reservation/commit contract, not ordinary public screenshot placement fields. |
| Private review screenshots | `/v1/inAppPurchaseAppStoreReviewScreenshots` relates to `inAppPurchaseV2`; `/v1/subscriptionAppStoreReviewScreenshots` relates to the parent subscription. They do not become version-linked merely because public product images did. |

Read localizations/images through `/v1/inAppPurchaseVersions/{id}/localizations` or `/images` and corresponding subscription/group-version relationships. Avoid deprecated direct-parent localization/image paths for new work. The version resources expose creation/read, not a generic PATCH to reset review state. Correct supported child metadata or use the actual review/support path for a genuinely stuck state.

The current IAP display name is 2–30 characters and description at most 45. Reference name is an internal value with a different limit/purpose. Validate each product type's current limits and locale requirements, distinguish the sale-facing benefit from an internal plan label and never stuff unrelated search terms into paywall copy.

For promoted products, use the actual promotional-image surface and the [official promotion specification](https://developer.apple.com/app-store/promoting-in-app-purchases/): a 1024×1024 PNG/high-quality JPEG representing the benefit, separate from a screenshot or app icon, readable small and clear of framing/overlaid app-icon areas. Promotion eligibility and ranking differ by product type. Do not assume consumables appear in search or that every reviewed product is automatically promoted.

The researched official guide uses `/v1/reviewSubmissions` and `/v1/reviewSubmissionItems` with `subscriptionVersion`, `subscriptionGroupVersion`, and related current version relationships. Resolve the actual create schemas and supported item types. Mark the submission submitted only after all items are ready. Old subscription/group submission endpoints are deprecated in this snapshot.

The first subscription submission requires submission with an app binary through App Store Connect according to the current guide. Prepare all API-supported resources, then complete that initial combined submission in the console. Subsequent eligible changes use the documented version-review flow. For other first IAP combinations, follow the actual current review guide and status. Never claim independent product approval eliminates required app review.

## App and backend integration

Use StoreKit 2 where supported by the actual deployment targets. Fetch localized products and prices from the store. Display plan name, period, full recurring price, trial/introductory duration, renewal terms, restoration, privacy, and terms before purchase. Do not hardcode a price that can diverge by territory or offer eligibility.

Handle purchase success, verified/unverified results, pending approval, cancellation, interrupted network, revoked purchases, restore, account switch, and expired/grace/billing-retry subscriptions. Process verified transaction updates while the app runs. With direct application-owned StoreKit processing, finish only after durable idempotent benefit delivery. Standard RevenueCat integration owns automatic transaction completion. Reconcile custom consumable delivery from its verified transaction records/webhooks rather than assuming the app can postpone that automatic completion or finish again independently.

For a direct backend, use the official App Store Server Library/API and Server Notifications V2. These are separate from the Connect API contract researched for this guide. Fetch their current documentation and schemas. Validate signed transaction and notification JWS with the official trust chain, expected bundle/app/environment, and replay/idempotency rules. Keep production and sandbox environments distinct. Reconcile server status instead of trusting a client-supplied active flag. Notifications can repeat or arrive out of order.

Model access by actual effective status and expiration. Cancellation stops future renewal and may leave access until expiration. Refund/revocation can remove access earlier. Billing retry and grace period differ. Upgrades/downgrades and linked replacement transactions require reconciliation. Never implement all events as a single boolean toggle.

## Test matrix

Exercise local StoreKit configuration, sandbox store products, and TestFlight as distinct environments. Local StoreKit success does not prove store-side product setup. Test every plan and locale, consumable duplicate delivery, interrupted purchase, pending/Ask to Buy, restore on another device, login/logout, upgrade, downgrade, trial eligibility, renewal, cancellation, expiration, grace, billing retry, refund, revocation, and webhook replay/out-of-order handling.

Check platform SDK support across iOS/iPadOS, macOS, tvOS, and visionOS. The shared app record does not automatically provide every target's purchase UI and backend integration. Record actual sandbox transaction evidence without storing full receipts or customer identifiers in public artifacts.
