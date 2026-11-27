# Voice, music, timing and captions

Read this reference when a video has recorded or generated narration, music, speech captions or
visuals that react to audio. Keep the real audio files and the reviewed timing together through
every revision.

## Prepare speech that fits the story

Choose between a supplied recording, approved cloud TTS and a synthesizer you have locally.
ElevenLabs is one cloud option. macOS `say` can give a rough placeholder voice. Piper or an
available Coqui deployment can work locally, after you check the specific maintained package, the
voice/model license and machine support. Browser speech synthesis plays differently on each
platform and does not give you a downloadable asset you can reproduce. Lock usable audio files
before rendering.

Find out which voices/models the real account can use. Try the same typical sentence with two or
three voices, and judge native-language pronunciation, warmth, clarity and fit for the role. Do not
hardcode the voice IDs of the source guide in [sources](sources.md) or guess language quality from a
display name. A clear explaining voice and an energetic ad voice need different direction.

Write short spoken sentences. Test names, numbers and acronyms, and respell them or use the chosen
model's supported pronunciation controls when needed. Keep the on-screen text spelled correctly even
if the TTS input uses phonetic spelling. Punctuation and supported emotion tags can guide delivery.
Compare a short generated sample before you produce every scene.

Lower stability or higher style can make delivery more expressive on models that offer those
controls, but which values are accepted, their ranges and the quality depend on the chosen model.
The source guide's `stability=0.3` and `style=0.55` are starting points for a tryout, not settings
to force onto every model. Some models use different stability choices or do not support a given
control. Avoid unsupported options and claims that one setup always sounds natural.

Generate one clip per scene when that helps revisions and timing. Keep approved clips instead of
generating them again on each render. Record the script revision, voice/model and real clip duration
in the project brief. Never put API credentials in `public/`, browser components, props or logs.

## Calculate the speech intervals

For a clip that lasts `seconds`, reserve at least `ceil(seconds * fps)` frames. Let:

- `s` = scene start in the composition.
- `a` = local opening delay.
- `L` = reserved speech length.
- `b` = silent tail.
- `d = a + L + b` = scene duration.
- `t` = overlap into the next scene.

The current speech interval is `[s+a, s+a+L)`. The next scene starts at `s+d-t`, and its speech
starts at `s+d-t+aNext`. The next speech must start at or after the current speech ends, plus the
pause you want. Check those **absolute** intervals. A tail longer than the transition is a useful
safe default, but the full formula includes both narration delays.

Example at 30fps: scene A has a five-frame delay, a 60-frame voice and a 25-frame tail, so it lasts
90 frames. A 15-frame overlap starts scene B at frame 75. With B's five-frame speech delay, B speaks
at frame 80. A's speech ended at frame 65, which leaves a 15-frame pause. Leaving A's five-frame
delay out of its duration would shorten its planned rest and can cut speech at other boundaries.

Place speech at the scene's local opening delay. Use the shared `from` timing prop directly on the
audio component or a `Sequence from={a}` wrapper. Check that the scene does not unmount before the
audio finishes. Keep the music at composition level when it should play across transitions. Avoid
playing it twice by mistake in overlapping scenes. Use `Audio` from `@remotion/media`, which uses
`trimBefore` and source-frame `durationInFrames`, and whose time in the parent changes with playback
rate. Do not use the deprecated `trimAfter`. Placement `from` is a separate offset on the parent
timeline.

If a 15-second ad's recorded speech is longer than the available holds, shorten the script, change
the delivery, or agree to a longer composition. Do not quietly speed up speech or cut the last word.
Recalculate transitions, captions, music volume curve and export duration after you change timing.

## Mix so speech is easy to understand

Start with clean speech and an instrumental bed that leaves room for it. Lower the music during
speech, shape fade-ins/fade-outs with volume driven by the frame, and add a controlled swell only
where it helps the payoff. Avoid a sudden cut at the final frame.

Use a numeric volume calculated from the relevant frame, as `@remotion/media` recommends.

Volume props are linear amplitude multipliers, not LUFS values. A gain ratio of `g` equals
`20 * log10(g)` dB. A value such as music `0.06` says nothing on its own about the final loudness
difference, because the source recordings have different levels. Raising narration can cause
clipping. Use the gain/normalization/limiting tools you have on purpose and check the final encoded
mix.

