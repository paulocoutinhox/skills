# Motion, transitions and finishing

Use frame arithmetic before choosing effects. A composition can render frames out of order and in
separate browser processes. Each requested frame must reconstruct the same visual state.

## Time, layers and scene boundaries

`useCurrentFrame()` is relative to the enclosing Sequence. `Sequence from={60}` makes the child's
frame zero appear at composition frame 60. Remotion components share the timing props `from`,
`trimBefore`, `durationInFrames`, `playbackRate` and `loop`, applied in that order. A child sees
`trimBefore + (frame - from) * playbackRate`. Set them directly on a component or through a Sequence
wrapper, following the installed API and the project's convention. `Series` lays out sequential segments. `AbsoluteFill`
creates full-frame layers whose DOM order establishes ordinary stacking unless an explicit stacking
context changes it. Keep background, primary subject, labels, captions and foreground finish ordered.

For transitions, install `@remotion/transitions`. Choose `fade`, `slide`, `wipe` or `flip` from its
presentation subpaths. A hard cut can be appropriate for rhythm or clarity. More transitions do not
automatically improve a piece. `linearTiming({durationInFrames: 15})` gives an explicit overlap.
`springTiming` produces a duration based on its configuration unless explicitly controlled. Resolve
its `getDurationInFrames({fps})` before calculating scene start times.

For scene lengths `d1...dn` and overlaps `t1...t(n-1)`:

- First scene starts at zero.
- Next start = previous start + previous duration − their overlap.
- Final duration = sum of scene durations − sum of overlaps.
- Each overlap must fit both adjacent scenes. Do not place adjacent transitions.

A 15-second, 30fps product ad can use the following **450-frame** plan:

| Scene | Length | Absolute visibility | Role |
| --- | --- | --- | --- |
| Hook | 90 | `[0, 90)` | Immediate readable problem/desire |
| Product | 135 | `[75, 210)` | Actual product image and reveal |
| Benefits | 135 | `[195, 330)` | Three supported benefits |
| Offer | 135 | `[315, 450)` | Approved price and CTA hold |

Three 15-frame transitions subtract 45 from 495. If instead the scene lengths total 450 before
adding these transitions, the result is 405 frames, or 13.5 seconds. Fix the storyboard and
Composition together. Extending only the Composition can leave an empty tail.

`TransitionSeries.Overlay` occupies a cut boundary without shortening scene durations. Use that
contract for an overlay flash or light leak when appropriate. Do not subtract its duration as if it
were a transition. Check availability in the installed version.

For a radial reveal, `clockWipe` comes from `@remotion/transitions/clock-wipe` and takes the
composition width/height. The `none` presentation has no built-in visual effect and permits a custom
effect driven by transition progress. It still occupies an overlap interval. Omitting a transition
between adjacent sequences is the straightforward hard cut without overlap. Do not treat `none()`
as a way to cancel overlap arithmetic.

## Make the motion communicate

Build a small arc within a reveal: preparation → anticipation → arrival → readable rest. A ten-frame
anticipation can be useful for a logo sting, but an ad may require its opening message immediately.
Use timing and spacing to indicate weight, and staging to make the focal point unambiguous.

Animate a primary element, then a small secondary reaction when it adds clarity. Tertiary particles,
background breathing and texture are optional. Avoid moving every element continuously. Smooth
camera drifts usually benefit from easing. Constant-speed rotation or a progress indicator can
deliberately be linear.

These spring settings are aesthetic starting points, not physical or vendor-mandated presets:

| Intent | `damping` | `stiffness` | `mass` |
| --- | --- | --- | --- |
| Playful badge | 12 | 100 | 1 |
| Quick title arrival | 25 | 180 | 1 |
| Soft background drift | 50 | 50 | 1 |
| Heavy object reveal | 30 | 80 | 3 |

Higher damping generally suppresses oscillation. Judge the actual result at the selected fps.
Keep overshoot away from crop edges and allow the motion to settle. For each staggered item use
`localFrame = frame - index * delayFrames` and derive motion from that value. The article's eight-frame
list stagger is about 267ms at 30fps. A tighter 50–120ms rhythm rounds to roughly 2–4 frames. Choose
by reading load and scene duration rather than treating these as equivalent prescriptions.

Use `interpolate` with left/right clamps for fade, slide and count-up boundaries. For a fictional
price reveal of 129 units over 45 frames, interpolate `[0, 45]` to `[0, 129]`, clamp both ends, then
format/round for the correct locale and currency. The final value must equal the approved price.
Do not animate misleading discounts or fabricate a sale.

For a recurring pulse, define the phase explicitly from frame/time or a repeating piecewise curve.
A single spring is a settling entrance and does not create an endless pulse by itself. Keep the CTA
readable and make a loop's first and final states join cleanly.

Choose a pattern by its communication role:

