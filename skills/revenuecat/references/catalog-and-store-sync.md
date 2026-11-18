# Catalog architecture and store synchronization

## Model the graph explicitly

| Entity | Purpose | Common mistake |
| --- | --- | --- |
| Project | Shared customer/catalog boundary | Selecting a project by ambiguous display name |
| Store app | Exact bundle/package and credential connection | Using one app's key in another build |
| Store product | Purchasable SKU/plan identity | Confusing internal resource ID with store identifier |
| Entitlement | Access benefit such as `pro` | Creating one entitlement per billing interval unnecessarily |
| Offering | A presentation set of packages | Assuming an offering grants access by itself |
| Package | A logical purchase choice and linked products | Linking the wrong store or subscription plan |
| Paywall | UI and targeting attached to offering/presentation | Publishing a design with missing eligible products |

A monthly and annual subscription can unlock the same entitlement. A lifetime non-consumable can unlock that entitlement permanently if the product design intends it. A consumable credit pack should feed an idempotent balance ledger or supported virtual currency design, not grant an unlimited permanent feature accidentally.

## Sequence

1. Read the existing project, apps, products, entitlements, offerings, and packages. Build a desired-state mapping, preserving existing customers and store identifiers.
2. Establish each store's product/subscription group/base-plan structure through supported connected-store capabilities or the store API. App identity and legal agreements must already be ready.
3. Create/import/link RevenueCat products with the exact store identifiers and supported subscription-plan details. Read the product create/update schema. Do not guess whether `store_identifier` means a Play subscription product or the required composite/base-plan mapping for that SDK/model.
4. Create or reuse stable entitlement identifiers and attach the intended products. Read the graph back.
5. Create the offering and packages, choose standard package identifiers/types when appropriate, and link the correct eligible product for each supported store. Respect current per-store and eligibility constraints rather than attaching every monthly product indiscriminately.
6. Verify current/store availability, prices, locales, offer eligibility, entitlement attachments, and SDK-visible package results.
7. Publish/select the offering only at the requested launch stage. `set-current` affects customers and is not a harmless naming operation.

## Store desired-state plans

The current CLI exposes `rc products store plan`, `list`, `show`, `apply`, `discard`, and `screenshot`, plus interactive sync. Read the live schemas to construct the desired-state file. Store-state plans can be account-limited. If unavailable, use documented store APIs and ordinary RevenueCat product linking instead of pretending a plan was applied.

Create a plan with the selected app and input file, inspect the saved plan/diff with `show`, verify currencies/locales/availability/product types and customer impact, then apply only the intended approved change. `--yes` bypasses a CLI prompt, not authorization. Plan IDs allow review and application in separate processes. Re-read store/RevenueCat state after application and reconcile partial failures. A plan is not an atomic transaction spanning both stores.

`rc products push` and v2 product create-in-store capabilities can configure supported products when credentials and account capabilities permit. They do not upload a new application binary or guarantee product review. Upload Apple review screenshots through the documented store screenshot command/schema when available and retain review state separately.

Test Store/Web Billing price commands do not set arbitrary Apple/Google prices. Use the appropriate store-connected route and actual price-point/regional model. Never assume a USD float is sufficient for every currency and store.

## Verification and migrations

Use `rc offerings verify` to inspect the full graph/issues and `rc offerings preview` for the SDK-facing response where supported. Also perform an actual device SDK request and purchase. A structurally correct graph can still contain an unapproved, inactive, region-restricted, or mismatched store product.

For migrations, inventory existing customer IDs, aliases, product identifiers, receipt/token history, transfer policy, observer-mode requirements, backend access logic, and outstanding transactions. Follow the current migration guide for the chosen SDK and store. Reconcile access before switching a live app. Avoid two transaction owners, duplicate fulfillment, or accidental entitlement removal.

Archiving retains different semantics from deletion and store deactivation. Detaching a product can change access recognition. Identify current subscribers and intended effects before applying a customer-affecting catalog cleanup. Keep a sanitized mapping and recovery plan that can restore configuration without inventing or replaying charges.
