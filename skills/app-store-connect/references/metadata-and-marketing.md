# Metadata, taxonomy, and product positioning

## Intake and output

Collect the product's purpose, audience, core job or game loop, a believable difference from other apps, supported platforms, real features, the line between free and paid, localizations, tone, brand limits, competitors to research, and the main conversion goal. Look at the app and the evidence. Do not advertise a roadmap item as a shipped feature.

Produce one reviewed metadata document per locale, a reason for the category choice, a keyword-intent table, a screenshot storyboard, checked URLs and checked field lengths. Keep draft text apart from API payloads so app-level and version-level resources do not get mixed up. The [complete core-field guide](store-fields-and-localizations.md) lists every supported normal app, version, localization and reviewer attribute and where each one is changed.

First recommendation: make good use of the 30 characters in both name and subtitle where you can. Every added term must add a real use case, audience, benefit or difference. Aim close to the limit when the pair still reads naturally and clearly. Do not pad with repeats, unrelated keywords or weak claims just to reach 30. This is the owner's writing preference, not an Apple minimum or a ranking promise.

| Field | Baseline limit | Placement and strategy |
| --- | --- | --- |
| App name | 30 characters | Brand plus a clear, relevant use case when it reads naturally |
| Subtitle | 30 characters | Add to the name with a different benefit or audience |
| Description | 4,000 characters | Strong opening, benefits backed by features, relevant details and purchase disclosures |
| Promotional text | 170 characters | A current, honest message above the description, not a pile of keywords |
| Keywords | 100 UTF-8 bytes | Relevant comma-separated terms, no repeated app/company names or competitor trademarks |
| What's new | 4,000 characters | Changes users can see and important fixes, no made-up improvements |
| Support URL | Valid reachable URL | Real support/contact information that matches the app |
| Marketing URL | Valid reachable URL when used | Landing page for this app with matching claims |
| Privacy policy URL | Required for all apps under current policy | Real policy that covers how the app and its SDKs behave |

Count Unicode text before submission and check the provider's response. For keywords use `len(value.encode("utf-8"))`, including commas. The detailed platform help gives the limit in bytes, while the marketing overview talks about characters. Stay safely within the byte limit, especially for accented and non-Latin languages. Do not fill unused bytes with unrelated terms. Check locale codes against Apple's current localization list instead of converting every language code by rote.

## Marketing method

1. Find the audience's problem, words, and hoped-for result. For utilities, lead with the task and benefit. For games, show the core mechanic, fantasy, and progress. For professional tools, stress workflow, supported formats, integration, and believable proof of trust. For education, make the level, subject, and way of learning clear without promising results.
2. Build a table of candidate keywords with search intent, how they relate to the real app, locale, where the evidence comes from, and competition where real data exists. Do not make up volume or ranking scores. Use research to find gaps, then write natural text.
3. Draft several name and subtitle pairs within the limits, using each field well and close to its limit. Prefer a readable pair that stands out, with an accurate main phrase. Avoid repeated words, too much punctuation, empty superlatives, price or ranking claims, and brands you have no right to use.
4. Write the description's opening so it is easy to scan. Follow with the main benefits, concrete features, compatibility, accessibility where tested, and purchase or account requirements. Use plain text. Do not rely on HTML being shown.
5. Localize the intent and examples, not just the words. Check text that grows longer, cultural meaning, UI terms, currency and date claims, and keyword bytes for each language. Review by a native speaker helps for major locales.
6. Make the first screenshots match the promise in the title and subtitle. Each image explains one real benefit. Run experiments through supported product-page optimization or custom pages where eligible, with a metric chosen in advance and a long enough observation period. Do not promise better rankings or conversion.

App Store optimization and web SEO share clear language and a useful landing page. Apple search is not the same as web search. Promotional copy and the description should persuade accurately and not claim search behavior you cannot back up. Never buy ratings, hide complaints, or game review prompts.

## Decide what each term earns

Make a short writing table: candidate phrase, user intent, the feature that shows it, locale, evidence, the field you plan to use, rejected options and why. Use real customer words, support and review themes, relevant store searches and the owner's allowed analytics or Apple Ads research where available. Mark qualitative notes as qualitative. Never make up search volumes, install attribution or how much a term counts for ranking.

