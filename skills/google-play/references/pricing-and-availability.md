# Download pricing, regional products and availability

Verified on **2026-11-05** against Publisher v3 revision **20261105**, [app pricing help](https://support.google.com/googleplay/android-developer/answer/6334373?hl=en) and current monetization methods. Distinguish app-download price, product price, subscription/cohort price, taxes, proceeds and eligibility. They are not one `price` attribute on a store listing.

## Commercial inventory before changing anything

Record free/paid download, actual payments profile, base decision/currency, sale countries, intended customer price per region, tax/product classification, dates, future-region policy, existing subscribers, offer eligibility and authorization. Read existing products/plans/options/offers and compare current to intended values. Preserve unrequested prices/countries and record independent operations in [the evidence template](../assets/release-evidence.md).

App-download pricing, product catalog writes and listing/track edits have different commit/review behavior. Deleting an edit does not undo a standalone price mutation. Do not use a full catalog replacement to change one translated word.

## Paid app versus free app

For an ordinary Play listing, AppDetails/Listing have no download-price or free/paid field. Use Play Console → Products → App pricing to select actual free/paid status, payments profile and supported regional prices. Read current country currency/minimum/maximum and tax behavior, review generated local prices, apply deliberate overrides and save. The console can present different pricing flows for accounts enrolled in the newer one-time-product program. Follow the applicable documented flow rather than inventing a special paid-app product ID.

**A published free app cannot be changed into a paid app.** Paid-to-free is supported, but creating another package to charge later is a new app/business decision, not an update shortcut. Do not change paid to free as a temporary workaround.

The current help notice retires linked pricing templates from October 27, 2025. Later parts of that help page still describe the former workflow. Follow the explicit retirement notice and current per-product/console methods, not obsolete instructions to create a new shared pricing template.

Availability must agree with pricing. A regional price does not distribute the app in that country. Read `edits.countryavailability.get`, actual track synchronization and production country setup. That ordinary family is read-only in the researched API. Release-level `countryTargeting` only applies to supported production `inProgress` releases. It is not a general app-country PATCH or a product sales-country setting.

## Money, currencies and region versions

Current monetization prices use `Money`:

```json
{"currencyCode": "USD", "units": "4", "nanos": 990000000}
```

This represents USD 4.99. `units` is an integer string and `nanos` is a signed integer fraction of 10^-9, with matching sign rules. Do not use a binary float, integer cents in `units` or older `priceMicros` fields in a Money model. The actual price must be legal for the selected region and product.

Use `monetization.convertRegionPrices` with the intended Money amount for supported conversion suggestions and related region data. Review returned currency/price/tax results before persisting. Do not fabricate unsupported currency choices or assume FX alone determines the final tax-inclusive customer price.

Catalog patch/update contracts can require `regionsVersion.version` in query parameters or a `regionsVersion` request object in a particular batch/action. Use the current supported version from official region documentation/provider responses for that operation. A Discovery parameter marked structurally optional can still say Required in its behavioral description. Do not omit update masks/region versions merely because a generated client allows omission.

## Current one-time product creation and prices

1. Read existing product IDs and current product state. Establish the real entitlement, localization, purchase option and regional availability.
2. Create through `monetization.onetimeproducts.patch` with deliberate `allowMissing=true`, actual `updateMask` and supported regions version. Normal updates should not silently create a misspelled product.
3. Supply required `packageName`, immutable `productId`, localized `listings` and `purchaseOptions`. Product IDs allow lowercase letters/digits/underscore/dot, unlike hyphenated purchase-option IDs. Keep these valid tool-required naming exceptions.
4. For each option, configure either supported `buyOption` or `rentOption`, actual `regionalPricingAndAvailabilityConfigs`, optional future-region settings, compliance and tags. State is output-only.
5. Activate the actual option using `purchaseOptions.batchUpdateStates` and its `activatePurchaseOptionRequest`, then verify availability through readback and Billing product details.

Shape example for a deliberately new repeatable coin product:

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

This is fictional shape data, not a recommended price, real product or complete existing catalog update. Replace package, product design, languages, regions, compliance and prices. A coin product belongs to a game that actually implements that economy. Explicitly decide future-region availability instead of accidentally enabling it. Creation/configuration does not activate an option or prove the client's delivery behavior.

The upsert path is `/applications/{packageName}/onetimeproducts/{productId}`. The documented state-action path uses `/applications/{packageName}/oneTimeProducts/{productId}/purchaseOptions:batchUpdateStates`. Preserve the published casing rather than constructing all paths by naming convention.

For an existing product, masks such as `listings` or `purchaseOptions` refer to repeated structures. Read and reconstruct the intended complete affected list. Do not remove other locales, options or regions by sending only the changed entry and assuming array merge behavior.

## Subscription prices and cohorts

Read the subscription's localized listings, every base plan, regional config, future-region configuration and offers. Define a real base-plan type: auto-renewing, prepaid or installments. The price of a base plan belongs to its actual region/currency, period and commitment, not merely its product ID.

For each `regionalConfigs` entry, `regionCode`, `price` and `newSubscriberAvailability` control new sales. Where sale is intended, explicitly set availability and the required regional price. Disabling new-subscriber availability does not cancel existing subscribers. Future-region behavior is a separate intentional configuration.

When changing price:

1. Preserve the complete intended base-plan array and immutable IDs/periods while updating only the actual allowed mask.
2. Verify new-customer prices/availability and propagation separately from existing-customer cohorts.
3. For an authorized migration, use `basePlans.migratePrices` / `batchMigratePrices`, required regions version and `regionalPriceMigrations`.
4. Each migration identifies `regionCode`, `oldestAllowedPriceVersionTime` and supported `priceIncreaseType`. Opt-in/opt-out eligibility, notice period and effective billing date depend on actual regional rules.
5. Explain affected cohorts, customer notification/consent and expected loss-of-access behavior before executing. Never migrate all old cohorts by selecting an arbitrary timestamp.
6. Re-read results and verify the intended cohort policy. A catalog price change is not evidence that all existing renewals now use it.

## Offers, rental and tax configuration

| Configuration | Required decisions |
| --- | --- |
| One-time buy | Actual benefit, optional multi-quantity support and idempotent quantity-aware delivery. Do not enable legacy compatibility for new work. |
| One-time rent | ISO 8601 rental period and optional post-start expiration period, with actual entitlement start/end semantics. |
| Discount offer | Supported regional price/availability, start/end and redemption limit. Review zero/unset unlimited behavior before mutation. |
| Preorder offer | Start/end/release time and immutable supported price-change behavior for existing preorders. Do not grant released content before the contract permits it. |
| Game-reward offer | Actual currently supported reward-offer configuration and eligible client/program. Do not model it as a generic discount. |
| Subscription offer | Active parent plan, actual targeting, one or two ordered phases, phase duration/recurrence, corresponding regional prices and future-region policy. |
| Offer tags | At most twenty custom billing tags at supported product/option/plan/offer layers. They help client offer selection and are not searchable store tags. |
| Tax/compliance | Actual product tax category code, regional tax data, tokenized-digital-asset declaration, applicable regional product age ratings and EEA withdrawal classification where supported. Owner facts govern answers. |

Current subscription types expose configurable grace/account-hold periods, resubscribe behavior and proration. Apply their allowed duration/combined constraints rather than copying defaults from a different period or plan type. Installment commitments and renewal behavior need clear disclosure. More detailed field ownership is in [products and subscriptions](products-and-subscriptions.md).

Promo codes, app sales and other console-only promotion surfaces need their own actual eligibility, dates and redemption terms. A supported subscription/one-time offer API does not imply a general app-sale or promo-code endpoint.

## Commercial acceptance

Read back configuration and inspect real store/Billing results for the intended country/locale/test account. Test new sales, trial then full renewal, ineligible offers, disabled countries, restored purchases, multi-quantity/rental where used and preserved subscriber prices. Cover cancel/error/pending states without delivering unsupported access.

Record prices/currencies, region version, masks, IDs, activation states, dates, cohort decision and evidence. Report propagation delays and unexecuted production checks explicitly. Paid-download price changes and refunds are actual customer-facing actions, not harmless metadata cleanup.
