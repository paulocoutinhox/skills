# API and bootstrap

Verified baseline: 2026-11-05. This is descriptive API guidance. Stored facts are revised only on the user's request. An actual provider operation still requires its applicable official contract and account state.

## Account and app identity

Confirm an active developer membership, correct organization/team, appropriate role and app access, paid-app agreements where needed, banking/tax status, and legal distribution authority. Enrollment, identity verification, agreement signatures, banking, tax, and trader attestations are owner actions. A signing certificate, App Store Connect API key, and In-App Purchase server key serve different purposes.

Choose stable reverse-domain bundle IDs, app name, SKU, primary language, target platforms, and purchase-sharing strategy before creating records. SKU is an internal immutable identifier. The numeric App Store app ID is a provider result, not the bundle ID. Avoid accidentally creating another app when an existing record is merely inaccessible to the selected key.

Provisioning API resources cover bundle IDs, capabilities, certificates, devices, and profiles. Search `bundleIds`, `bundleIdCapabilities`, `certificates`, `profiles`, and `devices`. Match distribution type, team, bundle ID, app extensions, entitlements, and platform. Never enable all capabilities speculatively.

The researched `/v1/apps` collection supports GET, not POST. Create the initial app record through App Store Connect's **Apps → New App** using the prepared values, then retrieve it by bundle ID. Add selected platforms in the existing app record when supported. Do not mistake `/v1/appStoreVersions` creation for initial app creation.

## Authentication

API base: `https://api.appstoreconnect.apple.com`. Team API keys use ES256 JWTs with the key ID in `kid`, issuer ID in `iss`, `aud: appstoreconnect-v1`, and a short `exp`. Use a maintained JWT library and the current Apple token guide. A conservative ordinary request token lasts at most 20 minutes. Individual keys use a different documented claim profile. Do not blindly apply team claims to individual keys or reuse a Connect JWT as an App Store Server API token.

| JWT part | Team key | Individual key |
| --- | --- | --- |
| Header | `alg: ES256`, actual `kid`, `typ: JWT` | Same header with its own key ID |
| Identity claim | Actual issuer UUID in `iss` | `sub: user`, omit `iss` |
| Time claims | `iat` and `exp` as Unix epoch seconds | Same time representation |
| Audience | `aud: appstoreconnect-v1` | Same audience |
| Optional restricted scope | Documented matching GET request strings | Same documented scope mechanism |

Generate with the private key matching `kid`, refresh expired tokens, and check both lifetime and clock skew. The guide has special long-lived scoped GET exceptions for selected safe resources. Use short-lived tokens for release automation rather than generalizing those exceptions to writes.

Store `.p8` material in the approved secret manager or temporary keychain-supported credential location. Use `Authorization: Bearer <token>`, `Content-Type: application/json`, TLS, and a correctly synchronized clock. Never print tokens or put them into a committed curl example. Disable shell tracing before handling secrets. Grant the lowest role that supports the actual release operations and app access.

## Read the official request contract

Use the official App Store Connect method reference for the selected resource. Read method/path, path/query/header parameters, request media types, required fields, relationships, response contracts, enums and applicable security. Resolve nested models before constructing a payload. This skill does not maintain a generated schema dump or query program.

1. Search the resource name.
2. Select the exact nondeprecated operation.
3. Read every path/query parameter, its required flag, allowed filters, sorting, fields, and page size.
4. Resolve the request schema and construct the actual JSON:API `data.type`, attributes, relationships, and related resource identifiers. A relationship ID is not a display name or a product ID unless specified.
5. Read success and error contracts. Execute the minimal request.
6. Follow `links.next` until complete. Keep the same scoped filters. Re-read the resulting resource and verify relationships and processing state.

JSON:API updates use PATCH when that operation exists. Never infer supported updates from a create model. Use relationship endpoints for the documented linkage operation. Read-only, nullable, omitted, empty, and deleted are distinct states.

## Resource map

