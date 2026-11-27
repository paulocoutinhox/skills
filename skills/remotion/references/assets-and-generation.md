# Assets, generation and brand consistency

Use approved product material and references before you invent stand-ins. A reference image can be
real footage/artwork, visual direction, or both. Say clearly which role it plays. Take the colors,
typography, hierarchy and motion intent from a reference. Do not promise to rebuild product shapes
that are not shown, and do not treat a competitor's screenshot as free marketing media.

## Organize the handoff

Use only the directories the project needs, for example:

```text
public/
  brand/                 Approved logo variants
  img/                   Product images and scene backgrounds
  footage/               Screen recordings and filmed demonstrations
  fonts/                 Licensed local fonts
  vo/                    Approved speech clips by scene
  music/                 Licensed music bed
```

Refer to `public/brand/logo-light.svg` as `staticFile('brand/logo-light.svg')`. Case and nested
folders must match exactly. Use stable scene/asset names, keep masters, and keep earlier approved
generations out of the replacement paths until you have checked the new versions. Outputs do not
belong in `public/` unless the project needs to use them as inputs.

Record the local path, source, rights, attribution, model/tool, prompt/settings and revision in the
[brief](../assets/video-brief.md). Keep this record easy for people to read. Do not store
credentials, model downloads, API responses with private data, or generated vendor catalogs in the
skill package.

## Image, voice and music generation as separate decisions

The source guide in [sources](sources.md) shows separate image, voice and music generators,
followed by putting everything together in Remotion. Keep those inputs and outputs separate. Use
the native/connected tools you already have. If a generator is not available, you can still build
the scene structure or use supplied media. These generation steps are optional, and they can cost
money or upload private material.

| Stage | Required input | Output and how to check it |
| --- | --- | --- |
| Scene image | Visual message, reference, aspect ratio, subject placement, empty space, output path | Check subject, brand accuracy, dimensions, crop, artifacts and room for text |
| Speech | Approved spoken script, language, a voice/model the account can use, delivery direction | Listen, check pronunciation and record the real duration per scene |
| Music | Mood, tempo/energy arc, duration, instrumental/vocal choice, approved provider/license | Listen for clashes with speech, endings, distortion and usable duration |
| Assembly | Approved assets plus measured timings | A composition that renders the same every time, and a checked render |

For an image request, describe how it supports that scene's claim and where text will sit. Prefer
real product photos or a checked screen recording when it matters that the image is genuine. Put
overlay text in Remotion instead of counting on an image model to spell small product text. Never
fake an app screenshot, customer or testimonial as proof.

Use the chosen generator's **real** model and supported output sizes. Asking for 1080×1920 does not
prove an image API accepts that exact size. Generate at an accepted size/aspect, then use the
approved editor/native workflow to crop/resize on purpose, keeping the subject and alpha.
Check the final dimensions and do not stretch subjects to fit. Pick PNG for alpha, or a suitable
JPEG/WebP for opaque images after you check compatibility and quality. Do not turn the source
guide's provider-specific size math into an API rule for everyone.

For voice, follow [speech and timing](audio-and-captions.md). Avoid passing a key on a command line,
where shell history or logs can keep it. Use the environment or the provider's credential method.
Load an existing `.env` only through the project's documented workflow, and keep it out of public
files.

For generated music, describe a bed that leaves room for speech and an end/payoff with a purpose.
The checked ElevenLabs Music API accepts a simple `prompt` or a `composition_plan`, not both. With a
prompt, `music_length_ms` is in milliseconds, and `force_instrumental` can ask for instrumental
output. Check the chosen model's current duration, access and format limits before you generate. Do
not pass a value in seconds as milliseconds. Check the audio you really get back instead of trusting
the requested duration. Generated or “royalty-free” does not mean free of limits under every
provider plan/use case.

If the user specifically asks for reusable automation in their own video project, write focused
Python 3.11+ commands with uv, explicit inputs/outputs and provider error handling. Keep keys out of
arguments/logs, reject unsupported sizes and missing text, keep inputs, and do not quietly overwrite
approved outputs. Check what happened to a paid request that timed out before you repeat it. Create
an orchestrator only when asked. This descriptive skill has no copied generator scripts or wrappers.
Native Remotion/React code and direct vendor commands are still fine project tools.

## Rights and asset discovery

These are places to look from the source guide, not blanket clearance:

- Music: YouTube Audio Library, Pixabay Music, Uppbeat, Epidemic Sound and Artlist.
- Photos/video: Pexels, Unsplash and Pixabay.
- Icons: Lucide, Heroicons, Tabler and Phosphor.
- Fonts: Google Fonts or licensed files supplied by the owner.

Check the specific asset, track, subscription, attribution terms, commercial/advertising scope,
territory and platform permissions. Stock-media permissions do not automatically clear every
recognizable person, trademark or property. Keep required license notices. Check the current license
instead of assuming every item in a catalog has the same terms.

Trending audio offered by a platform may have account, commercial-use and distribution limits.
Do not bake it into an export for any redistribution just because the app offers it. Prepare a clean
master or a separately licensed mix when the publishing workflow adds approved music later. Do not
claim that trending audio guarantees reach.

## Readiness and font integrity

Use Remotion media components that work with rendering. Prefer stable, approved local assets so
offline/cloud runs give the same result. A remote URL behind a login or with an expiring signature
may work in Studio and fail during a server render. Check that the real renderer can reach it,
without making private media public as a workaround.

`@remotion/google-fonts` loads a real font and blocks rendering until it is ready. Limit weights,
styles and subsets. Always pass explicit `weights` and `subsets` to `loadFont()`. Check the chosen
font's options. Test the video's accent marks, currency and punctuation. A font's Latin subset may
already cover Portuguese characters. Do not claim that `latin-ext` is always needed.

Use `@remotion/fonts` to load licensed local font files when repeatable results or network limits
make that the better choice. Confirm the font that really loaded in a still, including a long
heading. Having the font on the developer's desktop does not prove headless Chrome has the same font.

## Finish the brand with care

Use the exact approved brand colors. Prefer a light logo supplied by the owner on dark footage and a
dark logo on light backgrounds. Recolor an editable SVG only when the brand allows it. Keep the
source and check multi-color artwork instead of replacing every dark fill at once. A small symbol
watermark is optional. It must not compete with subtitles or the CTA.

Use one SVG icon family with a matching stroke/weight. Lucide and Phosphor are examples. Emoji
glyphs look different on different render machines, so planned SVG artwork can look more
consistent. Emoji can still be a style choice made on purpose. Line up cards and images on a grid.
Use depth, shadows and colored accents to show hierarchy instead of giving every object a border
and glow.

Pick scene images that support the spoken idea. Add a gentle pan/zoom with room to crop,
a dark or light scrim, and enough contrast for readable text. Human faces can help an emotional
beat when they fit and are approved. Do not suggest that every scene needs a face or generated photo.

Keep the end card calm: one action, short text, a visible destination/instruction if relevant, and a
hold long enough to read. Uppercase with letter spacing is an optional brand style, not a
conversion requirement. Text burned into an MP4 is not an interactive button or clickable link.
Use “link in bio” or a comment reference only if that is the real approved publishing plan.

The source guide's sample 120px top and 220px bottom margins at 1080×1920 are draft values.
The real placement may need more room, including right-side buttons and cover/grid crops. Review
current platform overlays and a typical device preview. Do not force a fixed bottom percentage or
square center crop on every platform. Keep the main subject, caption and CTA readable together.
