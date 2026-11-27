# App, product and subscription pricing

Checked on **2026-11-05** against the official OpenAPI 4.6 and [app pricing help](https://developer.apple.com/help/app-store-connect/manage-app-pricing/set-a-price/). Pricing and sales changes can take effect without binary review. A saved listing or an approved build does not prove the prices or sale territories are right.

## Establish the commercial decision

Collect: paid or free download, base country, the customer price and currency you want, sales territories, start and end dates, tax category, automatic equalization policy, manual country overrides, preorder plan, IAP and subscription catalog, and the price policy for existing customers. Keep customer price, developer proceeds, tax and store commission apart. Do not work out a payout by treating the displayed price as net revenue.

Read the current schedule, automatic and manual prices, territories and product and subscription prices before writing. Prepare a comparison of current and intended values by country, currency and date. Record who approved the real commercial choices. Do not turn “publish the next build” into permission to change every price or country.

## Download price: supported API route

1. Read `GET /v1/territories` and the app's `GET /v1/apps/{id}/appPricePoints`, using supported territory filters and pagination. Pick a returned price-point resource by its real customer price and currency. Never build an encoded price-point ID yourself.
2. Read `GET /v1/apps/{id}/appPriceSchedule` and its `baseTerritory`, `manualPrices` and `automaticPrices` relationships. Keep scheduled and manual decisions that are there on purpose.
3. When comparing regional prices, use the current `/v3/appPricePoints/{id}` and `/v3/appPricePoints/{id}/equalizations` operations. API versions differ between resource families. Do not use `/v1/` everywhere by habit.
4. Create the intended schedule with `POST /v1/appPriceSchedules`. Its required relationships are `app`, `baseTerritory` and `manualPrices`. Inline manual prices use `appPrices`, real `appPricePoints` IDs and the schema's `startDate`/`endDate` date attributes.
5. Read the resulting schedule and all automatic and manual rows back. Check the exact countries, dates, currencies and price points, then check what customers see after the change spreads.

For an approved base-price decision that takes effect now, the request shape is:

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

This shows the shape only. It is not a full schedule for an existing app. Replace the IDs and territory with the real decision. The inline identifier links the included object to its relationship. Rebuild every intended current and future manual interval instead of quietly replacing an existing schedule with this one row. Confirm what null and dates mean for the operation and the chosen state before you run it.

Apple's automatic equalization adjusts other stores for the chosen base. Manual territory prices opt out of that automatic adjustment. Changing the base country can delete scheduled price changes and affect inherited IAP base-country settings. List those effects before making the change. Do not treat a base change as a small metadata edit.

## App territories, release dates and preorder

Use the current v2 app-availability model:

- Read `GET /v1/apps/{id}/appAvailabilityV2` and the related `territoryAvailabilities`.
- Create the configuration with `POST /v2/appAvailabilities`, the required `availableInNewTerritories`, and the `app` and `territoryAvailabilities` relationships. The included `territoryAvailabilities` link each real territory and its `available`, `releaseDate` and `preOrderEnabled` choices.
- For supported changes to one territory, use `PATCH /v1/territoryAvailabilities/{id}` with only the attributes you mean to change.
- Decide clearly whether future territories become available automatically. An empty or omitted selection must not end up meaning worldwide sale by accident.
- To end a preorder, use the documented `endAppAvailabilityPreOrders` operation only for the allowed, eligible case. Confirm the release type, preorder dates, chosen binary and real country state together.

App availability, binary release and product availability are separate. A country open for sale with no released compatible version is not a checked store page people can install from. Removing the app from sale does not remove it from existing customers' devices. Confirm the exact business reason before removing countries or ending a preorder.

## In-app purchase prices and availability

Read the real product through `/v2/inAppPurchases/{id}`. Get its price points, the existing `inAppPurchasePriceSchedule`, automatic and manual prices and availability. Use `/v1/inAppPurchasePricePoints/{id}/equalizations` to see equal prices in other stores.

Create `POST /v1/inAppPurchasePriceSchedules` with the required `inAppPurchase`, `baseTerritory` and `manualPrices` relationships. Inline prices are `inAppPurchasePrices`, with `startDate`/`endDate` and an `inAppPurchasePricePoint` link. Do not reuse an app-download price-point ID or send a floating-point number in its place.

`inAppPurchaseAvailabilities` uses `availableInNewTerritories`, the `inAppPurchase` relationship and the full intended `availableTerritories` set. Read the existing countries first and keep the ones that do not change. Check the current product version, price schedule, sale availability and review state together before you expect StoreKit to sell it.

## Subscription prices, plans and existing subscribers

Read the subscription and group, the current product version, plan type, price points, prices, offers and availability. A price point for a period, plan or territory must belong to the real subscription. Use `subscriptionPricePoints` and their `equalizations` / `adjustedEqualizations` contracts as they apply.

Create `POST /v1/subscriptionPrices` with the required `subscription` and `subscriptionPricePoint` relationships, the intended territory and the supported `startDate`, `preserveCurrentPrice` and `planType` attributes. Decide clearly whether to keep an existing subscriber's price. Changing the price for new customers and moving existing customers to a new price are different business actions.

Check the current price-increase notice and consent rules for the real country, increase and group of customers. Do not make up a percentage threshold that applies everywhere or assume every increase is automatic. Record start dates and what is expected for customers who decline required consent. Do not let an increase happen as a side effect of changing a different locale or plan.

`subscriptionAvailabilities` controls product countries and how future territories behave. `subscriptionPlanAvailabilities` adds the current `planType` and countries for each plan. A subscription turned on in one territory does not make every offer or plan available there.

## Offers and billing grace

| Surface | What must be configured and checked |
| --- | --- |
| `subscriptionIntroductoryOffers` | Start/end, duration, number of periods, offer mode, intended plan, territory/price point and real introductory eligibility. |
| `subscriptionPromotionalOffers` | Stable offer code/name, duration, period count, mode, plan, regional prices and the separate signed-offer client/server flow. |
| `subscriptionOfferCodes`, custom/one-time-use codes | Eligibility, dates, redemption limits, regions/prices, who receives them and keeping codes secret. Creating codes does not allow handing them out. |
| `winBackOffers` | Offer ID/reference name, paid-history threshold, months since subscription, wait between offers, duration/period count/mode, plan, dates, priority/promotion intent and prices. |
| IAP offer-code families | Correct one-time product, supported eligibility and redemption setup and real country and product availability. Do not reuse subscription code schemas. |
| `subscriptionGracePeriods` | `optIn`, `sandboxOptIn`, `duration`, `renewalType` and the entitlement behavior you observe. A billing grace setting is not a refund or cancellation. |
| `retentionOffers`, `retentionMessages` and versions/localizations | Eligible retention screen, an honest offer, message media, localization and review. Do not promise you can stop cancellations in ways that are not supported. |

Use [the product lifecycle reference](purchases-and-subscriptions.md) for creation, review and delivery. Fetch StoreKit prices and eligible offers in the client. A price copied into a screenshot or description can become wrong across currencies and dates. Prefer value and plan wording that stays true, and the current localized purchase sheet.

## Tax and owner-only actions

The researched API has no general PATCH field for the app tax category. Use the real Connect steps: app → Pricing and Availability → Tax Category → Edit → the category, subcategory and attributes that apply → Done. Base this on the owner's product facts. Contracts, banking, tax submissions and required trader or legal statements each have their own screens that the owner controls.

Confirm the resulting store settings and record owner decisions that are blocked. Do not certify that tax is correct or make up an owner statement. Missing roles, paid-app agreements and banking or tax eligibility can block pricing requests that are otherwise valid.

## Commercial verification cases

Check free and paid download, the chosen base country, one automatic-equalization country, every manual override, the dates at the edges of a schedule, unavailable countries and the plan for future territories. For subscriptions, test a new customer and an existing customer who keeps an old price separately. Check the trial or discount and then the normal renewal price, taxes, restored permanent purchases and eligibility that depends on region.

Record the real read-back, timestamps, currency and price-point IDs, and what you saw in the store and in sandbox or production. An HTTP 201 shows the setting was saved. It does not prove every customer already sees the intended price.
