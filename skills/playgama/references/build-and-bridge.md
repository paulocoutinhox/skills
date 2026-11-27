# Build and required Bridge integration

## Research and engine selection

Read `get_bridge_sdk_docs` for the module index and the required `api` page, `get_game_checklist` for all requirements that apply, and the relevant `get_game_guides`. Read them again before every archive upload. Use the binding that matches the real engine. Draft creation, as checked, supports Unity, Construct 3, Cocos Creator, Defold, Godot, GDevelop, GameMaker, Scratch, and plain JavaScript. Check the current enums before creating.

Follow the engine's documented release HTML5/WebGL export and the repository's build command. Do not invent one build command for every engine. Confirm correct relative asset paths, runtime compression and server support, WebAssembly and thread needs, mobile memory behavior, and the Bridge plugin version.

## Mandatory SDK lifecycle

Ship a valid `playgama-bridge-config.json` next to the archive-root `index.html`. Load the supported Bridge SDK before the engine and assets, and finish initialization before starting the game. The current plain-JavaScript contract uses `bridge.initialize()`. Its documented head script must load before game code, without late dynamic loading or `async`. Engine templates or plugins may already do this setup, so do not initialize twice.

After initialization, use the platform language for localization, restore progress through Bridge Storage before gameplay, and send the documented `game_ready` message only when the first interactive frame can be used. Save important progress, settings and purchase changes in batches through Bridge Storage. Current requirements do not allow browser storage or engine save systems in its place for player progress.

Apply the starting audio permission before any sound, then handle platform audio and pause events and visibility changes. Request interstitial opportunities at natural breaks in gameplay through Bridge. Current guidance leaves ad timing and caps to Bridge rather than adding your own timers. Hide controls for payments, rewarded ads, leaderboards, sign-in or external links that are not supported, using their explicit capability APIs. This is intended platform behavior, not an invented silent fallback.

## Environment detection and initialization failures

