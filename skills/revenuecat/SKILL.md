---
name: revenuecat
description: Create and configure RevenueCat projects and store apps from scratch, connect credentials, map products to entitlements and offerings, publish localized paywalls, and check SDK and purchase lifecycles through supported API/CLI workflows.
license: MIT
---

# RevenueCat

Build a correct link between a paid store transaction, an app identity and the benefit the customer really gets. A configured product, a visible paywall, a successful sandbox purchase and a live approved app are different states.

This is descriptive knowledge, not a package that runs things. Do not create API catalogs, sync scripts, paywall generators or automatic rule updates. Explain the supported native tools and the decisions the agent must make during an allowed task. Stored facts change only when the user asks for maintenance.

## Brief, identity and ownership

Find the source and framework, supported platforms, RevenueCat project and store-app IDs, real bundle and package identities, store records, current SDKs and backend. Check existing resources before you create duplicates. Keep names, internal resource IDs and store product identifiers apart.

Collect the customer's signed-in ID policy, anonymous behavior, restore and transfer decision, paid benefits, products and plans, regions, prices and offers, offering structure, paywall audience and locales, and the last allowed step. Use [the monetization brief](assets/monetization-brief.json) to record decisions. Record the last allowed step as the brief's `authorized-endpoint` (`prepare`, catalog configuration, paywall publication, current-offering selection or customer operation) in its `authorized-endpoint` field. Do the steps needed inside that endpoint, then stop and report the next change customers would see instead of making it.

RevenueCat is not the app store. It does not replace native building and signing, app screenshots and categories, the first Apple or Google app records, the owner's legal setup or binary review. Creating products in a connected store is a narrower, supported feature.

## Native CLI/API setup

Use a real connected provider tool or the official installed CLI, after checking identity and capability. Current install options include the official `RevenueCat/tap/rc` formula and the `@revenuecat/cli` package. Do not confuse another program named `rc` with this CLI.

Run `rc version`, `rc commands --json` and `rc schema <command path>`. The first-app workflow targets CLI 0.1.8. Confirm the returned schema path and arguments, because an unknown nested command can resolve to its parent. Live schemas decide experimental status and `requires_human`. Use explicit project and profile overrides. `--yes` skips a prompt. It does not give permission.

Sign in through the supported flow the owner controls. CI and server keys belong in the approved secret store, not in command history or client source. Keep public app SDK keys, secret v1 keys, scoped secret v2 keys, customer access tokens and store credentials apart.

