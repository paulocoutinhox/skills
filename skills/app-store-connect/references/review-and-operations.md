# Review, publication, and ongoing operations

## Release preparation

Create the platform's editable version only after checking the existing versions and the allowed state changes. Use version localizations for description, keywords, promotional text, support/marketing URLs, and release notes. Use app information localizations for name/subtitle and privacy fields, following the exact schema. Link a processed compatible build. Confirm export compliance, age ratings, content rights, privacy and SDK disclosures, accessibility declarations, distribution, pricing, and that purchases are ready.

Prepare reviewer contact details, working credentials when needed, notes, attachments, and a backend that stays up. Reviewers must be able to find all paid features and repeat the important workflows. Write down hardware, region, account, or external accessory requirements honestly. Keep services running during review.

Use TestFlight internal testing first. For external testing, set up beta metadata, reviewer access, groups, testers, and beta review where needed. Inviting testers sends invitations, so use only the audience the user allowed. A public beta link is a decision about outside distribution. A successful external beta is not App Store review approval.

Complete the [policy/readiness matrix](policy-and-review-checklist.md), [field inventory](store-fields-and-localizations.md), [price/country checks](pricing-and-availability.md) and [release evidence](../assets/release-evidence.md). Checks you have not run stay BLOCKED. A known failure in a required item means you cannot call the release ready.

## Choose the smallest correct change

| Request | Correct route |
| --- | --- |
| New binary/version | Create the next eligible platform version, reserve a fresh build, upload and process, link the build, complete the content and submit for review. |
| Editable draft text | PATCH the real AppInfo/version localization, read it back and keep its parent review state. Do not create another app or a binary you do not need. |
| Live promotional text | Use the supported editable promotional-text field. This does not mean name, description or screenshots can change without their required version and review path. |
| New media | Upload current library assets, check processing and specification, create and order placements on an editable parent and follow its review route. |
| Price/country change | Use the real commercial resources and approved start dates. These changes do not depend on binary review and can affect current customers. |
| Metadata rejection | Fix the named metadata and resubmit the same binary when eligible. Do not reserve a new build just to get around a text issue. |
| Binary rejection | Reproduce and fix the code, reserve a new build, upload and process, replace the intended build and test the reviewer path again. |
| Approved pending manual release | Check the exact approved platform, version and build and create the supported release request within scope. Do not resubmit without need. |

## Submission state machine

1. Read the version, review submission, submission items, and selected build states.
2. Check that metadata is complete and assets are delivered for every selected platform and locale.
3. Build the current review submission and its items using the documented relationships. Include linked product versions when required.
4. Submit only when it is within the task scope the user asked for. Record submission IDs and timestamps.
5. Poll at limited intervals or use supported notifications. Tell apart waiting, in review, rejected, unresolved issues, approved/pending release, processing for distribution, and available. Never treat a state you do not recognize as success.
6. Fix rejection causes by checking the real review message, the code, and the current guidelines. Avoid unrelated binary changes when only metadata needs fixing.
7. Release with the chosen mode. A manual release request and a phased rollout need eligible states. Confirm dates, time zones and store coverage for scheduled or preorder launches.

If the user asked for preparation only, deliver all the files and the exact change still left before asking for approval to publish. If publishing was already allowed, do not ask again for the normal API steps needed to get there. Legal facts only the owner knows and console operations the API does not support stay as clear handoffs.

### Concrete current review requests

Create a submission with `POST /v1/reviewSubmissions`, the real `app` relationship and a supported platform. Then add the real eligible item with `POST /v1/reviewSubmissionItems`. A normal app version item uses:

```json
{
  "data": {
    "type": "reviewSubmissionItems",
    "relationships": {
      "reviewSubmission": {"data": {"type": "reviewSubmissions", "id": "<submission-id>"}},
      "appStoreVersion": {"data": {"type": "appStoreVersions", "id": "<version-id>"}}
    }
  }
}
```

Other supported item relationships include current `inAppPurchaseVersion`, `subscriptionVersion`, `subscriptionGroupVersion`, custom-page version, experiment, event, eligible asset-library image/video, background asset version, Game Center versions and retention-message version. Pick the real item type and follow its submission rules. Do not attach every possible relationship to one item.

When all items that apply are ready, `PATCH /v1/reviewSubmissions/<submission-id>` can submit:

```json
{
  "data": {
    "type": "reviewSubmissions",
    "id": "<submission-id>",
    "attributes": {"submitted": true}
  }
}
```

Use real IDs and record the returned state. Reading this skill does not run the example. A first combined product/subscription/binary submission still follows the documented console flow that applies. Being able to create items does not remove that requirement.

### Monitor, cancel, correct and resubmit

Submission states include `READY_FOR_REVIEW`, `WAITING_FOR_REVIEW`, `IN_REVIEW`, `UNRESOLVED_ISSUES`, `CANCELING`, `COMPLETING` and `COMPLETE`. Items report their own state: `READY_FOR_REVIEW`, `ACCEPTED`, `APPROVED`, `REJECTED` or `REMOVED`. A completed submission does not prove that every item you first asked for was approved. Check the real remaining items and the version state.

Read the version's real `appVersionState` and the meaning of any `appStoreState` in the response, without writing either one. Waiting for export compliance, an invalid binary, a metadata rejection, a release pending from you or Apple, and distribution processing each need a different next step. Contracts and country availability can still block things on their own.

