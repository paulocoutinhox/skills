# Game release review

Fill in this evidence template by hand. Replace the bracketed fields with real observations. Do not mark execution checks as passed based only on reading the source, mock behavior or archive processing.

## Identity and scope

- Game/application: [Name and real ID].
- Requested endpoint: [Local preparation, public QA upload, sandbox, moderation or specific catalog update].
- Source revision and build command: [Real values].
- Archive ID, version and SHA-256: [Real values, or not uploaded].
- Engine, export template and Bridge versions: [Real values].
- Checklist/documentation access dates: [Real dates and links].
- Destinations, devices, browsers, languages and orientation: [Real supported claims].
- Configuration and initialization owner: [Paths and which plugin, template or application code owns it].
- Environments: [Local mock, local QA harness, uploaded QA, sandbox or production].
- Detected adapter per environment: [Observed platform ID, never an assumed QA-specific ID].
- Evidence access: [Few non-secret links or files. No signed URLs, tokens or player personal data].

## Numbered requirement coverage

Use PASSED, FAILED, BLOCKED or NOT APPLICABLE. Add rows to cover every ID that applies in the skill's requirements matrix. A grouped result needs evidence for every item in it. Explain every NOT APPLICABLE entry.

| Requirement IDs | Applicability | Status | Build/environment | Steps and actual result | Evidence or blocker |
| --- | --- | --- | --- | --- | --- |
| [Exact IDs] | [Reason] | [Status] | [Real values] | [Observed behavior] | [Evidence] |

## Critical regression cases

Every row starts as not run. Replace BLOCKED only after the case runs, or after a justified exclusion of an optional feature.

| Case | Required observation | Status and evidence |
| --- | --- | --- |
| Fresh startup | Valid container detection, finished initialization and storage, and a usable first interactive frame before game-ready. No unhandled SDK rejection. | BLOCKED: Not executed. |
| SDK/network failure | Loader stays responsive with a clear failure or retry state. No endless wait, fake readiness or mock used in production. | BLOCKED: Not executed. |
| Local versus host | Local mock allows development. Uploaded QA checks real host messages, ads and storage. | BLOCKED: Not executed. |
| First launch and Start | No fullscreen ad triggered by the game during loading, readiness or the first Start before real play. Check ads triggered by messages or config too. | BLOCKED: Not executed. |
| Natural ad opportunities | Real level, loss or menu pauses request supported interstitials. The SDK controls how often. Active play is never interrupted by surprise. | BLOCKED: Not executed. |
| Ad no-fill, close and error | The game stays usable and keeps progress, audio choices and other pause reasons. | BLOCKED: Not executed. |
| Reward lifecycle | Clear opt-in and decline, optional benefit, one grant only on rewarded, no grant on cancel or error, recovery offer at most once per attempt. | BLOCKED: Not executed. |
| Menu and pause mute | A visible control you can reach affects music, effects and video audio. The state stays the same across scenes. | BLOCKED: Not executed. |
| Initial platform mute | Silent from the first frame and after reload while host mute is on, before any later event. | BLOCKED: Not executed. |
| Focus and overlapping pauses | Test player muted and unmuted, tab hide and show, host mute, platform pause and ad combinations. Clearing one reason never overrides another. | BLOCKED: Not executed. |
| Audio unlock | No forced playback before the player interacts. Browser or iOS context resume respects the user's saved mute. | BLOCKED: Not executed. |
| Save round trip | Real progress, economy, settings and the entitlements that apply survive reload, rotation and ads through Bridge. Record what the backend supports. | BLOCKED: Not executed. |
| Save failure/order | Missing data for a new user is different from a read failure. Failed or outdated writes do not erase known progress or claim a successful cloud sync. | BLOCKED: Not executed. |
| Cross-session/cloud | Where supported, check the real cloud or account round trip. Mock or local storage does not prove cloud syncing. | BLOCKED: Not executed. |
| Resource-limited action | Visible resource or requirement and a valid way to recover. No apparent dead end or enabled action that does nothing. | BLOCKED: Not executed. |
| Shops and repeatable items | Two valid purchases, leave and return, reload, not enough funds, fast clicks and error recovery. One correct deduction and grant per transaction. | BLOCKED: Not executed. |
| Real-money purchases | Supported prices, cancel and error, recovery after a crash, consumables can be bought again, permanent ownership with no second purchase. | BLOCKED: Not executed. |
| Complete core loop | First-time onboarding, every visible area and action, repeat rounds, restart, failure and finish, and all required progress paths. | BLOCKED: Not executed. |
| Layout/input | Claimed desktop and mobile controls, square, narrow and wide layouts, safe areas, orientation, dialogs and keyboard inputs. | BLOCKED: Not executed. |
| Content and marketing | Rights, banned themes, finished icons, localization, honest covers and a submitted title that matches the in-game title. | BLOCKED: Not executed. |
| Engine/partner constraints | The real engine setting and destination-specific limits and availability, checked against current sources. | BLOCKED: Not executed. |

## Findings and retests

| Finding | Requirement or engineering reason | Reproduction | Correction | Retest build and evidence | Status |
| --- | --- | --- | --- | --- | --- |
| [Concrete failure] | [Exact scope] | [Steps] | [Real change] | [New archive/hash and observed result] | [Status] |

## Publication state and handoff

- Archive processing and build verdict: [Real separate states].
- Sandbox eligibility and active archive: [Real values or not requested].
- Submission eligibility and moderation state: [Real values or not submitted].
- Catalog/live archive and confirmed URL: [Real values or not published].
- Mandatory failures and checks not run: [Explicit list].
- Owner console action or destination limit: [Exact remaining step].
- Specific catalog-update or traffic decision, if requested: [Real authorization scope. No assumed consent].
- Release-readiness conclusion: [Decision based on evidence, within the tested scope].

This report does not submit to moderation, approve the game or authorize publication by itself.
