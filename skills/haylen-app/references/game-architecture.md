# Game architecture

Use this guide when the product actually contains interactive simulation. Read the current game
sample, scene/input/assets/lifecycle references and [source record](sources.md). Do not impose
an entity loop on an ordinary business app, or a native screen for every game entity.

## Follow the sample's boundaries, not its exact genre

Tiny Island's `main.lua` defines asset groups, loads input actions/localization/theme, applies
preferences and pushes a boot scene. Its source separates `scenes`, `systems`, `entities`, `ui`
and configuration/data. The boot scene preloads menu resources, while gameplay's `load(context)`
preloads its own group. Its gameplay scene creates a game system and HUD, forwards update/draw,
handles pause/lifecycle and opens results. These are concrete engine patterns, not a mandatory
survival-game design or an ECS requirement.

| Layer | Owns | Keep separate |
| --- | --- | --- |
| Boot/composition | Validated configuration, preload declarations, localization, action maps, preferences and first scene. | Whole-world allocation before a loading screen can display. |
| Scene | Run/menu lifecycle, transition/load orchestration, interaction between world and HUD. | Every entity's rules and every widget implementation. |
| World/domain systems | Explicit run state, progression, collisions/rules and meaningful updates. | Direct navigation, widget handles and store SDK internals. |
| Entity/model modules | Entity-specific state/behavior appropriate to the game. | One giant entity containing every possible subsystem. |
| Presentation/HUD | World rendering, camera adaptation, retained meters/menus and feedback. | Authoritative progression implemented by drawing functions. |
| Input adapter | Actions mapped from keyboard, touch, controllers and remote as supported. | Domain rules repeated for each physical device. |
| Persistence/audio/native services | Durable progress, settings and integration boundaries with clear lifetimes. | Simulated purchase/ad success or reset audio preferences on focus return. |

Start with the concrete responsibilities the game requires. Introduce a shared system/helper when
there is a real shared rule. Do not add a universal manager, inheritance hierarchy or plugin for
every small function. Keep one class/module responsibility per file, and use actual Haylen APIs.

## Create a playable vertical slice

1. Define the intended session: menu, start action, playable loop, pause, fail/win, results and
   replay/return. Specify input devices, orientation, world/design resolution and safe-area HUD.
2. Create the correct Lua/C++ project and configure actual content paths. Separate placeholder assets
   from final licensed/generated assets. Preserve image aspect ratio, texture dimensions and audio
   formats supported by the selected revision. Do not include absolute paths.
3. Declare asset groups and load them with the documented load/preload ownership. Load what the next
   scene needs, display progress and handle a rejected preload without pretending the game is ready.
   In the sample, `scene.spawn(self, ...)` owns boot work and `scene.preload(scene):await()` reports
   load failure. Preserve the actual API contract instead of inventing synchronous loading helpers.
4. Construct a fresh gameplay scene/run with explicit initial state. Keep run data distinct from
   persistent settings and profile progression. Restart must create/reset the intended run state,
   not accidentally retain the old enemies, callbacks or RNG state.
5. Map actions through the current `haylen.input` contract and content action maps. Convert input to
   domain actions once. Gate raw pointer input with `ui.usingPointer()` and raw keys with
   `ui.usingKeyboard()` so a menu click or typed space does not also trigger gameplay.
6. Choose the timing model. Use `fixedUpdate(dt)` where fixed-step simulation/physics requires it.
   It can execute zero or multiple times per rendered frame. Use `update(dt)` for suitable frame
   updates. Tiny Island's game system uses `update(dt)`, so neither fixed-step nor an ECS is mandatory
   for every title. Avoid frame-count movement/timers and verify behavior across frame rates.
7. Render without advancing authoritative state. Use the world viewport/camera deliberately, then
   draw retained UI as an overlay. Do not stretch world assets or clip essential controls at notches.
   Keep important HUD controls focusable when appropriate and decorative status out of focus paths.
8. Verify one complete run and replay before extending content. Each progression/shop/action must
   have clear availability and feedback. A disabled action needs a visible reason when the user
   might otherwise conclude the game is broken.

## Pause and lifecycle are explicit state transitions

Stack `pause`/`resume`, process/game `paused`/`unpaused`, app inactive/background, audio interruption
and an SDK screen cover are different events. Follow the selected lifecycle guide rather than
assuming that stopping rendering saves data or that every covered scene is unloaded.

Tiny Island pushes a pause scene on background and, according to lifecycle settings, focus loss.
Its gameplay `pause` hides the HUD and clears virtual input, and `resume` either resumes the run or
performs an explicitly requested exit. The engine's away-time halt alone does not guarantee that a
player returns to an intentional pause menu. Adopt the behavior appropriate to the game.

For a pause overlay, decide whether the underlying world should remain visible and frozen. Set the
documented scene transparency/process behavior and implement the right hooks. Transitions use real
time, independently of game pause. Do not let a held touch/action remain active after a pause,
orientation change, native screen or focus loss. Prevent multiple queued pause/results scenes.

Maintain audio preference separately from temporary suspension. Resume audio only if the app is
allowed to play and the user's saved choice permits it. A focus/ad/native-screen close must not
unmute the user. Save required progression through documented persistence/lifecycle APIs, without
waiting for a guaranteed exit event. Test process termination and incomplete writes where relevant.

## Resource, async and native boundaries

Scene-owned work ends on unload, not merely on covering a scene. Explicitly owned world/HUD/audio
resources must have an exact cleanup path. The game sample destroys its manually owned HUD/world
on exit. Retained GUI mounted with a scene owner is already engine-managed, so do not also destroy
it through an unrelated lifetime rule. Cleanup must handle partially initialized runs and failed
loads. Cancel timers/listeners and clear references that could target a destroyed world.

Run SDK/network work through the actual async/native contracts without blocking the frame. A late
leaderboard, cloud-save or reward result must target the correct run/account and be applied once.
Do not grant a reward on an ad request, cancellation or failed purchase. Plugin screens and stream
resources need platform cleanup on pause/dismissal. Use the plugin guide for native ownership rather
than inventing callbacks or success fallbacks.

For C++ code, use the requested standard's facilities, RAII and explicit namespace/class ownership.
Keep frame-thread work and worker results separate, retain needed objects safely and release them
after native work is actually done. Validate lengths and arithmetic at content/native boundaries.
Use meaningful sanitizer/thread diagnostics for changed native lifetime/concurrency behavior when
the toolchain supports them. A static skill document cannot certify absence of memory or data races.

## Acceptance evidence

Verify boot/load → menu → play → pause/resume → results → replay/exit, plus load failure and the
requested save/restart behavior. Test repeated transitions, multiple starts, rapid input, controller
disconnect, touch cancellation, text entry over gameplay, low/high frame rates, resizing/safe areas,
background/focus/audio interruption and native integration cancellation. Include real denial/offline
paths if used. Inspect persistent progression after process restart and another valid session.

Build/check requested Debug and Release artifacts, then run the relevant target. Headless logic tests
can validate domain rules they exercise, but cannot establish GPU output, animation quality, mobile
ergonomics, native SDK behavior or store approval. Record screenshots/logs and real hardware gaps.
