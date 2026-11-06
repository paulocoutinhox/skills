# Sources and API coverage

Verified baseline: **2026-11-05**. The installed official CLI **0.1.7** schemas were inspected for creation, credential setup, catalog links and paywall publication. Runtime schemas, store behavior and account capability checks remain necessary.

| Source | Use |
| --- | --- |
| [API reference index](https://www.revenuecat.com/docs/api-reference/llms.txt) | Resource enumeration for both API generations |
| [API v2](https://www.revenuecat.com/docs/api-v2) | Project/configuration/customer API and permissions |
| [API v1](https://www.revenuecat.com/docs/api-v1) | Customer, entitlement, offering and transaction API/authentication |
| [Per-resource OpenAPI example](https://www.revenuecat.com/docs/redocusaurus/openapi-v2-project.yaml) | Official resource contract inspected during research. Consult the relevant current resource document for an authorized API operation |
| [CLI commands](https://www.revenuecat.com/docs/tools/cli/commands) | Command groups, flags, human-required setup and store plans |
| [CLI setup](https://www.revenuecat.com/docs/tools/cli/setup) | Installation and authentication |
| [MCP tools](https://www.revenuecat.com/docs/tools/mcp/tools-reference) | Available connected tool capabilities and constraints |
| [Quickstart](https://www.revenuecat.com/docs/getting-started/quickstart) | Project/app/product/SDK integration sequence |
| [Entitlements](https://www.revenuecat.com/docs/getting-started/entitlements) | Access model and product attachments |
| [Offerings](https://www.revenuecat.com/docs/offerings/overview) | Package graph and client presentation |
| [SDK installation](https://www.revenuecat.com/docs/getting-started/installation) | Current framework/platform support and dependencies |
| [Apple SDK package manifest](https://github.com/RevenueCat/purchases-ios/blob/main/Package.swift) | Actual declared platform minimums and products, recheck the selected tagged release |
| [Customer identification](https://www.revenuecat.com/docs/customers/identifying-customers) | Anonymous IDs, login and identity behavior |
| [Webhooks](https://www.revenuecat.com/docs/integrations/webhooks) | Authorization, optional HMAC and retry timestamps. Rechecked on 2026-11-05. |
| [Making purchases](https://www.revenuecat.com/docs/getting-started/making-purchases) and [non-subscriptions](https://www.revenuecat.com/docs/platform-resources/non-subscriptions) | Automatic completion versus custom consumable delivery. Rechecked on 2026-11-05. |
| [Sandbox testing](https://www.revenuecat.com/docs/test-and-launch/sandbox) | Environment differences and real store-backed tests |
| [Paywalls](https://www.revenuecat.com/docs/tools/paywalls) | Paywall design and supported presentation surfaces |

Research checked per-resource references for v1 and v2 because an overview specification alone can omit operation paths. The durable deliverable is descriptive guidance in Markdown. No generated API catalog, synchronization program or self-updater is bundled. Actual endpoint documentation governs request fields and permissions.

Coverage does not imply universal account access. Store-state plans, some paywall capabilities, customer authentication beta endpoints, and store creation features may be gated. Store account signup, legal declarations, first app records, binary builds, and store review do not become fully unattended merely because RevenueCat can synchronize store products. Core purchase support and hosted paywall UI can have different platform matrices.

## Professional foundation and evidence scope

Reviewed for this revision: 2026-11-05. The [monitoring chapter of Site Reliability Engineering](https://sre.google/sre-book/monitoring-distributed-systems/) supplies professional reasoning about observed health. Dunford's [positioning book](https://www.aprildunford.com/books) is further reading, not subscription conversion evidence. The exact RevenueCat and store contracts govern credentials, purchase state and customer effects.

Stored content is maintained only when the user requests a revision. There is no automated source collector or refresh mechanism.

## First-app workflow evidence

Inspected on **2026-11-05**. The first-project/app, existing-credential connection, catalog and hosted
paywall workflow was exercised during an authorized app setup. Examples intentionally use fictitious
product identities and omit owner paths, project IDs and credentials. This authoring revision inspected
schemas and documentation without creating another live project or executing store transactions. No genuine
store-backed purchase/restoration is claimed from configuration or native UI checks.

| Source/surface | Consequential decision |
| --- | --- |
| Official `@revenuecat/cli@0.1.7`: `version`, `schema` for projects/apps/keys, products, entitlements, offerings/packages, fonts/media-assets and paywalls | Use actual native commands and record returned IDs. Schema `path` must match the intended command. Ordinary JSON results use an envelope, raw API results do not. |
| [Official CLI releases](https://github.com/RevenueCat/cli/releases) and [setup documentation](https://www.revenuecat.com/docs/tools/cli/setup) | Verify the executable/version and use owner-controlled authentication. A RevenueCat account, project and store app are distinct resources. |
| [Connect apps](https://www.revenuecat.com/docs/projects/connect-a-store) and [API keys](https://www.revenuecat.com/docs/projects/authentication) | Create separate platform connections and retrieve automatically supplied public SDK keys. Store connection is distinct from app publication. |
| [App OpenAPI contract](https://www.revenuecat.com/docs/redocusaurus/openapi-v2-app.yaml) | App update is POST. Apple key fields belong under `app_store`. Google credentials are an entire JSON document encoded as a string under `play_store`. Configured flags are response evidence, not purchase evidence. |
| [Apple purchase key](https://www.revenuecat.com/docs/service-credentials/itunesconnect-app-specific-shared-secret/in-app-purchase-key-configuration) and [management API key](https://www.revenuecat.com/docs/service-credentials/itunesconnect-app-specific-shared-secret/app-store-connect-api-key-configuration) | Keep the two credential roles separate. Purchase keys are required for the current Apple transaction integration. Management-key guidance specifies at least App Manager access. |
| [Google service credentials](https://www.revenuecat.com/docs/service-credentials/creating-play-service-credentials) | Verify Cloud/Play access and package recognition separately. Propagation delays do not justify repeated key creation. |
| 0.1.7 `schema setup google`, `schema setup apple` and `schema apps apple check` | The web reference's Google positional-app example differs from the inspected runtime flags and output. Use runtime Cloud/developer/package inputs and connect the produced credential separately. Apple check tests Apple login/key access. |
| 0.1.7 `schema paywalls generate`, `edit`, `publish`, `schema fonts upload`, and [displaying paywalls](https://www.revenuecat.com/docs/tools/paywalls/displaying-paywalls) | Preserve the editing session, upload actual assets, review the design before publication and inspect native rendering. CLI previews omit restore controls and can miss custom fonts. |

Keep these version-specific observations scoped to the inspected interface. Do not turn display names,
resource ID prefixes, sample prices or one emulator's billing failure into universal contracts. Reconcile
any later schema difference before applying a write. These notes document research and execution scope,
not an automatic refresh policy.

## Independent notification and recovery states

Checked **2026-11-05** against [Platform Server Notifications](https://www.revenuecat.com/docs/platform-resources/server-notifications),
[webhooks](https://www.revenuecat.com/docs/integrations/webhooks) and
[Play Billing testing](https://developer.android.com/google/play/billing/test). Store notifications,
application webhooks, client product fetches and transactions are separate checks. A serverless/local
app does not need an invented backend solely to fill a template. A test track alone does not prove
that purchases use non-charging test payment methods. The added diagnosis table explains evidence
boundaries without creating live customers, sending events or performing purchases during authoring.
