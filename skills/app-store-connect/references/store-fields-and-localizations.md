# Store fields, ownership and safe edits

Verified against Apple's OpenAPI **4.6** and current Connect help on **2026-11-05**. This is a field/workflow explanation, not a generated schema catalog. The schemas distinguish create, update and response fields. A field appearing in a response does not make it writable.

## Establish the target graph

Read `GET /v1/apps?filter[bundleId]=<bundle-id>`, then the app's `appInfos`, `appStoreVersions`, builds and relevant localizations. Select by actual platform, version and editable state, not the first returned record. Follow pagination. Preserve the ID for each parent and locale. App ID, bundle ID, SKU, version ID and localization ID have different meanings.

Produce a field inventory before editing: current value, intended value, owning resource, locale/platform, API or console surface, requiredness, editability, verification and owner decision. Use [the release evidence template](../assets/release-evidence.md). Do not replace unknown fields with empty strings. Send only intentional PATCH attributes. A delete is a separate supported operation, not an empty localized value.

## App-level fields

`PATCH /v1/apps/{id}` supports the following researched attributes:

| Fields | Purpose and editing rule |
| --- | --- |
| `primaryLocale` | Default store language. Establish the intended localization and fallback before changing it. |
| `bundleId` | Supported by the update model but constrained by app state. Do not treat uploaded identity as freely renameable. |
| `accessibilityUrl` | Actual public accessibility information. Verify content and reachability. |
| `contentRightsDeclaration` | `DOES_NOT_USE_THIRD_PARTY_CONTENT` or `USES_THIRD_PARTY_CONTENT`, based on actual rights. |
| `subscriptionStatusUrl`, `subscriptionStatusUrlVersion` | Production server-notification destination/version. Use the intended authenticated, monitored receiver. |
| `subscriptionStatusUrlForSandbox`, `subscriptionStatusUrlVersionForSandbox` | Separate sandbox notification destination/version. Do not mix environments. |
| `streamlinedPurchasingEnabled` | A real purchasing-behavior choice. Check feature/account eligibility and customer impact before changing it. |

Response `name`, `sku` and derived status fields are not this model's name-update mechanism. Change localized name through AppInfo localization. Resolve app creation, SKU/platform ownership and any immutable identity changes through the supported console workflow.

## App information and taxonomy

`PATCH /v1/appInfos/{id}` changes category relationships using actual `appCategories` IDs:

- `primaryCategory`, `secondaryCategory`.
- `primarySubcategoryOne`, `primarySubcategoryTwo`.
- `secondarySubcategoryOne`, `secondarySubcategoryTwo`.

Select allowed parents/children from the live hierarchy and the real core use case. Do not populate every optional category. Gaming subcategories apply only to permitted game-category relationships.

Create AppInfo localizations with `POST /v1/appInfoLocalizations`, required `locale`, `name` and the `appInfo` relationship. Edit existing ones with `PATCH /v1/appInfoLocalizations/{id}`:

| Fields | Meaning and constraints |
| --- | --- |
| `name` | App name, at most 30 characters. Use the localized approved brand/purpose pair. |
| `subtitle` | Complementary value statement, at most 30 characters. |
| `privacyPolicyUrl` | Public, accurate policy URL. Required for all apps under the current policy. |
| `privacyChoicesUrl` | Optional actual privacy-choice/deletion/rights surface, not an invented contact page. |
| `privacyPolicyText` | Platform-specific policy text, including the tvOS presentation. Keep it aligned with the public policy. |

Locale is selected when creating the record. Do not send `locale` in a PATCH model that lacks it. App Privacy questionnaire answers are separate from these URLs/text and have a console publishing step.

`appTags` are Apple's generated tags. Read the app's tags and permitted territories, then use supported `visibleInAppStore` updates when appropriate. There is no arbitrary hashtag-create operation.

## Platform version fields

Create `POST /v1/appStoreVersions` with `platform`, `versionString` and the `app` relationship. Supported additional create attributes are `copyright`, `reviewType`, `releaseType`, `earliestReleaseDate` and `usesIdfa`. Optional build/localization linkage follows the exact create schema.

| Attribute | How to decide |
| --- | --- |
| `platform` | Actual `IOS`, `MAC_OS`, `TV_OS` or `VISION_OS` release. Creation-time choice, not a platform-changing PATCH. |
| `versionString` | Marketing version matching the intended release train, separate from the build number. |
| `copyright` | Real owner and year. A store name is not evidence of rights ownership. |
| `reviewType` | `APP_STORE` for ordinary store publication. `NOTARIZATION` is a different eligible distribution route. |
| `releaseType` | `MANUAL`, `AFTER_APPROVAL` or `SCHEDULED`, chosen before submission. |
| `earliestReleaseDate` | Supported timestamp for the selected release strategy. Record time zone and verify territory/preorder rules. |
| `usesIdfa` | Actual advertising-identifier behavior. It does not replace privacy answers or ATT compliance. |
| `downloadable` | Available in the update model and constrained by state. A customer-affecting availability choice, not a generic rollback switch. |

