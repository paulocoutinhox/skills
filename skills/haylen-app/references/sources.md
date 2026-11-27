# Haylen sources

Checked on 2026-11-18 against the official documentation, source, samples and templates at
upstream main commit `c8061996311d301dd5dc9b90e93a1113bf04f247`. This is a snapshot of a branch,
not a fixed engine release you can rely on. Record the real app/engine commit when you work on a
task. Check changed APIs/templates again against that revision. Reading working documentation does
not give permission to change this collection. Checked again on 2026-11-18 against main commit
`eb6cc791f5b2c2832eb5fa55a1982307060a745e`.

- [README](https://github.com/haylen-org/haylen/blob/main/README.md): purpose, C++20/Lua through Varn,
  2D scope, platform list, uv-only launcher, SDK-first quick start and features.
- [Documentation index](https://github.com/haylen-org/haylen/blob/main/docs/README.md): links to
  engine areas and the complete Lua API reference.
- [Lua guide](https://github.com/haylen-org/haylen/blob/main/docs/core/lua.md): Lua 5.5, package,
  module/asset paths, scene ownership and safe loading boundaries.
- [Lifecycle](https://github.com/haylen-org/haylen/blob/main/docs/core/lifecycle.md): start order,
  what pause/background mean, audio interruption, saved data and owned work.
- [Commands](https://github.com/haylen-org/haylen/blob/main/docs/tools/commands.md): the command tree,
  `new`, `doctor`, `devices`, `sdk build|join|list`, `app prepare|build|verify|run|package|sign|zip`,
  `plugin add|update|remove|list|new`, `project inspect` and `content verify` options and defaults.
- [Build](https://github.com/haylen-org/haylen/blob/main/docs/tools/build.md): uv, CMake 3.28+, Ninja
  and C++20 requirements, `doctor`, SDK manifests, logs and generated output.
- [Distribution](https://github.com/haylen-org/haylen/blob/main/docs/tools/distribution.md): targets,
  pipeline, generated projects under `build/apps/` that you can throw away, `platforms` sections and
  merge rules, running and its keys, version/build numbers, release builds, packages and the Apple
  archive route.
- [Navigation guide](https://github.com/haylen-org/haylen/blob/main/docs/ui/navigation.md) and
  [UI reference](https://github.com/haylen-org/haylen/blob/main/docs/lua-api/ui.md#navigation):
  `ui.Screen` hooks, stacks, tabs, splits, presentations, alerts, messages, system back from the top
  presentation layer down to the app layer, routes and restoration, and the line between scenes and
  navigation.
- [Retained UI guide](https://github.com/haylen-org/haylen/blob/main/docs/ui/ui.md): node trees,
  mount/owner behavior, patching, safe areas/units, scaling, collections, focus and accessibility.
  This is the normal app UI, separate from developer ImGui.
- [Text input](https://github.com/haylen-org/haylen/blob/main/docs/ui/text-input.md): hidden native
  fields, IME/composition, who owns revision/state, return/cancel, keyboards and avoidance.
- [Scene API](https://github.com/haylen-org/haylen/blob/main/docs/lua-api/scene.md): hooks, change
  promises and options, preload, transitions, `top`/`at`/`list` indexing and scene ownership.
- [Debug API](https://github.com/haylen-org/haylen/blob/main/docs/lua-api/debug.md): `addCommand`,
  argument contracts, owner cleanup and how the developer console differs from the build CLI.
- [Online Store sample](https://github.com/haylen-org/haylen/tree/main/samples/apps/online-store):
  manifest, main, Shell, Page, routes, checkout and browse show the frame/tabs/router app layout,
  forms and collection patterns. Demo orders are not real payments.
- [App sample index](https://github.com/haylen-org/haylen/tree/main/samples/apps): Music Streaming,
  Photo Social and Ride Hailing share the shell/page/routes structure. Smart Home and Car Dashboard
  are single-panel scene apps. Their file lists were read, not every screen implementation.
- [Tiny Island sample](https://github.com/haylen-org/haylen/tree/main/samples/games/tiny-island):
  main, boot and gameplay show preload, the split between scene/world/HUD, update timing and pause.
- [Plugin guide](https://github.com/haylen-org/haylen/blob/main/docs/platform/plugins.md): generation,
  manifest, parameters, placeholders, contributions, validation, references/lock, Lua handle, native
  classes, permissions and screens. Read the full API pages for a concrete native implementation.
- [Plugin template](https://github.com/haylen-org/haylen/tree/main/templates/plugin) and
  [app templates](https://github.com/haylen-org/haylen/tree/main/templates): starter parts, bridge
  handlers under `native/`, and the `.clang-format` files whose `ColumnLimit` is 1000000.
- [Debugger](https://github.com/haylen-org/haylen/blob/main/docs/tools/debugger.md): `app run` Debug
  sessions, port 4711 default, `--debugger-port`, attach configuration and the one-second evaluation
  limit.
- [Content guide](https://github.com/haylen-org/haylen/blob/main/docs/content/content.md): protected
  releases and `content verify <app> --target <target> [--release <folder>]`.
- [DAP overview](https://microsoft.github.io/debug-adapter-protocol/overview): initialization and
  protocol events that arrive on their own. Haylen's implementation decides which requests it
  supports.

## Interpretation and limits

Engine requirements, source behavior and sample design choices are separate things.
Shell/Page/routes filenames, transition timings, breakpoints, sample content and physical scale
choices are not engine rules for every app. Setting an app or plugin `.clang-format` to
`ColumnLimit: 0` is the owner's convention, not the upstream template value. The collection
recommends the samples' app structure for ordinary apps, with explicit product decisions for routes,
service state and errors. Request identity, side effects that are safe to repeat and ownership
checks are engineering advice applied to these contracts. They do not claim that the samples' fake
data implements production services.

These sources are the source of truth for this engine's behavior. They do not certify an outside
SDK, store, payment provider or every hardware feature. Large manuals were read by the relevant
sections. No claim is made that every upstream file, sample screen or provider SDK was read in full.
No book or secondary article that could not be reached is presented as read evidence.

Native app code uses C++/Lua and the supported plugin languages. Automation the user asks for
separately stays Python/uv. No new automation is bundled. Writing this guide did not run a
generator, SDK/app build, GPU run, permission/native-SDK session or store operation. Repository
validation and manual source/scenario review are separate evidence. They do not certify native
runtime behavior.
