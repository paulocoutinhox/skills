---
name: react-app
description: Build and evolve modular React applications in JavaScript or TypeScript. Use for component and hook design, state ownership, routes, forms, data access, async effects, accessibility, and production checks.
license: MIT
---

# React App

Build React applications whose behavior is easy to understand, debug and change in one place. Keep
components, hooks, transport and domain rules well grouped. Use the chosen JavaScript or TypeScript
language without keeping duplicate implementations. This skill bundles no scaffolding script.

## Settle product and rendering needs

Before editing, inspect AGENTS.md, the current framework and router, package scripts, dependencies
and the lockfile. Identify the key user journeys, browser support, SEO and rendering needs,
account/tenant boundaries, API contracts, localization and deployment. Keep a sound existing
architecture and the user's choices.

For a new client-rendered application, this collection defaults to Vite and function components.
Prefer TypeScript if no language is chosen. Scaffold with
`npm create vite@latest my-app -- --template react-ts`, or `react` for JavaScript, in the intended
parent directory. Inspect the current Node requirements and the generated scripts. Use the latest
compatible dependencies and keep the lockfile. Do not use Create React App or copy outdated setup
recipes.

React's official guidance recommends a suitable framework for new production applications. Our Vite
SPA default is a project preference for client-only work. If you need SSR, SSG, server functions or
built-in data routing, make the framework choice explicitly and follow its current contracts. Do
not present Next.js APIs as core React, and do not quietly replace the chosen platform.

## Set feature boundaries

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

Use only the directories you need. A route puts features together. A component owns one clear piece
of UI. A hook owns focused React state and effect lifecycle. A service owns transport and
operations. Pure functions own rules that do not depend on the framework. Keep dependencies pointing
toward clear domain and infrastructure boundaries. Do not import pages into shared primitives. Avoid
circular imports between features.

Put one component in each source file. Match names and filenames to project and tool conventions,
and prefer hyphens when allowed. Extract a large single-use responsibility when it helps. Do not
create a generic field renderer, a universal repository or a wrapper that only forwards props, just
for possible future reuse. A giant custom hook behind a tiny page is still a giant implementation.
Keep each function call on one line, and name intermediate values when arguments get complex. If
the project uses Prettier, keep or set a wide `printWidth`, such as 320, and join calls that a
narrower setting wrapped. See [architecture and async review](references/architecture.md).

## Design component contracts

Use explicit props, stable event contracts, and composition through children/slots in the React
way. Keep components pure during render. Do not define component functions inside another
component. That changes their identity and can reset state. Use stable data IDs for list keys. Use
keys on purpose to reset an editor when its record changes. Array positions are bad keys for records
that can change or be reordered. Keep local UI behavior close to the element or component that owns
it.

Avoid combinations of boolean props that create contradictory states. Use a clear variant or state
model when modes exclude each other. Keep a real API for each component instead of leaking a whole
controller, store or internal mutable object. Public props and events must show intent. Validate
untrusted API data at the boundary. TypeScript types and casts do not check network responses.

## Choose one owner for each state

| State kind | Owner |
| --- | --- |
| Draft input, dialog visibility, local selection | Owning component or focused custom hook. |
| Shareable filters/search/page | Validated router/URL state. |
| Values calculated from props/state | Derived during render, not mirrored by an effect. |
| Server records and mutations | Router data APIs or an intentional query layer/cache. |
| Cross-feature client state | A focused provider/store only when real independent consumers need it. |

Lift state to the nearest shared owner that makes sense. Use a reducer when named, related
transitions make a workflow clearer. Use context for scoped dependencies or small shared state, and
think about the provider value identity and update scope. Do not make a global context carry every
keystroke. For large shared client state, choose a maintained library based on the needs and the
existing project. For example, use Redux Toolkit for explicit complex workflows, or Zustand for a
smaller external store. Do not install more than one store, and do not claim one is always best.

Use a maintained query library when freshness, cancellation, deduplication, invalidation and
optimistic mutation lifecycles make it worth it. Do not copy its records into a separate global
store. Define cache keys scoped to identity and tenant, and clear protected state on logout or
account switch. Never use a frontend store or route guard as the authorization boundary.

## Hooks and syncing with outside systems

