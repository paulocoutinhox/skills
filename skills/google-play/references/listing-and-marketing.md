# Listing, categories, tags, and ASO

## Fields and links

First recommendation: use the 30-character title, and where practical the 80-character short description, close to their full length with meaningful words. Google Play has no ordinary App Store-style subtitle. Use the space for an accurate purpose, audience and benefits in natural wording. This is the owner's editorial preference, not a minimum or a ranking guarantee. Reject padding, mechanical repeats and claims you cannot back up.

| Field | Baseline limit | Contract/surface |
| --- | --- | --- |
| Title | 30 characters | `Listing.title`, localized |
| Short description | 80 characters | `Listing.shortDescription`, localized |
| Full description | 4,000 characters | `Listing.fullDescription`, localized |
| Release notes | 500 characters per locale | Track release `releaseNotes` entries, check current method behavior |
| Preview video | Valid eligible YouTube URL | `Listing.video`, not an uploaded video blob |
| Contact email, phone, website | Valid real contact details | `AppDetails` supported fields |
| Privacy policy | Real policy URL | Complete the supported Play Console policy surface |
| Category and approved tags | Current taxonomy, up to five tags | Play Console settings, not in Publisher listing schemas |

Listing text and release notes are published product content, written to customers about the app. Keep the reasons for each term, research tables and placeholders in the evidence record, never in a submitted field. Do not say how the copy was drafted, and do not mention AI, agents, tools or prompts in it unless the owner clearly asks. A required disclosure belongs in its declaration surface, such as the image upload's `aiGeneratedState` or Data safety, not in the listing text.

Use the provider's real character validation and check non-ASCII and localized text. Do not quietly cut off a sentence or split a grapheme (one visible character). Avoid unusual Unicode styling, repeating keywords that do not fit, banned ranking or price claims, and misleading badges. Do not invent an App Store-style subtitle, hidden keywords or a promotional text field for Google Play.

## Complete ordinary listing field ownership

| Resource | All researched core fields and correct handling |
| --- | --- |
| `AppDetails` | `defaultLanguage`, `contactEmail`, `contactPhone`, `contactWebsite`. Read them through the edit, set only the intended supported values and check the public support information. App price, category and policy questionnaire fields do not belong here. |
| `Listing` | `language`, `title`, `shortDescription`, `fullDescription`, `video`. `language` is the real BCP-47 localization. Use each locale's real path and record, and a real eligible YouTube URL. |
| `Track` | `track`, `releases`. The release list shows the intended changes and the graph of retained artifacts. It is not a place to paste a whole app object. |
| `TrackRelease` | `name`, `versionCodes`, `releaseNotes`, `status`, `userFraction`, `countryTargeting`, `inAppUpdatePriority`. These are release fields, not localized public listing attributes. |

`name` is an internal release label, not the app title or the Android `versionName`. `versionCodes` are strings in the API and include artifacts you mean to retain. `releaseNotes` pairs a real language with at most 500 Unicode characters about real changes. `status` uses the supported explicit release state.

`userFraction` must be more than zero and less than one, and it is allowed for `inProgress` or `halted` when that applies. `countryTargeting` is limited to production `inProgress` releases. `inAppUpdatePriority` is 0–5 for newly added artifacts, defaults to zero and cannot be changed after rollout. Decide the priority before release, and do not raise it just to get around an update problem.

To edit localized text inside an existing edit, use the supported PATCH or PUT at `/applications/{packageName}/edits/{editId}/listings/{language}`. Here is a PATCH example for an app that really captures and organizes reading notes:

```json
{
  "language": "en-US",
  "title": "Leafnote: Book Notes and Ideas",
  "shortDescription": "Save reading notes and quotes. Organize ideas by book and find them when needed."
}
```

The title uses 30 characters and the short description 80. They are made-up editorial examples, not keyword-volume research or ranking evidence. Read the listing that results and check the real locale. Keep the full description and video unless you mean to change them. This listing method has no generic `updateMask` parameter, so do not invent one. Finish validation, commit and review for the whole edit before you claim a public change.

Keep store policy, privacy and access declarations separate from listing text. A privacy link in a description does not replace the required policy form or the account-deletion URL. Check that the support, privacy, terms and deletion URLs open without login where the policy needs public access. What they say must match the code, backend and SDK behavior.

## App-specific marketing process

