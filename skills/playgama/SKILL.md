---
name: playgama
description: Guide HTML5 game creation, Bridge integration, metadata, monetization, numbered moderation requirements, QA and publication through documented Playgama tools. Use for a full launch, a rejected build or a release review based on evidence.
license: MIT
---

# Playgama

Prepare a game that plays well and is set up correctly, and explain exactly which build players can get. Draft records, public QA files, a sandbox, moderation eligibility and a catalog release are separate states.

This is written guidance. It does not include a game-launch program, a generated tool list, a refresh script or a scraper. Update the stored rules only when the user asks for that. Use the real connected service tools for an authorized game task.

## Identity, gameplay and scope

Look at the repository, engine, the real round or core loop, the organization and game ID, current archives and publications, the languages and devices the game claims to support, and the endpoint scope. Use [the launch brief](assets/launch-brief.json) to record decisions. Record the authorized endpoint (`prepare`, public QA upload, sandbox publication, moderation handoff or a specific catalog update) as `authorized-endpoint`. Finish the steps needed inside it, then stop. Report the next call or console action that changes state, and what it will do.

Read the existing games before you create another draft. If a create response is unclear, check the existing records, because titles are not unique. If the current organization cannot see a game, that does not prove the game never existed.

For a review, check every numbered requirement that applies, not just the reported defects. The current groups are technical, advertising and payments, UX, content and engine-specific requirements. Add the real destination limits and the required Bridge API steps. Keep mandatory rules apart from guide recommendations and the project's own engineering choices. [The review matrix](references/review-requirements.md) explains coverage and when each rule applies. Fill in [the evidence report](assets/review-report.md) for the real archive under review.

