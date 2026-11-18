# Sources and interpretation limits

Verified: **2026-11-09**, with the corrections listed under the 2026-11-18 recheck below. Scope: a
descriptive English workflow for Remotion/React video production on local hosts, Node rendering,
Player and optional AWS Lambda. The npm registry showed `remotion` **4.0.545** on 2026-11-18, and some
APIs document future v5 behavior. Check the installed version for operational work. This date does
not guarantee continued availability or authorize automatic updates.

## Requested source and adaptation

Paulo Coutinho's [complete Remotion guide](https://paulox.dev/blog/2026/7/3/remotion-skills-crie-videos-animados-com-ia-do-prompt-a-renderizacao-o-guia-completo/),
published 2026-07-03, is the user-requested source. Its conceptual, production and troubleshooting
sections and embedded generator examples were inspected. This package reorganizes their knowledge
into an actionable English procedure with focused references. It does not redistribute the article's
Python programs or treat their provider constants as universal API contracts.

| Subject from the guide | Knowledge location |
| --- | --- |
| Vocabulary, scene/component model, setup, vendor skills, interactive and direct prompting | Entrypoint workflow |
| Script, structured prompts, six-second launch, 15-second ad and six format recipes | [Prompts and copy](prompts-and-copy.md) |
| Composition, interpolation, springs, stagger, transitions, count-up and motion principles | [Motion and timing](motion-and-timing.md) |
| Real media, visual references, fonts, image/voice/music generators, rights and brand finish | [Assets and generation](assets-and-generation.md) |
| Expressive narration, auditioning, pronunciation, mix metering, scene synchronization and all caption routes | [Audio and captions](audio-and-captions.md) |
| Shadows/glow/blur/gradients, masks, motion blur, GSAP, grain/vignette, 3D and audio response | [Motion and timing](motion-and-timing.md) |
| Physical products, apps, fashion, courses, presentations, safe areas and truthful copy | [Prompts and copy](prompts-and-copy.md) and [assets](assets-and-generation.md) |
| Data-driven variants, dynamic metadata, codecs, transparency, GIF, Player, server render and Lambda | [Rendering and scale](rendering-and-scale.md) |
| Stills, deterministic rendering, missing assets/fonts, audio errors and honest completion | Entrypoint checks and the corresponding technical references |
| Practical inputs, timing and asset handoffs | [Video brief](../assets/video-brief.md) |

## Primary technical contracts inspected

All sources in this table were consulted on the verification date. The consequence column records
the decision supported, not a claim that every linked API was executed or every option exercised.

