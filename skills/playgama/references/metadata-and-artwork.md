# Metadata, category selection, and artwork

## Form and limits

| Field | Researched requirement | Guidance |
| --- | --- | --- |
| Title | English/Latin-script title with at least one Latin letter, at most 120 characters | Short, easy-to-remember name that fits the real game |
| Description | At least 100 characters for submission, shorter drafts can save | Core mechanic, what the player gets to be or do, progress and a real difference from other games |
| How to play | At least 100 characters for submission | Goals, controls, how you win or lose and the first useful action |
| Category | Required for sandbox and submission, current approved slug | Choose through `get_game_categories`, not a guessed label |
| Supported languages | At least one for form submission. English required by UX rules | List only languages the game really has and check all translations |
| Supported devices | At least one for the form. Current values `IOS`, `ANDROID`, `DESKTOP` | Desktop play is mandatory. Claim mobile only when tested |
| Story, when written | English Latin-script text, 150–900 characters after trimming, no links/email | Development note the owner confirms as accurate, not invented history |
| Other flags and enum arrays | Current live schema | Multiplayer, orientation, age and content and other declarations must be true |

The public documentation gives minimums for description and instructions, not a confirmed maximum for every text field. Check the live schemas or the current console before export. Do not invent limits, subtitle, keywords or promotional-text fields, or free-form tags that the tool does not accept. Arrays fully replace the saved arrays. Send only the partial updates you mean to make.

`create_application` and `update_application_form` also accept optional `agent`, `model` and `modelId` declaration fields that describe the coding agent and model used to build the game. Use `agent: none` and leave out the other two for a game made without an agent. Fill them only from facts the owner confirms or the runtime really reports. Never guess a model ID from a brand name. These declaration fields are the only place for that information. They are separate from git commit attribution.

Title, description, how-to-play, story and cover text are product content that players see. Describe the game itself. Never describe how the text or art was made, and never mention AI, agents, tools or prompts in them unless the owner asks for it. A story is the developer's account of the game's idea and development, written in the owner's voice from facts they give.

## Marketing and taxonomy

Play the game and look at its code before writing. Find out what players do again and again, why it is fun, the intended audience, progress, session length, input, and the unique features you have confirmed. Write a readable title, an opening promise that the gameplay backs up, and clear instructions. Avoid generic hype, made-up player counts, promised rewards, copied competitor text, or misleading purchase claims.

For puzzle or strategy games, stress the decision or challenge. For action or runner games, explain movement, timing, and progress. For simulation or management games, describe the loop and goals. For learning content, describe the real interaction without promising results. Use relevant search words naturally and keep the meaning when translating. Web search and catalog classification do not justify keyword stuffing.

Read `get_game_categories` before setting or changing the category. The current guide returns 30 ranked choices with examples and exclusion rules. Core gameplay decides the category, with some documented exceptions. The category the developer saves is separate from Playgama's own catalog classification. A successful save does not prove that the public catalog category changed. Follow the current category list rather than copying Apple or Google categories and subcategories.

## Cover images

All three current cover slots are required for sandbox publication:

| Slot | Exact dimensions | Accepted encoding | Maximum upload |
| --- | --- | --- | --- |
| `square` | 800×800 | PNG or JPEG | 10 MB |
| `portrait` | 1080×1920 | PNG or JPEG | 10 MB |
| `landscape` | 1920×1080 | PNG or JPEG | 10 MB |

The confirmed cover is also tagged by slot: `square` is the `icon`, `portrait` is `preview_vertical` and `landscape` is `preview`. The console shows them as rounded cards on a dark background, small next to the game title, so judge them there too.

### Cover art standard

A cover is store key art, at the level of the top games in the catalog. It sells the feeling of playing, not the interface:

- The game's real logo sits inside an illustrated scene of the game's own objects and mechanic, with depth, lighting, motion and one clear focal point. A brick breaker shows bricks bursting, the ball streaking through and the paddle. A runner shows the hero mid-jump. The scene matches the game's real art style, colors and characters.
- A screenshot, a UI capture inside a frame, a menu, a HUD or a logo floating over a plain gradient is not a cover. Such images look low quality at card size and do not attract players. Real gameplay captures belong in screenshots and videos, not in covers.
- Generate the illustration without any text, logo or UI. Give the image model the game's logo and icon as style references and ask for calm space where the logo goes. Then place the official logo file over it, scaled large, with a soft dark glow behind it for contrast. This keeps the name exact and on-brand. Never let the image model write the title.
- When no image generator is available, use art the owner supplies or commissions that meets this standard. Until that art exists, report the three cover slots as blocked rather than uploading a screenshot or placeholder.
- Recompose each slot: wide action with the logo in the upper center for `landscape`, a tall scene with the logo in the upper third for `portrait`, and a compact square with the logo on top for `square`. Never stretch or letterbox one image into another ratio.
- Check every slot at full size and as a thumbnail on a dark background: the logo reads, the rounded corners cut nothing important, colors are bright rather than dark or washed out, and the scene is not cluttered.

Keep character and object proportions, a purposeful layout and safe framing. Avoid made-up buttons, misleading gameplay, distorted hands or faces, stretched logos, and clutter.

Keep editable master files and export copies at the exact size. Check the real file encoding, dimensions, bytes, crop, readability at small sizes, and licensing. The `format` sent to `start_cover_upload` must match the bytes. Confirming publishes a permanent public image and replaces the matching saved cover. Keep the earlier source files you need until the replacement is checked.

Screenshots, trailers, and other console assets are not general fields in the form tool checked. Prepare real footage and captures and use the supported current console page when asked. Do not invent an MCP screenshot upload method or send a preview link as a form property that is not declared. Use the returned QA, publication and share links rather than guessing deployment URLs.
