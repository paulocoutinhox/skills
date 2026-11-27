# Briefs, copy direction and reusable video recipes

Write a script the audience can understand. Then make it buildable with frame ranges, assets and
motion. A precise prompt cuts down on guessing. It does not guarantee what a given agent will
produce, and you still need to check the rendered result.

## Prompt structure

Give the purpose/audience/language, output dimensions/fps/duration, approved assets, brand colors,
scene table, motion, typography, narration/captions, safe areas and deliverables. Say whether frame
ranges include transition overlaps. Be honest about which required assets are missing. Name the
real project directory so a coding agent does not create a second project by mistake.

You can send a first brief in interactive Claude Code, through its `-p` mode, or directly to another
compatible agent. Keep improving scene by scene against Studio and exported stills. Ask for a
specific change such as “reduce the product arrival from 24 to 16 frames and keep the speech hold,”
then check the timing that depends on it again. A vague “make it more professional” needs concrete
design decisions.

The recipes below assume the assets were supplied or approved. Their colors, typography, durations
and safe areas are working examples. Replace copy and claims with material the owner approved. Load
only the references the requested task needs.

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

Create a 150-frame, 30fps vertical logo sting with the supplied artwork. Frames `[0,20)` set up the
background and build anticipation, `[20,60)` reveal the logo with a playful spring, and `[60,150)`
settle the tagline and hold. Add light glow or motion blur only if the brand fits it. This slower
opening suits a brand sting. For an ad placement that needs text right away, show the hook at frame
zero instead of reusing the same blank intro.

### Product demo

Use the 450-frame plan above: problem/desire, real product, benefits, offer/CTA. Rotating a flat
image can add movement. A true 360-degree showcase needs the real footage or 3D model for it.
For physical goods, tie a demonstration to the benefit, show readable labels, and avoid fake
before/after proof. Lifestyle footage must have the right rights.

### Quote card

Create a 1080×1080, 240-frame, 30fps card. Use `[0,30)` for the quote mark and clear context about
who is speaking, `[30,180)` for a short approved quote with six-frame word staggers, and `[180,240)`
for an author/source hold. Pick a quote that fits the reading time. For longer text, reveal the
phrase all at once or make the video longer. Check the speaker and the quote. Do not attribute
generated words to a real person.

### Countdown

Create a 180-frame, 30fps sequence. Show 5, 4, 3, 2 and 1 for 30 frames each, then a 30-frame final
reveal. This fills all six seconds. Each number can arrive with a spring and a small shake that is
the same on every render. Use a steady baseline/scale and keep the reveal readable. Five one-second
numbers alone add up to five seconds, so do not leave an accidental blank sixth second.

### Testimonial or social proof

Create a 360-frame, 30fps piece with an approved portrait, the exact approved quote and a clear name
and source. Use `[0,60)` to introduce the person, `[60,270)` for the readable quote, and
`[270,360)` for a calm brand/CTA hold. Add rating stars only when the rating is real and its context
is approved. A synthetic actor or AI voice cannot be shown as a real customer's recording.

### Lesson opener

Create a 1920×1080, 300-frame, 30fps intro. Use `[0,60)` for context/module title, `[60,240)` for
lesson name/number and a readable lower-third, then `[240,300)` for the handoff. If a wipe overlaps
an included content scene, subtract that overlap from the total or lengthen the scenes on purpose.
Reuse the same title/lower-third setup across lessons, and keep real code and screen highlights
large enough for where people will watch.

## Adapt the structure to the destination

For a normal app demo, use real screen recordings with labels, focus highlights, captions and
planned zooms that keep the context. An App Store preview has different rules: the checked Apple
requirements say 15–30 seconds, accepted formats for each device and up to three previews per
localization. Show the real app experience with footage captured on the device, and keep the message
clear without sound. Do not assume that a random 1080×1920 social ad, a promo full of mockups or an
outside sales end card meets Apple's preview rules. Check the chosen platform/device specs and hand
off the store submission separately.

