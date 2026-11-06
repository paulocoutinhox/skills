---
name: vue-app
description: Build and evolve modular Vue applications in JavaScript or TypeScript. Use for Vue components, composables, routes, state, forms, API integration, feature architecture, accessibility, and production verification.
license: MIT
---

# Vue App

Implement Vue applications with explicit ownership and maintainable component boundaries. Prefer
readability and cohesive features over clever expressions, giant page components, or speculative
frameworks. This skill supports JavaScript and TypeScript. Respect the project's selected language.

## Establish the application shape

Read project instructions, package scripts, lockfile, routes, and existing components first. Confirm
product journeys, browser targets, rendering/SEO needs, authentication, API contracts, localization,
and deployment constraints. Preserve coherent existing architecture. Do not change frameworks or
introduce a store just because this skill is selected.

For a new client-rendered project, use current Vue 3, Vite, and Composition API single-file components.
Prefer TypeScript when the user has no language preference. This is a project default, not a Vue
requirement. Use JavaScript deliberately when selected. Run `npm create vue@latest` in the intended
parent directory and select only required router, state, testing, and language options. Inspect the
generated scripts and current Node/tool versions rather than guessing commands. Keep the lockfile.
Use a verified compatible toolchain, not an unexamined major upgrade in an existing project.

If public content requires server rendering or generation, resolve that requirement explicitly and
follow the selected framework's server/data conventions. A Vite SPA is not automatically an SSR
application. Do not install a full-stack framework or rewrite a working site without task scope.

## Organize by feature and responsibility

Use existing layout when coherent. For a new app, this is a scalable starting point, not a requirement
to create empty folders:

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

A page composes its feature and owns route-level coordination. A component owns a meaningful visual
responsibility, its local interactions, and an explicit public contract. A composable owns a focused
reactive workflow/lifecycle. A service owns transport or business operations. Pure calculations do
not need a composable. Shared code must be genuinely shared and domain-neutral. Do not create a
catch-all `utils`, `manager`, universal form engine, or forwarding-only facade.

Keep one component per `.vue` file. Match the component's name to the filename, using hyphens where
tooling permits. Use focused files for exported models/enums when applicable. Extract a single-use
component when it encapsulates substantial cohesive behavior. Do not split trivial markup merely
to reduce line count. Avoid circular feature imports and broad barrels that conceal dependencies.
See [architecture and worked feature](references/architecture.md).

## Component contracts and reactivity

Use `<script setup>` and `lang="ts"` for TypeScript. Keep script, template, and optional style sections
consistent. Use explicit props and emitted events, named for intent. Props are inputs, not mutable
child state. Emit changes or use a deliberate `v-model` contract. Avoid exposing an entire controller
or a grab bag of unrelated callbacks to make a component appear small.

Choose `ref` for owned state and `computed` for derived values. Use `reactive` only with clear object
identity and destructuring semantics. Keep expressions in templates simple and move meaningful
derivations into named computed values. Use stable domain keys for lists. Do not combine list and
conditional logic on one element when its scope becomes ambiguous. Do not use array indexes as keys
for editable/reorderable records. Preserve reactivity when extracting store state, using Pinia's
`storeToRefs` where appropriate. Do not assume arbitrary destructuring retains reactive behavior.

Watchers synchronize side effects, not copies of derived state. Watch the actual reactive source.
For async work, invalidate the previous request and register cleanup before asynchronous boundaries.
An old response must not overwrite a newer query, selected record, or route. Unmount, logout, and
tenant changes must stop subscriptions, observers, timers, and in-flight work owned by that scope.
Vue's component-owned watcher cleanup does not automatically close every external resource.

Composables use `use...` exports and return only consumer-facing state/actions. Keep pure validation
and mapping functions outside reactive bookkeeping. A composable called twice normally creates two
instances unless explicitly shared. Do not accidentally share request-specific state at module scope
in SSR. Register lifecycle work within the proper component/composable scope.

