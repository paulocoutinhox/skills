---
name: playgama
description: Guide HTML5 game creation, Bridge integration, metadata, monetization, numbered moderation requirements, QA and publication through documented Playgama capabilities. Use for a complete launch, a rejected build or an evidence-based release review.
license: MIT
---

# Playgama

Prepare a playable, correctly integrated game and explain exactly which build players can receive. Draft records, publicly available QA files, a sandbox, moderation eligibility and a catalog release are distinct states.

This is descriptive guidance. It does not bundle a game-launch program, generated tool catalog, refresh script or scraper. Update stored rules only when the user requests maintenance. Use the actual connected native service tools for an authorized game task.

## Identity, gameplay and scope

Inspect the repository, engine, actual round/core loop, organization/game ID, current archives/publications, supported language/device claims and endpoint scope. Use [the launch brief](assets/launch-brief.json) to record decisions.

Read existing games before creating another draft. An uncertain create response requires reconciliation because titles are not unique. A game inaccessible to the current organization is not evidence that it never existed.

For a review, inspect every applicable numbered requirement, not just reported defects. The current families are technical, advertising/payments, UX, content and engine-specific requirements. Add actual destination restrictions and the required Bridge API steps. Distinguish mandatory rules from guide recommendations and project engineering choices. [The review matrix](references/review-requirements.md) explains coverage and applicability. Complete [the evidence report](assets/review-report.md) against the actual archive being reviewed.

Connect the official remote MCP endpoint `https://developer.playgama.com/api/mcp` through the client's supported OAuth flow. Discover actual runtime tools/schemas. Undeclared arguments are rejected. Do not collect credentials in chat or extrapolate a private console REST endpoint. The researched sources do not document a general first-party publishing CLI.

## Research-backed tool responsibilities

The researched public reference describes the following management surface. Names explain capability, not authorization. Inspect the current tool contract for exact enums/nested parameters before executing a real action.

| Tools | Responsibility |
| --- | --- |
| get_launch_steps | Ordered progress and next action, including unresolved sources |
| list_applications, create_application, get_application | Organization games, draft creation and saved form/archive state |
| update_application_form, get_game_categories | Partial form save and current category-selection rules |
| get_submission_state, list_moderation_comments | Explicit-archive eligibility and read-only review correspondence |
| start_archive_upload, confirm_archive_upload, get_archive_status | Presigned upload, public QA processing and build verdict |
| start_cover_upload, confirm_cover_upload | Exact cover slots, validated replacement and public media |
| list_in_app_products, replace_in_app_products | Whole catalog plus optimistic-concurrency checksum |
| list_leaderboards, create_leaderboard, update_leaderboard | Stable tags and allowed ranking configuration |
| get_archive_qa_tool_link, get_local_game_qa_tool_link | Actual deployment-specific QA/certification URLs |
| get_bridge_sdk_docs, get_game_checklist, get_game_guides | Live engine/module requirements during actual development |
| get_game_telemetry_guide | Instrumentation/privacy/cardinality contract |
| get_game_telemetry_analytics, get_game_telemetry_event_analytics | Bounded overview and event-field aggregates |
| get_game_telemetry_timeseries, get_game_telemetry_session_facts | Time buckets and filtered pseudonymized sequence evidence |
| get_sandbox_state, get_sandbox_share, publish_sandbox | Sandbox revision/verdict, prepared sharing and public release |
| get_publications | Recorded publication destinations, reconciled with active archives |
| get_sandbox_traffic, start_sandbox_traffic | Eligibility/offer/run state versus irreversible traffic spending |
| send_playgama_catalog_update | Immediate unmoderated update for a game already live in catalog |
| get_referral_program, apply_referral_code | Organization referral state and developer-supplied acceptance |

Initial moderation submission, replies, leaderboard deletion and arbitrary screenshot/video uploads are not present on this researched management surface. Do not invent a method. Complete supported preparation and give the precise console handoff. [Tool detail](references/mcp-and-tool-map.md) expands all named responsibilities.

## Build and required Bridge lifecycle

Use the actual engine's supported release HTML5/WebGL export. The researched engine choices include plain JavaScript, Unity, Construct, Cocos Creator, Defold, Godot, GDevelop, GameMaker and Scratch. Choose real binding/tool versions and relative asset/server behavior, not one made-up compile command for every engine.

