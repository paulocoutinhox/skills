# Kotlin and Android

## Architecture

Keep an existing architecture when it is consistent. For a new Android app without one, use MVVM with separate models, views or Compose screens, and view models. Prefer one-way data flow. Immutable UI state moves down and events move up. Use repositories for real data boundaries. Add a domain layer only for useful shared business behavior. Use one class, enum, or screen per file, following Kotlin's symbol-based filename conventions.

Expose read-only state such as `StateFlow` and keep changes inside its owner. Make loading, empty, success, and error behavior clear. Keep navigation decisions and short-lived effects planned. Do not use a global event bus to hide dependencies or duplicate state across the screen and view model.

## Lifecycle, concurrency, and memory

Use structured coroutines in a scope with a clear owner, such as `viewModelScope`. Collect UI flows with the platform's lifecycle-aware APIs. Avoid `GlobalScope`, leaking Activity contexts, unmanaged listeners, and long-running references to views. Do not block the main thread. Inject dispatchers for blocking work and testability. Keep cancellation and do not turn `CancellationException` into a normal failure.

Limit concurrent requests, close streams, and clean up listeners and resources. Use atomic state updates or confinement where multiple coroutines modify shared state. A coroutine is not free of races by default. Review recomposition stability, list keys, and captured state in Compose.

## Safety and verification

Use null safety, exhaustive sealed states, and clear error results. Avoid `!!`, broad exception suppression, reflective behavior, and unnecessary mutable collections. Keep credentials in platform-backed secure storage, disable cleartext traffic where it fits, keep exported components and permissions to a minimum, validate intents and app links, and enforce permissions on the server.

Under the owner's single-line call convention, a call's argument list stays on one line. ktlint reads its line width from `max_line_length` in `.editorconfig`, so that file is ktlint's own configuration. Set `max_line_length = 320` in the `[*.{kt,kts}]` section. When ktfmt or the IDE formatter wraps ordinary calls, raise its configured width or hard-wrap setting to the same value. Then join calls that were already wrapped. Compose content lambdas and trailing lambdas keep their block bodies.

Use the checked-in Gradle wrapper, the version catalog when there is one, compatible Kotlin/AGP/JDK versions, a formatter or ktlint, static analysis, and the relevant unit, coroutine, and instrumentation tests. Check process recreation, lifecycle transitions, configuration changes, offline errors, and cancellation where the change affects them. For non-Android Kotlin, fit lifetime and architecture to the real framework instead of adding Android classes.

## Applied case: cancellation and atomic UI updates

A view model owns the screen's load operation and exposes immutable state. Collect it through the real lifecycle-aware UI API. Recomposition should not start another request without an owner just because a value was read.

For requests that replace each other, use the stream, operator or lifetime policy that keeps only the intended response current. A late callback can still need a clear check that it belongs to the current request. An atomic `StateFlow.update` protects a read-modify-write operation on that state, but it does not make a network request and a database write one transaction.

Broad `runCatching` or `catch (Exception)` around suspending work can turn cancellation into a failure shown on screen. Keep `CancellationException` and handle real domain or network failures on purpose. Use the project's injected dispatcher for blocking work, and keep Activity and view references out of long-lived services.

Check a delayed outdated response, lifecycle stop and restart, rotation and process restoration, retry after a real failure and cancellation during I/O. Use the real [Kotlin scope/cancellation contract](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-coroutine-scope/) and [Android lifecycle guidance](https://developer.android.com/topic/libraries/architecture/coroutines), instead of assuming every coroutine is scoped and free of races by default.
