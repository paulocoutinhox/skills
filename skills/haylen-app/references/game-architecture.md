# Game architecture

Use this guide when the product really contains an interactive simulation. Read the current game
sample, the scene/input/assets/lifecycle references and the [source record](sources.md). Do not
force an entity loop onto an ordinary business app, or a native screen onto every game entity.

## Follow the sample's boundaries, not its exact genre

Tiny Island's `main.lua` defines asset groups, loads input actions and the theme, applies
preferences and pushes a boot scene. Its source splits `scenes`, `systems`, `entities`, `ui`
and configuration/data. The boot scene preloads menu resources, while gameplay's `load(context)`
preloads its own group. Its gameplay scene creates a game system and HUD, passes on update/draw,
handles pause/lifecycle and opens results. These are concrete engine patterns. They are not a
required survival-game design or an ECS requirement.

| Layer | Owns | Keep separate |
| --- | --- | --- |
| Boot/composition | Validated configuration, preload declarations, localization, action maps, preferences and first scene. | Creating the whole world before a loading screen can show. |
| Scene | Run/menu lifecycle, running transitions/loads, and how the world and HUD work together. | Every entity's rules and every widget implementation. |
| World/domain systems | Explicit run state, progression, collisions/rules and meaningful updates. | Direct navigation, widget handles and store SDK internals. |
| Entity/model modules | Entity-specific state/behavior that fits the game. | One giant entity holding every possible subsystem. |
| Presentation/HUD | World rendering, camera changes, retained meters/menus and feedback. | Progression rules that decide the real result built into drawing functions. |
| Input adapter | Actions mapped from keyboard, touch, controllers and remote as supported. | Domain rules repeated for each physical device. |
| Persistence/audio/native services | Long-lived progress, settings and integration boundaries with clear lifetimes. | Faked purchase/ad success, or audio preferences reset when focus returns. |

Start with the concrete jobs the game needs. Add a shared system/helper when there is a real shared
rule. Do not add a catch-all manager, inheritance tree or plugin for every small function. Keep one
class/module job per file, and use real Haylen APIs.

## Build a small playable slice first

1. Define the session you want: menu, start action, play loop, pause, lose/win, results and
   replay/return. Say which input devices, orientation, world/design resolution and safe-area HUD
   you use.
2. Create the right Lua/C++ project with `haylen new` and set the real content paths. Keep
   placeholder assets apart from final licensed/generated assets. Keep image aspect ratio, texture
   dimensions and audio formats that the chosen revision supports. Do not include absolute paths.
3. Declare asset groups and load them with the documented load/preload ownership. Load what the next
   scene needs, show progress and handle a rejected preload without pretending the game is ready.
   In the sample, `scene.spawn(self, ...)` owns boot work and `scene.preload(scene):await()` reports
   load failure. Keep the real API contract instead of inventing synchronous loading helpers.
4. Build a fresh gameplay scene/run with explicit starting state. Keep run data separate from saved
   settings and profile progression. Restart must create/reset the intended run state, and must not
   keep the old enemies, callbacks or RNG state by mistake.
5. Map actions through the current `haylen.input` contract and content action maps. Turn input into
   domain actions once. Check `ui.usingPointer()` before raw pointer input drives gameplay, and
   `ui.usingKeyboard()` before raw keys do, so a menu click or typed space does not also trigger
   gameplay.
6. Choose the timing model. Use `fixedUpdate(dt)` where fixed-step simulation/physics needs it.
   It can run zero or several times per rendered frame. Use `update(dt)` for frame updates where it
   fits. Tiny Island's game system uses `update(dt)`, so neither fixed-step nor an ECS is required
   for every title. Avoid movement/timers based on frame counts, and check behavior across frame
   rates.
7. Render without moving the real game state forward. Use the world viewport/camera on purpose, then
   draw retained UI as an overlay. Do not stretch world assets or cut off key controls at notches.
   Keep important HUD controls focusable when it fits, and keep decorative status out of focus paths.
8. Check one full run and replay before you add more content. Each progression/shop/action must
   clearly show whether it is available and give feedback. A disabled action needs a visible reason
   when the user might otherwise think the game is broken.

## Pause and lifecycle are explicit state changes

Stack `pause`/`resume`, process/game `paused`/`unpaused`, app inactive/background, audio
interruption and an SDK screen cover are different events. Follow the chosen lifecycle guide
instead of assuming that stopping rendering saves data or that every covered scene is unloaded.

Tiny Island pushes a pause scene on background and, depending on lifecycle settings, on focus loss.
Its gameplay `pause` hides the HUD and clears virtual input, and `resume` either resumes the run or
does an exit that was explicitly asked for. The engine's away-time halt alone does not guarantee
that a player comes back to a planned pause menu. Choose the behavior that fits the game.

For a pause overlay, decide whether the world underneath should stay visible and frozen. Set the
documented scene transparency/process behavior and implement the right hooks. Transitions use real
time, separately from game pause. Do not let a held touch/action stay active after a pause,
orientation change, native screen or focus loss. Prevent several queued pause/results scenes.

Keep the audio preference separate from a short suspension. Resume audio only if the app may play
and the user's saved choice allows it. Closing a focus loss, an ad or a native screen must not
unmute the user. Save needed progression through documented storage/lifecycle APIs, without
waiting for an exit event that may never come. Test process termination and half-finished writes
where they matter.

## Resource, async and native boundaries

Work owned by a scene ends on unload, not just when the scene is covered. World/HUD/audio resources
you own explicitly must have an exact cleanup path. The game sample destroys the HUD/world it owns
by hand on exit. Retained GUI mounted with a scene owner is already managed by the engine, so do not
also destroy it through an unrelated lifetime rule. Cleanup must handle runs that only partly
started and failed loads. Cancel timers/listeners and clear references that could point at a
destroyed world.

Run SDK/network work through the real async/native contracts without blocking the frame. A late
leaderboard, cloud-save or reward result must go to the right run/account and be applied once.
Do not give a reward on an ad request, a cancel or a failed purchase. Plugin screens and stream
resources need platform cleanup on pause/dismissal. Use the plugin guide for native ownership
instead of inventing callbacks or fallbacks that report success.

For C++ code, use the requested standard's features, RAII and explicit namespace/class ownership.
Keep frame-thread work and worker results separate, hold needed objects safely and release them
after native work is really done. Check lengths and arithmetic at content/native boundaries.
Use sanitizer/thread diagnostics for changed native lifetime/concurrency behavior when the
toolchain supports them. A static skill document cannot prove there are no memory bugs or data
races.

## Acceptance evidence

Check boot/load → menu → play → pause/resume → results → replay/exit, plus load failure and the
requested save/restart behavior. Test repeated transitions, several starts, fast input, controller
disconnect, touch cancel, text entry over gameplay, low/high frame rates, resizing/safe areas,
background/focus/audio interruption and native integration cancel. Include real denial/offline
paths if used. Check saved progression after a process restart and another valid session.

Build and `app verify` the requested Debug and Release packages, then run the relevant target.
Headless logic tests can check the domain rules they cover, but cannot prove GPU output, animation
quality, mobile comfort, native SDK behavior or store approval. Record screenshots/logs and real
hardware gaps.
