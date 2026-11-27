---
name: remotion
description: Create, refine, and render videos in code with Remotion and React from scripts, prompts, brand assets, or data. Use for animated ads, product demos, course graphics, captions, motion design, reusable video templates, Player previews, local/server rendering, and authorized AWS Lambda rendering.
license: MIT
---

# Remotion

Turn a brief into a video you can rebuild the same way every time: story, storyboard, React scenes
driven by the frame number, prepared media, checked previews, and checked exports. This English
workflow adapts Paulo Coutinho's Remotion guide and checks technical details against the official
documentation. Read [sources and interpretation limits](references/sources.md) for where each fact
comes from and when it was checked.

Use this skill for new compositions, existing Remotion projects, data-driven variants, and video
product integrations. A simple manual clip cut can be faster in a visual editor. Traditional
hand-drawn animation, rotoscoping, and complex VFX may need special tools, and you can import their
rendered footage. Do not promise studio quality, ad performance, or zero production cost.
This package works on its own, without any other installed skill, including the vendor's skills.

## 1. Agree on what the video must be

Read the project instructions, existing compositions, package scripts, dependencies, lockfile,
entrypoint, `public/`, and output conventions. Keep the chosen package manager and structure.
Answer these inputs from the request and the files before you ask for missing facts:

| Input | Decision |
| --- | --- |
| Purpose | Ad, app demo, product launch, lesson, presentation, overlay, or interactive preview |
| Audience | Language, how well they know the subject, the feeling you want, an honest promise and one CTA |
| Destination | Platform/placement, dimensions, fps, duration, safe areas, codec and transparency |
| Content | Script, approved claims/prices/testimonials, scene order, captions and narration |
| Identity | Real logo variants, exact colors, fonts, reference images and product media |
| Resources | Target directory, existing runtime, local hardware, available generation tools and budget |
| Delivery | Source project, rendered files, stills, editable props, optional subtitles or Player |

When a short social draft has no stated format, propose 1080×1920 at 30fps, a six-second first
version, H.264 MP4, one clear visual idea per scene, and text that reads with the sound off. These
are working defaults, not rules for every platform. Keep instructions in English, but keep the video
in the language the user asked for. Ask when missing assets, audience language, factual claims,
publishing rules, or permission for paid services would change the result in a big way.

Use the [video brief template](assets/video-brief.md) to record the design and asset handoffs.
Do not invent a real product price, client quote, logo, or performance number. Clearly mark a
missing asset in a draft, and finish the scene and layout work that does not depend on it while you
wait.

## 2. Prepare a compatible project

Use Node.js and an npm-compatible package manager on a supported machine. Prefer a currently
supported Node LTS that the chosen template accepts. Check the current Remotion, browser and native
requirements for the real machine. The checked v4 baseline needs macOS 15+, Linux with glibc 2.35+
and the documented native dependencies, or Windows x64. Alpine and NixOS are not supported. Do not
assume that every container, ARM Windows machine, or older macOS machine can render. Read the
template's own `engines.node` range, which can be stricter than the general minimum in the docs.

For a new project, in the parent directory you want:

```bash
npx create-video@latest --yes --blank my-video
cd my-video
npm run dev
```

Read the scaffold output. Install dependencies with `npm install` if the install step was skipped.
For an existing project with a lockfile, use its documented install command. Blank is a useful
minimal starting point. With `--yes`, `create-video` skips the vendor Agent Skills question and
installs none. Add `--skills` to that command only when the task allows installing them.
Tailwind is optional and must match the real template choice. Read the Studio URL that the server
prints instead of assuming a fixed port. A failed scaffold or install leaves no usable project, so
report the exact error and stop before you write compositions into a half-made directory.

The official `remotion-dev/skills` package offers extra vendor guidance. If the task allows
installing it, pass `--skills` to `create-video` for a new project, use `npx remotion skills add`
inside an existing Remotion project, or `npx skills add remotion-dev/skills` where Remotion is not
installed. Check the destination and the files that were really loaded. Installing
this collection's `remotion` skill does not install the vendor package, Remotion, or a coding agent.
Do not install skills globally just to use this workflow.

Add only the Remotion packages you need, for example with `npx remotion add @remotion/transitions`.
Keep `remotion` and the installed `@remotion/*` packages on the same exact compatible version. Check
React, Zod and other peer requirements before you add a package. Keep the lockfile. Do not upgrade
an existing project just because you read newer documentation.

Claude Code can run interactively with `claude` or receive a first brief through `claude -p "..."`.
Non-interactive mode still follows its configured permissions and may not be able to ask for
approval. Other agents can read this package directly and follow the same workflow. Opening a second
agent is optional. It is not required, and it does not bypass permissions.

