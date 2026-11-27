# Products, base plans, offers, and fulfillment

## Catalog design

Collect the package, product IDs that never change, product type, localized name and description, entitlement or consumable benefit, supported countries, tax and compliance, regional prices, offer eligibility, subscription length, base-plan type, grace and account-hold rules, and replacement behavior. Keep a lasting map between Play IDs, app code, backend and any purchase platform.

Use the `monetization.onetimeproducts` model for one-time products. It includes purchase options, offers and regional configuration.

For subscriptions, keep the subscription product, base plan and optional offer separate. Monthly and annual can be base plans under the right product model. Auto-renewing and prepaid plans have different fields and lifecycle behavior. Offer tags are metadata for choosing a billing offer, not store-listing keywords. Do not apply a plan automatically just because its price is the lowest.

## Configuration sequence

1. Read the existing products, base plans and offers, and the country and region requirements.
2. Get or calculate regional prices with the supported money models and region-version rules. Use currency units/nanos or the real endpoint contract, never a binary float for stored prices.
3. Create or patch the product with exact update masks and the required `regionsVersion` when the docs ask for it. Required regional compliance fields must come from the owner and the implementation.
4. Create purchase options or base plans, then eligible offers. Set renew or prepaid behavior, length, billing period, trial phases, grace and account hold, installment details where supported, country targeting and regional price behavior on purpose.
5. Activate the right base plan, purchase option and offer through the supported lifecycle operations. Creating a product does not make it buyable by itself.
6. Read the whole graph again and check product, basePlan and offer IDs, state, locales, prices, countries and what the client really sees. Product changes happen outside edit transactions.

For price migrations, read existing subscribers, regional rules, consent rules, effective dates and opt-in or opt-out behavior. Explain the expected effect on customers before running an authorized migration. Deactivate only the sales surface you mean to. Subscription archiving is deprecated and not supported in the current contract. Do not assume deactivation cancels existing subscriptions. [Pricing and availability](pricing-and-availability.md) explains exact money, region-version, schedule and subscriber-group rules and console limits.

## Complete current catalog field ownership

| Model | Inputs and state rules |
| --- | --- |
| `OneTimeProduct` | `packageName`/`productId` that never change, required localized `listings` and `purchaseOptions`, optional `offerTags`, `restrictedPaymentCountries` and `taxAndComplianceSettings`. `regionsVersion` on the returned product is output-only. |
| `OneTimeProductListing` | `languageCode`, `title` up to 55 characters and `description` up to 200. No duplicate locale entries. Use the real default and supported translations. |
| `OneTimeProductPurchaseOption` | A `purchaseOptionId` that never changes, `buyOption` or `rentOption`, `regionalPricingAndAvailabilityConfigs`, optional `newRegionsConfig`, tags and tax and compliance. The returned `state` changes only through the dedicated state action. |
| Buy/rent details | Buy can support multi-quantity. Rent sets an ISO 8601 `rentalPeriod` and an optional `expirationPeriod`. New work does not turn on support for deprecated clients just because that field exists. |
| One-time regional entry | `regionCode`, `price` and current `availability` such as `AVAILABLE`, `NO_LONGER_AVAILABLE`, `AVAILABLE_IF_RELEASED` or `AVAILABLE_FOR_OFFERS_ONLY`. Choose the exact intended state, not a generic boolean. |
| `OneTimeProductOffer` | Package, product, option and offer IDs that never change, regional pricing and availability, tags and one supported preorder, discounted or game-reward setup. State and the returned regions version are output-only. |
| `Subscription` | Package and product IDs that never change, required localized `listings`, intended `basePlans`, optional restricted payment countries and tax and compliance. Do not write the deprecated `archived` output field. |
| `SubscriptionListing` | `languageCode`, `title`, description up to 200 characters and at most four ordered benefit strings. At least the app's default language is required. |
| `BasePlan` | A `basePlanId` that never changes, exactly one real supported type (auto-renewing, prepaid or installment), regional configs, future-region settings and tags. Use the dedicated activation and deactivation actions for its output state. |
| `SubscriptionOffer` | IDs that never change, required `regionalConfigs`, one or two ordered `phases`, optional targeting, tags and future-region configs. An active offer alone does not override an inactive base plan. |
| Subscription phase | ISO 8601 `duration`, `recurrenceCount`, per-region price, free or relative-price setup from the exact phase model, and future-region policy. Each phase must cover the offer's intended regions the same way. |

