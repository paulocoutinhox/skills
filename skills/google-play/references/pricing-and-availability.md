# Download pricing, regional products and availability

Monetization methods were checked on **2026-11-05**, and the Publisher v3 list of operations at revision **20261118** was checked on **2026-11-18**. [App pricing help](https://support.google.com/googleplay/android-developer/answer/6334373?hl=en) and the free-app lock were checked on **2026-11-24**. Tell apart the app download price, product price, subscription and subscriber-group price, taxes, proceeds and eligibility. They are not one `price` attribute on a store listing.

## Commercial inventory before changing anything

Record the free or paid download, the real payments profile, the base decision and currency, sale countries, the intended customer price per region, the tax and product classification, dates, the policy for future regions, existing subscribers, offer eligibility and authorization. Read the existing products, plans, options and offers and compare current values with intended ones. Keep prices and countries nobody asked to change, and record separate operations in [the evidence template](../assets/release-evidence.md).

App download pricing, product catalog writes and listing or track edits each commit and go through review differently. Deleting an edit does not undo a standalone price change. Do not replace the whole catalog to change one translated word.

## Paid app versus free app

For an ordinary Play listing, AppDetails and Listing have no download-price or free/paid field. Use Play Console → Products → App pricing to choose the real free or paid status, payments profile and supported regional prices. Read the current country currency, minimum, maximum and tax behavior, review the generated local prices, make deliberate overrides and save. The console can show different pricing flows for accounts enrolled in the newer one-time-product program. Follow the documented flow that applies instead of inventing a special paid-app product ID.

**A free app cannot be changed into a paid app once it has been sent for review.** The console says the choice can be edited "until publication", but sending a free app for review locks it as free, even when it was never published. App pricing then reads "The app is available for free on Google Play and can't be changed to paid". Remove changes does not unlock it. Paid-to-free is supported. Creating another package to charge later is a new app and business decision, not a shortcut for an update. Do not change paid to free as a temporary workaround.

Before you choose Free or Paid, read the owner's plan, release brief, store documents and the live price on the other stores. When any of them says paid, the Play app is paid. Check App pricing again right before Send changes for review. If the lock already applies, the way back is the owner-authorized deletion procedure in [the Console browser reference](play-console-browser.md#deleting-an-app-to-start-over): the package name stays reserved for seven days, then comes back only when the app had zero installs ever.

The current help notice retires linked pricing templates from October 27, 2025. Later parts of that help page still describe the former workflow. Follow the explicit retirement notice and the current per-product and console methods, not outdated instructions to create a new shared pricing template.

Availability must match pricing. A regional price does not make the app available in that country. Read `edits.countryavailability.get`, the real track sync and the production country setup. That ordinary family is read-only in the API we researched. Release-level `countryTargeting` applies only to supported production `inProgress` releases. It is not a general app-country PATCH or a product sales-country setting.

## Money, currencies and region versions

Current monetization prices use `Money`:

```json
{"currencyCode": "USD", "units": "4", "nanos": 990000000}
```

This means USD 4.99. `units` is an integer string, and `nanos` is a signed integer count of 10^-9 parts, with matching sign rules. Do not use a binary float, integer cents in `units` or older `priceMicros` fields in a Money model. The real price must be allowed for the chosen region and product.

Use `monetization.convertRegionPrices` with the intended Money amount to get supported conversion suggestions and related region data. Review the returned currency, price and tax results before you save them. Do not make up unsupported currency choices, or assume exchange rates alone set the final customer price with tax included.

Catalog patch and update contracts can require `regionsVersion.version` in query parameters, or a `regionsVersion` request object in a particular batch or action. Use the current supported version from the official region docs or provider responses for that operation. A Discovery parameter marked optional in its structure can still say Required in its behavior description. Do not leave out update masks or region versions just because a generated client lets you.

## Current one-time product creation and prices

1. Read the existing product IDs and the current product state. Settle the real entitlement, localization, purchase option and regional availability.
2. Create through `monetization.onetimeproducts.patch` with `allowMissing=true` set on purpose, the real `updateMask` and a supported regions version. Normal updates should not quietly create a misspelled product.
3. Send the required `packageName`, the `productId` that never changes, localized `listings` and `purchaseOptions`. Product IDs allow lowercase letters, digits, underscore and dot, unlike hyphenated purchase-option IDs. Keep these valid naming exceptions that the tool requires.
4. For each option, set up either a supported `buyOption` or `rentOption`, the real `regionalPricingAndAvailabilityConfigs`, optional future-region settings, compliance and tags. State is output-only.
5. Activate the real option using `purchaseOptions.batchUpdateStates` and its `activatePurchaseOptionRequest`, then check availability through readback and Billing product details.

Here is a shape example for a new repeatable coin product, created on purpose:

```json
{
  "packageName": "com.example.orbitgame",
  "productId": "coins.100",
  "listings": [
    {"languageCode": "en-US", "title": "100 coins", "description": "Add 100 coins to your game balance."}
  ],
  "purchaseOptions": [
    {
      "purchaseOptionId": "buy",
      "buyOption": {},
      "regionalPricingAndAvailabilityConfigs": [
        {
          "regionCode": "US",
          "price": {"currencyCode": "USD", "units": "4", "nanos": 990000000},
          "availability": "AVAILABLE"
        }
      ]
    }
  ]
}
```

This is made-up shape data, not a suggested price, a real product or a full update of an existing catalog. Replace the package, product design, languages, regions, compliance and prices. A coin product belongs in a game that really has that economy. Decide future-region availability on purpose instead of turning it on by accident. Creating and configuring a product does not activate an option or prove how the client delivers it.

The upsert path is `/applications/{packageName}/onetimeproducts/{productId}`. The documented state-action path uses `/applications/{packageName}/oneTimeProducts/{productId}/purchaseOptions:batchUpdateStates`. Keep the published casing instead of building every path from a naming pattern.

For an existing product, masks such as `listings` or `purchaseOptions` point to repeated structures. Read and rebuild the full intended list that is affected. Do not remove other locales, options or regions by sending only the changed entry and assuming the array will be merged.

## Subscription prices and cohorts

Read the subscription's localized listings, every base plan, the regional config, the future-region config and offers. Define a real base-plan type: auto-renewing, prepaid or installments. A base plan's price belongs to its real region and currency, period and commitment, not just its product ID.

For each `regionalConfigs` entry, `regionCode`, `price` and `newSubscriberAvailability` control new sales. Where you mean to sell, set availability and the required regional price explicitly. Turning off new-subscriber availability does not cancel existing subscribers. Future-region behavior is a separate setting you choose on purpose.

When you change a price:

1. Keep the full intended base-plan array and the IDs and periods that never change, while updating only the real allowed mask.
2. Check new-customer prices, availability and how they spread, separately from existing subscriber groups.
3. For an authorized move of existing prices, use `basePlans.migratePrices` / `batchMigratePrices`, the required regions version and `regionalPriceMigrations`.
4. Each migration names `regionCode`, `oldestAllowedPriceVersionTime` and a supported `priceIncreaseType`. Opt-in or opt-out eligibility, the notice period and the date billing changes depend on the real regional rules.
5. Before you run it, explain which subscriber groups are affected, how customers are notified or asked to agree, and when they could lose access. Never move all old subscriber groups by picking a random timestamp.
6. Read the results again and check the intended subscriber-group policy. A catalog price change does not prove that all existing renewals now use it.

## Offers, rental and tax configuration

| Configuration | Required decisions |
| --- | --- |
| One-time buy | The real benefit, optional multi-quantity support and idempotent delivery that respects quantity. |
| One-time rent | ISO 8601 rental period and optional expiry period after start, with the real meaning of entitlement start and end. |
| Discount offer | Supported regional price and availability, start and end, and redemption limit. Review how zero or unset (unlimited) behaves before any change. |
| Preorder offer | Start, end and release time, and the supported price-change behavior for existing preorders, which cannot be changed later. Do not grant released content before the contract allows it. |
| Game-reward offer | The real reward-offer setup supported today and an eligible client or program. Do not model it as a generic discount. |
| Subscription offer | An active parent plan, real targeting, one or two ordered phases, phase duration and repeats, matching regional prices and future-region policy. |
| Offer tags | At most twenty custom billing tags at the supported product, option, plan and offer levels. They help the client pick offers and are not searchable store tags. |
| Tax/compliance | The real product tax category code, regional tax data, tokenized-digital-asset declaration, regional product age ratings that apply and EEA withdrawal classification where supported. The owner's facts decide the answers. |

Current subscription types offer settings for grace and account-hold periods, resubscribe behavior and proration. Apply their allowed durations and combined limits instead of copying defaults from a different period or plan type. Installment commitments and renewal behavior need clear disclosure. More detail on which fields belong where is in [products and subscriptions](products-and-subscriptions.md).

Promo codes, app sales and other console-only promotion areas need their own real eligibility, dates and redemption terms. A supported subscription or one-time offer API does not mean a general app-sale or promo-code endpoint exists.

## Commercial acceptance

Read the configuration back and inspect real store and Billing results for the intended country, locale and test account. Test new sales, a trial followed by a full renewal, ineligible offers, disabled countries, restored purchases, multi-quantity and rental where used, and kept subscriber prices. Cover cancel, error and pending states without delivering access that is not supported.

Record prices and currencies, region version, masks, IDs, activation states, dates, the subscriber-group decision and evidence. Report spread delays and production checks you did not run explicitly. Paid download price changes and refunds are real actions that customers see, not harmless metadata cleanup.
