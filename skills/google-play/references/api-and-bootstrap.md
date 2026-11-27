# API, credentials, and initial setup

## Bootstrap boundaries

Check the developer account, identity or organization verification, account standing, distribution agreement, payments profile when relevant, tax and trader declarations, and the user's role. The first account sign-up and legal statements need the real owner.

Create the first app in Play Console with its permanent package name, default language, title, app or game type, free or paid setting, support contact and required acknowledgments. The Android Publisher API has no general method for creating apps. Do not confuse `edits.insert` with creating an application. Settle the record's package name and permissions before any upload. A package name is permanent and must match the built app.

Set up Play App Signing. The app signing key is the one Google uses for distribution. The upload key is the one CI uses. Keep the team's documented recovery process. The store limits changes from free to paid and changes of package name, so decide the commercial model before launch instead of assuming you can freely undo these fields.

## Authentication and access

Enable the Google Play Android Developer API in the chosen Cloud project. Give the service account or authorized user the Play Console permissions and app access they need. The current setup guide does not require linking the Play developer account to a Cloud project.

Use OAuth 2.0 with scope `https://www.googleapis.com/auth/androidpublisher`. Production CI should prefer a supported workload-identity or short-lived-credential setup, with the impersonated service account authorized in Play Console. If you cannot avoid a key file, keep it in the secret manager, limit access, rotate it, and write it out only in the job's protected temporary directory.

API root: `https://androidpublisher.googleapis.com/`. Service path: `androidpublisher/v3/`. Use the official Google client library and its resumable media upload support, or implement the exact Discovery contract. Do not use a Play Console browser cookie as an API credential. Never commit OAuth refresh tokens, service-account JSON, keystores, signing passwords or raw purchase tokens.

## Read the official operation contract

Use the official Publisher method reference for the chosen resource. Read the method and path, where each parameter goes, required flags, OAuth scopes, request and response models and the real media-upload options. Look up the models and global parameters it refers to. This descriptive skill has no schema dump or lookup program.

Before a write, read the operation and its models, including field behavior, update masks, regional versions, pagination and supported enum values. Method docs also list behavior rules that the schema does not show. Google partial updates work differently per endpoint. Never send a generic object copied from a method with a similar name.

| Domain | API family | Key distinction |
| --- | --- | --- |
| Listing, builds and tracks | `edits` | Explicit edit session and commit |
| Data safety | `applications.dataSafety` | Standalone official CSV contents in `safetyLabels`, with honest declarations |
| Device/distribution settings | `generatedapks`, `systemapks.variants`, `applications.deviceTierConfigs`, `internalappsharingartifacts` | Generated artifacts and internal sharing are not public releases |
| One-time products | `monetization.onetimeproducts` | Purchase options, offers, regional configuration |
| Subscriptions | `monetization.subscriptions` | Product, base plan, offer and activation lifecycles |
| Purchase status and fulfillment | `purchases.products`, `purchases.productsv2`, `purchases.subscriptions`, `purchases.subscriptionsv2` | App and store product setup is not the same as customer transactions |
| Refunds and revocations | `orders`, `purchases.voidedpurchases`, subscription revoke operations | Affects money and customers, and needs authorization and idempotency |
| Reviews | `reviews` | Public replies are messages to outside people, not read-only maintenance |
| Financial catalog details | `monetization.convertRegionPrices` and regional models | Currency and region setup is not a single float price |
| Recovery, access and specialized programs | [Complete functional coverage](api-coverage.md) | Real methods and workflows for recovery/signing, users/grants and eligible app-store-hosted review/catalog surfaces |

The separate Google Play Developer Reporting API, Play Integrity API, Firebase, Google Cloud Pub/Sub and Billing client API each have their own contracts and permissions. Get their current official references when you need those integrations. Do not guess other services' APIs from Publisher resources.

## Request reliability

Respect pagination, quota, rate headers, resumable upload state and limited retries. Look at 400 field errors, 401 token or scopes, 403 Play permissions or account eligibility, 404 package or record access, and 409 edit conflicts, instead of adding an unrelated fallback. Retry temporary failures with limited exponential backoff. After a timeout, check the real result before you replay an operation that changes state.

Keep a cleaned log of the package, operation, edit ID, update mask, payload hash, resource and version IDs, and the response state you saw. Avoid running listing edits for the same package at the same time. The console or another automation can change things while an edit is open.

Choose the current commit review-conflict behavior on purpose: the default can cancel a review in
progress. Use the real `ERROR_IF_IN_REVIEW` option when you mean to keep that review. Follow
[the edit/review procedure](edits-review-and-rollout.md), not a hidden retry that changes intent.
Listing edits, catalog and price writes, Data safety and specialized app-store-hosted changes have
different transaction and publishing effects. A deleted edit does not undo those separate calls.
