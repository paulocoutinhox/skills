---
name: revenuecat
description: Create and configure RevenueCat projects and store apps from scratch, connect credentials, map products to entitlements and offerings, publish localized paywalls, and verify SDK and purchase lifecycles through supported API/CLI workflows.
license: MIT
---

# RevenueCat

Build a correct relationship between a paid store transaction, an app identity and the customer's effective benefit. A configured product, visible paywall, successful sandbox purchase and live approved app are different states.

This is descriptive knowledge, not an execution package. Do not create API catalogs, synchronization scripts, paywall generators or automatic rule updates. Explain the supported native interfaces and the decisions the agent must make during an authorized task. Stored facts are revised only when the user requests maintenance.

## Brief, identity and ownership

Identify the source/framework, supported platforms, RevenueCat project/store-app IDs, actual bundle/package identities, store records, current SDKs and backend. Inspect existing resources before creating duplicates. Separate names, internal resource IDs and store product identifiers.

Collect the customer's authenticated ID policy, anonymous behavior, restore/transfer decision, paid benefits, products/plans, regions/prices/offers, offering structure, paywall audience/locales and publication endpoint. Use [the monetization brief](assets/monetization-brief.json) to record decisions.

RevenueCat is not the app storefront. It does not replace native compilation/signing, app screenshots/categories, initial Apple/Google app records, owner legal setup or binary review. Supported connected-store product creation is a narrower capability.

## Native CLI/API setup

Use an actual connected provider tool or the official installed CLI, after verifying identity and capability. Current installation options include the official `RevenueCat/tap/rc` formula and `@revenuecat/cli` package. Do not mistake another program named `rc` for this CLI.

Inspect `rc version`, `rc commands --json` and `rc schema <command path>`. CLI 0.1.7 schemas were inspected for the first-app workflow. Confirm the returned schema path and arguments because an unknown nested command can resolve to its parent. Live schemas decide experimental status and `requires_human`. Use explicit project/profile overrides. `--yes` skips a prompt, not authorization.

Authenticate through the supported owner-controlled flow. CI/server keys belong in the approved secret mechanism, not command history or client source. Distinguish public app SDK keys, secret v1 keys, scoped secret v2 keys, customer access tokens and store credentials.

