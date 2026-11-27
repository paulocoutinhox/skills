# Application architecture and navigation

Use this guide for ordinary apps: catalogs, forms, feeds, editors, dashboards, messaging, media or
service interfaces. Read the matching current app sample, the upstream navigation guide and the
`haylen.ui` navigation reference from [sources](sources.md). The names below describe an app
structure taken from those samples. They are not a required engine directory layout.

## Set up a small, clear app structure

```text
haylen.json
source/
  main.lua
  shell.lua
  page.lua
  routes.lua
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
native/
plugins/
```

Create only the modules the product really needs. `services`, `models` and `widgets` are a
suggested layout, not special loaders. The samples also use focused root modules and `data/`.
Follow an existing convention that makes sense instead of moving every file just to look like this
tree.

| Owner | What belongs there | What does not |
| --- | --- | --- |
| `main.lua` | Register styles/theme, localization/actions, app-owned services and start the shell scene. | Every route's widget tree, request logic or gameplay loop. |
| Shell | The app scene, frame GUI, `ui.navigationTabs`/stack, message area, shared alerts/toasts and router start. | Validation/business rules, account secrets or a generic service locator. |
| Page base | A `ui.Screen` subclass with shared `build`, layout changes, back-button visibility and first-show start. | Every possible page state and business action. |
| Routes | `ui.router` route table, link/web locations and screen factories. | Data fetching or permission decisions hidden inside path parsing. |
| Screen | Parameters, its GUI tree, local draft/query/selection and presentation state. | Another screen's internals or repeated raw native calls. |
| Domain model/service | Shared domain state, requests that decide the real result, storage boundaries and changes others can watch. | Widget references and navigation side effects hidden inside data access. |
| Widget module | Repeated presentation with explicit inputs/actions. | A second navigation system or duplicated domain state. |

Read Online Store's shell, routes and browse/product/checkout for tabs, forms and collections,
Music Streaming's shell/player for media controls across the app, Photo Social for feed/composing
and Ride Hailing for map-centered UI with a non-modal sheet. Their data, payment choices, transport
and media generation are demos. Do not suggest that placing a sample order makes a payment or that
the sample map is a production navigation provider.

## Configure UI as app UI

The Online Store manifest uses orientation `any`, a resizable high-DPI window,
`design.scaling: "none"` and `ui.scaleMode: "physical"`. These are good starting choices, not
required dimensions for every app. Change only the relevant fields in the current strict schema.
Use a physical UI scale when controls should keep readable point sizes across device density.
Avoid a desktop game canvas scaled down into a phone form that nobody can read.

`ui.scale()` returns the chosen scale and the design units per UI unit, followed by physical
points per UI unit. The sample works out the available width like this:

```lua
local ui = require('haylen.ui')
local viewport = require('haylen.viewport')

local _, unitsPerUiUnit = ui.scale()
local availableWidth = viewport.safeRect().width / unitsPerUiUnit
```

Choose a breakpoint from what the content needs, not from the sample's brand dimensions. A narrow
layout can use bottom tabs and a stacked form/summary, while a wide layout uses top
navigation/sidebar and side-by-side content. Switch a `ui.navigationSplit` between collapsed and
expanded at the same breakpoint. Patch the frame with `gui:set` when its mode changes instead of
rebuilding it, and keep stable IDs so input state survives. Do not poll and recreate the whole
interface each frame.

## Mount the frame once and show screens inside it

The frame is a GUI that the app scene owns. It holds bars and an empty node where screens appear.
Screens slide inside that node while the bars stay, keeping their focus and scroll.

```lua
local scene = require('haylen.scene')
local ui = require('haylen.ui')

local Shell = {scene = {}}

function Shell.frame()
    local tabsRow = ui.row{id = 'tabs', height = 96}
    local middle = ui.column{id = 'middle', grow = 1}
    return ui.column{gap = 0, tabsRow, middle}
end

function Shell.scene:enter()
    local mountOptions = {owner = self, sharedFocus = true}
    Shell.gui = ui.mount(Shell.frame(), mountOptions)
    ui.setMessageArea({gui = Shell.gui, id = 'middle'})
    local tabs = {{id = 'catalog', root = function() return require('screens.catalog')() end}}
    local tabOptions = {gui = Shell.gui, id = 'middle', tabs = tabs, owner = self}
    Shell.navigation = ui.navigationTabs(tabOptions)
end

function Shell.start()
    scene.push(Shell.scene)
end

return Shell
```

