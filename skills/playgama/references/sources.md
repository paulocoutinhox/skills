# Sources and capability limits

Checked baseline: **2026-11-05**. For the operation you are running, the live MCP schemas and the current game requirements are the source of truth.

| Source | Use |
| --- | --- |
| [Official MCP connection](https://wiki.playgama.com/playgama/mcp) | Endpoint, client connection and organization access |
| [Complete tools reference](https://wiki.playgama.com/playgama/mcp/tools) | All 37 management tools checked, with parameters, effects, refusals and consent rules |
| [Documentation index](https://wiki.playgama.com/playgama/llms.txt) | Finding current pages and modules |
| [Submitting a game](https://wiki.playgama.com/playgama/submitting-a-game) | Form meaning and moderation workflow |
| [Requirements index](https://wiki.playgama.com/playgama/game-requirements) | Mandatory numbered rules and the engine and destination rules that apply only in some cases |
| [Technical requirements](https://wiki.playgama.com/playgama/game-requirements/technical-requirements) | Archive, memory, controls, devices and runtime limits |
| [Advertising and payment requirements](https://wiki.playgama.com/playgama/game-requirements/advertising-requirements) | Supported monetization and banned real-world benefits |
| [User experience requirements](https://wiki.playgama.com/playgama/game-requirements/user-experience-requirements) | Progress, Bridge-only saves, required audio and mute, localization and title |
| [Content requirements](https://wiki.playgama.com/playgama/game-requirements/content-requirements) | Banned content, copyright, originality, quality of AI-assisted work and data permissions |
| [Engine-specific requirements](https://wiki.playgama.com/playgama/game-requirements/engine-specific-requirements) | Current Unity WebGL Decompression Fallback requirement 5.1.1 |
| [Destination-specific requirements](https://wiki.playgama.com/playgama/game-requirements/platform-specific-requirements) | Partner limits, recommendations and where publishing is really available |
| [Common-failure self-check](https://wiki.playgama.com/playgama/game-requirements/game-self-check) | Common moderation failures linked to numbered requirements |
| [Bridge API required steps](https://wiki.playgama.com/playgama/bridge-sdk/api) | Required initialization, config, storage, audio and pause, ready, ads and capabilities |
| [Current setup](https://wiki.playgama.com/playgama/bridge-sdk/setup) | Unified SDK setup, environment detection and which engine or plugin owns what |
| [Bridge config](https://wiki.playgama.com/playgama/bridge-sdk/config) | Where exported config goes and current adapter-specific settings |
| [Platform API](https://wiki.playgama.com/playgama/bridge-sdk/api/platform) | Starting audio permission, pause and audio events, exact ready message, language and ads triggered by messages |
| [Storage API](https://wiki.playgama.com/playgama/bridge-sdk/api/storage) | Batch get and set for each binding, completion and error contracts and available backends |
| [Player API](https://wiki.playgama.com/playgama/bridge-sdk/api/player) | Optional sign-in and the real callbacks for each binding |
| [Interstitial API](https://wiki.playgama.com/playgama/bridge-sdk/api/advertisement/interstitial) | Natural breaks, support, state, preload and the configurable timing default |
| [Rewarded API](https://wiki.playgama.com/playgama/bridge-sdk/api/advertisement/rewarded) | Grants only on rewarded, placement and state handling |
| [Bridge payments](https://wiki.playgama.com/playgama/bridge-sdk/api/payments) | Purchase, consume and restore, product config, support table and verification endpoint |
| [Sound guide](https://wiki.playgama.com/playgama/guides/game-development/sound) | One shared audio owner, menu and pause mute, autoplay and iOS context handling |
| [Saving progress guide](https://wiki.playgama.com/playgama/guides/game-development/saving-progress) | Important state, fixed keys, when to write and save checks |

The tool map describes the public management features that were checked. It is not a full nested runtime contract. Real tool schemas and official behavior guidance decide authorized operations. No generated catalog or refresh program is included.

The sources checked cover MCP management, presigned byte uploads, Bridge SDK APIs, and a documented purchase-verification endpoint. They do not document a general publishing REST API or first-party CLI, a recurring subscription catalog type, first moderation submission through MCP, moderation replies, leaderboard deletion through MCP, or general screenshot or video form uploads. Use explicit console handoffs for those unsupported management tasks, and check current features again before deciding a gap still exists.

The requirement groups, the self-check, the current setup and configuration, and the relevant platform, storage and advertising pages were read for this review. When a normal page could not be opened through one reader, its official Markdown version was read directly. Agents doing real work can get live engine-specific documentation with `get_bridge_sdk_docs` and live requirements with `get_game_checklist`. Category guidance and telemetry instructions come from the server and should be fetched live rather than copied as a fixed category list or model.

## Interpretation and conflict boundaries

- The current unified Bridge SDK pages decide current work. Do not move old engine-path examples or search snippets into a different installed binding. Check the real chosen plugin and export template.
- Required initialization finishes before the game starts. A responsive loading screen, handled rejections and clear retry or error states fit that order. Going on with APIs that are not initialized, or pretending production initialized in mock, is not a valid fix.
- A local mock chosen by the SDK and optional guest login are documented features. They do not prove real-container integration, a universal QA adapter ID or cloud saves on every destination.
- Progress uses the current Storage module. Bridge chooses the available backend. Mentions of a different module in another engine or version do not override this contract or justify saving directly in the browser.
- Current engine rule 5.1.1 turns on Unity's named Decompression Fallback option. Check the live numbered rule and the real target hosting contract, and resolve any real target conflict before claiming the game is ready.
- A natural-break ad opportunity and SDK frequency scheduling are separate decisions. The review matrix explains the careful rule of no opening ad requested by the game. The documented 60-second configurable minimum is not a deadline for the first ad, and advertising the host manages is not the same as an application show call.
- The saving guide covers defaults for new players and save structure. A transport failure does not prove a save is missing. The skill's protection against overwriting unknown progress is an engineering safeguard, not an invented promise of transactional or cross-device storage.
- A language selector is optional. If one is supplied, the numbered rule about making it easy to find applies. English support and complete declared translations are mandatory either way.
- Partner guidance mixes hard limits, quality recommendations and publishing routes that are not available. SDK adapter support does not mean distribution is available. Handle partner bans on external calls and analytics without inventing unsupported settings.
- Repeat-purchase, late-callback, write-order and overlapping-pause scenarios are engineering acceptance checks that support working gameplay. They are not extra official numbered rules, and they do not claim the game was really run.

The matrix restates the requirements in other words and adds guidance on building and evidence. It is not an official certification or a replacement for a current moderation decision.

## Professional foundation and evidence scope

Reviewed on 2026-11-05. Raph Koster's [A Theory of Fun for Game Design](https://www.theoryoffun.com/) is professional further reading, checked through the author's site and excerpt index. It helps with questions about a core loop that is playable and easy to learn, not with platform certification or a numeric retention promise. The real Playgama requirements and tool contracts decide publication.

Stored content is updated only when the user asks for a revision. There is no automatic source collector or refresh process.

## Recheck on 2026-11-18

The [complete tools reference](https://wiki.playgama.com/playgama/mcp/tools) was read again. It still lists the same 37 tools, a title up to 120 Latin-script characters with a Latin letter, a description and how-to-play minimum of 100 characters at submission, an English story of 150–900 characters without links, `IOS`/`ANDROID`/`DESKTOP` devices, 800×800, 1080×1920 and 1920×1080 PNG/JPEG covers up to 10 MB, a 300 MB archive with a name up to 200 characters, presigned URLs that last one hour, a Bridge 2.2.0 minimum for sandbox, a 31-day telemetry range and no MCP moderation submission or reply. It documents optional `agent`, `model` and `modelId` fields on `create_application` and `update_application_form`, with `agent: none` for games made without an agent. The page does not say whether these fields are shown publicly.

The rule for player-facing copy (no description of how it was made and no AI or tool mentions in title, description, how-to-play, story or covers, with agent and model facts kept in their declaration fields) is an owner content rule, not a Playgama requirement.

The [destination-specific requirements](https://wiki.playgama.com/playgama/game-requirements/platform-specific-requirements) were read again on 2026-11-18. Every limit and availability statement in the destination table matched: Facebook 200 MB/500 files, MSN below 50 MB, CrazyGames and VK not published by Playgama, Xiaomi 100 MB/15 seconds/5 minutes, YouTube Playables 30 MB initial build/8,000 files, TikTok 30 MB with publishing paused and GameSnacks 10 MiB per file, 100 MiB total, 15 MiB initial download and 3 MiB saves. The [technical requirements](https://wiki.playgama.com/playgama/game-requirements/technical-requirements) still state 300 MB, root `index.html`, Latin names, a startup peak below 2 GB, mandatory desktop play and no Esc key.

## Recheck on 2026-11-23

The [official MCP page](https://wiki.playgama.com/playgama/mcp.md) was read again. It says there is no token to create, that the client finds the sign-in from the endpoint and opens the console consent page, and it gives the setup commands for each client, the 10-minute consent request, one-hour access that the client renews, reconnection after 30 unused days, and revocation on the console MCP page. The [protected resource metadata](https://developer.playgama.com/.well-known/oauth-protected-resource) and [authorization server metadata](https://developer.playgama.com/.well-known/oauth-authorization-server) were read directly. They give the registration, authorization, token and revocation endpoints, scope `mcp`, PKCE `S256` and public clients without a secret.

A real first launch of an HTML5 game through the MCP on 2026-11-23 confirmed: the `create_application` engine values, the `GAME_NOT_READY` build-check reason, `PENDING` answers of `publish_sandbox`, the `MODERATION_UNAVAILABLE` answer for a new draft, the launch-step reason `NO_CERTIFICATION` pointing to `get_archive_qa_tool_link`, and cover slot tags `icon`, `preview_vertical` and `preview`. The live requirement pages read through `get_game_checklist` on that date matched the technical, advertising, user experience and content items recorded here, including no Esc key (1.5.2), a tutorial or onboarding (3.1.3), Bridge-only saves (3.2.1) and the in-game title matching the form (3.5.1).

The cover art standard (illustrated key art with the official logo placed over art with no text, never a screenshot or a UI capture) is an owner quality rule, not a Playgama requirement.
