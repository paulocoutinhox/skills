# Upload, QA, sandbox, moderation, and catalog updates

## Create the game

Call `list_applications` first. Titles are not unique, so a create whose result was unclear may already exist. Create the draft with `create_application`, an English Latin-script title and one `engine` value: `unity`, `construct3`, `cocos-creator`, `defold`, `godot`, `gdevelop`, `game_maker`, `scratch` or `js`. A custom or less common engine that ships a JavaScript and WebAssembly runtime uses `js`. Declare `agent`, `model` and `modelId` from confirmed facts.

The form title is the title players see, and requirement 3.5.1 compares it with the title inside the game. A store-search suffix such as "Brick Breaker" belongs in the form only when the game shows it too.

## First launch sequence

A new HTML5 game goes through these stages in order:

1. Call `create_application`, then `update_application_form` with title, category, description and how-to-play, a link to the game elsewhere, orientations, languages and devices. Description and how-to-play need at least 100 characters each for submission.
2. Upload the archive (below) until its build check is `PASSED` with the detected Bridge version. A `PROBLEM` with reason `GAME_NOT_READY` means the game never sent `game_ready`. Step 7 of the archive upload covers it.
3. Upload the three covers through reserve, PUT and confirm.
4. Call `publish_sandbox` with the passed archive and an update note of 80 to 500 characters. The answer is `PENDING`, and `get_sandbox_state` then shows the live revision, its archive and title, and `VISIBLE` discovery. If you change covers or the title later, call `publish_sandbox` again to update the live page.
5. Call `get_submission_state` for the archive. A new draft answers `MODERATION_UNAVAILABLE` because it cannot go to moderation directly. Call `get_launch_steps` for the path: the form step is `BLOCKED` with `NO_CERTIFICATION`, its next tool is `get_archive_qa_tool_link`, and share and traffic follow. Certification is a person playing the archive in that QA tool link.

## Upload the archive

1. Read the live checklist again and fix every known required failure. Check the ZIP root, entries, game-file and upload size, runtime assets, Bridge config and that secrets are left out.
2. Call `start_archive_upload` with the real application ID, a clear versioned name of at most 200 characters, and the exact compressed byte length.
3. PUT the ZIP bytes to the returned presigned URL with exactly the returned headers. Current URLs last one hour and are signed for size and type. Do not add unrelated account sign-in or log the URL.
4. Call `confirm_archive_upload` after the transfer. Confirming queues unpacking and analysis and makes QA files that process successfully public. It does not publish the sandbox.
5. Poll `get_archive_status` at limited intervals until unpacking and build checks reach a useful final state. `processing: DONE` alone is not enough. Current publication requires a `PASSED` build check. `NOT_CHECKED`, `PROBLEM`, and unknown states are not success.
6. On `bridgeSdk: NOT_FOUND`, get the real certification link and live Bridge docs, look into startup failures, fix them, and upload a new versioned archive. Opening the link does not unlock a failed build.
7. On `PROBLEM` with reason `GAME_NOT_READY`, the archive never sent `game_ready`. Serve the unpacked archive locally and open it in a headless browser such as Playwright's Chromium. Read every console error, since a crash after initialization is the usual cause. To confirm the message, wrap `sendMessage` on the prototype of `bridge.platform` after `bridge.isInitialized` turns true, because the platform object can be replaced during initialization. Also list what the page stored: IndexedDB databases, the origin private file system and `localStorage`. The Bridge keeps its own `localStorage` key, which is expected.

When a response is unclear, use the documented safe repeat of confirmation to check the state. Do not create a duplicate archive blindly. Keep the archive ID, build version and hash, size, processing state, Bridge analysis and version, and QA link.

## Upload covers and save the form

For each required slot, reserve with `start_cover_upload` using the current `cover`, `format`, and exact `contentSize`, PUT the bytes with the returned headers, then call `confirm_cover_upload`. Confirming checks full decoding, encoding and exact dimensions, publishes a permanent URL, and replaces the saved slot. A rejected image needs a fixed upload. Keep earlier files and check the saved media IDs.

