---
name: haylen-app
description: Create and maintain Haylen C++/Lua applications, games and native plugins. Use for app screen navigation and retained UI, game architecture, project/plugin generation, haylen.json platform customization, SDK builds, verification, packaging or upgrades against Haylen's actual templates.
license: MIT
---

# Haylen App

Use [Haylen](https://github.com/haylen-org/haylen) for an application, game or multimedia product
built on its C++20 engine and Lua API. The researched runtime uses Lua 5.5 through Varn and
implements 2D. Future 3D architecture is not implemented feature support. Engines are built once per
target into SDKs, and apps link those SDKs. A Lua app ships its package. A C++ app compiles its own
sources against the same SDK through the same build backends.

## Choose the correct product workflow

Confirm engine revision, existing repository, product type, targets, Lua/C++ scope, navigation,
interaction devices, orientation, persistence, network/native services and delivery stage. Read the
current README/features, documentation index, applicable APIs and actual sample/template sources
before implementation. Use the selected revision's APIs, not APIs remembered from other engines or
from an earlier Haylen layout. See [sources and evidence limits](references/sources.md).

| Task | Required design and focused reading |
| --- | --- |
| Ordinary app | Frame, screens, navigation stacks/tabs, presentations, forms and domain state. Read [app architecture](references/app-architecture.md), the upstream navigation guide and the matching `samples/apps/` implementation. |
| Game | World simulation, input actions, scenes and HUD. Read [game architecture](references/game-architecture.md) and `samples/games/tiny-island`. |
| Native integration/plugin | Stable Lua API and actual platform implementations. Read [plugin development](references/plugins.md), the plugin guide and `templates/plugin`. |
| Create, build, package or upgrade | Read [projects and upgrades](references/projects-and-upgrades.md), the command reference, distribution and upgrading guides. |

An ordinary app mounts one frame GUI in a scene, then shows its pages as `ui.Screen` classes inside
`ui.navigationStack`, `ui.navigationTabs` or `ui.navigationSplit`. The app samples name their frame
module `Shell` and their screen base `Page`. Those are application modules, not engine classes.
Scenes are whole flows such as sign-in, the main app or a game level. Do not implement forms, lists
or navigation as a manually drawn game world, and do not push one scene per app page.

Native SDK screens are a third case: authentication, paywalls or platform UI presented by a plugin
use the plugin screen contract through `handle:openScreen`. They are not navigation screens.

## Create the right project

The `haylen` launcher at the engine checkout root (`haylen.cmd` on Windows) runs the `tools/haylen`
package through uv, which supplies its Python. Building SDKs needs CMake 3.28+, Ninja and a C++20
compiler. Apple targets need macOS and Xcode. Android needs the Android SDK. Run `haylen doctor`
for what this machine has and lacks per target. It downloads nothing and accepts no license. Other
pinned tools download when a build first needs them. Identify downloads and required signing or
hardware before claiming that a build can complete.

```text
haylen --version
haylen doctor --target ios-simulator
haylen sdk build --target player
haylen sdk build --target ios-simulator
haylen new /path/to/my-app --kind lua --name "My App" --identifier com.example.myapp --orientation any
haylen new /path/to/my-game --kind cpp --name "My Game" --identifier com.example.mygame --orientation landscape
haylen devices
haylen app run /path/to/my-app
haylen app run /path/to/my-app --target ios-simulator --device "ACTUAL_DEVICE_ID"
haylen app run /path/to/my-app --target web --open
```

`sdk build` is the only command that compiles the engine for apps. An app command whose target has
no matching SDK stops and prints the `sdk build` command to run. Run it, then repeat the app command.
`new` needs an absent or empty folder. Lua is the default kind and landscape the default orientation,
so choose app orientation explicitly. Use actual identifiers from `devices`. Do not replace an
existing project with a fresh scaffold. A C++ app is justified by native engine work, not by the
assumption that a Lua app cannot present a professional interface.

## Establish source ownership and architecture

| Location | Responsibility |
| --- | --- |
| `haylen.json` | Strict identity, `version`, integer `build`, window/design, lifecycle, autoloads, `kind`, `cpp`, `plugins` and the `platforms` customization sections. |
| `haylen.lock` | Commits pinned for git plugin references. Keep it under version control. |
| `source/main.lua` | Lua entrypoint: theme/localization/actions and the first scene. A C++ app starts from `src/App.cpp`, which `cpp.sources` names. |
| App `source/shell.lua`, `page.lua`, `screens/` | Frame, routes, screen base and one screen class per file. These follow app samples, not mandatory engine filenames. |
| Focused `source/` modules | Domain rules, services, data models and reusable widgets. Game projects normally use `scenes/`, `systems/`, `entities/` and `ui/`. |
| `content/` | Fonts, images, audio, locale data, input/theme/preload data, maps and shaders. |
| `native/<platform>/` | App bridge handlers named by `platforms.apple.sources`, `platforms.android.sources` and `platforms.web.scripts`. |
| `plugins/<id>/` | Copied plugin manifest, Lua modules and native parts. Referenced plugins live elsewhere. |
| `config/` or similar | Files named by `file` plugin parameters or platform `files`, kept outside the package. |
| `build/apps/<app>-<hash>/` | Generated, disposable native projects, build trees, products and staged packages. Never edit them. |
| `platform/android/keystore/`, `dist/` | Ignored signing keys written by `app sign`, and packages written by `app package`. |

The app holds no platform project. Change a generated project only through `platforms` keys and
files of the app repository that `files` names. `haylen project inspect` shows every resolved value
with its origin. Keep one class, screen, enum or focused module per appropriately named file. Prefer
hyphenated filenames where valid. Do not introduce a universal manager, duplicate service calls
across screens, speculative abstractions or compatibility shims.

Asset paths are relative to `content/`: `assets.texture('images/hero.png')` addresses
`content/images/hero.png`. Module paths are relative to `source/`:
`require('screens.order-detail')` loads `source/screens/order-detail.lua`. A plugin ID owns its
module namespace. An app module whose first name part equals a plugin ID stops the app at start.

Keep each function call on one line. Extract named intermediate values or option tables instead of
continuation lines aligned under the open parenthesis, and never split one string literal into
adjacent literals. `haylen new` and `plugin new` write a `.clang-format` whose `ColumnLimit` is
1000000 in the researched revision. Under the owner's convention set it to `ColumnLimit: 0` so
clang-format never introduces call wrapping. That setting preserves existing line breaks, so join
already wrapped calls by hand once before formatting.

## Build ordinary applications as applications

1. Choose the closest actual app sample: Online Store for catalog/forms, Music Streaming for
   persistent player chrome, Photo Social for feeds/composition or Ride Hailing for map-oriented UI.
   Inspect its `main`, `shell`, `page`, `routes`, style/widgets and relevant screens. Smart Home and
   Car Dashboard are single-panel scene apps without a shell or routes. Extract the architecture,
   not the fake data, branding or simulated services.
2. Mount the frame once in an app scene with `{owner = self, sharedFocus = true}`. Keep bars, tabs
   and shared chrome there, with an empty node such as `middle` for the screens. Put durable domain
   state and network/storage boundaries in focused modules with an application or account lifetime.
3. Write each page as `haylen.class('Name', ui.Screen)` with a `build` method that returns its node
   table. Push a fresh instance per entry with `self.stack:push(Detail(params))`. Back uses
   `ui.goBack()`. `replace`, `popTo`, `popToRoot` and `setScreens` cover the other stack changes.
4. Use `ui.navigationTabs` when each tab keeps its own stack, scroll and fields. Selecting the shown
   tab pops it to its root. Use `ui.navigationSplit` for list/detail that collapses on narrow widths.
5. Present new flows with `ui.present` (sheet, fullScreen, dialog, drawer, popover) and await the
   presentation `result`. Ask with `ui.presentAlert` and confirm with `ui.showMessage`.
6. Let the navigation own the system back. A screen keeps unsaved work by returning `true` from
   `back` and asking first. An app built on the navigation never calls `window.setBackLeavesApp`.
7. Use `ui.router` for links and restoration with typed routes. Restore only still-authorized,
   intentionally persisted state, and recover to a meaningful screen when an item no longer exists.
8. Follow the app samples' `design.scaling = 'none'` and `ui.scaleMode = 'physical'` when suitable.
   Use containers, safe areas, content max widths and width-dependent layouts. Patch values with
   `gui:set` and keep stable node/item IDs so typing, focus and list state survive updates.
9. Implement real forms with `ui.formField` around typed `ui.textField` controls, native keyboard
   options and explicit submission states. Use `ui.collection` for large lists with stable item IDs.
10. Provide theme roles, localization/RTL, accessibility labels, keyboard/remote focus and reduced
    motion. `haylen.imgui` is for developer tooling, not ordinary app UI.

The [app guide](references/app-architecture.md) includes screen hooks, navigation code, form/list
procedures and acceptance paths.

## Build games with explicit simulation and presentation

Compose boot/menu/gameplay/pause/results scenes. Keep a run's world/entity state separate from HUD,
rendering, input adaptation, persistence and audio preferences. Use preload groups in `load`,
action maps for devices and the selected simulation's time contract. Fixed-step physics can use
`fixedUpdate(dt)`. Tiny Island updates its game system in `update(dt)`, so fixed update is not an
engine requirement for every game.

Render the world with appropriate viewport/camera APIs and the HUD with retained UI. Gate raw
pointer/keyboard gameplay through `ui.usingPointer()` and `ui.usingKeyboard()`. Pause deliberately
for overlays and lifecycle changes, clear virtual input when needed, and retain the user's audio
preference across interruption/resume. Do not turn every game entity into a scene-stack entry.
See [game architecture and verification](references/game-architecture.md).

## Respect lifecycle, deferred changes and asynchronous ownership

Scenes: `load` prepares, `enter` mounts, `pause` covers, `resume` uncovers, and `exit`/`unload`
remove. Owned GUI/listeners/tasks stop on unload, not merely because another scene covers it.
Process/game pause (`paused`/`unpaused`) differs from stack `pause`/`resume` and app
inactive/background events. Scene changes return promises that resolve `true`, resolve `false`
when `scene.clear` drops them, or reject on load failure. A `push` does not immediately change
`scene.size()`. Use a change's `onError(message)` for a deliberate recoverable load-failure UI.

Screens: `build` runs once, `appear`/`appeared` and `disappear`/`disappeared` follow visibility,
and `remove` ends the screen for good with everything it owns. A covered screen keeps its GUI and
state. Bind listeners with `{owner = self}` in `appear` when they should run only while visible.

Bind tasks/listeners to the correct scene, screen or account owner. Check request identity for
out-of-order responses. Persist necessary data on documented lifecycle events rather than relying
on an exit callback after process death. C++ uses RAII, explicit ownership and safe dispatch.

## Create and integrate plugins through the engine contracts

```text
haylen plugin new /path/to/plugins/device-kit
haylen plugin add /path/to/plugins/device-kit --app /path/to/my-app
haylen plugin add /path/to/plugins/device-kit --reference --app /path/to/my-app
haylen plugin list --app /path/to/my-app
haylen project inspect /path/to/my-app --target android
```

The new folder must be absent or empty. Its basename is the default dash-case ID. `plugin new`
copies `templates/plugin`, whose native part on every platform answers `<id>.echo` and sends
`<id>.echoed`. There are no generated feature fragments. Camera, location, ads and similar
capabilities are separate plugins or code the author writes with each platform's real APIs.

Write `plugin.json` with `interface`, `id`, `name`, `version`, `description` and `implementations`,
then optional `dependencies`, `permissions`, `parameters` and typed `contributions`. Expose a stable
Lua module from `source/init.lua`. Obtain `platform.plugin(id)` and use its `call`, `send`, `on`,
stream and `openScreen` contracts. Handle explicit `noHandler`, `unsupported`, `denied` and
cancellation outcomes. Never simulate success for a missing native implementation.

Implement the Apple class conforming to `HaylenPlugin`, the Android class extending
`dev.haylen.HaylenPlugin`, the web module's `load(context)` and the desktop C++ library from the
template. Register owned permissions with the native context and call `requirePermission` before
use. A native SDK screen must finish once, keep the app covered until its UI really closes and
handle restored ends. See [the complete plugin workflow](references/plugins.md).

## Build, verify, package and upgrade deliberately

```text
haylen app build /path/to/my-app --target android --config Release
haylen app verify /path/to/my-app --target android --config Release
haylen app prepare /path/to/my-app --target ios --config Release
haylen app package /path/to/my-app --target android --format bundle
haylen app zip /path/to/my-app -o /path/to/my-app.zip
```

`app build` prepares, builds and verifies without launching. `app verify` re-examines the **last
build** and exits with code 1 on a failed check. `app run` builds, verifies and launches. A build is
not runtime QA. `app prepare` generates the native project, such as the Xcode project from which
an App Store archive is made, because the Apple backend has no package format. `app package` makes
installers, Steam depots, an Android App Bundle or a device APK set. `app zip` makes a development
package with `haylen.json` at its root, not a signed or store artifact. Raise `build` in
`haylen.json` before every store upload. Keep debug services and secrets out of release.

Upgrade an app from the earlier `app.json`/`platform/` layout by following the upstream upgrading
guide once, moving each owner choice into `haylen.json`, app files or a plugin. For later engine
revisions, compare against a scratch `haylen new`/`plugin new` reference and the backend templates,
then rebuild and verify. `plugin update` pins a git plugin's current commit in `haylen.lock`. It does
not merge local changes, and `plugin add` replaces a copy. Follow
[the upgrade procedure](references/projects-and-upgrades.md).

For live Lua diagnosis, start the app with `haylen app run` in Debug and attach a DAP client to the
reported debugger port, 4711 by default. Installing or manually launching a binary has no debugger.
After release preparation, inspect the actual signed artifact and protected content separately from
`app verify`. The [debugging and release-evidence guide](references/debugging-and-release-evidence.md)
covers attachment, evaluation limits, scene inspection and content verification.

## Developer extensions and verification

Application debug-console commands use `debug.addCommand(name, fn, options)` from `haylen.debug`
with a correct owner/help/argument contract. This is different from a build-CLI extension. Do not
add wrappers, source refresh tools or a fictional universal commands directory. Separately
requested automation uses Python/uv.

Test the selected workflow through the desktop player, requested simulators/emulators and
hardware-dependent cases. Verify startup, navigation/back, forms and repeated actions, long/RTL
text, resizing/safe areas, focus/accessibility, background/resume/process death, async failure and
cleanup. For plugins, test the real native implementation, cancellation/denial and Release. For
games, also verify pause/time/input/render/save behavior. A desktop run is not native coverage.

Deliver focused source, engine revision and ownership decisions, actual command results, artifacts
and unresolved hardware/signing/account needs. Update the target project's AGENTS.md with its
present architecture, routes/scenes, state/service ownership, plugins, `platforms` customizations
and commands. Distinguish static checks, builds, runtime sessions and store evidence. Only a user
request updates this collection's stored engine knowledge.
