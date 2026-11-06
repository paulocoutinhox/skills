# Application architecture and navigation

Use this guide for ordinary applications: catalogs, forms, feeds, editors, dashboards, messaging,
media or service interfaces. Read the matching current app sample and UI/scene APIs from
[sources](sources.md). The naming below is an application architecture derived from those samples.
It is not a mandatory engine directory schema or an unimplemented native controller API.

## Establish a small, explicit application structure

```text
app.json
source/
  main.lua
  shell.lua
  page.lua
  style.lua
  screens/
    catalog.lua
    item-detail.lua
    checkout.lua
  services/
    catalog-service.lua
  models/
    cart.lua
  widgets/
    price-label.lua
content/
  fonts/
  images/
  locale/
plugins/
platform/
```

Create only modules the product actually needs. `services`, `models` and `widgets` are suggested
organization, not special loaders. The samples also use focused root modules and `data/`. Follow
an existing coherent convention rather than moving every file just to resemble this tree.

| Owner | What belongs there | What does not |
| --- | --- | --- |
| `main.lua` | Register styles/theme, localization/actions, app-owned services and initial shell. | Every route's widget tree, request logic or gameplay loop. |
| Shell | Route construction, push/back/tab policy, app chrome and intended app-wide overlays. | Validation/business rules, account secrets or a generic service locator. |
| Page base | Shared mount/resize/background behavior required by multiple screens. | Every possible page state and business action. |
| Screen | Screen parameters, retained GUI, local draft/query/selection and presentation state. | Another screen's internals or repeated raw native calls. |
| Domain model/service | Shared domain state, authoritative requests, persistence boundaries and observable changes. | Widget references and navigation side effects hidden inside data access. |
| Widget module | Repeated presentation with explicit inputs/actions. | A second navigation system or duplicated domain state. |

Inspect Online Store's checkout/catalog for forms/collections, Music Streaming's shell/player for
app-wide media controls, Photo Social for feed/composition and Ride Hailing for map-centered UI.
Their data, payment choices, transport and media generation are demonstrations. Replace simulations
with authorized real services when implementing a product. Do not imply sample order placement
performs a payment or that the sample map is a production navigation provider.

## Configure UI as application UI

The Online Store manifest uses orientation `any`, a resizable high-DPI window,
`design.scaling: "none"` and `ui.scaleMode: "physical"`. These are appropriate starting choices,
not required dimensions for every app. Change only the relevant fields in the current strict schema.
Use a physical UI scale when controls should retain readable point sizes across device density.
Avoid a desktop game canvas scaled down into an unreadable phone form.

`ui.scale()` returns the selected scale and the design units per UI unit, followed by physical
points per UI unit. The sample computes available width as:

```lua
local ui = require('haylen.ui')
local viewport = require('haylen.viewport')

local _, unitsPerUiUnit = ui.scale()
local availableWidth = viewport.safeRect().width / unitsPerUiUnit
```

Choose a breakpoint from content requirements, not the sample's brand dimensions. A narrow layout
can use bottom tabs and stacked form/summary, while a wide layout uses top navigation/sidebar and
side-by-side content. Use columns, rows, scroll areas, growth and max widths. Rebuild layout only
when its structural mode changes, preserving input state under stable IDs. Do not poll and recreate
the complete interface each frame. Size backgrounds separately from interactive safe-area content.

## Implement screens through the actual scene lifecycle

`haylen.class('ScreenName', scene.Scene)` gives a fresh screen instance when called. A small base
page can supply shared `mountGui`, resize adaptation and background painting, like the samples.
Keep specialized forms/data in the concrete page. A standalone detail screen also works:

```lua
local haylen = require('haylen')
local scene = require('haylen.scene')
local ui = require('haylen.ui')

local ItemDetail = haylen.class('ItemDetail', scene.Scene)

function ItemDetail:init(params)
    self.title = params.title
    self.quantity = 1
end

function ItemDetail:enter()
    self.gui = ui.mount(ui.column{
        padding = 24,
        gap = 16,
        onCancel = function()
            scene.pop()
        end,
        ui.label{text = self.title, font = 'heading'},
        ui.label{id = 'quantity', text = 'Quantity: 1'},
        ui.button{
            text = 'Add one',
            autofocus = true,
            onClick = function()
                self.quantity = self.quantity + 1

                self.gui:set('quantity', {text = 'Quantity: ' .. self.quantity})
            end,
        },
    }, {owner = self, sharedFocus = true})
end

return ItemDetail
```

