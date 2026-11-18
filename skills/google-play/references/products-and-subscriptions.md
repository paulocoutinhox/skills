# Products, base plans, offers, and fulfillment

## Catalog design

Collect package, immutable product IDs, product type, localized name/description, entitlement or consumable benefit, supported countries, tax/compliance, regional prices, offer eligibility, subscription duration, base-plan type, grace/account-hold rules, and replacement behavior. Use a durable mapping between Play IDs, app code, backend, and any purchase platform.

Prefer the current `monetization.onetimeproducts` model for new one-time catalogs where supported. It includes purchase options, offers, and regional configuration. Inspect the existing catalog's migration state before changing older `inappproducts` integrations. Do not create duplicate products to imitate an existing legacy SKU or claim all old products must be deleted immediately.

For subscriptions, separate the subscription product, base plan, and optional offer. Monthly versus annual can be base plans under the appropriate product model. Auto-renewing and prepaid plans have different fields and lifecycle behavior. Offer tags are billing-selection metadata, not store-listing keywords. Do not apply a plan automatically just because its price is lowest.

## Configuration sequence

1. Read existing products/base plans/offers and country/region requirements.
2. Retrieve or calculate regional prices using supported money models and region-version requirements. Use currency units/nanos or the actual endpoint contract, never a binary float for stored prices.
3. Create/patch the product with exact update masks and the required `regionsVersion` when specified. Required regional compliance fields must come from the owner and implementation.
4. Create purchase options or base plans, then eligible offers. Configure renew/prepaid behavior, duration, billing period, trial phases, grace/account hold, installment details where supported, country targeting, and regional price behavior deliberately.
5. Activate the appropriate base plan, purchase option, and offer through the supported lifecycle operations. Creation alone does not make a product purchasable.
6. Re-read the full graph and verify product/basePlan/offer IDs, state, locales, prices, countries, and client-visible results. Product mutations are outside edit transactions.

For price migrations, read existing subscribers, regional rules, consent requirements, effective dates, and opt-in/opt-out behavior. Explain expected customer impact before executing an authorized migration. Deactivate only the intended sales surface. Subscription archiving is deprecated/unsupported in the current contract. Do not assume deactivation cancels existing subscriptions. [Pricing and availability](pricing-and-availability.md) explains exact money, region-version, schedule/cohort and console boundaries.

## Complete current catalog field ownership

| Model | Inputs and state rules |
| --- | --- |
| `OneTimeProduct` | Immutable `packageName`/`productId`, required localized `listings` and `purchaseOptions`, optional `offerTags`, `restrictedPaymentCountries` and `taxAndComplianceSettings`. `regionsVersion` on the returned product is output-only. |
| `OneTimeProductListing` | `languageCode`, `title` up to 55 characters and `description` up to 200. No duplicate locale entries. Use the actual default and supported translations. |
| `OneTimeProductPurchaseOption` | Immutable `purchaseOptionId`, `buyOption` or `rentOption`, `regionalPricingAndAvailabilityConfigs`, optional `newRegionsConfig`, tags and tax/compliance. Returned `state` is changed only through the dedicated state action. |
| Buy/rent details | Buy can support multi-quantity. Rent defines ISO 8601 `rentalPeriod` and optional `expirationPeriod`. New work does not enable deprecated-client compatibility merely because that field exists. |
| One-time regional entry | `regionCode`, `price` and current `availability` such as `AVAILABLE`, `NO_LONGER_AVAILABLE`, `AVAILABLE_IF_RELEASED` or `AVAILABLE_FOR_OFFERS_ONLY`. Choose the exact intended state, not a generic boolean. |
| `OneTimeProductOffer` | Immutable package/product/option/offer IDs, regional pricing/availability, tags and one supported preorder, discounted or game-reward configuration. State and returned regions version are output-only. |
| `Subscription` | Immutable package/product IDs, required localized `listings`, intended `basePlans`, optional restricted payment countries and tax/compliance. Do not write the deprecated `archived` output field. |
| `SubscriptionListing` | `languageCode`, `title`, description up to 200 characters and at most four ordered benefit strings. At least the app's default language is required. |
| `BasePlan` | Immutable `basePlanId`, exactly the supported actual auto-renewing/prepaid/installment type, regional configs, future-region settings and tags. Use dedicated activation/deactivation actions for its output state. |
| `SubscriptionOffer` | Immutable IDs, required `regionalConfigs`, one or two ordered `phases`, optional targeting, tags and future-region configs. Active offer alone does not override an inactive base plan. |
| Subscription phase | ISO 8601 `duration`, `recurrenceCount`, per-region price/free/relative-price configuration from the exact phase model and future-region policy. Each phase must cover the offer's intended regions consistently. |