Ship valid `playgama-bridge-config.json` beside archive-root `index.html`. Complete the supported Bridge initialization before loading/starting the game. The current plain-JS loader belongs in the head and must not be loaded asynchronously after the game. Do not call SDK APIs before initialization or double-initialize an engine template that owns this step.

Keep a responsive loading/error interface and handle rejected promises, callbacks and chosen deadlines explicitly. Required initialization order does not justify an infinite spinner. Optional login cannot block play. Let Bridge detect its actual environment. Inspect accidental platform overrides such as `forciblySetPlatformId` against the installed binding's contract and remove inappropriate production forcing. Do not assume that every QA host has a particular adapter ID or replace a broken production handshake with mock success.

Local mock behavior is development evidence. Test real host messaging in the supported QA container and uploaded archive. Capture initialization stages, detected adapter and the first failed operation when investigating a timeout. A successful mock run does not validate production ads, authorization or cloud persistence.

Use platform language, restore progress through Bridge Storage before play, and emit game-ready only when the first interactive frame is usable. The plain-JS call is `bridge.platform.sendMessage("game_ready")`. Current Godot uses `Bridge.platform.send_message("game_ready")`. Verify the selected binding rather than copying a method from a different engine. Do not send ready at plugin import, before state restore or repeatedly on focus.

Batch meaningful progress/settings/purchase writes through Bridge Storage. Browser/engine-local save systems are not a substitute for the current required progress contract. Bridge selects the available platform backend, including cloud where supported. Verify cloud round trips on the real destination instead of claiming local mock writes prove synchronization. Distinguish a successful read with no saved value from a transport/read failure, and never overwrite unknown existing progress with a fabricated empty success.

Hide unsupported purchase/reward/auth/leaderboard/external-link UI through explicit capabilities rather than displaying broken controls. A worked load sequence is: valid archive/config → Bridge initialized → language/storage and initial audio restored → actual first interactive frame → game-ready → gameplay. An animation that looks loaded while input is blocked is not the ready boundary.

## Sound, focus and pause acceptance

Provide a visible mute control on the main menu and pause menu. Players must be able to silence all game audio before entering play. Supply suitable compressed music and action/interface sound assets with distribution rights. The current rules reject procedural tones generated in code as a substitute for finished audio. Respect browser autoplay: unlock audio on a valid gesture and do not force loading-screen playback.

One controller owns effective audio state. Keep the player's saved mute separate from platform audio permission, platform pause, an open fullscreen ad, page visibility and browser audio-context readiness. Audio may play only when every applicable condition allows it. Apply the initial `platform.isAudioEnabled` before any sound and subscribe to later audio/pause changes. An event-only implementation misses an already-muted host.

Hide/minimize and fullscreen ads silence the game. Pause gameplay/timers when required. Returning focus or closing an ad clears only that reason. It must not turn on player-muted music or resume gameplay still paused for another reason. Preserve the setting through Bridge Storage across reloads and scene changes. Test overlapping reasons, repeated events, music/SFX/video channels and iOS audio-context suspension. [Implementation and failure cases](references/build-and-bridge.md) explain these ownership boundaries.

## Packaging and usable gameplay

Current technical rules include Latin file/folder names, root index, total game files within 300 MB, ZIP upload within its 300 MB cap, startup peak memory below 2 GB and desktop playability. Bundle required game resources locally and integrate the actual supported SDK loader. Do not add unrelated external analytics/CDNs contrary to the rules.

Exclude `.git`, source-only secrets, local environment files, dependencies/caches, logs, debug data and unnecessary source maps. Inspect archive root and paths, not merely whether a ZIP was produced. A parent directory wrapped around index.html can break startup.

Test keyboard/mouse and every claimed touch device, responsive aspect ratios, orientation changes, loading/restart/progress restore, pause/audio and memory. No stretched art, overlapping labels, hidden controls, blocking sign-in or scroll interference. Use the actual local QA link/harness and numbered requirement evidence. State what could not be checked.

