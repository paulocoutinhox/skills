# React feature and lifecycle review

## Responsibility test

A file should have one clear reason to change. Keep large UI behavior apart from transport and
domain calculations. Keep a component's own state and events together. A shared button should not
import an order API or an authentication store. An order service should not call a React state
setter. A hook should hide a real workflow, not export fifty fields from unrelated jobs. A
single-use component is justified when it groups related work, not only when it is reused. Each
extra abstraction must reduce what the caller needs to understand.

Before extracting, identify the state owner, the input/output contract, the lifecycle and the
direction of dependencies. After extracting, walk through one realistic change. Editing a field
rule should not require changes to unrelated providers or pages. Do not build a configurable UI
framework to avoid writing three clear forms.

## Async state transitions

Define the operation's ID, pending state, cancellation or invalidation, failure and the conditions
for committing a result. For a record fetch, results are valid only for the current record or query
and while the owner still exists. For a save, the server mutation may continue after the browser
aborts. Fix differences using the real server state and idempotency or version contracts. Resetting
a spinner does not prove that a mutation did not happen. Keep the user's newer draft safe when an
older save response arrives.

Strict Mode and remounting must not leave duplicate listeners or resources. Clean up effects instead
of blocking them with a permanent "initialized" flag. A per-request server cache and a module-global
browser cache live for different lengths of time. Do not use Next.js-specific APIs in a plain Vite
app.

## Language and tooling

In TypeScript, use explicit prop and model types and discriminated states where they make invalid
states impossible to write. Use JavaScript on purpose, with suitable contract documentation and
runtime checks at the boundaries. Keep only one implementation. Prefer named intermediate values and
blank lines between responsibilities over nested expressions. Comments explain needed intent in
complete English sentences. Formatter and linter scripts follow the real project, not assumed
command names.