Field names and nested payloads differ between one-time and subscription pricing. Do not copy a `regionalConfigs` object into `regionalPricingAndAvailabilityConfigs` or use one type's activation endpoint for another. Repeated fields require reconstructing the intended list rather than assuming element-level merge.

### Base-plan decisions

- Auto-renewing: immutable `billingPeriodDuration`, actual `gracePeriodDuration`, `accountHoldDuration`, `resubscribeState` and `prorationMode`. Current constraints allow grace up to the lesser of 30 days and the billing period, account hold up to 60 days, and combined grace/hold from 30 to 60 days. Confirm the actual allowed ISO duration and selected period before saving.
- Prepaid: immutable `billingPeriodDuration` and supported `timeExtension`. A prepaid entitlement does not automatically renew because the UI calls it a subscription.
- Installments: immutable period, committed payment count and renewal type, plus supported grace/account hold/resubscribe/proration settings. Disclose the actual commitment and what happens after it ends.
- Future regions and existing-customer changes are explicit commercial choices. Do not enable global availability or migrate an old cohort while editing a title.

### State actions and offers

Current one-time products are created through supported upsert, not an invented `onetimeproducts.insert`. Configure purchase options in the parent and activate/deactivate through `purchaseOptions.batchUpdateStates` with one matching request branch per option. One-time offers use supported `batchUpdate` for creation/update and the actual activate/deactivate/cancel action. Their batch contracts can use the documented `-` parent selector across products, but never generalize that selector to methods that do not support it.

Subscriptions support actual create/patch. Base plans are configured in the subscription graph and activated through their dedicated actions. Subscription offers have their own create/patch and state endpoints. Read every batch's limit, update mask, regions-version placement, error semantics and returned per-item results. A successful request wrapper does not justify ignoring an item's failure.

Offers need truthful eligibility and terms: acquisition/upgrade/developer targeting, trial or discounted periods, ordinary renewal price, redemption limit, start/end/release dates and actual region support. Multi-quantity, rentals, prepaid top-ups and installments require the app/backend to implement their real entitlement semantics before enabling sale.

## Billing client and backend

Use a currently permitted Play Billing Library through the app's chosen native or cross-platform SDK. Query product details and current eligible offer tokens. Display localized full price, billing interval, trial/discount phases, renewal price, cancellation access, and material restrictions. Launch purchase from the appropriate foreground activity and handle service connection and lifecycle deliberately.

The secure backend verifies package, product, purchase token, purchase state, quantity, and subscription line items through the current purchase endpoints. Use `purchases.subscriptionsv2.get` for the current subscription model, and the appropriate product purchase endpoint for one-time products. Never trust a client success screen or local boolean alone.

Grant benefits only after `PURCHASED`, not `PENDING`. For direct application-owned processing, persist an idempotent transaction/fulfillment record before acknowledging or consuming. Normally acknowledge eligible purchases within three days of purchase completion to prevent automatic refund. Pending-purchase timing starts when the purchase completes. Confirm current exceptions and SDK ownership before implementation. Consumables use the appropriate consume flow, non-consumables/subscriptions use acknowledgment as required. Standard RevenueCat integration owns automatic acknowledgment/consumption. Reconcile custom consumable delivery against its verified records/webhooks without assuming an unconsumed store listing remains available or acknowledging independently a second time.

Use purchase tokens only in protected channels and storage. They identify purchases but do not replace app-user authorization. Associate purchases with authenticated accounts through a deliberate fraud-resistant policy and store-supported obfuscated account identifiers when applicable. Never attach one customer's transaction to another because the client supplied an arbitrary user ID.

## Notifications and lifecycle

Configure Real-time Developer Notifications through Google Cloud Pub/Sub with the intended topic permissions and authenticated delivery. Validate push identity/audience or use protected pull subscribers. Treat notifications as a prompt to query authoritative current purchase state. Deduplicate, tolerate delay/out-of-order delivery, and retain reconciliation jobs.

Test pending completion/cancellation, prepaid top-up, renewals, upgrade/downgrade and replacement modes, linked purchase tokens, cancellation, expiration, grace, account hold, pause/resume where available, refund, revocation, chargeback/voided purchases, restore, reinstall, and account switch. Cancellation can leave access through the paid period. Refund and revoke are distinct financial/entitlement operations. Preserve access until the verified entitlement policy says otherwise.

Use test-track builds, licensed testers, store-configured products, and approved test payment methods. A local mocked billing response does not prove Play catalog readiness. Record sandbox/test results without leaking raw purchase tokens or real payment data. Confirm production products remain active in the intended countries and that the release version contains the same identifiers.
