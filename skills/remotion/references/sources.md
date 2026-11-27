# Sources and interpretation limits

Checked: **2026-11-09** and checked again on **2026-11-18**. Scope: a descriptive English workflow
for Remotion/React video production on local machines, Node rendering, Player and optional AWS
Lambda. The npm registry showed `remotion` **4.0.545** on 2026-11-18. Check the installed version
for real work. This date does not promise that things stay available, and it does not allow
automatic updates.

## Requested source and adaptation

Paulo Coutinho's [complete Remotion guide](https://paulox.dev/blog/2026/7/3/remotion-skills-crie-videos-animados-com-ia-do-prompt-a-renderizacao-o-guia-completo/),
published 2026-07-03, is the source the user asked for. These references call it the source guide.
Its concept, production and troubleshooting sections and its embedded generator examples were
read. This package reorganizes that knowledge into a clear English procedure with focused
references. It does not redistribute the source guide's Python programs, and it does not treat
their provider constants as API rules that apply everywhere.

| Subject from the guide | Where to find it |
| --- | --- |
| Vocabulary, scene/component model, setup, vendor skills, interactive and direct prompting | Entrypoint workflow |
| Script, structured prompts, six-second launch, 15-second ad and six format recipes | [Prompts and copy](prompts-and-copy.md) |
| Composition, interpolation, springs, stagger, transitions, count-up and motion principles | [Motion and timing](motion-and-timing.md) |
| Real media, visual references, fonts, image/voice/music generators, rights and brand finish | [Assets and generation](assets-and-generation.md) |
| Expressive narration, voice tryouts, pronunciation, mix metering, scene sync and all caption routes | [Audio and captions](audio-and-captions.md) |
| Shadows/glow/blur/gradients, masks, motion blur, GSAP, grain/vignette, 3D and audio response | [Motion and timing](motion-and-timing.md) |
| Physical products, apps, fashion, courses, presentations, safe areas and honest copy | [Prompts and copy](prompts-and-copy.md) and [assets](assets-and-generation.md) |
| Data-driven variants, dynamic metadata, codecs, transparency, GIF, Player, server render and Lambda | [Rendering and scale](rendering-and-scale.md) |
| Stills, rendering the same every time, missing assets/fonts, audio errors and honest completion | Entrypoint checks and the matching technical references |
| Practical inputs, timing and asset handoffs | [Video brief](../assets/video-brief.md) |

## Main technical sources checked

All sources in this table were read on the check date. The second column records the decision each
source supports. It does not claim that every linked API was run or every option was tried.

