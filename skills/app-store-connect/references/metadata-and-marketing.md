# Metadata, taxonomy, and product positioning

## Intake and output

Collect product purpose, audience, core job or game loop, credible differentiator, supported platforms, actual features, paid/free boundaries, localizations, tone, brand constraints, competitors for research, and primary conversion goal. Inspect the app and evidence. Do not advertise a roadmap as a shipped feature.

Produce one reviewed metadata document per locale, a category rationale, a keyword-intent table, a screenshot storyboard, verified URLs and checked field lengths. Store draft text separately from API payloads so app-level and version-level resources are not confused. The [complete core-field guide](store-fields-and-localizations.md) identifies every supported ordinary app/version/localization/reviewer attribute and the actual mutation surface.

First recommendation: make meaningful use of the available 30 characters in both name and subtitle where possible. Every added term must contribute a real use case, audience, benefit or distinction. Aim near capacity when the pair remains natural and clear. Do not pad with repetition, irrelevant keywords or weak claims merely to hit 30. This is the owner's editorial preference, not an Apple minimum or ranking guarantee.

| Field | Baseline limit | Placement and strategy |
| --- | --- | --- |
| App name | 30 characters | Brand plus a clear, relevant use case when it reads naturally |
| Subtitle | 30 characters | Complement the name with a distinct benefit or audience |
| Description | 4,000 characters | Strong opening, benefits supported by features, relevant details and purchase disclosures |
| Promotional text | 170 characters | Timely truthful message above the description, not a keyword dump |
| Keywords | 100 UTF-8 bytes | Relevant comma-separated terms, no repeated app/company names or competitor trademarks |
| What's new | 4,000 characters | User-visible changes and material fixes, no fabricated improvements |
| Support URL | Valid reachable URL | Real support/contact information matching the app |
| Marketing URL | Valid reachable URL when used | App-specific landing page with consistent claims |
| Privacy policy URL | Required for all apps under current policy | Actual policy covering implementation and SDK behavior |

Count Unicode text before submission and inspect the provider response. For keywords use `len(value.encode("utf-8"))`, including commas. The detailed platform help specifies bytes while the marketing overview describes characters. Apply the byte ceiling conservatively, especially for accented and non-Latin languages. Do not fill unused bytes with irrelevant terms. Verify locale codes against Apple's current localization list rather than converting every language code mechanically.

## Marketing method

1. Identify the audience's problem, language, and expected outcome. For utilities, lead with the task and benefit. For games, communicate the core mechanic, fantasy, and progression. For professional tools, emphasize workflow, supported formats, integration, and credible trust evidence. For education, clarify level, subject, and learning interaction without guaranteeing outcomes.
2. Build a candidate keyword table with query intent, relevance to the actual app, locale, evidence source, and competitiveness where real data exists. Do not fabricate volume or ranking scores. Use research to identify gaps, then write natural text.
3. Draft several name/subtitle combinations within limits, making useful near-capacity use of each field. Prefer a readable, differentiated pair with an accurate primary phrase. Avoid duplicated words, excessive punctuation, generic superlatives, price/ranking claims, and unauthorized brands.
4. Write the description's opening for scanning. Follow with the main benefits, concrete capabilities, compatibility, accessibility where verified, and purchase/account requirements. Use plain text. Do not depend on HTML rendering.
5. Localize intent and examples, not just words. Check text expansion, cultural meaning, UI terminology, currency/date claims, and language-specific keyword bytes. Native review is valuable for major locales.
6. Align the first screenshots with the promise in the title/subtitle. Each image explains one actual benefit. Experiment through supported product-page optimization/custom pages where eligible, with a preselected metric and adequate observation window. Do not promise ranking or conversion improvements.

App Store optimization and web SEO overlap through clear language and a useful landing page. Apple search indexing is not identical to web search. Promotional copy and description should persuade accurately rather than claim unsupported indexing behavior. Never buy ratings, suppress complaints, or manipulate review prompts.

## Decide what each term earns

