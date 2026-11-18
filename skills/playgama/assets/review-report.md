# Game release review

This is a manually completed evidence template. Replace bracketed fields with real observations. Do not mark execution checks passed from source inspection, mock behavior or archive processing alone.

## Identity and scope

- Game/application: [Name and actual ID].
- Requested endpoint: [Local preparation, public QA upload, sandbox, moderation or specific catalog update].
- Source revision and build command: [Actual values].
- Archive ID, version and SHA-256: [Actual values, or not uploaded].
- Engine, export template and Bridge versions: [Actual values].
- Checklist/documentation access dates: [Actual dates and links].
- Destinations, devices, browsers, languages and orientation: [Actual supported claims].
- Configuration and initialization owner: [Paths and actual plugin/template/application responsibility].
- Environments: [Local mock, local QA harness, uploaded QA, sandbox or production].
- Detected adapter per environment: [Observed platform ID, never an assumed QA-specific ID].
- Evidence access: [Minimal non-secret links/files. No signed URLs, tokens or player personal data].

## Numbered requirement coverage

Use PASSED, FAILED, BLOCKED or NOT APPLICABLE. Expand the rows to cover all applicable IDs in the skill's requirements matrix. A grouped result needs evidence for every included item. Explain every NOT APPLICABLE entry.

| Requirement IDs | Applicability | Status | Build/environment | Steps and actual result | Evidence or blocker |
| --- | --- | --- | --- | --- | --- |
| [Exact IDs] | [Reason] | [Status] | [Actual values] | [Observed behavior] | [Evidence] |

## Critical regression cases

All rows start unexecuted. Replace BLOCKED only after execution or a justified optional-feature exclusion.

| Case | Required observation | Status and evidence |
| --- | --- | --- |
| Fresh startup | Valid container detection, completed initialization/storage and usable first interactive frame before game-ready. No unhandled SDK rejection. | BLOCKED: Not executed. |
| SDK/network failure | Loader remains responsive with a clear failure/retry state. No infinite wait, fake readiness or production mock substitution. | BLOCKED: Not executed. |
| Local versus host | Local mock permits development. Uploaded QA validates actual host messaging, ads and storage. | BLOCKED: Not executed. |
| First launch and Start | No game-triggered fullscreen ad during loading, readiness or initial Start before meaningful play. Audit message/config-triggered ads too. | BLOCKED: Not executed. |
| Natural ad opportunities | Real level/loss/menu pauses request supported interstitials. SDK controls frequency. Active play is never unexpectedly interrupted. | BLOCKED: Not executed. |
| Ad no-fill, close and error | Game remains usable and preserves progress, audio preferences and other pause reasons. | BLOCKED: Not executed. |
| Reward lifecycle | Clear opt-in and decline, optional benefit, rewarded-only single grant, cancellation/error without grant, recovery offer at most once per attempt. | BLOCKED: Not executed. |
| Menu and pause mute | Visible, reachable control affects music, effects and video audio. State remains consistent across scenes. | BLOCKED: Not executed. |
| Initial platform mute | Silent from first frame and after reload while host mute is active, before any later event. | BLOCKED: Not executed. |
| Focus and overlapping pauses | Test player muted/unmuted, tab hide/show, host mute, platform pause and ad combinations. Clearing one reason never overrides another. | BLOCKED: Not executed. |
| Audio unlock | No forced pre-interaction playback. Browser/iOS context resume respects the user's saved mute. | BLOCKED: Not executed. |
| Save round trip | Actual progress, economy, settings and applicable entitlements survive reload, rotation and ads through Bridge. Record backend capability. | BLOCKED: Not executed. |
| Save failure/order | Missing new-user data differs from read failure. Failed/stale writes do not erase known progress or advertise successful cloud sync. | BLOCKED: Not executed. |
| Cross-session/cloud | Where supported, verify the actual cloud/account round trip. Mock/local storage does not prove cloud synchronization. | BLOCKED: Not executed. |
| Resource-limited action | Visible resource/requirement and valid recovery path. No apparent dead end or enabled nonfunctional action. | BLOCKED: Not executed. |
| Shops and repeatable items | Two valid purchases, leave/return, reload, insufficient funds, rapid clicks and error recovery. Correct single deduction/grant per transaction. | BLOCKED: Not executed. |
| Real-money purchases | Supported prices, cancel/error, crash reconciliation, consumable repeatability and permanent ownership/no repurchase. | BLOCKED: Not executed. |
| Complete core loop | First-time onboarding, every visible area/action, repeat rounds, restart, failure/completion and all required progression paths. | BLOCKED: Not executed. |
| Layout/input | Claimed desktop/mobile controls, square/narrow/wide layouts, safe areas, orientation, dialogs and keyboard inputs. | BLOCKED: Not executed. |
| Content and marketing | Rights, prohibited themes, finished icons, localization, truthful covers and matching submitted/in-game title. | BLOCKED: Not executed. |
| Engine/partner constraints | Actual engine setting and destination-specific limits/availability checked against current sources. | BLOCKED: Not executed. |

## Findings and retests

| Finding | Requirement or engineering reason | Reproduction | Correction | Retest build and evidence | Status |
| --- | --- | --- | --- | --- | --- |
| [Concrete failure] | [Exact scope] | [Steps] | [Actual change] | [New archive/hash and observed result] | [Status] |

## Publication state and handoff

- Archive processing and build verdict: [Actual separate states].
- Sandbox eligibility and active archive: [Actual values or not requested].
- Submission eligibility and moderation state: [Actual values or not submitted].
- Catalog/live archive and confirmed URL: [Actual values or not published].
- Mandatory failures and unexecuted checks: [Explicit list].
- Owner console action or destination limitation: [Precise remaining step].
- Specific catalog-update or traffic decision, if requested: [Actual authorization scope. No assumed consent].
- Release-readiness conclusion: [Evidence-based decision within tested scope].

This report does not itself submit moderation, approve the game or authorize publication.
