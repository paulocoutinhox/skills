# Edits, testing, review, and production

## Edit transaction

1. Read the current package state, and run release operations for that package one at a time.
2. Create an edit with `androidpublisher.edits.insert`, and record the edit ID and expiry.
3. Read the current app details, localized listings, images, tracks and artifacts through that edit.
4. Upload the signed AAB with `androidpublisher.edits.bundles.upload` and the exact simple or resumable media path in the official method contract. Record the returned versionCode and check it against the reserved value and the bundle manifest.
5. Upload the deobfuscation files and native symbols that apply, through the supported methods. Set the intended listing and asset changes.
6. Update only the intended track with explicit releases, versionCodes, localized release notes and rollout state.
7. Call `edits.validate`, fix failures, choose the review-conflict behavior on purpose, then call `edits.commit` within the authorized scope.
8. Read the remote release and track state, and the console publishing and review state, through a valid fresh read context or the supported release-history surface. The committed edit is no longer an editable transaction. A successful commit does not prove approval or public availability.

For example, a draft track release object can contain:

```json
{
  "track": "internal",
  "releases": [
    {
      "name": "1.0.0",
      "versionCodes": ["23"],
      "status": "draft",
      "releaseNotes": [
        {"language": "en-US", "text": "Initial release."}
      ]
    }
  ]
}
```

Replace every value with the state you want for the real package. `tracks.update` can replace the release list, so keep the releases you mean to retain and multivariant version codes. An `inProgress` rollout needs an allowed `userFraction` that you choose on purpose. `completed` can show the release to the whole intended audience. Never use it as a general fix for a rollout error.

Internal app sharing has different links, limits, signatures and eligibility from an internal testing track. Pick the right one for the user's goal. Promoting to another track usually reuses an artifact that is already uploaded instead of rebuilding it. A newly built and uploaded artifact needs a new reserved code.

### Field and state decisions

Use all the relevant `TrackRelease` fields on purpose: internal `name`, string `versionCodes`, localized `releaseNotes`, `status`, allowed `userFraction`, allowed `countryTargeting` and `inAppUpdatePriority`. A form-factor track can be named `wear:production` or `automotive:production` when that really applies. Look up the current track IDs. `tracks.create` supports the documented closed-testing setup, not any made-up track type.

Set the update priority before rollout, within 0–5. You cannot change it after rollout for those artifacts. For country targeting on a production in-progress release, use the real `countries` and a clear `includeRestOfWorld` choice. It is not global product availability or an API for changing all the countries where the app is sold.

Record `expiryTimeSeconds` as the edit's real expiry. Console changes or another publisher can make your snapshot out of date. On a conflict or expiry, read the live state again and apply only the intended changes in a new edit, one at a time. Do not replay an outdated full track array over another release.

### Commit and existing review

`edits.commit` has an empty request body. Query parameters control important behavior. Current `changesInReviewBehavior` defaults to `CANCEL_IN_REVIEW_AND_SUBMIT`, also when it is not set. It can cancel a review in progress and send the combined changes for publishing.

For routine updates that should keep an existing review, choose `ERROR_IF_IN_REVIEW` explicitly. If changes are in review, the call returns an error and the edit stays valid. Look at the real error and decide whether to wait or do a replacement the user authorized. Do not catch the error and quietly switch to cancellation.

```http
POST /androidpublisher/v3/applications/<package>/edits/<edit-id>:commit?changesInReviewBehavior=ERROR_IF_IN_REVIEW
```

When replacing a review in progress really is the intended, authorized operation, use the documented cancel-and-submit behavior knowingly and report the combined set of changes. A commit can affect more than the one field you edited last.

`changesNotSentForReview` has its own contract, related to rejections, for holding changes until the explicit console Send for review step. It is not managed publishing, a general draft flag or a way to force approval. Use it only for the real supported state and workflow. A successful validate or commit does not give you a full API for policy-review messages.

## Review and managed publishing

Finish the open app content forms, credentials and app access, screenshots, signing, pricing and countries, content rating and policy checks. Some changes need an explicit review submission in the console or a managed-publishing action. Read the current `edits.commit` behavior and what `changesNotSentForReview` means for the real app. Do not flip it on an error to quietly change the release intent, or claim it forces all changes into review.

