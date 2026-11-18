# Review, publication, and ongoing operations

## Release preparation

Create the platform's editable version only after checking existing versions and allowed transitions. Use version localizations for description, keywords, promotional text, support/marketing URLs, and release notes. Use app information localizations for name/subtitle and privacy fields according to the exact schema. Associate a processed compatible build. Confirm export compliance, age ratings, content rights, privacy and SDK disclosures, accessibility declarations, distribution, pricing, and purchase readiness.

Prepare reviewer contact details, working credentials when needed, notes, attachments, and a reliable backend. Reviewers must be able to find all paid features and reproduce important workflows. Document hardware, region, account, or external accessory requirements honestly. Keep services running during review.

Use TestFlight internal testing first. For external testing, configure beta metadata, reviewer access, groups, testers, and beta review where required. Inviting testers sends invitations, so use the user-authorized audience. A public beta link is an external distribution decision. A successful external beta does not equal App Store review approval.

Complete the [policy/readiness matrix](policy-and-review-checklist.md), [field inventory](store-fields-and-localizations.md), [price/country checks](pricing-and-availability.md) and [release evidence](../assets/release-evidence.md). Unexecuted checks remain BLOCKED. A known mandatory failure prevents a release-ready conclusion.

## Choose the smallest correct change

| Request | Correct route |
| --- | --- |
| New binary/version | Create the eligible next platform version, reserve a fresh build, upload/process, associate build, complete content and submit review. |
| Editable draft text | PATCH the actual AppInfo/version localization, read back and retain its parent review state. Do not create another app or unnecessary binary. |
| Live promotional text | Use the supported editable promotional-text field. This does not imply name/description/screenshots can change without their required version/review path. |
| New media | Upload current library assets, verify processing/specification, create/order placements on an editable parent and follow its review route. |
| Price/country change | Use the actual commercial resources and approved effective dates. Changes are independent of binary review and can affect current customers. |
| Metadata rejection | Correct the identified metadata and resubmit the same binary when eligible. Do not allocate a new build solely to work around a text issue. |
| Binary rejection | Reproduce/fix the implementation, allocate a new build, upload/process, replace the intended build and retest the reviewer path. |
| Approved pending manual release | Verify the exact approved platform/version/build and create the supported release request within scope. Do not resubmit unnecessarily. |

## Submission state machine

1. Read version, review submission, submission items, and selected build states.
2. Validate complete metadata and asset delivery states for every selected platform/locale.
3. Build the current review submission and item graph using documented relationships. Include associated product versions when required.
4. Execute submission only when it is within the requested task scope. Record submission IDs and timestamps.
5. Poll at bounded intervals or use supported notifications. Distinguish waiting, in review, rejected, unresolved issues, approved/pending release, processing for distribution, and available. Never translate an unfamiliar state into success.
6. Address rejection causes against the actual review message, implementation, and current guidelines. Avoid unrelated binary changes during metadata-only remediation.
7. Release using the chosen mode. A manual release request and phased rollout require eligible states. Confirm dates/time zones and storefront coverage for scheduled/preorder launches.

If the user requested preparation only, deliver the complete artifacts and exact remaining mutation before asking for publication approval. If publication was already authorized, do not ask redundant approval for ordinary prerequisite API operations. Owner-only legal facts and unsupported console operations remain explicit handoffs.

### Concrete current review requests

Create a submission with `POST /v1/reviewSubmissions`, the actual `app` relationship and supported platform. Then add the actual eligible item with `POST /v1/reviewSubmissionItems`. An ordinary app version item uses:

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

Other supported item relationships include current `inAppPurchaseVersion`, `subscriptionVersion`, `subscriptionGroupVersion`, custom-page version, experiment, event, eligible asset-library image/video, background asset version, Game Center versions and retention-message version. Select the real item type and submission rules. Do not attach every possible relationship to one item.

Once all applicable items are ready, `PATCH /v1/reviewSubmissions/<submission-id>` can submit:

```json
{
  "data": {
    "type": "reviewSubmissions",
    "id": "<submission-id>",
    "attributes": {"submitted": true}
  }
}
```

Use actual IDs and record the returned state. This example is not executed by reading the skill. A first combined product/subscription/binary submission still follows the documented applicable console flow. Current item creation capability alone does not override that behavioral prerequisite.

### Monitor, cancel, correct and resubmit

Submission states include `READY_FOR_REVIEW`, `WAITING_FOR_REVIEW`, `IN_REVIEW`, `UNRESOLVED_ISSUES`, `CANCELING`, `COMPLETING` and `COMPLETE`. Items separately report `READY_FOR_REVIEW`, `ACCEPTED`, `APPROVED`, `REJECTED` or `REMOVED`. Completion does not prove every originally requested item was approved. Inspect the actual remaining item graph and version state.

Read the version's actual `appVersionState` and applicable `appStoreState` response meanings without writing either. Export-compliance waiting, invalid binary, metadata rejection, pending developer/Apple release and distribution processing need different next actions. Contracts and country availability can remain independent blockers.

For an authorized eligible cancellation, update the submission with `canceled: true` and wait for its real result. Cancelling is not an instantaneous state assignment. Do not create a second conflicting submission while cancellation is in progress.

