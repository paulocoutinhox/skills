# Edits, testing, review, and production

## Edit transaction

1. Read current package state and serialize release operations for that package.
2. Create an edit with `androidpublisher.edits.insert`, recording edit ID and expiry.
3. Read current app details, localized listings, images, tracks, and artifacts through that edit.
4. Upload the signed AAB using `androidpublisher.edits.bundles.upload` and the exact simple/resumable media path in the official method contract. Record the returned versionCode and validate it against the reserved value and bundle manifest.
5. Upload applicable deobfuscation/native symbols through supported methods. Set intended listing/asset changes.
6. Update only the intended track with explicit releases, versionCodes, localized release notes, and rollout state.
7. Call `edits.validate`, resolve failures, choose review-conflict behavior explicitly, then `edits.commit` within the authorized scope.
8. Read remote release/track and console publishing/review state through a valid fresh read context or supported release-history surface. The committed edit is no longer an editable transaction. Commit success is not proof of approval or public availability.

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

Replace every value with the actual package's desired state. `tracks.update` can replace the release list, so preserve intended retained releases and multivariant version codes. An `inProgress` rollout requires an explicitly chosen allowed `userFraction`. `completed` can expose the release to the full intended audience. Never use it as a generic recovery from a rollout error.

Internal app sharing has different links, limits, signatures, and eligibility from an internal testing track. Choose the correct one for the user's goal. Promotion to another track normally reuses an already uploaded artifact rather than rebuilding it. A newly compiled/uploaded artifact requires a new reserved code.

### Field and state decisions

Use all relevant `TrackRelease` fields deliberately: internal `name`, string `versionCodes`, localized `releaseNotes`, `status`, permitted `userFraction`, permitted `countryTargeting` and `inAppUpdatePriority`. A form-factor track can be named `wear:production` or `automotive:production` when actually applicable. Discover current track IDs. `tracks.create` supports the documented closed-testing configuration, not creation of any imaginary track type.

Set update priority before rollout, within 0–5. It cannot be edited after rollout for those artifacts. For production in-progress country targeting, use actual `countries` and explicit `includeRestOfWorld` intent. It is not global product availability or an API for changing all app sale countries.

Record `expiryTimeSeconds` as the edit's actual expiry. Console changes/another publisher can invalidate the snapshot. On conflict or expiry, re-read live state and reapply only intended changes in a new serialized edit. Do not replay a stale full track array over another release.

### Commit and existing review

`edits.commit` has an empty request body. Query parameters control consequential behavior. Current `changesInReviewBehavior` defaults to `CANCEL_IN_REVIEW_AND_SUBMIT`, including when unspecified. It can cancel an ongoing review and send the combined changes for publishing.

For routine updates that should preserve an existing review, explicitly choose `ERROR_IF_IN_REVIEW`. If changes are in review, the call returns an error without invalidating the edit. Inspect the actual error and decide whether to wait or carry out a user-authorized replacement. Do not catch the error and silently switch to cancellation.

```http
POST /androidpublisher/v3/applications/<package>/edits/<edit-id>:commit?changesInReviewBehavior=ERROR_IF_IN_REVIEW
```

When replacing an ongoing review is actually the intended authorized operation, use the documented cancellation/submission behavior knowingly and report the combined change set. A commit can have effects beyond the one field most recently edited.

`changesNotSentForReview` has a separate rejection-related contract for retaining changes until the explicit console Send for review step. It is not managed publishing, a universal draft flag or a way to force approval. Use it only for the actual supported state/workflow. Validate/commit returning successfully does not expose a complete policy-review message API.

## Review and managed publishing

Complete outstanding app-content forms, credentials/app access, screenshots, signing, pricing/countries, content rating, and policy checks. Some changes need explicit console review submission or managed-publishing action. Read current `edits.commit` behavior and `changesNotSentForReview` semantics for the actual app. Do not toggle it on error to silently change the release intent or claim it forces all changes into review.

