# Sources and capability limits

Verified baseline: **2026-11-05**. Live MCP schemas and current game requirements are authoritative for the operation being executed.

| Source | Use |
| --- | --- |
| [Official MCP connection](https://wiki.playgama.com/playgama/mcp) | Endpoint, client connection and organization access |
| [Complete tools reference](https://wiki.playgama.com/playgama/mcp/tools) | All 37 researched management tools, parameters, effects, refusals and consent rules |
| [Documentation index](https://wiki.playgama.com/playgama/llms.txt) | Current page/module discovery |
| [Submitting a game](https://wiki.playgama.com/playgama/submitting-a-game) | Form semantics and moderation workflow |
| [Requirements index](https://wiki.playgama.com/playgama/game-requirements) | Mandatory numbered rules and conditional engine/destination scope |
| [Technical requirements](https://wiki.playgama.com/playgama/game-requirements/technical-requirements) | Archive, memory, controls, devices and runtime constraints |
| [Advertising and payment requirements](https://wiki.playgama.com/playgama/game-requirements/advertising-requirements) | Supported monetization and prohibited real-world benefits |
| [User experience requirements](https://wiki.playgama.com/playgama/game-requirements/user-experience-requirements) | Progression, Bridge-only saves, required audio/mute, localization and title |
| [Content requirements](https://wiki.playgama.com/playgama/game-requirements/content-requirements) | Prohibited content, copyright, originality, AI-assisted quality and data permissions |
| [Engine-specific requirements](https://wiki.playgama.com/playgama/game-requirements/engine-specific-requirements) | Current Unity WebGL Decompression Fallback requirement 5.1.1 |
| [Destination-specific requirements](https://wiki.playgama.com/playgama/game-requirements/platform-specific-requirements) | Partner constraints, recommendations and actual publishing availability |
| [Common-failure self-check](https://wiki.playgama.com/playgama/game-requirements/game-self-check) | Frequent moderation failures mapped to numbered requirements |
| [Bridge API required steps](https://wiki.playgama.com/playgama/bridge-sdk/api) | Required initialization, config, storage, audio/pause, ready, ads and capabilities |
| [Current setup](https://wiki.playgama.com/playgama/bridge-sdk/setup) | Unified SDK setup, environment detection and supported engine/plugin ownership |
| [Bridge config](https://wiki.playgama.com/playgama/bridge-sdk/config) | Exported config locations and current adapter-specific configuration |
| [Platform API](https://wiki.playgama.com/playgama/bridge-sdk/api/platform) | Initial audio permission, pause/audio events, exact ready message, language and message-triggered ads |
| [Storage API](https://wiki.playgama.com/playgama/bridge-sdk/api/storage) | Binding-specific batch get/set, completion/error contracts and available backends |
| [Player API](https://wiki.playgama.com/playgama/bridge-sdk/api/player) | Optional authorization and actual binding-specific callbacks |
| [Interstitial API](https://wiki.playgama.com/playgama/bridge-sdk/api/advertisement/interstitial) | Natural breaks, support, state, preload and configurable timing default |
| [Rewarded API](https://wiki.playgama.com/playgama/bridge-sdk/api/advertisement/rewarded) | Rewarded-only grants, placement and state handling |
| [Bridge payments](https://wiki.playgama.com/playgama/bridge-sdk/api/payments) | Purchase/consume/restore, product config, support matrix and verification endpoint |
| [Sound guide](https://wiki.playgama.com/playgama/guides/game-development/sound) | Shared audio owner, menu/pause mute, autoplay and iOS context handling |
| [Saving progress guide](https://wiki.playgama.com/playgama/guides/game-development/saving-progress) | Meaningful state, fixed keys, write timing and persistence checks |

The descriptive tool map records the researched public management capabilities. It is not a full nested runtime contract. Real tool schemas and official behavioral guidance govern authorized operations. No generated catalog or refresh program is bundled.

The researched sources expose MCP management, presigned byte uploads, Bridge SDK APIs, and a documented purchase-verification endpoint. They do not document a general publishing REST API or first-party CLI, a recurring subscription catalog type, initial moderation submission through MCP, moderation replies, leaderboard deletion through MCP, or generic screenshot/video form uploads. Use explicit console handoffs for those unsupported management surfaces and recheck current capabilities before concluding a gap still exists.

The requirement families, self-check, current setup/configuration and relevant platform/storage/advertising bodies were inspected for this review. When a regular page was inaccessible through one reader, its official Markdown representation was read directly. Operational agents can obtain live engine-specific documentation with `get_bridge_sdk_docs` and live requirements with `get_game_checklist`. Category guidance and telemetry instructions are server-returned content and should be retrieved live rather than copied as a permanent taxonomy/model.

## Interpretation and conflict boundaries

- The current unified Bridge SDK pages govern current work. Do not transplant old engine-path examples or search snippets into a different installed binding. Verify the actual selected plugin and export template.
- Required initialization completes before the game starts. Responsive loading, handled rejection and explicit retry/error states are compatible with that order. Continuing with uninitialized APIs or pretending production initialized in mock is not a compliant repair.
- SDK-selected local mock and optional guest login behavior are documented capabilities. They do not prove real-container integration, a universal QA adapter ID or cloud persistence on every destination.
- Progress uses the current Storage module. Bridge chooses the available backend. References to a different module in another engine/version do not override this contract or justify direct browser saves.
- Current engine rule 5.1.1 explicitly enables Unity's named Decompression Fallback option. Older indexed guidance can say the opposite. Check the live numbered rule and the actual target hosting contract, and resolve an actual target conflict before claiming readiness.
- A natural-break ad opportunity and SDK frequency scheduling are separate decisions. The conservative no-game-owned-opening-ad acceptance profile is explained in the review matrix. The documented 60-second configurable minimum is not a first-ad deadline, and host-managed advertising is not the same as an application show call.
- The saving guide discusses new-player defaults and save structure. A transport failure is not proof of a missing save. The skill's protection against overwriting unknown progress is an engineering safeguard, not an invented guarantee of transactional or cross-device storage.
- A language selector is optional. If supplied, the numbered discoverability requirement applies. English support and complete declared translations are mandatory independently of that choice.
- Partner guidance mixes hard constraints, quality recommendations and unavailable publishing routes. SDK adapter support does not imply distribution availability. Resolve partner-specific no-external-call/analytics restrictions without inventing unsupported configuration.
- Repeat-purchase, stale-callback, write-order and overlapping-pause scenarios are engineering acceptance checks supporting functional gameplay. They are not additional official numbered rules or a claim of actual game execution.

The matrix paraphrases requirements and adds implementation/evidence guidance. It is not an official certification or a substitute for a current moderation decision.

## Professional foundation and evidence scope

Reviewed for this revision: 2026-11-05. Raph Koster's [A Theory of Fun for Game Design](https://www.theoryoffun.com/) is professional further reading verified through the author site and excerpt index. It informs questions about a playable/learnable core loop, not platform certification or a numerical retention guarantee. The actual Playgama requirements and tool contracts govern publication.

Stored content is maintained only when the user requests a revision. There is no automated source collector or refresh mechanism.
