# Sources and verified limitations

Research date: **2026-11-05**. Official requirements depend on current platform, SDK, account permissions, region, and review state. Marketing guidance is a recommended process, not an approval or ranking guarantee.

| Source | Use |
| --- | --- |
| [App Store Connect API](https://developer.apple.com/documentation/appstoreconnectapi) | Resource model, operation guidance, current release notes |
| [Official OpenAPI archive](https://developer.apple.com/sample-code/app-store-connect/app-store-connect-openapi-specification.zip) | Complete researched 4.6 structural operation and schema inventory |
| [API token guide](https://developer.apple.com/documentation/appstoreconnectapi/generating-tokens-for-api-requests) | Team versus individual authentication profiles |
| [Add a new app](https://developer.apple.com/help/app-store-connect/create-an-app-record/add-a-new-app) | Initial app record console workflow |
| [Upload builds](https://developer.apple.com/help/app-store-connect/manage-builds/upload-builds) | Supported Xcode, Transporter, and command-line upload paths |
| [Upcoming requirements](https://developer.apple.com/news/upcoming-requirements/) | SDK/toolchain and submission deadlines |
| [Platform version information](https://developer.apple.com/help/app-store-connect/reference/app-information/platform-version-information/) | Field meanings, keyword byte limit, URLs and release notes |
| [App information](https://developer.apple.com/help/app-store-connect/reference/app-information/app-information/) | Name, subtitle, categories and app-level fields |
| [Product page guidance](https://developer.apple.com/app-store/product-page/) | Accurate product positioning, screenshots, localization and discovery |
| [App Store search](https://developer.apple.com/app-store/search/) | Text relevance, categories, keyword selection, non-ranking promotional text and measured search outcomes |
| [Manage app tags](https://developer.apple.com/help/app-store-connect/manage-app-information/manage-app-tags/) | Generated tags and permitted management |
| [Screenshot specifications](https://developer.apple.com/help/app-store-connect/reference/app-information/screenshot-specifications/) | Display slots, Duo condition, sizes, formats, and image counts |
| [App preview specifications](https://developer.apple.com/help/app-store-connect/reference/app-information/app-preview-specifications/) | Current video-specific requirements |
| [App Asset Library](https://developer.apple.com/documentation/appstoreconnectapi/app-asset-library) | Current reusable media/placement model replacing deprecated public screenshot/preview sets |
| [Discovering asset specifications](https://developer.apple.com/documentation/appstoreconnectapi/discovering-asset-specifications) | Dynamic device groups/specifications, six reference-data arrays, categories and per-feature limits |
| [Image upload and management](https://developer.apple.com/documentation/appstoreconnectapi/uploading-and-managing-image-assets) | Exact reserve/transfer/commit states, no checksum attribute, immutable bytes and placement-aware deletion |
| [Video upload and management](https://developer.apple.com/documentation/appstoreconnectapi/uploading-and-managing-video-assets) | Video validation, preview frame and shared-placement effects |
| [Placement and ordering](https://developer.apple.com/documentation/appstoreconnectapi/placing-assets-on-your-app-store-surfaces) | Exact type/group/asset/target relationships, immutable placements and group ordering |
| [Dedicated asset uploads](https://developer.apple.com/documentation/appstoreconnectapi/uploading-assets-to-app-store-connect) | Attachment-specific upload/checksum contracts and explicit old-media deprecation notice |
| [Set app price](https://developer.apple.com/help/app-store-connect/manage-app-pricing/set-a-price/) | Base-country equalization, manual overrides and scheduled-price deletion consequences |
| [App availability](https://developer.apple.com/help/app-store-connect/manage-your-apps-availability/manage-availability-for-your-app-on-the-app-store) | Sale countries, preorder and actual availability |
| [Set tax category](https://developer.apple.com/help/app-store-connect/manage-app-information/set-a-tax-category) | Real console category/subcategory/attribute workflow |
| [App Privacy](https://developer.apple.com/help/app-store-connect/manage-app-information/manage-app-privacy) | Questionnaire publication distinct from privacy URLs and all-app policy requirements |
| [IAP metadata versions](https://developer.apple.com/documentation/appstoreconnectapi/migrating-in-app-purchase-metadata-to-v2) | Current version-linked localizations/public images and parent-linked private review screenshots |
| [IAP information](https://developer.apple.com/help/app-store-connect/reference/in-app-purchases-and-subscriptions/in-app-purchase-information) | Internal versus public names, localized display/description limits and review fields |
| [Promoted IAP](https://developer.apple.com/app-store/promoting-in-app-purchases/) | Promotion-specific image/copy and product-type discovery limits |
| [Version-based subscription review](https://developer.apple.com/documentation/appstoreconnectapi/submitting-subscriptions-and-subscription-groups-for-app-review) | Current version resources and first-submission constraint |
| [StoreKit](https://developer.apple.com/documentation/storekit) | Client purchase and transaction lifecycle |
| [RevenueCat purchase completion](https://www.revenuecat.com/docs/getting-started/making-purchases) and [non-subscriptions](https://www.revenuecat.com/docs/platform-resources/non-subscriptions) | Standard SDK automatic store completion versus application-owned consumable fulfillment and reconciliation. Rechecked on 2026-11-05. |
| [App Store Server API](https://developer.apple.com/documentation/appstoreserverapi) | Backend transaction and subscription operations, separate API |
| [Server Notifications](https://developer.apple.com/documentation/appstoreservernotifications) | Signed notifications and lifecycle events, separate contract |
| [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) | Review, privacy, payment and metadata policy |
| [Reply to App Review](https://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/reply-to-app-review-messages/) | Actual owner-role console correspondence and same-build metadata remediation |
| [Submission/version statuses](https://developer.apple.com/help/app-store-connect/reference/app-information/app-and-submission-statuses) | Different version, review and distribution meanings |
| [Phased release](https://developer.apple.com/help/app-store-connect/update-your-app/release-a-version-update-in-phases) | Seven-day automatic-update schedule, manual-download exception and total pause allowance |

The official OpenAPI 4.6 contract was inspected as research material. The skill stores the resulting procedural knowledge in Markdown, not a generated schema dump. Current operation documentation governs an actual API call. Content maintenance is a user-requested editorial action.

Known boundaries: the current app collection cannot create the initial app record, account/legal/privacy/tax actions retain documented console steps and first combined subscription submission needs its actual console flow. Current public media uses Asset Library reference data with dynamic placement groups. A missing Duo value in a deprecated screenshot enum is not evidence of a gap in that newer API. Query the actual supported specification/group before concluding a console handoff is required.

This snapshot does not include the separate App Store Server API's full signed payload schemas. Fetch those official contracts for direct server implementation. Connect webhooks, purchase notifications and App Review/customer-review messages are separate surfaces. There is no researched general API to post App Review correspondence or arbitrary legal attestations.

## Coverage and interpretation

The [functional map](api-coverage.md) accounts for the current OpenAPI resource families. [Core fields](store-fields-and-localizations.md), [commercial configuration](pricing-and-availability.md), media and review references explain actual ordered operations. This is a manually authored procedure, not a verbatim manual, generated endpoint catalog or claim of live account execution. The exact current operation still governs a real request's nested constraints, permissions and state eligibility.

The official Markdown forms of the Asset Library articles were read directly where the browser reader could only show a JavaScript shell. Current core create/update models, review relationships/states, pricing/availability versions, product localization ownership and media commit fields were checked against the downloaded temporary OpenAPI research material. No raw contract or research downloader is distributed.

Near-capacity name/subtitle use is an explicit owner preference when meaningful, not an Apple requirement or evidence of greater ranking weight per character. Search documentation supports relevance-based term selection, nonduplication and the promotional-text distinction. Exact ranking weights, fixed keyword density and guaranteed growth are not established. The 100-byte detailed keyword limit takes precedence over looser marketing-page character wording for conservative validation.

Policy coverage routes all five guideline families and relevant conditional branches. It does not assert every regional exception applies to every app, replace current owner facts or certify unexecuted runtime behavior. Changes to actual public price, countries, subscriber cohorts and release state remain separate authorized operations.

## Professional foundation and evidence scope

Reviewed for this revision: 2026-11-05. [Site Reliability Engineering](https://sre.google/sre-book/), edited by Betsy Beyer, Chris Jones, Jennifer Petoff and Niall Richard Murphy, provides professional release/monitoring context. Apple's own documentation governs API/review requirements. Dunford's [Obviously Awesome](https://www.aprildunford.com/books) is further reading for product positioning, verified through the author description. No source guarantees approval or search ranking.

Stored content is maintained only when the user requests a revision. There is no automated source collector or refresh mechanism.

## Operational procedure checks

Checked **2026-11-05** against Apple OpenAPI **4.6**, installed Xcode **27.2** help and the
previously exercised release workflow. This authoring pass did not submit/cancel another release.

- [Cloud-managed certificates](https://developer.apple.com/help/account/certificates/cloud-managed-certificates/) and [UserRole](https://developer.apple.com/documentation/appstoreconnectapi/userrole): metadata roles and cloud-signing permission are separate capabilities. Inspect the actual selected credential.
- Installed `xcodebuild -help`: authentication-key overrides, provisioning updates and export options govern whether the configured Xcode account or supplied key is used. Installed `altool --help` confirms the example's hyphenated flags and original-directory key lookup.
- [Official OpenAPI](https://developer.apple.com/sample-code/app-store-connect/app-store-connect-openapi-specification.zip): inspected cancellation/update, review-item target relationships, placement-ordering request and app-scoped build-upload listing. No general App Review message route was present.
- Installed `xcrun simctl help io`: display enumeration and explicit screenshot selection are supported. Display numbers and the observed Duo grouping are execution examples, not permanent device identifiers. Current reference data remains authoritative.

The worked media/submission sequences describe dependency and reconciliation decisions. They do not
claim that all future accounts, SDK versions or first-product submission states behave identically.
