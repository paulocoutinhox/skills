# Store fields, ownership and safe edits

Checked against Apple's OpenAPI **4.6** and current Connect help on **2026-11-05**. This page explains fields and workflows. It is not a generated schema catalog. The schemas keep create, update and response fields separate. A field that appears in a response is not always writable.

## Establish the target graph

Read `GET /v1/apps?filter[bundleId]=<bundle-id>`, then the app's `appInfos`, `appStoreVersions`, builds and relevant localizations. Pick records by their real platform, version and editable state, not by the first one returned. Follow pagination. Keep the ID for each parent and locale. App ID, bundle ID, SKU, version ID and localization ID each mean something different.

Make a field list before editing: current value, intended value, owning resource, locale/platform, API or console screen, whether it is required, whether it can be edited, how you will check it and the owner's decision. Use [the release evidence template](../assets/release-evidence.md). Do not replace unknown fields with empty strings. Send only the PATCH attributes you mean to change. A delete is its own supported operation, not an empty localized value.

## App-level fields

`PATCH /v1/apps/{id}` supports these researched attributes:

| Fields | Purpose and editing rule |
| --- | --- |
| `primaryLocale` | Default store language. Decide the intended localization and fallback before changing it. |
| `bundleId` | Allowed by the update model but limited by app state. Do not treat an uploaded identity as something you can freely rename. |
| `accessibilityUrl` | Real public accessibility information. Check the content and that the page loads. |
| `contentRightsDeclaration` | `DOES_NOT_USE_THIRD_PARTY_CONTENT` or `USES_THIRD_PARTY_CONTENT`, based on the real rights. |
| `subscriptionStatusUrl`, `subscriptionStatusUrlVersion` | Production server-notification address and version. Use the intended receiver that is authenticated and monitored. |
| `subscriptionStatusUrlForSandbox`, `subscriptionStatusUrlVersionForSandbox` | Separate sandbox notification address and version. Do not mix environments. |
| `streamlinedPurchasingEnabled` | A real choice about purchase behavior. Check feature and account eligibility and the effect on customers before changing it. |

The response fields `name`, `sku` and the derived status fields are not how this model updates the name. Change the localized name through the AppInfo localization. Handle app creation, SKU and platform ownership and any identity changes that cannot be made here through the supported console workflow.

## App information and taxonomy

`PATCH /v1/appInfos/{id}` changes category relationships using real `appCategories` IDs:

- `primaryCategory`, `secondaryCategory`.
- `primarySubcategoryOne`, `primarySubcategoryTwo`.
- `secondarySubcategoryOne`, `secondarySubcategoryTwo`.

Pick allowed parent and child categories from the live category tree and the app's real main use. Do not fill every optional category. Game subcategories apply only to allowed game-category relationships.

Create AppInfo localizations with `POST /v1/appInfoLocalizations`, the required `locale` and `name`, and the `appInfo` relationship. Edit existing ones with `PATCH /v1/appInfoLocalizations/{id}`:

| Fields | Meaning and limits |
| --- | --- |
| `name` | App name, at most 30 characters. Use the approved localized brand and purpose pair. |
| `subtitle` | A short statement that adds value, at most 30 characters. |
| `privacyPolicyUrl` | Public, accurate policy URL. Required for all apps under the current policy. |
| `privacyChoicesUrl` | Optional real page for privacy choices, deletion or rights, not a made-up contact page. |
| `privacyPolicyText` | Policy text for a specific platform, including the tvOS display. Keep it in line with the public policy. |

You choose the locale when you create the record. Do not send `locale` in a PATCH model that does not have it. App Privacy questionnaire answers are separate from these URLs and text and have their own publish step in the console.

`appTags` are tags that Apple generates. Read the app's tags and allowed territories, then use supported `visibleInAppStore` updates when it makes sense. There is no operation to create free-form hashtags.

## Platform version fields

Create with `POST /v1/appStoreVersions` using `platform`, `versionString` and the `app` relationship. Other supported create attributes are `copyright`, `reviewType`, `releaseType`, `earliestReleaseDate` and `usesIdfa`. Optional build and localization links follow the exact create schema.

| Attribute | How to decide |
| --- | --- |
| `platform` | The real `IOS`, `MAC_OS`, `TV_OS` or `VISION_OS` release. You choose it at creation. A PATCH cannot change the platform. |
| `versionString` | Marketing version that matches the intended release line, separate from the build number. |
| `copyright` | Real owner and year. A store name does not prove who owns the rights. |
| `reviewType` | `APP_STORE` for normal store publishing. `NOTARIZATION` is a different eligible distribution route. |
| `releaseType` | `MANUAL`, `AFTER_APPROVAL` or `SCHEDULED`, chosen before submission. |
| `earliestReleaseDate` | Supported timestamp for the chosen release strategy. Record the time zone and check territory and preorder rules. |
| `usesIdfa` | Real use of the advertising identifier. It does not replace privacy answers or ATT compliance. |
| `downloadable` | In the update model and limited by state. It changes availability for customers. It is not a general rollback switch. |