Managed publishing requires an app already available and cannot hold back an app's first publication. Internal testing and some price/product/rollout changes have different immediate-effect rules. Read the current publishing overview rather than treating managed publishing as a universal transaction or scheduled first-launch mechanism.

For personal developer accounts created after November 13, 2023, the researched requirement is a closed test with at least 12 opted-in testers continuously for 14 days, followed by production-access application. Check current account eligibility. Do not invent testers, automate fake engagement, or claim that an internal-track upload bypasses that requirement.

Run the applicable pre-launch report and form-factor quality checks. Review policy status and actual rejection messages. Correct the identified issue and affected consumers. Keep the backend/reviewer access available throughout review. A successful `edits.validate` checks API consistency, not policy compliance or user experience.

Complete [the policy/readiness checks](policy-and-review-checklist.md) and [field/release evidence](../assets/release-evidence.md). Separate app status, update status and individual item status. A live production app can simultaneously have a rejected pending update. Missing reviewer login or a declaration update does not necessarily require a new binary.

### Rejection, correction and resubmission

1. Read the actual policy message, affected artifact/item and console Needs attention/Publishing overview state. Record requirement, reproduction and customer scope without copying private correspondence into public files.
2. Correct the actual field, declaration, reviewer access or implementation. For metadata/access-only remediation, preserve the existing eligible artifact. For binary fixes, reserve a fresh higher code, build/test and upload it.
3. Re-run related regression checks and preserve intended unaffected listing/product/release state. Do not disable a paid feature solely to conceal it from review.
4. Validate/commit supported API changes using deliberate review-conflict behavior. Complete any actual App content or policy tasks in the console.
5. On Publishing overview, inspect the full Changes not yet sent/ready-to-send set, keep unrelated changes out as the supported UI permits and use Send for review within scope. Verify the new actual review state.
6. If disagreeing with a decision, prepare evidence and use the documented appeal/support surface when authorized. `reviews.reply` posts a public customer review response and is not a policy appeal.

Review duration is not guaranteed. Adding/replacing changes can affect the review window. Do not promise a launch date from an API commit timestamp or repeatedly resubmit unchanged content.

For a first production release on a draft app, use the [worked API-to-Console sequence](first-production-release.md).
A draft-only API error is a state constraint, not a reason to reupload or create another app. Preserve
the build, complete factual setup and confirm the exact release before sending the full pending set.

## Rollout and recovery

Select the internal, closed, open or production track, countries, release timing, managed publishing and rollout fraction before mutation. Confirm the exact desired release graph and customer impact. Preserve established user authorization without requesting redundant approval for every API call. Do not infer production publication from a request to prepare screenshots or compile a bundle.

Observe actual track states, live storefront, installability, Android vitals, backend errors, billing outcomes, and support signals. The separate Developer Reporting API may support metrics automation, with its own current schema and permissions. Record actual data, not an invented all-green result.

Halt a staged rollout when appropriate within the authorized operation, then prepare a higher-code forward fix. A halted rollout does not remove already installed versions. Verify compatibility of backend/schema changes with versions still in circulation, even when the repository's coding style does not preserve unnecessary source-level legacy layers.

The current store also supports [halting eligible fully rolled-out releases](https://support.google.com/googleplay/android-developer/answer/16285429?hl=en), through Console or the Publishing API. It excludes internal test tracks and cannot halt the first release on a track because no previous full release exists. The prior serving version must remain policy-eligible. When the halt succeeds, Play serves the eligible previous version to new/otherwise eligible users. Already updated users are not remotely downgraded.

For an authorized full-release halt, inspect actual release history and eligibility, update the intended track/release state through the supported edit contract, validate/commit, then verify serving/release state. Do not set an invalid `userFraction: 1`, invent a rollback endpoint or assume the previous artifact can replace installed higher codes. Resumption and a repaired higher-code release remain explicit decisions.

Deliver package, git revision, versionName/versionCode, artifact hash, signing certificate fingerprint, edit ID, track/release state, countries/fraction, product graph, policy status, review state, public link, and outstanding tasks. Retain sanitized evidence and restricted symbol artifacts. Never include private signing material or raw customer purchases.
