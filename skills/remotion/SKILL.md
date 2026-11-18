---
name: remotion
description: Create, refine, and render programmatic videos with Remotion and React from scripts, prompts, brand assets, or data. Use for animated ads, product demos, course graphics, captions, motion design, reusable video templates, Player previews, local/server rendering, and authorized AWS Lambda rendering.
license: MIT
---

# Remotion

Turn a brief into a reproducible video: narrative, storyboard, frame-driven React scenes, prepared
media, inspected previews, and verified exports. This English workflow adapts Paulo Coutinho's
Remotion guide and checks technical contracts against official documentation. Read
[sources and interpretation limits](references/sources.md) for provenance and the verification date.

Use this skill for new compositions, existing Remotion projects, data-driven variants, and video
product integrations. A simple manual clip cut can be faster in a visual editor. Traditional
hand-drawn animation, rotoscoping, and complex VFX may need specialist tools whose rendered footage
can be imported. Do not promise studio quality, advertising performance, or zero production cost.
This package works independently of any other installed skill, including the vendor's skills.

## 1. Establish the video contract

Inspect project instructions, existing compositions, package scripts, dependencies, lockfile,
entrypoint, `public/`, and output conventions. Preserve the chosen package manager and architecture.
Resolve these inputs from the request and files before asking for missing facts:

| Input | Decision |
| --- | --- |
| Purpose | Ad, app demo, product launch, lesson, presentation, overlay, or interactive preview |
| Audience | Language, familiarity with the subject, desired emotion, truthful promise and one CTA |
| Destination | Platform/placement, dimensions, fps, duration, safe areas, codec and transparency |
| Content | Script, approved claims/prices/testimonials, scene order, captions and narration |
| Identity | Actual logo variants, exact colors, fonts, reference images and product media |
| Resources | Target directory, existing runtime, local hardware, available generation tools and budget |
| Delivery | Source project, rendered files, stills, editable props, optional subtitles or Player |

For an unspecified short social draft, propose 1080×1920 at 30fps, a six-second first iteration,
H.264 MP4, one clear visual idea per scene, and readable text with sound off. These are working
defaults, not universal platform requirements. Keep instructions in English while preserving the
requested language of the video. Ask when missing assets, audience language, factual claims,
publication requirements, or paid-service permissions would change the result materially.

Use the [video brief template](assets/video-brief.md) to record the design and asset handoffs.
Do not invent a real product price, client quote, logo, or performance statistic. Mark a missing
asset explicitly in a draft and complete independent scene/layout work while awaiting it.

## 2. Prepare a compatible project

Use Node.js and an npm-compatible package manager on a supported host. Prefer a currently supported
Node LTS accepted by the selected template. Check current Remotion/browser/native requirements for
the actual machine. The researched v4 baseline requires macOS 15+, Linux with glibc 2.35+ and the
documented native dependencies, or Windows x64. Alpine and NixOS are unsupported. Do not assume that
every container, ARM Windows machine, or older macOS host can render. Read the template's own
`engines.node` range, which can be stricter than the documentation's general minimum.

In the intended parent directory, for a new project:

```bash
npx create-video@latest --yes --blank my-video
cd my-video
npm run dev
```

Inspect scaffold output. Install dependencies with `npm install` if installation was skipped.
For an existing locked project use its documented installation command. Blank is a useful minimal
starting point. With `--yes`, `create-video` skips the vendor Agent Skills prompt and installs none.
Add `--skills` to that command only when the task authorizes installing them.
Tailwind is optional and must follow the actual template choice. Read the Studio URL printed by the
server rather than assuming a fixed port. A failed scaffold or install leaves no usable project, so
report the exact error and stop before writing compositions into a partial directory.

The official `remotion-dev/skills` package offers extra vendor guidance. If the task authorizes
installing it, pass `--skills` to `create-video` for a new project, use `npx remotion skills add`
inside an existing Remotion project, or `npx skills add remotion-dev/skills` where Remotion is not
installed. Inspect the destination and actual loaded files. Installing
this collection's `remotion` skill does not install the vendor package, Remotion, or a coding agent.
Do not globally install skills merely to use this workflow.

Add only needed Remotion packages through, for example, `npx remotion add @remotion/transitions`.
Keep `remotion` and installed `@remotion/*` packages on the same exact compatible version. Check
React, Zod and other peer requirements before adding a package. Preserve the lockfile. Do not upgrade
an existing project as a side effect of reading newer documentation.

Claude Code can run interactively with `claude` or receive a first brief through `claude -p "..."`.
Noninteractive mode still follows its configured permissions and may lack interactive approval.
Other agents can read this package directly and perform the same workflow. Opening a second agent
is optional, not a prerequisite or a permission bypass.

Check Remotion license eligibility for the actual organization and use. The researched pricing
page provides a free license for individuals and companies of up to three people, subject to terms.
Larger organizations must resolve the applicable creator/automation license. This package's MIT
license does not license the Remotion runtime, third-party assets, voices, or music.

