# Vue

Use current compatible Vue and a Vite-based setup for a new application. Follow an existing structure when it is consistent. Prefer single-file components with one component per file and the Composition API for new code when no different project convention applies.

Keep templates declarative. Put reusable stateful behavior in focused composables. Keep pure domain operations and API access outside view components. Use clear props and emitted events. Do not change props or duplicate derived state. Use computed values for derived data and watchers only for real side effects. Clean up effects and requests to match the component's lifetime.

Use Pinia when you really need a shared client store. Keep server-cache ownership apart, and do not put session credentials in a persisted public store. Respect SSR request boundaries so state does not leak across users. Avoid injecting untrusted HTML, unsafe URL bindings, index-based keys for mutable lists, and large deep watchers without need.

Run type checking with the project's Vue tooling, lint, production build, and relevant component and integration tests. Check loading, errors, keyboard use, route transitions, cleanup, and any SSR hydration behavior affected by the change.

## Applied case: reactive scope and server rendering

A computed value should derive a total or filter from its real reactive inputs. A watcher that copies the same result into another mutable store adds syncing and can hide who owns a change. Use watchers for real effects with planned invalidation and cleanup.

For async search, make sure invalidated work cannot publish an outdated result. Register cleanup through the chosen Vue version's supported lifecycle at the required point. Do not assume a callback registered after an await has the same owner as one created synchronously in setup.

In SSR, a mutable module-level store can be shared across requests. Set up state per request, and test that two controlled users cannot receive each other's data. Pinia does not authorize backend access on its own or make every persisted value safe. The official [Vue watcher guide](https://vuejs.org/guide/essentials/watchers.html) and [SSR guidance](https://vuejs.org/guide/scaling-up/ssr.html) define those boundaries.