Hooks combine stateful behavior and start with `use`. Call them only at the supported top level, not
inside loops, conditions, event handlers or arbitrary functions. The `use` API is the documented
exception and can be called conditionally. Pure helpers do not need hooks. Return a small, clear
contract to callers, not every internal setter and implementation detail.

Use effects to sync with external systems. Calculate derived render values directly. Put the
mutation for a user action in its event or action workflow, not in an effect that watches a submit
flag. Follow the dependency rules, and fix unstable dependencies at their cause. Do not silence the
linter to hide stale closures. For updates based on the previous state, use the right functional
update. Refs hold mutable values that are not rendered. They are not a hidden second store for data
on screen.

Every subscription, listener, timer, observer and request needs an owner and a rule for cleanup or
commit. Abort or ignore replaced work so an old response cannot overwrite the current route or
query. Cancelling alone does not undo a server mutation. Define idempotency (safe to repeat) and how
to fix differences with the server where the operation needs them. Development Strict Mode can
reveal missing cleanup. Do not remove it just to make duplicate effects go away. Do not let
rendering or an effect charge a customer.

## Forms, navigation, and errors

Keep form drafts, field display, submission flow, domain validation and transport apart where each
is big enough to need it. Use labeled semantic inputs, correct types and autocomplete, keyboard
support, errors linked to their fields, focus restoration and accessible status messages. Keep
drafts after failures. Prevent duplicate submission, and keep the server-side rules in force. For
large forms, use a maintained schema or form library when the real needs call for it, not for every
simple input. `useActionState` and a `<form action>` function can own the pending state and the
latest result with plain client functions. Server Functions belong to a framework that supports
them, not to a Vite SPA.

Show loading, empty, success, denied, validation, conflict and transport failure as separate states.
Do not turn a failed fetch into an empty list that looks successful. Follow the chosen framework's
error boundaries and route-error mechanism. Error boundaries do not catch every rejected async event
handler. Handle those failures where the operation happens.

Use route contracts and real not-found states. Define what happens to unsaved changes when that
applies. For query changes while the user types, decide on cancellation, debounce and navigation
explicitly. Do not add a manual router or custom query cache around a library that already does
those jobs.

## Security, styling, and measured performance

Keep secrets out of client bundles and public environment variables. Treat dynamic HTML, URLs,
embedded third-party content, storage and messages as untrusted. Use `dangerouslySetInnerHTML` only
with a justified trust and sanitization contract. Scope protected data by the real user and tenant
permission. SSR and server components must not share mutable request data between users. Follow the
chosen framework's server/client module boundaries instead of moving server credentials into a hook.

Use consistent tokens and primitives, and keep feature styles next to their feature. If Tailwind is
chosen, keep complete class names and clear component variants. Start independent requests
together, avoid network waterfalls, and lazy-load routes and features that are truly heavy. Measure
bundles and interactions before adding memoization. `useMemo`, `useCallback`, transitions and
virtualization solve different measured problems. They do not make up for duplicated state or a
provider that covers too much. When React Compiler is enabled, rely on it for new memoization. Use
`useMemo`/`useCallback` only as a precise escape hatch, such as a value used as an effect
dependency. Keep existing manual memoization unless you test its removal, because removing it can
change the compiled output.

## Worked scenario and checks

An order editor page resolves the order ID. A form owns its draft and field behavior. A focused hook
owns the load/save lifecycle. A service maps HTTP DTOs (data transfer objects). Pure order rules
validate the operation. Navigate from A to B while A's fetch is delayed. B must stay B when A's
response arrives. Make a save fail, keep the draft, then retry without running the operation twice.
If the user edits during a save, an old response must not overwrite the newer draft. Check that
logout or a tenant change clears protected cached content.

Test the real domain rules and rendered behavior with the project's chosen runner, and with React
Testing Library where it fits. Use browser tests for key navigation and focus journeys. Use server
integration tests where component mocks cannot prove the contract. Read the `package.json` scripts,
then run the defined lint, type checks, tests and the production build. If the project does not
define a check, report that instead of inventing its command. Vite alone does not type-check
TypeScript. A failing check blocks completion. Fix its cause, or report the exact failure and the
remaining work. Inspect rendered layouts at the widths that matter, and check keyboard and assistive
technology use. Update the README and a current AGENTS.md with the real architecture, state
ownership, commands and configuration. Report the checks you really ran and the limits that remain.
Read [sources](references/sources.md) for where the guidance comes from and what it covers.