Fill in the form text, category, languages, supported devices, orientation and features, and required declarations. Use a partial save for the scalar changes you mean to make, and keep whole enum arrays intact. Read `get_application` and `get_launch_steps` again after each stage. A missing source gives `UNKNOWN`, which is still unresolved. A saved draft does not prove moderation eligibility.

## Sandbox launch

Read `get_sandbox_state` for the archive you plan to use and the current publication verdict. The sandbox gates checked include all three covers, a complete form and category, passed unpack and build checks, an eligible Bridge version (currently at least 2.2.0), organization quotas, publication-rate limits, and an allowed game status. Multiplayer, a game already live in the catalog or a blocked game can stop sandbox publishing. Read the current refusal codes rather than trying to get around them.

If sandbox publication is authorized and eligible, call `publish_sandbox` for the chosen archive, then read the sandbox state, publication records, and active archive again. Open the real returned link and test the game. Do not decide it worked from a link to an earlier revision. Anyone with the link can open a sandbox, and it is separate from approved catalog distribution.

`get_sandbox_share` prepares text and share URLs. It does not post to networks. Send or post outside only when the user explicitly authorizes that channel and action. Never invent public social post links to qualify for traffic.

## Moderation

Before you treat an archive as ready for release, complete the [numbered review matrix](review-requirements.md) and the [evidence report](../assets/review-report.md). Include every technical, monetization, UX, content, engine and chosen destination requirement that applies, not just the automatic archive checks. A passed upload or build analysis does not prove sound, playable progress, correct purchases or human approval.

The report must name the exact archive and hash, source revision, engine and Bridge versions, the real host and adapter, the browsers, devices and languages tested, the requirement IDs and observations that can be reproduced. A recording of a different version is not evidence for the submitted archive. Mark checks that could not run as BLOCKED, real defects as FAILED and optional exclusions as NOT APPLICABLE with a reason. Do not submit a required flow you know is broken as ready.

Call `get_submission_state` with the named game and archive and the intended `MANUAL` or `AUTO` review type. A current `catalogAvailable: false` is a real eligibility blocker, which can include sandbox targets or cooldowns that must be met. Check the real console targets and current state. Do not promise that filling in metadata alone unlocks moderation.

The owner submits the first catalog publication and other moderation destinations in the developer console. The MCP checked has no moderation-submission or reply tool. Finish all upload, setup and QA work, give the exact eligible archive and the returned console QA link, explain the submit action still needed, and watch comments and state once they appear. Never make up a submission receipt.

When comments arrive, reproduce each failure and link it to the requirement and game state it concerns. Fix the cause and retest nearby flows, then upload a new, clearly versioned build and run the full checklist that applies again. Do not copy private messages into public source notes, or claim that support accepted a fix before it is really checked. Give a neutral summary of findings, fixes and evidence for the authorized owner handoff.

## Catalog updates and traffic consent

For a game already live in the catalog, `send_playgama_catalog_update` changes the build for all its catalog players without moderation. The provider requires an explicit yes for that one update, after you name the game, the archive or build, and the instant effect on all players with no moderation. Earlier consent to another update or the sandbox is not enough. Prepare the concrete reviewed update first, then follow this provider rule. Do not add the same confirmation rule to normal read or preparation calls.

`start_sandbox_traffic` spends the related bonus or budget over its time window and cannot be undone. Read eligibility and the real offer and run details first, explain the concrete effect, and get the explicit decision the provider requires before starting. Do not quote an internal accounting budget as the user's price, assume a "free" bonus has no consequences, or suggest that general launch authorization means buying paid traffic.

Referral acceptance also has effects on the organization that cannot be undone. Only apply the real code or link that the developer gives, within eligibility and scope. Never invent one or quietly link the account to an affiliate.
