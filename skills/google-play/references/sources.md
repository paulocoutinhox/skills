# Sources and limitations

Checked on **2026-11-05**, with later rechecks dated in their own sections. At release time, check the current method behavior, target SDK and Billing deadlines, account requirements and special device rules again.

| Source | Coverage |
| --- | --- |
| [Android Publisher Discovery](https://androidpublisher.googleapis.com/$discovery/rest?version=v3) | All 149 Publisher v3 operations at revision 20261118 (checked 2026-11-18) and full structural models |
| [Android Publisher reference](https://developers.google.com/android-publisher/api-ref/rest) | Endpoint behavior, limits and examples |
| [API getting started](https://developers.google.com/android-publisher/getting_started) | Enabling the API, OAuth and service-account setup, and the current account model |
| [Edits workflow](https://developers.google.com/android-publisher/edits) | Edit sessions, uploads and how transactions work |
| [Review and managed publishing](https://support.google.com/googleplay/android-developer/answer/9859654?hl=en) | Review handoffs, the first-release limit and changes that take effect right away |
| [Current edit commit](https://developers.google.com/android-publisher/api-ref/rest/v3/edits/commit) | Empty-body commit, the default that cancels an existing review, and ERROR_IF_IN_REVIEW behavior |
| [Publishing statuses](https://support.google.com/googleplay/android-developer/answer/9859751?hl=en) | Separate app, update and item state, and rejection, removal and suspension |
| [Review preparation](https://support.google.com/googleplay/android-developer/answer/9859455?hl=en) | Real App content, a privacy policy reachable everywhere and not a PDF, ads and restricted-access instructions |
| [Eligible full-release halt](https://support.google.com/googleplay/android-developer/answer/16285429?hl=en) | Publisher and console support, first-release and internal exclusions, and serving the earlier version instead of downgrading installed apps |
| [Pre-review checks](https://support.google.com/googleplay/android-developer/answer/14807773?hl=en) | Automated review-preparation evidence and its limits |
| [Prepare and roll out a release](https://support.google.com/googleplay/android-developer/answer/9859348?hl=en) | Release notes, review prerequisites and rollout workflow |
| [Create and set up an app](https://support.google.com/googleplay/android-developer/answer/9859152?hl=en) | First console app creation, metadata limits and package name |
| [Preview assets](https://support.google.com/googleplay/android-developer/answer/9866151?hl=en) | Icons, screenshots, feature graphics, videos and form-factor rules |
| [Console Asset Library](https://support.google.com/googleplay/android-developer/answer/16386748?hl=en) | Real console media for reuse, experiments and events, with no made-up ordinary Publisher placement APIs |
| [App pricing](https://support.google.com/googleplay/android-developer/answer/6334373?hl=en) | Free-to-paid limit, regional pricing and the explicit notice retiring pricing templates |
| [One-time product upsert](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.onetimeproducts/patch) | Real allowMissing, updateMask and regions version, and the product graph |
| [Option state actions](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.onetimeproducts.purchaseOptions/batchUpdateStates) | Purchase-option activation and deactivation, and the real state-action path |
| [Version the app](https://developer.android.com/studio/publish/versioning) | VersionName/versionCode behavior and the Play maximum |
| [Sign the app](https://developer.android.com/studio/publish/app-signing) | Upload key, app signing key, Play App Signing |
| [Build app bundles](https://developer.android.com/build/building-cmdline) | Gradle command-line build and release output |
| [Gradle project properties](https://docs.gradle.org/current/userguide/build_environment.html#sec:project_properties) and [Provider.get](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html#get()) | Explicit -P inputs, and failure when a required provider has no value. Rechecked on 2026-11-05 for the build example. |
| [Target API requirements](https://support.google.com/googleplay/android-developer/answer/11926878?hl=en) | Current deadlines that depend on the release |
| [16 KB page-size support](https://developer.android.com/guide/practices/page-sizes) | Native library compatibility and testing |
| [Personal-account testing](https://support.google.com/googleplay/android-developer/answer/14151465?hl=en) | Closed-test threshold and production access |
| [Billing integration](https://developer.android.com/google/play/billing/integrate) | Product details, pending purchases, fulfillment and acknowledgment |
| [Billing support timeline](https://developer.android.com/google/play/billing/deprecation-faq) | Current client deadlines, the ended version-7 extension and the supported 8/9 timeline |
| [RevenueCat purchase completion](https://www.revenuecat.com/docs/getting-started/making-purchases) and [non-subscriptions](https://www.revenuecat.com/docs/platform-resources/non-subscriptions) | Automatic acknowledgment and consumption in the standard SDK, compared with consumable fulfillment and matching that the app owns. Rechecked on 2026-11-05. |
| [Subscription lifecycle](https://developer.android.com/google/play/billing/lifecycle/subscriptions) | State changes and replacement behavior |
| [One-time product lifecycle](https://developer.android.com/google/play/billing/lifecycle/one-time) | Pending and completed one-time purchases and entitlement |
| [Real-time notifications](https://developer.android.com/google/play/billing/rtdn-reference) | Notification types and matching against purchase state |
| [Data safety](https://support.google.com/googleplay/android-developer/answer/10787469?hl=en) | Required factual declarations and SDK responsibility |
| [Store listing guidance](https://play.google.com/console/about/storelistings/) | Listing messages, localization and experiments |
| [Listing best practices](https://support.google.com/googleplay/android-developer/answer/13393723?hl=en) | Accurate titles and descriptions, messages that support each other and compliant visual and copy choices |
| [Metadata policy](https://support.google.com/googleplay/android-developer/answer/9898842) | Banned identity badges, keyword repetition, deceptive claims and public-content rules |
| [Discovery and ranking](https://support.google.com/googleplay/android-developer/answer/9958766) | Metadata, relevance, quality and user-response factors, with no fixed keyword-weight promises |
| [Current Policy Center](https://play.google/developer-content-policy/) | Which policy family applies, and the real conditional program, permission and content requirements |
| [AI-generated content](https://support.google.com/googleplay/android-developer/answer/13985936) | Safeguards for generated content and the in-app reporting requirement |

The official Publisher Discovery contract was studied as research material. This skill explains its resource families, how requests work and the workflow in Markdown. It does not keep generated API data or a query tool. Reporting, Integrity, Pub/Sub, Firebase and client Billing are separate service contracts.

Known console-only areas include first app creation, category and tags, the owner's legal and account actions, and app-specific declaration, review and publishing tasks that the chosen API does not offer. The agent does those console steps in the owner's signed-in browser when browser use is authorized for the task, and otherwise records them as exact owner handoffs. Data safety is present in this researched Publisher contract, so do not label it as entirely console-only. Provider schemas and UI features can change separately.

## Coverage and interpretation

The current Discovery revision is **20261118** with 149 operations, checked on 2026-11-18. It includes the `purchases.subscriptionsv2` customer operations `schedulePlanTransition`, `cancelPlanTransition`, `activateOfferTargeting` and `deactivateOfferTargeting`. Their request models were read on 2026-11-18, including the definite (not cancelable) and tentative (cancelable) plan transition modes. The hand-written [functional map](api-coverage.md) covers its resource families, including app-store-hosted review and catalog operations. That special program is not ordinary Play app creation or a general policy-review API. It needs eligible access and the real host and app context.

The current AppDetails, Listing and TrackRelease fields, image types and AI upload attestation, upload size and protocols, Data safety CSV request, commit conflict behavior and monetization input, output and state models were read directly. Repeated catalog structures, subscriber-group prices and app distribution each change within a different scope. You cannot set an output state through a generic product PATCH.

The app-pricing help still has some former template instructions below a clear retirement notice. Use the explicit retirement notice and the current per-product route. General asset validity, special device rules and newer console-only media types also each need their own scope, not one assumed limit for everything.

Using the title and short description close to their full length is the owner's preference when it adds meaning. It does not prove a ranking bonus for character count or a keyword-density formula. The official metadata and discovery guidance supports relevant, accurate, readable language, quality and measurement. Public listing rules apply regardless of the app's age rating and across all translations.

No raw Discovery data, generated endpoint catalog, runtime client or scheduled refresh is shipped. Reading schemas and examples, and running contributor checks, do not prove that a real app, account, payment, review or rollout was tried.

## Professional foundation and evidence scope

Reviewed on 2026-11-05. [Site Reliability Engineering: Release Engineering](https://sre.google/sre-book/release-engineering/) supports the wider artifact and release discipline. Dunford's [Obviously Awesome](https://www.aprildunford.com/books) is further reading on positioning, with the clear limit that it is written for a B2B context. The official Publisher, Billing and policy documents are the rules for real Google operations and eligibility.

Stored content is updated only when the user asks for a revision. There is no automatic source collector or refresh process.

## First-release and declaration sequence

Checked **2026-11-05** against [release preparation](https://support.google.com/googleplay/android-developer/answer/9859348?hl=en),
[App content](https://support.google.com/googleplay/android-developer/answer/9859455?hl=en) and
[publishing statuses](https://support.google.com/googleplay/android-developer/answer/9859751?hl=en).
These separate dashboard setup, production draft confirmation, submission and public availability.
The draft-only API error and the child and parent save behavior are workflow problems we observed,
not new API fields or a promise that future Console labels stay the same. These checks did not send
a new app or release.

[Firebase collection controls](https://firebase.google.com/docs/analytics/android/configure-data-collection)
and the final artifact and SDK setup decide how to investigate identifier use. Contains ads,
Advertising ID purposes, collection consent, IARC results and intended audience stay separate
facts. A manifest declaration, or an SDK that starts out disabled, is not enough for all those answers.

## Recheck on 2026-11-18

- [Publisher Discovery](https://androidpublisher.googleapis.com/$discovery/rest?version=v3) revision 20261118: `edits.commit` still defaults `changesInReviewBehavior` to `CANCEL_IN_REVIEW_AND_SUBMIT` and offers `ERROR_IF_IN_REVIEW`. `edits.images.upload` still accepts the eight listed image types, the optional `aiGeneratedState` attestation and a 15,728,640-byte upload limit.
- [Target API requirements](https://support.google.com/googleplay/android-developer/answer/11926878?hl=en): mobile API 36, Wear OS API 35, Automotive API 35 and XR API 34 by August 31, 2026, TV API 34 since August 31, 2025, with the November 1, 2026 extension date.
- [Billing support timeline](https://developer.android.com/google/play/billing/deprecation-faq): version 7 ended August 31, 2026 with a November 1, 2026 extension. Version 8 runs to August 31, 2027 (extension November 1, 2027) and version 9 to August 31, 2028 (extension November 1, 2028).
- The rule for customer-facing copy (no story of how it was made and no AI or tool mentions in listing text, release notes or captions, with required disclosures kept in declaration surfaces) is an owner content convention, not a Google requirement.
- [Personal-account testing](https://support.google.com/googleplay/android-developer/answer/14151465?hl=en): personal developer accounts created after November 13, 2023 must run a closed test with at least 12 testers opted in for at least 14 days in a row, then use Apply for production on the Play Console Dashboard. Opting out and later opting in again restarts the count of days in a row.
- Publisher Discovery revision 20261118 models: `SubscriptionListing.description` up to 200 characters with at most four benefits, `OneTimeProductListing` title up to 55 and description up to 200 characters, auto-renewing grace from P0D to 30 days or the billing period, whichever is shorter, account hold from P0D to P60D and their sum from P30D to P60D.

## Recheck on 2026-11-24

- [Set up your app's prices](https://support.google.com/googleplay/android-developer/answer/6334373?hl=en): "You can change your app from paid to free" and "Once your app has been offered for free, the app can't be changed to paid". Console behavior checked on 2026-11-24: the lock applies at the first Send changes for review of an app that was never published, and it stays after Remove changes.
- [Delete an app](https://support.google.com/googleplay/android-developer/answer/16483176?hl=en): owner only, unpublished, no changes in review, fewer than 1000 active devices, not rejected, blocked or suspended, and monetized apps only with zero installs ever. Advanced settings → App availability → Delete app, with the registration transaction ID and the package name. Recovery is possible within seven days. With zero installs ever, the package name is freed for anyone, and any installs keep it blocked forever. Console behavior checked on 2026-11-24: Create app reports the name as already in use during the seven days.
- Google sign-in with Chrome 158, checked on 2026-11-24: it refuses a Chrome launched by Playwright ("This browser or app may not be secure") and accepts a Chrome launched normally with `--remote-debugging-port` and a separate `--user-data-dir`, attached with `connect_over_cdp`.
