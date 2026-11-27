---
name: vue-app
description: Build and evolve modular Vue applications in JavaScript or TypeScript. Use for Vue components, composables, routes, state, forms, API integration, feature architecture, accessibility, and production checks.
license: MIT
---

# Vue App

Build Vue applications where every piece has a clear owner and component boundaries are easy to
maintain. Prefer readable code and well-grouped features over clever expressions, giant page
components or frameworks built for guessed future needs. This skill supports JavaScript and
TypeScript. Respect the language the project chose.

## Set the application shape

First read the project instructions, package scripts, lockfile, routes and existing components.
Confirm the product journeys, browser targets, rendering and SEO needs, authentication, API
contracts, localization and deployment limits. Keep a sound existing architecture. Do not change
frameworks or add a store just because this skill is in use.

For a new client-rendered project, use current Vue 3, Vite, and Composition API single-file
components. Prefer TypeScript when the user has no language preference. This is a project default,
not a Vue requirement. Use JavaScript on purpose when it is chosen. Run `npm create vue@latest` in
the intended parent directory, and pick only the router, state, testing and language options you
need. Inspect the generated scripts and the current Node and tool versions instead of guessing
commands. Keep the lockfile. Use a checked, compatible toolchain, not an untested major upgrade in an
existing project.

If public content needs server rendering or generation, settle that need explicitly and follow the
chosen framework's server and data conventions. A Vite SPA is not an SSR application by default. Do
not install a full-stack framework or rewrite a working site unless the task covers it.

## Organize by feature and responsibility

Use the existing layout when it is sound. For a new app, this is a starting point that can grow. It
is not a reason to create empty folders:

```text
src/
  app/                       Bootstrap, router, providers, global configuration
  features/
    customers/
      pages/                 Route-level composition
      components/            Customer-specific UI
      composables/           Owned reactive workflows
      services/              API transport and response mapping
      models/                Domain types and pure rules
  shared/
    components/              Proven cross-feature UI primitives
    services/                Real shared infrastructure
  styles/                    Global tokens and baseline styles
```

A page puts its feature together and owns route-level coordination. A component owns one clear
visual job, its local interactions, and an explicit public contract. A composable owns a focused
reactive workflow or lifecycle. A service owns transport or business operations. Pure calculations
do not need a composable. Shared code must really be shared and must not depend on one domain. Do
not create a catch-all `utils`, `manager`, universal form engine, or a facade that only forwards
calls.

Keep one component per `.vue` file. Match the component's name to the filename, using hyphens where
the tooling allows. Use focused files for exported models and enums when they apply. Extract a
single-use component when it wraps a large, well-grouped piece of behavior. Do not split trivial
markup just to reduce the line count. Avoid circular imports between features and broad barrel
files that hide dependencies. Keep each function call on one line. When a call's arguments get
complex, name intermediate values instead of wrapping arguments across lines. If the project uses
Prettier, keep or set a wide `printWidth`, such as 320, so the formatter does not wrap calls. Join
calls that a narrower setting split. See [architecture and worked feature](references/architecture.md).

## Component contracts and reactivity

Use `<script setup>` and `lang="ts"` for TypeScript. Keep the script, template and optional style
sections consistent. Use explicit props and emitted events, named for their intent. Props are
inputs, not state the child can change. Emit changes, or use a planned `v-model` contract. Declare
that contract with `defineModel()`. Do not expose a whole controller or a grab bag of unrelated
callbacks to make a component look small.

Choose `ref` for owned state and `computed` for derived values. Use `reactive` only when object
identity and destructuring behavior are clear. Keep template expressions simple, and move meaningful
calculations into named computed values. Use stable domain keys for lists. Do not combine list and
condition logic on one element when its scope becomes unclear. Do not use array indexes as keys for
records that can be edited or reordered. Keep reactivity when you pull state out of a store, using
Pinia's `storeToRefs` where it fits. Do not assume that any destructuring keeps reactive behavior.

Watchers sync side effects. They do not keep copies of derived state. Watch the real reactive
source. For async work, cancel the previous request and register its cleanup in the same callback.
`onWatcherCleanup()` works only before the first `await` in the callback. When the cleanup can only
be registered after an `await`, use the `onCleanup` argument passed to `watch`/`watchEffect`
callbacks, which has no such limit. An `AbortController` aborted in that cleanup cancels the fetch.
An old response must not overwrite a newer query, selected record or route. Unmount, logout and
tenant changes must stop the subscriptions, observers, timers and running work owned by that scope.
Vue's cleanup of component-owned watchers does not close every external resource for you.

