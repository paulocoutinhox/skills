# Catalog architecture and store synchronization

## Model the graph explicitly

| Entity | Purpose | Common mistake |
| --- | --- | --- |
| Project | Shared boundary for customers and catalog | Picking a project by a display name that could mean more than one |
| Store app | Exact bundle or package and credential connection | Using one app's key in another build |
| Store product | The SKU or plan identity that can be bought | Confusing the internal resource ID with the store identifier |
| Entitlement | An access benefit such as `pro` | Creating one entitlement per billing period without need |
| Offering | A set of packages to show | Assuming an offering grants access by itself |
| Package | A purchase choice and its linked products | Linking the wrong store or subscription plan |
| Paywall | UI and targeting attached to an offering or presentation | Publishing a design that is missing eligible products |

A monthly and an annual subscription can unlock the same entitlement. A lifetime non-consumable can unlock that entitlement for good if the product design means it to. A consumable credit pack should feed a balance ledger that is safe to repeat, or the supported virtual currency design. It should not grant an unlimited permanent feature by accident.

## Sequence

1. Read the existing project, apps, products, entitlements, offerings, and packages. Build a desired-state mapping that keeps existing customers and store identifiers.
2. Set up each store's product, subscription group and base-plan structure through supported connected-store features or the store API. App identity and legal agreements must already be ready.
3. Create, import or link RevenueCat products with the exact store identifiers and supported subscription-plan details. Read the product create and update schema. Do not guess whether `store_identifier` means a Play subscription product or the combined base-plan mapping that the SDK or model needs.
4. Create or reuse stable entitlement identifiers and attach the intended products. Read the setup back.
5. Create the offering and packages, choose standard package identifiers and types when they fit, and link the correct eligible product for each supported store. Follow the current per-store and eligibility limits instead of attaching every monthly product without thinking.
6. Check current and store availability, prices, locales, offer eligibility, entitlement attachments, and the package results the SDK sees.
7. Publish or select the offering only at the requested launch stage. `set-current` affects customers and is not a harmless naming step.

## Store desired-state plans

The current CLI has `rc products store plan`, `list`, `show`, `apply`, `discard`, and `screenshot`, plus interactive sync. Read the live schemas to build the desired-state file. Store-state plans may be limited to some accounts. If they are not available, use the documented store APIs and normal RevenueCat product linking. Do not pretend a plan was applied.

Create a plan with the chosen app and input file, check the saved plan or diff with `show`, check currencies, locales, availability, product types and the effect on customers, then apply only the intended approved change. `--yes` skips a CLI prompt. It does not give permission. Plan IDs let you review and apply in separate processes. Read the store and RevenueCat state again after applying and fix any partial failures. A plan is not one all-or-nothing transaction across both stores.

`rc products push` and the v2 create-in-store product features can set up supported products when credentials and account features allow. They do not upload a new app binary or promise product review. Upload Apple review screenshots through the documented store screenshot command or schema when available, and track review state separately.

Test Store and Web Billing price commands do not set Apple or Google prices at will. Use the right store-connected route and the real price-point and regional model. Never assume a USD float is enough for every currency and store.

## Verification and migrations

Use `rc offerings verify` to check the whole setup and its issues, and `rc offerings preview` for the response the SDK sees where supported. Also make a real device SDK request and purchase. A setup that is built correctly can still hold an unapproved, inactive, region-limited, or mismatched store product.

For migrations, list existing customer IDs, aliases, product identifiers, receipt and token history, transfer policy, app-owned completion needs, backend access logic, and transactions still in progress. Follow the current migration guide for the chosen SDK and store. Match up access before switching a live app. Avoid two transaction owners, double delivery, or removing an entitlement by accident.

Archiving means something different from deletion and store deactivation. Detaching a product can change whether access is recognized. Find the current subscribers and intended effects before running a catalog cleanup that affects customers. Keep a cleaned mapping and a recovery plan that can restore the setup without making up or replaying charges.
