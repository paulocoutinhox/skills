---
name: haylen-app
description: Create and maintain Haylen C++/Lua applications, games and native plugins. Use for app screen navigation and retained UI, game architecture, project/plugin generation, haylen.json platform customization, SDK builds, verification, packaging or upgrades against Haylen's real templates.
license: MIT
---

# Haylen App

Use [Haylen](https://github.com/haylen-org/haylen) for an app, game or multimedia product built on
its C++20 engine and Lua API. The checked runtime uses Lua 5.5 through Varn and supports 2D only, so
do not offer 3D as a supported feature. The engine is built once per target into SDKs, and apps link
those SDKs. A Lua app ships its package. A C++ app compiles its own sources against the same SDK
through the same build backends.

## Choose the right product workflow

Confirm the engine revision, existing repository, product type, targets, Lua/C++ scope, navigation,
input devices, orientation, saved data, network/native services and delivery stage. Before you
build, read the current README/features, the documentation index, the APIs you need and the real
sample/template sources. Use the chosen revision's APIs, not APIs you remember from other engines.
See [sources and evidence limits](references/sources.md).

| Task | Required design and focused reading |
| --- | --- |
| Ordinary app | Frame, screens, navigation stacks/tabs, presentations, forms and domain state. Read [app architecture](references/app-architecture.md), the upstream navigation guide and the matching `samples/apps/` implementation. |
| Game | World simulation, input actions, scenes and HUD. Read [game architecture](references/game-architecture.md) and `samples/games/tiny-island`. |
| Native integration/plugin | Stable Lua API and real platform implementations. Read [plugin development](references/plugins.md), the plugin guide and `templates/plugin`. |
| Create, build, package or upgrade | Read [projects and upgrades](references/projects-and-upgrades.md), the command reference and distribution guide. |

An ordinary app mounts one frame GUI in a scene. It then shows its pages as `ui.Screen` classes
inside `ui.navigationStack`, `ui.navigationTabs` or `ui.navigationSplit`. The app samples name their
frame module `Shell` and their screen base `Page`. Those are app modules, not engine classes.
Scenes are whole flows such as sign-in, the main app or a game level. Do not build forms, lists or
navigation as a hand-drawn game world, and do not push one scene per app page.

Native SDK screens are a third case. Sign-in, paywalls or platform UI shown by a plugin use the
plugin screen contract through `handle:openScreen`. They are not navigation screens.

## Create the right project

The `haylen` launcher at the root of the engine checkout (`haylen.cmd` on Windows) runs the
`tools/haylen` package through uv, which provides its Python. Building SDKs needs CMake 3.28+, Ninja
and a C++20 compiler. Apple targets need macOS and Xcode. Android needs the Android SDK. Run
`haylen doctor` to see what this machine has and lacks for each target. It downloads nothing and
accepts no license. Other pinned tools download when a build first needs them. Name the downloads
and any required signing or hardware before you claim that a build can finish.

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

`sdk build` is the only command that compiles the engine for apps. If an app command's target has no
matching SDK, it stops and prints the `sdk build` command to run. Run it, then repeat the app
command. `new` needs a folder that does not exist or is empty. Lua is the default kind and landscape
the default orientation, so choose the app orientation explicitly. Use real identifiers from
`devices`. Do not replace an existing project with a fresh scaffold. Choose a C++ app because you
need native engine work, not because you assume a Lua app cannot show a professional interface.

## Decide who owns each source file and the structure

| Location | Responsibility |
| --- | --- |
| `haylen.json` | Strict identity, `version`, integer `build`, window/design, lifecycle, autoloads, `kind`, `cpp`, `plugins` and the `platforms` customization sections. |
| `haylen.lock` | Pinned commits for git plugin references. Keep it under version control. |
| `source/main.lua` | Lua entrypoint: theme/localization/actions and the first scene. A C++ app starts from `src/App.cpp`, which `cpp.sources` names. |
| App `source/shell.lua`, `page.lua`, `screens/` | Frame, routes, screen base and one screen class per file. These follow the app samples. They are not required engine filenames. |
| Focused `source/` modules | Domain rules, services, data models and reusable widgets. Game projects normally use `scenes/`, `systems/`, `entities/` and `ui/`. |
| `content/` | Fonts, images, audio, locale data, input/theme/preload data, maps and shaders. |
| `native/<platform>/` | App bridge handlers named by `platforms.apple.sources`, `platforms.android.sources` and `platforms.web.scripts`. |
| `plugins/<id>/` | Copied plugin manifest, Lua modules and native parts. Referenced plugins live elsewhere. |
| `config/` or similar | Files named by `file` plugin parameters or platform `files`, kept outside the package. |
| `build/apps/<app>-<hash>/` | Generated native projects, build trees, products and staged packages that you can throw away. Never edit them. |
| `platform/android/keystore/`, `dist/` | Ignored signing keys written by `app sign`, and packages written by `app package`. |

The app holds no platform project. Change a generated project only through `platforms` keys and
through files in the app repository that `files` names. `haylen project inspect` shows every final
value and where it came from. Keep one class, screen, enum or focused module per well-named file.
Prefer hyphenated filenames where they are valid. Do not add a catch-all manager, repeat service
calls across screens, add abstractions you do not need yet or add compatibility shims.

Asset paths are relative to `content/`: `assets.texture('images/hero.png')` points to
`content/images/hero.png`. Module paths are relative to `source/`:
`require('screens.order-detail')` loads `source/screens/order-detail.lua`. A plugin ID owns its
module namespace. If the first part of an app module's name equals a plugin ID, the app stops at
start.

Keep each function call on one line. Pull out named in-between values or option tables instead of
continuation lines lined up under the open parenthesis, and never split one string literal into
side-by-side literals. `haylen new` and `plugin new` write a `.clang-format` whose `ColumnLimit` is
1000000 in the checked revision. Under the owner's convention, set it to `ColumnLimit: 0` so
clang-format never wraps calls. That setting keeps existing line breaks, so join calls that are
already wrapped by hand once before formatting.

## Build ordinary applications as applications

1. Choose the closest real app sample: Online Store for catalog/forms, Music Streaming for a player
   bar that stays on screen, Photo Social for feeds/composing or Ride Hailing for map-based UI.
   Read its `main`, `shell`, `page`, `routes`, style/widgets and the screens you need. Smart Home and
   Car Dashboard are single-panel scene apps without a shell or routes. Take the structure, not the
   fake data, branding or simulated services.
2. Mount the frame once in an app scene with `{owner = self, sharedFocus = true}`. Keep bars, tabs
   and shared chrome there, with an empty node such as `middle` for the screens. Put long-lived
   domain state and network/storage boundaries in focused modules that live as long as the app or
   the account.
3. Write each page as `haylen.class('Name', ui.Screen)` with a `build` method that returns its node
   table. Push a fresh instance each time with `self.stack:push(Detail(params))`. Back uses
   `ui.goBack()`. `replace`, `popTo`, `popToRoot` and `setScreens` cover the other stack changes.
4. Use `ui.navigationTabs` when each tab keeps its own stack, scroll and fields. Selecting the tab
   that is already shown pops it to its root. Use `ui.navigationSplit` for list/detail that
   collapses on narrow widths.
5. Show new flows with `ui.present` (sheet, fullScreen, dialog, drawer, popover) and await the
   presentation `result`. Ask with `ui.presentAlert` and confirm with `ui.showMessage`.
6. Let the navigation handle the system back. A screen keeps unsaved work by returning `true` from
   `back` and asking first. An app built on the navigation never calls `window.setBackLeavesApp`.
7. Use `ui.router` for links and restoration with typed routes. Restore only state that was saved on
   purpose and that the user is still allowed to see. When an item no longer exists, fall back to a
   useful screen.
8. Follow the app samples' `design.scaling = 'none'` and `ui.scaleMode = 'physical'` when that fits.
   Use containers, safe areas, content max widths and layouts that depend on width. Patch values
   with `gui:set` and keep stable node/item IDs so typing, focus and list state survive updates.
9. Build real forms with `ui.formField` around typed `ui.textField` controls, native keyboard
   options and clear submit states. Use `ui.collection` for large lists with stable item IDs.
10. Provide theme roles, localization/RTL, accessibility labels, keyboard/remote focus and reduced
    motion. `haylen.imgui` is for developer tools, not ordinary app UI.

The [app guide](references/app-architecture.md) includes screen hooks, navigation code, form/list
steps and acceptance paths.

## Build games with a clear split between simulation and presentation

Build the game from boot/menu/gameplay/pause/results scenes. Keep a run's world/entity state
separate from HUD, rendering, input handling, saved data and audio preferences. Use preload groups
in `load`, action maps for devices and the chosen simulation's time rules. Fixed-step physics can
use `fixedUpdate(dt)`. Tiny Island updates its game system in `update(dt)`, so the engine does not
require fixed update for every game.

Render the world with the right viewport/camera APIs and the HUD with retained UI. Check
`ui.usingPointer()` and `ui.usingKeyboard()` before raw pointer/keyboard input drives gameplay.
Pause on purpose for overlays and lifecycle changes, clear virtual input when needed, and keep the
user's audio preference across interruption/resume. Do not turn every game entity into a
scene-stack entry.
See [game architecture and verification](references/game-architecture.md).

## Respect lifecycle, deferred changes and async ownership

Scenes: `load` prepares, `enter` mounts, `pause` covers, `resume` uncovers, and `exit`/`unload`
remove. Owned GUI/listeners/tasks stop on unload, not just because another scene covers the scene.
Process/game pause (`paused`/`unpaused`) is different from stack `pause`/`resume` and from app
inactive/background events. Scene changes return promises that resolve `true`, resolve `false`
when `scene.clear` drops them, or reject when loading fails. A `push` does not change `scene.size()`
right away. Use a change's `onError(message)` when you want a load-failure UI the user can recover
from.

Screens: `build` runs once, `appear`/`appeared` and `disappear`/`disappeared` follow visibility,
and `remove` ends the screen for good with everything it owns. A covered screen keeps its GUI and
state. Bind listeners with `{owner = self}` in `appear` when they should run only while visible.

Bind tasks/listeners to the right scene, screen or account owner. Check the request identity for
responses that arrive out of order. Save needed data on documented lifecycle events instead of
counting on an exit callback after the process dies. C++ uses RAII, explicit ownership and safe
dispatch.

## Create and add plugins through the engine contracts

```text
haylen plugin new /path/to/plugins/device-kit
haylen plugin add /path/to/plugins/device-kit --app /path/to/my-app
haylen plugin add /path/to/plugins/device-kit --reference --app /path/to/my-app
haylen plugin list --app /path/to/my-app
haylen project inspect /path/to/my-app --target android
```

The new folder must not exist or must be empty. Its basename is the default dash-case ID.
`plugin new` copies `templates/plugin`, whose native part on every platform answers `<id>.echo` and
sends `<id>.echoed`. There are no generated feature fragments. Camera, location, ads and similar
features are separate plugins or code the author writes with each platform's real APIs.

Write `plugin.json` with `interface`, `id`, `name`, `version`, `description` and `implementations`,
then optional `dependencies`, `permissions`, `parameters` and typed `contributions`. Expose a stable
Lua module from `source/init.lua`. Get `platform.plugin(id)` and use its `call`, `send`, `on`,
stream and `openScreen` contracts. Handle the explicit `noHandler`, `unsupported`, `denied` and
cancellation results. Never fake success for a missing native implementation.

Implement the Apple class that conforms to `HaylenPlugin`, the Android class that extends
`dev.haylen.HaylenPlugin`, the web module's `load(context)` and the desktop C++ library from the
template. Register the plugin's permissions with the native context and call `requirePermission`
before use. A native SDK screen must finish once, keep the app covered until its UI really closes
and handle ends that arrive after a restore. See [the complete plugin workflow](references/plugins.md).

## Build, verify, package and upgrade with care

```text
haylen app build /path/to/my-app --target android --config Release
haylen app verify /path/to/my-app --target android --config Release
haylen app prepare /path/to/my-app --target ios --config Release
haylen app package /path/to/my-app --target android --format bundle
haylen app zip /path/to/my-app -o /path/to/my-app.zip
```

`app build` prepares, builds and verifies without launching. `app verify` checks the **last build**
again and exits with code 1 when a check fails. `app run` builds, verifies and launches. A build is
not runtime QA. `app prepare` generates the native project, such as the Xcode project you make an
App Store archive from, because the Apple backend has no package format. `app package` makes
installers, Steam depots, an Android App Bundle or a device APK set. `app zip` makes a development
package with `haylen.json` at its root. It is not a signed or store package. Raise `build` in
`haylen.json` before every store upload. Keep debug services and secrets out of release.

To upgrade to a later engine revision, compare against a scratch `haylen new`/`plugin new`
reference and the backend templates, then rebuild and verify. `plugin update` pins a git plugin's
current commit in `haylen.lock`. It does not merge local changes, and `plugin add` replaces a copy.
Follow [the upgrade procedure](references/projects-and-upgrades.md).

For live Lua debugging, start the app with `haylen app run` in Debug and attach a DAP client to the
reported debugger port, 4711 by default. Installing or launching a binary by hand gives no debugger.
After release preparation, check the real signed package and protected content separately from
`app verify`. The [debugging and release-evidence guide](references/debugging-and-release-evidence.md)
covers attaching, evaluation limits, scene inspection and content checks.

## Developer extensions and verification

App debug-console commands use `debug.addCommand(name, fn, options)` from `haylen.debug` with a
correct owner/help/argument contract. This is different from a build-CLI extension. Do not add
wrappers, source refresh tools or a made-up universal commands directory. Automation that the user
asks for separately uses Python/uv.

Test the chosen workflow on the desktop player, the requested simulators/emulators and the cases
that depend on hardware. Check startup, navigation/back, forms and repeated actions, long/RTL text,
resizing/safe areas, focus/accessibility, background/resume/process death, async failure and
cleanup. For plugins, test the real native implementation, cancel/deny and Release. For games, also
check pause/time/input/render/save behavior. A desktop run is not native coverage.

Deliver the focused source, engine revision and ownership decisions, real command results, packages
and any open hardware/signing/account needs. Update the target project's AGENTS.md with its current
structure, routes/scenes, who owns which state and service, plugins, `platforms` customizations and
commands. Keep static checks, builds, runtime sessions and store evidence separate. Only a user
request updates this collection's stored engine knowledge.
