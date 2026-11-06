# Listing, categories, tags, and ASO

## Fields and links

First recommendation: make meaningful near-capacity use of the 30-character title and, where practical, the 80-character short description. Google Play has no ordinary App Store-style subtitle. Use the space for accurate purpose, audience and benefits with natural wording. This is the owner's editorial preference, not a minimum or ranking guarantee. Reject padding, mechanical duplication and unsupported claims.

| Field | Baseline limit | Contract/surface |
| --- | --- | --- |
| Title | 30 characters | `Listing.title`, localized |
| Short description | 80 characters | `Listing.shortDescription`, localized |
| Full description | 4,000 characters | `Listing.fullDescription`, localized |
| Release notes | 500 characters per locale | Track release `releaseNotes` entries, verify current method behavior |
| Preview video | Valid eligible YouTube URL | `Listing.video`, not an uploaded video blob |
| Contact email, phone, website | Valid real contact details | `AppDetails` supported fields |
| Privacy policy | Actual policy URL | Complete the supported Play Console policy surface |
| Category and approved tags | Current taxonomy, up to five tags | Play Console settings, absent from Publisher listing schemas |

Use the provider's actual character validation and check non-ASCII/localized text. Do not silently truncate a sentence or split a grapheme. Avoid unusual Unicode styling, irrelevant keyword repetition, prohibited ranking/price claims, and misleading badges. Do not invent an App Store-style subtitle, hidden keywords, or promotional text field for Google Play.

## Complete ordinary listing field ownership

| Resource | All researched core fields and correct handling |
| --- | --- |
| `AppDetails` | `defaultLanguage`, `contactEmail`, `contactPhone`, `contactWebsite`. Read through the edit, set only intended supported values and verify public support information. No app price, category or policy questionnaire fields belong here. |
| `Listing` | `language`, `title`, `shortDescription`, `fullDescription`, `video`. `language` is the actual BCP-47 localization. Use each locale's actual path/record and a real eligible YouTube URL. |
| `Track` | `track`, `releases`. The release list represents the intended changes/retained artifact graph, not a place to paste a complete app object. |
| `TrackRelease` | `name`, `versionCodes`, `releaseNotes`, `status`, `userFraction`, `countryTargeting`, `inAppUpdatePriority`. These are release fields, not localized public listing attributes. |

`name` is an internal release label, not the app title or Android `versionName`. `versionCodes` are string representations in the API and include artifacts intentionally retained. `releaseNotes` pairs actual language with at most 500 Unicode characters of real changes. `status` uses the supported explicit release state.

`userFraction` must be greater than zero and less than one and is allowed for `inProgress` or `halted` when applicable. `countryTargeting` is restricted to production `inProgress` releases. `inAppUpdatePriority` is 0–5 for newly added artifacts, defaults to zero and cannot be changed after rollout. Make the priority decision before release and do not inflate it merely to bypass an update problem.

To edit localized text inside an existing edit, use the supported PATCH or PUT at `/applications/{packageName}/edits/{editId}/listings/{language}`. A PATCH example for an app that genuinely captures and organizes reading notes is:

```json
{
  "language": "en-US",
  "title": "Leafnote: Book Notes and Ideas",
  "shortDescription": "Save reading notes and quotes. Organize ideas by book and find them when needed."
}
```

The title uses 30 characters and the short description 80. They are fictional editorial examples, not keyword-volume research or ranking evidence. Read the resulting listing and verify the actual locale. Preserve the full description/video unless their change is intended. No generic `updateMask` parameter is invented for this listing method. Complete validation/commit/review for the whole edit before claiming public change.

Store policy/privacy/access declarations separately from listing text. A privacy link in a description does not replace the required policy form or account-deletion URL. Check support/privacy/terms/deletion URLs without login where the policy requires public access. Their claims must match code, backend, and SDK behavior.

## App-specific marketing process

