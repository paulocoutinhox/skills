---
name: react-app
description: Build and evolve modular React applications in JavaScript or TypeScript. Use for component and hook design, state ownership, routes, forms, data access, async effects, accessibility, and production verification.
license: MIT
---

# React App

Build React applications whose behavior can be understood, debugged, and changed locally. Keep
components, hooks, transport, and domain rules cohesive. Use the chosen JavaScript or TypeScript
language without maintaining duplicate implementations. No executable scaffolder is bundled here.

## Resolve product and rendering requirements

Inspect AGENTS.md, current framework/router, package scripts, dependencies, and lockfile before
editing. Identify critical journeys, browser support, SEO/rendering needs, account/tenant boundaries,
API contracts, localization, and deployment. Preserve coherent architecture and user choices.

For a new client-rendered application, this collection defaults to Vite and function components.
Prefer TypeScript if no language is selected. Scaffold with
`npm create vite@latest my-app -- --template react-ts`, or `react` for JavaScript, in the intended
parent directory. Inspect current Node requirements and generated scripts. Use the latest compatible
dependencies and retain the lockfile. Do not use Create React App or import obsolete setup recipes.

React's official guidance recommends a suitable framework for new production applications. Our Vite
SPA default is a project preference for client-only scope. If SSR, SSG, server functions, or integrated
data routing is needed, resolve the framework choice explicitly and follow its current contracts.
Do not present Next.js APIs as core React or silently replace the selected platform.

## Establish feature boundaries

```text
src/
  app/                        Bootstrap, router, providers, app-wide configuration
  features/
    orders/
      pages/                  Route composition
      components/             Order UI responsibilities
      hooks/                  Focused stateful workflows
      services/               API transport and response mapping
      models/                 Domain types and pure rules
  shared/
    components/               Proven cross-feature primitives
    services/                 Real shared infrastructure
  styles/                     Global tokens and baseline
```

Use only needed directories. A route composes features, a component owns coherent UI, a hook owns
focused React state/effect lifecycle, a service owns transport/operations, and pure functions own
framework-independent rules. Keep dependencies flowing toward explicit domain/infrastructure
boundaries rather than importing pages into shared primitives. Avoid circular feature imports.

One component per source file. Match names and filenames with project/tool conventions, preferring
hyphens when permitted. Extract substantial single-use responsibilities when useful. Do not create
a generic field renderer, universal repository, or forwarding-only wrapper for hypothetical reuse.
A giant custom hook behind a tiny page is still a giant implementation. See
[architecture and async review](references/architecture.md).

## Design component contracts

Use explicit props, stable event contracts, and composition through children/slots appropriate to
React. Keep components pure during render. Do not define component functions inside another component,
which changes their identity and can reset state. Use stable data identities for list keys and use
keys intentionally to reset an editor when its record identity changes. Array positions are unsuitable
keys for mutable/reorderable records. Keep local UI behavior near its owning element/component.

Avoid boolean-prop combinations that create contradictory states. Use a clear variant or state
model when there are exclusive modes. Keep a real component-specific API rather than leaking an
entire controller, store, or internal mutable object. Public props/events must communicate intent.
Validate untrusted API data at the boundary. TypeScript types/casts do not check network responses.

## Choose one state authority

| State kind | Owner |
| --- | --- |
| Draft input, dialog visibility, local selection | Owning component or cohesive custom hook. |
| Shareable filters/search/page | Validated router/URL state. |
| Values calculated from props/state | Derived during render, not mirrored by an effect. |
| Server records and mutations | Router data APIs or an intentional query layer/cache. |
| Cross-feature client state | A focused provider/store only when real independent consumers need it. |

Lift state to the nearest meaningful shared owner. Use a reducer when explicit related transitions
clarify a workflow. Use context for scoped dependencies or modest shared state, with provider value
identity and update scope considered. Do not make a global context carry every keystroke.
For substantial shared client state, choose a maintained library according to requirements and the
existing project, such as Redux Toolkit for explicit complex workflows or Zustand for a smaller
external store. Do not install multiple stores or claim one is universally best.

