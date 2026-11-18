# Build and required Bridge integration

## Research and engine selection

Read `get_bridge_sdk_docs` for the module index and required `api` page, `get_game_checklist` for all applicable requirements, and relevant `get_game_guides`. Refresh these before every archive upload. Use the matching actual engine binding. The researched draft creation supports Unity, Construct 3, Cocos Creator, Defold, Godot, GDevelop, GameMaker, Scratch, and plain JavaScript. Query current enums before creating.

Follow the existing engine's documented release HTML5/WebGL export and repository build command. Do not invent a single compiler command for every engine. Confirm correct relative asset paths, runtime compression/server compatibility, WebAssembly/thread requirements, mobile memory behavior, and the Bridge plugin version.

## Mandatory SDK lifecycle

Ship a valid `playgama-bridge-config.json` next to the archive-root `index.html`. Load the supported Bridge SDK before engine/assets and complete initialization before starting the game. The current plain-JavaScript contract uses `bridge.initialize()`. Its documented head script must load before game code, without late dynamic loading or `async`. Engine templates/plugins may own that setup, so avoid double initialization.

After initialization, use platform language for localization, restore progress through Bridge Storage before gameplay, and send the documented `game_ready` message only when the first interactive frame is usable. Persist meaningful progress/settings/purchase changes in batches through Bridge Storage. Current requirements disallow replacing it with browser storage or engine-local save systems for player progress.

Apply initial audio permission before any sound, then handle platform audio/pause events and visibility changes. Request interstitial opportunities at natural gameplay breaks through Bridge. Current guidance delegates ad timing/caps to Bridge rather than adding independent timers. Hide controls for unsupported payments, rewarded ads, leaderboards, authorization, or external links according to their explicit capability APIs. This is intentional platform behavior, not an invented silent fallback.

## Environment detection and initialization failures

