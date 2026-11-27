# Testing, launch, and operations

## Distinct test environments

| Environment | Proves | Does not prove |
| --- | --- | --- |
| RevenueCat Test Store | Early SDK, catalog and paywall flow | Real Apple or Google product readiness |
| Local StoreKit configuration | Local Apple purchase UI and transaction logic | Store approval, pricing, or credential connection |
| Apple sandbox/TestFlight | Store-backed product and lifecycle integration | Production availability or final review approval |
| Google licensed tester on eligible test release | Real Play billing integration and catalog mapping | Production access approval or public rollout |
| Production smoke test | Real live configuration and access | All future renewals or every regional case |

Use the current test environment instructions and accounts. Avoid real charges unless they are clearly allowed as part of a production test. Never create fake refunds or grant promotional entitlements just to make an unfinished integration look successful.

## Required scenarios

Test every active product, base plan and offer, each entitlement, supported platform, key locale, and intended region. Include new and existing users, moving from anonymous to signed in, logout and login, another device, reinstall, store-account change, restore, purchase transfer policy, cancellation, pending purchase, network interruption, trial eligibility, renewal, upgrade and downgrade, expiration, grace or billing issue, refund or revocation, duplicate and out-of-order webhooks, and consumable delivery after a crash.

Check empty offerings, unavailable region, invalid app key, inactive product, missing entitlement or package link, stale customer information, server or API throttling, and a turned-off paywall. Handle known states on purpose. Do not make up generic success behavior when you cannot tell which product was bought.

Use `rc offerings verify` and the SDK-facing preview as evidence of configuration, then check real SDK and store transactions. Check store credentials and backend notifications separately. Record expected and observed access and money state without raw purchase credentials.

## Launch sequence

1. Check credentials, the product setup, regional pricing, review and activation state, offering and packages, and paywall versions.
2. Confirm the identity, restore and transfer policy and a working webhook and matching path.
3. Run release-mode device tests and sandbox lifecycle tests with evidence.
4. Prepare the app store submission separately, including honest paywall disclosures, reviewer access, product screenshots, and store product review requirements.
5. Select or publish the reviewed offering or paywall only when the real release scope calls for it. Keep the previous configuration ID and understand what changes would restore the setup if needed.
6. Check the configuration the production SDK audience sees, then watch purchases, access, webhook delay, failures, refunds and support.

## Operational API use

Use the official v2 reference for charts and metrics, audiences, integrations, collaborators/IAM, audit logs, invoices, virtual currency, customer resources, purchases and subscriptions. Use v1 where its supported customer or transaction operation fits. The exact permissions, environment, pagination, and schema decide each call.

Customer deletion, access grants and revokes, transfers, subscription cancellation, refunds, price changes, and integration changes all affect customers. Read the current state and the requested identity before changing anything. An API endpoint existing does not mean you are allowed to use it. Produce a cleaned before-and-after receipt and fix any partial failures.

Keep a release record with project and store app IDs, store product and base-plan mappings, entitlement, offering and package IDs, paywall version, SDK versions and platforms, credential-check timestamps, test evidence, webhook status, publish state, and owner or store actions still open. Never report a resource as live based only on a local generated file or an accepted background request.

## First-setup acceptance record

Use the [monetization brief](../assets/monetization-brief.json) and the returned remote IDs to record:

| Layer | Evidence needed | Insufficient substitute |
| --- | --- | --- |
| Account/project/apps | Real project and platform identities you can reach | A successful local login alone |
| Credentials | Stored configured flags plus the scope of the real checks | Calling an interactive Apple key-access check a purchase check |
| Catalog | Exact store IDs and base plans, active and review state and entitlement and package links | Four RevenueCat product records alone |
| Presentation | Reviewed published paywall, correct offering attachment and current state, SDK components for each app | A generated preview or publication ID alone |
| Native UI | Build with the correct public key, real localized prices, restore, legal and close controls you can reach | CLI preview fonts or sample prices |
| Transactions | Observed store-backed purchase and restore with verified customer info | Tapping a restore button, local developer access or an emulator where billing is unavailable |
| Release | Real submission, review and market availability | Setting up RevenueCat or committing a store edit |

Record each layer as verified, prepared, untested or blocked, with the real reason. Keep final
screenshots, signed-artifact references and cleaned receipts as needed. Remove temporary editor
sessions, OAuth login logs, schema scratch files and throwaway test files from the app repository.
Do not delete original credentials, user CLI profiles or symbol files needed to debug the release.

## Diagnose a partial setup without replacing working resources

| Observation | Inspect next | Completion evidence |
| --- | --- | --- |
| Project/app missing from a scoped list | Signed-in account, OAuth and project access, other app matches you can reach | Correct identity read-back or a clear scope block |
| Credential flag is true but products fail | App and team identity, real store permissions, package recognition, product state and SDK logs | The real check result, not another upload of the same key |
| Catalog products exist but the entitlement does not unlock | The exact product or base plan bought, entitlement attachments and verified CustomerInfo | A store-backed transaction maps to the stable entitlement |
| Packages empty or wrong on one platform | Public key and app, current offering, the platform product for each package and eligibility | SDK-facing preview plus a real product fetch on a device |
| Paywall published but a fallback appears | Attachment and current offering, published components, SDK and platform compatibility and audience | That app receives and shows the intended components |
| Preview font or restore control looks different | Known CLI renderer limits and the real design and native UI | Correct native font and control behavior, not repeated design edits without checking |
| No purchase possible on a separate emulator | Eligible store account, testing and install path and the full billing error | A suitable test environment or a transaction case clearly marked as not run |
| Generation, upload or write interrupted | Returned resource ID, session and the remote draft or publication state | Check what exists before retrying, without duplicates |

A successful product fetch and real prices can come before purchase testing. Keep that useful evidence
without treating it as a passed transaction. Fix the layer that failed. Do not fix a local setup by
granting a promotional entitlement, replacing customer info or changing business terms.

### Notifications and backend status remain independent

Tell apart store-to-RevenueCat notifications and RevenueCat-to-app webhooks. Record the real Apple
server-notification and Google RTDN setup needed for the chosen integration, using current provider
instructions and the owner's signed-in scope. Do not make up a webhook URL, Pub/Sub project or
working delivery just because credentials are connected.

If the app has no backend or webhook consumer of its own, record that design and which service owns
purchase state. Do not build a server only to fill in a template field. If a backend does grant
benefits, test its authenticated, repeat-safe matching with real provider events and allowed test
data. Keep missing notification delivery, untested restore and store review as named open states
instead of a blanket 'monetization complete'.