1. Inspect the real app, the paid limits, the target audience and the main use case. For a game, identify the mechanic, genre, progression and player fantasy. For productivity, stress the job and the effort saved only when you can back it up. For finance, health, education or children, apply the extra policy and claim limits.
2. Research relevant search phrases in each locale using real evidence. Record the intent, feature fit and source. Never make up search volume, competitor performance, medical benefits or an award.
3. Draft candidate titles close to full length, with a distinctive brand and an accurate, relevant purpose. Make the short description use its useful space to state a concrete promise that the first screenshots show. Prefer clear shorter text when filling the field would weaken the meaning.
4. Structure the full description so it is easy to scan: a useful opening, benefits tied to features, workflows, compatibility, account and offline requirements, and clear purchases. Repeat a relevant phrase only where it reads naturally. Avoid SEO stuffing and claims copied from competitors.
5. Localize the message, examples, text direction, screenshots and feature availability. Do not promise a payment method, language or country that the app does not support.
6. Make the icon, feature graphic, first screenshots, video and copy all speak to the same audience and use case. Use eligible store listing experiments or custom listings to test a clear hypothesis. Measure qualified conversion and retention instead of claiming guaranteed rank gains.

App store search and web SEO are separate systems. The app landing page should have accurate content that search engines can crawl and links that work, but HTML SEO metadata does not replace Play listing fields. Do not use review manipulation or false scarcity as marketing tricks.

## Per-term selection and description structure

Record each candidate term or phrase, the user's task, the shipped feature it matches, the locale, the real evidence source, the intended field and the reason for keeping or rejecting it. Use customer and support language, and authorized real acquisition and search data where you have it. Competitor research shows vocabulary and gaps. It does not allow you to copy titles or insert their trademarks.

Put the strongest accurate purpose phrase where it reads naturally in the title. Use the short description space for the main outcome and a meaningful difference. The full description explains how the app achieves that outcome, who it is for, the main workflows and features, compatibility and offline behavior, and clear account and payment requirements. Do not just repeat the short sentence, or fill 4,000 characters with low-value details.

For games, identify the real mechanic and genre, decisions, progression and session experience. For tools, put the task, inputs and outputs, workflow and checked integrations first. For regulated or children-focused apps, apply their stricter claim and content rules before you push discovery text to the limit.

The title, short description and description should support one clear promise while each adds information. Relevant terms belong in natural sentences that explain something. The exact search ranking weights, keyword density and effect of repeating a phrase are not public guarantees. Do not invent numeric density targets or promise that a title change will improve rank.

Google's metadata policy bans misleading ranking, price and promotional badges, and irrelevant special characters, in the identity surfaces it covers. Avoid “#1”, “free”, “no ads”, fake endorsements and discount copy in the title, icon and developer identity. Public listing content and translations must suit a general audience and match the real app behavior. Keep qualified evidence you can attribute instead of anonymous testimonials.

Measure a clear hypothesis through real eligible store experiments or custom listings and authorized acquisition and quality data. Choose the audience, source, locale, metric and observation window in advance. Compare qualified conversion and retained users, not only impressions. Do not credit growth to one word when campaigns, price changes or a new binary running at the same time could explain it. These optimization surfaces have console workflows where the ordinary Publisher listing APIs do not expose them.

## Taxonomy

Choose app or game correctly, then the current main category that matches the core purpose. Use up to five current approved tags that describe real features or gameplay. Tags are not random hashtags or a list of competitor names. Explain why you chose them, and keep the chosen display names and IDs from the current console, with the date and locale where relevant.

The researched Publisher `Listing` and `AppDetails` schemas cannot write category or tags. Prepare the exact choices and set them in Play Console's app category and tags settings. Do this in the owner's signed-in browser when browser use is authorized for this task, and otherwise as an exact owner handoff. Check first for newly supported APIs. Do not send made-up `category`, `subcategory` or `tags` fields and assume success because the server ignored them.

## Required declarations

Check the data flows of the app and third-party SDKs before you answer Data safety. Identify collection, sharing, purposes, required or optional status, encryption, deletion and account behavior. The Publisher API includes `applications.dataSafety` and a safety-label payload. Look up its exact model and official instructions before you submit. Valid JSON does not prove the answers are honest.

The current request is `SafetyLabelsUpdateRequest`, with a required `safetyLabels` field that holds the official Data Safety **CSV contents as a string**. Use the current Console export or template and the supported CSV columns and answers. It is not a free-form nested JSON data-collection object, and a filename is not the CSV contents. Submit to `POST /applications/{packageName}/dataSafety` outside the edit, then check the real saved declaration and policy status. Keep personal and user data out of that template.

Other app content tasks can include ads, content rating, target audience and children, app access and review credentials, sensitive permissions, health and finance declarations, news and government claims, external payments programs and account deletion. Check the real current console tasks and eligibility. Never conclude "no collection" from an empty analytics setup while advertising or payment SDKs still collect data.
