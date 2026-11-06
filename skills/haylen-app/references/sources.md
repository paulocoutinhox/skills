# Haylen sources

Verified on 2026-11-05 against selected official documentation, source, samples and templates on
upstream main. This is a branch snapshot, not an immutable engine release guarantee. Record the
actual application/engine commit when implementing a task. Recheck changed APIs/templates against
that revision. Reading operational documentation does not authorize changing this collection.

- [README](https://github.com/haylen-org/haylen/blob/main/README.md): purpose, C++20/Lua architecture,
  current 2D scope, platform inventory, features, and starter commands.
- [Documentation index](https://github.com/haylen-org/haylen/blob/main/docs/README.md): routing to
  selected engine areas and the complete Lua API reference.
- [Lua guide](https://github.com/haylen-org/haylen/blob/main/docs/core/lua.md): app package, Lua 5.5,
  module/asset paths, scene ownership, strict app.json, and safe loading boundaries.
- [Lifecycle](https://github.com/haylen-org/haylen/blob/main/docs/core/lifecycle.md): start order,
  pause/background semantics, audio interruption, persistence, and owned work.
- [Build](https://github.com/haylen-org/haylen/blob/main/docs/tools/build.md): Python/CMake requirements,
  real command families, platform prerequisites, tool pins, logs, and generated output.
- [Distribution](https://github.com/haylen-org/haylen/blob/main/docs/tools/distribution.md): package,
  developer-owned native projects, devices, app run/build flags, and deployment distinctions.
- [Debug API](https://github.com/haylen-org/haylen/blob/main/docs/lua-api/debug.md): addCommand,
  argument contracts, owner cleanup, and developer-console versus build-CLI separation.
- [Scene API](https://github.com/haylen-org/haylen/blob/main/docs/lua-api/scene.md): actual hooks,
  deferred/queued operations, navigation promises, preload, transitions and scene ownership.
- [Retained UI guide](https://github.com/haylen-org/haylen/blob/main/docs/ui/ui.md): node trees,
  mount/owner behavior, patching, safe areas/units, responsive scaling, collections, focus,
  text entry and accessibility. This is the normal application UI, distinct from developer ImGui.
- [Text input](https://github.com/haylen-org/haylen/blob/main/docs/ui/text-input.md): hidden native
  fields, IME/composition, revision/state ownership, return/cancel, keyboards and avoidance.
- [Online Store sample](https://github.com/haylen-org/haylen/tree/main/samples/apps/online-store):
  manifest/main, Page, Shell, checkout and browse source establish app layout, root replacement,
  detail pushes, forms and collection patterns. Demonstration orders are not real payments.
- [Music Streaming sample](https://github.com/haylen-org/haylen/tree/main/samples/apps/music-streaming):
  Page and source organization corroborate app-owned player chrome and page layout responsibilities.
- [App sample index](https://github.com/haylen-org/haylen/tree/main/samples/apps): Photo Social and
  Ride Hailing are additional task-specific references. Their directory/module inventory was
  inspected, not every screen or provider implementation. Read relevant source before using it.
- [Tiny Island sample](https://github.com/haylen-org/haylen/tree/main/samples/games/tiny-island):
  main, boot and gameplay establish preload, scene/world/HUD separation, update timing and pause.
- [Plugin guide](https://github.com/haylen-org/haylen/blob/main/docs/platform/plugins.md): selected
  generation/manifest, Lua/native integration, permission, stream and native-screen sections explain
  supported contracts. Consult the full applicable API details for a concrete native implementation.
- [Plugin template](https://github.com/haylen-org/haylen/tree/main/templates/plugin): manifest,
  README, Lua entry and Apple/web starter contracts. Platform folders are implementation source,
  not a guarantee of every feature on every listed target.
- [Feature templates](https://github.com/haylen-org/haylen/tree/main/templates/plugin-features):
  generated optional feature composition. The plugin guide documents their capabilities/limitations.
  Inspect selected native feature files before changing a real implementation.
- [Layered templates](https://github.com/haylen-org/haylen/tree/main/templates): common, Lua and
  C++ ownership and target distinctions. Read the matching target's current source when merging.
- [Upgrading guide](https://github.com/haylen-org/haylen/blob/main/docs/tools/upgrading.md):
  scratch references, platform diffs, per-platform source merges and plugin integration upgrades.
- [CLI implementation](https://github.com/haylen-org/haylen/blob/main/haylen.py): selected generator
  and manifest validation sections corroborate plugin ID/folder equality and real command behavior.
  Use an ID-matching scratch plugin folder, even where an illustrative path in a guide differs.

## Interpretation and limits

Engine requirements, source behavior and sample design choices are separate. Shell/Page filenames,
tab replacement, exact transition timings, breakpoints, sample content and physical scale choices
are not universal engine mandates. The collection recommends the sample's app architecture for
ordinary apps, with explicit product decisions for route restoration, service state and errors.
Request identity, idempotent side effects and ownership checks are engineering recommendations
applied to these contracts, not claims that sample fake data implements production services.

The source set is authoritative for this engine's behavior. It does not establish certification for
an external SDK, store, payment provider or every hardware feature. Large manuals were consulted
by relevant sections. No claim is made that every upstream file, sample screen or provider SDK was
read in full. No inaccessible book or secondary article is represented as consulted evidence.

Native app implementation uses C++/Lua and supported plugin languages. Separately requested
automation remains Python/uv. No new automation is bundled. Authoring did not execute a generator,
engine/mobile build, GPU run, permission/native-SDK session or store operation. Repository validation
and manual source/scenario review are separate evidence, not native runtime certification.

## Debugger and final-content checks

Checked **2026-11-05** against local maintainer source revision
`2efc895f5e9547191cf5f62ed7ed20fc081bc3c2` and the corresponding official guides:

- [Debugger](https://github.com/haylen-org/haylen/blob/2efc895f5e9547191cf5f62ed7ed20fc081bc3c2/docs/tools/debugger.md): Debug development launch, relay, evaluation limits and disconnect/lifetime reasoning.
- [Scene API](https://github.com/haylen-org/haylen/blob/2efc895f5e9547191cf5f62ed7ed20fc081bc3c2/docs/lua-api/scene.md): bottom-to-top indexing, current top scene, covered update and ownership cancellation.
- [Content guide](https://github.com/haylen-org/haylen/blob/2efc895f5e9547191cf5f62ed7ed20fc081bc3c2/docs/content/content.md) and native `content verify --help`: the positional source app differs from the extracted release directory selected by `--release`.
- [DAP overview](https://microsoft.github.io/debug-adapter-protocol/overview): initialization/configuration sequencing and asynchronous protocol events. Haylen's inspected implementation decides supported requests.

This revision read source/help and reviewed the previously exercised integration. It did not rerun
native builds or certify new transactions, hardware behavior or performance.
