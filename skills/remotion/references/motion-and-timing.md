# Motion, transitions and finishing

Do the frame math before you choose effects. A composition can render frames out of order and in
separate browser processes. Each requested frame must rebuild exactly the same picture.

## Time, layers and scene boundaries

`useCurrentFrame()` counts from the start of the Sequence it sits in. `Sequence from={60}` makes the
child's frame zero appear at composition frame 60. Remotion components share the timing props
`from`, `trimBefore`, `durationInFrames`, `playbackRate` and `loop`, applied in that order. A child
sees `trimBefore + (frame - from) * playbackRate`. Set them directly on a component or through a
Sequence wrapper, following the installed API and the project's habit. `Series` lays out segments
one after another. `AbsoluteFill` creates full-frame layers. Their DOM order sets the normal
stacking, unless an explicit stacking context changes it. Keep background, main subject, labels,
captions and foreground finish in order.

For transitions, install `@remotion/transitions`. Pick `fade`, `slide`, `wipe` or `flip` from its
presentation subpaths. A hard cut can be right for rhythm or clarity. More transitions do not make
a piece better on their own. `linearTiming({durationInFrames: 15})` gives an explicit overlap.
`springTiming` works out a duration from its settings unless you control it explicitly. Get its
`getDurationInFrames({fps})` before you calculate scene start times.

For scene lengths `d1...dn` and overlaps `t1...t(n-1)`:

- First scene starts at zero.
- Next start = previous start + previous duration − their overlap.
- Final duration = sum of scene durations − sum of overlaps.
- Each overlap must fit inside both neighboring scenes. Do not put two transitions next to each
  other.

A 15-second, 30fps product ad can use the following **450-frame** plan:

| Scene | Length | Absolute visibility | Role |
| --- | --- | --- | --- |
| Hook | 90 | `[0, 90)` | Readable problem/desire right away |
| Product | 135 | `[75, 210)` | Real product image and reveal |
| Benefits | 135 | `[195, 330)` | Three benefits you can back up |
| Offer | 135 | `[315, 450)` | Approved price and CTA hold |

Three 15-frame transitions subtract 45 from 495. If the scene lengths instead add up to 450 before
you add these transitions, the result is 405 frames, or 13.5 seconds. Fix the storyboard and the
Composition together. Making only the Composition longer can leave an empty tail.

`TransitionSeries.Overlay` sits on a cut without shortening the scenes. Use it for an overlay flash
or light leak when it fits. Do not subtract its duration as if it were a transition. Check that it
exists in the installed version.

For a radial reveal, `clockWipe` comes from `@remotion/transitions/clock-wipe` and takes the
composition width/height. The `none` presentation has no built-in visual effect and lets you add
your own effect driven by transition progress. It still takes up an overlap interval. Leaving out a
transition between neighboring sequences is the simple hard cut without overlap. Do not use
`none()` as a way to skip the overlap math.

## Make the motion say something

Build a small arc inside a reveal: preparation → anticipation → arrival → readable rest. A ten-frame
anticipation can help a logo sting, but an ad may need its opening message right away.
Use timing and spacing to show weight, and staging to make the focal point clear.

Animate a main element, then add a small secondary reaction when it makes things clearer. Extra
particles, background breathing and texture are optional. Avoid moving every element all the time.
Smooth camera drifts usually look better with easing. Constant-speed rotation or a progress bar can
be linear on purpose.

These spring settings are style starting points, not physical or vendor-required presets:

| Intent | `damping` | `stiffness` | `mass` |
| --- | --- | --- | --- |
| Playful badge | 12 | 100 | 1 |
| Quick title arrival | 25 | 180 | 1 |
| Soft background drift | 50 | 50 | 1 |
| Heavy object reveal | 30 | 80 | 3 |

Higher damping usually reduces bouncing. Judge the real result at the chosen fps. Keep overshoot
away from crop edges and let the motion settle. For each staggered item use
`localFrame = frame - index * delayFrames` and build the motion from that value. The eight-frame
list stagger in the source guide from [sources](sources.md) is about 267ms at 30fps. A tighter
50–120ms rhythm rounds to roughly 2–4 frames. Choose based on how much there is to read and how long
the scene is. Do not treat these as interchangeable rules.

Use `interpolate` with left/right clamps for the start and end of fades, slides and count-ups. For a
fictional price reveal of 129 units over 45 frames, interpolate `[0, 45]` to `[0, 129]`, clamp both
ends, then format/round for the right locale and currency. The final value must equal the approved
price. Do not animate misleading discounts or make up a sale.

For a repeating pulse, set the phase explicitly from frame/time or from a repeating piecewise curve.
A single spring is an entrance that settles. It does not make an endless pulse by itself. Keep the
CTA readable and make a loop's first and last states join cleanly.