Composables use `use...` exports and return only the state and actions callers need. Keep pure
validation and mapping functions outside the reactive bookkeeping. A composable called twice
normally creates two instances unless it is shared on purpose. In SSR, do not share request-specific
state at module scope by accident. Register lifecycle work inside the right component or composable
scope.

## Put state in the right place

| State | Default owner |
| --- | --- |
| Input draft, expanded row, open dialog | Local component or closely related feature workflow. |
| Search, filters, pagination that should survive navigation | Validated route query/params. |
| Derived totals or filtered visible values | Computed state from the source of truth. |
| Shared client identity/preferences/workflow | Pinia when several independent consumers need it. |
| Remote records with freshness/invalidation requirements | A defined query/data layer. Use a maintained query library when its cache lifecycle is actually needed. |

Pinia is the official recommendation for larger shared client state. It is not a place for every
variable. Keep stores focused on one feature and keep actions explicit. Do not copy remote records
into local state, Pinia and a query cache without one clear source of truth. Store only chosen,
non-sensitive data, and clear user-scoped state when the identity or tenant changes. The server still
enforces authentication and permissions, even when the router hides a page.

## Forms, routes, and data access

Keep the form's display and draft apart from the submit flow and API transport. Define field types,
defaults, normalization, when validation runs, where errors appear, and the pending/success/failure
behavior. Keep the user's draft when a submit fails. Show empty, loading, permission-denied,
validation, conflict and transport-error states separately. Prevent duplicate submits, and keep
server idempotency (safe repeats) for operations that need it. Use an existing schema or form
library only when the real form needs it.

Use semantic controls with labels that stay visible, keyboard interaction, `autocomplete`, correct
input types, and error and help text linked to their fields. Restore focus after dialogs and
navigation. Announce important errors and status without too many live regions. Test input methods,
not only click handlers.

Keep API URL building, request contracts, cancellation, response mapping and transport errors in
focused services. Do not scatter `fetch` calls across templates and components. Validate untrusted
data at the boundary, and map server DTOs (data transfer objects) on purpose. A TypeScript assertion
does not validate JSON. Route params, query values and local storage are untrusted inputs too. Use
runtime validation where the contract needs it, without repeating every internal type check.

Use Vue Router for real route needs, named route contracts, useful not-found and error views, and
lazy-loaded features where they help. Decide whether a record change resets or keeps local drafts.
Guard unsaved changes when the product needs it. Route guards cannot protect an API from a direct
request that is not authorized.

## Security, styling, and performance

Treat `v-html`, dynamic URLs, third-party content and stored state as security boundaries. Do not
render untrusted templates or HTML without a planned sanitization and trust model. Keep credentials
out of client bundles. Check cross-tenant access and what happens when authentication expires.

Use shared tokens and small, meaningful UI primitives. Keep feature styles with their component, and
global tokens and baselines in the chosen stylesheet. If you use Tailwind, keep complete class names
and readable variants. Avoid one-off global overrides and competing style systems.

Optimize bottlenecks you have actually seen. Start independent requests at the same time, lazy-load
heavy routes, keep lists limited or virtualized when needed, and inspect the real bundles. Do not add
deep watchers, memoization, global stores or component wrappers as guesses at optimization. Read
Vue's current SSR and performance guidance for the chosen rendering mode.

## Worked feature and acceptance

For a customer editor, the page resolves the route and customer. A form owns its draft and field
errors. A composable owns the load/save state. A service owns HTTP and DTO mapping. Pure validation
lives with the customer domain. Saving emits a clear result and invalidates the lists that are
really affected. Switch from customer A to B while A's request is delayed. A must never fill B's
form. Submit an invalid draft, lose the network, restore it, and check that the draft is still
editable and that the result does not create a duplicate mutation. Inspect keyboard focus and check
that errors are linked to their fields for assistive technology.

Test pure rules, behavior the user can see in components, and the integration boundaries that
matter. Use the project's current Vue Test Utils/Vitest setup where it is chosen, and browser tests
for real navigation, focus and key journeys. Read the `package.json` scripts, then run the defined
lint, type check (`vue-tsc` when configured), tests and production build. If the project does not
define a check, report that instead of inventing its command. Vite transpilation alone does not
prove the types are correct. A failing check blocks completion. Fix its cause, or report the exact
failure and the remaining work. Update the README and a current-state AGENTS.md with structure, state
ownership, commands, configuration and checks. Report the real results and the external
dependencies that remain. See [sources](references/sources.md).