## 3. Write the story before the animation

Draft the message in ordinary language, then convert it into a scene table. A frame is one image.
At 30fps, 90 frames occupy three seconds. Rendering exports those frames to media. A composition
defines dimensions, fps and duration. Scenes contain reusable components such as titles, photos,
labels and buttons. The prompt specifies their appearance, timing and motion.

For a sales piece, choose an appropriate arc: hook → problem/desire → reveal → benefit/proof → CTA.
For a lesson, choose context → explanation/demo → recap. Name the emotion of each beat. Use the
audience's vocabulary, concrete outcomes, and substantiated proof. Show important opening copy at
frame zero when a blank opening would weaken the requested piece. Do not assert that every service
uses frame zero as its thumbnail or that a retention threshold guarantees distribution.

For each scene specify exact copy, assets, start/end frames, entrance, hold, exit, transition,
narration interval and reading time. Use hex colors, font weights, layer order, and concrete motion
such as `translateY: 40 → 0` with a clamped fade. Aesthetic terms like cinematic need an implementation
decision: background image, scrim, camera drift, easing, restrained texture and audio direction.

Use zero-based half-open ranges in storyboards: `[0, 60)` means frames 0 through 59. Convert seconds
to integer frames consistently. CLI frame ranges may instead include both ends. Distinguish
composition time from the local frame returned inside a `Sequence`.

Read [prompts and copy direction](references/prompts-and-copy.md) for the reusable prompt structure,
six complete format recipes, product/app/fashion variants and script review criteria.

## 4. Implement deterministic scenes

Register the root through the template entrypoint and `registerRoot`. Register each export with
`Composition`: a stable `id`, component, positive integer `durationInFrames`, fps, width and height.
Keep registration, composition assembly, scenes and reusable visual elements in separate files as
their responsibilities warrant. Give each component its own file. Do not create unused scaffolding.

Use `useCurrentFrame()` and `useVideoConfig()` to derive every animated value. Use `interpolate`
for ranges, `Easing` for acceleration, and `spring` for physically styled arrivals. Clamp fades,
prices, and other bounded values. A spring can overshoot, so clamp its value before using it as
opacity while keeping desired overshoot in translation or scale.

This scene is a complete frame-driven title, intended for its own `src/launch-title.tsx` file:

```tsx
import {AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig} from 'remotion';

export const LaunchTitle = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const arrival = spring({frame, fps, config: {damping: 25, stiffness: 180}});
  const clamp = {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'} as const;
  const scale = interpolate(frame, [0, 14], [1.06, 1], clamp);

  return (
    <AbsoluteFill style={{backgroundColor: '#0B1120', justifyContent: 'center', padding: 100}}>
      <h1 style={{color: '#E2E8F0', fontSize: 96, transform: `scale(${scale})`}}>
        Make room for your next idea
      </h1>
      <p style={{color: '#22C7B5', fontSize: 48, opacity: Math.min(1, Math.max(0, arrival))}}>
        A simpler creative workflow
      </p>
    </AbsoluteFill>
  );
};
```

Register that component in the template's root file with `id="LaunchTitle"`, `fps={30}`,
`durationInFrames={180}`, `width={1080}`, and `height={1920}`. The opening headline is visible on
frame zero. Load the selected font explicitly before judging final text layout.

Keep each function call on one line, as above. Extract named values such as `clamp` when arguments
grow, and never split one string literal into adjacent literals. The blank template's `.prettierrc`
sets no `printWidth`, so Prettier's 80-column default wraps long calls. When the project formats with
Prettier, set a wide `printWidth` such as 320 in its configuration so formatting never forces call
wrapping, then run the project's formatter and confirm the calls stayed on one line.

Remotion components share the timing props `from`, `trimBefore`, `durationInFrames`, `playbackRate`
and `loop`. Set them directly on a component or wrap children in a `Sequence`, following the
project's existing convention. Use `Series` for successive scenes and `TransitionSeries` for
overlapping transitions. The total with transitions is **sum of scene durations minus sum of
overlap durations**. Read [motion and timing](references/motion-and-timing.md) before allocating
transition or narration frames. A visual overlay around a cut is a different timing operation.

Use Remotion's seeded `random()` for repeatable particles/positions. Derive temporal noise from a
stable seed and frame. Avoid `Math.random()`, wall-clock time, CSS keyframes/transitions and libraries
advancing their own animation clock. GSAP can work when time is owned by Remotion. The motion
reference explains both pure easing and the current `@remotion/gsap` integration.

## 5. Prepare assets, voice, captions and finish

Put approved media in `public/` and reference `public/img/product.png` with
`staticFile('img/product.png')`, without the `public/` prefix. Use `Img` for images and
`OffthreadVideo` for compatible recorded footage in projects using that API. Follow the installed
version's media contract. For current projects, consider the recommended `@remotion/media` Audio
and Video components rather than silently rewriting older media code.