Save this as `source/screens/item-detail.lua`. After the shell has installed a root screen, open
it with `scene.push(require('screens.item-detail')({title = 'Travel notebook'}))`. This example
assumes an internal validated title and an existing root. In a real app, delegate its back action
to the shell's back policy and use a domain model if quantity belongs to a shared cart.

| Hook/state | Correct responsibility |
| --- | --- |
| `init(params)` | Establish instance parameters/state. No assumption that the screen is already mounted. |
| `load(context)` | Prepare resources/preload groups. Use the documented owned async loading contract. |
| `enter(params)` | Create the retained GUI and subscriptions appropriate to entry. |
| `enterTransitionFinished()` | Work that requires entry completion and available input. |
| `pause()` / `resume()` | Covered/uncovered screen behavior. The screen remains on the stack. |
| `exit()` / `unload()` | Removal and release. Explicitly owned external resources still need correct cleanup. |
| `update(dt)` | Necessary presentation adaptation or polling supported by the API. No forced simulation or UI recreation. |

With a scene owner, the engine hides its GUI while covered, retains its focus/state and unmounts
it on unload. Do not manually unmount that GUI as if it were unowned. Owned tasks/listeners can
continue while covered, so decide whether a hidden page should keep receiving data. Unload can also
follow partial load failure. Cleanup must tolerate resources that were never acquired.

App-owned toasts or a persistent player can deliberately use a GUI without a scene owner. Such a
GUI remains until explicitly unmounted/app shutdown, so give it an actual app lifecycle. Do not make
every page global to keep it visible accidentally. `sharedFocus` allows shared shell GUIs to
participate in navigation. It does not change source/state ownership.

## Define navigation as a product contract

1. List root tabs and detail routes, their parameter types and authentication requirements. Pass
   stable domain identifiers, then resolve current authorized data through a service/model. Do not
   transfer widget handles between screens or assume a URL identifier authorizes an object.
2. Construct a fresh screen for each stack entry. The same scene object cannot be on the stack
   twice. `push` covers the previous screen, `pop` removes the top and resumes the one below,
   `replace` removes/replaces the current screen, and `popToRoot` removes details above the root.
3. Choose root-tab state explicitly. Online Store's `showTab` returns to root and replaces it.
   Filters, scroll position and drafts therefore need separate deliberate preservation if the
   product expects them. Independent per-tab history is additional app behavior, not provided by
   calling the sample's `showTab`.
4. Route toolbar back and root `onCancel` to one shell decision. UI cancel first closes its open
   popup/dialog or editing scope. At the root, define whether back selects Home or leaves the app.
   Use `window.setBackLeavesApp` consistently with this rule on applicable targets.
5. Navigation is deferred and ordered. Reserve a navigation action immediately so two taps cannot
   enqueue two detail pages before the next scene update. Settle that reservation through the
   returned promise/completion/error path. Do not infer completed navigation from an immediate
   `scene.size()` read. Consider load failure and a promise resolving false when cleared.
6. Use short directional transitions for app hierarchy when appropriate and no unnecessary
   transition on root-tab switches. Respect reduced-motion settings/options. The samples' exact
   durations are design choices. Input is normally blocked during a transition, but that does not
   eliminate duplicate requests queued before it begins.
7. Preserve a useful focus target when returning to the parent. Define unsaved-draft confirmation,
   external deep-link routing and restoration only where needed. Validate restored route IDs and
   account access, and recover to a meaningful screen when an item no longer exists.

A focused shell can guard a detail push like this in `source/shell.lua`. Its `onFailure` callback
is a required app-owned function that presents a useful load error. Other navigation entrypoints
must share the same reservation and completion policy in a real shell.

```lua
local scene = require('haylen.scene')
local window = require('haylen.window')

local Shell = {navigating = false}

function Shell.open(Screen, params, onFailure)
    if Shell.navigating or scene.transitioning() then
        return false
    end

    local destination = Screen(params)
    Shell.navigating = true

    return scene.push(destination, {
        duration = 0.24,
        effect = 'slideIn',
        direction = 'left',
        reducedMotion = 'skip',
        onComplete = function(completed)
            Shell.navigating = false

            if completed then
                window.setBackLeavesApp(false)
            end
        end,
        onError = onFailure,
    })
end

return Shell
```