Keep each call on one line by naming child nodes and option tables, as above. With the scene as
owner, the frame, tabs and their stacks end when the scene unloads, so no `exit` needs to unmount
them. Add the tab bar buttons to the `tabs` row and change only their look with `gui:set` from the
tabs' `onChange`.

## Build screens through the screen hooks

A screen is a `haylen.class('Name', ui.Screen)` instance with a `build` method that returns its node
table. The engine sets `gui`, `stack` and `presentation` on it. Create a fresh instance each time it
opens, because one screen object can be held only once, by one stack or presentation.

```lua
local haylen = require('haylen')
local ui = require('haylen.ui')

local ItemDetail = haylen.class('ItemDetail', ui.Screen)

function ItemDetail:init(params)
    self.title = params.title
    self.quantity = 1
end

function ItemDetail:build()
    local backButton = ui.button{text = 'Back', onClick = ui.goBack}
    local titleLabel = ui.label{text = self.title, font = 'heading'}
    local quantityLabel = ui.label{id = 'quantity', text = 'Quantity: 1'}
    local addButton = ui.button{text = 'Add one', autofocus = true, onClick = function() self:addOne() end}
    return ui.column{padding = 24, gap = 16, backButton, titleLabel, quantityLabel, addButton}
end

function ItemDetail:addOne()
    self.quantity = self.quantity + 1
    self.gui:set('quantity', {text = 'Quantity: ' .. self.quantity})
end

return ItemDetail
```

Save this as `source/screens/item-detail.lua`. From a screen already in a stack, open it with
`self.stack:push(require('screens.item-detail')({title = 'Travel notebook'}))`. In a real app the
title comes from a validated domain model, and quantity belongs to a shared cart model.

| Hook | What it is for |
| --- | --- |
| `init(params)` | Set up instance parameters/state. The screen is not built yet. |
| `build()` | Return the node table once, the first time the screen shows. |
| `appear()` / `appeared()` | Starts showing, then the transition finished and input is available. Subscribe here with `{owner = self}` when work should run only while visible. |
| `disappear()` / `disappeared()` | Covered by another screen, tab hidden or leaving. The screen keeps its GUI and state. |
| `update(dt)` / `render()` | Per-frame layout changes or drawing while the screen draws. No forced simulation or UI recreation. |
| `back()` | Return `true` to keep the screen, such as to confirm throwing away unsaved work. |
| `remove()` | The screen left for good. Owned timers/listeners/tasks end and its GUI unmounts right after. |

`ui.screenState(screen)` returns `created`, `appearing`, `shown`, `disappearing`, `hidden` or
`removed`. Use it to ignore async results that arrive late for a removed screen. A failing hook
reaches the error screen as a lifecycle failure. Do not catch programming errors to fake a loaded
route.

## Define navigation as a product contract

1. List root tabs, detail routes, presented flows, their parameter types and sign-in rules.
   Pass stable domain IDs, then load the current data the user may see through a service/model.
   Do not hand widget handles from one screen to another, or assume a link ID gives access to an
   object.
2. Pick stack operations by what you mean: `push` for a detail, `pop` or `ui.goBack()` for back,
   `replace` for the next step of a form, `popTo`/`popToRoot` to return, `setScreens` for a whole
   deep state. A change that starts while another one plays finishes the earlier one at once, so fast
   taps never leave half-shown screens. Still guard actions with side effects, such as submissions.
3. Use `ui.navigationTabs` for separate per-tab stacks. Each tab's root factory runs on first show,
   and other tabs keep their screens, scroll and fields. Selecting the shown tab pops to its root.
   System back on another tab's root goes to the first tab.
4. Use `ui.present(screen, options)` for a new flow: `sheet` with detents, `fullScreen`, `dialog`,
   `drawer` or `popover`. A presented screen can host its own `ui.navigationStack`. Dismiss with
   `self.presentation:dismiss({result = value})` and await `presentation.result`, which resolves
   `nil` when the person dismisses it. Results are JSON-compatible values.
5. Use `ui.presentAlert` for decisions and action sheets. Await its `result`, the chosen action ID.
   Use `ui.showMessage` for toasts, snackbars with undo and banners, and keep them above the bars
   with `ui.setMessageArea`.
