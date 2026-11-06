# Metadata, category selection, and artwork

## Form and limits

| Field | Researched requirement | Guidance |
| --- | --- | --- |
| Title | English/Latin-script title with at least one Latin letter, at most 120 characters | Short memorable name that reflects the actual game |
| Description | At least 100 characters for submission, shorter drafts can save | Core mechanic, player fantasy, progression and genuine differentiator |
| How to play | At least 100 characters for submission | Objectives, controls, win/lose conditions and first useful action |
| Category | Required for sandbox/submission, current approved slug | Choose through `get_game_categories`, not a guessed label |
| Supported languages | At least one for form submission. English required by UX rules | List only implemented languages and verify all translations |
| Supported devices | At least one for the form. Current values `IOS`, `ANDROID`, `DESKTOP` | Desktop playability is mandatory. Add mobile claims only when tested |
| Story, when written | English Latin-script text, 150–900 trimmed characters, no links/email | Owner-accurate development note, not invented history |
| Other flags and enum arrays | Current live schema | Multiplayer, orientation, age/content and other declarations must be factual |

The public documentation gives minimums for description/instructions, not a universal verified maximum for every text field. Inspect live schemas/current console before export. Do not invent limits, subtitle/keywords/promotional-text fields, or free-form tags that the tool does not accept. Arrays replace saved arrays completely. Send only intended partial updates.

Optional attribution/model fields must be truthful if supplied and comply with the user's content preferences. Never infer an unknown runtime model ID from a brand name. These fields are distinct from git commit attribution.

## Marketing and taxonomy

Play the game and inspect its code before writing. Identify what players repeatedly do, why it is satisfying, the intended audience, progression, session length, input, and unique verified features. Write a readable title, an opening promise supported by gameplay, and clear instructions. Avoid generic hype, invented player counts, guaranteed rewards, copied competitor text, or deceptive purchase claims.

For puzzle/strategy, emphasize the decision or challenge. For action/runner, explain movement, timing, and progression. For simulation/management, describe the loop and goals. For educational content, describe actual interaction without promising outcomes. Use relevant search language naturally and preserve meaning when localizing. Web discovery and catalog classification do not justify keyword stuffing.

Read `get_game_categories` before setting/changing the category. The current guide returns 30 prioritized choices with examples and exclusion rules. Core gameplay determines category, with specific documented exceptions. The developer's saved category is separate from Playgama's independent catalog classification. A successful save does not prove the public catalog category changed. Respect current taxonomy rather than copying Apple or Google categories/subcategories.

## Cover images

All three current cover slots are required for sandbox publication:

| Slot | Exact dimensions | Accepted encoding | Maximum upload |
| --- | --- | --- | --- |
| `square` | 800×800 | PNG or JPEG | 10 MB |
| `portrait` | 1080×1920 | PNG or JPEG | 10 MB |
| `landscape` | 1920×1080 | PNG or JPEG | 10 MB |

Generate high-quality artwork with the available image model, matched to the actual game's genre/style. Preserve character/object proportions, purposeful composition, readable localized type, and safe framing. Use genuine gameplay captures when representing UI. Avoid hallucinated buttons, misleading gameplay, distorted hands/faces, stretched logos, and clutter. Create separate compositions for different aspect ratios rather than stretching one cover.

Keep editable masters and export exact-size derivatives. Inspect actual file encoding, dimensions, bytes, crop, legibility at small sizes, and licensing. The `format` sent to `start_cover_upload` must match bytes. Confirming publishes a permanent public image and replaces the corresponding saved cover. Preserve intended prior source assets until the replacement is verified.

Screenshots, trailers, and other console assets are not generic fields in the researched form tool. Prepare actual footage/captures and use the supported current console surface when requested. Do not invent an MCP screenshot upload method or submit a preview link as an undeclared form property. Use returned QA/publication/share links rather than guessing deployment URLs.