Load actual fonts with `@remotion/fonts` for local files or `@remotion/google-fonts`. Select only
used styles, weights and character subsets, verify the video's glyphs, and wait for readiness.
Merely setting `fontFamily` does not install a font. Use render-blocking components/loaders or
`delayRender` with balanced continuation/cancellation for asynchronous resources.

Read [assets and media generation](references/assets-and-generation.md) for reference images,
image/voice/music generation, permissions, licensing, portable asset organization and brand finish.
Use available native tools or existing generators. This skill bundles no generation scripts.

Generate or record final speech before freezing narrated scene lengths. Measure each clip, allow
an opening delay and ending pause, and place it explicitly in the timeline. Keep narration legible
above music, listen to the full mix, and measure loudness/peaks. Render captions from reviewed
timestamps using the same audio version. Read [audio and captions](references/audio-and-captions.md)
for local multilingual Whisper, cloud/manual/SRT routes, overlap arithmetic and mix diagnosis.

Finish deliberately: align grids, establish a typographic hierarchy, use consistent SVG icons,
and add shadows, masks, motion blur, 3D or audio response only when they support the message.
Show product media that supports the spoken benefit. A slowly moving image plus a readable scrim
is one option, not a rule that all scenes require photographs. Leave a calm readable CTA hold.

The finished video speaks about its subject, never about its own production. Narration, captions,
on-screen copy, end cards and file metadata must not mention Remotion, code, prompts, agents, AI
generation or how the piece was made, unless the user asks for that content. When a destination's
policy requires disclosure of synthetic or altered media, use that platform's own disclosure setting
or label during publication and record the requirement in the brief rather than adding production
commentary to the video.

## 6. Inspect before the final render

Preview in Studio, then export and inspect stills of frame zero, each scene's settled state,
both sides and the middle of transitions, caption changes, and the final frame. Use actual frames
from the timing table. Example commands assume the inspected entrypoint is `src/index.ts`:

```bash
npx remotion still src/index.ts LaunchTitle out/opening.png --frame=0
npx remotion still src/index.ts LaunchTitle out/settled.png --frame=90
npx remotion render src/index.ts LaunchTitle out/launch.mp4 --codec=h264 --crf=18 --overwrite=false
```

Run the project's declared type, lint and applicable build checks. Inspect the exported video at
normal speed, with sound and muted. Confirm dimensions, fps, duration, codec, file size, text
spelling/overflow, real assets, font loading, transition continuity, voice overlaps, caption sync,
audio clipping, reading time, destination safe areas and the absence of production commentary.
A successful CLI exit alone is insufficient. Rendering overwrites an existing output by default, so
keep `--overwrite=false` or a new filename whenever an approved export already exists.

| Failure | Next action |
| --- | --- |
| Missing image/404 | Match filename/case and `staticFile` path to `public/`, inspect the URL, rerender the affected still |
| Flicker or different frames | Check readiness, clocks, seeded randomness, media and GPU behavior before changing concurrency |
| Font timeout/wrong wrapping | Restrict variants/subsets, check glyph coverage and network/local font loading, inspect again |
| Speech overlaps or is cut | Compare absolute audio intervals after transition overlaps, adjust timing and regenerate captions |
| Render exhausts memory | Reduce concurrency/resolution for diagnosis, isolate the heavy scene/effect, preserve final requirements |
| Unsupported host/codec | Identify the exact native/browser/codec constraint and use a supported environment/output |
| Missing credentials or service | Finish local/source work and name the exact generation, upload or render step not executed |

Single-process rendering can diagnose resource pressure. It does not repair nondeterministic code
or guarantee an unloaded asset appears. Do not hide failed media by reporting placeholder renders
as finished. Preserve previous approved exports and failed-job identifiers when recovering.

## 7. Render reusable variants or integrate a video product

For data-driven videos, define a small validated props contract, realistic `defaultProps`, and
optional `calculateMetadata` for data-dependent duration or dimensions. Render two meaningfully
different products before scaling, including a long title or missing-asset failure. Do not encode
customer data or credentials into a public bundle. Keep preview and final-render props identical.

Read [rendering and scale](references/rendering-and-scale.md) for codecs, alpha, GIFs, prop files,
batch recovery, Player, server-side `bundle` → `selectComposition` → `renderMedia`, and the complete
AWS Lambda preparation/deploy/render sequence. Player displays a live component. Rendering creates
an encoded file. AWS setup, media uploads, paid generation, bulk jobs and publishing require the
user's actual authorization, including any already agreed budget and destination.

## Deliver with evidence

Return source paths, composition IDs, reproducible commands, rendered files, representative stills,
resolved props and the final timing/asset decisions. Include captions if requested and note whether
they are burned in or delivered as a sidecar. State what was actually previewed, rendered, measured
and inspected, plus unresolved missing media, licensing eligibility, tooling or destination checks.
Keep drafted, previewed, rendered, quality-checked, uploaded and published states distinct.
