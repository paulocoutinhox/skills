# Briefs, copy direction and reusable video recipes

Use a script the audience can understand, then make it implementable with frame ranges, assets and
motion. A precise prompt reduces avoidable guessing. It does not guarantee a particular agent's
output or remove the need to inspect the rendered result.

## Prompt structure

Supply purpose/audience/language, output dimensions/fps/duration, approved assets, brand palette,
scene table, motion, typography, narration/captions, safe areas and deliverables. State whether frame
ranges include transition overlaps. Identify missing required assets honestly. Keep the actual
project directory explicit so a coding agent does not create a second project accidentally.

An initial brief can be submitted in interactive Claude Code, by its `-p` mode, or directly to another
compatible agent. Continue scene-by-scene iterations against Studio and exported stills. Ask for a
specific change such as “reduce the product arrival from 24 to 16 frames and keep the speech hold,”
then recheck dependent timing. A vague “make it more professional” needs concrete design decisions.

The recipes below assume supplied/authorized assets. Their colors, typography, durations and safe
areas are working examples. Replace copy and claims with owner-approved material. Load only the
references needed for the requested operation.

## First iteration: six-second launch

```text
In [PROJECT_DIRECTORY], create LaunchDemo at 1080x1920, 30fps, 180 frames.
Language: English. Background #0B1120, primary text #E2E8F0, accent #22C7B5.
Use public/brand/logo-light.svg and the approved font files in public/fonts/.
Use hard cuts for this first iteration, with no transition overlap.

Frames [0,60): Show "Make room for your next idea" immediately at frame zero.
Let the logo settle from scale 0.8 to 1 with damping 25 and stiffness 180.
Frames [60,120): Show the supplied three benefits with a four-frame stagger,
translateY 40 to 0 and a clamped fade. Keep each item readable once settled.
Frames [120,180): Hold the approved CTA with a restrained scale pulse.

Reserve a draft 120px top and 220px bottom plus right-side clearance, then
review the actual destination overlay. Produce frame-zero, settled-benefit
and CTA stills, inspect them, and render H.264 MP4 without overwriting an
approved file. Report actual playback checks and missing inputs.
```

## Complete product ad: 15 seconds with overlaps

```text
Create ProductAd in [PROJECT_DIRECTORY]: 1080x1920, 30fps, exactly 450 frames.
Use public/img/cloud-runner.png, approved logo/fonts and the supplied offer.
The shoe name and $129 price are fictional examples until approved.
Use #0B1120, #E2E8F0 and #22C7B5. Keep text clear of platform overlays.

Scene 1: 90 frames, composition [0,90). Hook visible at frame zero.
Scene 2: 135 frames, [75,210). Reveal the real shoe photo with a spring and
subtle flat-image tilt. Do not invent a 3D view of unseen surfaces.
Scene 3: 135 frames, [195,330). Three approved benefits, staggered eight frames.
Scene 4: 135 frames, [315,450). Count up to the approved price over 45 local
frames, clamp the result, then hold the price and one CTA.

Use TransitionSeries with 15-frame fade, slide and fade overlaps.
495 scene frames minus 45 overlap frames equals 450 frames.
Generate/use narration only within the authorized service budget. Measure
clips before fixing the speech intervals. If speech does not fit, revise
the script or explicitly resolve a longer duration. Prevent voice overlaps.
Review captions from those exact audio clips. Load the actual font.

Inspect frame 0, scene holds, both sides/midpoints of each overlap and frame
449. Listen to the full mix, inspect loudness/peaks, and review muted playback.
Render a checked MP4 plus source, final timing table and requested stills.
```

## Six format recipes

### Brand reveal

Create a 150-frame, 30fps vertical logo sting with supplied artwork. Frames `[0,20)` establish the
background/anticipation, `[20,60)` reveal the logo with a playful spring, and `[60,150)` settle the
tagline and hold. Add restrained glow or motion blur only if the identity supports it. This slower
opening serves a brand sting. For an advertising placement requiring immediate copy, show the hook
at frame zero rather than reusing the same blank introduction.

### Product demo

Use the 450-frame plan above: problem/desire, real product, benefits, offer/CTA. A flat-image rotation
can supply movement. A true 360-degree showcase requires the necessary real footage or 3D model.
For physical goods, connect a demonstration to the benefit, show legible labels, and avoid fabricated
before/after proof. Lifestyle footage must have appropriate rights.

### Quote card

Create a 1080×1080, 240-frame, 30fps card. Use `[0,30)` for the quote mark and clear attribution
context, `[30,180)` for a short approved quotation in six-frame word staggers, and `[180,240)` for
an author/source hold. Choose a quote that fits the reading time. For longer copy, reveal the phrase
together or extend the duration. Verify the speaker and quotation. Do not attribute generated words
to a real person.

### Countdown

Create a 180-frame, 30fps sequence. Show 5, 4, 3, 2 and 1 for 30 frames each, then a 30-frame final
reveal. This accounts for all six seconds. Each number can arrive with a spring and a small
deterministic shake. Use a consistent baseline/scale and keep the reveal legible. Five one-second
numbers alone total five seconds, so do not leave an accidental blank sixth second.

### Testimonial or social proof

