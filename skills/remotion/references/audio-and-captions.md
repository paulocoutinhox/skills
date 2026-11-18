# Voice, music, timing and captions

Read this reference when a video contains recorded/generated narration, music, speech captions or
audio-reactive visuals. Keep the actual audio files and reviewed timing together through revisions.

## Prepare speech that fits the story

Choose between a supplied recording, authorized cloud TTS and a locally available synthesizer.
ElevenLabs is one cloud option. macOS `say` can supply a scratch voice. Piper or an available Coqui
deployment can be local alternatives after checking the specific maintained package, voice/model
license and host support. Browser speech synthesis is platform-dependent playback and does not
automatically provide a reproducible downloadable asset. Freeze usable audio files before rendering.

Discover voices/models available to the actual account. Audition the same representative sentence
with two or three voices, assessing native-language pronunciation, warmth, intelligibility and role.
Do not hardcode a blog's voice IDs or infer language quality from a display name. A clear explanatory
voice and an energetic advertising voice need different direction.

Write short spoken sentences. Test names, numbers and acronyms, and respell or use the selected
model's supported pronunciation controls when needed. Keep displayed copy correctly spelled even
if the TTS input uses phonetic wording. Punctuation and supported emotion tags can direct delivery.
Compare a short generated sample before producing every scene.

Lower stability or higher style can increase expressiveness on models exposing those controls,
but acceptance/ranges and quality depend on the chosen model. The blog's `stability=0.3` and
`style=0.55` are audition starting points, not settings to force onto every model. Some models
use different stability choices or do not support a given control. Avoid unsupported options and
claims that one configuration always sounds natural.

Generate one clip per scene when revisions and timing benefit. Preserve approved clips rather than
regenerating them each render. Record script revision, voice/model and actual clip duration in the
project brief. Never place API credentials in `public/`, browser components, props or logs.

## Calculate the speech intervals

For a clip lasting `seconds`, reserve at least `ceil(seconds * fps)` frames. Let:

- `s` = scene start in the composition.
- `a` = local opening delay.
- `L` = reserved speech length.
- `b` = silent tail.
- `d = a + L + b` = scene duration.
- `t` = overlap into the next scene.

The current speech interval is `[s+a, s+a+L)`. The next scene starts at `s+d-t`, and its speech starts
at `s+d-t+aNext`. Require the next speech start to be at or after the current speech end, plus the
desired pause. Inspect those **absolute** intervals. A tail longer than the transition is a useful
conservative default, but the full formula includes both narration delays.

Example at 30fps: scene A has a five-frame delay, a 60-frame voice and a 25-frame tail, so it lasts
90 frames. A 15-frame overlap starts scene B at frame 75. With B's five-frame speech delay, B speaks
at frame 80. A's speech ended at frame 65, leaving a 15-frame pause. Omitting A's five-frame delay
from its duration would reduce its planned rest and can cut speech at other boundaries.

Place speech at the scene's local opening delay, using the shared `from` timing prop directly on the
audio component or a `Sequence from={a}` wrapper. Verify the scene does not unmount before the audio finishes.
Keep the music at composition level when it should span transitions.
Avoid accidentally playing it twice in overlapping scenes. Choose `Audio` from the installed API:
current `@remotion/media` or the project's compatible legacy Remotion component. Do not mix prop
assumptions between versions. Current `@remotion/media` uses `trimBefore` and source-frame
`durationInFrames`, with parent occupancy affected by playback rate. `trimAfter` is deprecated there.
Legacy APIs may use it as a source endpoint. Placement `from` is a separate parent-timeline offset.

If a 15-second ad's recorded speech exceeds the available holds, shorten the script, adjust delivery,
or agree to a longer composition. Do not silently speed up speech or cut the last word. Recalculate
transitions, captions, music envelope and export duration after changing timing.

## Mix for intelligibility

Start with clean speech and an instrumental bed that leaves room for it. Reduce music during speech,
shape entrances/exits with frame-derived volume, and place a controlled swell only where
it supports the payoff. Avoid sudden truncation at the final frame.

Current `@remotion/media` recommends numeric volume calculated from the relevant frame. A volume
callback remains available in compatible APIs, but its frame semantics must match the trimmed/offset
clip. Do not assume an old callback recipe is the preferred current contract.

Volume props are linear amplitude multipliers, not LUFS values. A gain ratio of `g` corresponds to
`20 * log10(g)` dB. A value such as music `0.06` says nothing by itself about the final loudness
difference because the source recordings have different levels. Raising narration can cause clipping.
Use available gain/normalization/limiting tools deliberately and inspect the final encoded mix.