Use the current [setup](https://wiki.playgama.com/playgama/bridge-sdk/setup), [configuration](https://wiki.playgama.com/playgama/bridge-sdk/config) and [platform](https://wiki.playgama.com/playgama/bridge-sdk/api/platform) contracts for the installed integration. Prefer automatic platform detection. Unsupported local environments use the SDK's mock adapter. That behavior is provided by the SDK, not an application-created success response.

Inspect `forciblySetPlatformId` or equivalent forced adapter settings if they exist in the selected binding. Do not introduce that older option into a current config whose documentation does not expose it. Remove inappropriate production forcing and use an override only for a documented, deliberately controlled diagnostic environment. Do not assert a universal `qa_tool` platform ID. The QA harness is a test environment, and the adapter ID must be observed through the actual SDK.

| Environment | What it establishes |
| --- | --- |
| Local static server with detected mock | Relative assets, rendering, input and application flows. Simulated capabilities are not real platform acceptance. |
| Supported local QA harness | Host-connected testing through the returned local QA link, subject to actual browser/network access. |
| Uploaded archive in QA Tool | Actual packaged files, host communication, capability handling, readiness and supported services. |
| Published sandbox or production | Behavior of the actual active archive and destination adapter. A prior QA build is insufficient evidence. |

Model startup as explicit stages: SDK loading → initialization → required state restore → interactive frame → ready. Keep the loader responsive. Catch each promise rejection or engine callback failure and report the stage. Use an application-chosen finite deadline and an actionable retry/error state instead of an indefinite spinner. Do not describe that deadline as a vendor-mandated number.

An initialization timeout does not authorize calling uninitialized SDK APIs, sending early game-ready, or changing a production build to mock. Inspect the first failed request, installed template/plugin, configuration location, detected adapter, container/embed, network/privacy interference and duplicate initialization. Validate in the supported real container after correcting the cause. SDK initialization remains required before loading the game under the current API contract.

Separate optional authentication from required initialization. Rejected/cancelled optional login must return to playable guest behavior where the initialized platform supports it. Do not force login at launch or make profile fetching an unnecessary start gate. A network failure is never evidence that an existing cloud save is empty.

Maintain one owner for initialization and completion. A deadline expiring does not necessarily cancel its underlying promise. Ignore obsolete completions after a deliberate retry or disposal, avoid duplicate scene activation, and remove event listeners when their owner is destroyed. Record stage timings, SDK/engine versions and sanitized errors. Never expose tokens or full player/save data in diagnostic logs.

## Godot integration checks

Use the official plugin release matching the project's actual Godot major version. For a Godot 4 project, install into `res://addons/`, enable the plugin, and put the `Bridge` singleton first in AutoLoad as the current setup requires. The plugin initializes automatically. Observe its documented initialization state/signal before dependent gameplay and API calls rather than adding a second independent initialization.

Set the Web export's Custom HTML Shell to `res://addons/playgama_bridge/template/index.html`. Edit the plugin template's `playgama-bridge-config.json` at `addons/playgama_bridge/template/` and verify the resulting exported config next to the root index. Check the exported archive, not just the editor paths.

Current binding examples include `Bridge.platform.id`, `Bridge.platform.is_audio_enabled`, `Bridge.platform.send_message("game_ready")` and the `audio_state_changed` / `pause_state_changed` signals. Godot 4 connects callbacks through `Callable`. Follow the current plugin's exact initialization/storage callback contract. Plain-JS camelCase or a Unity callback is not a Godot method.

Exercise browser export input, audio, scene transitions and storage in the actual host. A native editor run cannot establish browser iframe messaging or ad readiness. Debug a stalled exported build at the first unsuccessful stage rather than treating engine rendering and platform initialization as interchangeable.

## One audio and pause owner

Use [the sound guide](https://wiki.playgama.com/playgama/guides/game-development/sound) for implementation guidance alongside mandatory UX section 3.3 and advertising rule 2.1.6.

Expose a recognizable mute/unmute button on the main menu and pause menu. Its icon/label reflects the player's preference. Save that preference through Bridge Storage and apply it to music, sound effects, interface sounds and in-game video. Separate channel sliders can be offered, but they do not replace a usable master mute.

Keep independent state for player mute, host audio permission, host pause, page visibility, actual fullscreen-ad state and browser audio unlock. Compute effective audio centrally from those states. Only the mute control changes the player's preference. Focus events and ad completion must not overwrite it.

Read `platform.isAudioEnabled` immediately after initialization and before starting any audio. Then subscribe to `AUDIO_STATE_CHANGED` and `PAUSE_STATE_CHANGED`, or the actual binding equivalents. Listening only for later events fails when the host is already muted at launch. A newly created scene/audio node must inherit the current effective state immediately.

Pause gameplay/timers and silence audio during fullscreen ads and required platform pauses. Observe the actual interstitial/rewarded state and page visibility through the same owner. Clearing one pause reason does not clear others. On return, restore the scene/time state without advancing hidden combat or resetting progress. Repeated blur/focus and ad callbacks must be idempotent, not accumulate volume changes or listeners.

For example, player mute + open ad + hidden page means silent. Closing the ad still means silent. Returning to the page still means silent until the player changes their own preference and the platform permits audio. If the player was unmuted but manually paused, ad closure must not resume gameplay.

Unlock browser audio through the engine's supported first-gesture handler. Resuming a suspended context, including on iOS after backgrounding, must still respect all mute reasons. An audio-context resume is not permission to start music. Do not force sound during loading before a gesture. Use appropriate licensed/produced compressed audio assets rather than procedural code tones.

## Restore and persist meaningful state

Use [Bridge Storage](https://wiki.playgama.com/playgama/bridge-sdk/api/storage) and the [saving guide](https://wiki.playgama.com/playgama/guides/game-development/saving-progress). Group a small fixed set of keys for actual progress, economy, settings and onboarding. After initialization, load required keys together before gameplay. In plain JS, `storage.get(["progress", "economy", "settings"])` returns positional values and `storage.set(keys, values)` uses parallel arrays. Do not invent a universal object-shaped API across engines.

For current Godot 4, `Bridge.storage.get(keys, Callable(...))` reports success separately from returned data. A successful missing value can initialize a new player. A failed operation cannot establish that the account has no save. Do not erase known state, report cloud synchronization or silently fall back to application-owned `localStorage`, IndexedDB, cookies or engine saves. Bridge may internally use browser storage on some destinations. That is distinct from bypassing its API.

Write meaningful changed keys together at progression, purchase/reward and settings boundaries. Preserve progress before an ad or an operation likely to end a session, and handle visibility changes through the same save owner. Do not rely solely on an asynchronous unload callback, which the browser may terminate. Avoid frame/tap writes. For idle accumulation, follow documented batching guidance rather than persisting every increment.

Serialize/coalesce overlapping saves so an older snapshot cannot finish last and undo a newer purchase or settings change. Keep the newest dirty state until confirmed. Do not clear it just because a write was attempted. This prevents local write races, but does not prove cross-device conflict resolution or transactional platform storage. Use the actual backend guarantees and a trusted entitlement service where valuable state requires stronger protection.

Test progress and settings across reload, orientation, ads, account/session boundaries and write/read failures. Confirm the available backend and a real cloud round trip when that destination supports cloud storage. A mock adapter or a browser cache round trip cannot prove synchronization. Unsupported cloud capabilities must be reported accurately.

## SDK module routing

| Module | Implementation checks |
| --- | --- |
| Platform | Language, messages, pause/audio, device/orientation and allowed external links |
| Storage | Initial batch load, meaningful batch writes, cloud/player scope, errors and crash recovery |
| Player | Supported authorization, user identity, optional sign-in without blocking first play |
| Advertisement | Interstitial, rewarded, banners, state events, reward completion and placement |
| Payments | Supported stores, product config, prices, purchase, consume, restore and verification |
| Leaderboards | Available mode, immutable tags, score types, authorization and score protection |
| Analytics | Supported bounded events and privacy/cardinality rules |
| Other current modules | Discover through the live index and read the requested page before using methods |

Use exact engine-specific methods/events and current platform support from those pages. The offline management tool catalog is not a Bridge SDK type declaration. Do not infer JavaScript method names from C#/Lua/Godot samples.

## Build quality

The current technical requirements include archive-root `index.html`, Latin file/folder names, game files within 300 MB, startup peak memory below 2 GB, and desktop playability. The upload method also caps the ZIP size at 300 MB. Check both total game-file size and compressed upload size. Bundle game resources locally, with the required supported SDK loader integrated as documented. Do not add unrelated external analytics or resource CDNs contrary to the current rules.

Test mouse/keyboard and touch on every claimed device. Adapt the canvas to available aspect ratio, including narrow/wide/square and fold/orientation changes where relevant. Avoid distorted art, cut-off controls, overlapping text, inaccessible dialogs, browser scroll interference, and audio that continues behind ads or in the background. Desktop support is mandatory, and the game must not use Esc. Inspect all conditional mobile/video requirements in the [review matrix](review-requirements.md).

For Unity WebGL, current engine-specific rule 5.1.1 requires **Decompression Fallback enabled**. Verify the exported loader and compression behavior on the actual host as well. This named build option is a required engine setting, not a generic application fallback. Do not reverse it from an obsolete search result or apply Unity settings to another engine.

Use a deterministic release version in the game metadata/archive name and maintain a monotonically increasing internal build allocation. A new corrected upload creates a new archive ID and recognizable version. Preserve source revision, engine/Bridge versions, build command, archive hash, and size. Do not imply Playgama enforces Apple's or Android's exact version-number fields.

## Packaging and local QA

Package only release runtime files, with `index.html` at the ZIP root. Exclude `.git`, source-only secrets, `.env`, signing material, dependency caches, editor files, logs, local databases, server credentials, and unnecessary source maps. Inspect archive entries for traversal paths and absolute names, and test extraction into a clean temporary directory.

Serve the output locally and request `get_local_game_qa_tool_link` with the actual local index URL. Exercise load, game-ready timing, progress restore, pause/audio, ads, purchases, leaderboards, localization, resize, and failure states through the harness. Check the numbered live checklist and explicitly record anything that cannot be tested. Do not upload an archive already known to fail required checks.
