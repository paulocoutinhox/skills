---
name: haylen-app
description: Create and maintain Haylen C++/Lua applications, games and native plugins. Use for app-style navigation and retained UI, game architecture, project/plugin generation, native integration, builds or upgrades against Haylen's actual templates.
license: MIT
---

# Haylen App

Use [Haylen](https://github.com/haylen-org/haylen) for an application, game or multimedia product
built on its C++20 engine and Lua/Varn API. The researched runtime uses Lua 5.5 and implements 2D.
Future 3D architecture is not implemented feature support. A Lua project uses engine artifacts,
which the tool can build when needed. A C++ project compiles/embeds the engine.

## Choose the correct product workflow

Confirm engine revision, existing repository, product type, targets, Lua/C++ scope, navigation,
interaction devices, orientation, persistence, network/native services and delivery stage. Read the
current README/features, documentation index, applicable APIs and actual sample/template sources
before implementation. Use the selected revision's APIs, not APIs remembered from other engines.
See [sources and evidence limits](references/sources.md).

| Task | Required design and focused reading |
| --- | --- |
| Ordinary app | Retained UI, shell, screen stack, forms and domain state. Read [app architecture](references/app-architecture.md) and the matching `samples/apps/` implementation. |
| Game | World simulation, input actions, scenes and HUD. Read [game architecture](references/game-architecture.md) and `samples/games/tiny-island`. |
| Native integration/plugin | Stable Lua API and actual platform implementations. Read [plugin development](references/plugins.md), the plugin guide and selected feature templates. |
| Create, build or upgrade | Read [projects and upgrades](references/projects-and-upgrades.md), current distribution/upgrading guides and the correct template kind. |

For an ordinary app, use the app samples' `Shell`/`Page`/`screens` approach. These are application
modules built on `haylen.scene` and `haylen.ui`, not engine classes named Shell or Page. Treat a
scene as a screen controller with lifecycle and retained UI. Do not implement forms, lists or
navigation as a manually drawn game world. Use simulation only where the product requires it.

Native SDK screens are a third case: authentication, paywalls or platform UI presented by a plugin
use the plugin screen contract. They do not replace normal Lua screen navigation.

## Create the right project

The researched tooling needs Python 3.12+, CMake 3.28+, C++20 and normally Ninja. Apple targets
require macOS/Xcode. Read current Android SDK/NDK/JDK and other host requirements from upstream
instead of inventing pins. Haylen downloads pinned supporting tools. Identify downloads and required
signing/hardware before claiming that a build can complete.

The documented `haylen` launcher invokes `haylen.py`. It can also be invoked directly with a suitable
Python through uv: `uv run --no-project python /path/to/haylen/haylen.py --help`. Use native commands
without additional shell/JavaScript wrappers. Inspect the selected revision's command help.

```text
haylen --version
haylen new /path/to/my-app --kind lua --name "My App" --identifier com.example.myapp --orientation any
haylen new /path/to/my-game --kind cpp --name "My Game" --identifier com.example.mygame --orientation landscape
haylen devices
haylen run /path/to/my-app
haylen run /path/to/my-app --platform ios-simulator --device "ACTUAL_DEVICE_NAME"
haylen run /path/to/my-app --platform android --device ACTUAL_DEVICE_SERIAL
haylen run /path/to/my-app --platform web --open
```

The destination must be absent or empty. Lua is the default kind and landscape is the default
orientation, so choose app orientation explicitly. Use actual devices from `devices`. Do not replace
an existing project with a fresh scaffold. A C++ project is justified by embedding/native engine work,
not by the assumption that a Lua app cannot present a professional interface.

## Establish source ownership and architecture

| Location | Responsibility |
| --- | --- |
| `app.json` | Strict identity, version, window/design, lifecycle, plugin configuration and autoload declarations. |
| `source/main.lua` | Small startup composition: configuration, theme/localization/actions and first screen. |
| App `source/shell.lua`, `page.lua`, `screens/` | Shared navigation/chrome, focused page base and one screen class per file. These follow app samples, not mandatory engine filenames. |
| Focused `source/` modules | Domain rules, services, data models and reusable UI. Game projects normally use `scenes/`, `systems/`, `entities/` and `ui/`. |
| `content/` | Fonts, images, audio, locale data, input/theme/preload data, maps and shaders. |
| `plugins/<id>/` | Plugin manifest, Lua modules and declared native implementation folders. |
| `platform/<template>/` | Developer-owned native project source. Lua templates include apple/android/web/windows/linux. C++ templates include android/web, with CMake handling the other targets. |
| A native project's `haylen/` | Generated engine/plugin integration. Regenerate it from configuration. |
| Engine `build/` and `.tools/` | Outputs, artifacts, logs and downloaded tools. Never the application's source of truth. |

Keep one class, screen, enum or focused module per appropriately named file. Prefer hyphenated
filenames where valid. Use explicit owners, readable names and blank lines between responsibilities.
Extract shared UI or context helpers when repetition warrants it. Do not introduce a universal
manager, duplicate service calls across screens, speculative abstractions or compatibility shims.

Asset paths are relative to `content/`: `assets.texture('images/hero.png')` addresses
`content/images/hero.png`. Module paths are relative to `source/`:
`require('screens.order-detail')` loads `source/screens/order-detail.lua`. Plugin module namespaces
belong to their IDs. Do not shadow them with app modules or use absolute machine paths in packages.

## Build ordinary applications as applications

1. Choose the closest actual app sample: Online Store for catalog/forms, Music Streaming for
   persistent player chrome, Photo Social for feeds/composition or Ride Hailing for map-oriented UI.
   Inspect its `main`, `shell`, `page`, style/widgets and relevant screens. Extract the architecture,
   not its fake business data, branding or simulated service behavior.
2. Keep the shell responsible for routes, tabs, back policy and shared chrome. Keep each page
   responsible for its UI and screen-local state. Put durable domain state and network/storage
   boundaries in focused modules with a lifetime appropriate to the application or account.
3. Use `scene.push(Screen(params), options)` for a detail screen, `scene.pop(options)` for back,
   `scene.replace(...)` when replacing the current screen and `scene.popToRoot()` for root return.
   Instantiate a fresh screen per stack entry. Do not invent `UIViewController` methods for Lua.
4. Specify tab behavior. The Online Store shell pops to root and replaces it on a tab switch. This
   does not preserve an independent stack per tab. Preserve selected filters, drafts or scroll state
   explicitly when required, and define restoration before introducing multiple retained stacks.
5. Route root `onCancel` through the shell. Let the UI close dialogs, menus and text editing first.
   Define root exit versus switching to the home tab, and set `window.setBackLeavesApp` to match.
   Re-evaluate stack-dependent policy after navigation completes, not from a stale stack size.
6. Mount retained UI once with `ui.mount(tree, {owner = self, sharedFocus = true})` when shared
   shell focus is needed. Patch values with `gui:set`. Replace a subtree only when structure changes.
   Keep stable node/item IDs so typing, focus and list state survive legitimate updates.
7. Follow the app samples' `design.scaling = 'none'` and `ui.scaleMode = 'physical'` when suitable for
   application UI. Use containers, safe areas, content max widths and width-dependent layouts. Never
   force every phone form into a fixed game canvas. Read UI units before defining breakpoints.
8. Implement real forms, validation, submission state and service errors. Use `ui.formField` around
   typed `ui.textField` controls, native keyboard options and explicit event values. Do not recreate
   a field every frame, overwrite composing text or treat the sample checkout as real payment code.
9. Use `ui.collection` for large lists/grids with stable item IDs, templates and incremental updates.
   Handle loading, empty, error and pagination states. Retain intended selection/scroll state and
   reject obsolete query/account responses before they update the current view.
10. Provide theme roles, localization/RTL, readable text, accessibility labels, keyboard/remote focus
    and reduced-motion transitions. `haylen.imgui` is for developer tooling, not ordinary app UI.

The [app guide](references/app-architecture.md) includes exact lifecycle/navigation semantics,
screen code, form/list procedures and realistic acceptance paths.

## Build games with explicit simulation and presentation

Compose boot/menu/gameplay/pause/results scenes. Keep a run's world/entity state separate from HUD,
rendering, input adaptation, persistence and audio preferences. Use preload groups in `load`,
action maps for devices and the selected simulation's time contract. Fixed-step physics can use
`fixedUpdate(dt)`. The actual Tiny Island sample updates its game system in `update(dt)`, so fixed
update is not an engine requirement for every game.

Render the world with appropriate viewport/camera APIs and the HUD with retained UI. Gate raw
pointer/keyboard gameplay through `ui.usingPointer()` and `ui.usingKeyboard()`. Pause deliberately
for overlays and lifecycle changes, clear virtual input when needed, and retain the user's audio
preference across interruption/resume. Do not turn every game entity into a scene-stack entry.
See [game architecture and verification](references/game-architecture.md).

## Respect lifecycle, deferred navigation and asynchronous ownership

`load` prepares a scene, `enter` mounts its active interface, `pause` covers it and `resume` uncovers
it. `exit`/`unload` remove it. Owned GUI/listeners/tasks stop on unload, not merely because another
screen covers it. Cleanup must also handle a partially failed load. Process/game pause
(`paused`/`unpaused`) differs from stack `pause`/`resume` and app inactive/background events.

Navigation requests are deferred to a scene update and queued in order. A call to `push` does not
immediately change `scene.size()`. Disable duplicate navigation/submission synchronously, then use
the returned promise or completion contract to settle state. A navigation promise may reject on load
failure or resolve false if a clear drops it. Do not treat queued, loaded and interactive as identical.
Use `enterTransitionFinished` when work specifically requires completed entry/input availability.
Use a change's `onError(message)` for a deliberate recoverable load-failure UI. A failed `push`
can retain its parent, while a replacement that unloaded the old screen can leave no usable screen.
Errors inside entry/exit hooks still reach the engine error screen and require correction.

Bind tasks/listeners to the correct scene/account owner. Check request identity for out-of-order
search responses. Persist necessary data on documented lifecycle events rather than relying on an
exit callback after process death. Keep CPU/I/O off the frame where appropriate using actual engine
APIs. C++ uses RAII, explicit ownership and safe dispatch, with no callbacks into destroyed objects.

## Create and integrate plugins through the engine contracts

```text
haylen plugin new /path/to/plugins/device-kit --id device-kit --with camera,microphone
haylen plugin add /path/to/plugins/device-kit --app /path/to/my-app
haylen plugin list --app /path/to/my-app
```

The new folder must be absent/empty and its basename must equal the dash-case ID. The generator
uses `templates/plugin` and chosen `templates/plugin-features` fragments. Current optional features
are camera, microphone, location and banner. A generated banner is a native UI feature, not an ad
network implementation. Feature availability still depends on target implementation and hardware.

Define the manifest, typed app parameters, dependencies and platform declarations before exposing
a stable Lua module from `source/init.lua`. That Lua file contains the public API. Obtain
`platform.plugin(id)` and use its `call`, `send`, `on`, stream and `openScreen` contracts. Keep wire
method names inside the plugin API, validate results and handle explicit denied/unsupported/error
outcomes. Never simulate success for a missing native implementation.

Implement Apple `HaylenPlugin`, Android `dev.haylen.HaylenPlugin`, web module `load(context)` or
the desktop native interface according to the selected template. Use engine permission, thread,
callback, screen and lifecycle services. A native SDK screen must finish/cancel exactly once, keep
the app covered until UI really closes and handle supported restoration. Ordinary app page pushes
continue to use the scene stack. See [the complete plugin workflow](references/plugins.md).

## Build, inspect artifacts and update templates deliberately

```text
haylen run /path/to/my-app --platform android --config Release --build-only
haylen check /path/to/my-app --platform android --config Release
haylen prepare /path/to/my-app --platform ios-simulator
haylen platform diff /path/to/my-app apple
haylen package /path/to/my-app -o /path/to/my-app.zip
```

`run` builds and optionally launches. `--build-only` does not test runtime behavior. `prepare`
produces integration/artifacts for native IDE work. `check` compares the **last build** against
engine/plugin requirements and fails on missing requirements. Build the intended target/configuration
first. `run`'s ordinary diagnostic warnings do not replace a successful explicit `check`.

A package ZIP has `app.json` at its root and the supported source/content/plugin subset. It is not
a signed application, Android bundle or store submission. Use current protected-release, signing and
distribution procedures for actual release artifacts. Keep debug services and secrets out of release.

For upgrades, compare the current engine revision's layered templates to developer-owned projects,
merge intentional changes, regenerate `haylen/` and rebuild. Use a separate scratch project/plugin
for comparison, with matching plugin ID/features. `platform diff` is read-only. There is no documented
universal project/plugin upgrade command. Plugin add copies/replaces the installed plugin, so merge
customizations deliberately. Follow [the upgrade procedure](references/projects-and-upgrades.md).

For live Lua diagnosis, start the app through `haylen run` in Debug and attach to its reported DAP
relay. Installing or manually launching a binary does not establish that development connection.
Inspect the current top scene and owner lifetime before scheduling asynchronous actions. Use native
UI tests for native SDK sheets. Keep debugger execution out of protected releases.

After release preparation, inspect the actual signed artifact and protected content separately from
`haylen check`. Reinstall/restart the tested final binary after source/configuration changes. The
[debugging and release-evidence guide](references/debugging-and-release-evidence.md) covers DAP
handshake/evaluation boundaries, scene ownership, exact content verification and session cleanup.

## Developer extensions and verification

Application debug-console commands use `haylen.debug.addCommand(name, handler, options)` with a
correct owner/help/argument contract. This is different from a build-CLI extension. Read the actual
dispatcher before changing it. Separately requested automation uses Python/uv. Do not add wrappers,
source refresh tools or a fictional universal commands directory.

Test the selected workflow through desktop development, actual requested simulators/emulators and
hardware-dependent cases. Verify startup, navigation/teardown, forms and repeated actions, long/RTL
text, resizing/safe areas, focus/accessibility, background/resume/process death, async failure and
cleanup. For plugins, test the real native implementation, cancellation/denial and Release retention.
For games, also verify pause/time/input/render/save behavior. A desktop mock is not native coverage.

Deliver focused source, source/template revision and ownership decisions, actual command results,
artifacts and unresolved hardware/signing/account needs. Update the target project's AGENTS.md with
its present architecture, routes/scenes, state/service ownership, plugins, generated boundaries and
commands. Distinguish static checks, builds, runtime sessions and store evidence. Only a user request
updates this collection's stored engine knowledge.
