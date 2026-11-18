# Vue

Use current compatible Vue and a Vite-based setup for a new application. Follow an existing coherent structure. Prefer single-file components with one component per file and the Composition API for new code when no different project convention applies.

Keep templates declarative. Put reusable stateful behavior in focused composables. Keep pure domain operations and API access outside view components. Use explicit props and emitted events. Avoid mutating props or duplicating derived state. Use computed values for derivation and watchers only for actual side effects. Clean up effects and requests according to component lifetime.

Use Pinia when a genuine shared client store is needed. Keep server-cache ownership separate and do not put session credentials in a persisted public store. Respect SSR request boundaries so state does not leak across users. Avoid injecting untrusted HTML, unsafe URL bindings, index-based keys for mutable lists, and large deep watchers without need.

Run type checking with the project's Vue tooling, lint, production build, and relevant component and integration tests. Verify loading, errors, keyboard use, route transitions, cleanup, and any SSR hydration behavior affected by the change.

## Applied case: reactive scope and server rendering

A computed value should derive a total/filter from its actual reactive inputs. A watcher that copies the same result into another mutable store adds synchronization and can conceal the owner of a change. Use watchers for real effects with deliberate invalidation/cleanup.

For async search, ensure invalidated work cannot publish an obsolete result. Register cleanup through the selected Vue version's supported lifecycle at the required point. Do not assume a callback registered after an await has the same owner as one created synchronously in setup.

In SSR, a mutable module-level store can be shared across requests. Establish per-request state and test that two controlled users cannot receive each other's data. Pinia does not automatically authorize backend access or make every persisted value safe. The official [Vue watcher guide](https://vuejs.org/guide/essentials/watchers.html) and [SSR guidance](https://vuejs.org/guide/scaling-up/ssr.html) govern those boundaries.
