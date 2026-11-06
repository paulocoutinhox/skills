# Plugin development

A distributable Haylen plugin provides a public Lua module and optional native parts. It is
different from a C++ engine subsystem. Follow the current plugin guide, template/features and
native API pages in [sources](sources.md). Generate from the engine revision used by the app.

## Generate, install and configure

```text
haylen plugin new /path/to/plugins/device-kit --id device-kit --with camera,microphone
haylen plugin add /path/to/plugins/device-kit --app /path/to/my-app
haylen plugin list --app /path/to/my-app
haylen plugin add https://github.com/OWNER/PLUGIN.git --ref EXACT_COMMIT --app /path/to/my-app
```

Choose a new/empty folder whose basename equals the dash-case plugin ID. `--id` defaults to that
basename, and a mismatch fails. `--with` accepts comma-separated/repeated feature choices. Omit it
for a minimal custom integration. The CLI layers selected `templates/plugin-features` into
`templates/plugin`, substitutes IDs/class/module names and writes the starter implementations.

`plugin add` copies the folder/repository into `plugins/<id>`, records its parameters/defaults in
`app.json` and reports required plugins. It does not install the dependency graph automatically.
`--ref` applies to repositories only. Inspect the destination first because adding replaces an
existing plugin copy. Preserve app-specific modifications intentionally. Existing app parameter
choices survive installation, but newly required empty values must be completed deliberately.
`plugin remove <id> --app <app>` deletes the installed copy and app declaration. Use it only for
an intended removal after checking dependents and local modifications.

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
```

Generate native implementation only for supported targets, and declare them honestly. Lua loads
`require('device-kit')` from `source/init.lua` and plugin submodules through its ID namespace.
This Lua init file contains the public API. Keep individual classes and result types in separate
files when adding application code, even if a starter template nests a demonstration type.

## Choose features or a real SDK implementation

| Current feature | Generated responsibility | Important boundary |
| --- | --- | --- |
| `camera` | Camera start/stop, photo capture and video stream integration. | Platform permission, actual capture availability and cleanup still apply. |
| `microphone` | Start/stop and microphone audio stream. | Handle interruption and denied permission. Do not leave recording active after the owning feature ends. |
| `location` | One-shot location and watching/events. | Accuracy, denied/revoked permission and subscription cleanup are real product decisions. |
| `banner` | Show/hide and tapped events for a native banner UI. | This is not an integrated advertising provider, consent flow or monetization SDK. |

Inspect each feature's current platform files. A declared desktop implementation can explicitly
return unsupported rather than implement capture/location. This is a limitation of that generated
implementation, not proof that desktop hardware cannot support the capability. The researched
Apple TV feature paths do not provide camera/microphone capture or continuous location watching.
Do not extrapolate iPhone functionality to tvOS, Catalyst, visionOS or the desktop player.

For a real SDK, establish supported versions/platforms, initialization, credentials, entitlement,
privacy, threading, callback and shutdown requirements first. Replace the demonstration echo/banner
behavior with that SDK's actual flow. Document missing platforms and reject unsupported operations
with a useful reason. Do not return fake purchases, ad completions or account credentials.

## Author the manifest as a contract

Required fields are `id`, `name`, `version`, `description` and `platforms`. The ID matches its folder.
The researched version accepts one to three numeric components. Platforms are unique entries from
`ios`, `catalyst`, `tvos`, `visionos`, `macos`, `android`, `web`, `windows` and `linux`.
Use only fields supported by the selected strict schema.

Optional `requires` lists other plugin IDs. Resolve all dependencies and cycles before building.
Initialization respects dependencies, then declared app order where applicable. Do not assume a
random directory enumeration order initializes an SDK dependency before its consumer.

Parameter declarations use camelCase keys and a `type` plus `description`. Types include string,
number, integer, boolean, array, object and file, with optional `required`, `default` and `platforms`.
Values belong under the plugin's entry in app.json, as in the generated README. File parameters
are relative to the **application** folder. Keep native configuration files outside source/content
when they should not become ordinary Lua package assets. A bundled app file is still extractable,
so do not bundle server secrets or signing material.

`${parameterName}` substitutions refer to declared parameters. A standalone placeholder retains
its value's type, while interpolation inside text produces text. An unset optional parameter can
remove its containing key/item. Platform filters matter. Do not confuse these substitutions with
native Xcode `$(NAME)` build settings or invent environment-variable expansion rules.

| Section | What to declare and verify |
| --- | --- |
| `apple` | Runtime `class`, `sources`, system `frameworks`, Swift `packages`, `binaryFrameworks`, resources, Info.plist, entitlements, privacy declarations and supported extensions/asset packs. Match exact schema and target scope. |
| `android` | Gradle library `module`, HTTPS repositories, Gradle plugins/versions, manifest placeholders and declared copied files. Use actual dependency/manifest registration in the module. |
| `web` | Native ES module path and supported web implementation. Do not omit its prepared-site registration. |
| `native` | Desktop library's CMake source/target and exported entrypoint as the current template declares. Preserve the native ABI/version contract. |

Apple package products/versions and binary names must agree across plugins. Do not embed a static
framework as if it were dynamic or duplicate linked SDKs. Place usage descriptions, required-reason
APIs/tracking declarations and capabilities in their actual source manifest/configuration. Privacy
declarations must match implementation. Never edit generated `haylen/` to hide a missing manifest.
If a plugin needs a build phase, use its documented field. Do not introduce a shell/JavaScript
automation wrapper. Separately requested automation in this collection uses Python/uv.

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

return DeviceKit
```