For unresolved issues, inspect each rejected item and actual message, correct the responsible content/implementation, retest and use supported item `resolved` or `removed` updates only for the intended eligible operation. Removing an item changes release scope and must not conceal a required unresolved feature. Re-read the whole submission before resubmitting or completing remaining items.

App Review correspondence is not `customerReviewResponses`. The researched API has no general App Review message-post endpoint. Use app → App Review/unresolved submission → Resolve → Reply to App Review, with the actual authorized role, concise factual explanation and relevant attachments. Draft the response during preparation, but send it only within the user's messaging authorization. Appeals and expedited review have their actual owner/support surfaces and no invented API shortcut.

Track each finding as requirement/message → reproduction → actual fix → replacement resource/build → observed retest. Keep reviewer access/backend live. Do not resubmit unchanged defects or claim a response was sent from a saved local draft.

## Release controls

Set `releaseType` deliberately: `MANUAL`, `AFTER_APPROVAL` or `SCHEDULED` with a supported `earliestReleaseDate`. Confirm time zone, preorder/country dates and app-specific eligibility. Scheduled release is not a guarantee that review will finish by the requested time.

For manual publication, `POST /v1/appStoreVersionReleaseRequests` relates the actual eligible approved `appStoreVersion`. Verify subsequent distribution/storefront state. Never release whichever version happens to be first in a list.

For an eligible update, use `appStoreVersionPhasedReleases` and supported `phasedReleaseState` transitions. Current phases span seven days at 1%, 2%, 5%, 10%, 20%, 50% and 100% of eligible automatic updates. Anyone can still manually download the app, so this is not a strict access percentage. Total pause allowance is 30 days. Read actual current day/pause duration before pausing/resuming/completing. Removing sale stops that phased run and is not a harmless pause.

## Launch verification

Read live version and availability, open the actual storefront link for each selected market/platform, install a production build, and smoke-test launch, login/account deletion, core flow, paywall/prices, purchase/restore, links, accessibility, and backend configuration. Verify that screenshots and translations match the released build and that review-only credentials do not expose real users.

For phased releases, observe crash rate, startup, API errors, purchase conversion, refund signals, and support reports against a known baseline. Pause a rollout when justified by real evidence and user scope. A pause does not uninstall a version already downloaded. Apple normally requires a new reviewed build for a code rollback. Preserve the next build reservation and prepare a forward fix rather than reusing an old upload number.

## Extended administration

Use the catalog for review responses, custom product pages, product page experiments, in-app events, Game Center, accessibility, analytics, sales/finance reports, asset packs, and supported alternative distribution. Check per-operation roles, platform eligibility, asynchronous states, and territory rules. Public replies, account invitations, product price changes, app availability removal, account transfers, and customer-affecting actions require the actual requested scope. Do not run them merely because they appear in an API inventory.

Keep an operational release record: app/bundle/team identifiers, git revision, toolchain, marketing version/build, platform, artifact SHA-256, selected build IDs, metadata revision, asset inventory, products/offers, submission IDs, release mode, remote state, verification time, and unresolved items. Redact signing secrets, authentication material, receipts, and personal data.

## Replace a queued submission without losing its items

Use this when an already submitted version needs editable media/metadata or an intended replacement
build. First read the current version, submission and **all** item pages/relationships. Record the
build, release mode, reviewer notes/access, localizations and each app/product/group version target.
Do not assume the graph contains only the binary. A queued submission can also contain subscription
group and monthly/annual product versions.

1. Establish that cancellation and resubmission are actually within scope. If the user has authorized
   this replacement, preserve that authorization across the prerequisite calls. Otherwise explain the
   concrete queued submission and possible review delay before seeking the needed decision.
2. Send the documented `canceled: true` update to that submission and wait for its terminal result.
   Read the version and item states again. Do not submit a competing graph during `CANCELING`.
3. On the editable version, apply only the intended changes. Process, place and order new media.
   Associate the exact valid build if replacement was requested. Preserve reviewer access and the
   existing automatic/manual release strategy unless changing them was requested.
4. Inspect eligibility of each previously intended target again. Reuse eligible unchanged version
   resources instead of creating new products, subscriptions or review versions automatically.
5. Create one replacement submission, attach the intended eligible app version and every required
   product/group version, and compare the resulting graph with the recorded scope before submitting.
6. Set `submitted: true` only after the graph is complete. Read back both submission and app-version
   state, the selected build and item relationships. Record the new submission ID and submission time.

For example, a graph with an app version, a subscription group version and two subscription versions
must still represent those four intended targets after replacement. New item IDs are expected. Match
by target type/resource identity rather than insisting the old item IDs survive. If an item is already
approved or no longer attachable, reconcile that actual state instead of silently dropping it or forcing
an invalid duplicate. Initial combined-product submission prerequisites still apply.

An active screenshot placement is not a review approval. A submission in `COMPLETE` can be the
canceled old submission. Verify the actual replacement ID and the version's current state before
reporting success. Review notes/attachments can be updated through their own supported resources,
but that is not a reply to Apple's reviewer conversation. The 4.6 public contract exposes no general
App Review correspondence endpoint. Use the actual authorized console flow for a reply.