Create a 360-frame, 30fps piece with an authorized portrait, exact approved quote and clear
attribution. Use `[0,60)` to establish the person, `[60,270)` for the readable quote, and `[270,360)`
for a restrained brand/CTA hold. Add rating stars only when the rating is real and its context is
approved. A synthesized actor or AI voice cannot be presented as an authentic customer's recording.

### Lesson opener

Create a 1920×1080, 300-frame, 30fps introduction. Use `[0,60)` for context/module title,
`[60,240)` for lesson name/number and a readable lower-third, then `[240,300)` for the handoff.
If a wipe overlaps an included content scene, subtract that overlap from the total or extend the
scene lengths deliberately. Reuse a title/lower-third contract across lessons, keeping real code
and screen highlights large enough for the viewing environment.

## Adapt the structure to the destination

For an ordinary application demo, use genuine screen recordings with labels, focus highlights,
captions and deliberate zooms that preserve context. An App Store preview has a different contract:
the researched Apple requirements specify 15–30 seconds, device-specific accepted formats and up
to three previews per localization. Show the actual app experience using device-captured footage
and keep the message understandable without sound. Do not assume an arbitrary 1080×1920 social ad,
mockup-heavy promotion or external sales end card meets Apple's preview rules. Verify the selected
platform/device specifications and hand off store submission separately.

For fashion, use approved garment imagery or try-on footage, rhythmic cuts and a truthful drop/date.
Pick beat positions from the actual track. Build a clean master when platform music will be added
later. Do not promise distribution benefits from a particular trending sound.

For courses, prioritize explanation, lesson continuity, code/screen readability, recap cards and
accurate captions. For presentations, use a 16:9 working format such as 1920×1080, chart drawings,
count-ups and clear transitions. A video plays on a timed schedule and cannot assume a live speaker
will control the audience's reading time.

Common starting formats are 9:16 social video, 16:9 presentations/landscape video and 1:1 feed cards.
Choose actual placement requirements over these examples. Recompose each aspect ratio rather than
simply cropping off important copy. Keep the same truthful promise when producing A/B variants.

## Copy and emotional direction

Use real customer language from supplied reviews, interviews or support conversations when that
material is available and authorized. Extract the actual frustration, desired outcome and objections,
then paraphrase accurately. Remove private details and never turn a paraphrase into a fake quotation.
Combine useful information, an achievable aspiration and empathy for the viewer's situation. Keep
one idea per spoken line and define necessary technical terms through the problem they solve.

Choose one primary structure rather than stacking every formula into a short piece:

| Structure | Use |
| --- | --- |
| PAS: problem → agitation → solution | Audience recognizes a concrete problem. Keep the stakes truthful |
| AIDA: attention → interest → desire → action | Introduce an unfamiliar offer with enough explanation |
| BAB: before → after → bridge | Show a supported transformation and explain the path |
| Viewer-as-hero framing | Make the audience's outcome central and present the product as assistance |

Match awareness: an unfamiliar audience may need the problem/desire first, while an informed audience
may need mechanism, proof or offer details. Explain a technical term through the problem it solves,
then define it accurately if needed. Use the audience's everyday language without concealing material
conditions. Replace vague praise with an observable benefit, example or evidence.

For value, clarify the desired result, why it is credible, the expected time and the effort required.
Do not invent certainty, speed, scarcity, authority or testimonials. Keep one honest persuasion cue
when supported. Read the narration aloud, cut awkward jargon, and let each line motivate the next.
Align the delivery, image, music and final payoff with the intended emotion, such as relief or pride.

The article discusses Schwartz's awareness framing, Miller's audience-centered story, Ogilvy's
specificity, Hormozi's value framing, Cialdini's persuasion principles and Sugarman's sentence flow.
It also points to Wiebe's customer-language approach, Handley's useful/empathic writing and plain
language guidance. Apply these as editorial questions tied to actual audience evidence.
These are creative lenses, not an experimentally verified guarantee for the requested video. The
source notes identify which primary pages were actually consulted and which books remain further
reading. Do not claim to have read an unavailable book in full.

Keep the copy about the viewer's subject. Do not script lines, captions or end cards that describe
how the video was produced or mention AI, prompts, agents or tools, unless the user requests that
content. A required synthetic-media disclosure belongs in the publishing platform's own setting.

Before producing final speech, inspect ten decisions: immediate opening point, appropriate awareness,
audience vocabulary, coherent structure, audience-centered outcome, concrete wording, credible value,
substantiated proof, clean spoken rhythm, and one feasible CTA. Resolve a failed decision directly.
A ten-point editorial review is not a predicted conversion score.

## Review the result, not the aesthetic labels

Use loaded fonts and consistent artwork, deliberate acceleration and readable holds, aligned grids,
clear hierarchy, restrained glow/texture, relevant imagery and a simple end card. A minimum half-second
settled hold may be a useful starting point for a very short label. Full phrases need enough time
to read. Check that the message survives muted playback, a small screen and the actual crop.

Do not promise that a hook within three seconds, a particular retention rate, a stock background,
a human face or an uppercase CTA guarantees reach or sales. These are choices to inspect and test
against real results. Keep claims about savings and production speed specific to observed work.