| Source | Applicable surface and consequence |
| --- | --- |
| [Creating a project](https://www.remotion.dev/docs) | Blank creation command, optional Tailwind, scaffold scripts and current native host requirements |
| [Official Agent Skills](https://www.remotion.dev/docs/ai/skills) | Vendor guidance and installation are separate from this independently usable package |
| [Composition](https://www.remotion.dev/docs/composition) | Registration, metadata, schema/default props and serialization boundary |
| [Sequence](https://www.remotion.dev/docs/sequence) and [timing](https://www.remotion.dev/docs/timing) | Relative frame behavior and the shared `from`/`trimBefore`/`durationInFrames`/`playbackRate`/`loop` props. The timing page states no preference over Sequence wrapping |
| [TransitionSeries](https://www.remotion.dev/docs/transitions/transitionseries) | Overlaps shorten the total, overlays do not, transition length rules and resolved spring duration |
| [Clock wipe](https://www.remotion.dev/docs/transitions/presentations/clock-wipe) and [none](https://www.remotion.dev/docs/transitions/presentations/none) | Radial dimensions and the distinction between no built-in effect and no overlap |
| [GIF input](https://www.remotion.dev/docs/gif) and [Lottie](https://www.remotion.dev/docs/lottie) | Frame-synchronized imported animation and Lottie's SVG/expression limits |
| [GSAP integration](https://www.remotion.dev/docs/gsap) and [useGsapTimeline](https://www.remotion.dev/docs/gsap/use-gsap-timeline) | Current paused-timeline adapter, deterministic builders and forbidden clock/callback/randomness patterns |
| [Three](https://www.remotion.dev/docs/three) | Frame-driven React Three Fiber integration instead of a separate animation loop |
| [Audio visualization](https://www.remotion.dev/docs/visualize-audio) | Power-of-two sample count and source-track frame offsets |
| [Light leaks](https://www.remotion.dev/docs/light-leaks) and [legacy API](https://www.remotion.dev/docs/light-leaks/api) | Current `lightLeak()` from `@remotion/effects/light-leak`. The legacy page marks `@remotion/light-leaks` deprecated and unpublished from Remotion 5.0 |
| [Font loading](https://www.remotion.dev/docs/google-fonts/load-font) | Render readiness, limited variants, v4 no-argument behavior and documented v5 requirements |
| [Audio](https://www.remotion.dev/docs/media/audio) | Current media timing/trim behavior, deprecated `trimAfter`, numeric volume recommendation |
| [Whisper transcription](https://www.remotion.dev/docs/install-whisper-cpp/transcribe) | Local native dependency, 16-bit/16kHz WAV, language/model and timestamp/version decisions |
| [Whisper model download](https://www.remotion.dev/docs/install-whisper-cpp/download-whisper-model) | Model names, model folder and existing-download behavior |
| [Caption pages](https://www.remotion.dev/docs/captions/create-tiktok-style-captions) | Grouping options, absolute token timestamps and whitespace sensitivity |
| [SRT parsing](https://www.remotion.dev/docs/captions/parse-srt) | Existing subtitle text as an alternative to transcription |
| [CLI render](https://www.remotion.dev/docs/cli/render) and [still](https://www.remotion.dev/docs/cli/still) | Explicit entrypoint/ID/output, JSON files for portable props, frame selection and overwrite behavior |
| [Transparent video](https://www.remotion.dev/docs/transparent-videos) | Alpha codecs/pixel formats/intermediate frames and Lambda chunk-boundary limitation |
| [GIF rendering](https://www.remotion.dev/docs/render-as-gif) | GIF export and sampling every nth frame without changing nominal duration |
| [Parameterized rendering](https://www.remotion.dev/docs/parameterized-rendering) and [metadata](https://www.remotion.dev/docs/calculate-metadata) | Default/input props and pre-render metadata transformation |
| [Player](https://www.remotion.dev/docs/player/player) | Direct component preview, explicit input props and composition dimensions/duration |
| [renderMedia](https://www.remotion.dev/docs/renderer/render-media) | Node rendering contract and identical input props during composition selection and export |
| [Lambda setup](https://www.remotion.dev/docs/lambda/setup) and [authentication](https://www.remotion.dev/docs/lambda/authentication) | Execution/caller roles, credential modes, regional resources and explicit account setup |
| [Lambda production checklist](https://www.remotion.dev/docs/lambda/production-checklist) | Cloud production readiness distinct from a small successful local render |
| [Lambda CLI](https://www.remotion.dev/docs/lambda/cli) and [site creation](https://www.remotion.dev/docs/lambda/cli/sites/create) | Region default, bundle upload, returned serve URL, public site requirement and name-based overwrite |
| [Lambda render](https://www.remotion.dev/docs/lambda/cli/render) | Remote output, privacy default, versioned cancellation support and chunk/concurrency controls |
| [License/pricing](https://www.remotion.dev/docs/license/pricing) | Individual/small-company eligibility subject to terms and distinct creator/automation licensing |
| [ElevenLabs speech best practices](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/best-practices) | Voice audition, pronunciation and model-dependent delivery controls. Do not assume one model's tags/options work on all models |
| [ElevenLabs Music compose](https://elevenlabs.io/docs/api-reference/music/compose) | Prompt/plan exclusivity, millisecond length and instrumental option on the applicable request route |
| [FFmpeg ebur128](https://ffmpeg.org/ffmpeg-filters.html#ebur128-1) | Integrated/short-term/momentary loudness and true-peak metering, not automatic normalization |
| [Apple app previews](https://developer.apple.com/app-store/app-previews/) and [specifications](https://developer.apple.com/help/app-store-connect/reference/app-information/app-preview-specifications/) | Actual app footage, device-specific exports, 15–30-second range and preview limits |
| [Agent Skills specification](https://agentskills.io/specification) | Portable entrypoint metadata and focused supporting resources |

## Conflicts and recommendations

- The article's scene ranges sometimes precede adding transitions. Explicit overlap arithmetic in
  this package prevents shortening a requested 15-second export or creating a blank tail.
- The local Whisper example uses `medium.en` alongside Portuguese narration. Use a multilingual
  model for Portuguese. The blog's fixed Whisper version, voice IDs and model defaults are examples,
  not current-account or all-version guarantees.
- Remotion components share the same timing props, and the timing page does not rank them above a
  Sequence wrapper. Follow the project's convention and inspect the installed API before applying new
  timing/media examples. Do not mix `durationInFrames` source trimming with parent placement,
  especially with playback-rate changes.
- GSAP requires a Remotion-owned clock. The researched vendor adapter supports this and replaces
  the need to invent a custom timeline loop on compatible versions.
- A linear amplitude value is not a loudness target. The article's stem targets and separation are
  mix examples, not a universal delivery standard or proof of measured final loudness.
- Exact safe-area pixels, fixed cover crops, frame-zero thumbnail behavior and distribution/retention
  thresholds are not universal platform rules. Treat them as design hypotheses requiring placement
  inspection, rather than repeating unsupported algorithmic guarantees.
- Restrained glow, strong copy, SVG icons, brand consistency and a clear CTA are creative direction.
  They do not prohibit intentional flat design, emoji, linear motion or a typographic scene.
- “Free,” “royalty-free” and an available platform soundtrack do not settle every asset's rights.
  The research did not inspect every listed stock catalog's terms or any user's account eligibility.
  Resolve those for the actual production asset. No generic commercial-use clearance is claimed.

## Recheck on 2026-11-18

These pages were read on 2026-11-18 and corrected or confirmed the stated facts:

- [Getting started](https://www.remotion.dev/docs) and [Linux dependencies](https://www.remotion.dev/docs/miscellaneous/linux-dependencies): macOS 15+, glibc 2.35+, Alpine/NixOS unsupported. [v4 migration](https://www.remotion.dev/docs/4-0-migration) limits Windows to x64. The blank `create-video` command also adds Agent Skills.
- [create-video source](https://github.com/remotion-dev/remotion/tree/main/packages/create-video/src), read 2026-11-18: `init.ts` installs vendor skills only with `--skills`, skips them under `--yes` without that flag, and otherwise prompts. `help.ts` describes `--skills` as installing all Remotion agent skills without prompting. This resolves the getting-started page's ambiguous wording.
- [Agent Skills](https://www.remotion.dev/docs/ai/skills): `npx remotion skills add` inside a project and `npx skills add remotion-dev/skills` without Remotion.
- [Timing](https://www.remotion.dev/docs/timing): shared timing props and the child-frame formula, with no stated preference over `Sequence`.
- [CLI render](https://www.remotion.dev/docs/cli/render) and [still](https://www.remotion.dev/docs/cli/still): overwrite enabled by default, `--overwrite=false`, JSON or file `--props`.
- [Media](https://www.remotion.dev/docs/media) and [Audio](https://www.remotion.dev/docs/media/audio): recommended for new projects, `trimAfter` deprecated in favor of `durationInFrames`, numeric volume recommended.
- [Calculate metadata](https://www.remotion.dev/docs/calculate-metadata): returned metadata/props and the `abortSignal` argument.
- [Lambda render](https://www.remotion.dev/docs/lambda/cli/render) and [region selection](https://www.remotion.dev/docs/lambda/region-selection): optional composition/output arguments, `public`/`private`/`no-acl` privacy and the `us-east-1` default.
- [Blank template configuration](https://github.com/remotion-dev/remotion/tree/main/packages/template-blank): `.prettierrc` without `printWidth`, so the 80-column default applies.

## Professional foundations and access limits

The guide names Richard Williams's *The Animator's Survival Kit* and Frank Thomas/Ollie Johnston's
*The Illusion of Life*. Timing, spacing, anticipation, staging and secondary action provide useful
motion vocabulary. The [Disney publisher page](https://books.disney.com/book/the-illusion-of-life/)
was inspected for bibliographic verification. The Animator's Survival Kit site timed out. Neither
full book was accessed, so both remain further reading rather than fully consulted
texts or additional Remotion requirements.

The guide also names Schwartz, Miller, Ogilvy, Hormozi, Sugarman, Wiebe and Handley as copywriting lenses. Their
books were not accessed in full and their summarized ideas are identified as creative heuristics.
[Cialdini's primary overview](https://www.influenceatwork.com/7-principles-of-persuasion/) was inspected
for the persuasion concepts. It does not establish a conversion prediction for these video recipes.

The attempted separate ElevenLabs voice-settings page redirected to sign-in. The public speech
best-practices page was available. Account-specific voice availability, every model's exact control
range, provider image-size constraints and account-specific commercial permissions remain live
operational checks, not stored universal facts.

These notes come from a documentation adaptation and source review. No video generation, TTS request,
transcription, Remotion render, AWS deployment, cloud job, store upload or publication was performed
to establish these instructions. Mechanical package validation and manual scenario review are
separate from executing those domain operations. The package's [license](../LICENSE.md) covers its
authored content and does not replace third-party licenses or paid service terms.
