# Upload, QA, sandbox, moderation, and catalog updates

## Upload the archive

1. Re-read the live checklist and fix all known required failures. Inspect the ZIP root, entries, game-file/upload size, runtime assets, Bridge config and secret exclusions.
2. Call `start_archive_upload` with the real application ID, a recognizable versioned name of at most 200 characters, and exact compressed byte length.
3. PUT the ZIP bytes to the returned presigned URL with exactly the returned headers. Current URLs last one hour and are signed for size/type. Do not add unrelated account authentication or log the URL.
4. Call `confirm_archive_upload` after transfer. Confirmation queues unpack/analysis and makes successfully processed QA files publicly accessible. It does not publish the sandbox.
5. Poll `get_archive_status` with bounded intervals until unpack and build checks reach a meaningful terminal state. `processing: DONE` alone is insufficient. Current publication requires a `PASSED` build check. `NOT_CHECKED`, `PROBLEM`, and unknown states are not success.
6. On `bridgeSdk: NOT_FOUND`, retrieve the actual certification link and live Bridge docs, inspect startup failures, fix, and upload a new versioned archive. Opening the link does not unlock a failed build.

Use confirmation's documented safe repeat behavior to reconcile an uncertain response. Do not duplicate archive creation blindly. Retain archive ID, build version/hash, size, processing state, Bridge analysis/version, and QA link.

## Upload covers and save the form

For each required slot, reserve with `start_cover_upload` using current `cover`, `format`, and exact `contentSize`, PUT returned bytes/headers, then `confirm_cover_upload`. Confirm checks complete decoding, encoding and exact dimensions, publishes a permanent URL, and replaces the saved slot. A rejected image requires a corrected upload. Preserve previous files and verify saved media IDs.

Complete form text, category, languages, supported devices, orientation/features, and required declarations. Use a partial save for intended scalar changes and preserve whole enum arrays. Re-read `get_application` and `get_launch_steps` after each stage. A missing source gives `UNKNOWN`, which remains unresolved. A saved draft does not establish moderation eligibility.

## Sandbox launch

Read `get_sandbox_state` for the intended archive and current publication verdict. The researched sandbox gates include all three covers, a complete form/category, passed unpack/build checks, an eligible Bridge version (currently at least 2.2.0), organization quotas, publication-rate limits, and allowed game status. Multiplayer/current catalog-live/blocked conditions can prevent sandbox publishing. Read current refusal codes rather than trying to bypass them.

If sandbox publication is authorized and eligible, call `publish_sandbox` for the intended archive, then re-read sandbox state, publication records, and active archive. Open the actual returned link and test the game. Do not conclude success from a link to a prior revision. A sandbox is public to anyone with its link and is separate from approved catalog distribution.

`get_sandbox_share` prepares text and share URLs. It does not post to networks. Only send/post externally when the user explicitly authorizes that channel/action. Never invent public social post links for traffic eligibility.

## Moderation

Before treating an archive as release-ready, complete the [numbered review matrix](review-requirements.md) and [evidence report](../assets/review-report.md). Include all applicable technical, monetization, UX, content, engine and selected destination requirements, not just automatic archive checks. A passed upload/build analysis does not establish sound, playable progression, purchase correctness or human approval.

The report must identify the exact archive/hash, source revision, engine/Bridge versions, actual host/adapter, tested browsers/devices/languages, requirement IDs and reproducible observations. A recording of a different version is not evidence for the submitted archive. Mark unavailable execution BLOCKED, actual defects FAILED and optional exclusions NOT APPLICABLE with a reason. Do not submit a known-broken required flow as ready.

Call `get_submission_state` with the explicit game/archive and intended `MANUAL` or `AUTO` review type. A current `catalogAvailable: false` is a genuine eligibility blocker, including possible sandbox targets/cooldowns that must be met. Inspect real console targets and current state. Do not promise that filling metadata alone unlocks moderation.

Initial catalog publication and other moderation destinations are submitted by the owner in the developer console. The researched MCP has no moderation-submission or reply tool. Finish all upload/configuration/QA work, provide the exact eligible archive and returned console QA link, explain the outstanding submit action, and monitor comments/state once available. Never fabricate a submission receipt.

When comments arrive, reproduce each failure and map it to the applicable requirement and game state. Correct the cause and retest neighboring flows, then upload a new recognizable build and rerun the full applicable checklist. Do not copy private correspondence into public source notes or claim support accepted a fix before actual verification. Provide a neutral finding/correction/evidence summary for the authorized owner handoff.

## Catalog updates and traffic consent

For a game already live in the catalog, `send_playgama_catalog_update` changes the build for all its catalog players without moderation. The provider requires an explicit yes for that individual update after naming the game, archive/build, and immediate all-player/no-moderation effect. Prior consent to another update or sandbox is insufficient. Prepare the concrete reviewed update first, then follow this provider requirement. Do not add this same confirmation rule to ordinary read/preparation calls.

`start_sandbox_traffic` spends the relevant bonus/budget over its window and cannot be undone. Read eligibility and actual offer/run details first, explain the concrete effect, and obtain the provider-required explicit decision before starting. Do not quote an internal accounting budget as the user's price, assume a "free" bonus is consequence-free, or imply that general launch authorization is a purchase of paid traffic.

Referral acceptance also has organization-level irreversible implications. Only apply the developer's actual supplied code/link within eligibility and scope. Never invent one or silently affiliate the account.