## Put state in the correct place

| State | Default owner |
| --- | --- |
| Input draft, expanded row, open dialog | Local component or cohesive feature workflow. |
| Search, filters, pagination that should survive navigation | Validated route query/params. |
| Derived totals or filtered visible values | Computed state from an authoritative source. |
| Shared client identity/preferences/workflow | Pinia when multiple independent consumers justify it. |
| Remote records with freshness/invalidation requirements | A defined query/data layer. Use a maintained query library when its cache lifecycle is actually needed. |

Pinia is the official recommendation for larger shared client state, not a place for every variable.
Keep stores feature-focused and actions explicit. Do not duplicate remote records in local state,
Pinia, and a query cache without a clear authority. Persist only intentional non-sensitive data and
clear user-scoped state on identity/tenant transitions. Authentication and permission enforcement
remain server responsibilities, even when the router hides a page.

## Forms, routes, and data access

Separate form presentation/draft from submit orchestration and API transport. Define field types,
defaults, normalization, validation timing, error placement, and pending/success/failure behavior.
Keep the user's draft on failed submission. Distinguish empty, loading, permission-denied, validation,
conflict, and transport-error states. Prevent duplicate submits while preserving server idempotency
for operations that require it. Use an existing schema/form library only when the actual form needs it.

Use semantic controls with persistent labels, keyboard interaction, `autocomplete`, correct input
types, and associated error/help text. Restore focus after dialogs/navigation and announce important
errors/status without excessive live regions. Test input methods, not only click handlers.

Keep API URL construction, request contracts, cancellation, response mapping, and transport errors
in focused services. Do not scatter `fetch` calls throughout templates and components. Validate
untrusted boundary data and map server DTOs deliberately. A TypeScript assertion does not validate
JSON. Route params/query and local storage are untrusted inputs too. Use runtime validation where
the contract requires it, without duplicating every internal type check.

Use Vue Router for real route requirements, named route contracts, meaningful not-found/error views,
and lazy feature boundaries where useful. Decide whether a record change resets or preserves local
drafts. Guard unsaved changes when required by the product. Route guards cannot protect an API from
an unauthorized direct request.

## Security, styling, and performance

Treat `v-html`, dynamic URLs, third-party content, and persisted state as security boundaries.
Do not render untrusted templates or HTML without a deliberate sanitization/trust model. Keep
credentials out of client bundles. Confirm cross-tenant access and authentication expiry behavior.

Use shared tokens and small meaningful UI primitives. Keep feature styles with their component and
global tokens/baselines in the designated stylesheet. If using Tailwind, keep complete class names
and readable variants. Avoid one-off global overrides and conflicting competing style systems.

Optimize observed bottlenecks. Start independent requests concurrently, lazy-load heavy routes,
keep lists bounded/virtualized when needed, and inspect actual bundles. Do not add deep watchers,
memoization, global stores, or component wrappers as speculative optimizations. Read Vue's current
SSR/performance guidance for the selected rendering mode.

## Worked feature and acceptance

For a customer editor, let the page resolve the route/customer, a form own its draft and field
errors, a composable own load/save state, and a service own HTTP/DTO mapping. Pure validation lives
with the customer domain. Saving emits a clear result and invalidates the actual affected lists.
Switch from customer A to B while A's request is delayed. A must never populate B's form. Submit an
invalid draft, lose the network, restore it, and verify the draft remains editable and the result
does not create a duplicate mutation. Inspect keyboard focus and accessible error associations.

Test pure rules, component-visible behavior, and the integration boundaries that matter. Use the
project's current Vue Test Utils/Vitest setup where selected, and browser tests for real navigation,
focus, and critical journeys. Run the defined lint, type check (`vue-tsc` when configured), tests,
and production build. Vite transpilation alone does not establish type correctness.
Update README and a current-state AGENTS.md with structure, state ownership, commands, configuration,
and verification. Report actual results and remaining external dependencies. See [sources](references/sources.md).
