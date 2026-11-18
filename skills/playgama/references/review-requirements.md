# Release and moderation requirements

Verified against the current official requirement pages on **2026-11-05**. Use this matrix for a complete review, including a corrected build returning from moderation. It is written guidance, not an executable test suite or an assertion that a game has passed.

## Authority and review method

The [requirements index](https://wiki.playgama.com/playgama/game-requirements) makes every numbered item mandatory. Apply engine-specific sections only to that engine. Evaluate additional destination requirements only for the actual distribution targets. Guides explain implementation and quality practices, with recommendations distinguished from hard requirements.

For an authorized release task, retrieve the live checklist and relevant engine/module documentation. Record the source dates, applicable IDs, exact archive/hash and real environments in the [review report](../assets/review-report.md). Use **PASSED**, **FAILED**, **BLOCKED** or **NOT APPLICABLE** per check. Missing execution evidence is BLOCKED. NOT APPLICABLE requires a reason, such as no video content or an unavailable optional payment feature. It cannot excuse universally required desktop support, audio or Bridge integration.

An automated archive verdict, eligibility response, sandbox publication and human moderation approval prove different things. Do not substitute one for another. The following rows paraphrase the requirements and add concrete ways to inspect them. The cited official pages govern wording and any subsequent changes.

## 1. Technical requirements

Source: [technical requirements](https://wiki.playgama.com/playgama/game-requirements/technical-requirements).

| IDs | Acceptance and useful evidence |
| --- | --- |
| 1.1.1–1.1.2 | Current supported Bridge and every required integration step. Record installed/exported versions, initialization owner, config and event trace. |
| 1.2.1–1.2.3 | No required external registration or automatic launch login. Supported optional login works, and rejection cannot freeze play. Exercise signed-out, cancel and error cases. |
| 1.2.4–1.2.5 | Required resources ship in the game, with the official SDK integration. Audit network requests for unrelated analytics, CDN dependencies and third-party services. |
| 1.2.6–1.2.7 | Gate outbound links on platform permission. No host/domain lock. Test denied links and legitimate alternate host/container loading. |
| 1.3.1–1.3.3 | Game files within 300 MB, root index and Latin paths, startup memory below 2 GB. Inspect extracted files and measure peak initialization memory. Check the separate upload ZIP cap too. |
| 1.4.1–1.4.6 | For claimed mobile support: fullscreen, usable keyboard inputs, declared orientation/rotation notice, complete touch controls, no browser long-press interference or unsupported-runtime warnings. Test actual mobile browsers. |
| 1.5.1–1.5.3 | Desktop is mandatory. Keyboard/mouse must complete play, and the game must not use Esc. Games claiming mobile also retain complete desktop controls. |
| 1.6.1–1.6.4 | Correct responsive proportions, visible boundaries, no outer-page scrolling, overlap or clipped information. Include narrow, wide and square viewports. |
| 1.6.5–1.6.8 | Closable dialogs, appropriate one-hand mobile interaction, readable text and usable 1:1 layout. Ordinary main scenes must not require panning. Large-world genre navigation is conditional. |
| 1.7.1–1.7.3 | No crashes, hangs or impossible progression. Cover long sessions, every level/path, resize, rotation, history, focus and ads on claimed systems with current major browsers. |
| 1.8.1–1.8.2 | If using video, keep playback inside the game with its own controls and archive-local files. No embedded external video player or departure from gameplay. |

## Required Bridge integration gates

The [required API steps](https://wiki.playgama.com/playgama/bridge-sdk/api) apply alongside the numbered requirements:

1. Export valid configuration beside root `index.html`, following the engine template's documented ownership.
2. Complete Bridge initialization before loading/starting the game and before any SDK calls. For plain JS, use the documented blocking head loader and initialization promise. Engine plugins can own the equivalent lifecycle.
3. Resolve localization from `platform.language` after initialization, with English available.
4. Load saved keys together through Bridge Storage before gameplay and batch meaningful changes when saving.
5. Apply the initial platform audio permission and handle later pause/audio events.
6. Send `game_ready` at the first usable interactive frame after loading screens, not at script import or halfway through asset loading.
7. Offer interstitials at natural gameplay pauses, allowing SDK scheduling to enforce actual display frequency.
8. Expose optional rewards, purchases, authorization, leaderboards and external links only when supported/allowed.

See [build and lifecycle implementation](build-and-bridge.md) for startup errors, environment detection, Godot setup, audio and persistence.

## 2. Advertising and payments

Source: [advertising and payment requirements](https://wiki.playgama.com/playgama/game-requirements/advertising-requirements).

| IDs | Acceptance and useful evidence |
| --- | --- |
| 2.1.1–2.1.2 | Use Bridge advertising and integrate interstitials where supported. No extra ad network, static third-party ad or replacement monetization SDK. |
| 2.1.3–2.1.5 | Display at logical pauses without interrupting active play, misleading pointer placement or wrong orientation. Inspect all direct calls, custom-message triggers and ad configuration. |
| 2.1.6–2.1.7 | Fullscreen ads pause sound and play. Close/error/no-fill restores the correct state without lost progress or a blocked screen. |
| 2.2.1–2.2.3 | Explicit opt-in names both the ad and exact optional benefit. Declining preserves ordinary play. Advertising cannot become a mandatory progression toll. |
| 2.2.4–2.2.5 | Recovery offers occur at most once per attempt. Grant the promised reward only on successful completion, never on cancel, close alone or failure. |
| 2.3.1–2.3.2 | Only supported Bridge sticky/advanced banners. Keep controls and gameplay visible, including after resize and safe-area changes. |
| 2.4.1–2.4.2 | Bridge-only payments, supported product configuration and real platform currency/prices. No external checkout or invented static localized price. |
| 2.4.3–2.4.4 | Successful payment precedes benefit delivery. Consume a consumable only after durable delivery. Failed or cancelled payment grants nothing. |
| 2.4.5–2.4.6 | Reconcile unprocessed purchases on launch. Restore permanent ownership every launch and prevent repurchase. Test crash/reload and duplicate delivery callbacks. |
| 2.5.1–2.5.2 | No prohibited cash-out, real-world/external benefits, subscriptions, gambling or lottery schemes. Review the entire product/economy design, not just catalog types. |

### First-session interstitial acceptance

Use a conservative game-owned placement policy: no show request in initialization, loading, `game_ready`, focus restoration or the first Start button before meaningful play. A button press alone does not make an opening-screen ad a natural break. Let the player enter the core loop, then offer an opportunity at a real completion, loss or appropriate return to menu. A Start handler that only starts play should not also request an ad.

Audit `advertisement.interstitial.autoShow` mappings and custom platform messages, because a message can trigger an ad without an explicit show call. Distinguish preload from show. Check the selected engine/SDK's actual configuration contract before changing any option.

The SDK owns frequency. The current interstitial page documents a configurable 60-second minimum by default. It is neither a universal first-ad deadline nor permission to interrupt play. Do not implement a second game timer or an arbitrary every-N-rounds/game-days counter as a substitute for the required opportunities. Partner/host-owned initial ad behavior must be distinguished from a game-triggered call and handled through the same pause/audio contract. See [monetization details](monetization-and-player-services.md).

## 3. User experience

Source: [user experience requirements](https://wiki.playgama.com/playgama/game-requirements/user-experience-requirements).

| IDs | Acceptance and useful evidence |
| --- | --- |
| 3.1.1 and 3.1.1.1–3.1.1.3 | Provide at least one meaningful progression, interactive-engagement or story basis. Demonstrate what changes and why the player continues. |
| 3.1.2–3.1.3 | Coherent setting/story, increasing challenge and practical onboarding. A first-time player can identify controls, objective and first action without a wall of text. |
| 3.2.1–3.2.3 | Bridge-only progress storage. Save levels/story or endless best score as relevant. Reload, rotation and advertisements must preserve progress. Inspect persistence calls and verify round trips in a real container. |
| 3.3.1–3.3.2 | Music plus appropriate action/interface effects from proper audio assets. Code-generated procedural tones are not accepted. Inspect asset rights, compression and playback. |
| 3.3.3–3.3.5 | Usable mute control, initial platform mute respected, silence while hidden and correct resume. Test menu/gameplay/pause, all audio channels, focus, ads and reload while already muted. |
| 3.4.1–3.4.2 | English available as default/fallback. Read language through Bridge rather than independent browser/OS/geolocation selection. |
| 3.4.3–3.4.4 | Translate every claimed language completely. If a language selector is provided, make it discoverable through recognizable language names/flags and universal navigation icons. |
| 3.5.1 | In-game title agrees with the submitted title. Compare the menu/loading UI with the saved form. |

### Gameplay and economy review

These concrete checks implement progression, functional controls and understandable UX. They are not invented numbered platform rules:

- Play an entire first loop without knowledge of the design. When actions require energy, action points, currency, cooldowns or a prior unlock, show the remaining resource and the unmet requirement next to the action. Explain the valid recovery step.
- Disabled actions need a visible reason. Enabled actions must work. A scene that looks like a dead end is a review risk even if an undocumented rule makes it technically intentional.
- Test every visible area, shop, item, upgrade, exit and return path. Remove unfinished controls from release or implement their advertised behavior. Do not label an empty feature functional.
- Buy an ordinary repeatable item twice, then after leaving/re-entering and reloading. Check both deductions and grants, inventory, refreshed affordability and release of in-flight locks after success/cancel/error. A valid first purchase does not prove the second works.
- Separate repeatable consumables from permanent ownership, daily limits, stock and eligibility. Permanent products must not become repurchasable merely to make a repeat-purchase test pass. Legitimate limits require clear feedback.
- Replay after failure/completion and perform multiple cycles. Check timers, listener duplication, stale UI, scene transitions and progression softlocks.

## 4. Content, rights and data

Source: [content requirements](https://wiki.playgama.com/playgama/game-requirements/content-requirements).

| IDs | Acceptance and useful evidence |
| --- | --- |
| 4.1.1–4.1.5 | Exclude realistic abusive violence, political/war content, religious subject matter, life/health/death predictions and sexual/erotic content covered by the rules. Inspect all scenes, text and marketing. |
| 4.1.6–4.1.10 | Exclude hatred/discrimination, profanity, self-harm encouragement/instructions, misleading illegal advice/crime promotion and extremist/unlawful content. Review user-facing assets as well as mechanics. |
| 4.2.1–4.2.2 | Hold distribution rights and avoid duplicate catalog entries. A superficial reskin is not a qualifying new sequel. Prefer updating the existing game when the design is substantially the same. |
| 4.2.3–4.2.5 | Clear copyright/trademark permissions. No unauthorized characters/music, official-brand impersonation or unrelated brand traffic bait in game/title/artwork. |
| 4.3.1–4.3.2 | Meaningful human refinement of AI-assisted output. No low-quality generated template or emoji substituted for purpose-designed UI icons. AI assistance itself is not a blanket ban. |
| 4.4.1 | Explicit permission for applicable personal-data actions and required legal notices. Minimize diagnostic data and document actual collection. |

## 5. Engine and destination requirements

Source: [engine-specific requirements](https://wiki.playgama.com/playgama/game-requirements/engine-specific-requirements).

**5.1.1 applies to Unity:** enable the named **Decompression Fallback** setting in WebGL build settings. This is an official engine build option, not an excuse for silent application error handling. Verify the current rule and actual hosting/compression behavior together. Do not adopt the opposite setting from stale search results.

Read the [partner-specific page](https://wiki.playgama.com/playgama/game-requirements/platform-specific-requirements) for each intended destination. It mixes hard constraints, quality recommendations and distribution availability. Record their different strengths instead of declaring every recommendation a universal gate.

| Destination | Additional scope to check from the current page |
| --- | --- |
| Facebook | No very-early ads or references to other apps/sites. Web/iOS/Android compatibility and at least two of IAP, leaderboards, multiplayer and social sharing. Build up to 200 MB and 500 files. Unity Brotli/Gzip. Clear CTA, personalization/replay and high-quality audiovisuals. Loading below 3 seconds is a preference. |
| MSN | Build below 50 MB, landscape or both orientations. Distribution is selective. |
| CrazyGames | Unique polished play for 13+, over 20 minutes of engaging content, loading within 5 seconds, onboarding and no landscape sidebars. Playgama currently does not publish there. SDK support alone does not create a publishing route. |
| Playhop / Yandex | Russian localization and more than 10 minutes of engaging content. |
| GameDistribution | Clear onboarding, engaging replay and consistent polished graphics. Self-contained hosting, no outbound links/analytics/social redirects, violence or explicit blood. Real-time multiplayer has a hosting exception. |
| VK | Russian/default localization, mobile safe areas, polished UI and over 10 minutes of play. Energy/lives regenerate, with a full balance and no progress for a new player. Optional social actions cannot gate play. Playgama currently does not publish there. |
| Discord | IAP and multiplayer requirements for that destination. |
| Xiaomi | Android, build up to 100 MB, loading below 15 seconds and average playtime at least 5 minutes. |
| YouTube Playables | Initial payload up to 30 MB, all device types and both adapted orientations without sidebars. No external calls including built-in analytics, no copied/low-value wholly generated content. Filenames only letters/digits/dot/hyphen/underscore, no spaces, up to 8,000 files. Average playtime over 8 minutes is an ideal. Selection is not guaranteed. |
| TikTok | iOS/Android portrait, game up to 30 MB, average playtime at least 10 minutes and no external calls including built-in analytics. Home Screen Shortcut and Sidebar integration expected. Publishing is currently paused. |
| GameSnacks | Every file below 10 MiB, game up to 100 MiB, initial payload below 15 MiB and saves below 3 MiB, preferably below 500 KiB. iOS/Android and 9:16 portrait. Playable below 15 seconds at at least 10 Mbps. No external calls including built-in analytics. Final selection rests with the partner. |

Do not confuse MB with MiB, initial payload with whole archive, or a selected destination's limits with general limits. Resolve per-destination analytics restrictions through the actual supported adapter/configuration. Do not invent a config key or silently retain forbidden calls. Recheck availability for the real task.

## Final review and correction cycle

Record evidence for every applicable row and the [official common-failure self-check](https://wiki.playgama.com/playgama/game-requirements/game-self-check). Include representative browsers/devices and exact test sequences, not just a recording of an unidentifiable build.

For each moderation comment, map it to the relevant requirement and reproducible flow, fix the underlying state transition, rebuild and retest related cases. An audio fix requires muted/unmuted startup, ad and focus combinations. A shop fix requires repeat purchases and terminal error paths. A startup fix requires both local and real-container checks. Close a finding only against the new archive actually being submitted.

Deliver a completed report with unresolved failures and handoffs. A failed mandatory check blocks a release-ready conclusion. Unavailable platform testing remains BLOCKED even if the source looks correct. Actual moderation acceptance remains the platform's decision.
