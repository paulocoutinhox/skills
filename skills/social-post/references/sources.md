# Sources and freshness

Verified: 2026-11-05. Limits and account capabilities are volatile.

- [YouTube video API fields](https://developers.google.com/youtube/data/reference/rest/v3/videos): title, byte-limited API description, tag accounting.
- [YouTube descriptions](https://support.google.com/youtube/answer/12948449): Studio character limit and creator guidance.
- [YouTube hashtag policy](https://support.google.com/youtube/answer/6390658): hashtag behavior and excessive tagging.
- [TikTok Direct Post](https://developers.tiktok.com/docs/en/content-posting-api-reference-direct-post): API caption and publication settings.
- [Instagram media endpoint](https://developers.facebook.com/docs/instagram-platform/instagram-graph-api/reference/ig-user/media/) and [Instagram help](https://help.instagram.com/351460621611097): live retrieval returned rate limits. Recheck before treating indexed limits as current.
- [Current Instagram hashtag analysis](https://later.com/blog/ultimate-guide-to-using-instagram-hashtags/): corroborates the five-hashtag app change. This is secondary guidance, not an API contract.
- [X posting help](https://help.x.com/en/using-x/how-to-post) and [twitter-text](https://github.com/twitter/twitter-text): standard-post ceiling and weighted parsing.
- [LinkedIn feed posts](https://www.linkedin.com/help/lms/answer/a528176): 3,000-character feed-post limit.
- [YouTube title and thumbnail lesson](https://support.google.com/youtube/answer/12340300), including its linked creator videos: accurate, readable packaging.
- [TikTok video-ad guidance](https://ads.tiktok.com/business/en/guides/video-advertising-guide): hook and action recommendations for ads.
- [LinkedIn content training](https://training.marketing.linkedin.com/path/content-strategy) and [social marketing overview](https://blog.hubspot.com/marketing/social-media-marketing): strategy and measurement context.

- [YouTube GenAI disclosure](https://support.google.com/youtube/answer/14328491?hl=en): checked 2026-11-18. Realistic AI-generated or meaningfully altered content is disclosed through the "AI use" attribute during Studio upload, YouTube adds the label, and production assistance with a script, title or thumbnail does not require disclosure.
- [Instagram hashtag limit coverage](https://www.socialmediatoday.com/news/instagram-implements-new-limits-on-hashtag-use/808309/): checked 2026-11-18. Quotes Instagram's December 18, 2025 statement about gradually limiting post and Reel captions to five hashtags. Secondary coverage of an official statement, not an API contract.
- [YouTube videos resource](https://developers.google.com/youtube/v3/docs/videos): checked 2026-11-18. `snippet.title` is 100 characters and `snippet.description` is 5,000 bytes, both excluding `<` and `>`. `snippet.tags[]` is 500 characters for the whole list, with separating commas counted and tags containing spaces counted as if quoted.
- [TikTok Direct Post](https://developers.tiktok.com/docs/en/content-posting-api-reference-direct-post): checked 2026-11-18. The `title` field is the video caption, with a maximum of 2,200 UTF-16 runes.
- [X counting characters](https://docs.x.com/fundamentals/counting-characters): checked 2026-11-18. A post is limited to 280 weighted characters, URLs count as 23 through t.co, and CJK characters and emoji weigh 2. The X help page returned an access error to automated retrieval on that date.
- [LinkedIn feed posts](https://www.linkedin.com/help/lms/answer/a528176): checked 2026-11-18. Posts can contain up to 3,000 characters.

Marketing recommendations are a synthesis and hypotheses to test. No inaccessible book, unpublished algorithm, or unviewed video is represented as verified evidence.

## Professional foundation and evidence scope

Reviewed: 2026-11-05. April Dunford's [Obviously Awesome](https://www.aprildunford.com/books) and Chip/Dan Heath's [Made to Stick](https://heathbrothers.com/books/made-to-stick/) are professional further reading on positioning and communication. Author descriptions/resources were inspected, not the entire commercial books. Their concepts inform explicit audience/promise/proof questions and do not establish an algorithm or guaranteed performance. The skill is descriptive and uses native-interface validation rather than counters/parsers.

Stored content is maintained only when the user requests a revision. There is no automated source collector or refresh mechanism.