For fashion, use approved garment images or try-on footage, rhythmic cuts and an honest drop/date.
Pick beat positions from the real track. Build a clean master when platform music will be added
later. Do not promise reach benefits from a particular trending sound.

For courses, put explanation, lesson flow, code/screen readability, recap cards and accurate captions
first. For presentations, use a 16:9 working format such as 1920×1080, chart drawings, count-ups and
clear transitions. A video plays on a fixed schedule and cannot count on a live speaker to control
how long the audience has to read.

Common starting formats are 9:16 social video, 16:9 presentations/landscape video and 1:1 feed cards.
Follow the real placement requirements over these examples. Rearrange the layout for each aspect
ratio instead of just cropping off important text. Keep the same honest promise when you make A/B
variants.

## Copy and emotional direction

Use real customer language from supplied reviews, interviews or support conversations when that
material is available and approved. Pull out the real frustration, desired result and objections,
then paraphrase them accurately. Remove private details and never turn a paraphrase into a fake
quote. Combine useful information, a goal the viewer can reach and empathy for the viewer's
situation. Keep one idea per spoken line and explain needed technical terms through the problem
they solve.

Pick one main structure instead of stacking every formula into a short piece:

| Structure | Use |
| --- | --- |
| PAS: problem → agitation → solution | The audience knows a concrete problem. Keep the stakes honest |
| AIDA: attention → interest → desire → action | Introduce an unfamiliar offer with enough explanation |
| BAB: before → after → bridge | Show a change you can back up and explain the path |
| Viewer-as-hero framing | Put the audience's result at the center and show the product as help |

Match how much the audience already knows. An audience new to the topic may need the problem/desire
first, while an informed audience may need how it works, proof or offer details. Explain a technical
term through the problem it solves, then define it accurately if needed. Use the audience's everyday
words without hiding important conditions. Replace vague praise with a benefit people can see, an
example or evidence.

For value, make clear the desired result, why it is believable, the expected time and the effort
needed. Do not invent certainty, speed, scarcity, authority or testimonials. Keep one honest
persuasion cue when you can back it up. Read the narration aloud, cut awkward jargon, and let each
line lead to the next. Match the delivery, image, music and final payoff to the feeling you want,
such as relief or pride.

The source guide in [sources](sources.md) discusses Schwartz's awareness framing, Miller's
audience-centered story, Ogilvy's specificity, Hormozi's value framing, Cialdini's persuasion
principles and Sugarman's sentence flow. It also points to Wiebe's customer-language approach,
Handley's useful/empathic writing and plain language guidance. Use these as editing questions tied
to real evidence about the audience. They are creative ways of looking at copy, not a tested
guarantee for the requested video. The source notes say which primary pages were really read and
which books stay as further reading. Do not claim to have read an unavailable book in full.

Keep the copy about the viewer's subject. Do not write lines, captions or end cards that describe
how the video was made or mention AI, prompts, agents or tools, unless the user asks for that
content. A required synthetic-media disclosure belongs in the publishing platform's own setting.

Before you produce the final speech, check ten decisions: a clear point right at the start, the
right level for what the audience knows, the audience's words, a structure that holds together, a
result centered on the audience, concrete wording, believable value, proof you can back up, a clean
spoken rhythm, and one doable CTA. Fix a failed decision directly. A ten-point editing review is not
a predicted conversion score.

## Review the result, not the style labels

Use loaded fonts and matching artwork, planned speed-up and readable holds, lined-up grids, clear
hierarchy, light glow/texture, relevant images and a simple end card. A settled hold of at least
half a second may be a useful starting point for a very short label. Full phrases need enough time
to read. Check that the message still works when muted, on a small screen and in the real crop.

Do not promise that a hook within three seconds, a given retention rate, a stock background,
a human face or an uppercase CTA guarantees reach or sales. These are choices to check and test
against real results. Keep claims about savings and production speed tied to work you saw.