Field names and nested payloads differ between one-time and subscription pricing. Do not copy a `regionalConfigs` object into `regionalPricingAndAvailabilityConfigs`, or use one type's activation endpoint for another. Repeated fields mean you rebuild the intended list instead of assuming each element is merged.

### Base-plan decisions

- Auto-renewing: a `billingPeriodDuration` that never changes, and the real `gracePeriodDuration`, `accountHoldDuration`, `resubscribeState` and `prorationMode`. Current limits allow grace up to 30 days or the billing period, whichever is shorter, account hold up to 60 days, and grace plus hold together from 30 to 60 days. Confirm the real allowed ISO duration and chosen period before saving.
- Prepaid: a `billingPeriodDuration` that never changes and a supported `timeExtension`. A prepaid entitlement does not renew automatically just because the UI calls it a subscription.
- Installments: a period, committed payment count and renewal type that never change, plus supported grace, account hold, resubscribe and proration settings. Disclose the real commitment and what happens after it ends.
- Future regions and changes for existing customers are explicit commercial choices. Do not turn on global availability or move an old subscriber group while you edit a title.

### State actions and offers

You create current one-time products through the supported upsert, not a made-up `onetimeproducts.insert`. Set up purchase options in the parent, and activate or deactivate them through `purchaseOptions.batchUpdateStates` with one matching request branch per option. One-time offers use the supported `batchUpdate` to create and update, and the real activate, deactivate or cancel action. Their batch contracts can use the documented `-` parent selector across products, but never use that selector with methods that do not support it.

Subscriptions support real create and patch. You set up base plans in the subscription graph and activate them through their own actions. Subscription offers have their own create, patch and state endpoints. Read each batch's limit, update mask, where the regions version goes, how errors work and the per-item results. A successful request wrapper is no reason to ignore an item that failed.

Offers need honest eligibility and terms: acquisition, upgrade or developer targeting, trial or discounted periods, the normal renewal price, redemption limit, start, end and release dates and real region support. Multi-quantity, rentals, prepaid top-ups and installments need the app and backend to handle their real entitlement rules before you turn on sales.

## Billing client and backend

Use a Play Billing Library version that is currently allowed, through the app's chosen native or cross-platform SDK. Query product details and the current eligible offer tokens. Show the localized full price, billing interval, trial and discount phases, renewal price, access after cancellation and any important restrictions. Start the purchase from the right foreground activity, and handle the service connection and lifecycle on purpose.

The secure backend checks the package, product, purchase token, purchase state, quantity and subscription line items through the current purchase endpoints. Use `purchases.subscriptionsv2.get` for the current subscription model, and the right product purchase endpoint for one-time products. Never trust a client success screen or a local boolean alone.

Grant benefits only after `PURCHASED`, not `PENDING`. When the app processes purchases itself, save an idempotent (safe to repeat) transaction and fulfillment record before you acknowledge or consume. Normally acknowledge eligible purchases within three days of purchase completion, or they are refunded automatically. For pending purchases, the time starts when the purchase completes. Confirm current exceptions and which SDK owns this before you build it. Consumables use the consume flow, and non-consumables and subscriptions use acknowledgment as required. A standard RevenueCat integration handles acknowledgment and consumption automatically. Match custom consumable delivery against its checked records and webhooks. Do not assume an unconsumed store item stays available, and never acknowledge a second time on your own.

Send and store purchase tokens only through protected channels and storage. They identify purchases but do not replace authorization of the app user. Link purchases to signed-in accounts through a deliberate policy that resists fraud, and use store-supported obfuscated account IDs when they apply. Never attach one customer's transaction to another because the client sent some user ID.

## Notifications and lifecycle

Set up Real-time Developer Notifications through Google Cloud Pub/Sub with the intended topic permissions and authenticated delivery. Check the push identity and audience, or use protected pull subscribers. Treat a notification as a signal to query the current purchase state from the source of truth. Remove duplicates, handle delayed or out-of-order delivery, and keep matching jobs running.

Test pending completion and cancellation, prepaid top-up, renewals, upgrade, downgrade and replacement modes, linked purchase tokens, cancellation, expiry, grace, account hold, pause and resume where available, refund, revocation, chargebacks and voided purchases, restore, reinstall and account switch. A cancellation can leave access until the end of the paid period. Refund and revoke are different money and entitlement operations. Keep access until the checked entitlement policy says otherwise.

Use test-track builds, licensed testers, products set up in the store and approved test payment methods. A local mocked billing response does not prove the Play catalog is ready. Record sandbox and test results without leaking raw purchase tokens or real payment data. Confirm that production products stay active in the intended countries and that the release version uses the same IDs.