The contract returns false for an intentionally ignored duplicate, otherwise the navigation
promise. Handle that distinction when observing completion. There is no inferred success when
a request is ignored. The duration/direction are example design choices. `onComplete` receives
false on dropped/failed changes and releases the reservation. `onError` receives a load failure.
Implement back/tab/root policy with the same documented operations, settling one user intent at a
time. Recompute root exit policy after completion, not before a deferred pop changes the stack.

The engine logs a failed load when a parent remains, or shows its error screen if no usable scene
remains, unless a change's `onError` handles the load failure. A failed push and an eager-unloading
replace are therefore different recovery cases. Entry/exit hook bugs still reach the error screen.
Do not catch arbitrary programming errors and present the route as successfully loaded.

## Forms, requests and lists

For each form, declare field labels, types, required rules, keyboard/return key, normalization,
local validation, authoritative server validation and the successful navigation/result. Wrap
`ui.textField` with `ui.formField`. The checkout sample sets `formField.error` and consumes
`onChange(event).value`. Apply that mechanism to meaningful field-specific messages.

Keep a draft table outside the rendered tree. Use stable field IDs and `gui:set` to update error,
enabled or summary properties. Do not assign the field's value on every unrelated update. Native
text entry handles IME/composition, selection, copy/paste and platform keyboards. Do not interpret
UTF-8 bytes as characters, duplicate native key handling or modify composing text from raw input.
Use returnKey `next`/`done`/`search` appropriately. Verify keyboard avoidance and scroll-to-field on
actual mobile destinations. Do not put secrets into diagnostics or persistent draft storage.

Submission must have an explicit idle/submitting/success/error state. Disable repeated submission
before starting work, retain user input on failure and restore controls after a settled error.
Use backend idempotency where an operation can charge, purchase or create duplicate records. A
locally disabled button alone cannot guarantee exactly-once service effects. Do not navigate away
as success before authoritative acceptance. Cancellation and timeout must have truthful outcomes.

For feeds/catalogs, create a `ui.collection` with item type/template and stable domain item IDs.
Access its model with `gui:collection(id)` and apply `setItems` for initial/replaced results or
the documented insert/remove/move/replace operations for incremental changes. Virtual cells reuse
presentation, so bind displayed values from the item's identity and do not retain another item's
selection/photo state in a recycled cell. Save/restore collection state where navigation requires it.

Define first load, refresh, empty, failure, pagination and end-of-data behavior independently.
Associate each response with the active query/page generation and account. An older search response
must not replace the newer query's list. Cancel owned work when appropriate, and reject stale
results even when underlying transport cancellation cannot undo completion. Keep all UI application
on the engine's documented thread and avoid blocking synchronous requests in a frame callback.

## Accessibility and acceptance paths

Use theme/font roles and current localization APIs. Test long text, RTL, system text size and
high-contrast/reduced-transparency behavior. Keep images proportional. Add accessibility names for
icon-only actions. Set sensible `autofocus` or `gui:command(id, 'focus')`, verify keyboard order,
remote/D-pad neighbors, dialog focus containment and focus restoration. Do not hard-code pointer-only
gestures for primary navigation. The built-in UI exposes platform screen-reader semantics.

Validate at least these actual app paths, with evidence for each requested target:

- Root tab → list → detail → back retains the intended query, scroll and focus. Repeated quick taps
  do not duplicate routes. A detail load failure leaves a usable parent/error state.
- Form editing survives resize/layout mode changes. Required/invalid/server-error states are clear.
  A successful repeated-use workflow does not become permanently disabled after the first action.
- Back dismisses a dialog or editing before leaving its page. Root back matches documented exit/tab
  policy. Unsaved work follows the chosen product rule.
- Out-of-order search and an account switch cannot display the wrong result or another user's data.
  Offline, timeout, revoked authorization and deleted-item paths are understandable and recoverable.
- Screen unload releases work and native resources. Background/resume does not duplicate listeners,
  requests or music. Process restart restores only intentionally persisted, still-authorized state.

Report builds, real interaction sessions and untested hardware cases separately. A simulated
service or desktop run does not verify payment, mobile permissions or native platform UI.