| Pattern | Frame-driven implementation |
| --- | --- |
| Fade/slide/scale entrance or exit | Clamped progress mapped to opacity, position or scale, with a readable hold |
| Float or rotate | Continuous phase derived from time, with deliberate loop boundaries |
| Shake, bounce or wiggle emphasis | Small bounded periodic or seeded offsets around a stable position |
| Typewriter or word reveal | Visible text count from elapsed frames, respecting graphemes and reading time |
| Painted word highlight | Mask or background progress tied to the selected word interval |
| Parallax | Shared camera progress mapped to different layer distances/speeds, with crop margin |

For an animated GIF used as an input, `Gif` from `@remotion/gif` synchronizes playback to Remotion's
frame. This is distinct from exporting the whole composition as GIF. For Lottie inputs, add
`@remotion/lottie` and its `lottie-web` peer, resolve the animation data/readiness, and inspect its
dimensions, timing and direct seeks. The researched integration supports the SVG renderer and has
limited expression support. A Lottie expression can still produce flicker, so test the actual file
rather than assuming all After Effects exports are deterministic.

## Effects with purpose

| Request | Implementation decision and inspection |
| --- | --- |
| Depth or glow | `boxShadow`, `drop-shadow`, restrained colored `textShadow`. Check contrast and compression |
| Blur-in | Frame-derived filter and opacity, followed by sharp held text. Check render cost |
| Animated gradient | Compute stops/angle/position from frame. Avoid an independent CSS animation |
| Tilted product card | CSS perspective and `rotateX`/`rotateY`. A rotating photograph remains a flat image |
| Shape reveal | Animated `clip-path` or SVG mask. Inspect clipping and glyph edges |
| Camera drift/Ken Burns | Small scale/translation inside a clipped container, with sufficient crop margin |
| Film texture | Subtle grain and vignette. Use deterministic per-frame seeds and unique SVG filter IDs |
| Fast-motion trails | `Trail` or `CameraMotionBlur` from `@remotion/motion-blur`, tested for render cost |
| Shapes or drawn paths | `@remotion/shapes` and `@remotion/paths`, with frame-driven progress |
| Organic movement | Seeded `@remotion/noise` values rather than a new random position each frame |
| CSS transform helpers | `@remotion/animation-utils` when it improves an actual transform composition |

Grain around five percent opacity is one visual starting point, not a required filter. Test a still
and a compressed motion sample. Heavy grain can increase bitrate and distract from the message.
The original `@remotion/light-leaks` package is deprecated in the researched baseline. New projects
can use `lightLeak` from `@remotion/effects/light-leak` on supported canvas components, driven by
frame-derived progress. Preserve existing versions deliberately rather than mixing the two APIs.

## GSAP without an independent clock

For easing alone, GSAP's `parseEase` is a pure mapping that can be evaluated at a clamped frame
progress. `power3.out`, `expo.out` and `back.out(1.6)` provide different acceleration/overshoot shapes.
Do not feed overshooting ease values directly into opacity without bounding them.

For choreography on Remotion versions supporting it, add `@remotion/gsap` and its `gsap` peer.
`useGsapTimeline` owns a paused timeline, seeks it from the Remotion frame and returns a scoped ref.
Attach that ref and target elements through its scoped selector. Rebuild with declared dependencies
when prop changes affect the timeline.

The builder must be synchronous and target DOM/SVG elements. Do not play, seek or resume it yourself,
use playback callbacks, animate plain-object state, or use unseeded GSAP random values. Remotion owns
the clock. For an older project with an explicit paused timeline adapter, initialize and clean up
the timeline, seek it to `frame / fps` on every visited frame, and compare direct-seek stills against
playback. Prefer pure Remotion primitives unless the choreography justifies that adapter.

## Real 3D and audio response

Use `ThreeCanvas` from `@remotion/three` when real geometry, camera and lighting are required. Pass
composition dimensions and verify compatible Three.js/React Three Fiber peers. Derive mesh rotations,
camera positions and lighting changes from `useCurrentFrame()`. Avoid the independent `useFrame`
animation loop. Load models/textures with render readiness and test the actual GPU/headless/cloud
environment. CSS perspective alone does not synthesize a product's unseen surfaces.

For music-driven bars, use `useAudioData` and `visualizeAudio` from `@remotion/media-utils`. Choose a
power-of-two sample count such as 32. Ensure the decoded data is ready and bound the displayed
amplitude for the composition. The analyzed frame refers to time in the audio file, so account for
Sequence offsets, trims and playback-rate changes. Keep the actual audio playback alongside the
visualization. FFT energy indicates frequency content, not a guarantee of musically meaningful beats.

## Visual acceptance

Inspect anticipation, peak motion, settling and reading holds. Compare direct seeks with playback
and repeated renders. Check the first frame, final frame, safe areas, hierarchy, icon alignment,
mask edges and contrast after compression. An expressive piece can use only typography and strong
layout. Restraint and a clear focal point matter more than an effects inventory.