Explain resource limits where actions occur: remaining action points/energy, price, prerequisites and the valid next action. Disabled buttons need a clear reason. Test every visible scene and shop, multiple progression cycles, repeated purchases and recovery after cancel/error. Consumables may be repeatable while permanent products must not be repurchased. Fix genuinely broken controls and stale locks instead of calling unclear behavior intentional.

Check English and all claimed translations, onboarding, matching in-game/submitted title, content restrictions, artwork/audio rights and personal-data permissions. Human refinement of AI-assisted output matters. Emoji cannot replace purpose-designed UI icons. For Unity, current numbered rule 5.1.1 requires the named WebGL **Decompression Fallback** setting. Read engine and selected partner requirements before export, including actual distribution availability. The [full review matrix](references/review-requirements.md) covers conditional video/mobile/payment and destination rules too.

Give every new release archive a recognizable version and source/hash record. Playgama archive identities are not Apple's CFBundleVersion or Android's versionCode. [Build detail](references/build-and-bridge.md) explains the specific integration boundaries.

## Metadata, category and artwork

Write the promise from the real mechanic and player experience. A strategy game should explain decisions/progression, a runner its control/timing, and a puzzle its actual challenge. Do not fabricate popularity, earnings or a feature. Clear instructions explain objective, controls, success/failure and the first meaningful action.

The researched title allows at most 120 English/Latin-script characters with a Latin letter. Description and how-to-play need at least 100 characters for submission. Shorter drafts can save. Supported languages/devices must be real, with at least one at submission. Current device values are IOS, ANDROID and DESKTOP. A story, when supplied, is an English Latin-script 150–900-character development note without links/email, not invented author history.

Read category guidance and choose by core mechanic/exclusion rules, not only title/theme. The developer's saved category is separate from Playgama's independent catalog classification. Do not promise that a form save controls the public catalog category.

| Cover slot | Exact dimensions | Encoding/size |
| --- | --- | --- |
| square | 800×800 | PNG/JPEG, at most 10 MB |
| portrait | 1080×1920 | PNG/JPEG, at most 10 MB |
| landscape | 1920×1080 | PNG/JPEG, at most 10 MB |

All three are required for the researched sandbox path. Generate original proportional image-model artwork when requested, using genuine gameplay evidence for UI claims. Recompose per aspect ratio. Inspect exact text, anatomy, crop, small-size readability and real output format/bytes. Confirmation publishes a permanent media file and replaces that slot. See [metadata/artwork detail](references/metadata-and-artwork.md).

## Ads, purchases and player services

Use supported Bridge ads and implement interstitial opportunities where supported. Do not request a game-owned fullscreen ad during initialization/loading, `game_ready`, focus restoration or the initial Start click before meaningful play. Request at a genuine level transition, completed attempt/game over or appropriate menu return. A click alone is not a valid placement. Audit custom messages and configuration such as `advertisement.interstitial.autoShow`, not just explicit show calls. Preloading an ad is different from showing it.

Let Bridge enforce its scheduling and caps. The current configurable interstitial minimum defaults to 60 seconds, not a universal first-ad deadline. Do not add independent every-N-round/day counters or competing timers. Prevent duplicate requests and delayed requests from interrupting resumed gameplay. Distinguish host-managed ads from game-triggered ones and handle both through the pause/audio contract.

Rewarded ads require deliberate opt-in with the ad and exact benefit disclosed, a decline path and an optional bonus. A recovery offer is limited to once per attempt. Grant the promised benefit once on the documented `rewarded` state, never on close alone. Failure/cancellation grants nothing and cannot trap gameplay. Banners must not cover controls, and fullscreen ads pause audio/gameplay without resetting player progress.

Read the existing IAP catalog/checksum before whole-state replacement. Preserve every intended product. An omitted product is deleted and an empty list clears the catalog. A stale checksum requires reread/reapplication, not an overwrite. Follow the provider's explicit consent requirement for removals.

Current product fields include stable unique productId, title, optional description, consumable/non_consumable type and nonnegative priceUsd with at most two decimals. Map exact IDs to Bridge config and each platform dashboard. There is no documented recurring-subscription catalog type here. Do not emulate recurring charges or sell prohibited external/real-world benefits.