Check whether the real organization and use qualify for a Remotion license. The checked pricing
page gives a free license to individuals and to companies of up to three people, under its terms.
Larger organizations must get the right creator/automation license. This package's MIT license does
not license the Remotion runtime, third-party assets, voices, or music.

## 3. Write the story before the animation

Write the message in everyday language first, then turn it into a scene table. A frame is one image.
At 30fps, 90 frames last three seconds. Rendering exports those frames to media. A composition
sets dimensions, fps and duration. Scenes contain reusable components such as titles, photos,
labels and buttons. The prompt says how they look, when they appear and how they move.

For a sales piece, pick a fitting arc: hook → problem/desire → reveal → benefit/proof → CTA.
For a lesson, pick context → explanation/demo → recap. Name the feeling of each beat. Use the
audience's words, concrete results, and proof you can back up. Show important opening text on
frame zero when a blank opening would weaken the piece. Do not claim that every service uses frame
zero as its thumbnail or that a retention number guarantees reach.

For each scene, give the exact text, assets, start/end frames, entrance, hold, exit, transition,
narration interval and reading time. Use hex colors, font weights, layer order, and concrete motion
such as `translateY: 40 → 0` with a clamped fade. Style words like cinematic need a concrete
choice: background image, scrim, camera drift, easing, light texture and audio direction.

In storyboards, use ranges that start at zero and leave out the end frame: `[0, 60)` means frames 0
through 59. Convert seconds to whole frames the same way every time. CLI frame ranges may include
both ends instead. Keep composition time separate from the local frame you get inside a `Sequence`.

Read [prompts and copy direction](references/prompts-and-copy.md) for the reusable prompt structure,
six complete format recipes, product/app/fashion variants and script review criteria.

## 4. Build scenes that render the same every time

Register the root through the template entrypoint and `registerRoot`. Register each export with
`Composition`: a stable `id`, component, positive whole-number `durationInFrames`, fps, width and
height. Keep registration, composition assembly, scenes and reusable visual parts in separate files
when their jobs call for it. Give each component its own file. Do not create unused scaffolding.

Use `useCurrentFrame()` and `useVideoConfig()` to work out every animated value. Use `interpolate`
for ranges, `Easing` for speed-up and slow-down, and `spring` for arrivals that feel physical. Clamp
fades, prices, and other values that must stay inside a range. A spring can overshoot, so clamp its
value before you use it as opacity, while keeping the overshoot you want in translation or scale.

This scene is a complete title driven by the frame number, meant for its own `src/launch-title.tsx`
file:

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
`durationInFrames={180}`, `width={1080}`, and `height={1920}`. The opening headline shows on
frame zero. Load the chosen font explicitly before you judge the final text layout.

Keep each function call on one line, as above. Pull out named values such as `clamp` when arguments
grow, and never split one string literal into side-by-side literals. The blank template's
`.prettierrc` sets no `printWidth`, so Prettier's 80-column default wraps long calls. When the
project formats with Prettier, set a wide `printWidth` such as 320 in its configuration so
formatting never forces calls to wrap. Then run the project's formatter and confirm the calls stayed
on one line.

Remotion components share the timing props `from`, `trimBefore`, `durationInFrames`, `playbackRate`
and `loop`. Set them directly on a component or wrap children in a `Sequence`, following the
project's existing habit. Use `Series` for scenes that follow each other and `TransitionSeries` for
transitions that overlap. The total with transitions is **sum of scene durations minus sum of
overlap durations**. Read [motion and timing](references/motion-and-timing.md) before you assign
transition or narration frames. A visual overlay around a cut is a different timing operation.

Use Remotion's seeded `random()` for particles and positions that must repeat. Build noise that
changes over time from a fixed seed and the frame. Avoid `Math.random()`, wall-clock time, CSS
keyframes/transitions and libraries that run their own animation clock. GSAP can work when Remotion
controls time. The motion reference explains both pure easing and the current `@remotion/gsap`
integration.

## 5. Prepare assets, voice, captions and finish

Put approved media in `public/` and reference `public/img/product.png` with
`staticFile('img/product.png')`, without the `public/` prefix. Use `Img` for images and the
`@remotion/media` `Video` and `Audio` components for recorded footage and sound.

Load real fonts with `@remotion/fonts` for local files or with `@remotion/google-fonts`. Pick only
the styles, weights and character subsets you use, check the video's glyphs, and wait until the font
is ready. Setting `fontFamily` alone does not install a font. For resources that load in the
background, use components/loaders that block rendering, or `delayRender` with a matching
continue/cancel call.