Use the current [setup](https://wiki.playgama.com/playgama/bridge-sdk/setup), [configuration](https://wiki.playgama.com/playgama/bridge-sdk/config) and [platform](https://wiki.playgama.com/playgama/bridge-sdk/api/platform) contracts for the installed integration. Prefer automatic platform detection. Unsupported local environments use the SDK's mock adapter. The SDK provides that behavior. It is not a success response that the application creates.

Use a forced adapter setting only when the chosen binding's current documentation offers it, and only in a documented test environment that you control on purpose. Never force the platform in production. Do not claim a universal `qa_tool` platform ID. The QA harness is a test environment, and you must read the adapter ID from the real SDK.

| Environment | What it establishes |
| --- | --- |
| Local static server with detected mock | Relative assets, rendering, input and application flows. Simulated features are not real platform acceptance. |
| Supported local QA harness | Testing connected to the host through the returned local QA link, if the browser and network allow it. |
| Uploaded archive in QA Tool | The real packaged files, host messages, capability handling, readiness and supported services. |
| Published sandbox or production | Behavior of the real active archive and destination adapter. An earlier QA build is not enough evidence. |

Treat startup as clear stages: SDK loading → initialization → required state restore → interactive frame → ready. Keep the loader responsive. Catch each promise rejection or engine callback failure and report the stage. Use a time limit that the application chooses and a retry or error state the player can act on, instead of an endless spinner. Do not describe that time limit as a number the vendor requires.

An initialization timeout does not allow calling SDK APIs before initialization, sending game-ready early, or switching a production build to mock. Check the first failed request, the installed template or plugin, where the config is, the detected adapter, the container or embed, network or privacy blocking and double initialization. After fixing the cause, test in the supported real container. Under the current API contract, SDK initialization is still required before loading the game.

Keep optional sign-in apart from required initialization. If the player rejects or cancels optional login, return to playable guest mode where the initialized platform supports it. Do not force login at launch or make loading the profile a needless start gate. A network failure never proves that an existing cloud save is empty.

Keep one owner for initialization and its completion. A time limit running out does not always cancel the promise behind it. Ignore old completions after a planned retry or disposal, avoid starting a scene twice, and remove event listeners when their owner is destroyed. Record stage timings, SDK and engine versions and cleaned errors. Never show tokens or full player or save data in diagnostic logs.

## Godot integration checks

Use the official plugin release that matches the project's real Godot major version. For a Godot 4 project, install into `res://addons/`, turn on the plugin, and put the `Bridge` singleton first in AutoLoad as the current setup requires. The plugin initializes by itself. Wait for its documented initialization state or signal before gameplay and API calls that depend on it, rather than adding a second separate initialization.

Set the Web export's Custom HTML Shell to `res://addons/playgama_bridge/template/index.html`. Edit the plugin template's `playgama-bridge-config.json` at `addons/playgama_bridge/template/` and check that the exported config sits next to the root index. Check the exported archive, not just the editor paths.

Current binding examples include `Bridge.platform.id`, `Bridge.platform.is_audio_enabled`, `Bridge.platform.send_message("game_ready")` and the `audio_state_changed` / `pause_state_changed` signals. Godot 4 connects callbacks through `Callable`. Follow the current plugin's exact initialization and storage callback contract. Plain-JS camelCase or a Unity callback is not a Godot method.

Test browser export input, audio, scene changes and storage in the real host. A native editor run cannot prove browser iframe messages or ad readiness. Debug a stuck exported build at the first stage that fails, rather than treating engine rendering and platform initialization as the same thing.

## One audio and pause owner

Use [the sound guide](https://wiki.playgama.com/playgama/guides/game-development/sound) for implementation help together with mandatory UX section 3.3 and advertising rule 2.1.6.

Show a clear mute/unmute button on the main menu and the pause menu. Its icon or label shows the player's choice. Save that choice through Bridge Storage and apply it to music, sound effects, interface sounds and in-game video. You can offer separate channel sliders, but they do not replace a working master mute.

Keep separate state for player mute, host audio permission, host pause, page visibility, the real fullscreen-ad state and browser audio unlock. Work out the effective audio in one place from those states. Only the mute control changes the player's choice. Focus events and ad completion must not overwrite it.

Read `platform.isAudioEnabled` right after initialization and before starting any audio. Then subscribe to `AUDIO_STATE_CHANGED` and `PAUSE_STATE_CHANGED`, or the binding's real equivalents. Listening only for later events fails when the host is already muted at launch. A new scene or audio node must take the current effective state right away.

Pause gameplay and timers and silence audio during fullscreen ads and required platform pauses. Track the real interstitial and rewarded state and page visibility through the same owner. Clearing one pause reason does not clear the others. On return, restore the scene and time state without running hidden combat forward or resetting progress. Repeated blur/focus and ad callbacks must be idempotent, which means running them again has no extra effect. They must not stack volume changes or listeners.

For example, player mute + open ad + hidden page means silent. Closing the ad still means silent. Returning to the page still means silent until the player changes their own choice and the platform allows audio. If the player was unmuted but paused by hand, closing the ad must not resume gameplay.

Unlock browser audio through the engine's supported first-gesture handler. Resuming a suspended context, including on iOS after the app was in the background, must still respect every mute reason. Resuming the audio context is not permission to start music. Do not force sound during loading before a gesture. Use proper licensed or produced compressed audio files rather than tones made in code.

## Restore and persist meaningful state

Use [Bridge Storage](https://wiki.playgama.com/playgama/bridge-sdk/api/storage) and the [saving guide](https://wiki.playgama.com/playgama/guides/game-development/saving-progress). Group a small fixed set of keys for real progress, economy, settings and onboarding. After initialization, load the required keys together before gameplay. In plain JS, `storage.get(["progress", "economy", "settings"])` returns values by position and `storage.set(keys, values)` uses parallel arrays. Do not invent one object-shaped API for all engines.

For current Godot 4, `Bridge.storage.get(keys, Callable(...))` reports success apart from the returned data. A successful read with a missing value can start a new player. A failed operation cannot prove that the account has no save. Do not erase known state, report cloud syncing or quietly switch to the application's own `localStorage`, IndexedDB, cookies or engine saves. Bridge may use browser storage inside itself on some destinations. That is different from going around its API.

Write the changed important keys together at progress, purchase or reward, and settings points. Save progress before an ad or an action likely to end a session, and handle visibility changes through the same save owner. Do not rely only on an async unload callback, which the browser may cut off. Avoid writing on every frame or tap. For idle progress that builds up over time, follow the documented batching guidance rather than saving every small increase.

Queue or merge overlapping saves so an older snapshot cannot finish last and undo a newer purchase or settings change. Keep the newest unsaved state until the save is confirmed. Do not clear it just because a write was attempted. This stops local write races, but it does not prove conflict handling across devices or transactional platform storage. Use the real backend guarantees and a trusted entitlement service where valuable state needs stronger protection.

Test progress and settings across reload, orientation, ads, account and session changes, and write or read failures. Confirm the available storage backend and a real cloud round trip when that destination supports cloud storage. A mock adapter or a browser cache round trip cannot prove syncing. Report cloud features that are not supported accurately.

## SDK module routing

| Module | Implementation checks |
| --- | --- |
| Platform | Language, messages, pause/audio, device/orientation and allowed external links |
| Storage | First batch load, important batch writes, cloud/player scope, errors and crash recovery |
| Player | Supported sign-in, user identity, optional sign-in that does not block first play |
| Advertisement | Interstitial, rewarded, banners, state events, reward completion and placement |
| Payments | Supported stores, product config, prices, purchase, consume, restore and verification |
| Leaderboards | Available mode, fixed tags, score types, sign-in and score protection |
| Analytics | Supported, limited events and privacy and distinct-value rules |
| Other current modules | Find them through the live index and read the needed page before using methods |

Use the exact engine-specific methods and events and the current platform support from those pages. The offline management tool list is not a Bridge SDK type declaration. Do not guess JavaScript method names from C#, Lua or Godot samples.

## Build quality

The current technical requirements include an archive-root `index.html`, Latin file and folder names, game files within 300 MB, startup peak memory below 2 GB, and desktop play. The upload method also caps the ZIP size at 300 MB. Check both the total game-file size and the compressed upload size. Bundle game resources locally, with the required supported SDK loader added as documented. Do not add unrelated external analytics or resource CDNs against the current rules.

Test mouse and keyboard, and touch on every device you claim. Fit the canvas to the available aspect ratio, including narrow, wide and square screens and fold or orientation changes where relevant. Avoid stretched art, cut-off controls, overlapping text, dialogs that cannot be reached, browser scroll problems, and audio that keeps playing behind ads or in the background. Desktop support is mandatory, and the game must not use Esc. Check all mobile and video requirements that may apply in the [review matrix](review-requirements.md).

For Unity WebGL, current engine-specific rule 5.1.1 requires **Decompression Fallback enabled**. Also check the exported loader and compression behavior on the real host. This named build option is a required engine setting, not a generic application fallback. Do not turn it off because of an outdated search result, and do not apply Unity settings to another engine.

Use a fixed, repeatable release version in the game metadata and archive name, and keep an internal build number that only goes up. A new fixed upload creates a new archive ID and a clear version. Keep the source revision, engine and Bridge versions, build command, archive hash, and size. Do not suggest that Playgama enforces Apple's or Android's exact version-number fields.

## Packaging and local QA

Package only the runtime files for release, with `index.html` at the ZIP root. Leave out `.git`, source-only secrets, `.env`, signing material, dependency caches, editor files, logs, local databases, server credentials, and source maps you do not need. Check archive entries for path traversal (paths that climb out of the folder) and absolute names, and test unpacking into a clean temporary folder.

Serve the output locally and request `get_local_game_qa_tool_link` with the real local index URL. Test load, game-ready timing, progress restore, pause and audio, ads, purchases, leaderboards, localization, resizing, and failure states through the harness. Check the numbered live checklist and record anything that cannot be tested. Do not upload an archive that you already know fails required checks.