The source guide's speech at about −21 LUFS against music at about −36 LUFS shows roughly 15 LU of
separation. Treat the 12–16 difference as a starting point for listening comparisons, not a platform
master spec. Measure stems over similar time spans and check the moments with speech. A final mixed
file cannot show the separate stem levels. Find out the final integrated loudness and true-peak
requirements for the real destination.

With FFmpeg installed, check the final file and stems with the native meter:

```bash
ffmpeg -i out/ad.mp4 -af ebur128=peak=true -f null -
ffmpeg -i public/vo/scene-01.wav -af ebur128=peak=true -f null -
ffmpeg -i public/music/bed.wav -af ebur128=peak=true -f null -
```

Read the integrated result, short-term behavior and peaks, then listen on headphones and a small
speaker. Compare stem measurements after you account for gains and timeline placement. Do not claim
that running the meter normalized the file or proved that speech is easy to understand.

## Choose a caption route

| Route | Use and limit |
| --- | --- |
| Manual timing | Short approved script with known cue times. No transcription install needed |
| Existing SRT | Import with `parseSrt({input: srtText})` from `@remotion/captions` and review timestamps/text |
| Local Whisper.cpp | Private/local transcription after downloading software/models and meeting native requirements |
| Cloud transcription | Approved upload and paid/account access, using the current supported service contract |

`@remotion/captions` renders and structures timed text. It does not transcribe speech on its own.
For local Whisper use `@remotion/install-whisper-cpp`: install a supported Whisper.cpp version,
download the chosen model into a known folder, run transcription, convert results with `toCaptions`,
and save the reviewed captions as project data. These are steps with dependencies, not a helper
bundled here.

The local input must be **16-bit PCM WAV at 16kHz**. Resample a copy and keep the approved master:

```bash
ffmpeg -i public/vo/scene-01.mp3 -ar 16000 -ac 1 -c:a pcm_s16le public/vo/scene-01-transcription.wav
```

Choose a multilingual model such as `small` or `medium` for Portuguese or mixed-language speech.
Models ending in `.en` are English-only. Do not use the source guide's `medium.en` example for
Portuguese. Bigger models use more memory and time but transcribe better. Match Whisper.cpp and
Remotion versions, pass the documented `whisperCppVersion` where required, and ask for token-level
timestamps for word highlighting. Set `modelFolder` explicitly if model files are outside the
default models directory. Downloads need network and disk, even though transcription can then stay
local.

Cloud `@remotion/openai-whisper` is another package option. Its installed version does not promise
access to every current speech endpoint/model. Check the real wrapper before you choose it. Get
permission for private uploads or use the local/manual route. Keep credentials on the server.
Do not upload just to show off a skill.

## Render and review captions

A `Caption` includes `text`, `startMs`, `endMs`, `timestampMs` and `confidence` according to the
installed type. With local scene captions, compare `frame / fps * 1000` against local cue times.
With global captions, either render outside the scene or add the scene offset explicitly.

For phrase captions, show a cue when `startMs <= timeMs < endMs`. For word highlighting,
`createTikTokStyleCaptions` groups captions into pages with tokens. Its `fromMs`/`toMs` token values
are absolute within the input caption timeline. If you render in a page-local Sequence, add the
page's start back to local time before you compare tokens. Apply a scene offset only when the source
data uses scene-local times. Keep the whitespace in the token text instead of joining words without
spaces. Group size is a reading choice.

A normal phrase-level SRT does not hold word-level timing you can trust. Show phrase pages, get
alignment/transcription, or mark the timing as an estimated draft. Do not call a rough word split
accurate sync. Fix transcription errors, especially names and punctuation.

Use high-contrast type over a scrim/shadow, a limited number of lines, and safe areas for the
specific placement. Check the real language, the longest phrase and the smallest screen you expect.
Burned-in captions cannot be turned off. Deliver SRT/VTT separately when asked, and do not claim
that a burned overlay is an accessible subtitle track viewers can select. After you change speech,
regenerate and review the timings that depend on it.

Test the first/last word of every scene, silent gaps, cut boundaries, transition overlaps and caption
page changes. A missing local compiler, a failed model download or a refused cloud credential means
transcription did not happen. Finish the manual/source work and report the exact missing dependency
instead of making up a transcript.