Start purchases from direct player action after capability checks. Restore/list owned permanent products and unconsumed purchases through the actual SDK. In researched plain JavaScript, consumePurchase takes the configured product ID, not an invented order token. Verify valuable purchases through the documented backend/platform route, bind product/order/user correctly, persist one durable benefit grant, then consume only consumables. Reconcile crashes and duplicate callbacks without awarding twice.

The documented verification endpoint is `POST https://playgama.com/api/bridge/v1/verify`, with platform, purchase type and returned purchase data. Its researched support is Playgama/MSN/Microsoft Store, not every Bridge destination. Use the actual other platform contract where needed.

Leaderboard tags are stable/unique and match SDK identifiers. Choose numeric/time and ascending/descending semantics deliberately. Display decimals do not turn integer score storage into arbitrary fractional storage. Respect actual score protection and player authorization. [Monetization/player detail](references/monetization-and-player-services.md) expands these checks.

## Upload, QA and publication states

Start archive upload with exact game/name/bytes, PUT the returned presigned contract exactly, then confirm and poll. Confirmation adds the archive and starts public QA-file processing. It does not publish the sandbox. URLs expire and are bound to exact size/type. Do not add unrelated account authorization headers to storage.

Distinguish processing DONE from a PASSED build check. PROBLEM, NOT_CHECKED, CHECKING or missing Bridge detection do not mean success. Use the real certification link, fix startup/integration and upload a corrected version. Opening a QA link does not unlock a failed build.

Upload covers through reserve → exact byte transfer → confirm. Save only intended form fields, preserving whole arrays. Re-read launch steps/application after each stage. UNKNOWN is unresolved, not green.

Read the intended archive's sandbox verdict. Current gates include passed checks, required covers/form/category, eligible Bridge version (researched minimum 2.2.0), game/status/quota/rate rules and actual allowed features. Publish only when eligible and authorized, then verify the live active revision and actual link.

Initial moderation is an owner console action. Get submission eligibility for the explicit archive and review type. Catalog availability can remain blocked by actual sandbox targets/cooldowns. Do not promise a filled form automatically unlocks review.

Before calling a build release-ready, complete the requirement matrix and regression report for that exact archive/hash. Mark unexecuted checks BLOCKED and explain NOT APPLICABLE entries. Provider build PASSED is not human moderation approval. For a rejected build, map every finding to a reproducible flow, fix its cause and retest adjacent flows against the replacement archive. Audio requires menu/focus/ad/reload combinations, shops require repeat and failed transactions, and startup requires actual host verification.

For an already live game, a catalog update affects all catalog players without moderation. The provider requires an explicit yes for that named game/build/update after explaining the effect. Previous update/sandbox consent does not satisfy it. Prepare concrete reviewed work before that final decision.

Traffic starts spend the relevant bonus/budget and cannot be undone. Read actual offer/eligibility and obtain the provider-required decision. Prepared share links do not authorize posting, and invented social links are invalid evidence. Referral acceptance requires the developer's actual supplied invitation and scope. [Publication detail](references/upload-qa-and-publication.md) preserves these distinctions.

## Observe actual player outcomes

Use bounded telemetry for a defined question, starting with overview/freshness/event inventory. Current ranges are at most 31 inclusive days. Use event distributions, timeseries and filtered session facts for their distinct meanings. Do not combine every page into an unauthorized raw-player export or interpret event counts as a complete individual history.

Compare equivalent build/audience windows and actual sample reach. Report a playable first loop, progress preservation, errors, ad behavior and purchase reconciliation rather than just total visits. Raph Koster's [A Theory of Fun for Game Design](https://www.theoryoffun.com/) is relevant professional further reading on learning/play, verified through the author site. It does not provide platform compliance or a retention formula.

Deliver source/archive/version/hash, completed [review evidence](assets/review-report.md), form/category/media, product checksum, player-service checks, QA/moderation/sandbox/catalog states and actual links. A failed mandatory check blocks a release-ready conclusion. A descriptive review does not certify an unexecuted game. [Telemetry detail](references/telemetry-and-operations.md), [official tools](https://wiki.playgama.com/playgama/mcp/tools), [Bridge requirements](https://wiki.playgama.com/playgama/bridge-sdk/api), [source notes](references/sources.md) and [license](LICENSE.md) provide focused support.
