# Swift and Apple applications

## Architecture

Preserve a coherent existing architecture. If there is none, use MVVM: `Models/`, `Views/`, `ViewModels/`, and concrete service or repository boundaries as needed. Keep business and networking logic outside views. Use one type per file named after it. Organize by feature when that makes ownership clearer, with view, view model, and models separated within the feature.

Represent loading, loaded, empty, and error states explicitly. Model navigation and presentation as deliberate state. Keep a single owner for each observable state source and choose the observation mechanism supported by the deployment target. Do not combine incompatible property-wrapper generations or add old-OS bridges by default.

## Concurrency and lifetime

Use structured `async`/`await` and actor isolation. Isolate UI state to `MainActor`. Review `Sendable` boundaries and the chosen Swift language mode. Do not suppress concurrency errors with unchecked conformance or unsafe isolation without a documented, proven invariant. Propagate cancellation and avoid detached tasks without a concrete lifetime requirement.

Understand ARC ownership. Audit escaping closures, delegates, notification observers, timers, subscriptions, and tasks for retain cycles. Use weak captures when ownership requires them, not mechanically everywhere. Choose `unowned` only when the lifetime guarantee is proven. Cancel or remove owned long-lived work when its owner ends. Keep heavy work off the main actor and bound cached resources.

## Safety and verification

Avoid force unwraps and forced casts in production flows. Use exhaustive enums, validated decoding, explicit failures, and value semantics where appropriate. Store credentials in Keychain, respect transport security, avoid secrets in logs, and minimize capabilities. Validate incoming deep links and server-side authorization.

Build and test with the actual Xcode scheme, SDK, Swift mode, and deployment target. Use Swift Testing or the established XCTest suite. Run static analysis and Instruments for relevant leak or performance concerns. Exercise navigation, cancellation, background transitions, and accessibility when affected. Consult current Apple documentation before choosing observation or concurrency APIs. MVVM is this skill's default, not an Apple requirement.

## Applied case: search ownership across suspension

A main-actor-isolated view model can still display a stale result. Request A starts, suspends, request B starts and finishes, then A resumes. Actor isolation prevents unsynchronized memory access, but does not make the complete user operation atomic across `await`.

Define a request identity or selected-query invariant, cancel owned obsolete work, and check that a completion still belongs to current state before assigning results. Preserve cancellation rather than presenting a canceled request as a user-visible network failure. A weak capture solves a particular lifetime relationship, not this ordering defect.

Keep UI mutations on their intended actor. Move expensive decoding/computation according to the actual isolation model and selected Swift mode, without unsafe annotations merely to silence the compiler. Test rapid query replacement, navigation away, background/resume and a deliberately delayed first response. Check that no long-lived task/observer retains the screen after its owner ends.

Use the official [Swift concurrency chapter](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/concurrency/) and selected Xcode diagnostics to reason about actor reentrancy and task lifetime. Do not add old-OS bridges when the new final target does not need them.
