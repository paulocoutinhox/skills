# API and bootstrap

Checked baseline: 2026-11-05. This is descriptive API guidance. Stored facts change only when the user asks. A real provider operation still needs its official contract and the right account state.

## Account and app identity

Confirm an active developer membership, the correct organization or team, a suitable role and app access, paid-app agreements where needed, banking and tax status, and the legal right to distribute. Enrollment, identity checks, signing agreements, banking, tax, and trader statements are owner actions. A signing certificate, an App Store Connect API key, and an In-App Purchase server key each do a different job.

Choose stable reverse-domain bundle IDs, app name, SKU, primary language, target platforms, and how purchases are shared before creating records. The SKU is an internal identifier that cannot change. The numeric App Store app ID comes from the provider. It is not the bundle ID. Avoid creating another app by mistake when an existing record is simply not visible to the chosen key.

Provisioning API resources cover bundle IDs, capabilities, certificates, devices, and profiles. Search `bundleIds`, `bundleIdCapabilities`, `certificates`, `profiles`, and `devices`. Match distribution type, team, bundle ID, app extensions, entitlements, and platform. Never turn on all capabilities just in case.

The researched `/v1/apps` collection supports GET, not POST. Create the first app record in App Store Connect under **Apps → New App** with the prepared values, then find it by bundle ID. Add chosen platforms to the existing app record when supported. Do not confuse creating `/v1/appStoreVersions` with creating the app.

## Authentication

API base: `https://api.appstoreconnect.apple.com`. Team API keys use ES256 JWTs with the key ID in `kid`, issuer ID in `iss`, `aud: appstoreconnect-v1`, and a short `exp`. Use a maintained JWT library and Apple's current token guide. To be safe, a normal request token lasts at most 20 minutes. Individual keys use a different documented set of claims. Do not apply team claims to individual keys without checking, or reuse a Connect JWT as an App Store Server API token.

| JWT part | Team key | Individual key |
| --- | --- | --- |
| Header | `alg: ES256`, real `kid`, `typ: JWT` | Same header with its own key ID |
| Identity claim | Real issuer UUID in `iss` | `sub: user`, omit `iss` |
| Time claims | `iat` and `exp` as Unix epoch seconds | Same time format |
| Audience | `aud: appstoreconnect-v1` | Same audience |
| Optional restricted scope | Documented matching GET request strings | Same documented scope mechanism |

Sign with the private key that matches `kid`, refresh expired tokens, and check both lifetime and clock drift. The guide has special long-lived scoped GET exceptions for some safe resources. Use short-lived tokens for release automation and do not stretch those exceptions to writes.

Store `.p8` material in the approved secret manager or a temporary keychain-backed credential location. Use `Authorization: Bearer <token>`, `Content-Type: application/json`, TLS, and a correctly synced clock. Never print tokens or put them in a committed curl example. Turn off shell tracing before handling secrets. Give the lowest role that supports the real release operations and app access.

## Read the official request contract

Use the official App Store Connect method reference for the chosen resource. Read the method and path, path/query/header parameters, request media types, required fields, relationships, response contracts, enums and security that applies. Resolve nested models before building a payload. This skill does not keep a generated schema dump or query program.

1. Search for the resource name.
2. Pick the exact operation that is not deprecated.
3. Read every path and query parameter, whether it is required, allowed filters, sorting, fields, and page size.
4. Resolve the request schema and build the real JSON:API `data.type`, attributes, relationships, and related resource identifiers. A relationship ID is not a display name or a product ID unless the docs say so.
5. Read the success and error contracts. Run the smallest request that does the job.
6. Follow `links.next` to the end. Keep the same filters. Read the resulting resource again and check relationships and processing state.

JSON:API updates use PATCH when that operation exists. Never guess supported updates from a create model. Use relationship endpoints for the documented link operation. Read-only, nullable, omitted, empty, and deleted are different states.

## Resource map