| Source | What it covers and what it means here |
| --- | --- |
| [Creating a project](https://www.remotion.dev/docs) | Blank creation command, optional Tailwind, scaffold scripts and current native machine requirements |
| [Official Agent Skills](https://www.remotion.dev/docs/ai/skills) | Vendor guidance and installation are separate from this package, which works on its own |
| [Composition](https://www.remotion.dev/docs/composition) | Registration, metadata, schema/default props and serialization limit |
| [Sequence](https://www.remotion.dev/docs/sequence) and [timing](https://www.remotion.dev/docs/timing) | Relative frame behavior and the shared `from`/`trimBefore`/`durationInFrames`/`playbackRate`/`loop` props. The timing page does not prefer them over Sequence wrapping |
| [TransitionSeries](https://www.remotion.dev/docs/transitions/transitionseries) | Overlaps shorten the total, overlays do not, transition length rules and the final spring duration |
| [Clock wipe](https://www.remotion.dev/docs/transitions/presentations/clock-wipe) and [none](https://www.remotion.dev/docs/transitions/presentations/none) | Radial dimensions and the difference between no built-in effect and no overlap |
| [GIF input](https://www.remotion.dev/docs/gif) and [Lottie](https://www.remotion.dev/docs/lottie) | Imported animation kept in sync with the frame, and Lottie's SVG/expression limits |
| [GSAP integration](https://www.remotion.dev/docs/gsap) and [useGsapTimeline](https://www.remotion.dev/docs/gsap/use-gsap-timeline) | Current paused-timeline adapter, builders that give the same result every time, and banned clock/callback/randomness patterns |
| [Three](https://www.remotion.dev/docs/three) | React Three Fiber driven by the frame instead of a separate animation loop |
| [Audio visualization](https://www.remotion.dev/docs/visualize-audio) | Power-of-two sample count and source-track frame offsets |
| [Light leaks](https://www.remotion.dev/docs/light-leaks) | `lightLeak()` from `@remotion/effects/light-leak` |
| [Font loading](https://www.remotion.dev/docs/google-fonts/load-font) | Render readiness, limited variants and explicit `weights` and `subsets` |
| [Audio](https://www.remotion.dev/docs/media/audio) | Current media timing/trim behavior, deprecated `trimAfter`, numeric volume recommendation |
| [Whisper transcription](https://www.remotion.dev/docs/install-whisper-cpp/transcribe) | Local native dependency, 16-bit/16kHz WAV, language/model and timestamp/version decisions |
| [Whisper model download](https://www.remotion.dev/docs/install-whisper-cpp/download-whisper-model) | Model names, model folder and what happens with an existing download |
| [Caption pages](https://www.remotion.dev/docs/captions/create-tiktok-style-captions) | Grouping options, absolute token timestamps and sensitivity to whitespace |
| [SRT parsing](https://www.remotion.dev/docs/captions/parse-srt) | Existing subtitle text as an alternative to transcription |
| [CLI render](https://www.remotion.dev/docs/cli/render) and [still](https://www.remotion.dev/docs/cli/still) | Explicit entrypoint/ID/output, JSON files for portable props, frame selection and overwrite behavior |
| [Transparent video](https://www.remotion.dev/docs/transparent-videos) | Alpha codecs/pixel formats/intermediate frames and the Lambda chunk-boundary limit |
| [GIF rendering](https://www.remotion.dev/docs/render-as-gif) | GIF export and sampling every nth frame without changing the stated duration |
| [Parameterized rendering](https://www.remotion.dev/docs/parameterized-rendering) and [metadata](https://www.remotion.dev/docs/calculate-metadata) | Default/input props and changing metadata before the render |
| [Player](https://www.remotion.dev/docs/player/player) | Direct component preview, explicit input props and composition dimensions/duration |
| [renderMedia](https://www.remotion.dev/docs/renderer/render-media) | Node rendering contract and the same input props during composition selection and export |
| [Lambda setup](https://www.remotion.dev/docs/lambda/setup) and [authentication](https://www.remotion.dev/docs/lambda/authentication) | Execution/caller roles, credential modes, regional resources and explicit account setup |
| [Lambda production checklist](https://www.remotion.dev/docs/lambda/production-checklist) | Cloud production readiness, which is different from one small successful local render |
| [Lambda CLI](https://www.remotion.dev/docs/lambda/cli) and [site creation](https://www.remotion.dev/docs/lambda/cli/sites/create) | Region default, bundle upload, returned serve URL, public site requirement and overwrite by name |
| [Lambda render](https://www.remotion.dev/docs/lambda/cli/render) | Remote output, privacy default, cancellation support by version and chunk/concurrency controls |
| [License/pricing](https://www.remotion.dev/docs/license/pricing) | Eligibility for individuals/small companies under its terms, and separate creator/automation licensing |
| [ElevenLabs speech best practices](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/best-practices) | Voice tryouts, pronunciation and delivery controls that depend on the model. Do not assume one model's tags/options work on all models |
| [ElevenLabs Music compose](https://elevenlabs.io/docs/api-reference/music/compose) | Prompt and plan cannot be used together, length in milliseconds and the instrumental option on the matching request route |
| [FFmpeg ebur128](https://ffmpeg.org/ffmpeg-filters.html#ebur128-1) | Integrated/short-term/momentary loudness and true-peak metering, not automatic normalization |
| [Apple app previews](https://developer.apple.com/app-store/app-previews/) and [specifications](https://developer.apple.com/help/app-store-connect/reference/app-information/app-preview-specifications/) | Real app footage, exports for each device, 15–30-second range and preview limits |
| [Agent Skills specification](https://agentskills.io/specification) | Portable entrypoint metadata and focused supporting resources |

## Conflicts and recommendations

- The source guide sometimes sets scene ranges before it adds transitions. This package spells out
  the overlap math so a requested 15-second export does not come out shorter or end on blank frames.
- The local Whisper example uses `medium.en` with Portuguese narration. Use a multilingual
  model for Portuguese. The source guide's fixed Whisper version, voice IDs and model defaults are
  examples. They are not promises about the current account or every version.
- Remotion components share the same timing props, and the timing page does not rank them above a
  Sequence wrapper. Follow the project's habit and check the installed API before you use new
  timing/media examples. Do not mix `durationInFrames` source trimming with parent placement,
  especially when the playback rate changes.
- GSAP needs a clock that Remotion controls. The checked vendor adapter supports this, so on
  compatible versions you do not need to invent your own timeline loop.
- A linear amplitude value is not a loudness target. The source guide's stem targets and separation
  are mix examples. They are not a delivery standard for everyone or proof of the measured final
  loudness.
- Exact safe-area pixels, fixed cover crops, frame-zero thumbnail behavior and reach/retention
  numbers are not rules on every platform. Treat them as design guesses that need checking in the
  real placement, and do not repeat unsupported promises about algorithms.
- Light glow, strong copy, SVG icons, brand consistency and a clear CTA are creative direction.
  They do not forbid planned flat design, emoji, linear motion or a scene made only of text.
- “Free,” “royalty-free” and an available platform soundtrack do not settle every asset's rights.
  The research did not read the terms of every listed stock catalog or check any user's account
  eligibility. Settle those for the real production asset. No general commercial-use clearance is
  claimed.

## Recheck on 2026-11-18

These pages were read on 2026-11-18:

- [Getting started](https://www.remotion.dev/docs) and [Linux dependencies](https://www.remotion.dev/docs/miscellaneous/linux-dependencies): macOS 15+, glibc 2.35+, Alpine/NixOS not supported. The [Remotion 4.0 notes](https://www.remotion.dev/docs/4-0-migration) limit Windows to x64. The blank `create-video` command offers vendor Agent Skills, installed only with `--skills`.
- [create-video source](https://github.com/remotion-dev/remotion/tree/main/packages/create-video/src), read 2026-11-18: `init.ts` installs vendor skills only with `--skills`, skips them under `--yes` without that flag, and asks otherwise. `help.ts` describes `--skills` as installing all Remotion agent skills without asking. This settles the unclear wording on the getting-started page.
- [Agent Skills](https://www.remotion.dev/docs/ai/skills): `npx remotion skills add` inside a project and `npx skills add remotion-dev/skills` without Remotion.
- [Timing](https://www.remotion.dev/docs/timing): shared timing props and the child-frame formula, with no stated preference over `Sequence`.
- [CLI render](https://www.remotion.dev/docs/cli/render) and [still](https://www.remotion.dev/docs/cli/still): overwrite on by default, `--overwrite=false`, JSON or file `--props`.
- [Media](https://www.remotion.dev/docs/media) and [Audio](https://www.remotion.dev/docs/media/audio): recommended for new projects, `trimAfter` deprecated in favor of `durationInFrames`, numeric volume recommended.
- [Calculate metadata](https://www.remotion.dev/docs/calculate-metadata): returned metadata/props and the `abortSignal` argument.
- [Lambda render](https://www.remotion.dev/docs/lambda/cli/render) and [region selection](https://www.remotion.dev/docs/lambda/region-selection): optional composition/output arguments, `public`/`private`/`no-acl` privacy and the `us-east-1` default.
- [Blank template configuration](https://github.com/remotion-dev/remotion/tree/main/packages/template-blank): `.prettierrc` without `printWidth`, so the 80-column default applies.

## Professional foundations and access limits

The guide names Richard Williams's *The Animator's Survival Kit* and Frank Thomas/Ollie Johnston's
*The Illusion of Life*. Timing, spacing, anticipation, staging and secondary action give useful
words for motion. The [Disney publisher page](https://books.disney.com/book/the-illusion-of-life/)
was read to confirm the book details. The Animator's Survival Kit site timed out. Neither
full book was read, so both stay as further reading. They are not fully read texts or extra
Remotion requirements.

The guide also names Schwartz, Miller, Ogilvy, Hormozi, Sugarman, Wiebe and Handley as ways to think
about copywriting. Their books were not read in full, and their summarized ideas are marked as
creative rules of thumb.
[Cialdini's primary overview](https://www.influenceatwork.com/7-principles-of-persuasion/) was read
for the persuasion ideas. It does not predict conversion for these video recipes.

The separate ElevenLabs voice-settings page that was tried redirected to sign-in. The public speech
best-practices page was available. Voice availability for an account, every model's exact control
range, provider image-size limits and an account's commercial permissions stay as live checks at
work time. They are not stored facts that apply everywhere.

These notes come from adapting documentation and reviewing sources. No video generation, TTS
request, transcription, Remotion render, AWS deployment, cloud job, store upload or publishing was
done to write these instructions. Mechanical package validation and manual scenario review are
separate from running those domain operations. The package's [license](../LICENSE.md) covers its
own written content and does not replace third-party licenses or paid service terms.