Managed publishing needs an app that is already available, and it cannot hold back an app's first publication. Internal testing and some price, product and rollout changes take effect right away under different rules. Read the current publishing overview instead of treating managed publishing as a general transaction or a way to schedule a first launch.

For personal developer accounts created after November 13, 2023, the researched rule is a closed test with at least 12 opted-in testers for 14 days in a row, and then an application for production access. Check the account's current eligibility. Do not invent testers, automate fake engagement, or claim that an internal-track upload skips that rule.

Run the pre-launch report and the form-factor quality checks that apply. Review the policy status and the real rejection messages. Fix the issue they name and everything it affects. Keep backend and reviewer access available for the whole review. A successful `edits.validate` checks API consistency, not policy compliance or user experience.

Complete [the policy/readiness checks](policy-and-review-checklist.md) and [field/release evidence](../assets/release-evidence.md). Keep app status, update status and the status of each item separate. A live production app can also have a rejected pending update at the same time. A missing reviewer login or a declaration update does not always need a new binary.

### Rejection, correction and resubmission

1. Read the real policy message, the affected artifact or item and the console Needs attention and Publishing overview state. Record the requirement, how to reproduce it and which customers it affects, without copying private messages into public files.
2. Fix the real field, declaration, reviewer access or code. For a fix that only touches metadata or access, keep the existing eligible artifact. For a binary fix, reserve a fresh higher code, build and test it, and upload it.
3. Run the related regression checks again, and keep the listing, product and release state that should not change. Do not turn off a paid feature only to hide it from review.
4. Validate and commit the supported API changes with a review-conflict behavior you chose on purpose. Finish any real App content or policy tasks in the console.
5. On Publishing overview, look at the full set of Changes not yet sent and ready to send. Keep unrelated changes out as far as the UI allows, and use Send for review within scope. Check the new real review state.
6. If you disagree with a decision, prepare evidence and use the documented appeal or support channel when authorized. `reviews.reply` posts a public reply to a customer review and is not a policy appeal.

Review time is not guaranteed. Adding or replacing changes can affect the review window. Do not promise a launch date based on an API commit time, and do not keep resubmitting unchanged content.

For a first production release on a draft app, use the [worked API-to-Console sequence](first-production-release.md).
An API error that happens only because the app is a draft is a state limit, not a reason to upload
again or create another app. Keep the build, finish the factual setup and confirm the exact release
before you send the full pending set.

## Rollout and recovery

Choose the internal, closed, open or production track, countries, release timing, managed publishing and rollout fraction before you change anything. Confirm the exact release graph you want and its effect on customers. Respect the authorization the user already gave, without asking again for every API call. Do not read a request to prepare screenshots or build a bundle as a request to publish to production.

Watch the real track states, live store page, installability, Android vitals, backend errors, billing results and support signals. The separate Developer Reporting API may support automated metrics, with its own current schema and permissions. Record real data, not a made-up all-green result.

Halt a staged rollout when it makes sense within the authorized operation, then prepare a forward fix with a higher code. A halted rollout does not remove versions that are already installed. Check that backend and schema changes still work with versions people still use, even when the repository's coding style does not keep unneeded legacy layers in the source.

The current store also supports [halting eligible fully rolled-out releases](https://support.google.com/googleplay/android-developer/answer/16285429?hl=en), through the Console or the Publishing API. It does not apply to internal test tracks, and it cannot halt the first release on a track because there is no earlier full release. The earlier serving version must still meet policy. When the halt works, Play serves the eligible earlier version to new users and other eligible users. Users who already updated are not downgraded remotely.

For an authorized full-release halt, inspect the real release history and eligibility, update the intended track and release state through the supported edit contract, validate and commit, then check the serving and release state. Do not set an invalid `userFraction: 1`, invent a rollback endpoint or assume the earlier artifact can replace installed higher codes. Resuming, and shipping a fixed release with a higher code, stay explicit decisions.

Deliver the package, git revision, versionName/versionCode, artifact hash, signing certificate fingerprint, edit ID, track and release state, countries and fraction, product graph, policy status, review state, public link and open tasks. Keep cleaned evidence and restricted symbol artifacts. Never include private signing material or raw customer purchases.
