# Plugin development

A Haylen plugin you can share provides a public Lua module and optional native parts. It is
different from a C++ engine subsystem under `haylen::plugins`. Follow the current plugin guide,
`templates/plugin` and the native API pages in [sources](sources.md). Generate from the engine
revision the app uses.

## Generate, install and configure

```text
haylen plugin new /path/to/plugins/device-kit
haylen plugin add /path/to/plugins/device-kit --app /path/to/my-app
haylen plugin add /path/to/plugins/device-kit --reference --app /path/to/my-app
haylen plugin add https://github.com/OWNER/PLUGINS.git --ref EXACT_TAG_OR_COMMIT --path device-kit --reference --app /path/to/my-app
haylen plugin update device-kit --app /path/to/my-app
haylen plugin list --app /path/to/my-app
haylen project inspect /path/to/my-app --target ios-simulator
```

Choose a new or empty folder. `--id` defaults to the folder basename and must be dash-case. The
command copies `templates/plugin` and puts the ID into file, class and module names. Every native
part answers `<id>.echo` and sends `<id>.echoed`, so the plugin works on each platform from its
first build. There are no optional feature fragments. Real features come from your own native code
or from the separate plugin repositories of the haylen-org organization.

`plugin add` without `--reference` copies the plugin into `plugins/<id>/`. It replaces an earlier
copy without merging it. With `--reference` it lists the folder as `path`, or the repository as
`git`, `ref` and `path`, deletes an earlier copy and pins a repository commit in `haylen.lock`. It
lists required parameters with empty text for the developer to fill in, keeps existing values and
writes no defaults. `--ref` and `--path` are for repositories only. `plugin update <id>` pins a
referenced repository again to the commit its ref names now. `plugin remove <id> --app <app>`
deletes the entry, pin and copy, but never a referenced folder or repository. Check what depends on
the plugin before you remove it.

`plugin list` reports each plugin's version, implementations, source and every problem that keeps
it from building, such as a missing required value or a folder without `plugin.json`. A Release
build refuses a git plugin without a pin and names `haylen plugin update <id>`.

```text
device-kit/
  plugin.json
  README.md
  source/
    init.lua
  apple/
  android/
  web/
  native/
  .gitignore
  .editorconfig
  .clang-format
```

Keep only the folders of supported platforms, and declare them honestly. `require('device-kit')`
loads `source/init.lua`, and `require('device-kit.camera')` loads `source/camera.lua`. That init
file contains the public API. Keep each class and result type in its own file when you add app
code. Set the plugin `.clang-format` to `ColumnLimit: 0` under the owner's convention.

## Write the manifest as a contract

Required fields are `interface` (`1`), `id`, `name`, `version`, `description` and
`implementations`. The ID equals the app's entry key and the package folder name. The version has
one to three numeric parts. `implementations` maps each supported platform (`ios`, `catalyst`,
`tvos`, `visionos`, `macos`, `android`, `web`, `windows`, `linux`) to `native` or `lua`. A missing
platform is not supported, and an app build for it fails and names the supported platforms. Check
against the current schema `tools/haylen/schemas/plugin.schema.json`.

Optional `dependencies` maps plugin IDs to the oldest compatible version of the same major version.
The app must list each dependency. Load order follows `haylen.json`, after each plugin's listed
dependencies. Plugins that depend on each other fail the build. Optional `permissions` lists the
camelCase permission names the plugin owns, never `screens` or `localNetwork`, and never a name
another plugin of the app declares.

Parameters use camelCase keys with `type` (`string`, `number`, `integer`, `boolean`, `array`,
`object`, `file`) and `description`, plus optional `required`, `default` and `platforms`. Use one
parameter per platform when values differ. Values go under the plugin's `parameters` entry in
`haylen.json`. File parameters are relative to the **application** folder. Keep such files outside
`source/` and `content/`, for example under `config/`. Anyone can still pull a bundled file out, so
do not bundle server secrets or signing material.

`${name}` placeholders in contribution strings refer to declared parameters. A placeholder on its
own keeps its value's type, while a placeholder inside text produces text. A key or item whose
placeholder has no value is left out. Shell expansions such as `${BUILD_DIR%/Build/*}` and Xcode
`$(NAME)` build settings are not placeholders.

Every contribution has a `type`, the `platforms` it applies to and its type's fields. A contribution
names only platforms where the plugin has a native part, and every native part needs one.

| Host | Main contribution types |
| --- | --- |
| Apple | `appleClass`, `appleSources`, `swiftPackage` (exact version, shared by URL), `framework`, `binaryFramework` (`embed` true for dynamic), `infoPlist`, `entitlements`, `privacy`, `appleResource`, `buildScript`, `appExtension`, `assetPacks`. |
| Android | `gradleModule`, `mavenRepository` (https), `gradlePlugin`, `manifestPlaceholder`, `projectFile`, `assetPacks`. |
| Web | `webModule`, an ES module whose default export is `load(context)`. |
| Desktop and native libraries | `nativeLibrary` with `files` or `cmake`, `urlScheme` for Windows/Linux links, `minimumSystemVersion`. |

Contributions merge by type: `accumulate`, `unique` by identity, key-by-key `dictionary`, or
`exclusive` to one owner. Conflicting values from two owners stop resolution and name both. Run
`haylen project inspect` to see merged contributions and their owners. Never edit the generated
project to hide a missing contribution. Do not add a shell or JavaScript automation wrapper.

## Keep wire methods inside a focused Lua API