Create a compact editorial table: candidate phrase, user's intent, demonstrated feature, locale, evidence, intended field, rejected alternatives and why. Use genuine customer language, support/review themes, relevant store queries and the owner's authorized analytics/Apple Ads research where available. Label qualitative observations as qualitative. Never invent query volumes, install attribution or a term's ranking weight.

Allocate the strongest accurate purpose phrase to the name. Use the subtitle for complementary outcomes or capabilities. Put additional relevant terms in the keyword field without repeating words already covered by name, subtitle or category. Keep comma separators compact, avoid redundant singular/plural variants and preserve meaningful multiword phrases when appropriate. Do not claim every cross-field combination or locale spillover is guaranteed to index.

Apple identifies title, subtitle, keywords and categories as text-relevance inputs, alongside behavioral signals. Promotional text explicitly does not affect search ranking. Descriptions need to inform and convert: stuffing them with terms is not a documented ranking technique. The user-facing meaning and first impression remain critical even where a field is not a direct keyword input.

For a fictional app that genuinely captures and organizes reading notes:

| Field | Candidate | Editorial role |
| --- | --- | --- |
| Name | Leafnote: Book Notes and Ideas | Distinct brand plus the actual primary task, within 30 characters. |
| Subtitle | Save quotes, organize insights | Complementary capture/organization benefits, within 30 characters. |
| Additional keyword candidates | annotation,highlights,books,library,journal | Consider only features and language actually supported. Remove category/word duplication and validate final UTF-8 bytes. |

This is a reasoning example, not researched keyword-volume data or a mandatory template. A drawing app, accessibility tool and strategy game require different terms and promises. Explain why each retained word deserves scarce space and why a shorter candidate may read better.

## Description, release notes and conversion

Write a concrete first sentence naming who the app helps and what they can accomplish. Follow with a short readable benefit/capability sequence, a typical workflow, verified compatibility/offline/accessibility details and transparent account/subscription requirements. Separate shipped features from future plans. Do not insert a fixed localized price that can diverge from StoreKit, tax or eligibility.

Release notes identify material new behavior and actual fixes. Generic wording is appropriate for ordinary bug/security/performance maintenance only when truthful. Promotional text can describe a real current update or campaign, but should not suggest unavailable functionality or unverified savings. Check dates and territorial scope.

Make the icon, first screenshot captions and first preview seconds reinforce the selected intent. Each subsequent screenshot demonstrates a different useful capability. Review small-size readability, truncation, local-language expansion and actual device layouts. Use native review for commercially important locales where available.

For optimization, state one hypothesis, intended audience/source and primary metric before an experiment. Compare impressions, product-page views, qualified downloads and downstream retention with consistent locale/source/build windows. Apple Ads can affect reported search acquisition. Avoid claiming causal organic ranking improvement from a short campaign, simultaneous product changes or a small sample.

## Categories, subcategories, and tags

Read the current `/v1/appCategories` inventory and relationships. Select a primary category that matches the core function, a secondary category only when justified, and game subcategories where the current model permits them. Use real category IDs and permitted parent/child combinations. Patch the selected `AppInfo` relationships using `AppInfoUpdateRequest`, not free-text category names in version metadata.

Apple app tags are a separate surface from keywords. Current tools can list a particular app's generated tags and update allowed visibility properties through `appTags`. Inspect the current schema and territorial eligibility. Do not invent arbitrary tags, a user-defined hashtag field, or a tag-creation endpoint. Document owner review of inferred tags and make only supported changes.

## Other required information

Capture copyright owner/year, content rights, age-rating answers and regional overrides, app access/login needs, privacy policy and tracking behavior, encryption/export compliance, content moderation, account deletion, paid-app contracts, distribution territories, app price/tax category, and applicable legal/trader information. Accessibility labels and Vision Pro motion information must describe tested behavior. Some declarations remain console-controlled or account-dependent. An absent API does not authorize a guessed value or a fake declaration.

Reviewer notes explain nonobvious workflows, paid content, test credentials, hardware, geographic limitations, and where to find each product. Supply a functioning review account without unnecessary personal data. Keep demo data realistic and harmless. Do not gate review behind inaccessible SMS codes, invitation flows, or unavailable servers.
