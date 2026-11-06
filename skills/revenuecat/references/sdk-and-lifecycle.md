# SDK integration, customer identity, and access

## Platform matrix

Use the current official SDK for the app framework and deployment targets. For native Apple apps, inspect the current `purchases-ios` package's declared support and target availability for iOS/iPadOS, macOS, tvOS, and visionOS. Core purchases support and hosted paywall UI support can differ. Do not assume every UIKit, SwiftUI, AppKit, TV, or spatial view is available merely because the package compiles on one Apple platform.

Prefer the current documented Swift Package Manager distribution for new native Apple integration. Inspect the selected release's actual package manifest and supported products before adding it to targets. The researched installation guide announces CocoaPods publication interruptions in November 2026 and permanent trunk publication closure in December 2026. Recheck those dates/status if updating an existing CocoaPods project rather than assuming the latest native SDK was published there.

For Android, use the current supported native SDK or the actual cross-platform binding. Check Billing Library compatibility, minimum SDK, lifecycle, and ProGuard/R8 setup. For Flutter, React Native, Unity, Kotlin Multiplatform, or other bindings, use their current platform matrix and integration instructions. Pin compatible versions and check release notes before choosing APIs.

Configure once at the correct application lifecycle point with the app-specific public SDK key. Keep secret v1/v2 keys, Apple keys, Google credentials, and webhook authorization exclusively on trusted servers/secret stores. Do not log customer purchases or keys to crash/analytics systems.

## Identity policy

Choose stable opaque authenticated App User IDs without email addresses, phone numbers, or unnecessary personal data. Define anonymous behavior, login, logout, account switch, alias/merge, restore, and purchase transfer policy before launch. Test them with multiple devices/accounts. An entitlement attached to an anonymous ID must not disappear or transfer unpredictably during sign-in.

Treat app identity and store account identity as distinct. Do not allow a client to request arbitrary access for another user. Backend customer lookup must authorize the requesting app user before exposing subscription information. Server operations that grant/transfer access have real entitlement effects and require the intended scope.

## Client flow

1. Configure the SDK and identify the current app user according to the selected policy.
2. Fetch offerings and eligible packages. Handle configured empty/unavailable/error states explicitly with a usable user message rather than a fabricated free upgrade or fallback product.
3. Render localized product/offer information returned by the SDK, including renewal/trial terms.
4. Purchase from the actual foreground UI. Distinguish user cancellation, pending payment/approval, failure, and verified completion.
5. Refresh `CustomerInfo` and use the intended entitlement state. Listen for updates using the supported lifecycle mechanism. Cached data, live refresh, expiration, and the product's deliberate offline policy are different states.
6. Provide restore/manage-subscription actions where required and appropriate, plus privacy and terms links. Restore can trigger identity/transfer behavior, so test the configured policy.

RevenueCat normally owns store transaction finishing/acknowledgment in its standard integration. Do not add independent StoreKit finishing or Play acknowledgment that conflicts with that ownership. Observer/custom transaction modes require the explicitly documented division of responsibility and migration tests.

Automatic store completion and custom benefit fulfillment are separate. Reconcile consumables from
verified transaction history and `NON_RENEWING_PURCHASE` events, using the transaction identity for
one durable grant across client/webhook delivery. Do not assume an unconsumed store purchase remains.
Use either the selected provider-managed currency ledger or the application's ledger for purchase
credit, without awarding both.

## Backend and webhooks

Configure and verify the actual Authorization header. Optional HMAC signing uses
`X-RevenueCat-Webhook-Signature` with `t` and `v1`. Validate HMAC-SHA256 over the timestamp, a period,
and unmodified request-body bytes using the integration secret and constant-time comparison. Apply
a delivery-time tolerance. Retries receive a fresh signature timestamp while retaining the event
identity and business timestamp. Do not reject legitimate retries based on event age alone. Follow
the documented secret-rotation contract. Keep TLS, redacted logs, idempotency, and bounded processing.

Persist event IDs and important timing, acknowledge safely, and reconcile current customer/subscription state through the supported API. Events can be duplicated, delayed, or out of order. Avoid toggling access from event names alone. Cancellation does not necessarily end access immediately. Billing issue, grace period, expiration, refund/revocation, transfer, product change, and extension have different effective dates and meanings.

Keep sandbox and production events/data logically distinguished. Verify app/store/project/customer identifiers before granting access. Use an idempotent server ledger for consumables or virtual currency. Never award a pack twice because both the client callback and webhook arrived. Reconcile after crashes and partial delivery.

## Security and observability

Check least-privilege API keys, protected project roles, PII minimization, access checks, account deletion, webhook replay, log redaction, purchase fraud, and app-user identity injection. Record useful sanitized correlation IDs and state transitions without retaining raw receipts unnecessarily. Metrics should distinguish store purchase failure, SDK/network failure, configuration failure, and entitlement synchronization delay.