`PATCH /v1/appStoreVersions/{id}` supports the editable attributes above except `platform`, plus documented `build` and `appClipDefaultExperience` relationships. Use the dedicated build relationship when appropriate. Never PATCH `appStoreState`, `appVersionState` or `createdDate` to force approval.

### Version localizations

Create `POST /v1/appStoreVersionLocalizations` with `locale` and `appStoreVersion`. Its text attributes, also editable through `PATCH /v1/appStoreVersionLocalizations/{id}`, are:

| Field | Limit and required intent |
| --- | --- |
| `description` | 4,000 characters. Concrete benefits, shipped capabilities, compatibility and commercial/account conditions. |
| `keywords` | Conservatively 100 UTF-8 bytes including commas, based on detailed help. Complement indexed name/subtitle/category. |
| `promotionalText` | 170 characters. Accurate timely information, independently editable when supported. It is not a search-ranking keyword field. |
| `supportUrl` | Functioning support surface and real contact path. |
| `marketingUrl` | Optional product-specific landing page, truthful and reachable. |
| `whatsNew` | 4,000 characters. Actual changes for this update, with material behavior changes explained. |

The create model can relate `placements`. Manage actual images/videos through [the current Asset Library procedure](screenshots-and-media.md), not an imaginary screenshot attribute in this localization object.

### Worked metadata update

For an existing editable AppInfo localization, `PATCH /v1/appInfoLocalizations/<localization-id>` can carry:

```json
{
  "data": {
    "type": "appInfoLocalizations",
    "id": "<localization-id>",
    "attributes": {
      "name": "Leafnote: Book Notes and Ideas",
      "subtitle": "Save quotes, organize insights"
    }
  }
}
```

This fictional example assumes the app really provides those features. The identifiers are placeholders. Read the result back, verify locale/parent/state and inspect storefront preview. A description change belongs to the version-localization endpoint, not this request. [ASO guidance](metadata-and-marketing.md) explains how to choose and validate the words.

## Review contact and access

Create/update `appStoreReviewDetails` for the selected version using:

- `contactFirstName`, `contactLastName`, `contactPhone`, `contactEmail`.
- `demoAccountRequired`, `demoAccountName`, `demoAccountPassword`.
- `notes` explaining the actual review path, products, hardware and nonobvious constraints.

The create request requires the `appStoreVersion` relationship. Reviewer credentials go through the approved secret mechanism into the actual review record. Never place them in committed metadata or reports. Upload supporting files using `appStoreReviewAttachments`, with the correct parent and dedicated asset protocol. Review notes/attachments are distinct from a reply to Apple's moderation correspondence.

## Compliance fields and separate owner decisions

| Resource/surface | Complete decision area |
| --- | --- |
| `ageRatingDeclarations` | Advertising, alcohol/tobacco/drugs, contests, gambling and simulated gambling, weapons, health/wellness and medical information, loot boxes, messaging/chat, parental controls, age assurance, sexual content/nudity, social media and age-restricted social media, horror, mature themes, unrestricted web, UGC, cartoon/realistic/prolonged graphic violence, Kids age band and applicable regional overrides. |
| Regional rating properties | Current `ageRatingOverrideV2`, Korea override, GRAC classification number and developer age-rating information URL. Read allowed current enums, not a superseded rating scale. |
| `accessibilityDeclarations` | `deviceFamily` plus actual support for audio descriptions, captions, dark interface, differentiation without color alone, larger text, reduced motion, sufficient contrast, Voice Control and VoiceOver. Validate before making the claim. |
| `appEncryptionDeclarations` and documents | App description, proprietary/third-party cryptography and French-store availability. Attach actual supporting documents and associate eligible builds. Do not infer exemption from HTTPS usage alone. |
| `endUserLicenseAgreements` | Actual agreement text and territory relationships. Default/custom EULA and subscription disclosures must agree. |
| Console App Privacy | Data types, purposes, linking to identity and tracking across first/third-party SDKs, then actual Publish action. A policy URL is not the questionnaire. |
| Console tax/legal/compliance | App tax category, contracts, bank/tax/trader facts, regional licenses, medical-device and other applicable attestations. Do not invent a writable tax-category attribute on `apps`. |

Keep **verified**, **missing**, **not applicable with reason** and **blocked** distinct. An OpenAPI-optional attribute can still be required for review because of the actual app's features. Conversely, a response-only field cannot be filled merely to make an inventory look complete.

After any edit, re-read every changed resource and its relevant relationships. Record saved values and remaining state restrictions. Compare the actual selected locale/platform and customer-facing result, not just HTTP success.