`PATCH /v1/appStoreVersions/{id}` supports the editable attributes above except `platform`, plus the documented `build` and `appClipDefaultExperience` relationships. Use the dedicated build relationship when it fits. Never PATCH `appStoreState`, `appVersionState` or `createdDate` to force approval.

### Version localizations

Create with `POST /v1/appStoreVersionLocalizations` using `locale` and `appStoreVersion`. Its text attributes, which you can also edit through `PATCH /v1/appStoreVersionLocalizations/{id}`, are:

| Field | Limit and what it is for |
| --- | --- |
| `description` | 4,000 characters. Concrete benefits, features that have shipped, compatibility and purchase or account conditions. |
| `keywords` | To be safe, 100 UTF-8 bytes including commas, based on the detailed help. Add to the indexed name, subtitle and category. |
| `promotionalText` | 170 characters. Accurate, current information that you can edit on its own when supported. It is not a keyword field for search ranking. |
| `supportUrl` | A working support page and a real way to get in touch. |
| `marketingUrl` | Optional landing page for this product, honest and reachable. |
| `whatsNew` | 4,000 characters. The real changes in this update, with important behavior changes explained. |

The create model can link `placements`. Manage real images and videos through [the current Asset Library procedure](screenshots-and-media.md), not through a screenshot attribute that does not exist on this localization object.

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

This made-up example assumes the app really has those features. The identifiers are placeholders. Read the result back, check the locale, parent and state, and look at the store preview. A description change goes to the version-localization endpoint, not this request. [ASO guidance](metadata-and-marketing.md) explains how to choose and check the words.

## Review contact and access

Create or update `appStoreReviewDetails` for the selected version using:

- `contactFirstName`, `contactLastName`, `contactPhone`, `contactEmail`.
- `demoAccountRequired`, `demoAccountName`, `demoAccountPassword`.
- `notes` that explain the real review path, products, hardware and limits that are not obvious.

The create request needs the `appStoreVersion` relationship. Reviewer credentials go through the approved secret store into the real review record. Never put them in committed metadata or reports. Upload supporting files with `appStoreReviewAttachments`, using the correct parent and the dedicated asset protocol. Review notes and attachments are not the same as a reply to Apple's review messages.

## Compliance fields and separate owner decisions

| Resource/surface | Full area to decide |
| --- | --- |
| `ageRatingDeclarations` | Advertising, alcohol/tobacco/drugs, contests, gambling and simulated gambling, weapons, health/wellness and medical information, loot boxes, messaging/chat, parental controls, age assurance, sexual content/nudity, social media and age-restricted social media, horror, mature themes, unrestricted web, UGC, cartoon/realistic/prolonged graphic violence, Kids age band and any regional overrides that apply. |
| Regional rating properties | Current `ageRatingOverrideV2`, Korea override, GRAC classification number and developer age-rating information URL. Read the allowed current enums, not an older rating scale. |
| `accessibilityDeclarations` | `deviceFamily` plus real support for audio descriptions, captions, dark interface, differentiation without color alone, larger text, reduced motion, sufficient contrast, Voice Control and VoiceOver. Test before you make the claim. |
| `appEncryptionDeclarations` and documents | App description, own or third-party cryptography and availability in the French store. Attach the real supporting documents and link eligible builds. Do not assume an exemption just because the app uses HTTPS. |
| `endUserLicenseAgreements` | Real agreement text and territory relationships. The default or custom EULA and the subscription disclosures must match. |
| Console App Privacy | Data types, purposes, linking to identity and tracking across your own and third-party SDKs, then the real Publish action. A policy URL is not the questionnaire. |
| Console tax/legal/compliance | App tax category, contracts, bank/tax/trader facts, regional licenses, medical-device and other statements that apply. Do not make up a writable tax-category attribute on `apps`. |

Keep **verified**, **missing**, **not applicable with reason** and **blocked** separate. An attribute that is optional in OpenAPI can still be required for review because of the app's real features. On the other hand, you cannot fill a response-only field just to make a list look complete.

After any edit, read every changed resource and its relevant relationships again. Record the saved values and any state limits that remain. Compare the real selected locale and platform and what the customer sees, not just HTTP success.
