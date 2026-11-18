# Vue feature design

## Design a customer editor

| File responsibility | Owns | Does not own |
| --- | --- | --- |
| Customer page | Route identity and feature composition. | Every field handler or API implementation. |
| Customer form | Draft, labels, field interaction, local validation presentation. | Global account state or raw HTTP policy. |
| Customer address component | A cohesive address input contract if its behavior warrants extraction. | Unrelated customer actions forwarded through dozens of props. |
| Customer editor composable | Load/save state and coordination of the editor lifecycle. | All validation, transport, formatting, and every child UI behavior. |
| Customer service | HTTP contracts and explicit response mapping. | Reactive UI state or toast policy. |
| Customer model/rules | Domain values and pure validation/calculation. | Vue instance access or browser APIs. |

Split responsibilities that change for different reasons or have their own state/lifecycle. Keep
related state and behavior together. Do not move a giant page into a giant `useCustomer` function and
call that modularity. Avoid a shared component that imports a feature-specific store or API service.
Avoid multiple parallel copies of the same editable record.

## Async transition review

List the owner, start condition, cancellation/cleanup, and commit condition for each asynchronous
operation. When route identity changes, abort or invalidate earlier loading before committing the
new result. Loading A, switching to B, then receiving A last must still display B. Saving a snapshot
does not authorize overwriting a draft edited after the save began. Define server conflict/version
behavior where concurrent edits are real. Display errors in the owning feature rather than swallowing
them into an empty record.

## JavaScript and TypeScript

Use TypeScript props/emits/models in TS projects and JSDoc/runtime boundary validation where useful
in JS projects. Do not maintain two parallel implementations. Keep files aligned with the selected
language, formatter, and naming conventions. Prefer named domain values over `any`, chained casts,
or a generic object used everywhere. Avoid speculative generic repositories and abstract factories.
Use a context-specific helper class only for actual shared support responsibilities.
