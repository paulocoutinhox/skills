# App, product and subscription pricing

Verified on **2026-11-05** against the official OpenAPI 4.6 and [app pricing help](https://developer.apple.com/help/app-store-connect/manage-app-pricing/set-a-price/). Commercial operations can take effect independently of binary review. A saved listing or approved build does not prove correct prices or sale territories.

## Establish the commercial decision

Collect paid/free download, base country, desired customer price/currency, sales territories, start/end dates, tax category, automatic equalization policy, manual country overrides, preorder strategy, IAP/subscription catalog and existing-customer price policy. Distinguish customer price, developer proceeds, tax and store commission. Do not calculate a payout by treating the displayed price as net revenue.

Read the current schedule, automatic/manual prices, territories and product/subscription prices before writing. Prepare a country/currency/date comparison of current and intended values. Record who approved actual commercial choices. Do not convert “publish the next build” into permission to change every price or country.

## Download price: supported API route

1. Read `GET /v1/territories` and the app's `GET /v1/apps/{id}/appPricePoints`, using supported territory filters and pagination. Select a returned price-point resource by its actual customer price/currency. Never construct an encoded price-point ID.
2. Read `GET /v1/apps/{id}/appPriceSchedule` and its `baseTerritory`, `manualPrices` and `automaticPrices` relationships. Preserve deliberate scheduled/manual decisions.
3. When comparing regional prices, use the current `/v3/appPricePoints/{id}` and `/v3/appPricePoints/{id}/equalizations` operations. API versions differ across resource families. Do not mechanically use `/v1/` everywhere.
4. Create the intended schedule with `POST /v1/appPriceSchedules`. Its required relationships are `app`, `baseTerritory` and `manualPrices`. Inline manual prices use `appPrices`, actual `appPricePoints` IDs and the schema's `startDate`/`endDate` date attributes.
5. Read the resulting schedule and all automatic/manual rows back. Verify exact countries, dates, currencies and price points, then verify the customer-facing result after propagation.

For an approved immediate base-price decision, the request shape is:

```json
{
  "data": {
    "type": "appPriceSchedules",
    "relationships": {
      "app": {"data": {"type": "apps", "id": "<app-id>"}},
      "baseTerritory": {"data": {"type": "territories", "id": "USA"}},
      "manualPrices": {"data": [{"type": "appPrices", "id": "${base-price}"}]}
    }
  },
  "included": [
    {
      "type": "appPrices",
      "id": "${base-price}",
      "attributes": {"startDate": null, "endDate": null},
      "relationships": {
        "appPricePoint": {"data": {"type": "appPricePoints", "id": "<returned-price-point-id>"}}
      }
    }
  ]
}
```

This is a shape example, not a complete schedule for an existing app. Replace IDs and territory with the actual decision. The inline identifier links the included object to its relationship. Reconstruct every intended current/future manual interval rather than silently replacing an existing schedule with this single row. Confirm null/date semantics for the operation and selected state before execution.

Apple's automatic equalization adjusts other storefronts for the chosen base. Manual territory prices opt out of that automatic adjustment. A base-country change can delete scheduled price changes and affect inherited IAP base-country settings. Inventory those consequences before making the change. Do not treat changing the base as cosmetic metadata maintenance.

## App territories, release dates and preorder

Use the current v2 app-availability model:

- Read `GET /v1/apps/{id}/appAvailabilityV2` and related `territoryAvailabilities`.
- Create configuration with `POST /v2/appAvailabilities`, required `availableInNewTerritories`, `app` and `territoryAvailabilities` relationships. Included `territoryAvailabilities` relate each actual territory and its `available`, `releaseDate` and `preOrderEnabled` choices.
- For supported per-territory changes, use `PATCH /v1/territoryAvailabilities/{id}` with only intended attributes.
- Explicitly decide whether future territories become available automatically. An empty/omitted selection must not accidentally mean worldwide sale.
- For preorder termination, use the documented `endAppAvailabilityPreOrders` operation only for the authorized eligible case. Confirm release type, preorder dates, selected binary and actual country state together.

App availability, binary release and product availability are separate. A sale-enabled country with no released compatible version is not a verified installable storefront. Removing sale does not remotely uninstall existing customers' apps. Confirm the exact business purpose before removing countries or ending a preorder.

## In-app purchase prices and availability

Read the actual product through `/v2/inAppPurchases/{id}`. Retrieve its price points, existing `inAppPurchasePriceSchedule`, automatic/manual prices and availability. Use `/v1/inAppPurchasePricePoints/{id}/equalizations` to inspect equivalents.

Create `POST /v1/inAppPurchasePriceSchedules` with required `inAppPurchase`, `baseTerritory` and `manualPrices` relationships. Inline prices are `inAppPurchasePrices`, with `startDate`/`endDate` and `inAppPurchasePricePoint` linkage. Do not reuse an app-download price-point ID or send a floating-point number in its place.

`inAppPurchaseAvailabilities` uses `availableInNewTerritories`, the `inAppPurchase` relationship and the complete intended `availableTerritories` set. Read existing countries first and preserve unchanged ones. Validate the current product version, price schedule, sale availability and review state together before expecting StoreKit to sell it.

## Subscription prices, plans and existing subscribers

Read the subscription/group, current product version, plan type, price points, prices, offers and availability. A period/plan/territory price point must belong to the actual subscription. Use `subscriptionPricePoints` and their `equalizations` / `adjustedEqualizations` contracts as applicable.

Create `POST /v1/subscriptionPrices` with the required `subscription` and `subscriptionPricePoint` relationships, intended territory and supported `startDate`, `preserveCurrentPrice` and `planType` attributes. Explicitly decide whether to preserve an existing subscriber's price. A new-customer price update and a migration of existing customers are different commercial actions.

Check current price-increase notification/consent eligibility for the actual country, increase and customer cohort. Do not invent a universal percentage threshold or assume every increase is automatic. Record effective dates and the expected behavior for customers who decline required consent. Avoid introducing any increase as a side effect of changing a different locale or plan.

`subscriptionAvailabilities` controls product countries and future-territory behavior. `subscriptionPlanAvailabilities` adds the current `planType` and plan-specific countries. A subscription enabled in one territory does not make every offer or plan available there.

## Offers and billing grace

| Surface | What must be configured and checked |
| --- | --- |
| `subscriptionIntroductoryOffers` | Start/end, duration, number of periods, offer mode, intended plan, territory/price point and actual introductory eligibility. |
| `subscriptionPromotionalOffers` | Stable offer code/name, duration, period count, mode, plan, regional prices and the separate signed-offer client/server flow. |
| `subscriptionOfferCodes`, custom/one-time-use codes | Eligibility, dates, redemption limits, regions/prices, distribution scope and code secrecy. Creating codes does not authorize distributing them. |
| `winBackOffers` | Offer ID/reference name, paid-history threshold, months since subscription, wait between offers, duration/period count/mode, plan, dates, priority/promotion intent and prices. |
| IAP offer-code families | Correct one-time product, supported eligibility/redemption configuration and actual country/product availability. Do not reuse subscription code schemas. |
| `subscriptionGracePeriods` | `optIn`, `sandboxOptIn`, `duration`, `renewalType` and observed entitlement behavior. A billing grace setting is not a refund or cancellation. |
| `retentionOffers`, `retentionMessages` and versions/localizations | Eligible retention surface, truthful offer, message media, localization and review. Do not promise unsupported cancellation interception. |

Use [the product lifecycle reference](purchases-and-subscriptions.md) for creation, review and fulfillment. Fetch StoreKit prices and eligible offers in the client. A price copied into a screenshot or description can become false across currencies and dates. Prefer durable value/plan wording and the current localized purchase sheet.

## Tax and owner-only actions

The researched API does not expose a general app-tax-category PATCH field. Complete the actual Connect procedure: app → Pricing and Availability → Tax Category → Edit → applicable category/subcategory/attributes → Done. Base this on the owner's product facts. Contracts, banking, tax submissions and required trader/legal attestations have their own owner-controlled surfaces.

Confirm the resulting store configuration and record blocked owner decisions. Do not certify tax correctness or invent an owner attestation. Appropriate roles, paid-app agreements and banking/tax eligibility can block otherwise valid pricing requests.

## Commercial verification cases

Check free/paid download, selected base country, one automatic-equalization country, every manual override, scheduled boundary dates, unavailable countries and future-territory intent. For subscriptions, test a new customer and an existing preserved-price customer separately. Verify trial/discount then ordinary renewal price, taxes, restored permanent purchases and region-dependent eligibility.

Record actual readback, timestamps, currency/price-point IDs, storefront and sandbox/production observations. An HTTP 201 is configuration evidence, not proof that every customer already sees the intended price.
