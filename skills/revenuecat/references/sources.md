# Sources and API coverage

Checked baseline: **2026-11-05**. The skill targets the official CLI **0.1.8**. Its schemas for creation, credential setup, catalog links and paywall publishing were checked at 0.1.7, and the 0.1.8 command sources were compared on the dates recorded below. You still need to check runtime schemas, store behavior and account capabilities.

| Source | Use |
| --- | --- |
| [API reference index](https://www.revenuecat.com/docs/api-reference/llms.txt) | List of resources for both API generations |
| [API v2](https://www.revenuecat.com/docs/api-v2) | Project, configuration and customer API and permissions |
| [API v1](https://www.revenuecat.com/docs/api-v1) | Customer, entitlement, offering and transaction API and authentication |
| [Per-resource OpenAPI example](https://www.revenuecat.com/docs/redocusaurus/openapi-v2-project.yaml) | Official resource contract checked during research. Read the current document for the resource before an allowed API operation |
| [CLI commands](https://www.revenuecat.com/docs/tools/cli/commands) | Command groups, flags, setup that needs a person and store plans |
| [CLI setup](https://www.revenuecat.com/docs/tools/cli/setup) | Installation and authentication |
| [MCP tools](https://www.revenuecat.com/docs/tools/mcp/tools-reference) | Available connected tool capabilities and limits |
| [Quickstart](https://www.revenuecat.com/docs/getting-started/quickstart) | Order of project, app, product and SDK integration |
| [Entitlements](https://www.revenuecat.com/docs/getting-started/entitlements) | Access model and product attachments |
| [Offerings](https://www.revenuecat.com/docs/offerings/overview) | Package setup and how the client shows it |
| [SDK installation](https://www.revenuecat.com/docs/getting-started/installation) | Current framework and platform support and dependencies |
| [Apple SDK package manifest](https://github.com/RevenueCat/purchases-ios/blob/main/Package.swift) | Real stated platform minimums and products. Check the chosen tagged release again |
| [Customer identification](https://www.revenuecat.com/docs/customers/identifying-customers) | Anonymous IDs, login and identity behavior |
| [Webhooks](https://www.revenuecat.com/docs/integrations/webhooks) | Authorization, optional HMAC and retry timestamps. Rechecked on 2026-11-05. |
| [Making purchases](https://www.revenuecat.com/docs/getting-started/making-purchases) and [non-subscriptions](https://www.revenuecat.com/docs/platform-resources/non-subscriptions) | Automatic completion versus custom consumable delivery. Rechecked on 2026-11-05. |
| [Sandbox testing](https://www.revenuecat.com/docs/test-and-launch/sandbox) | How environments differ and real store-backed tests |
| [Paywalls](https://www.revenuecat.com/docs/tools/paywalls) | Paywall design and supported ways to show it |

The research checked the per-resource references for v1 and v2, because an overview specification alone can leave out operation paths. The lasting deliverable is descriptive guidance in Markdown. No generated API catalog, sync program or self-updater is included. The real endpoint documentation decides request fields and permissions.

Coverage does not mean every account has access. Store-state plans, some paywall features, customer authentication beta endpoints, and store creation features may be limited. Store account signup, legal declarations, first app records, binary builds, and store review do not become fully automatic just because RevenueCat can sync store products. Core purchase support and hosted paywall UI can have different platform tables.

## Professional foundation and evidence scope

Reviewed on 2026-11-05. The [monitoring chapter of Site Reliability Engineering](https://sre.google/sre-book/monitoring-distributed-systems/) gives professional thinking about observed health. Dunford's [positioning book](https://www.aprildunford.com/books) is further reading, not evidence about subscription conversion. The exact RevenueCat and store contracts decide credentials, purchase state and effects on customers.

Stored content is updated only when the user asks for a revision. There is no automated source collector or refresh mechanism.

## First-app workflow evidence

Checked on **2026-11-05**. The first project and app, existing-credential connection, catalog and
hosted paywall workflow is based on an observed, allowed app setup. Examples use made-up product
identities on purpose and leave out owner paths, project IDs and credentials. The schema and
documentation checks did not create a live project or run store transactions. No real store-backed
purchase or restore is claimed from configuration or native UI checks.

| Source/surface | Important decision |
| --- | --- |
| Official `@revenuecat/cli@0.1.8`: `version`, `schema` for projects/apps/keys, products, entitlements, offerings/packages, fonts/media-assets and paywalls | Use the real native commands and record returned IDs. The schema `path` must match the intended command. Normal JSON results use an envelope, raw API results do not. |
| [Official CLI releases](https://github.com/RevenueCat/cli/releases) and [setup documentation](https://www.revenuecat.com/docs/tools/cli/setup) | Check the executable and version and use sign-in the owner controls. A RevenueCat account, project and store app are separate resources. |
| [Connect apps](https://www.revenuecat.com/docs/projects/connect-a-store) and [API keys](https://www.revenuecat.com/docs/projects/authentication) | Create separate platform connections and fetch the public SDK keys that are created automatically. Connecting a store is not publishing the app. |
| [App OpenAPI contract](https://www.revenuecat.com/docs/redocusaurus/openapi-v2-app.yaml) | App update is POST. Apple key fields go under `app_store`. Google credentials are a whole JSON document encoded as a string under `play_store`. Configured flags are evidence from the response, not evidence of a purchase. |
| [Apple purchase key](https://www.revenuecat.com/docs/service-credentials/itunesconnect-app-specific-shared-secret/in-app-purchase-key-configuration) and [management API key](https://www.revenuecat.com/docs/service-credentials/itunesconnect-app-specific-shared-secret/app-store-connect-api-key-configuration) | Keep the two credential roles apart. Purchase keys are required for the current Apple transaction integration. The management-key guidance says at least App Manager access. |
| [Google service credentials](https://www.revenuecat.com/docs/service-credentials/creating-play-service-credentials) | Check Cloud and Play access and package recognition separately. Delays while changes spread do not justify creating keys again and again. |
| `schema setup google`, `schema setup apple` and `schema apps apple check` | Schema argument hints come from usage strings, so the Google schema leaves out the optional RevenueCat app ID that the command accepts. Apple check tests Apple login and key access. |
| `schema paywalls generate`, `edit`, `publish`, `schema fonts upload`, and [displaying paywalls](https://www.revenuecat.com/docs/tools/paywalls/displaying-paywalls) | Keep the editing session, upload real assets, review the design before publishing and check native rendering. CLI previews leave out restore controls and can miss custom fonts. |

Keep these version-specific notes limited to the interface that was checked. Do not turn display
names, resource ID prefixes, sample prices or one emulator's billing failure into rules for every
case. Look into any later schema difference before applying a write. These notes record the research
and what was run, not an automatic refresh policy.

## Independent notification and recovery states

Checked **2026-11-05** against [Platform Server Notifications](https://www.revenuecat.com/docs/platform-resources/server-notifications),
[webhooks](https://www.revenuecat.com/docs/integrations/webhooks) and
[Play Billing testing](https://developer.android.com/google/play/billing/test). Store notifications,
app webhooks, client product fetches and transactions are separate checks. A serverless or local
app does not need a made-up backend just to fill a template. A test track alone does not prove that
purchases use test payment methods that do not charge. The diagnosis table explains where each kind
of evidence stops. These checks did not create live customers, send events or make purchases.

## Recheck on 2026-11-18

- [CLI setup](https://www.revenuecat.com/docs/tools/cli/setup): Homebrew `RevenueCat/tap/rc`, npm `@revenuecat/cli`, `npx @revenuecat/cli <command>` and release binaries. The same binary runs as `rc` and `revenuecat`. `rc auth login`, `rc auth signup` and the `RC_API_KEY` v2 secret for CI are still documented.
- [Webhooks](https://www.revenuecat.com/docs/integrations/webhooks): optional HMAC signing for each integration uses `X-RevenueCat-Webhook-Signature` with `t=<unix timestamp>,v1=<hex HMAC-SHA256>` over `<t>.<raw body>`. Retries compute `t`/`v1` again while keeping the event `id` and `event_timestamp_ms`. The authorization header is still a separate optional check.
- The rule for customer-facing paywall copy (no description of how it was made and no AI or tool mentions) is the owner's content rule, not a RevenueCat requirement.
- [Installation](https://www.revenuecat.com/docs/getting-started/installation): CocoaPods trunk becomes read-only on December 2, 2026 and stops accepting new releases, so native SDK updates need Swift Package Manager.
- [Official CLI source](https://github.com/RevenueCat/cli) at tags `v0.1.7` and `v0.1.8`: `rc setup google` accepts an optional RevenueCat Play app ID (`cobra.MaximumNArgs(1)`) although `rc schema` builds argument hints only from the usage string `google`. It uploads the new key through the v2 app update and reports `credential_uploaded`, falls back to writing `--key-out`, and removes older service-account keys unless `--keep-old-keys` is set. `rc apps apple check` makes read-only Apple key-management requests and changes no RevenueCat app. `rc api` paths are relative to the v2 root. Image uploads are capped at 2 MiB and fonts at 5 MiB. The projects, apps, products, entitlements, offerings and packages command flags used in the first-app workflow are the same in 0.1.8, released on 2026-11-13.

## Recheck on 2026-11-24

- [Official CLI comparison](https://github.com/RevenueCat/cli/compare/v0.1.7...v0.1.8) of tags `v0.1.7` and `v0.1.8`: the `fonts` and `media-assets` command sources are the same. `paywalls generate`, `edit` and `publish` keep their flags, including `edit --session` and `--base-url`. In 0.1.8, `paywalls edit` names `--session` in its usage string and removes old preview images from the session directory.
