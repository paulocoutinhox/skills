# Sources and limitations

Verified: **2026-11-05**. Recheck current method behavior, target SDK/Billing deadlines, account requirements, and specialized device rules at release time.

| Source | Coverage |
| --- | --- |
| [Android Publisher Discovery](https://androidpublisher.googleapis.com/$discovery/rest?version=v3) | All 145 researched Publisher v3 operations and full structural models |
| [Android Publisher reference](https://developers.google.com/android-publisher/api-ref/rest) | Endpoint behavior, constraints and examples |
| [API getting started](https://developers.google.com/android-publisher/getting_started) | Enable API, OAuth/service-account setup and current account model |
| [Edits workflow](https://developers.google.com/android-publisher/edits) | Edit sessions, uploads and transaction semantics |
| [Review and managed publishing](https://support.google.com/googleplay/android-developer/answer/9859654?hl=en) | Review handoffs, first-release limitation and immediate-effect exceptions |
| [Current edit commit](https://developers.google.com/android-publisher/api-ref/rest/v3/edits/commit) | Empty-body commit, existing-review cancellation default and ERROR_IF_IN_REVIEW behavior |
| [Publishing statuses](https://support.google.com/googleplay/android-developer/answer/9859751?hl=en) | Separate app/update/item state and rejection/removal/suspension |
| [Review preparation](https://support.google.com/googleplay/android-developer/answer/9859455?hl=en) | Actual App content, global non-PDF privacy policy, ads and restricted-access instructions |
| [Eligible full-release halt](https://support.google.com/googleplay/android-developer/answer/16285429?hl=en) | Publisher/console support, first/internal exclusions and prior-version serving rather than installed-app downgrade |
| [Pre-review checks](https://support.google.com/googleplay/android-developer/answer/14807773?hl=en) | Automated review-preparation evidence and its limits |
| [Prepare and roll out a release](https://support.google.com/googleplay/android-developer/answer/9859348?hl=en) | Release notes, review prerequisites and rollout workflow |
| [Create and set up an app](https://support.google.com/googleplay/android-developer/answer/9859152?hl=en) | Initial console app creation, metadata limits and package identity |
| [Preview assets](https://support.google.com/googleplay/android-developer/answer/9866151?hl=en) | Icons, screenshots, feature graphics, videos and form-factor rules |
| [Console Asset Library](https://support.google.com/googleplay/android-developer/answer/16386748?hl=en) | Actual console reuse/experiment/event media without invented ordinary Publisher placement APIs |
| [App pricing](https://support.google.com/googleplay/android-developer/answer/6334373?hl=en) | Free-to-paid restriction, regional pricing and explicit pricing-template retirement notice |
| [One-time product upsert](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.onetimeproducts/patch) | Actual allowMissing/updateMask/regions-version and product graph |
| [Option state actions](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.onetimeproducts.purchaseOptions/batchUpdateStates) | Purchase-option activation/deactivation and actual state-action path |
| [Version the app](https://developer.android.com/studio/publish/versioning) | VersionName/versionCode behavior and Play maximum |
| [Sign the app](https://developer.android.com/studio/publish/app-signing) | Upload key, app signing key, Play App Signing |
| [Build app bundles](https://developer.android.com/build/building-cmdline) | Gradle command-line build and release output |
| [Gradle project properties](https://docs.gradle.org/current/userguide/build_environment.html#sec:project_properties) and [Provider.get](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html#get()) | Explicit -P inputs and failure when a required provider has no value. Rechecked on 2026-11-05 for the build example. |
| [Target API requirements](https://support.google.com/googleplay/android-developer/answer/11926878?hl=en) | Current release-dependent deadlines |
| [16 KB page-size support](https://developer.android.com/guide/practices/page-sizes) | Native library compatibility and testing |
| [Personal-account testing](https://support.google.com/googleplay/android-developer/answer/14151465?hl=en) | Closed-test threshold and production access |
| [Billing integration](https://developer.android.com/google/play/billing/integrate) | Product details, pending purchases, fulfillment and acknowledgment |
| [Billing support timeline](https://developer.android.com/google/play/billing/deprecation-faq) | Current client deadlines, expired version-7 extension and supported 8/9 timeline |
| [RevenueCat purchase completion](https://www.revenuecat.com/docs/getting-started/making-purchases) and [non-subscriptions](https://www.revenuecat.com/docs/platform-resources/non-subscriptions) | Standard SDK automatic acknowledgment/consumption versus application-owned consumable fulfillment and reconciliation. Rechecked on 2026-11-05. |
| [Subscription lifecycle](https://developer.android.com/google/play/billing/lifecycle/subscriptions) | State transitions and replacement behavior |
| [One-time product lifecycle](https://developer.android.com/google/play/billing/lifecycle/one-time) | Pending/completed one-time purchases and entitlement |
| [Real-time notifications](https://developer.android.com/google/play/billing/rtdn-reference) | Notification types and reconciliation |
| [Data safety](https://support.google.com/googleplay/android-developer/answer/10787469?hl=en) | Required factual declarations and SDK responsibility |
| [Store listing guidance](https://play.google.com/console/about/storelistings/) | Listing communication, localization and experimentation |
| [Listing best practices](https://support.google.com/googleplay/android-developer/answer/13393723?hl=en) | Accurate titles/descriptions, complementing messages and compliant visual/copy choices |
| [Metadata policy](https://support.google.com/googleplay/android-developer/answer/9898842) | Prohibited identity badges, keyword repetition, deceptive claims and public-content requirements |
| [Discovery and ranking](https://support.google.com/googleplay/android-developer/answer/9958766) | Metadata/relevance/quality/user-response factors, without fixed keyword-weight promises |
| [Current Policy Center](https://play.google/developer-content-policy/) | Policy-family routing and actual conditional program/permission/content requirements |
| [AI-generated content](https://support.google.com/googleplay/android-developer/answer/13985936) | Generated-content safeguards and in-app reporting requirement |

The official Publisher Discovery contract was inspected as research material. This skill explains its resource families, request semantics and workflow in Markdown. It does not maintain generated API data or a query tool. Reporting, Integrity, Pub/Sub, Firebase and client Billing are separate service contracts.

Known console boundaries include initial application creation, category/tags, owner legal/account actions, and app-specific declarations/review/publishing tasks not exposed by the selected API. Data safety is specifically present in this researched Publisher contract and must not be incorrectly labeled entirely console-only. Provider schemas and UI capabilities can change independently.

## Coverage and interpretation

The current Discovery revision inspected is **20261105**, containing the researched 145 operations. The manually authored [functional map](api-coverage.md) covers its resource families, including app-store-hosted review/catalog operations. That specialized program is not ordinary Play application creation or a generic policy-review API. Eligible access and actual host/app context are prerequisites.

Current AppDetails/Listing/TrackRelease fields, image types/AI upload attestation, upload size/protocols, Data safety CSV request, commit conflict behavior and monetization input/output/state models were inspected directly. Repeated catalog structures, price cohorts and app distribution have different mutation scopes. An output state cannot be assigned through a generic product PATCH.

The app-pricing help retains some former template instructions below a clear retirement notice. Use the explicit retirement/current per-product route. General asset validity, specialized device rules and newer console-only media types likewise need their own scope rather than a single assumed universal limit.

Near-capacity title/short-description use is the owner's preference when meaningful. It does not establish a character-count ranking bonus or a keyword-density formula. Official metadata/discovery guidance supports relevant, accurate, readable language, quality and measurement. Public listing rules apply independently of the app's age rating and across all translations.

No raw Discovery data, generated endpoint catalog, runtime client or scheduled refresh is distributed. Schema/example inspection and contributor checks do not prove that a real app, account, payment, review or rollout was exercised.

## Professional foundation and evidence scope

Reviewed for this revision: 2026-11-05. [Site Reliability Engineering: Release Engineering](https://sre.google/sre-book/release-engineering/) supports the broader artifact/release discipline. Dunford's [Obviously Awesome](https://www.aprildunford.com/books) is positioning further reading with an explicit B2B-context limitation. Official Publisher/Billing/policy documents govern actual Google operations and eligibility.

Stored content is maintained only when the user requests a revision. There is no automated source collector or refresh mechanism.

## First-release and declaration sequence

Checked **2026-11-05** against [release preparation](https://support.google.com/googleplay/android-developer/answer/9859348?hl=en),
[App content](https://support.google.com/googleplay/android-developer/answer/9859455?hl=en) and
[publishing statuses](https://support.google.com/googleplay/android-developer/answer/9859751?hl=en).
These distinguish dashboard setup, production draft confirmation, submission and public availability.
The draft-only API error and child/parent-save behavior are observed workflow diagnostics, not new
API fields or a guarantee of identical future Console labels. No new app/release was sent while
writing this revision.

[Firebase collection controls](https://firebase.google.com/docs/analytics/android/configure-data-collection)
and the final artifact/SDK configuration govern identifier-use investigation. Contains ads,
Advertising ID purposes, collection consent, IARC outcomes and intended audience remain independent
facts. A manifest declaration or initially disabled SDK is insufficient for all those answers.
