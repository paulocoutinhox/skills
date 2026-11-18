# Haylen sources

Verified on 2026-11-18 against official documentation, source, samples and templates at upstream
main commit `c8061996311d301dd5dc9b90e93a1113bf04f247`. That revision replaced `haylen.py`, `app.json`,
developer-owned `platform/` projects and the old plugin manifest with the `tools/haylen` package,
`haylen.json`, generated projects and typed contributions. This is a branch snapshot, not an
immutable engine release guarantee. Record the actual application/engine commit when implementing a
task. Recheck changed APIs/templates against that revision. Reading operational documentation does
not authorize changing this collection. Rechecked on 2026-11-18 against main commit
`eb6cc791f5b2c2832eb5fa55a1982307060a745e`, whose only change after that revision updates SDL and its
UIKit patches, which this skill does not describe. The system back order of the
[navigation guide](https://github.com/haylen-org/haylen/blob/main/docs/ui/navigation.md#the-system-back)
goes through presentation layers from the top before the app layer.

- [README](https://github.com/haylen-org/haylen/blob/main/README.md): purpose, C++20/Lua through Varn,
  2D scope, platform inventory, uv-only launcher, SDK-first quick start and features.
- [Documentation index](https://github.com/haylen-org/haylen/blob/main/docs/README.md): routing to
  engine areas and the complete Lua API reference.
- [Lua guide](https://github.com/haylen-org/haylen/blob/main/docs/core/lua.md): Lua 5.5, package,
  module/asset paths, scene ownership and safe loading boundaries.
- [Lifecycle](https://github.com/haylen-org/haylen/blob/main/docs/core/lifecycle.md): start order,
  pause/background semantics, audio interruption, persistence and owned work.
- [Commands](https://github.com/haylen-org/haylen/blob/main/docs/tools/commands.md): the command tree,
  `new`, `doctor`, `devices`, `sdk build|join|list`, `app prepare|build|verify|run|package|sign|zip`,
  `plugin add|update|remove|list|new`, `project inspect` and `content verify` options and defaults.
- [Build](https://github.com/haylen-org/haylen/blob/main/docs/tools/build.md): uv, CMake 3.28+, Ninja
  and C++20 requirements, `doctor`, SDK manifests, logs and generated output.
- [Distribution](https://github.com/haylen-org/haylen/blob/main/docs/tools/distribution.md): targets,
  pipeline, generated disposable projects under `build/apps/`, `platforms` sections and merge rules,
  running and its keys, version/build numbers, release builds, packages and the Apple archive route.
- [Upgrading guide](https://github.com/haylen-org/haylen/blob/main/docs/tools/upgrading.md): moving an
  earlier-layout app and plugins to `haylen.json`, `platforms`, contributions and the new commands.
- [Navigation guide](https://github.com/haylen-org/haylen/blob/main/docs/ui/navigation.md) and
  [UI reference](https://github.com/haylen-org/haylen/blob/main/docs/lua-api/ui.md#navigation):
  `ui.Screen` hooks, stacks, tabs, splits, presentations, alerts, messages, system back, routes and
  restoration, and the scene/navigation boundary.
- [Retained UI guide](https://github.com/haylen-org/haylen/blob/main/docs/ui/ui.md): node trees,
  mount/owner behavior, patching, safe areas/units, scaling, collections, focus and accessibility.
  This is the normal application UI, distinct from developer ImGui.
- [Text input](https://github.com/haylen-org/haylen/blob/main/docs/ui/text-input.md): hidden native
  fields, IME/composition, revision/state ownership, return/cancel, keyboards and avoidance.
- [Scene API](https://github.com/haylen-org/haylen/blob/main/docs/lua-api/scene.md): hooks, change
  promises and options, preload, transitions, `top`/`at`/`list` indexing and scene ownership.
- [Debug API](https://github.com/haylen-org/haylen/blob/main/docs/lua-api/debug.md): `addCommand`,
  argument contracts, owner cleanup and developer-console versus build-CLI separation.
- [Online Store sample](https://github.com/haylen-org/haylen/tree/main/samples/apps/online-store):
  manifest, main, Shell, Page, routes, checkout and browse establish the frame/tabs/router app
  layout, forms and collection patterns. Demonstration orders are not real payments.
- [App sample index](https://github.com/haylen-org/haylen/tree/main/samples/apps): Music Streaming,
  Photo Social and Ride Hailing share the shell/page/routes structure. Smart Home and Car Dashboard
  are single-panel scene apps. Their inventories were inspected, not every screen implementation.
- [Tiny Island sample](https://github.com/haylen-org/haylen/tree/main/samples/games/tiny-island):
  main, boot and gameplay establish preload, scene/world/HUD separation, update timing and pause.
- [Plugin guide](https://github.com/haylen-org/haylen/blob/main/docs/platform/plugins.md): generation,
  manifest, parameters, placeholders, contributions, validation, references/lock, Lua handle, native
  classes, permissions and screens. Consult the full API pages for a concrete native implementation.
- [Plugin template](https://github.com/haylen-org/haylen/tree/main/templates/plugin) and
  [app templates](https://github.com/haylen-org/haylen/tree/main/templates): starter parts, bridge
  handlers under `native/`, and the `.clang-format` files whose `ColumnLimit` is 1000000.
- [Debugger](https://github.com/haylen-org/haylen/blob/main/docs/tools/debugger.md): `app run` Debug
  sessions, port 4711 default, `--debugger-port`, attach configuration and the one-second evaluation limit.
- [Content guide](https://github.com/haylen-org/haylen/blob/main/docs/content/content.md): protected
  releases and `content verify <app> --target <target> [--release <folder>]`.
- [DAP overview](https://microsoft.github.io/debug-adapter-protocol/overview): initialization and
  asynchronous protocol events. Haylen's implementation decides supported requests.

## Interpretation and limits

Engine requirements, source behavior and sample design choices are separate. Shell/Page/routes
filenames, transition timings, breakpoints, sample content and physical scale choices are not
universal engine mandates. Setting an app or plugin `.clang-format` to `ColumnLimit: 0` is the owner's
convention, not the upstream template value. The collection recommends the samples' app architecture
for ordinary apps, with explicit product decisions for routes, service state and errors. Request
identity, idempotent side effects and ownership checks are engineering recommendations applied to
these contracts, not claims that sample fake data implements production services.

The source set is authoritative for this engine's behavior. It does not establish certification for
an external SDK, store, payment provider or every hardware feature. Large manuals were consulted
by relevant sections. No claim is made that every upstream file, sample screen or provider SDK was
read in full. No inaccessible book or secondary article is represented as consulted evidence.

Native app implementation uses C++/Lua and supported plugin languages. Separately requested
automation remains Python/uv. No new automation is bundled. Authoring did not execute a generator,
SDK/app build, GPU run, permission/native-SDK session or store operation. Repository validation and
manual source/scenario review are separate evidence, not native runtime certification.