Connect the official remote MCP endpoint `https://developer.playgama.com/api/mcp`. There is no token to create or paste: the server uses OAuth 2.1 with dynamic client registration and PKCE, and the owner approves the agent on a consent page of developer.playgama.com. In Claude Code, add it with `claude mcp add --transport http playgama-developer-cabinet https://developer.playgama.com/api/mcp`, then run `/mcp`, pick the server and sign in. A server added during a session loads only in a new session. When the current session must go on, the agent can run the same standard OAuth flow itself and speak MCP over Streamable HTTP, as [the connection guide](references/mcp-and-tool-map.md#log-in-with-oauth) describes. Find the real tools and schemas at runtime. Arguments that a schema does not declare are rejected. Do not ask for credentials in chat or guess a private console REST endpoint. The sources checked do not document a general first-party publishing CLI.

## What each tool does

The public reference checked for this skill describes the management tools below. A tool name tells you what it can do, not that you are allowed to use it. Check the current tool contract for exact enums and nested parameters before you run a real action.

| Tools | Responsibility |
| --- | --- |
| get_launch_steps | Ordered progress and next action, including unresolved sources |
| list_applications, create_application, get_application | Organization games, draft creation and saved form/archive state |
| update_application_form, get_game_categories | Partial form save and current category-selection rules |
| get_submission_state, list_moderation_comments | Eligibility for a named archive and read-only review messages |
| start_archive_upload, confirm_archive_upload, get_archive_status | Presigned upload, public QA processing and build result |
| start_cover_upload, confirm_cover_upload | Exact cover slots, checked replacement and public media |
| list_in_app_products, replace_in_app_products | Whole catalog plus a checksum that blocks overwriting newer changes |
| list_leaderboards, create_leaderboard, update_leaderboard | Fixed tags and allowed ranking settings |
| get_archive_qa_tool_link, get_local_game_qa_tool_link | Real QA and certification URLs for each deployment |
| get_bridge_sdk_docs, get_game_checklist, get_game_guides | Live engine and module requirements during real development |
| get_game_telemetry_guide | Rules for events, privacy and the number of distinct values |
| get_game_telemetry_analytics, get_game_telemetry_event_analytics | Limited overview and per-field event totals |
| get_game_telemetry_timeseries, get_game_telemetry_session_facts | Time buckets and filtered, pseudonymized event sequences |
| get_sandbox_state, get_sandbox_share, publish_sandbox | Sandbox revision and verdict, prepared sharing and public release |
| get_publications | Recorded publication destinations, checked against active archives |
| get_sandbox_traffic, start_sandbox_traffic | Eligibility, offer and run state, versus traffic spending that cannot be undone |
| send_playgama_catalog_update | Instant update without moderation for a game already live in the catalog |
| get_referral_program, apply_referral_code | Organization referral state and acceptance of a code the developer gives |

The first moderation submission, replies, leaderboard deletion and free screenshot or video uploads are not part of these management tools. Do not invent a method. Finish the supported preparation and give the exact console handoff. [Tool detail](references/mcp-and-tool-map.md) explains every named tool.

## Build and required Bridge lifecycle

Use the engine's own supported release HTML5/WebGL export. The engines checked include plain JavaScript, Unity, Construct, Cocos Creator, Defold, Godot, GDevelop, GameMaker and Scratch. Choose real binding and tool versions and real relative asset and server behavior, not one made-up build command for every engine.

Ship a valid `playgama-bridge-config.json` next to the archive-root `index.html`. Finish the supported Bridge initialization before loading or starting the game. The current plain-JS loader goes in the head and must not load asynchronously after the game. Do not call SDK APIs before initialization. Do not initialize twice in an engine template that already does this step.

Keep a loading and error screen that responds, and handle rejected promises, callbacks and your chosen time limits on purpose. The required start order does not excuse a spinner that never ends. Optional login must not block play. Let Bridge detect the real environment. Look for accidental platform overrides such as `forciblySetPlatformId`, check them against the installed binding's contract, and remove wrong forcing from production. Do not assume that every QA host has a certain adapter ID. Do not replace a broken production handshake with a fake success.

Local mock behavior is only evidence for development. Test real host messaging in the supported QA container and in the uploaded archive. When you look into a timeout, record the initialization stages, the detected adapter and the first operation that failed. A successful mock run does not prove production ads, sign-in or cloud saves.

Use the platform language, restore progress through Bridge Storage before play, and send game-ready only when the first interactive frame can be used. The plain-JS call is `bridge.platform.sendMessage("game_ready")`. Current Godot uses `Bridge.platform.send_message("game_ready")`. Check the binding you chose rather than copying a method from another engine. Do not send ready when the plugin is imported, before state is restored or again on each focus.

Save important progress, settings and purchase changes in batches through Bridge Storage. Browser or engine save systems cannot replace the current required progress contract. Bridge picks the platform storage that is available, including cloud where supported. Check cloud round trips on the real destination instead of claiming that local mock writes prove syncing. Tell apart a successful read with no saved value from a transport or read failure. Never overwrite unknown existing progress with a made-up empty success.

Hide purchase, reward, sign-in, leaderboard and external-link UI that the platform does not support, using the explicit capability checks, rather than showing broken controls. A worked load order is: valid archive and config → Bridge initialized → language, storage and starting audio restored → real first interactive frame → game-ready → gameplay. An animation that looks loaded while input is still blocked is not the ready point.

## Sound, focus and pause acceptance

Put a visible mute control on the main menu and the pause menu. Players must be able to silence all game audio before they start playing. Supply suitable compressed music and action and interface sounds that you have the rights to distribute. The current rules reject tones generated in code as a stand-in for finished audio. Respect browser autoplay rules: unlock audio on a valid gesture and do not force sound on the loading screen.

One controller owns the effective audio state. Keep the player's saved mute apart from platform audio permission, platform pause, an open fullscreen ad, page visibility and whether the browser audio context is ready. Audio may play only when every condition that applies allows it. Apply the starting `platform.isAudioEnabled` value before any sound and subscribe to later audio and pause changes. Code that only listens for events misses a host that is already muted.

When the game is hidden or minimized, or a fullscreen ad is open, the game must be silent. Pause gameplay and timers when required. Getting focus back or closing an ad clears only that one reason. It must not turn on music the player muted or resume gameplay that is still paused for another reason. Keep the setting through Bridge Storage across reloads and scene changes. Test overlapping reasons, repeated events, music, sound effect and video channels, and iOS audio-context suspension. [Implementation and failure cases](references/build-and-bridge.md) explain who owns each part.

## Packaging and usable gameplay

Current technical rules include Latin file and folder names, a root index, total game files within 300 MB, a ZIP upload within its 300 MB cap, startup peak memory below 2 GB and desktop play. Bundle the needed game resources locally and add the real supported SDK loader. Do not add unrelated external analytics or CDNs against the rules.

Leave out `.git`, source-only secrets, local environment files, dependencies and caches, logs, debug data and source maps you do not need. Check the archive root and paths, not just whether a ZIP was made. A parent folder wrapped around index.html can break startup.

Test keyboard and mouse and every touch device you claim, different screen shapes, orientation changes, loading, restart and progress restore, pause and audio, and memory. There must be no stretched art, overlapping labels, hidden controls, blocking sign-in or scroll problems. Use the real local QA link or harness and evidence for each numbered requirement. Say what you could not check.

Explain resource limits where the action happens: remaining action points or energy, price, requirements and the next valid action. Disabled buttons need a clear reason. Test every visible scene and shop, several progress cycles, repeated purchases and recovery after cancel or error. Consumables may be bought again, but permanent products must not be bought twice. Fix truly broken controls and stuck locks instead of calling unclear behavior intentional.

Check English and every translation you claim, onboarding, a matching title in the game and in the form, content limits, art and audio rights, and personal-data permissions. A person must really improve any AI-assisted art or text. Emoji cannot replace UI icons designed for the game. For Unity, current numbered rule 5.1.1 requires the named WebGL **Decompression Fallback** setting. Read the engine and chosen partner requirements before export, including where the game can really be distributed. The [full review matrix](references/review-requirements.md) also covers the video, mobile, payment and destination rules that apply only in some cases.

Give every new release archive a clear version and a record of its source and hash. Playgama archive identities are not Apple's CFBundleVersion or Android's versionCode. [Build detail](references/build-and-bridge.md) explains the specific integration limits.

## Metadata, category and artwork

Write the promise from the real mechanic and player experience. A strategy game should explain its decisions and progress, a runner its controls and timing, and a puzzle its real challenge. Do not make up popularity, earnings or a feature. Clear instructions explain the goal, controls, how you win or lose, and the first useful action.

The title allows at most 120 English or Latin-script characters and must have a Latin letter. Description and how-to-play need at least 100 characters for submission. Shorter drafts can be saved. Supported languages and devices must be real, with at least one of each at submission. Current device values are IOS, ANDROID and DESKTOP. A story, when supplied, is an English Latin-script development note of 150–900 characters, with no links or email, and not an invented author history.

These texts and the cover art are product content that players see. Never describe how they were made or mention AI, agents, tools or prompts in them unless the owner asks for it. Record agent and model information only in the form's optional `agent`, `model` and `modelId` declaration fields, from confirmed facts. [Metadata detail](references/metadata-and-artwork.md) explains those fields.

Read the category guidance and choose by the core mechanic and the exclusion rules, not only by title or theme. The category the developer saves is separate from Playgama's own catalog classification. Do not promise that saving the form controls the public catalog category.

| Cover slot | Exact dimensions | Encoding/size |
| --- | --- | --- |
| square | 800×800 | PNG/JPEG, at most 10 MB |
| portrait | 1080×1920 | PNG/JPEG, at most 10 MB |
| landscape | 1920×1080 | PNG/JPEG, at most 10 MB |

All three are required for the sandbox path. Covers are store key art, held to the level of the top games in the catalog: the game's real logo inside an illustrated, high-energy scene of the game's own objects and mechanic, with depth, lighting and one clear focal point. A screenshot, a UI capture in a frame or a logo floating over a plain gradient is not a cover. Generate art with no text using an available image generator in the game's own style, place the official logo file over it so the name is exact, and recompose each aspect ratio. When no image generator is available, use art the owner supplies or commissions, and report the cover slots as blocked until that art exists. Check the exact text, crop, readability at small size on the console's dark background, and the real output format and bytes. Confirming publishes a permanent media file and replaces that slot. See [metadata/artwork detail](references/metadata-and-artwork.md#cover-art-standard).

## Ads, purchases and player services

Use the supported Bridge ads and add interstitial opportunities where supported. Do not request a game-owned fullscreen ad during initialization or loading, at `game_ready`, when focus returns or on the first Start click before real play. Request one at a real level change, a finished attempt or game over, or a suitable return to the menu. A click alone is not a valid placement. Check custom messages and settings such as `advertisement.interstitial.autoShow`, not just direct show calls. Preloading an ad is not the same as showing it.

Let Bridge apply its own scheduling and caps. The current configurable interstitial minimum defaults to 60 seconds, which is not a universal deadline for the first ad. Do not add your own every-N-rounds or per-day counters or competing timers. Prevent duplicate requests, and stop late requests from interrupting gameplay that has resumed. Tell apart ads the host manages from ads the game triggers, and handle both through the pause and audio rules.

Rewarded ads need a clear choice by the player, with the ad and the exact benefit stated, a way to say no, and a bonus that is optional. A recovery offer is limited to once per attempt. Grant the promised benefit once, on the documented `rewarded` state, never on close alone. Failure or cancel grants nothing and must not trap gameplay. Banners must not cover controls, and fullscreen ads pause audio and gameplay without resetting player progress.

Read the existing IAP catalog and checksum before replacing the whole list. Keep every product you mean to keep. A product left out is deleted, and an empty list clears the catalog. An outdated checksum means you must read again and reapply the change, not overwrite. Follow the provider's rule to ask for explicit consent before removals.

Current product fields include a stable, unique productId, a title, an optional description, a consumable or non_consumable type and a priceUsd that is not negative and has at most two decimals. Map the exact IDs to the Bridge config and each platform dashboard. There is no documented recurring-subscription catalog type here. Do not fake recurring charges or sell banned external or real-world benefits.

Start purchases from a direct player action after the capability checks. Restore or list owned permanent products and unconsumed purchases through the real SDK. In the plain JavaScript checked, consumePurchase takes the configured product ID, not an invented order token. Verify valuable purchases through the documented backend or platform route, link product, order and user correctly, save one lasting benefit grant, and then consume only consumables. Recover from crashes and duplicate callbacks without granting twice.

The documented verification endpoint is `POST https://playgama.com/api/bridge/v1/verify`, with platform, purchase type and the returned purchase data. In the sources checked it supports Playgama, MSN and Microsoft Store, not every Bridge destination. Use the other platform's real contract where needed.

Leaderboard tags are stable and unique and match the SDK identifiers. Choose numeric or time scoring and ascending or descending order on purpose. Showing decimals does not turn whole-number score storage into storage for any fraction. Respect the real score protection and player sign-in rules. [Monetization/player detail](references/monetization-and-player-services.md) explains these checks.

## Upload, QA and publication states

Start the archive upload with the exact game, name and byte size, PUT to the returned presigned contract exactly, then confirm and poll. Confirming adds the archive and starts public QA-file processing. It does not publish the sandbox. URLs expire and are tied to an exact size and type. Do not add unrelated account sign-in headers to the storage request.

Tell apart processing DONE from a PASSED build check. PROBLEM, NOT_CHECKED, CHECKING or missing Bridge detection do not mean success. Use the real certification link, fix startup or integration and upload a fixed version. Opening a QA link does not unlock a failed build.

Upload covers in three steps: reserve → send the exact bytes → confirm. Save only the form fields you mean to change, and keep whole arrays intact. Read the launch steps and application again after each stage. UNKNOWN means not resolved, not green.

Read the sandbox verdict for the archive you mean to use. Current gates include passed checks, required covers, form and category, an eligible Bridge version (minimum 2.2.0 in the sources checked), game status, quota and rate rules, and the features that are really allowed. Publish only when it is eligible and authorized, then check the live active revision and the real link.

The first moderation submission is an owner action in the console. Get submission eligibility for the named archive and review type. A new draft answers `MODERATION_UNAVAILABLE` until it goes through the sandbox path that `get_launch_steps` shows: archive, Bridge, covers, sandbox, the certification of the form (`NO_CERTIFICATION` until a person plays the archive in the link of `get_archive_qa_tool_link`), share and traffic. Real sandbox targets and cooldowns can still block catalog availability. Do not promise that a filled form unlocks review by itself.

A build check `PROBLEM` with reason `GAME_NOT_READY` means the archive never sent `game_ready`. The usual cause is a startup failure after Bridge initialization, not the message itself. Serve the archive locally, open it in a headless browser, read the console and confirm that `sendMessage('game_ready')` fires, then upload a new versioned archive. After you change covers or the title, publish the sandbox again so the live revision shows them.

Before you call a build ready for release, finish the requirement matrix and regression report for that exact archive and hash. Mark checks you did not run as BLOCKED and explain each NOT APPLICABLE entry. A provider build PASSED is not human moderation approval. For a rejected build, link every finding to a flow you can reproduce, fix its cause and retest nearby flows on the replacement archive. Audio needs menu, focus, ad and reload combinations. Shops need repeat and failed purchases. Startup needs a check on the real host.

For a game that is already live, a catalog update reaches all catalog players without moderation. The provider requires an explicit yes for that named game, build and update after you explain the effect. Consent given for an earlier update or the sandbox does not count. Prepare concrete, reviewed work before that final decision.

Starting traffic spends the related bonus or budget and cannot be undone. Read the real offer and eligibility and get the decision the provider requires. Prepared share links do not give permission to post, and made-up social links are not valid evidence. Referral acceptance needs the real invitation the developer gives and its scope. [Publication detail](references/upload-qa-and-publication.md) keeps these differences clear.

## Observe real player outcomes

Use limited telemetry to answer a defined question. Start with the overview, data freshness and the list of events. Current ranges are at most 31 days, counting both ends. Use event distributions, time series and filtered session facts each for its own meaning. Do not join every page into a raw player export nobody authorized, and do not read event counts as a full personal history.

Compare matching build and audience time windows and the real sample size. Report whether the first loop is playable, progress is kept, errors, ad behavior and purchase matching, rather than just total visits. Raph Koster's [A Theory of Fun for Game Design](https://www.theoryoffun.com/) is useful professional reading on learning and play, checked through the author's site. It does not cover platform compliance or give a retention formula.

Deliver the source, archive, version and hash, the completed [review evidence](assets/review-report.md), form, category and media, the product checksum, player-service checks, QA, moderation, sandbox and catalog states, and the real links. A failed mandatory check blocks a ready-for-release conclusion. A written review does not certify a game that was never run. [Telemetry detail](references/telemetry-and-operations.md), [official tools](https://wiki.playgama.com/playgama/mcp/tools), [Bridge requirements](https://wiki.playgama.com/playgama/bridge-sdk/api), [source notes](references/sources.md) and [license](LICENSE.md) give focused support.
