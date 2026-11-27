# Publications and content prompts

Books, workbooks, social posts, thumbnails and Remotion videos. Read
[how to use the prompts](../task-prompts.md) before you copy one.

## Book

```text
Use book-creator from paulocoutinhox/skills.
First read [SKILLS_ROOT]/book-creator/SKILL.md and the references for the chosen production mode.
Briefly list the skill path you found. If it is missing, say so.

Create [PRINT_DIGITAL_OR_BOTH] editions from [MANUSCRIPT_AND_SOURCES] for [AUDIENCE].
Title, author, language, trim size, and target length: [BOOK_BRIEF].
Citation/layout standard: [ABNT_OR_OTHER]. Production provider/template: [DETAILS_OR_UNDECIDED].
Paper, binding, cover stock/finish, color mode, and ISBN: [DETAILS_OR_UNDECIDED].

Ask about production choices that change page size, layout or exports. This includes front and
back matter, whether the cover goes in the interior PDF, image titles and a list of figures, and
where page numbers go. Set the same styles throughout for headings, body, quotes, notes, citations,
bibliography, tables, and figures.
Justify body text to both margins. Keep interior page backgrounds white. Build working navigation
and a correct bibliography and notes. The book holds only its normal parts and content. It never
has notes about how it was made, the tools used or artificial intelligence.
Make the requested artwork with an available image model and keep its proportions. Check page
breaks, overlaps, readability, bleed and safe areas, and where images sit. Work out the spine from
the final page count and the real paper and binding rules, with author and title where they fit. Do
not make up an ISBN.
Deliver the requested interior PDF and front and back cover PNGs. Add a full-wrap cover for print
or when asked, any required production PDF, editable sources, and a production manifest. Report the
real checks and any missing inputs.
```

## Workbook

```text
Use book-creator from paulocoutinhox/skills.
First read [SKILLS_ROOT]/book-creator/SKILL.md and its references/intake.md and references/typesetting.md.
Briefly list the skill path you found. If it is missing, say so.

Create an A4 workbook from [CONTENT] for [AUDIENCE_AND_LEARNING_GOALS].
Delivery: [PRINT_DIGITAL_OR_BOTH]. Style/citation standard: [ABNT_OR_OTHER].
Exercises, answer space/key, illustrations, and production requirements: [DETAILS].

Ask whether the cover goes in the same PDF and which inner sections are required.
Set readable styles, page margins, spacing, page numbers, notes, citations, and bibliography.
Justify body text, keep page backgrounds white, add working navigation, and keep exercises, figures,
and tables readable across page breaks. Never describe inside the workbook how it was made. Make the
requested illustrations without stretching or squashing them. Prepare the chosen cover and binding
files with the real production sizes. Check the rendered pages. Deliver PDFs, the requested cover
images, editable sources, and a clear list of checks and inputs still open.
```

## Social post

```text
Use social-post from paulocoutinhox/skills.
First read [SKILLS_ROOT]/social-post/SKILL.md and the references for the chosen platforms.
Briefly list the skill path you found. If it is missing, say so.

Prepare copy for [YOUTUBE_SHORTS_TIKTOK_INSTAGRAM_X_LINKEDIN_SELECTION].
Source material and destination link: [TRANSCRIPT_PRODUCT_OR_ARTICLE_AND_URL].
Audience, language, brand voice, goal, and call to action: [BRIEF].
Post formats and required variants: [FORMATS_AND_VARIANTS].

Fit the hook, promise, structure, search-friendly wording, and CTA to each platform and audience.
Return a separate labeled package with every publishing field that applies, including titles,
descriptions/captions, tags, hashtags, links, and accessibility text. Use the field limits written
in the skill, and keep hard limits apart from recommendations. Back up claims with the material you
were given. Avoid misleading hooks and hashtags that do not fit. Name any limit that needs a fresh
check.
Write natural copy for the audience. It never tells how it was made or mentions AI, agents, tools
or prompts. Put a required AI disclosure in the platform's own setting, not in the copy.
Give the copy directly. Do not create counters, datasets, scripts, or automatic updates.
This task prepares content without posting it.
```

## Social thumbnail

```text
Use social-thumbnail from paulocoutinhox/skills.
First read [SKILLS_ROOT]/social-thumbnail/SKILL.md and the matching platform and design references.
Briefly list the skill path you found. If it is missing, say so.

Create thumbnail artwork for [PLATFORM_AND_CONTENT].
Audience, language, main promise, visual identity, and text: [BRIEF].
Reference images, required subjects, and restrictions: [ASSETS_AND_CONSTRAINTS].
Aspect ratio: [RATIO_OR_16:9]. Export format, dimensions, and byte limit: [REQUIREMENTS_OR_ASK].

Ask about any missing export limits. Design an honest, focused layout with readable type, good
contrast and theme, safe placement, and subjects in proportion. Make a high-resolution PNG master
with an available image model. Check text, faces, hands, perspective, and how readable it is at small
size. Prepare the requested versions with the tools already on the system, and meet the real format
and file-size limits. Keep the master. Report the real output properties and any missing tool.
Keep prompts, tool names, production notes and AI captions out of the artwork.
Do not bundle converters, counters, or automatic refresh scripts. Do not publish the artwork.
```

## Remotion video

```text
Use remotion from paulocoutinhox/skills.
First read [SKILLS_ROOT]/remotion/SKILL.md and the references that match the chosen output.
Briefly list the skill path you found. If it is missing, or a different package with the same name
is loaded, say so. Do not quietly use another source instead.

Create or update a Remotion video in [ABSOLUTE_PROJECT_DIRECTORY].
Goal, audience, language and CTA: [BRIEF].
Script, approved product claims/prices and visual references: [CONTENT_AND_REFERENCES].
Real logo, product images, footage, fonts and audio: [ASSET_PATHS_OR_MISSING_ITEMS].
Destination, aspect ratio/dimensions, fps and duration: [OUTPUT_CONTRACT_OR_PROPOSE_DEFAULTS].
Narration, captions, soundtrack and transparency: [REQUIREMENTS_OR_NONE].
Required variants or interactive Player integration: [VARIANTS_OR_NONE].
Allowed paid generation/cloud services, uploads, region and budget: [SCOPE_OR_NONE].

Look at the project and assets. Then turn the script into a table of scenes and frames. Build
components that give the same frames every time, with explicit type, colors, holds long enough to
read and correct math for overlapping transitions. Prepare the approved media and measure the
speech before you fix scene lengths. Stop voices from overlapping and sync the reviewed captions to
those same audio files. Use safe areas for each placement.
Narration, captions, on-screen text and metadata talk about the subject, never about how the video
was made.

Check key still frames, including frame zero, scene holds, transitions and the last frame. Run the
project checks that apply, render the requested local output, and watch the full video with sound
and on mute. For reusable variants, check different inputs and one failure case that matters before
you make many.
Use cloud rendering only within the allowed scope. Do not publish or deploy outside that scope.

Deliver source paths, composition IDs, rendered files, sample stills, final timing and props, and
commands that rebuild the result. Report the real media properties, checks and the exact steps not
done or blocked.
Do not create generation or batch automation scripts unless asked for them separately.
```