| Task | Official API resource families | Important ordering |
| --- | --- | --- |
| Team and signing | `users`, `userInvitations`, `bundleIds`, `certificates`, `profiles`, `devices` | Identity and role before mutation |
| App information | `apps`, `appInfos`, `appInfoLocalizations`, `appCategories`, `appTags` | App record before localized app information |
| Versions and binaries | `appStoreVersions`, `builds`, `buildUploads`, `buildUploadFiles`, `preReleaseVersions` | Upload, processing, then select compatible build |
| Listing media | `appStoreVersionLocalizations`, `appAssetLibraries`, `appAssetLibraryImages`, `appAssetLibraryVideos`, `appAssetLibraryRefData`, `appAssetLibraryPlacements`, `appAssetLibraryPlacementOrderingRequests` | Discover specifications, reserve/upload/commit, verify, place and order |
| Compliance | `ageRatingDeclarations`, `appEncryptionDeclarations`, `accessibilityDeclarations` | Truth from implementation and owner |
| Review and release | `appStoreReviewDetails`, `reviewSubmissions`, `reviewSubmissionItems`, `appStoreVersionReleaseRequests`, `appStoreVersionPhasedReleases` | Resolve all blocking states before submission/release |
| Prices and availability | `appPriceSchedules`, `appPricePoints`, `appAvailabilities`, `territoryAvailabilities`, `territories` | Select base territory, preserve schedules and use current v2 availability |
| Purchases | `inAppPurchases`, `inAppPurchaseVersions`, `inAppPurchasePriceSchedules`, `inAppPurchaseAvailabilities` | Parent product before draft version and submission |
| Subscriptions | `subscriptionGroups`, `subscriptions`, `subscriptionVersions`, `subscriptionGroupVersions`, `subscriptionPrices`, `subscriptionIntroductoryOffers`, `subscriptionOfferCodes`, `winBackOffers` | Group, product, version, plan/price, localization, review |
| Beta and diagnostics | `betaGroups`, `betaTesters`, `betaAppReviewDetails`, `betaAppReviewSubmissions`, `betaFeedbackCrashSubmissions`, `betaFeedbackScreenshotSubmissions`, `diagnosticSignatures` | App access and beta review precede external distribution |
| Store optimization | `appCustomProductPages`, `appStoreVersionExperiments`, `appEvents`, `nominations` | Feature eligibility and platform-specific assets |
| Games and reporting | `gameCenter*` and `analyticsReport*` families, `salesReports`, `financeReports` | Resource-specific roles, version/release graphs and report availability |
| Extended administration | [Full functional coverage](api-coverage.md) | Explicit routes for testing, optimization, retention, App Clips, games, hosted assets, alternative distribution, Xcode Cloud, SCM, signing, reviews and webhooks |

The table routes the documented functional domains. The official API reference also covers specialized features beyond a normal release. App Store Server API and notification formats are separate contracts. Use those actual contracts for direct transaction verification, rather than inventing them from Connect resources.

## Uploads, errors, and resumability

For reserved assets, POST the actual resource with filename, exact byte size and parent/category fields. Execute each returned upload operation using its exact method, URL, headers, byte offset and length. Split bytes correctly. Do not attach Apple authorization to another upload host. For current Asset Library images/videos, commit with `uploaded: true` and no checksum field, then poll resource state. Dedicated review attachments and other asset resources have their own documented checksum/delivery contract. Read [the media procedure](screenshots-and-media.md) instead of applying one old upload schema universally. Store IDs before continuing.

Handle 401 by checking token profile, time, and key status. Handle 403 by checking role, agreements, app access, and feature eligibility. Handle 404 by checking team, ID type, and actual existence. Inspect JSON:API error codes and source pointers for 409/422. Respect 429, `Retry-After` when supplied, and bounded exponential retry for transient service failures. Never retry an uncertain create blindly. Reconcile by known identifiers and state first.

Write a sanitized operation journal with method, resource ID, payload hash, timestamp, response status, and next action. Resume from confirmed remote state. Local generated files do not prove the corresponding remote changes happened.
