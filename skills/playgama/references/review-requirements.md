# Release and moderation requirements

Checked against the current official requirement pages on **2026-11-05**. Use this matrix for a full review, including a fixed build coming back from moderation. It is written guidance. It is not a test suite you can run, and it does not claim that a game has passed.

## Authority and review method

The [requirements index](https://wiki.playgama.com/playgama/game-requirements) makes every numbered item mandatory. Apply engine-specific sections only to that engine. Check extra destination requirements only for the real distribution targets. Guides explain how to build things and good quality practices, and they mark recommendations apart from hard requirements.

For an authorized release task, get the live checklist and the relevant engine and module documentation. Record the source dates, the IDs that apply, the exact archive and hash and the real environments in the [review report](../assets/review-report.md). Use **PASSED**, **FAILED**, **BLOCKED** or **NOT APPLICABLE** for each check. A check with no evidence that it ran is BLOCKED. NOT APPLICABLE needs a reason, such as no video content or an optional payment feature that is not available. It cannot excuse desktop support, audio or Bridge integration, which are always required.

An automatic archive verdict, an eligibility response, a sandbox publication and human moderation approval prove different things. Do not use one in place of another. The rows below restate the requirements in other words and add concrete ways to check them. The cited official pages decide the exact wording and any later changes.

## 1. Technical requirements

Source: [technical requirements](https://wiki.playgama.com/playgama/game-requirements/technical-requirements).

| IDs | Acceptance and useful evidence |
| --- | --- |
| 1.1.1–1.1.2 | Current supported Bridge and every required integration step. Record installed and exported versions, who owns initialization, config and an event trace. |
| 1.2.1–1.2.3 | No required external sign-up or automatic login at launch. Supported optional login works, and saying no cannot freeze play. Test signed-out, cancel and error cases. |
| 1.2.4–1.2.5 | Required resources ship inside the game, with the official SDK integration. Check network requests for unrelated analytics, CDN dependencies and third-party services. |
| 1.2.6–1.2.7 | Allow outbound links only with platform permission. No host or domain lock. Test denied links and loading from a different valid host or container. |
| 1.3.1–1.3.3 | Game files within 300 MB, root index and Latin paths, startup memory below 2 GB. Check the unpacked files and measure peak memory during startup. Also check the separate upload ZIP cap. |
| 1.4.1–1.4.6 | For claimed mobile support: fullscreen, usable keyboard inputs, declared orientation and a rotation notice, complete touch controls, no browser long-press problems and no warnings about unsupported runtimes. Test real mobile browsers. |
| 1.5.1–1.5.3 | Desktop is mandatory. Keyboard and mouse must be enough to play to the end, and the game must not use Esc. Games that claim mobile still keep complete desktop controls. Engines whose UI uses Escape as the cancel or back key need that binding removed in the web build only, so native builds keep Escape and TV or Android back buttons. |
| 1.6.1–1.6.4 | Correct proportions on every screen size, visible edges, no scrolling of the outer page, no overlap or cut-off information. Include narrow, wide and square viewports. |
| 1.6.5–1.6.8 | Dialogs that can be closed, mobile use that works with one hand where suitable, readable text and a usable 1:1 layout. Normal main scenes must not need panning. Navigation in large-world genres depends on the case. |
| 1.7.1–1.7.3 | No crashes, freezes or progress that cannot continue. Cover long sessions, every level and path, resizing, rotation, history, focus and ads on the claimed systems with current major browsers. |
| 1.8.1–1.8.2 | If you use video, keep playback inside the game with its own controls and files stored in the archive. No embedded external video player and no leaving the gameplay. |

## Required Bridge integration gates

The [required API steps](https://wiki.playgama.com/playgama/bridge-sdk/api) apply together with the numbered requirements:

1. Export a valid configuration next to the root `index.html`, following who owns it in the engine template's documentation.
2. Finish Bridge initialization before loading or starting the game and before any SDK calls. For plain JS, use the documented blocking head loader and initialization promise. Engine plugins can own the same lifecycle.
3. Choose the localization from `platform.language` after initialization, with English available.
4. Load saved keys together through Bridge Storage before gameplay, and save important changes in batches.
5. Apply the starting platform audio permission and handle later pause and audio events.
6. Send `game_ready` at the first usable interactive frame after loading screens, not when the script is imported or halfway through asset loading.
7. Offer interstitials at natural pauses in gameplay, and let SDK scheduling decide how often they really show.
8. Show optional rewards, purchases, sign-in, leaderboards and external links only when they are supported or allowed.

See [build and lifecycle implementation](build-and-bridge.md) for startup errors, environment detection, Godot setup, audio and saving.

## 2. Advertising and payments

Source: [advertising and payment requirements](https://wiki.playgama.com/playgama/game-requirements/advertising-requirements).

| IDs | Acceptance and useful evidence |
| --- | --- |
| 2.1.1–2.1.2 | Use Bridge advertising and add interstitials where supported. No extra ad network, static third-party ad or replacement monetization SDK. |
| 2.1.3–2.1.5 | Show at logical pauses without interrupting active play, with no misleading pointer placement or wrong orientation. Check all direct calls, custom-message triggers and ad settings. |
| 2.1.6–2.1.7 | Fullscreen ads pause sound and play. Close, error or no-fill restores the right state without lost progress or a blocked screen. |
| 2.2.1–2.2.3 | A clear opt-in names both the ad and the exact optional benefit. Saying no keeps normal play. Ads cannot become a required toll for progress. |
| 2.2.4–2.2.5 | Recovery offers happen at most once per attempt. Grant the promised reward only on successful completion, never on cancel, close alone or failure. |
| 2.3.1–2.3.2 | Only supported Bridge sticky and advanced banners. Keep controls and gameplay visible, including after resizing and safe-area changes. |
| 2.4.1–2.4.2 | Payments only through Bridge, supported product setup and real platform currency and prices. No external checkout and no made-up fixed local price. |
| 2.4.3–2.4.4 | A successful payment comes before the benefit is given. Consume a consumable only after delivery is saved. A failed or cancelled payment grants nothing. |
| 2.4.5–2.4.6 | Finish unprocessed purchases on launch. Restore permanent ownership on every launch and block a second purchase. Test crash and reload and duplicate delivery callbacks. |
| 2.5.1–2.5.2 | No banned cash-out, real-world or external benefits, subscriptions, gambling or lottery schemes. Review the whole product and economy design, not just catalog types. |

### First-session interstitial acceptance

Use a careful placement policy for ads the game requests: no show request in initialization, loading, `game_ready`, the return of focus or the first Start button before real play. A button press alone does not make an ad on the opening screen a natural break. Let the player enter the core loop, then offer an opportunity at a real finish, loss or suitable return to the menu. A Start handler that only starts play should not also request an ad.

Check `advertisement.interstitial.autoShow` mappings and custom platform messages, because a message can trigger an ad without a direct show call. Tell preload apart from show. Check the chosen engine and SDK's real configuration contract before changing any option.

The SDK owns how often ads show. The current interstitial page documents a configurable 60-second minimum by default. It is not a universal deadline for the first ad, and it does not allow interrupting play. Do not build a second game timer or an arbitrary every-N-rounds or game-days counter in place of the required opportunities. Opening ad behavior owned by the partner or host must be told apart from a call the game triggers, and handled through the same pause and audio rules. See [monetization details](monetization-and-player-services.md).

## 3. User experience

Source: [user experience requirements](https://wiki.playgama.com/playgama/game-requirements/user-experience-requirements).

| IDs | Acceptance and useful evidence |
| --- | --- |
| 3.1.1 and 3.1.1.1–3.1.1.3 | Provide at least one real basis for play: progress, interactive engagement or story. Show what changes and why the player keeps going. |
| 3.1.2–3.1.3 | A setting and story that make sense, rising challenge and practical onboarding. A first-time player can find the controls, goal and first action without a wall of text. |
| 3.2.1–3.2.3 | Progress saved only through Bridge. Save levels or story, or the endless best score, as relevant. Reload, rotation and ads must keep progress. Check the save calls and confirm round trips in a real container. Also list what the runtime itself creates in the browser: some engine runtimes mount an IndexedDB file system or cache their content in the origin private file system even when the game saves nothing there. Record it as a moderation risk, with the evidence that progress goes only through the Bridge. |
| 3.3.1–3.3.2 | Music plus suitable action and interface effects from proper audio files. Tones generated in code are not accepted. Check audio rights, compression and playback. |
| 3.3.3–3.3.5 | A usable mute control, the starting platform mute respected, silence while hidden and correct resume. Test menu, gameplay and pause, all audio channels, focus, ads and reload while already muted. |
| 3.4.1–3.4.2 | English available as the default and fallback language. Read the language through Bridge rather than choosing it on your own from the browser, OS or location. |
| 3.4.3–3.4.4 | Translate every claimed language completely. If you provide a language selector, make it easy to find with recognizable language names or flags and universal navigation icons. |
| 3.5.1 | The title in the game matches the submitted title. Compare the menu and loading UI with the saved form. Store-search words added to the name in other stores do not belong in this title unless the game shows them. |

### Gameplay and economy review

These concrete checks put progress, working controls and clear UX into practice. They are not invented numbered platform rules:

- Play a whole first loop without knowing the design. When actions need energy, action points, currency, cooldowns or an earlier unlock, show the remaining resource and the unmet requirement next to the action. Explain the valid way to recover.
- Disabled actions need a visible reason. Enabled actions must work. A scene that looks like a dead end is a review risk, even if an undocumented rule makes it technically intended.
- Test every visible area, shop, item, upgrade, exit and way back. Remove unfinished controls from the release or make them do what they advertise. Do not call an empty feature working.
- Buy a normal repeatable item twice, then again after leaving and re-entering and after reloading. Check both deductions and grants, the inventory, the refreshed affordability and that in-progress locks clear after success, cancel and error. A valid first purchase does not prove the second one works.
- Keep repeatable consumables apart from permanent ownership, daily limits, stock and eligibility. Permanent products must not become buyable again just to make a repeat-purchase test pass. Real limits need clear feedback.
- Play again after failure and after finishing, and run several cycles. Check timers, duplicate listeners, outdated UI, scene changes and progress dead ends (softlocks).

## 4. Content, rights and data

Source: [content requirements](https://wiki.playgama.com/playgama/game-requirements/content-requirements).

| IDs | Acceptance and useful evidence |
| --- | --- |
| 4.1.1–4.1.5 | Leave out realistic abusive violence, political or war content, religious subjects, predictions about life, health or death, and sexual or erotic content covered by the rules. Check all scenes, text and marketing. |
| 4.1.6–4.1.10 | Leave out hatred or discrimination, profanity, encouraging or explaining self-harm, misleading illegal advice or promoting crime, and extremist or unlawful content. Review the assets players see as well as the mechanics. |
| 4.2.1–4.2.2 | Hold distribution rights and avoid duplicate catalog entries. A shallow reskin is not a real new sequel. Prefer updating the existing game when the design is mostly the same. |
| 4.2.3–4.2.5 | Clear copyright and trademark permissions. No unauthorized characters or music, no posing as an official brand and no unrelated brand names used as traffic bait in the game, title or art. |
| 4.3.1–4.3.2 | Real human improvement of AI-assisted output. No low-quality generated template and no emoji in place of UI icons designed for the game. AI help itself is not banned outright. |
| 4.4.1 | Explicit permission for the personal-data actions that apply and the required legal notices. Collect as little diagnostic data as possible and document what you really collect. |

## 5. Engine and destination requirements

Source: [engine-specific requirements](https://wiki.playgama.com/playgama/game-requirements/engine-specific-requirements).

**5.1.1 applies to Unity:** turn on the named **Decompression Fallback** setting in WebGL build settings. This is an official engine build option, not an excuse for hiding application errors. Check the current rule and the real hosting and compression behavior together. Do not use the opposite setting because of outdated search results.

Read the [partner-specific page](https://wiki.playgama.com/playgama/game-requirements/platform-specific-requirements) for each destination you plan to use. It mixes hard limits, quality recommendations and where publishing is available. Record how strong each one is instead of treating every recommendation as a universal gate.

| Destination | Additional scope to check from the current page |
| --- | --- |
| Facebook | No very early ads or mentions of other apps or sites. Web, iOS and Android support and at least two of IAP, leaderboards, multiplayer and social sharing. Build up to 200 MB and 500 files. Unity Brotli/Gzip. Clear call to action (CTA), personalization and replay, and high-quality sound and visuals. Loading below 3 seconds is a preference. |
| MSN | Build below 50 MB, landscape or both orientations. Distribution is selective. |
| CrazyGames | Unique, polished play for ages 13+, over 20 minutes of engaging content, loading within 5 seconds, onboarding and no landscape sidebars. Playgama currently does not publish there. SDK support alone does not create a way to publish. |
| Playhop / Yandex | Russian localization and more than 10 minutes of engaging content. |
| GameDistribution | Clear onboarding, engaging replay and consistent, polished graphics. Self-contained hosting, no outbound links, analytics or social redirects, no violence or explicit blood. Real-time multiplayer has a hosting exception. |
| VK | Russian as the default localization, mobile safe areas, polished UI and over 10 minutes of play. Energy and lives refill, with a full balance and no progress for a new player. Optional social actions cannot block play. Playgama currently does not publish there. |
| Discord | IAP and multiplayer requirements for that destination. |
| Xiaomi | Android, build up to 100 MB, loading below 15 seconds and average playtime of at least 5 minutes. |
| YouTube Playables | First download up to 30 MB, all device types and both orientations adapted without sidebars. No external calls, including built-in analytics, and no copied or low-value fully generated content. Filenames only letters, digits, dot, hyphen and underscore, no spaces, up to 8,000 files. Average playtime over 8 minutes is the ideal. Selection is not guaranteed. |
| TikTok | iOS and Android portrait, game up to 30 MB, average playtime of at least 10 minutes and no external calls, including built-in analytics. Home Screen Shortcut and Sidebar integration expected. Publishing is currently paused. |
| GameSnacks | Every file below 10 MiB, game up to 100 MiB, first download below 15 MiB and saves below 3 MiB, ideally below 500 KiB. iOS and Android and 9:16 portrait. Playable in less than 15 seconds at 10 Mbps or faster. No external calls, including built-in analytics. The partner makes the final selection. |

Do not mix up MB and MiB, the first download and the whole archive, or one destination's limits and the general limits. Handle each destination's analytics limits through the real supported adapter or configuration. Do not invent a config key or quietly keep banned calls. Check availability again for the real task.

## Final review and correction cycle

Record evidence for every row that applies and for the [official common-failure self-check](https://wiki.playgama.com/playgama/game-requirements/game-self-check). Include typical browsers and devices and exact test steps, not just a recording of a build nobody can identify.

For each moderation comment, link it to the related requirement and a flow you can reproduce, fix the state change behind it, rebuild and retest related cases. An audio fix needs muted and unmuted startup, ad and focus combinations. A shop fix needs repeat purchases and final error paths. A startup fix needs both local and real-container checks. Close a finding only against the new archive that is really being submitted.

Deliver a completed report with unresolved failures and handoffs. A failed mandatory check blocks a ready-for-release conclusion. Platform testing that was not available stays BLOCKED, even if the source looks right. Real moderation acceptance is still the platform's decision.