6. Let the navigation handle system back. A focused popup or dialog takes it first. Then the layers
   go from the top presentation down to the app. In each layer the innermost stack that can pop goes
   back, then tabs return to the first tab, then a dismissible modal presentation closes. A modal
   presentation keeps the back from the layers under it even when it is not dismissible, and a
   non-modal sheet first moves down to its lowest detent. Only when nothing goes back does the root
   GUI hear `cancel` and Android leave the app. A toolbar back button calls `ui.goBack()`, and
   `ui.canGoBack()` decides whether to show it. Do not call `window.setBackLeavesApp` in such an app.
7. Use `ui.router` with typed paths such as `product/{id:integer}`, tabs, parents, details and
   presentations. `router:open(location)` builds the whole state, and `router:push(location)` opens
   a location in the visible flow. With `restore = true` the router rebuilds routed screens after the
   system ended the app. Keep drafts and scroll beyond that through the resume state of
   `haylen.storage`. Handle unmatched links with `onUnmatched` and a useful missing-item screen.

Scenes are still the right tool when the whole app changes, such as sign-in versus the main app. A
scene change moves the frame and its screens together. Scene changes return promises, and a
failed load can call the change's `onError(message)`, so handle those cases separately from screen
navigation inside one frame.

## Forms, requests and lists

For each form, list field labels, types, required rules, keyboard/return key, cleanup of input,
local checks, server checks that decide the real result and the navigation/result on success. Wrap
`ui.textField` with `ui.formField`. The checkout sample sets `formField.error` and reads
`onChange(event).value`. Use that for clear messages about each specific field.

Keep a draft table outside the rendered tree. Use stable field IDs and `gui:set` to update error,
enabled or summary properties. Do not set the field's value on every unrelated update. Native text
entry handles IME/composition, selection, copy/paste and platform keyboards. Do not read UTF-8
bytes as characters, repeat native key handling or change composing text from raw input. Use
returnKey `next`/`done`/`search` where each fits. Check keyboard avoidance and scroll-to-field on
real mobile targets. Do not put secrets into diagnostics or saved draft storage.

Submitting must have a clear idle/submitting/success/error state. Turn off repeat submits before
work starts, keep the user's input on failure and turn controls back on once an error is final.
Use backend idempotency where an operation can charge, buy or create duplicate records. A button
turned off locally cannot on its own guarantee that the service acts exactly once. Do not navigate
away as if it worked before the server accepts it. Cancel and timeout must report honest results.

For feeds/catalogs, create a `ui.collection` with item type/template and stable domain item IDs.
Get its model with `gui:collection(id)` and use `setItems` for first/replaced results or the
documented insert/remove/move/replace operations for small changes. Virtual cells reuse
presentation, so bind shown values from the item's identity and do not keep another item's
selection/photo state in a reused cell.

Define first load, refresh, empty, failure, paging and end-of-data behavior one by one. Tie each
response to the active query/page generation and account. An older search response must not replace
the newer query's list. Cancel owned work when it makes sense, and ignore stale results even when
the transport cannot undo a request that already finished. Keep all UI updates on the engine's
documented thread and avoid blocking synchronous requests in a frame callback.

## Accessibility and acceptance paths

Use theme/font roles and current localization APIs. Test long text, RTL, system text size and
high-contrast/reduced-transparency behavior. Keep images in proportion. Add accessibility names for
icon-only actions. Set a sensible `autofocus` or `gui:command(id, 'focus')`, and check keyboard
order, remote/D-pad neighbors, focus staying inside presentations and focus coming back. Do not
hard-code pointer-only gestures for main navigation. The built-in UI exposes platform screen-reader
semantics.

Check at least these real app paths, with evidence for each requested target:

- Tab → list → detail → back keeps the intended query, scroll and focus. Switching tabs and back
  keeps each tab's stack. A missing or forbidden item leads to a usable screen.
- Form editing survives resize/layout mode changes. Required/invalid/server-error states are clear.
  A workflow that works and is used again does not stay turned off after the first action.
- Back closes a popup or editing scope, then a presentation or detail, then follows the documented
  tab/root rule. A screen with unsaved work asks before it leaves.
- A link opens the intended route from a cold start and while running. Restoring after the system
  ended the app rebuilds only routed state that the user may still see.
- Out-of-order search and an account switch cannot show the wrong result or another user's data.
  Offline, timeout, revoked access and deleted-item paths are clear and the user can recover.
- Removing a screen releases work and native resources. Background/resume does not duplicate
  listeners, requests or music.

Report builds, real interaction sessions and untested hardware cases separately. A simulated
service or desktop run does not verify payment, mobile permissions or native platform UI.