Pick a pattern by what it needs to say:

| Pattern | How to build it from the frame |
| --- | --- |
| Fade/slide/scale entrance or exit | Clamped progress mapped to opacity, position or scale, with a readable hold |
| Float or rotate | Continuous phase from time, with planned loop boundaries |
| Shake, bounce or wiggle emphasis | Small, limited repeating or seeded offsets around a steady position |
| Typewriter or word reveal | Visible text count from elapsed frames, respecting graphemes and reading time |
| Painted word highlight | Mask or background progress tied to the chosen word interval |
| Parallax | Shared camera progress mapped to different layer distances/speeds, with crop margin |

For an animated GIF used as an input, `Gif` from `@remotion/gif` keeps playback in sync with
Remotion's frame. This is different from exporting the whole composition as a GIF. For Lottie
inputs, add `@remotion/lottie` and its `lottie-web` peer, load the animation data and wait until it
is ready, and check its dimensions, timing and direct seeks. The checked integration supports the
SVG renderer and has limited expression support. A Lottie expression can still cause flicker, so
test the real file. Do not assume all After Effects exports render the same every time.

## Effects with purpose

| Request | What to build and what to check |
| --- | --- |
| Depth or glow | `boxShadow`, `drop-shadow`, light colored `textShadow`. Check contrast and compression |
| Blur-in | Filter and opacity from the frame, followed by sharp held text. Check render cost |
| Animated gradient | Compute stops/angle/position from frame. Avoid a separate CSS animation |
| Tilted product card | CSS perspective and `rotateX`/`rotateY`. A rotating photo is still a flat image |
| Shape reveal | Animated `clip-path` or SVG mask. Check clipping and glyph edges |
| Camera drift/Ken Burns | Small scale/translation inside a clipped container, with enough crop margin |
| Film texture | Subtle grain and vignette. Use fixed per-frame seeds and unique SVG filter IDs |
| Fast-motion trails | `Trail` or `CameraMotionBlur` from `@remotion/motion-blur`, tested for render cost |
| Shapes or drawn paths | `@remotion/shapes` and `@remotion/paths`, with progress from the frame |
| Organic movement | Seeded `@remotion/noise` values instead of a new random position each frame |
| CSS transform helpers | `@remotion/animation-utils` when it improves a real transform setup |

Grain at about five percent opacity is one visual starting point, not a required filter. Test a still
and a compressed motion sample. Heavy grain can raise the bitrate and pull attention from the
message. Use `lightLeak` from `@remotion/effects/light-leak` on supported canvas components, driven
by progress from the frame.

## GSAP without its own clock

For easing alone, GSAP's `parseEase` is a pure mapping that you can evaluate at a clamped frame
progress. `power3.out`, `expo.out` and `back.out(1.6)` give different speed-up/overshoot shapes.
Do not feed easing values that overshoot straight into opacity without limiting them.

For choreography, add `@remotion/gsap` and its `gsap` peer.
`useGsapTimeline` owns a paused timeline, seeks it from the Remotion frame and returns a scoped ref.
Attach that ref and target elements through its scoped selector. Rebuild with declared dependencies
when prop changes affect the timeline.

The builder must be synchronous and target DOM/SVG elements. Do not play, seek or resume it yourself,
use playback callbacks, animate plain-object state, or use unseeded GSAP random values. Remotion owns
the clock. Prefer plain Remotion building blocks unless the choreography is worth a GSAP timeline.

## Real 3D and audio response

Use `ThreeCanvas` from `@remotion/three` when you need real geometry, camera and lighting. Pass
composition dimensions and check that the Three.js/React Three Fiber peers are compatible. Work out
mesh rotations, camera positions and lighting changes from `useCurrentFrame()`. Avoid the separate
`useFrame` animation loop. Load models/textures with render readiness and test the real
GPU/headless/cloud environment. CSS perspective alone does not create a product's unseen surfaces.

For music-driven bars, use `useAudioData` and `visualizeAudio` from `@remotion/media-utils`. Pick a
power-of-two sample count such as 32. Make sure the decoded data is ready and limit the shown
amplitude for the composition. The analyzed frame points to time in the audio file, so account for
Sequence offsets, trims and playback-rate changes. Keep the real audio playing alongside the
visualization. FFT energy shows frequency content. It does not guarantee beats that make musical
sense.

## Visual acceptance

Check anticipation, peak motion, settling and reading holds. Compare direct seeks with playback
and repeated renders. Check the first frame, last frame, safe areas, hierarchy, icon alignment,
mask edges and contrast after compression. An expressive piece can use only typography and strong
layout. Restraint and a clear focal point matter more than a long list of effects.