1. Inspect the real app, paid boundaries, target audience, and principal use case. For a game, identify mechanic, genre, progression, and player fantasy. For productivity, emphasize the job and saved effort only when substantiated. For finance, health, education, or children, apply the extra policy/claim restrictions.
2. Research relevant search phrases in each locale using actual evidence. Record intent, feature relevance, and source. Never invent search volume, competitor performance, medical benefits, or an award.
3. Draft near-capacity candidate titles with a distinctive brand and an accurate relevant purpose. Make the short description use its useful available space to state a concrete promise that the first screenshots demonstrate. Prefer clear shorter text when filling the field would weaken meaning.
4. Structure the full description for scanning: useful opening, benefits connected to features, workflows, compatibility, account/offline requirements, and transparent purchases. Repeat a relevant phrase only where natural. Avoid SEO stuffing and copy-pasted competitor claims.
5. Localize the message, examples, text direction, screenshots, and feature availability. Do not promise a payment method, language, or country that the app does not support.
6. Align icon, feature graphic, first screenshots, video, and copy around the same audience and use case. Use eligible store listing experiments or custom listings to test a defined hypothesis. Measure qualified conversion and retention rather than claiming guaranteed rank improvements.

App store search and web SEO are distinct systems. The app landing page should have crawlable accurate content and usable links, but HTML SEO metadata does not replace Play listing fields. Do not use review manipulation or false scarcity as marketing techniques.

## Per-term selection and description structure

Record candidate term/phrase, user's task, matching shipped feature, locale, real evidence source, intended field and reason for keeping/rejecting it. Use customer/support language and authorized actual acquisition/search data where available. Competitor research identifies vocabulary and gaps, not permission to copy titles or insert their trademarks.

Place the strongest accurate purpose phrase where it reads naturally in the title. Use short description space for the principal outcome and a meaningful differentiator. The full description explains how the app accomplishes that outcome, who it is for, main workflows/features, compatibility/offline behavior and transparent account/payment requirements. Do not merely repeat the short sentence or fill 4,000 characters with low-value details.

For games, identify actual mechanic/genre, decisions, progression and session experience. For tools, prioritize task, inputs/outputs, workflow and verified integration. For regulated or children-focused apps, apply their stricter claims and content rules before maximizing discovery text.

The title, short description and description should reinforce a coherent promise while adding information. Relevant terminology belongs in natural explanatory sentences. The exact search ranking weights, keyword density and effect of repeating a phrase are not public guarantees. Do not invent numeric density targets or promise a title change will improve rank.

Google's metadata policy prohibits misleading ranking/price/promotional badges and irrelevant special characters in the covered identity surfaces. Avoid “#1”, “free”, “no ads”, fake endorsement and discount copy in title/icon/developer identity. Public listing content and translations must be suitable for a general audience and actual app behavior. Preserve qualified, attributable evidence rather than anonymous testimonials.

Measure a defined hypothesis through actual eligible store experiments/custom listings and authorized acquisition/quality data. Choose the audience/source/locale, metric and observation window in advance. Compare qualified conversion and retained users, not only impressions. Do not attribute growth to one word when simultaneous campaigns, price changes or a new binary confound it. These optimization surfaces have console workflows where ordinary Publisher listing APIs do not expose them.

## Taxonomy

Choose app versus game correctly, then the current primary category matching the core purpose. Use up to five current approved tags that describe actual functionality/gameplay. Tags are not arbitrary hashtags or a list of competitor names. Explain the rationale and retain the selected display names/IDs from the current console, with date and locale where relevant.

The researched Publisher `Listing` and `AppDetails` schemas do not expose category/tag writes. Prepare exact selections and complete them in Play Console's app category/tags settings. Recheck for newly supported APIs before the handoff. Do not send invented `category`, `subcategory`, or `tags` fields and assume success because the server ignored them.

## Required declarations

Audit app and third-party SDK data flows before answering Data safety. Identify collection, sharing, purposes, required/optional status, encryption, deletion, and account behavior. The Publisher API includes `applications.dataSafety` and a safety-label payload. Resolve its exact model and official instructions before submission. JSON validity is not evidence of truthful answers.

The current request is `SafetyLabelsUpdateRequest` with required `safetyLabels` containing the official Data Safety **CSV contents as a string**. Use the current Console export/template and supported CSV columns/answers. It is not an arbitrary nested JSON data-collection object, and a filename is not the CSV contents. Submit to `POST /applications/{packageName}/dataSafety` outside the edit, then verify actual saved declaration and policy status. Keep personal/user data out of that template.

Other app content tasks can include ads, content rating, target audience/children, app access/review credentials, sensitive permissions, health/finance declarations, news/government claims, external payments programs, and account deletion. Check actual current console tasks and eligibility. Never infer "no collection" from an empty analytics configuration while advertising/payment SDKs still collect data.
