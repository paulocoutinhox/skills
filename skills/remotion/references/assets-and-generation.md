# Assets, generation and brand consistency

Use approved product material and references before inventing substitutes. A reference image can
serve as actual footage/artwork, visual direction, or both. Identify its role explicitly. Extract
palette, typography, hierarchy and motion intent from a reference without promising to reconstruct
unseen product geometry or treating a competitor's screenshot as freely reusable marketing media.

## Organize the handoff

Use only the directories needed by the project, for example:

```text
public/
  brand/                 Approved logo variants
  img/                   Product images and scene backgrounds
  footage/               Screen recordings and filmed demonstrations
  fonts/                 Licensed local fonts
  vo/                    Approved speech clips by scene
  music/                 Licensed music bed
```

Refer to `public/brand/logo-light.svg` as `staticFile('brand/logo-light.svg')`. Case and nested folders
must match exactly. Use stable scene/asset identities, preserve masters, and keep previous approved
generations outside replacement paths until their successors are inspected. Outputs do not belong
in `public/` unless the project needs to consume them as inputs.

Record local path, source, rights, attribution, model/tool, prompt/settings and revision in the
[brief](../assets/video-brief.md). Keep this record human-readable. Do not store credentials, model
downloads, API responses containing private data, or generated vendor catalogs in the skill package.

## Image, voice and music generation as separate decisions

The source article demonstrates independent image, voice and music generators followed by Remotion
assembly. Preserve that separation of inputs and outputs. Use existing native/connected tools when
available. An unavailable generator does not prevent building scene structure or using supplied media.
These generation operations are optional and can incur cost or upload private material.

| Stage | Required input | Artifact and verification |
| --- | --- | --- |
| Scene image | Visual message, reference, aspect ratio, subject placement, negative space, output path | Inspect subject, brand accuracy, dimensions, crop, artifacts and text clearance |
| Speech | Approved spoken script, language, account-available voice/model, delivery direction | Listen, check pronunciation and record actual duration per scene |
| Music | Mood, tempo/energy arc, duration, instrumental/vocal choice, authorized provider/license | Listen for speech conflicts, endings, distortion and usable duration |
| Assembly | Approved assets plus measured timings | Deterministic composition and inspected render |

For an image request, describe how it supports that scene's claim and where text will sit. Prefer
real product photography or a verified screen recording when authenticity matters. Put overlay copy
in Remotion rather than relying on an image model to spell small product text. Never fabricate an
app screenshot, customer or testimonial as documentary proof.

Use the selected generator's **actual** model and supported output sizes. A request for 1080×1920
does not prove an image API accepts that exact size. Generate at an accepted size/aspect, then use
the approved editor/native workflow for a deliberate crop/resize, preserving the subject and alpha.
Validate the final dimensions and do not stretch subjects to fit. Select PNG for alpha, or a suitable
JPEG/WebP for opaque imagery after checking compatibility and quality. Do not copy the article's
provider-specific dimension arithmetic into a universal API requirement.

For voice, follow [speech and timing](audio-and-captions.md). Avoid passing a key on a command line
where shell history or logs can retain it. Use the environment or the provider's credential mechanism.
Only load an existing `.env` using the project's documented workflow, and keep it outside public files.

For generated music, describe a speech-friendly bed and a purposeful end/payoff. The researched
ElevenLabs Music API accepts a simple `prompt` or a `composition_plan`, not both. With a prompt,
`music_length_ms` expresses milliseconds, and `force_instrumental` can request instrumental output.
Verify the chosen model's live duration, access and format limits before generating. A seconds value
must not be passed as milliseconds. Check actual returned audio instead of trusting a requested
duration. Generated or “royalty-free” does not mean unrestricted under every provider plan/use case.

If the user specifically requests reusable automation in their own video project, implement focused
Python 3.11+ commands with uv, explicit inputs/outputs and provider error handling. Keep keys out of
arguments/logs, reject unsupported sizes and missing text, preserve inputs, and do not silently
overwrite approved outputs. Reconcile a timed-out paid request before repeating it. Only create an
orchestrator when requested. This descriptive skill contains no copied generator scripts or wrappers.
Native Remotion/React code and direct vendor commands remain appropriate project tools.

## Rights and asset discovery

The following are discovery options from the article, not blanket clearance:

- Music: YouTube Audio Library, Pixabay Music, Uppbeat, Epidemic Sound and Artlist.
- Photos/video: Pexels, Unsplash and Pixabay.
- Icons: Lucide, Heroicons, Tabler and Phosphor.
- Fonts: Google Fonts or owner-supplied licensed files.

Check the particular asset, track, subscription, attribution condition, commercial/advertising scope,
territory and platform permissions. Stock-media permissions do not automatically clear every
recognizable person, trademark or property. Keep required license notices. Verify the current license
instead of assuming every item in a catalog has identical terms.

Platform-provided trending audio may have account, commercial-use and distribution restrictions.
Do not bake it into an export for arbitrary redistribution on the assumption that in-app availability
grants those rights. Prepare a clean master or a separately licensed mix when the publishing workflow
adds approved music later. Do not claim that trending audio guarantees reach.

## Readiness and font integrity

Use Remotion media components that coordinate with rendering. Prefer stable, authorized local assets
for reproducible offline/cloud operation. A remote URL behind login or an expiring signature may
work in Studio and fail during a server render. Check the actual renderer's access without making
private media publicly readable as a workaround.

`@remotion/google-fonts` loads a real font and blocks rendering until ready. Limit weights, styles
and subsets. In v4, a no-argument `loadFont()` can fetch every variant. The researched docs describe
nonempty weight/subset arrays as required starting in v5. Inspect the actual version and selected
font's options. Test the video's accent marks, currency and punctuation. Portuguese characters may
already be covered by a font's Latin subset. Do not claim that `latin-ext` is always necessary.

Use `@remotion/fonts` to load licensed local font files when reproducibility/network restrictions
make that preferable. Confirm the actual loaded font in a still, including a long heading. Local
font availability on the developer's desktop does not prove headless Chrome has the same font.

## Finish the brand deliberately

Use exact approved brand colors. Prefer an owner-supplied light logo on dark footage and a dark logo
on light backgrounds. Recolor an editable SVG only when the brand permits it. Preserve the source
and check multi-color artwork rather than globally replacing every dark fill. A discreet symbol
watermark is optional. It must not compete with subtitles or the CTA.

Use a consistent SVG icon family and stroke/weight. Lucide and Phosphor are examples. Emoji glyphs
vary across render hosts, so deliberate SVG artwork can improve consistency. Emoji can still be an
intentional style choice. Align cards and imagery on a grid. Use depth, shadows and colored accents
to establish hierarchy rather than giving every object a border and glow.

Choose scene imagery that supports the spoken idea. Add a restrained pan/zoom with crop headroom,
a dark or light scrim, and enough contrast for readable text. Human faces can support an emotional
beat when relevant and authorized. Do not imply that every scene needs a face or generated photo.

Make the end card calm: one action, short copy, visible destination/instruction if relevant, and a
hold long enough to read. Uppercase with letter spacing is an optional brand treatment, not a
conversion requirement. Text burned into an MP4 is not an interactive button or clickable link.
Use “link in bio” or a comment reference only if that is the actual authorized publishing plan.

The article's sample 120px top and 220px bottom reserves at 1080×1920 are drafting values. Actual
placement may need more room, including right-side buttons and cover/grid crops. Review current
platform overlays and a representative device preview. Do not impose a fixed bottom percentage or
square center crop on every platform. Keep the important subject, caption and CTA readable together.
