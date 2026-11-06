# React feature and lifecycle review

## Responsibility test

A file should have a coherent reason to change. Separate substantial UI behavior from transport and
domain calculations. Keep a component's owned state and events together. A shared button should not
import an order API or authentication store. An order service should not call a React state setter.
A hook should hide a real workflow rather than export fifty fields from unrelated responsibilities.
Single-use components are justified by cohesion, not only reuse. Additional abstractions must reduce
what the caller needs to understand.

Before extracting, identify the state owner, input/output contract, lifecycle, and dependency direction.
After extracting, trace one realistic change. Editing a field rule should not require changing unrelated
providers or pages. Do not introduce a configurable UI framework to avoid writing three clear forms.

## Async state transitions

Specify operation identity, pending state, cancellation/invalidation, failure, and commit conditions.
For a record fetch, results are valid only for the current record/query and owner lifetime. For a save,
the server mutation may continue after the browser aborts. Reconcile using actual server state and
idempotency/version contracts. Resetting a spinner is not proof that a mutation did not happen.
Keep the user's newer draft safe when an older save response arrives.

Strict Mode and remounting must not leave duplicate listeners or resources. Clean up effects instead
of suppressing them with a permanent initialized flag. A per-request server cache and a module-global
browser cache have different lifetimes. Do not apply Next.js-specific APIs in a plain Vite app.

## Language and tooling

Use explicit props/model types and discriminated states in TypeScript where they make invalid states
unrepresentable. Use JavaScript intentionally with appropriate contract documentation and runtime
boundary checks. Keep only one implementation. Prefer named intermediate values and blank lines
between responsibilities over nested expressions. Comments explain necessary intent in complete
English sentences. Formatter/linter scripts follow the actual project, not assumed command names.
