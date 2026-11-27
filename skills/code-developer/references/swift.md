# Swift and Apple applications

## Architecture

Keep an existing architecture when it is consistent. If there is none, use MVVM: `Models/`, `Views/`, `ViewModels/`, and concrete service or repository boundaries as needed. Keep business and networking logic outside views. Use one type per file, named after the type. Group by feature when that makes ownership clearer, with the view, view model, and models kept apart inside the feature.

Represent loading, loaded, empty, and error states clearly. Model navigation and presentation as planned state. Keep one owner for each observable state source and choose the observation method that the deployment target supports. Do not mix incompatible property-wrapper generations or add old-OS bridges by default.

## Concurrency and lifetime

Use structured `async`/`await` and actor isolation. Isolate UI state to `MainActor`. Review `Sendable` boundaries and the chosen Swift language mode. Do not hide concurrency errors with unchecked conformance or unsafe isolation unless a documented, proven rule supports it. Pass cancellation on and avoid detached tasks unless a concrete lifetime need calls for one.

Understand ARC ownership. Check escaping closures, delegates, notification observers, timers, subscriptions, and tasks for retain cycles. Use weak captures when ownership needs them, not out of habit everywhere. Choose `unowned` only when the lifetime guarantee is proven. Cancel or remove long-lived work when its owner ends. Keep heavy work off the main actor and limit cached resources.

## Safety and verification

Avoid force unwraps and forced casts in production flows. Use exhaustive enums, validated decoding, clear failures, and value semantics where they fit. Store credentials in Keychain, respect transport security, keep secrets out of logs, and request as few capabilities as you can. Validate incoming deep links and server-side authorization.

Use the project's formatter and linter configuration. When swift-format wraps ordinary calls or SwiftLint reports their length, set `"lineLength": 320` in `.swift-format` and `line_length: 320` in `.swiftlint.yml` together, then join calls that were already wrapped. Under the owner's single-line call convention, a call's argument list stays on one line. A trailing closure keeps its block body.

Build and test with the real Xcode scheme, SDK, Swift mode, and deployment target. Use Swift Testing or the existing XCTest suite. Run static analysis and Instruments when leaks or performance matter. Test navigation, cancellation, background transitions, and accessibility when the change affects them. Read the current Apple documentation before choosing observation or concurrency APIs. MVVM is this skill's default, not an Apple requirement.

## Applied case: search ownership across suspension

A main-actor-isolated view model can still show an outdated result. Request A starts, suspends, request B starts and finishes, then A resumes. Actor isolation prevents unsynchronized memory access, but it does not make the whole user operation atomic across `await`.

Define a request ID or a selected-query rule, cancel outdated work that the screen owns, and check that a completion still belongs to the current state before you assign results. Keep cancellation as cancellation. Do not show a canceled request to the user as a network failure. A weak capture solves one specific lifetime problem, not this ordering bug.

Keep UI changes on their intended actor. Move costly decoding or computation according to the real isolation model and chosen Swift mode, without unsafe annotations just to silence the compiler. Test fast query replacement, navigating away, background and resume, and a first response that is delayed on purpose. Check that no long-lived task or observer keeps the screen alive after its owner ends.

Use the official [Swift concurrency chapter](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/concurrency/) and the chosen Xcode diagnostics to reason about actor reentrancy and task lifetime. Do not add old-OS bridges when the new final target does not need them.