```lua
local platform = require('haylen.platform')

local handle = platform.plugin('device-kit')
local DeviceKit = {}

function DeviceKit.echo(message)
    return handle:call('echo', {message = message})
end

function DeviceKit.onEchoed(listener)
    return handle:on('echoed', listener)
end

DeviceKit.available = handle.native

return DeviceKit
```

This shows the starter echo contract, not a camera implementation. The generated init file also
loads the desktop library with `native.load('device-kit', {init = 'device_kit_haylen_init'})` when
`handle.native` is false on `macos`, `windows` or `linux`. Keep that check. `call` returns an async
platform call, `send` is one-way, and `on` returns a connection that needs an owner or cleanup. The
handle also exposes `id`, `version`, `config`, `native`, `videoStream`, `audioStream` and
`openScreen`. `platform.plugins()` shows which native parts really loaded.

Tell apart `noHandler`, `unsupported` with `data.missing`, `denied`, cancel and real SDK failure. Do
not wrap everything into one empty result that looks like success. Respect who owns the real bytes,
data views and streams. Streams are not JSON arrays of every video frame. Stop/release capture and
borrowed buffers as the native API says when the feature ends.

## Implement each native part in the right host

| Host | Real entry and integration | Lifecycle and safety |
| --- | --- | --- |
| Apple | Swift/Objective-C class conforming to `HaylenPlugin`, named by `appleClass` and `@objc(Name)` in Swift. Register handlers in `load(with:)`. | Loads during launch, before a UI presenter may exist. Use documented context/thread/lifecycle APIs, typed payloads and one result per request. |
| Android | Public no-argument class extending `dev.haylen.HaylenPlugin`, with `onLoad(context)`. The module manifest registers `dev.haylen.plugin.<id>` meta-data and depends on `dev.haylen:haylen-plugins:$haylenEngineVersion`. | Loads from a content provider before `Application.onCreate`, so no Activity exists yet. Use activity callbacks and ActivityResult registration. Do not hold on to a destroyed Activity. Follow R8 rules. |
| Web | ES module exporting `load(context)`, registering handlers/events on that context. | The loader waits for a returned promise before app startup, and a failing load stops the app. Never await an outside UI operation there. |
| Desktop | `native/` C++20 CMake library using `find_package(haylen CONFIG REQUIRED)` and `haylen::native`, with an `extern "C"` init `<id_with_underscores>_haylen_init` that forwards to a C++ class. | Check ABI/version, buffer lifetime and callback ownership. Keep the C ABI only at the boundary. |

The desktop player runs a plugin's desktop library, including on macOS. A macOS app built for the
`macos` target runs the Apple class instead. So a desktop player run does not prove the Swift
integration works. Android plugin logs use the plugin ID as the `Log` tag, so `app run` shows them.

## Declare and request permissions in the plugin

A plugin owns each protected feature it serves. List the names in `permissions`, register each one
with every native context, and call `requirePermission` before use:

| Language | Register | Ask before a use |
| --- | --- | --- |
| Swift | `context.register(HaylenPermission(name:capability:requirements:state:request:))` | `try await context.requirePermission("camera")` |
| Kotlin | `context.registerPermission(HaylenPermission("camera", "the camera", Manifest.permission.CAMERA))` | `context.requirePermission("camera", reply) { ... }` |
| JavaScript | `context.registerPermission({name, capability, needs, query, state, request})` | `await context.requirePermission("camera")` |

Apps keep calling `system.permission(name)` and `system.requestPermission(name)`. A missing usage
description or manifest entry answers `unsupported` with `data.missing`, which names the file and
snippet to add. A refusal fails with `denied`. Put Apple usage text in a plugin parameter, such as
`cameraUsage`, not in the app's `infoPlist`, which would conflict. Explain how the app stays usable.
Do not ask again and again or fake permission. Test first grant, denial, later revocation and
interruption on real supported targets. Checking the config is not checking the permission
experience.

## Show SDK screens separately from app navigation

Use `handle:openScreen(name, params, options)` and native screen registration for a real SDK's
foreground UI, such as sign-in or paywall flows. The engine covers the app first, halting and muting
it, then hands the screen to the platform. Ordinary app pages stay `ui.Screen` entries in the app's
navigation. A native overlay/banner that does not take the whole app is another supported contract.

Define success, failure, cancel, timeout, dismissal and restoration before you show the screen. One
screen at a time serves the whole process: another request fails with `busy`, a background request
fails with `notActive`, and an unregistered name fails with `noHandler`. The native side ends each
screen exactly once through the screen relay. `call:cancel()` or a timeout settles the Lua call at
once, while the cover stays until the platform reports the screen gone. Cope with late callbacks
without giving results twice. Handle the retained `<id>.screenRestored` event, which carries the
`state` the app supplied, and use `platform.screenShowing()` to understand a restart under a screen.
Apple platforms do not restore a controller after the process dies.

## Verify and distribute the plugin

Document installation, implementations, prerequisites, parameters, public methods/results,
events/connection cleanup, native screens/streams, permissions and errors in its README. Test from a
fresh app, not only inside the plugin developer's customized host. Pin the chosen upstream revision
in `haylen.lock` so builds repeat. Publishing a repository needs its own permission.

For every target you claim, build the host, run `haylen app verify` for that built configuration and
try real registration/calls. Include no native handler, missing parameter/dependency, denial,
duplicate callbacks, repeated presentation, cancel/timeout, background/rotation/activity
recreation, removal and Release as they apply. A native class being present does not prove its SDK
works, and an echo test does not cover camera, billing or ad providers.