This demonstrates the actual starter echo contract, not a camera implementation. Place it in
`source/init.lua`. Extend it with real methods and explicit payload/result contracts. `call`
returns an asynchronous platform call, `send` is for its documented one-way semantics and `on`
returns a connection requiring appropriate owner/cleanup. `handle` also exposes id/version/config,
native availability, video/audio streams and `openScreen`. `platform.plugins()` is useful for
diagnosing which native implementations actually loaded.

Distinguish no registered handler, unsupported capability, denied permission, cancellation and real
SDK failure. Do not wrap everything into one success-shaped empty result. Respect actual bytes,
data-view and stream ownership. Streams are not JSON arrays of every video frame. Stop/release
capture and borrowed buffers according to the native API when the feature ends or becomes invalid.

## Implement each native part in the right host

| Host | Actual entry and integration | Lifecycle and safety |
| --- | --- | --- |
| Apple | Swift/Objective-C class conforming to `HaylenPlugin`. Match Swift `@objc(Name)` with `apple.class` and register handlers in `load(with:)`. Template bridging headers expose the context APIs. | Initialization occurs during app launch. A UI presenter may not yet exist. Use documented context/thread/lifecycle APIs, typed payloads and one result per request. Release native observations/resources at their actual end. |
| Android | Public no-argument class extending `dev.haylen.HaylenPlugin`, with `onLoad(context)`. The library manifest registers `dev.haylen.plugin.<id>`. The provider and generated config determine native loading. | Initialization precedes activity availability. Use activity callbacks and documented ActivityResult/lifecycle registration. Avoid retaining a destroyed Activity. Follow frame/UI/background dispatch and R8 rules. |
| Web | ES module exporting `load(context)`, registering handlers/events on that context. | The loader waits for returned initialization promises before app startup. Do not await a never-resolving external UI operation during module initialization. Honor browser gestures, visibility, permission, popup and cleanup requirements. |
| Desktop | `native/` C/C++ library loaded through `native.load(id, {init = '<id_with_underscores>_haylen_init'})` where needed. | The exported C ABI registers handlers/plugin identity. Handlers run on the frame thread, replies can arrive from other threads through the actual API. Validate ABI/version, buffer lifetime and callback ownership. |

The desktop player uses a plugin's desktop native part, including on macOS. A macOS app built from
the Apple template uses its Apple plugin class. A successful desktop player run therefore does not
prove Swift integration. Follow generated Lua loading conditions instead of loading desktop native
code a second time over an already registered native part. An ABI-required C entry symbol is a
boundary exception to normal C++ class/namespace organization. Keep implementation in focused C++
classes with RAII and explicit ownership, without an unnecessary C-style application architecture.

Android's Gradle module uses the engine plugin library at the current engine version. Inspect the
starter for exact coordinates/tool versions instead of mixing old artifacts. Required permissions,
components and copied files must survive the actual merged manifest. An app's intentional
`tools:node="remove"` restriction is not permission to force the removed capability back in.

## Request permission through engine services

Use the current `haylen.system` permission API and native context `requirePermission` flow for the
feature. Supply truthful usage descriptions/declarations before requesting. Apple Swift supports
`try await context.requirePermission("camera")`, while web uses
`await context.requirePermission("camera")`. Use Android's documented callback form and thread.

Missing declarations can return unsupported with missing-requirement data. User refusal is denied.
Explain how the app remains usable and what feature is unavailable. Do not repeatedly prompt, bypass
the platform or quietly simulate permission. Test first grant, denial, later revocation and lifecycle
interruption on real supported targets. Config validation is not permission UX verification.

## Present SDK screens separately from Lua pages

Use `handle:openScreen(name, params, options)` and native screen registration for a real SDK's
foreground UI, such as authentication/paywall flows. The engine covers the app before native UI
presentation, suspending gameplay/audio through its lifecycle. Ordinary app pages remain scene-stack
screens. A native overlay/banner that does not take the whole app is another supported contract.

Define success, failure and cancellation, timeout, dismiss and restoration before presentation.
There is one process-wide foreground screen flow. Conflicting requests can report busy, and an
inactive app cannot always start a new screen. Use documented ScreenRequest/ScreenRelay protocols
and finish once. Do not start arbitrary native controllers with no relationship to that request.

Cancel/timeout can settle the Lua call before native UI has actually disappeared. Keep the cover
until real dismissal, release native state and tolerate late callbacks without granting results
twice. Where supported, handle retained `<id>.screenRestored` events with state/result or error,
and use `platform.screenShowing()` to interpret restart coverage. Do not promise restoration of
an Apple controller after process death or across unsupported SDK/platform boundaries.

## Verify and distribute the plugin

Document installation, declared platforms, prerequisites, configuration, public methods/results,
events/connection cleanup, native screens/streams and errors in its README. Test from a fresh app,
not only within the plugin developer's customized host. Pin the chosen upstream revision when
installing for reproducibility. Publishing a repository/package is a separately authorized action.

For every claimed target, build the host, run `haylen check` for that built configuration and
exercise actual registration/calls. Include no native handler, missing parameter/dependency,
denial, duplicate callbacks, repeated presentation, cancellation/timeout, background/rotation/activity
recreation, unload and Release retention as applicable. Ensure unavailable methods report explicit
outcomes and no resource/callback survives its owner accidentally. A native class's presence alone
does not prove its SDK works, and a mock/echo test is not camera, billing or ad-provider coverage.
