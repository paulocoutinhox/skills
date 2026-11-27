# Platform fields and limits

Baseline checked: 2026-11-05. Check the exact publishing surface again before release. Character limits are maximums, not writing targets. Hashtags and mentions use the same caption budget unless a platform clearly says otherwise.

| Surface | Native text fields and working ceiling | Recommended editorial treatment |
| --- | --- | --- |
| YouTube video | Title: 100 characters. Studio description: 5,000 characters. Data API description: 5,000 UTF-8 bytes. Tags: 500 characters under the API's comma/quote accounting. | Put the subject and benefit first. Use a unique description. Put the main promise and useful links near the top. |
| YouTube Shorts | Same video title, description and tags fields, with the same API/Studio difference. | A short hook and a clear subject. `#Shorts` is optional, not required for format classification. |
| TikTok video Direct Post | API `title` is the caption, up to 2,200 UTF-16 units according to the current endpoint wording. Native app limits may differ. | Put the searchable topic and hook first. Give the spoken/on-screen hook and cover text as creative support, not as made-up API fields. |
| Instagram feed/Reel | Working caption limit: 2,200. Working maximum of 5 hashtags per post or Reel caption, under Instagram's gradually applied cap. | Use no more than 5 relevant hashtags. Check the exact account and endpoint. Include alt text for supported image surfaces. |
| X standard post | 280 weighted characters. URLs and Unicode use platform weighting. | One clear idea, a specific hook and an optional short CTA. Use a thread only when asked or when it adds real value. |
| LinkedIn feed post | 3,000 characters. A normal feed post has no separate native title/description/tag field. | Open with a professional problem or useful observation, then evidence or a method people can act on, and one relevant action. |

Do not call a 5,000-character non-ASCII YouTube description valid for the API unless its UTF-8 byte count also fits. The API rejects `<` and `>` in title and description. Tags with spaces count as if they had quotation marks around them, and the commas between tags use up the budget. Tags are not hashtags, and they should not be dumped into the visible description.

X longer-post limits differ by product and documentation. Public help pages disagree between 4,000 and larger limits. Use 280 by default unless the user's real account and publishing surface confirm a longer allowance. Do not promise one paid-tier limit for everyone. X URLs usually count as the platform's fixed shortened length, not their visible string length.

Treat five hashtags as the Instagram working maximum. Do not claim that every API surface enforces it. Check mention allowances on the real account and endpoint. If you cannot check, clearly name the uncertainty and use up to five hashtags.

## Complete field packages

For YouTube and Shorts, give the title, description, tags as a separate list, hashtags already placed in their intended visible field, and an optional pinned comment. Include category, language, audience/made-for-kids status, visibility, publishing time/time zone, paid-promotion status and the Studio "AI use" attribute as decisions to confirm where they apply. That attribute is required for realistic content that is meaningfully AI-generated or altered, such as a real person shown saying something they did not say. Production help, such as AI help with a script, title or thumbnail, does not require it. The disclosure is the setting, and YouTube adds its own label. Do not write a disclosure or production note into the title or description. Do not decide content is for children just because the tone is casual. Timestamps need the real media. Do not make up chapters for a video you have not seen.

For TikTok, give the caption, the hashtag and mention choices inside it, optional cover text and spoken hook, and the privacy/comment/duet/stitch decisions that apply to the real account. For Instagram, give the caption, included hashtags and mentions, image alt text when supported, optional cover text for a Reel, and any chosen location, collaborators, product tags or disclosures the surface supports.

For X, give each final post separately, with alt text for attached images and a clear thread order if asked. For LinkedIn, give the post body, image alt text where supported, and an optional first comment as a separate item. Article titles, article bodies, newsletter descriptions and sponsored-ad fields belong to separate surfaces. Check their limits before you create them.

## Hashtag practice

Use a few relevant topic, audience or brand tags. Do not add unrelated trending tags or engagement bait. On YouTube, more than 60 hashtags makes YouTube ignore all hashtags on that content. That is not a suggestion to get close to 60. A default of about 2–5 relevant tags is an editorial starting point, adjusted to the chosen platform and audience, not a promise of reach.
