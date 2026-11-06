# Platform fields and limits

Baseline verified: 2026-11-05. Verify the exact publishing surface again before release. Character limits are ceilings, not writing targets. Hashtags and mentions consume the same caption budget unless a platform explicitly says otherwise.

| Surface | Native text fields and working ceiling | Recommended editorial treatment |
| --- | --- | --- |
| YouTube video | Title: 100 characters. Studio description: 5,000 characters. Data API description: 5,000 UTF-8 bytes. Tags: 500 characters under the API's comma/quote accounting. | Front-load the subject and benefit. Use a unique description. Put the main promise and useful links near the top. |
| YouTube Shorts | Same video title, description, and tags fields, with the same API/Studio distinction. | A short hook and a clear subject. `#Shorts` is optional, not a requirement for format classification. |
| TikTok video Direct Post | API `title` is the caption, up to 2,200 UTF-16 units according to the current endpoint wording. Native app limits may differ. | Put the searchable topic and hook first. Supply spoken/on-screen hook and cover text as creative support, not invented API fields. |
| Instagram feed/Reel | Working caption ceiling: 2,200. API reference has documented 30 hashtags and 20 mentions. Current app guidance can restrict hashtags to 5. | Use no more than 5 relevant hashtags as the conservative default. Verify the exact account and endpoint. Include alt text for supported image surfaces. |
| X standard post | 280 weighted characters. URLs and Unicode use platform weighting. | One clear idea, a specific hook, and an optional concise CTA. Use a thread only when requested or substantively useful. |
| LinkedIn feed post | 3,000 characters. A normal feed post has no separate native title/description/tag field. | Open with a professional problem or useful observation, then evidence or an actionable method and one relevant action. |

Do not call a 5,000-character non-ASCII YouTube description API-valid unless its UTF-8 byte count also fits. The API rejects `<` and `>` in title and description. Tags containing spaces count as if surrounded by quotation marks, and separating commas consume budget. Tags are not hashtags and should not be dumped into the visible description.

X longer-post limits vary by product and documentation. Public help pages conflict across 4,000 and larger ceilings. Default to 280 unless the user's actual account and publishing surface verify a longer allowance. Do not promise a universal paid-tier limit. X URLs normally count as the platform's fixed shortened length rather than their visible string length.

Instagram's official help and developer endpoints returned access/rate-limit errors during this research. The 2,200/30/20 developer wording is indexed and corroborated, but the current live body was not independently retrieved. The five-hashtag app policy is corroborated by current marketing coverage. Treat these as a conservative working profile requiring account-level verification, not a claim that every current API enforces the same hashtag limit. If verification is unavailable, explicitly identify the uncertainty and use up to five hashtags.

## Complete field packages

For YouTube and Shorts, supply title, description, tags as a separate list, hashtags already included in their intended visible field, and optional pinned comment. Include category, language, audience/made-for-kids status, visibility, publishing time/timezone, paid-promotion status, and synthetic-content disclosure as decisions to confirm where applicable. Do not infer a children's designation solely from a casual tone. Timestamps need the actual media. Do not fabricate chapters for an unseen video.

For TikTok, supply the caption, hashtag and mention selections within it, optional cover text and spoken hook, and privacy/comment/duet/stitch decisions applicable to the actual account. For Instagram, supply the caption, included hashtags and mentions, image alt text when supported, optional cover text for a Reel, and any selected location, collaborators, product tags, or disclosures supported by the surface.

For X, supply each final post separately, with alt text for attached images and an explicit thread order if requested. For LinkedIn, supply post body, image alt text where supported, and optional first comment as a separate artifact. Article titles, article bodies, newsletter descriptions, and sponsored-ad fields belong to separate surfaces. Verify their limits before creating them.

## Hashtag practice

Use a few relevant topic, audience, or brand tags. Do not add unrelated trending tags or engagement bait. On YouTube, more than 60 hashtags causes all hashtags on that content to be ignored. That is not a recommendation to approach 60. Defaults of roughly 2–5 relevant tags are editorial starting points, adjusted to the selected platform and audience, not a guarantee of reach.