The blog's speech around −21 LUFS versus music around −36 LUFS illustrates roughly 15 LU of
separation. Treat the 12–16 difference as a starting listening comparison, not a platform master
specification. Measure stems over comparable time spans and inspect speech-active moments. A final
mixed file cannot reveal the isolated stem levels. Resolve final integrated loudness and true-peak
requirements for the actual destination.

With FFmpeg installed, inspect the final file and stems using the native meter:

```bash
ffmpeg -i out/ad.mp4 -af ebur128=peak=true -f null -
ffmpeg -i public/vo/scene-01.wav -af ebur128=peak=true -f null -
ffmpeg -i public/music/bed.wav -af ebur128=peak=true -f null -
```

Read the integrated result, short-term behavior and peaks, then listen on headphones and a small
speaker. Compare stem measurements after accounting for gains and timeline placement. Do not claim
that merely running the meter normalized the file or proved speech intelligibility.

## Choose a caption route

| Route | Use and boundary |
| --- | --- |
| Manual timing | Short approved script with known cue times. No transcription installation needed |
| Existing SRT | Import with `parseSrt({input: srtText})` from `@remotion/captions` and review timestamps/text |
| Local Whisper.cpp | Private/local transcription after downloading software/models and meeting native prerequisites |
| Cloud transcription | Authorized upload and paid/account capability, using the current supported service contract |

`@remotion/captions` renders/structures timed text. It does not transcribe speech by itself. For local
Whisper use `@remotion/install-whisper-cpp`: install a supported Whisper.cpp version, download the
selected model into a known folder, run transcription, convert results with `toCaptions`, and save
the reviewed captions as project data. This is a dependency sequence, not a helper bundled here.

The local input must be **16-bit PCM WAV at 16kHz**. Resample a copy, preserving the approved master:

```bash
ffmpeg -i public/vo/scene-01.mp3 -ar 16000 -ac 1 -c:a pcm_s16le public/vo/scene-01-transcription.wav
```

Choose a multilingual model such as `small` or `medium` for Portuguese or mixed-language speech.
Models ending in `.en` are English-only. Do not use the article's `medium.en` example for Portuguese.
Model size trades memory/time against transcription quality. Match Whisper.cpp and Remotion versions,
pass the documented `whisperCppVersion` where required, and request token-level timestamps for word
highlighting. Set `modelFolder` explicitly if model files are outside the default models directory.
Downloads require network/disk even though transcription can subsequently stay local.

Cloud `@remotion/openai-whisper` is an alternative package, not a guarantee that every contemporary
speech endpoint/model is exposed by its installed version. Check the actual wrapper before choosing
it. Get authorization for private uploads or use the local/manual route. Keep credentials server-side.
Do not upload just to demonstrate a skill.

## Render and review captions

A `Caption` includes `text`, `startMs`, `endMs`, `timestampMs` and `confidence` according to the
installed type. With local scene captions, compare `frame / fps * 1000` against local cue times.
With global captions, either render outside the scene or add the scene offset explicitly.

For phrase captions, display a cue when `startMs <= timeMs < endMs`. For word highlighting,
`createTikTokStyleCaptions` groups captions into pages with tokens. Its `fromMs`/`toMs` token values
are absolute within the input caption timeline. If rendering in a page-local Sequence, add the page's
start back to local time before comparing tokens. Apply a scene offset only when the source data
uses scene-local times. Preserve whitespace in
the token text rather than concatenating words without spaces. Group size is a reading choice.

An ordinary phrase-level SRT does not contain trustworthy word-level timing. Display phrase pages,
obtain alignment/transcription, or mark an estimated timing draft. Do not describe approximate word
division as accurate synchronization. Correct transcription errors, especially names and punctuation.

Use high-contrast type over a scrim/shadow, a limited line count, and placement-specific safe areas.
Check the actual language, longest phrase and smallest intended screen. Burned-in captions cannot be
disabled. Deliver SRT/VTT separately when requested rather than claiming a burned overlay is an
accessible selectable subtitle track. After changing speech, regenerate/review dependent timings.

Test the first/last word of every scene, silence gaps, cut boundaries, transition overlaps and caption
page changes. A missing local compiler, model download failure or denied cloud credential leaves
transcription unperformed. Finish manual/source work and report the exact dependency instead of
fabricating a transcript.