Give the name the strongest accurate purpose phrase. Use the subtitle for added results or features. Put other relevant terms in the keyword field without repeating words that the name, subtitle or category already cover. Keep comma separators tight, skip extra singular/plural variants and keep meaningful multiword phrases when they fit. Do not claim that every combination across fields or across locales is sure to be indexed.

Apple names the title, subtitle, keywords and categories as text inputs for search relevance, along with behavior signals. Apple says promotional text does not affect search ranking. Descriptions need to inform and convert: stuffing them with terms is not a documented ranking method. What the user reads and the first impression still matter a lot, even where a field is not a direct keyword input.

For a made-up app that really captures and organizes reading notes:

| Field | Candidate | Writing role |
| --- | --- | --- |
| Name | Leafnote: Book Notes and Ideas | A clear brand plus the real main task, within 30 characters. |
| Subtitle | Save quotes, organize insights | Added capture and organization benefits, within 30 characters. |
| Additional keyword candidates | annotation,highlights,books,library,journal | Use only features and words the app really supports. Remove words repeated from the category or other fields and check the final UTF-8 bytes. |

This is an example of the thinking, not researched keyword-volume data or a required template. A drawing app, an accessibility tool and a strategy game need different terms and promises. Explain why each word you keep earns its limited space and why a shorter candidate may read better.

## Description, release notes and conversion

Write a concrete first sentence that says who the app helps and what they can do. Follow with a short, readable list of benefits and features, a typical workflow, tested compatibility, offline and accessibility details, and clear account or subscription requirements. Keep shipped features apart from future plans. Do not put in a fixed localized price that can drift from StoreKit, tax or eligibility.

Every text in this section is published product content for customers about the app. Keep reasons for candidates, term tables, source notes and placeholders in the evidence record, never in a submitted field. Do not describe how the copy was written or mention AI, agents, tools or prompts in it unless the owner clearly asks. A required disclosure, such as sharing data with a third-party AI, belongs in App Privacy, age rating or the in-app consent flow, not in the description or release notes.

Release notes name important new behavior and real fixes. Generic wording is fine for normal bug, security or performance maintenance only when it is honest. Promotional text can describe a real current update or campaign, but should not suggest features that are not available or savings that are not checked. Check dates and which territories it covers.

Make the icon, first screenshot captions and first seconds of the preview support the chosen intent. Each later screenshot shows a different useful feature. Check readability at small size, cut-off text, text that grows in other languages and real device layouts. Use native-speaker review for locales that matter commercially, where available.

For optimization, state one hypothesis, the intended audience or source and the main metric before an experiment. Compare impressions, product-page views, qualified downloads and later retention over the same locale, source and build periods. Apple Ads can change reported search downloads. Do not claim a short campaign, product changes made at the same time or a small sample caused better organic ranking.

## Categories, subcategories, and tags

Read the current `/v1/appCategories` list and relationships. Choose a primary category that matches the core function, a secondary category only when there is a reason, and game subcategories where the current model allows them. Use real category IDs and allowed parent/child pairs. Patch the selected `AppInfo` relationships with `AppInfoUpdateRequest`, not free-text category names in version metadata.

Apple app tags are separate from keywords. Current tools can list the tags Apple generated for an app and update allowed visibility properties through `appTags`. Check the current schema and which territories are eligible. Do not make up tags, a user-defined hashtag field, or an endpoint to create tags. Record the owner's review of suggested tags and make only supported changes.

## Other required information

Collect the copyright owner and year, content rights, age-rating answers and regional overrides, app access and login needs, privacy policy and tracking behavior, encryption and export compliance, content moderation, account deletion, paid-app contracts, distribution territories, app price and tax category, and any legal or trader information that applies. Accessibility labels and Vision Pro motion information must describe behavior you tested. Some declarations can only be set in the console or depend on the account. A missing API does not allow a guessed value or a fake declaration.

Reviewer notes explain workflows that are not obvious, paid content, test credentials, hardware, location limits, and where to find each product. Give a working review account without personal data it does not need. Keep demo data realistic and harmless. Do not block review behind SMS codes, invitation flows, or servers the reviewer cannot reach.