Use a maintained query solution when freshness, cancellation, deduplication, invalidation, and
optimistic mutation lifecycles justify it. Do not duplicate its records in a separate global store.
Define identity/tenant-scoped cache keys and clear protected state on logout/account switching.
Never use a frontend store or route guard as the authorization boundary.

## Hooks and external synchronization

Hooks compose stateful behavior and begin with `use`. Call them at the supported top-level locations,
not inside loops, conditions, event handlers, or arbitrary functions. Pure helpers do not need hooks.
Return a small coherent consumer contract, not every internal setter and implementation detail.

Use effects to synchronize external systems. Calculate derived render values directly. Put a user
action's mutation in its event/action workflow rather than an effect watching a submit flag.
Respect dependency rules and fix unstable dependencies at their cause. Do not suppress the linter
to hide stale closures. For updates based on previous state, use the appropriate functional update.
Refs hold mutable non-rendered values, not a secret second state store for displayed data.

Every subscription, listener, timer, observer, and request needs an owner and a cleanup/commit rule.
Abort or invalidate superseded work so an old response cannot overwrite the current route/query.
Cancellation alone does not undo a server mutation. Define idempotency and reconciliation where the
operation requires them. Development Strict Mode can expose missing cleanup. Do not remove it merely
to make duplicate effects disappear. Do not make rendering or an effect charge a customer.

## Forms, navigation, and errors

Keep form drafts, field presentation, submission orchestration, domain validation, and transport
separate where their responsibilities warrant it. Use labeled semantic inputs, correct types and
autocomplete, keyboard support, associated errors, focus restoration, and accessible status feedback.
Preserve drafts after failures. Prevent duplicate submission while retaining server-side invariants.
For large forms, adopt a maintained schema/form library based on actual needs, not every simple input.

Represent loading, empty, success, denied, validation, conflict, and transport failure distinctly.
Do not turn a failed fetch into an empty list that appears successful. Follow the selected framework's
error boundaries and route-error mechanism. Error boundaries do not automatically catch every async
event-handler rejection. Handle those failures at their operation boundary.

Use route contracts and real not-found states. Define unsaved-change behavior when applicable.
For query changes during typing, decide cancellation/debounce/navigation explicitly. Do not add a
manual router or custom query cache around a library that already owns those responsibilities.

## Security, styling, and measured performance

Keep secrets out of client bundles and public environment variables. Treat dynamic HTML, URLs,
embedded third-party content, storage, and messages as untrusted. Use `dangerouslySetInnerHTML` only
with a justified trust/sanitization contract. Scope protected data by actual user/tenant permission.
SSR/server components must not share mutable request data between users. Follow the selected
framework's server/client module boundaries rather than moving server credentials into a hook.

Use coherent tokens/primitives and colocated feature styles. If Tailwind is selected, keep complete
class names and clear component variants. Start independent requests together, avoid network
waterfalls, and lazy-load genuinely heavy routes/features. Measure bundles and interactions before
adding memoization. `useMemo`, `useCallback`, transitions, and virtualization solve different measured
problems. They do not compensate for duplicated state or an overly broad provider.

## Worked scenario and verification

An order editor page resolves the order identity. A form owns its draft/field behavior, a focused
hook owns load/save lifecycle, a service maps HTTP DTOs, and pure order rules validate the operation.
Navigate A to B while A's fetch is delayed. B must remain B when A resolves. Fail a save, preserve the
draft, then retry without duplicating the operation. If the user edits during save, an old response
must not overwrite the newer draft. Verify logout/tenant change clears protected cached content.

Test the actual domain rules and rendered behavior with the project's selected runner and React
Testing Library where appropriate. Use browser tests for critical navigation/focus journeys and
server integration where component mocks cannot prove the contract. Run defined lint, type checks,
tests, and the production build. Vite alone does not type-check TypeScript. Inspect rendered layouts
at relevant widths and keyboard/assistive interaction. Update setup docs and a current AGENTS.md
with actual architecture, state ownership, commands, and configuration. Report real checks and
remaining limitations. Read [sources](references/sources.md) for provenance and scope.