Read [assets and media generation](references/assets-and-generation.md) for reference images,
image/voice/music generation, permissions, licensing, portable asset layout and brand finish.
Use the native tools or existing generators you have. This skill bundles no generation scripts.

Generate or record the final speech before you lock the length of narrated scenes. Measure each clip,
leave a short delay at the start and a pause at the end, and place it explicitly in the timeline.
Keep narration clear above the music, listen to the full mix, and measure loudness/peaks. Render
captions from reviewed timestamps that use the same audio version. Read
[audio and captions](references/audio-and-captions.md) for local multilingual Whisper,
cloud/manual/SRT routes, overlap math and mix problems.

Finish with care: line up grids, set a clear text hierarchy, use matching SVG icons, and add
shadows, masks, motion blur, 3D or audio response only when they help the message.
Show product media that backs up the spoken benefit. A slowly moving image with a readable scrim
is one option, not a rule that every scene needs a photo. Leave a calm, readable CTA hold.

The finished video talks about its subject, never about how it was made. Narration, captions,
on-screen text, end cards and file metadata must not mention Remotion, code, prompts, agents, AI
generation or how the piece was made, unless the user asks for that content. When a destination's
policy requires a disclosure for synthetic or altered media, use that platform's own disclosure
setting or label when publishing and record the requirement in the brief. Do not add production
commentary to the video.

## 6. Check before the final render

Preview in Studio. Then export and check stills of frame zero, each scene once it has settled,
both sides and the middle of transitions, caption changes, and the final frame. Use real frames
from the timing table. The example commands assume the checked entrypoint is `src/index.ts`:

```bash
npx remotion still src/index.ts LaunchTitle out/opening.png --frame=0
npx remotion still src/index.ts LaunchTitle out/settled.png --frame=90
npx remotion render src/index.ts LaunchTitle out/launch.mp4 --codec=h264 --crf=18 --overwrite=false
```

Run the project's declared type, lint and relevant build checks. Watch the exported video at
normal speed, with sound and muted. Confirm dimensions, fps, duration, codec, file size, text
spelling/overflow, real assets, font loading, smooth transitions, voice overlaps, caption sync,
audio clipping, reading time, destination safe areas and that there is no production commentary.
A successful CLI exit is not enough on its own. Rendering overwrites an existing output by default,
so keep `--overwrite=false` or use a new filename whenever an approved export already exists.

| Failure | Next action |
| --- | --- |
| Missing image/404 | Match filename/case and `staticFile` path to `public/`, check the URL, rerender the affected still |
| Flicker or different frames | Check readiness, clocks, seeded randomness, media and GPU behavior before changing concurrency |
| Font timeout/wrong wrapping | Limit variants/subsets, check glyph coverage and network/local font loading, check again |
| Speech overlaps or is cut | Compare absolute audio intervals after transition overlaps, adjust timing and regenerate captions |
| Render runs out of memory | Lower concurrency/resolution to find the cause, isolate the heavy scene/effect, keep the final requirements |
| Unsupported machine/codec | Find the exact native/browser/codec limit and use a supported environment/output |
| Missing credentials or service | Finish local/source work and name the exact generation, upload or render step that did not run |

Rendering in a single process can help find resource pressure. It does not fix code that renders
differently each time, and it does not guarantee that an asset that did not load will appear. Do not
hide failed media by reporting placeholder renders as finished. Keep earlier approved exports and
failed-job IDs when you recover.

## 7. Render reusable variants or integrate a video product

For data-driven videos, define a small validated props contract, realistic `defaultProps`, and
optional `calculateMetadata` for duration or dimensions that depend on data. Render two clearly
different products before you scale up, including a long title or a missing-asset failure. Do not
put customer data or credentials into a public bundle. Keep preview and final-render props the same.

Read [rendering and scale](references/rendering-and-scale.md) for codecs, alpha, GIFs, prop files,
batch recovery, Player, server-side `bundle` → `selectComposition` → `renderMedia`, and the complete
AWS Lambda prepare/deploy/render sequence. Player shows a live component. Rendering creates
an encoded file. AWS setup, media uploads, paid generation, bulk jobs and publishing need the
user's real permission, including any budget and destination already agreed.

## Deliver with evidence

Return source paths, composition IDs, commands that reproduce the result, rendered files, sample
stills, the final props and the final timing/asset decisions. Include captions if requested and say
whether they are burned in or delivered as a separate file. State what was really previewed,
rendered, measured and checked, plus any open issues with missing media, license eligibility,
tooling or destination checks. Keep drafted, previewed, rendered, quality-checked, uploaded and
published states separate.
