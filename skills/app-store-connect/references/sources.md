# Sources and verified limitations

Research date: **2026-11-05**. Official requirements depend on the current platform, SDK, account permissions, region, and review state. Marketing guidance is a suggested process, not a promise of approval or ranking.

| Source | Use |
| --- | --- |
| [App Store Connect API](https://developer.apple.com/documentation/appstoreconnectapi) | Resource model, operation guidance, current release notes |
| [Official OpenAPI archive](https://developer.apple.com/sample-code/app-store-connect/app-store-connect-openapi-specification.zip) | Full researched 4.6 list of operations and schemas |
| [API token guide](https://developer.apple.com/documentation/appstoreconnectapi/generating-tokens-for-api-requests) | Team and individual authentication types |
| [Add a new app](https://developer.apple.com/help/app-store-connect/create-an-app-record/add-a-new-app) | Console workflow for the first app record |
| [Upload builds](https://developer.apple.com/help/app-store-connect/manage-builds/upload-builds) | Supported Xcode, Transporter, and command-line upload paths |
| [Upcoming requirements](https://developer.apple.com/news/upcoming-requirements/) | SDK/toolchain and submission deadlines |
| [Platform version information](https://developer.apple.com/help/app-store-connect/reference/app-information/platform-version-information/) | Field meanings, keyword byte limit, URLs and release notes |
| [App information](https://developer.apple.com/help/app-store-connect/reference/app-information/app-information/) | Name, subtitle, categories and app-level fields |
| [Product page guidance](https://developer.apple.com/app-store/product-page/) | Accurate product positioning, screenshots, localization and discovery |
| [App Store search](https://developer.apple.com/app-store/search/) | Text relevance, categories, keyword choice, promotional text that does not affect ranking and measured search results |
| [Manage app tags](https://developer.apple.com/help/app-store-connect/manage-app-information/manage-app-tags/) | Generated tags and allowed management |
| [Screenshot specifications](https://developer.apple.com/help/app-store-connect/reference/app-information/screenshot-specifications/) | Display slots, Duo condition, sizes, formats, and image counts |
| [App preview specifications](https://developer.apple.com/help/app-store-connect/reference/app-information/app-preview-specifications/) | Current video requirements |
| [App Asset Library](https://developer.apple.com/documentation/appstoreconnectapi/app-asset-library) | Current reusable media and placement model that replaces deprecated public screenshot/preview sets |
| [Discovering asset specifications](https://developer.apple.com/documentation/appstoreconnectapi/discovering-asset-specifications) | Dynamic device groups and specifications, six reference-data arrays, categories and limits for each feature |
| [Image upload and management](https://developer.apple.com/documentation/appstoreconnectapi/uploading-and-managing-image-assets) | Exact reserve/transfer/commit states, no checksum attribute, bytes that cannot change and deletion rules tied to placements |
| [Video upload and management](https://developer.apple.com/documentation/appstoreconnectapi/uploading-and-managing-video-assets) | Video validation, preview frame and effects on shared placements |
| [Placement and ordering](https://developer.apple.com/documentation/appstoreconnectapi/placing-assets-on-your-app-store-surfaces) | Exact type/group/asset/target relationships, placements that cannot change and group ordering |
| [Dedicated asset uploads](https://developer.apple.com/documentation/appstoreconnectapi/uploading-assets-to-app-store-connect) | Upload and checksum contracts for attachments and a clear notice that old media is deprecated |
| [Set app price](https://developer.apple.com/help/app-store-connect/manage-app-pricing/set-a-price/) | Base-country equalization, manual overrides and the deletion of scheduled prices |
| [App availability](https://developer.apple.com/help/app-store-connect/manage-your-apps-availability/manage-availability-for-your-app-on-the-app-store) | Sale countries, preorder and real availability |
| [Set tax category](https://developer.apple.com/help/app-store-connect/manage-app-information/set-a-tax-category) | Real console workflow for category, subcategory and attributes |
| [App Privacy](https://developer.apple.com/help/app-store-connect/manage-app-information/manage-app-privacy) | Questionnaire publishing, separate from privacy URLs, and policy requirements for all apps |
| [IAP metadata versions](https://developer.apple.com/documentation/appstoreconnectapi/migrating-in-app-purchase-metadata-to-v2) | Current localizations and public images linked to versions, and private review screenshots linked to the parent |
| [IAP information](https://developer.apple.com/help/app-store-connect/reference/in-app-purchases-and-subscriptions/in-app-purchase-information) | Internal and public names, localized display and description limits and review fields |
| [Promoted IAP](https://developer.apple.com/app-store/promoting-in-app-purchases/) | Image and copy for promotion and discovery limits by product type |
| [Version-based subscription review](https://developer.apple.com/documentation/appstoreconnectapi/submitting-subscriptions-and-subscription-groups-for-app-review) | Current version resources and the first-submission rule |
| [StoreKit](https://developer.apple.com/documentation/storekit) | Client purchase and transaction lifecycle |
| [RevenueCat purchase completion](https://www.revenuecat.com/docs/getting-started/making-purchases) and [non-subscriptions](https://www.revenuecat.com/docs/platform-resources/non-subscriptions) | The standard SDK finishes store transactions automatically, while the app owns consumable delivery and checking it. Rechecked on 2026-11-05. |
| [App Store Server API](https://developer.apple.com/documentation/appstoreserverapi) | Backend transaction and subscription operations, a separate API |
| [Server Notifications](https://developer.apple.com/documentation/appstoreservernotifications) | Signed notifications and lifecycle events, a separate contract |
| [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) | Review, privacy, payment and metadata policy |
| [Reply to App Review](https://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/reply-to-app-review-messages/) | Real console messages for owner roles and metadata fixes on the same build |
| [Submission/version statuses](https://developer.apple.com/help/app-store-connect/reference/app-information/app-and-submission-statuses) | Different meanings for version, review and distribution |
| [Phased release](https://developer.apple.com/help/app-store-connect/update-your-app/release-a-version-update-in-phases) | Seven-day automatic-update schedule, manual-download exception and total pause allowance |

The official OpenAPI 4.6 contract was read as research material. The skill stores what was learned as steps in Markdown, not as a generated schema dump. The current operation documentation decides how a real API call works. Content maintenance is a writing task the user asks for.

Known limits: the current app collection cannot create the first app record, account, legal, privacy and tax actions keep their documented console steps and the first combined subscription submission needs its real console flow. Current public media uses Asset Library reference data with dynamic placement groups. A missing Duo value in a deprecated screenshot enum does not show a gap in that newer API. Look up the real supported specification and group before you decide a console handoff is needed.

This snapshot does not include the full signed payload schemas of the separate App Store Server API. Fetch those official contracts when you build a server directly. Connect webhooks, purchase notifications and App Review or customer-review messages are separate. There is no researched general API to post App Review messages or any legal statements.

## Coverage and interpretation

The [functional map](api-coverage.md) covers the current OpenAPI resource families. [Core fields](store-fields-and-localizations.md), [commercial configuration](pricing-and-availability.md), media and review references explain the real operations in order. This is a hand-written procedure, not a word-for-word manual, a generated endpoint catalog or a claim that it ran on a live account. The exact current operation still decides a real request's nested limits, permissions and state eligibility.

The official Markdown versions of the Asset Library articles were read directly where the browser reader showed only a JavaScript shell. Current core create and update models, review relationships and states, pricing and availability versions, who owns product localizations and media commit fields were checked against the temporary downloaded OpenAPI research material. No raw contract or research downloader is shipped.

Using the name and subtitle close to their limit is the owner's stated preference when it stays meaningful. It is not an Apple requirement or proof that each character adds ranking weight. The search documentation supports choosing terms for relevance, avoiding repeats and the separate role of promotional text. Exact ranking weights, a fixed keyword density and guaranteed growth are not established. The 100-byte keyword limit in the detailed help wins over the looser character wording on the marketing page, to keep checks safe.

Policy coverage points to all five guideline families and the relevant conditional branches. It does not claim every regional exception applies to every app, replace current owner facts or certify runtime behavior nobody ran. Changes to the real public price, countries, groups of subscribers and release state stay separate operations that each need permission.

## Professional foundation and evidence scope

Reviewed on 2026-11-05. [Site Reliability Engineering](https://sre.google/sre-book/), edited by Betsy Beyer, Chris Jones, Jennifer Petoff and Niall Richard Murphy, gives professional background on releases and monitoring. Apple's own documentation decides API and review requirements. Dunford's [Obviously Awesome](https://www.aprildunford.com/books) is further reading on product positioning, checked through the author's description. No source guarantees approval or search ranking.

Stored content is updated only when the user asks for a revision. There is no automated source collector or refresh mechanism.

## Operational procedure checks

Checked **2026-11-05** against Apple OpenAPI **4.6**, the installed Xcode **27.2** help and an observed
release workflow. These checks did not submit or cancel a release.

- [Cloud-managed certificates](https://developer.apple.com/help/account/certificates/cloud-managed-certificates/) and [UserRole](https://developer.apple.com/documentation/appstoreconnectapi/userrole): metadata roles and cloud-signing permission are separate. Check the real credential in use.
- Installed `xcodebuild -help`: authentication-key overrides, provisioning updates and export options decide whether the set-up Xcode account or the supplied key is used. Installed `altool --help` confirms the example's hyphenated flags and key lookup in the original folder.
- [Official OpenAPI](https://developer.apple.com/sample-code/app-store-connect/app-store-connect-openapi-specification.zip): checked cancellation and update, review-item target relationships, the placement-ordering request and app-scoped build-upload listing. No general App Review message route was there.
- Installed `xcrun simctl help io`: display enumeration and choosing a display for a screenshot are supported. Display numbers and the observed Duo grouping are examples from one run, not fixed device identifiers. Current reference data is still the source of truth.

The worked media and submission steps describe dependencies and how to match up states. They do not
claim that all future accounts, SDK versions or first-product submission states behave the same way.

## Recheck on 2026-11-18

- The [official OpenAPI archive](https://developer.apple.com/sample-code/app-store-connect/app-store-connect-openapi-specification.zip) still reports version 4.6. The app, version, version-localization, AppInfo-localization, Asset Library image/placement, review-submission, subscription-price and IAP v2 create and update models used in this skill matched the stored descriptions.
- The [screenshot specification](https://developer.apple.com/help/app-store-connect/reference/app-information/screenshot-specifications/) still lists the Duo outer and inner sizes, the April 2027 iOS 27.1 SDK condition, the medium Dynamic Island required slot, 13-inch iPad sizes and 1–10 opaque JPEG/PNG screenshots per size.
- The rule for customer-facing copy (no description of how it was made and no AI or tool mentions in listing text, release notes or captions, with required disclosures kept in declaration screens) is the owner's content rule, not an Apple requirement.
- The [screenshot specification](https://developer.apple.com/help/app-store-connect/reference/app-information/screenshot-specifications/) also marks iPhone with Face ID large display (1284×2778 or 1242×2688) as required when the app runs on iPhone and no Dynamic Island large display (1260×2736, 1290×2796 or 1320×2868) screenshots are given. Each large family is scaled from the other when one is left out.
- [Upcoming requirements](https://developer.apple.com/news/upcoming-requirements/): Xcode 26 with the iOS/iPadOS/tvOS/visionOS/watchOS 26 SDK since April 28, 2026, and an iOS 13 minimum deployment target for iOS/iPadOS uploads since September 9, 2026. The listed SDK condition does not name a macOS SDK.

Checked **2026-11-18**. The [October 5, 2026 iPhone Duo announcement](https://developer.apple.com/news/?id=kkphp5qo) says that starting April 2027 any apps or games submitted need iPhone Duo screenshots. The [screenshot specifications](https://developer.apple.com/help/app-store-connect/reference/app-information/screenshot-specifications/) say the screenshots are required for any app using the iOS 27.1 SDK or later and list 1398×2034 outer and 2007×2853 inner sizes in both orientations. The skill prepares Duo screenshots for every iPhone submission to meet both. The [in-app purchase information reference](https://developer.apple.com/help/app-store-connect/reference/in-app-purchases-and-subscriptions/in-app-purchase-information) confirms a display name of 2 to 30 characters, a description of at most 45 and a reference name of at most 64.
