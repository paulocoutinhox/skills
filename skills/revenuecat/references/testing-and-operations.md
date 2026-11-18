# Testing, launch, and operations

## Distinct test environments

| Environment | Proves | Does not prove |
| --- | --- | --- |
| RevenueCat Test Store | Early SDK/catalog/paywall flow | Actual Apple/Google product readiness |
| Local StoreKit configuration | Local Apple purchase UI and transaction logic | Store approval, pricing, or credential connection |
| Apple sandbox/TestFlight | Store-backed product and lifecycle integration | Production availability or final review approval |
| Google licensed tester on eligible test release | Real Play billing integration and catalog mapping | Production access approval or public rollout |
| Production smoke test | Actual live configuration and access | All future renewals or every regional case |

Use current test environment instructions and accounts. Avoid real charges unless specifically authorized as part of a production test. Never create fake refunds or grant promotional entitlements just to make an incomplete integration appear successful.

## Required scenarios

Test every active product/base plan/offer, each entitlement, supported platform, key locale, and intended region. Include new and existing users, anonymous-to-authenticated transition, logout/login, another device, reinstall, store-account change, restore, purchase transfer policy, cancellation, pending purchase, network interruption, trial eligibility, renewal, upgrade/downgrade, expiration, grace/billing issue, refund/revocation, duplicate/out-of-order webhook, and consumable delivery after a crash.

Validate empty offerings, unavailable region, invalid app key, inactive product, missing entitlement/package link, stale customer information, server/API throttling, and a disabled paywall. Handle known states deliberately. Do not invent generic success behavior when the purchased product cannot be determined.

Use `rc offerings verify` and SDK-facing preview as configuration evidence, then verify actual SDK and store transactions. Check store credentials and backend notifications separately. Record expected versus observed access and financial state without raw purchase credentials.

## Launch sequence

1. Validate credentials, product graph, regional pricing, review/activation state, offering/packages, and paywall versions.
2. Confirm identity/restore/transfer policy and a working webhook/reconciliation path.
3. Run release-mode device tests and sandbox lifecycle tests with evidence.
4. Prepare the app store submission separately, including truthful paywall disclosures, reviewer access, product screenshots, and store product review requirements.
5. Select/publish the reviewed offering/paywall only when the actual release scope calls for it. Preserve the previous configuration ID and understand what changes would restore configuration if needed.
6. Verify the configuration visible to the production SDK audience, then observe purchases, access, webhook latency, failures, refunds and support.

## Operational API use

Use the official v2 reference for charts/metrics, audiences, integrations, collaborators/IAM, audit logs, invoices, virtual currency, customer resources, purchases and subscriptions. Use v1 where its supported customer/transaction operation is appropriate. Exact permissions, environment, pagination, and schema decide each call.

Customer deletion, access grants/revokes, transfers, subscription cancellation, refunds, price changes, and integration changes are customer-affecting operations. Read current state and the requested identity before mutation. An API endpoint's presence is not authorization. Produce a sanitized before/after receipt and reconcile partial failures.

Keep a release record with project/store app IDs, store product/base-plan mappings, entitlement/offering/package IDs, paywall version, SDK versions/platforms, credential-check timestamps, test evidence, webhook status, publication state, and outstanding owner/store actions. Never report a resource as live based only on a local generated file or an accepted asynchronous request.

## First-setup acceptance record

Use the [monetization brief](../assets/monetization-brief.json) and the returned remote IDs to record:

| Layer | Evidence needed | Insufficient substitute |
| --- | --- | --- |
| Account/project/apps | Actual accessible project and platform identities | A successful local login alone |
| Credentials | Stored configured flags plus scope of actual checks | Calling an interactive Apple key-access check a purchase validation |
| Catalog | Exact store IDs/base plans, active/review state and entitlement/package links | Four RevenueCat product records alone |
| Presentation | Reviewed published paywall, correct offering attachment/current state, per-app SDK components | A generated preview or publication ID alone |
| Native UI | Correct public-key build, actual localized prices, reachable restore/legal/close controls | CLI preview fonts or sample prices |
| Transactions | Observed store-backed purchase and restoration with verified customer info | Tapping a restore button, local developer access or a billing-unavailable emulator |
| Release | Actual submission/review and market availability | Configuring RevenueCat or committing a store edit |

Record each layer as verified, prepared, untested or blocked with the actual reason. Preserve final
screenshots, signed-artifact references and sanitized receipts as needed. Remove temporary editor
sessions, OAuth login logs, schema scratch files and disposable test artifacts from the app repository.
Do not delete original credentials, user CLI profiles or symbol files needed for release diagnostics.

## Diagnose a partial setup without replacing working resources

| Observation | Inspect next | Completion evidence |
| --- | --- | --- |
| Project/app absent from a scoped list | Authenticated account, OAuth/project access, other accessible app matches | Correct identity readback or an explicit scope block |
| Credential flag is true but products fail | App/team identity, effective store permissions, package recognition, product state and SDK logs | The actual check result, not another upload of the same key |
| Catalog products exist but entitlement does not unlock | Exact purchased product/base plan, entitlement attachments and verified CustomerInfo | Store-backed transaction maps to the stable entitlement |
| Packages empty/wrong on one platform | Public key/app, current offering, per-package platform product and eligibility | SDK-facing preview plus actual device product fetch |
| Paywall published but fallback appears | Attachment/current offering, published components, SDK/platform compatibility and audience | That app receives and renders the intended components |
| Preview font/restore control differs | Known CLI renderer limitations and actual design/native UI | Correct native font/control behavior, not repeated blind design edits |
| No purchase possible on an isolated emulator | Eligible store account, testing/install path and full billing error context | A suitable test environment or a precisely unexecuted transaction case |
| Generation/upload/write interrupted | Returned resource ID, session and remote draft/publication state | Reconciliation before retry, without duplicates |

A successful product fetch and real prices can precede purchase testing. Retain that useful evidence
without elevating it to a transaction pass. Fix the failed layer. Do not repair a local setup by
granting a promotional entitlement, replacing customer info or changing commercial terms.

### Notifications and backend status remain independent

Distinguish store-to-RevenueCat notifications from RevenueCat-to-application webhooks. Record the
actual Apple server-notification and Google RTDN configuration needed for the selected integration,
using current provider instructions and authenticated owner scope. Do not invent a webhook URL,
Pub/Sub project or working delivery merely because credentials are connected.

If the application has no own backend/webhook consumer, record that architecture and the service
responsible for purchase state. Do not scaffold a server solely to make a template field nonempty.
If a backend does grant benefits, test its authenticated, idempotent reconciliation with genuine
provider events and authorized test data. Keep missing notification delivery, untested restoration
and store review as named remaining states rather than a blanket 'monetization complete'.