| Task | Official API resource families | Important ordering |
| --- | --- | --- |
| Team and signing | `users`, `userInvitations`, `bundleIds`, `certificates`, `profiles`, `devices` | Identity and role before changes |
| App information | `apps`, `appInfos`, `appInfoLocalizations`, `appCategories`, `appTags` | App record before localized app information |
| Versions and binaries | `appStoreVersions`, `builds`, `buildUploads`, `buildUploadFiles`, `preReleaseVersions` | Upload, processing, then select a compatible build |
| Listing media | `appStoreVersionLocalizations`, `appAssetLibraries`, `appAssetLibraryImages`, `appAssetLibraryVideos`, `appAssetLibraryRefData`, `appAssetLibraryPlacements`, `appAssetLibraryPlacementOrderingRequests` | Find specifications, reserve/upload/commit, verify, place and order |
| Compliance | `ageRatingDeclarations`, `appEncryptionDeclarations`, `accessibilityDeclarations` | Facts from the code and the owner |
| Review and release | `appStoreReviewDetails`, `reviewSubmissions`, `reviewSubmissionItems`, `appStoreVersionReleaseRequests`, `appStoreVersionPhasedReleases` | Clear all blocking states before submission or release |
| Prices and availability | `appPriceSchedules`, `appPricePoints`, `appAvailabilities`, `territoryAvailabilities`, `territories` | Choose the base territory, keep schedules and use current v2 availability |
| Purchases | `inAppPurchases`, `inAppPurchaseVersions`, `inAppPurchasePriceSchedules`, `inAppPurchaseAvailabilities` | Parent product before draft version and submission |
| Subscriptions | `subscriptionGroups`, `subscriptions`, `subscriptionVersions`, `subscriptionGroupVersions`, `subscriptionPrices`, `subscriptionIntroductoryOffers`, `subscriptionOfferCodes`, `winBackOffers` | Group, product, version, plan/price, localization, review |
| Beta and diagnostics | `betaGroups`, `betaTesters`, `betaAppReviewDetails`, `betaAppReviewSubmissions`, `betaFeedbackCrashSubmissions`, `betaFeedbackScreenshotSubmissions`, `diagnosticSignatures` | App access and beta review come before outside distribution |
| Store optimization | `appCustomProductPages`, `appStoreVersionExperiments`, `appEvents`, `nominations` | Feature eligibility and platform-specific assets |
| Games and reporting | `gameCenter*` and `analyticsReport*` families, `salesReports`, `financeReports` | Roles for each resource, version and release links and report availability |
| Extended administration | [Full functional coverage](api-coverage.md) | Clear routes for testing, optimization, retention, App Clips, games, hosted assets, alternative distribution, Xcode Cloud, SCM, signing, reviews and webhooks |

The table points to the documented functional areas. The official API reference also covers special features beyond a normal release. App Store Server API and notification formats are separate contracts. Use those real contracts for direct transaction checks instead of making them up from Connect resources.

## Uploads, errors, and resumability

For reserved assets, POST the real resource with the filename, exact byte size and parent or category fields. Run each returned upload operation with its exact method, URL, headers, byte offset and length. Split the bytes correctly. Do not attach Apple authorization to a different upload host. For current Asset Library images and videos, commit with `uploaded: true` and no checksum field, then poll the resource state. Dedicated review attachments and other asset resources have their own documented checksum and delivery contract. Read [the media procedure](screenshots-and-media.md) instead of using one old upload schema everywhere. Save IDs before you continue.

For a 401, check the token type, time, and key status. For a 403, check role, agreements, app access, and feature eligibility. For a 404, check team, ID type, and whether the item really exists. Read JSON:API error codes and source pointers for 409/422. Respect 429, `Retry-After` when given, and a limited exponential retry for temporary service failures. Never retry an uncertain create without checking. First check what exists by known identifiers and state.

Keep a cleaned log of operations with method, resource ID, payload hash, timestamp, response status, and next step. Resume from the remote state you confirmed. Local generated files do not prove the matching remote changes happened.
