# SDK integration, customer identity, and access

## Platform matrix

Use the current official SDK for the app framework and deployment targets. For native Apple apps, check the current `purchases-ios` package's stated support and target availability for iOS/iPadOS, macOS, tvOS, and visionOS. Support for core purchases and for hosted paywall UI can differ. Do not assume every UIKit, SwiftUI, AppKit, TV, or spatial view is available just because the package builds on one Apple platform.

Use the documented Swift Package Manager distribution for native Apple integration. Check the chosen release's real package manifest and supported products before adding it to targets. RevenueCat's installation guide says CocoaPods trunk becomes read-only on December 2, 2026, so native SDK releases ship through Swift Package Manager.

For Android, use the current supported native SDK or the real cross-platform binding. Check Billing Library compatibility, minimum SDK, lifecycle, and ProGuard/R8 setup. For Flutter, React Native, Unity, Kotlin Multiplatform, or other bindings, use their current platform matrix and integration steps. Pin compatible versions and read the release notes before choosing APIs.

Configure once, at the right point in the app lifecycle, with the public SDK key for that app. Keep secret v1/v2 keys, Apple keys, Google credentials, and webhook authorization only on trusted servers and secret stores. Do not log customer purchases or keys to crash or analytics systems.

## Identity policy

Choose stable, opaque, signed-in App User IDs without email addresses, phone numbers, or personal data you do not need. Decide the policy for anonymous use, login, logout, account switch, alias and merge, restore, and purchase transfer before launch. Test them with several devices and accounts. An entitlement on an anonymous ID must not disappear or move unpredictably when the user signs in.

Treat the app identity and the store account identity as different. Do not let a client ask for any access for another user. Backend customer lookup must check that the requesting app user is allowed before showing subscription information. Server operations that grant or transfer access really change entitlements and need the intended scope.

## Client flow

1. Configure the SDK and identify the current app user according to the chosen policy.
2. Fetch offerings and eligible packages. Handle the configured empty, unavailable and error states clearly with a useful message for the user, not a made-up free upgrade or fallback product.
3. Show the localized product and offer information the SDK returns, including renewal and trial terms.
4. Start the purchase from the real foreground UI. Tell apart user cancellation, pending payment or approval, failure, and verified completion.
5. Refresh `CustomerInfo` and use the intended entitlement state. Listen for updates with the supported lifecycle method. Cached data, a live refresh, expiration, and the product's chosen offline policy are different states.
6. Give restore and manage-subscription actions where required and suitable, plus privacy and terms links. Restore can trigger identity or transfer behavior, so test the configured policy.

In its standard integration, RevenueCat normally owns finishing and acknowledging store transactions. Do not add separate StoreKit finishing or Play acknowledgment that clashes with that. App-owned purchase completion needs the documented split of duties and tests of the handover.

Automatic store completion and custom benefit delivery are separate. Match up consumables from
verified transaction history and `NON_RENEWING_PURCHASE` events, using the transaction identity to
make one lasting grant across client and webhook delivery. Do not assume an unconsumed store purchase
is still there. Use either the chosen provider-managed currency ledger or the app's own ledger for
purchase credit, not both.

## Backend and webhooks

Set and check the real Authorization header. Optional HMAC signing uses
`X-RevenueCat-Webhook-Signature` with `t` and `v1`. Check HMAC-SHA256 over the timestamp, a period,
and the unchanged request-body bytes, using the integration secret and a constant-time comparison.
Allow a tolerance on delivery time. Retries get a fresh signature timestamp but keep the event
identity and business timestamp. Do not reject real retries because of event age alone. Follow the
documented secret-rotation contract. Keep TLS, redacted logs, repeat-safe handling, and time-limited
processing.

Save event IDs and important times, acknowledge safely, and check the current customer and subscription state through the supported API. Events can be duplicated, delayed, or out of order. Do not switch access on or off from event names alone. Cancellation does not always end access right away. Billing issue, grace period, expiration, refund or revocation, transfer, product change, and extension have different effective dates and meanings.

Keep sandbox and production events and data apart. Check app, store, project and customer identifiers before granting access. Use a server ledger that is safe to repeat for consumables or virtual currency. Never award a pack twice because both the client callback and the webhook arrived. Match things up again after crashes and partial delivery.

## Security and observability

Check API keys with the least access needed, protected project roles, keeping PII to a minimum, access checks, account deletion, webhook replay, log redaction, purchase fraud, and injection of fake app-user identities. Record useful cleaned correlation IDs and state changes without keeping raw receipts you do not need. Metrics should tell apart a store purchase failure, an SDK or network failure, a setup failure, and a delay in entitlement sync.