Store setup assistants need a person. In 0.1.8, `rc setup apple [app-id]` uses a RevenueCat app ID and Apple login/2FA. `rc setup google` takes Cloud project, developer and package flags plus an optional RevenueCat Play app ID that its schema does not list. It uploads the new service-account key to that app, or writes it to `--key-out` when the upload fails, and removes older keys unless `--keep-old-keys` is set. Prefer the documented app-update API when the owner has already given credentials. Do not collect passwords or one-time codes in chat. See [credential connection and CLI contract](references/api-cli-and-setup.md#connect-existing-store-credentials).

Create or select the project and each exact store app. Set the current required Apple and Google credential roles and check them with the supported checks. A passing credential check proves access for that check only. It does not prove product approval or a working purchase UI.

REST v2 uses `https://api.revenuecat.com/v2` with the right scoped secret key or a supported OAuth bearer token. REST v1 uses `https://api.revenuecat.com/v1`, and each operation needs its own public or secret key. The new customer-authentication API has its own token and beta eligibility. Do not use one credential model for every route.

## First project and first platform apps

For a product that is not in RevenueCat yet, follow this order. The
[worked first-app setup](references/first-app-setup.md) gives native CLI examples, how to handle
returned IDs, credential payloads, a four-product mapping and checks for restarting and recovery.

1. Find out whether the account, project, RevenueCat platform connections or real store records are
   missing. Sign in to the existing account when there is one. Creating an app connection does not
   create the store listing or prove legal enrollment.
2. List the projects and apps you can reach and match bundle and package identities before creating
   anything. Create the missing project, then separate `app_store` and `play_store` apps in that
   project. Record the returned resource IDs. Get their public SDK keys, which are created
   automatically.
3. Connect existing approved Apple subscription/API keys and Google service-account JSON through the
   documented app update. Read the original credential paths and send the contents through protected
   stdin. Record the configured flags apart from real permission and purchase tests.
4. Match up the real store subscriptions and base plans and create only the RevenueCat catalog
   records that are missing. Link all intended monthly and annual products to one stable paid-benefit
   entitlement. Keep existing prices, regions and subscribers unless the request is to change them.
5. Create or reuse an offering and monthly and annual packages, each linked to the correct product
   for each store. Quote standard `$rc_...` package keys exactly. Check the whole setup before serving
   it.
6. Add the platform public keys and the entitlement lookup key to the real app. Upload fonts and
   artwork, generate and edit in the same paywall session, check localizations, review the concrete
   design and publish within the allowed scope. Selecting the current offering is a separate step.
7. Read the offerings the SDK sees for both apps and show the native paywall with real store prices.
   Run real sandbox or test-track purchase and restore cases when suitable accounts are available.
   Report configuration, native UI, transactions and public release as separate checked states.

Normal 0.1.8 JSON commands wrap results in a `data` envelope. `rc api` returns the API body
directly. Look at the output before you pull out IDs. After an interruption, reuse confirmed remote
resources instead of recreating the project, rotating credentials or replacing a published paywall.

## Complete API/CLI domain map

| Domain | Native resource/command groups | Professional check |
| --- | --- | --- |
| Account scope | Authentication, profiles, projects, apps, keys and credential checks | Clear project and app and the least access needed |
| Product catalog | Products, store push/plan/sync, prices, archive/restore | Store identity and the real regional price model |
| Access | Entitlements and attached products | Who owns the benefit, and existing customers |
| Presentation | Offerings, packages, current offering, verification/preview | Correct eligible store product for each choice |
| Paywall | Draft/design/media/font/publish/attach and targeting capabilities | SDK and platform support and the change customers see |
| Customer | Identity/resources, access, purchases, subscriptions and transactions | Authentication, privacy, real state and allowed action |
| Operations | Integrations/webhooks, virtual currency, discounts/audiences, metrics/charts, collaborators/IAM, audit/invoices | Capability, pagination, permissions and real effect |
| v1 customer APIs | Customer/entitlement/offering/transaction operations | Exact key and endpoint meaning, SDK versus server role |

Read the exact official method model before you use a route. Updates are not always PATCH. CLI names are not REST paths. Work out pagination and cursors, request fields, permissions, environment and returned state. `rc api` is a native way around missing commands, only for a known supported contract. It does not allow making up an endpoint.

Handle validation, identity and scope, capability, conflict and rate errors each in their own way. When a write might or might not have worked, check before you replay it. A refund, access grant or revoke, purchase transfer, deletion or price change affects customers and needs the real task scope. See [API/setup detail](references/api-cli-and-setup.md).

## Model the catalog graph

| Entity | Responsibility | Example distinction |
| --- | --- | --- |
| Store app | The exact connection to one platform store | Apple bundle versus Android package |
| Product | The real store identity or plan that can be bought | Internal resource ID versus store SKU/base plan |
| Entitlement | The lasting benefit the customer has access to | `pro`, the same for monthly and annual billing |
| Offering | Set of choices shown to an audience | Does not grant access by itself |
| Package | A purchase option linked to eligible products | A monthly choice needs the correct product on each store |
| Paywall | The screen attached to a real offering or targeting rule | A design draft is not a production release |

A concrete design can have Apple monthly and annual subscriptions and their matching Play plans all unlock one `pro` entitlement. The offering shows monthly and annual packages. If a real lifetime product exists, it can unlock the same benefit for good, by design. Consumable credits need a lasting ledger or the supported virtual-currency model, not unlimited permanent access by accident.

Choose one source of truth for every mapping. Record the store identifier and base-plan details, internal product ID, entitlement, package and app. Check that each package's platform and eligibility choice matches what the SDK will really return. Do not attach every product with the same length without thinking.

## Store synchronization and customer impact

Read the existing store and RevenueCat state. Work out the real store group, base plan, option and offer structure first, then create, import or link the exact products. Attach the intended products to stable entitlements. Create packages and offerings and check the setup before you select a current offering.

Current native store-plan commands can save a desired-state plan or diff, show it, apply it or discard it. Some accounts may not have that feature. Review changes to type, IDs, localizations, currencies, availability, prices and effects on existing subscribers before applying. Read both systems again after a partial failure. This is not a single all-or-nothing transaction across two stores and RevenueCat.

Test Store and Web Billing price commands do not set Apple or Google prices at will. Creating or pushing to a connected store does not upload an app binary or promise product review. Archive, deletion, detach and deactivation each have different effects. Do not use them as if they were the same cleanup command.

Use supported offering checks and SDK preview, plus a real device request. A setup that looks complete can still hold an inactive, unapproved or region-limited product. [Catalog detail](references/catalog-and-store-sync.md) explains matching up and migrations in more depth.

## SDK lifecycle and platform support

Use the current supported SDK for the real framework and deployment target. Check iOS/iPadOS, macOS, tvOS and visionOS one by one. Core purchases and hosted paywall UI may be available in different places. Do not stretch a phone paywall into a Mac, TV or spatial interface, or assume a package's top-level platform list proves every UI product works there.

For native Apple integration, use the documented Swift Package Manager distribution. Check the chosen release instead of copying an old version number. RevenueCat's installation guide says CocoaPods trunk becomes read-only on December 2, 2026, so later native SDK releases need SPM. For Android and cross-platform, check Billing compatibility, real binding versions, lifecycle and platform minimums.

Configure once with the intended public app SDK key. Use stable, opaque, signed-in App User IDs, without email, phone or other PII as identifiers. Decide anonymous-to-login, logout, account switch, aliases, restore and purchase transfer before launch. The app account and the store account are different identities.

Fetch offerings and eligible packages, show accurate product information, start the purchase from the real UI, tell apart cancelled, pending, failed and verified results, refresh CustomerInfo and listen for supported updates. Show unavailable offerings and stale, cached or offline state clearly. Do not make up a free entitlement or a fallback SKU when setup is missing.

A standard RevenueCat setup owns finishing and acknowledging transactions. Avoid a second, separate StoreKit or Play processing owner. App-owned purchase completion needs a clear, tested split of who does what. Restore and manage actions must follow the chosen identity and transfer policy.

## Effective entitlement and webhook model

| Event/state | Access decision |
| --- | --- |
| Verified purchase/renewal | Match up the real active benefit and its dates |
| User cancellation | Usually stops future renewal, but not always current paid access |
| Grace/billing issue | Apply the checked policy and state, not a generic inactive switch |
| Expiration | Remove access when the period or state from the source of truth ends |
| Refund/revocation | Match up the real early loss of access and the money effect |
| Upgrade/downgrade/transfer | Match up the new product, identity and dates |
| Consumable delivery | Save a unique, lasting grant and avoid duplicate credit |

Protect backend customer reads and writes with app-user authorization. A public key or a known customer ID is not permission to show another person's purchase information. Never trust an entitlement-active flag sent by the client for server access.

Check the webhook integration's configured Authorization value and the optional HMAC contract. Never fall back to a weaker authentication mode when a required check fails. Handle TLS, secret comparison, replay, duplicate and out-of-order delivery, minimal logging and time-limited processing. Treat events as evidence to check against the source of truth, not as a series of blind on/off switches.

If both the client and a webhook can grant a consumable, end up with one lasting ledger entry keyed by transaction. Standard SDK completion can happen before custom backend delivery. Recover from verified purchase records or webhooks instead of relying on an unfinished store transaction. For provider-managed in-app currency, do not add a second purchase credit. App-owned completion is a separate integration mode you choose on purpose. See [SDK/lifecycle detail](references/sdk-and-lifecycle.md).

## Recover at the layer that failed

Keep account and scope, stored credentials, store product eligibility, catalog links, the offering
the SDK sees, the published screen, native UI and verified transaction evidence separate. Match up
partial writes by returned IDs before retrying. Do not replace working keys or grant fake access to
fix a blocked billing environment. Use [the setup diagnosis table](references/testing-and-operations.md#diagnose-a-partial-setup-without-replacing-working-resources).
Store-to-RevenueCat notifications and RevenueCat-to-app webhooks are separate integrations. Record
the real configuration and delivery, or the exact step still missing, for the app's real design.

## Paywall communication and testing

Start with the audience's real use case and the value the app has already shown. Write a specific headline and a few benefits you can back up. Show the store or SDK localized price, billing period, trial or intro length and eligibility, full renewal terms, restore and manage, privacy and terms. Never hardcode an old regional price or call a paid conversion simply free.

Paywall headlines, benefits, package labels and product display names are product content customers see. Generation prompts and context are internal instructions, not copy. The published text must never describe how it was made or mention AI, agents, tools or prompts unless the owner clearly asks. A required disclosure belongs in the store or privacy declaration that owns it, not in paywall copy.

Use artwork in proportion with cleared rights, real UI evidence and readable, editable localized type. Check font scaling, screen-reader order, remote and keyboard focus, contrast, RTL and text growth, safe areas and each supported layout. Publishing a paywall or current offering can change existing apps without a binary release, so check the audience and permission.

Define a real experiment hypothesis and metric. Purchase conversion must state the eligible audience and denominator. Pair it with refunds, cancellation and retention. Do not call a small sample a winner or optimize terms people cannot see. See [paywall detail](references/paywalls-and-marketing.md).

Test Store proves an early integration, local StoreKit proves another layer, and real Apple or Google sandbox and test-track purchases prove store-backed behavior. None of them proves final production approval. Test every plan, key locale and region, account change, restore, pending and interruption, trial, renewal, replacement, grace and expiry, refund and webhook replay. Do not make real charges just to make a report look complete.

Deliver the full mapping, credential status, SDK and platform versions, reviewed paywall and offering state, test evidence, webhook and matching behavior and store actions still left. [Operations detail](references/testing-and-operations.md) gives the final evidence shape.

The provider's [quickstart](https://www.revenuecat.com/docs/getting-started/quickstart), [CLI reference](https://www.revenuecat.com/docs/tools/cli/commands), [API v2](https://www.revenuecat.com/docs/api-v2), [API v1](https://www.revenuecat.com/docs/api-v1) and [identity guidance](https://www.revenuecat.com/docs/customers/identifying-customers) decide how their own tools work. Google SRE's [monitoring chapter](https://sre.google/sre-book/monitoring-distributed-systems/) gives professional background on telling system health apart from one successful request. Dunford's [positioning book](https://www.aprildunford.com/books) is useful further reading, not a promise of revenue. See [sources](references/sources.md) and [license](LICENSE.md).
