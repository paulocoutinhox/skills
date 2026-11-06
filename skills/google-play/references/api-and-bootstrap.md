# API, credentials, and initial setup

## Bootstrap boundaries

Verify the developer account, identity/organization verification, account standing, distribution agreement, payments profile when relevant, tax/trader declarations, and the user's role. Initial account enrollment and legal attestations require the real owner.

Create the first app in Play Console with its permanent package name, default language, title, app/game type, free/paid setting, support contact, and required acknowledgments. The Android Publisher API has no general app-creation method. Do not confuse `edits.insert` with creating an application. Resolve the record's package identity and permissions before any upload. A package name is permanent and must match the built app.

Prepare Play App Signing and distinguish the app signing key used by Google for distribution from the upload key used by CI. Retain the team's documented recovery process. Free-to-paid and package-name changes have store restrictions, so establish the commercial model before launch rather than assuming these fields are freely reversible.

## Authentication and access

Enable the Google Play Android Developer API in the selected Cloud project. Give the service account or authorized user the required Play Console permissions and app access. The obsolete requirement to link a Play developer account to a Cloud project is not a prerequisite in the current setup guide.

Use OAuth 2.0 with scope `https://www.googleapis.com/auth/androidpublisher`. Production CI should prefer a supported workload-identity/short-lived-credential setup, with the impersonated service account authorized in Play Console. If a key file is unavoidable, keep it in the secret manager, restrict access, rotate it, and materialize it only in the job's protected temporary directory.

API root: `https://androidpublisher.googleapis.com/`. Service path: `androidpublisher/v3/`. Use the official Google client library and its resumable media upload support, or implement the exact Discovery contract. Do not treat a Play Console browser cookie as an API credential. Never commit OAuth refresh tokens, service-account JSON, keystores, signing passwords, or raw purchase tokens.

## Read the official operation contract

Use the official Publisher method reference for the selected resource. Read method/path, parameter locations, required flags, OAuth scopes, request/response models and actual media-upload options. Resolve referenced models and global parameters. This descriptive skill does not contain a schema dump or lookup program.

Before a write, read the operation and models, including field behavior, update masks, regional versions, pagination, and supported enum values. Method documentation also contains behavioral constraints that are not represented by schema. Google partial updates differ per endpoint. Never send a generic object from a similarly named method.

| Domain | API family | Key distinction |
| --- | --- | --- |
| Listing, builds and tracks | `edits` | Explicit edit session and commit |
| Data safety | `applications.dataSafety` | Standalone official CSV contents in `safetyLabels`, with truthful declarations |
| Device/distribution settings | `generatedapks`, `systemapks.variants`, `applications.deviceTierConfigs`, `internalappsharingartifacts` | Generated artifacts and internal sharing are not public releases |
| Modern one-time products | `monetization.onetimeproducts` | Purchase options, offers, regional configuration |
| Subscriptions | `monetization.subscriptions` | Product, base plan, offer and activation lifecycles |
| Existing legacy products | `inappproducts` | Inspect current migration state, do not choose legacy for new catalogs by habit |
| Purchase status and fulfillment | `purchases.products`, `purchases.productsv2`, `purchases.subscriptions`, `purchases.subscriptionsv2` | App/store product configuration is distinct from customer transactions |
| Refunds and revocations | `orders`, `purchases.voidedpurchases`, subscription revoke operations | Financial/customer effect, authorization and idempotency required |
| Reviews | `reviews` | Public replies are external messages, not read-only maintenance |
| Financial catalog details | `monetization.convertRegionPrices` and regional models | Currency/region configuration is not a universal float price |
| Recovery, access and specialized programs | [Complete functional coverage](api-coverage.md) | Actual methods and workflows for recovery/signing, users/grants and eligible app-store-hosted review/catalog surfaces |

The separate Google Play Developer Reporting API, Play Integrity API, Firebase, Google Cloud Pub/Sub, and Billing client API have their own contracts and permissions. Fetch their current official references when those integrations are needed. Do not infer unrelated service APIs from Publisher resources.

## Request reliability

Respect pagination, quota, rate headers, resumable upload state, and bounded retries. Inspect 400 field errors, 401 token/scopes, 403 Play permissions/account eligibility, 404 package/record access, and 409 edit conflicts rather than adding an unrelated fallback. Retry transient failures with bounded exponential backoff. Reconcile a timeout before replaying a state-changing operation.

Keep a sanitized journal of package, operation, edit ID, update mask, payload hash, resource/version IDs, and observed response state. Avoid concurrent listing edits for the same package. The console or another automation can invalidate assumptions while an edit is open.

Choose current commit review-conflict behavior deliberately: the default can cancel an ongoing review.
Use the actual `ERROR_IF_IN_REVIEW` option when preserving that review is intended. Follow
[the edit/review procedure](edits-review-and-rollout.md), not an implicit retry that changes intent.
Listing edits, catalog/price writes, Data safety and specialized app-store-hosted mutations have
different transaction/publication effects. A deleted edit does not roll back those independent calls.
