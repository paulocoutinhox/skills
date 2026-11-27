# Angular

Use a current compatible Angular release and its supported CLI and build system. Angular CLI integrates Vite in its development tooling, but a standalone generic Vite scaffold is not a drop-in replacement for Angular's compiler and builder. Keep the supported Angular toolchain while meeting the goals of modern frontend tooling.

Use one component, service, directive, pipe, or primary type per file with hyphenated filenames. Organize by feature. Use current standalone component APIs for new code where supported. Keep templates focused, put business behavior in a fitting service or domain boundary, and make dependencies clear through dependency injection.

Use signals for suitable local reactive state and RxJS for streams where they fit. Use lifecycle-aware subscription cleanup and cancellation. Do not nest subscriptions to hide control flow, or keep subscriptions after destruction. Keep derived state computed and avoid multiple mutable sources for the same concept.

Use the existing store when it is consistent. Consider NgRx Store or SignalStore for large shared state only when its structure solves a real problem. Validate forms and external payloads, use the framework's safe bindings, and do not bypass sanitization without a proven trusted boundary.

Run the real Angular build, type and template checks, lint when configured, and the relevant tests. Test routing, forms, request errors, change detection, and SSR hydration when the change affects them. Do not assume a successful TypeScript compile validates every template or browser behavior.

## Applied case: request cancellation and derived state

Compute a derived view value from its source instead of keeping parallel mutable copies. Use the chosen boundary between signals and RxJS on purpose. An observable stream and a signal have different lifetime and error behavior.

For a changing query, a fitting stream operator can replace outdated requests without nested subscriptions. Tie the real subscription to the component or service lifetime through supported destruction APIs. Do not add a global subscription collection that hides ownership.

Check form validation, template bindings and runtime payload validation one by one. A successful TypeScript compile does not prove strict template correctness, safe HTML, keyboard behavior or hydration. Test delayed responses, route destruction, error recovery and the real production build. Use the current [Angular RxJS interoperability](https://angular.dev/ecosystem/rxjs-interop) and supported builder instead of a generic frontend scaffold.