For an allowed, eligible cancellation, update the submission with `canceled: true` and wait for the real result. Cancelling does not happen instantly. Do not create a second, conflicting submission while cancellation is still running.

For unresolved issues, check each rejected item and its real message, fix the content or code that caused it, test again and use the supported item `resolved` or `removed` updates only for the eligible operation you mean. Removing an item changes what gets released and must not hide a required feature that is still unresolved. Read the whole submission again before you resubmit or complete the remaining items.

App Review messages are not `customerReviewResponses`. The researched API has no general endpoint for posting App Review messages. Use app → App Review/unresolved submission → Resolve → Reply to App Review, with a real allowed role, a short factual explanation and relevant attachments. Write the reply during preparation, but send it only if the user allowed you to send messages. Appeals and expedited review have their own owner and support channels and no made-up API shortcut.

Track each finding as requirement/message → reproduction → real fix → replacement resource/build → observed retest. Keep reviewer access and the backend live. Do not resubmit defects that are not fixed, and do not claim a reply was sent when it is only a saved local draft.

## Release controls

Set `releaseType` on purpose: `MANUAL`, `AFTER_APPROVAL` or `SCHEDULED` with a supported `earliestReleaseDate`. Confirm the time zone, preorder and country dates and the app's own eligibility. A scheduled release does not promise that review will finish by that time.

For a manual release, `POST /v1/appStoreVersionReleaseRequests` links the real eligible approved `appStoreVersion`. Then check the distribution and store state. Never release whatever version happens to be first in a list.

For an eligible update, use `appStoreVersionPhasedReleases` and supported `phasedReleaseState` changes. Current phases run over seven days at 1%, 2%, 5%, 10%, 20%, 50% and 100% of eligible automatic updates. Anyone can still download the app by hand, so this is not a strict access percentage. Pauses can add up to 30 days in total. Read the real current day and pause time before pausing, resuming or completing. Removing the app from sale stops that phased release and is not a harmless pause.

## Launch verification

Read the live version and availability, open the real store link for each chosen market and platform, install a production build, and quickly test launch, login/account deletion, the core flow, paywall/prices, purchase/restore, links, accessibility, and backend settings. Check that screenshots and translations match the released build and that review-only credentials do not expose real users.

For phased releases, watch crash rate, startup, API errors, purchase conversion, refund signals, and support reports against a known baseline. Pause a rollout when real evidence and the user's scope support it. A pause does not remove a version people have already downloaded. Apple usually needs a new reviewed build to roll back code. Keep the next build reservation and prepare a forward fix instead of reusing an old upload number.

## Extended administration

Use the catalog for review responses, custom product pages, product page experiments, in-app events, Game Center, accessibility, analytics, sales/finance reports, asset packs, and supported alternative distribution. Check the roles each operation needs, platform eligibility, background states, and territory rules. Public replies, account invitations, product price changes, removing app availability, account transfers, and other actions that affect customers need the real scope the user asked for. Do not run them just because they appear in a list of API operations.

Keep a release record: app/bundle/team identifiers, git revision, toolchain, marketing version/build, platform, artifact SHA-256, selected build IDs, metadata revision, asset list, products/offers, submission IDs, release mode, remote state, time of checking, and open items. Hide signing secrets, authentication material, receipts, and personal data.

## Replace a queued submission without losing its items

Use this when a version that is already submitted needs editable media or metadata changes or an
intended replacement build. First read the current version, the submission and **all** item pages
and relationships. Record the build, release mode, reviewer notes and access, localizations and each
app, product and group version target. Do not assume it holds only the binary. A queued submission
can also hold subscription group and monthly/annual product versions.

1. Confirm that cancelling and resubmitting are really within scope. If the user allowed this
   replacement, keep that permission through the steps needed to get there. Otherwise, explain the
   specific queued submission and the possible review delay before asking for the decision.
2. Send the documented `canceled: true` update to that submission and wait for its final result.
   Read the version and item states again. Do not submit a competing set of items during `CANCELING`.
3. On the editable version, make only the intended changes. Process, place and order new media.
   Link the exact valid build if a replacement was requested. Keep reviewer access and the existing
   automatic or manual release strategy unless the user asked to change them.
4. Check again whether each target you meant to include is eligible. Reuse eligible version resources
   that did not change instead of automatically creating new products, subscriptions or review
   versions.
5. Create one replacement submission, attach the intended eligible app version and every required
   product and group version, and compare the result with the recorded scope before submitting.
6. Set `submitted: true` only after all items are in place. Read back both the submission and the
   app-version state, the selected build and the item relationships. Record the new submission ID and
   the submission time.

For example, a submission with an app version, a subscription group version and two subscription
versions must still cover those four intended targets after the replacement. New item IDs are
expected. Match items by target type and resource identity, not by old item IDs. If an item is
already approved or can no longer be attached, deal with that real state instead of quietly dropping
it or forcing an invalid duplicate. The rules for a first combined-product submission still apply.

An active screenshot placement is not a review approval. A submission in `COMPLETE` can be the old
cancelled submission. Check the real replacement ID and the version's current state before you report
success. You can update review notes and attachments through their own supported resources, but that
is not a reply to Apple's reviewer conversation. The 4.6 public contract has no general endpoint for
App Review messages. Use the real allowed console flow for a reply.
