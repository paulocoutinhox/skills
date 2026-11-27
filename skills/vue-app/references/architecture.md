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

Split work that changes for different reasons or has its own state or lifecycle. Keep related state
and behavior together. Do not move a giant page into a giant `useCustomer` function and call that
modular. Avoid a shared component that imports a feature-specific store or API service. Avoid
several parallel copies of the same editable record.

## Async transition review

For each async operation, list its owner, start condition, cancellation or cleanup, and the
condition for committing its result. When the route identity changes, abort or ignore earlier
loading before committing the new result. Loading A, switching to B, and then getting A's response
last must still show B. Saving a snapshot does not give the right to overwrite a draft that was
edited after the save began. Define server conflict and version behavior where edits can really
happen at the same time. Show errors in the feature that owns them, instead of hiding them as an
empty record.

## JavaScript and TypeScript

Use TypeScript props, emits and models in TS projects. Use JSDoc and runtime checks at the
boundaries where they help in JS projects. Do not keep two parallel implementations. Keep files in
line with the chosen language, formatter and naming conventions. Prefer named domain values over
`any`, chained casts or one generic object used everywhere. Avoid generic repositories and abstract
factories built for guessed needs. Use a helper class for one context only when there is real shared
support work.