Store setup assistants are human-required flows. In 0.1.7, `rc setup apple [app-id]` uses a RevenueCat app ID and Apple login/2FA. The inspected `rc setup google` instead uses Cloud project/developer/package flags and produces a service-account credential for a separate connection step. Prefer the documented app-update API when the owner already supplied credentials. Do not collect passwords or one-time codes in chat. See [credential connection and version differences](references/api-cli-and-setup.md#connect-existing-store-credentials).

Create/select the project and each exact store app. Configure the current required Apple/Google credential roles and validate them through supported checks. A successful credential check proves access for that check, not product approval or working purchase UI.

REST v2 uses `https://api.revenuecat.com/v2` with the appropriate scoped secret key or supported OAuth bearer token. REST v1 uses `https://api.revenuecat.com/v1` with per-operation public/secret key requirements. The new customer-authentication surface has its own token and beta eligibility. Do not apply one credential model to every route.

## First project and first platform apps

For a product absent from RevenueCat, follow this dependency order. The
[worked first-app setup](references/first-app-setup.md) gives native CLI examples, returned-ID handling,
credential payloads, a four-product mapping and restart/recovery checks.

1. Establish whether the account, project, RevenueCat platform connections or actual store records
   are missing. Authenticate the existing account when available. Creating an app connection does
   not create the store listing or prove legal enrollment.
2. List accessible projects/apps and reconcile matching bundle/package identities before creating.
   Create the missing project, then separate `app_store` and `play_store` apps in that project.
   Record returned resource IDs. Retrieve their automatically created public SDK keys.
3. Connect existing approved Apple subscription/API keys and Google service-account JSON through
   the documented app update. Read original credential paths and send contents through protected
   stdin. Record configured flags separately from effective permission and purchase tests.
4. Reconcile real store subscriptions/base plans and create only missing RevenueCat catalog records.
   Link all intended monthly/annual products to one stable paid-benefit entitlement. Preserve existing
   prices, regions and subscribers unless changing them is part of the request.
5. Create/reuse an offering and monthly/annual packages, each linked to the correct product for each
   store. Quote standard `$rc_...` package keys literally. Verify the graph before serving it.
6. Integrate platform public keys and the entitlement lookup key into the real app. Upload fonts and
   artwork, generate/edit the same paywall session, verify localizations, review the concrete design
   and publish within the authorized scope. Selecting the current offering is a separate transition.
7. Read SDK-facing offerings for both apps and present the native paywall with actual store prices.
   Run real sandbox/test-track purchase and restore scenarios when suitable accounts are available.
   Report configuration, native UI, transactions and public release as separate verified states.

Ordinary 0.1.7 JSON commands use a `data` envelope. `rc api` returns the API body directly. Inspect
before extracting IDs. On interruption, reuse confirmed remote resources instead of recreating the
project, rotating credentials or replacing a published paywall.

## Complete API/CLI domain map

| Domain | Native resource/command groups | Professional check |
| --- | --- | --- |
| Account scope | Authentication, profiles, projects, apps, keys and credential checks | Explicit project/app and least required access |
| Product catalog | Products, store push/plan/sync, prices, archive/restore | Store identity and actual regional price model |
| Access | Entitlements and attached products | Benefit ownership and existing customers |
| Presentation | Offerings, packages, current offering, verification/preview | Correct eligible store product per logical choice |
| Paywall | Draft/design/media/font/publish/attach and targeting capabilities | SDK/platform support and customer-visible transition |
| Customer | Identity/resources, access, purchases, subscriptions and transactions | Authentication, privacy, effective state and authorized action |
| Operations | Integrations/webhooks, virtual currency, discounts/audiences, metrics/charts, collaborators/IAM, audit/invoices | Capability, pagination, permissions and actual effect |
| v1 customer APIs | Customer/entitlement/offering/transaction operations | Exact key and endpoint semantics, SDK versus server role |

Consult the exact official method model before using a route. Updates are not uniformly PATCH. CLI names are not REST paths. Resolve pagination/cursors, request fields, permissions, environment and returned state. `rc api` is a native escape hatch only for a known supported contract, not permission to invent an endpoint.

Handle validation, identity/scope, capability, conflict and rate errors distinctly. Reconcile uncertain writes before replay. A refund, access grant/revoke, purchase transfer, deletion or price change affects customers and requires the actual task scope. See [API/setup detail](references/api-cli-and-setup.md).

## Model the catalog graph

| Entity | Responsibility | Example distinction |
| --- | --- | --- |
| Store app | Exact platform store connection | Apple bundle versus Android package |
| Product | Actual purchasable store identity/plan | Internal resource ID versus store SKU/base plan |
| Entitlement | Durable access benefit | `pro`, independent of monthly versus annual billing |
| Offering | Set of presented choices for an audience | Does not grant access on its own |
| Package | Logical purchase option linked to eligible products | Monthly choice needs correct product on each store |
| Paywall | Presentation attached to actual offering/targeting | A design draft is not a production publication |

A concrete design can have Apple monthly/annual subscriptions and their corresponding Play plans all unlocking one `pro` entitlement. The offering presents monthly and annual packages. If a genuine lifetime product exists, it can unlock the same benefit permanently by deliberate design. Consumable credits require a durable ledger or supported virtual-currency model, not unlimited permanent access by accident.

Choose one source of truth for every mapping. Record store identifier/base-plan details, internal product ID, entitlement, package and app. Verify that each package's platform/eligibility selection corresponds to what the SDK will actually return. Do not attach every same-duration product indiscriminately.

## Store synchronization and customer impact

Read existing store and RevenueCat state. Establish actual store group/base-plan/option/offer structure first, then create/import/link the exact products. Attach intended products to stable entitlements. Create packages/offerings and verify the graph before selecting a current offering.

Current native store-plan commands can persist a desired-state plan/diff, show it, apply or discard it. Some accounts may not expose that capability. Review changed type, IDs, localizations, currencies, availability, prices and existing subscriber effects before applying. Re-read both systems after partial failures. This is not an atomic transaction spanning two stores and RevenueCat.

Test Store/Web Billing price commands do not arbitrarily set Apple/Google prices. Creation/push to a connected store does not upload an app binary or guarantee product review. Archive, deletion, detachment and deactivation have different effects and must not be used as interchangeable cleanup commands.

Use supported offering verification/SDK preview plus an actual device request. An apparently complete graph can contain an inactive, unapproved or region-restricted product. [Catalog detail](references/catalog-and-store-sync.md) expands reconciliation and migrations.

## SDK lifecycle and platform support

Use the current supported SDK for the actual framework/deployment target. Check iOS/iPadOS, macOS, tvOS and visionOS separately. Core purchases and hosted paywall UI may have different availability. Do not stretch a phone paywall into a Mac/TV/spatial interface or assume a package's top-level platform list proves every UI product works there.

For native Apple integration, prefer the current documented Swift Package Manager distribution. Inspect the selected release rather than blindly copying a historical version. The researched guide notes CocoaPods publication changes in late 2026. For Android/cross-platform, check Billing compatibility, actual binding versions, lifecycle and platform minimums.

Configure once with the intended public app SDK key. Use stable opaque authenticated App User IDs, without email/phone/PII as identifiers. Define anonymous-to-login, logout, account switch, aliases, restore and purchase transfer before launch. App account and store account identity are distinct.

Fetch offerings/eligible packages, show accurate product information, start purchase from actual UI, distinguish canceled/pending/failed/verified outcomes, refresh CustomerInfo and observe supported updates. Represent unavailable offerings and stale/cache/offline state explicitly. Do not invent a free entitlement or fallback SKU when configuration is missing.

Standard RevenueCat integration owns transaction finishing/acknowledgment. Avoid a second independent StoreKit/Play processing owner. Observer/migration modes require an explicit tested responsibility split. Restore/manage actions must respect the selected identity/transfer policy.

## Effective entitlement and webhook model

| Event/state | Access decision |
| --- | --- |
| Verified purchase/renewal | Reconcile actual active benefit and effective dates |
| User cancellation | Usually stops future renewal, not necessarily current paid access |
| Grace/billing issue | Apply verified policy/state, not a generic inactive toggle |
| Expiration | Remove access when the authoritative period/state ends |
| Refund/revocation | Reconcile the actual early access/financial effect |
| Upgrade/downgrade/transfer | Reconcile new product/identity/effective dates |
| Consumable delivery | Persist a unique durable grant and avoid duplicate credit |

Protect backend customer reads/writes with app-user authorization. A public key or known customer ID is not permission to expose another person's purchase information. Never trust a client-provided entitlement-active flag for server access.

Verify the webhook integration's configured Authorization value and optional HMAC contract. Never downgrade a failed required check to another authentication mode. Handle TLS, secret comparison, replay, duplicate/out-of-order delivery, minimal logging and bounded processing. Treat events as evidence to reconcile authoritative state, not a sequence of blind boolean toggles.

If both client and webhook can grant a consumable, converge on one durable transaction-keyed ledger entry. Standard SDK completion can precede custom backend delivery. Recover from verified purchase records/webhooks rather than relying on an unfinished store transaction. For provider-managed in-app currency, do not add a second purchase credit. Application-owned completion is a separate explicit integration mode. See [SDK/lifecycle detail](references/sdk-and-lifecycle.md).

## Recover at the layer that failed

Keep account/scope, stored credentials, store product eligibility, catalog links, SDK-facing offering,
published presentation, native UI and verified transaction evidence separate. Reconcile partial writes
by returned IDs before retrying. Do not replace working keys or grant fake access to repair a blocked
billing environment. Use [the setup diagnosis table](references/testing-and-operations.md#diagnose-a-partial-setup-without-replacing-working-resources).
Store-to-RevenueCat notifications and RevenueCat-to-app webhooks are separate integrations. Record
actual configuration/delivery or the exact remaining prerequisite for the app's real architecture.

## Paywall communication and testing

Start with the audience's actual use case and value already demonstrated. Write a specific headline and a few supported benefits. Show store/SDK-localized price, billing period, trial/intro duration and eligibility, full renewal terms, restore/manage, privacy and terms. Never hardcode a stale regional price or label a paid conversion simply free.

Use proportional rights-cleared artwork, real UI evidence and readable editable localized type. Inspect font scaling, screen-reader order, remote/keyboard focus, contrast, RTL/expansion, safe areas and each supported layout. Publishing a paywall/current offering can affect existing clients without a binary release, so verify audience and authorization.

Define a real experiment hypothesis and metric. Purchase conversion must specify eligible audience/denominator. Pair it with refunds, cancellation and retention. Do not declare a small sample winner or optimize hidden terms. See [paywall detail](references/paywalls-and-marketing.md).

Test Store proves an early integration, local StoreKit proves another layer, and actual Apple/Google sandbox/test-track purchases prove store-backed behavior. None proves final production approval. Test every plan, key locale/region, account transition, restore, pending/interruption, trial, renewal, replacement, grace/expiry, refund and webhook replay. Do not run real charges merely to make a report look complete.

Deliver the complete mapping, credential status, SDK/platform versions, reviewed paywall/offering state, test evidence, webhook/reconciliation behavior and outstanding store actions. [Operations detail](references/testing-and-operations.md) provides the final evidence shape.

The provider's [quickstart](https://www.revenuecat.com/docs/getting-started/quickstart), [CLI reference](https://www.revenuecat.com/docs/tools/cli/commands), [API v2](https://www.revenuecat.com/docs/api-v2), [API v1](https://www.revenuecat.com/docs/api-v1) and [identity guidance](https://www.revenuecat.com/docs/customers/identifying-customers) govern their surfaces. Google SRE's [monitoring chapter](https://sre.google/sre-book/monitoring-distributed-systems/) is professional context for distinguishing system health from one successful request. Dunford's [positioning book](https://www.aprildunford.com/books) is relevant further reading, not a monetization guarantee. See [sources](references/sources.md) and [license](LICENSE.md).
