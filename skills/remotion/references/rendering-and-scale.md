# Rendering, reusable templates and product integrations

Start with a locally inspected composition and a clear output contract. Examples assume the actual
entrypoint is `src/index.ts` and a registered `ProductAd` composition exists. Substitute inspected
paths and IDs. Commands are examples, not evidence that a render or deployment ran.

## Choose and inspect the export

| Output | Decision |
| --- | --- |
| H.264 MP4 | Broad compatibility for ordinary opaque social/web delivery. CRF 18 is one quality starting point |
| H.265 | Potentially smaller files, with compatibility and encoding-cost tradeoffs |
| VP9 WebM | Web delivery when target playback supports it |
| GIF | Short silent loops, restricted colors and potentially large files. Reduce frame rate/size deliberately |
| VP8/VP9 with alpha | Transparent web overlays with verified target-player support |
| ProRes 4444 with alpha | Editing/compositing interchange, usually much larger than delivery MP4 |

For codecs supporting CRF, a lower value generally improves quality and increases file size.
Check the actual codec's available controls. Container extension must match the selected codec and
audio combination. Do not rename MP4 to WebM as a conversion or expect H.264 MP4 to preserve alpha.

```bash
npx remotion render src/index.ts ProductAd out/ad.mp4 --codec=h264 --crf=18 --overwrite=false
npx remotion render src/index.ts ProductAd out/ad.gif --codec=gif --every-nth-frame=2 --overwrite=false
```

For a 30fps composition, every second frame produces a 15fps GIF at the same nominal duration.
Check the actual loop, palette, size and destination support. Audio does not survive as a GIF track.

For an existing composition named `Badge`, remove opaque backgrounds and use the checkerboard
preview before exporting alpha:

```bash
npx remotion render src/index.ts Badge out/badge.webm --codec=vp8 --image-format=png --pixel-format=yuva420p --overwrite=false
npx remotion render src/index.ts Badge out/badge.mov --codec=prores --prores-profile=4444 --image-format=png --pixel-format=yuva444p10le --overwrite=false
```

JPEG intermediate frames cannot carry alpha. Confirm transparent areas over contrasting backgrounds
in the actual target application. Alpha WebM on parallel Lambda renders has a documented risk of
flicker at chunk boundaries. Prefer an appropriate ProRes alpha workflow or a local one-pass WebM
render. Fewer chunk boundaries can mitigate the issue but do not prove correctness.

Export stills with `npx remotion still` for early layout review and a candidate thumbnail. The frame
chosen for a published cover depends on that service's actual upload/selection UI. Inspect final
media metadata with available native tools such as FFprobe and play the encoded output fully.

## Props and validated variants

Separate the visual template from per-product data. Define a small Zod schema compatible with the
installed Remotion version, infer the component's prop type, and supply matching `schema` and
`defaultProps` to `Composition`. Use one contract for Studio, Player and final rendering. Current
schemas/peer requirements must be checked before copying an older Zod example.

A practical fictional contract contains `productName`, `priceLabel`, `accentColor` and `image`.
Validate nonempty copy, allowed brand colors, usable file paths and legitimate offer values. Treat
external data as untrusted. Do not accept arbitrary private filesystem paths or arbitrary URLs in
a public render endpoint. Schema controls in Studio do not replace server-side input validation.

Example props file contents for `props/shoe.json`:

```json
{
  "productName": "Cloud Runner",
  "priceLabel": "$129",
  "accentColor": "#22C7B5",
  "image": "img/cloud-runner.png"
}
```

These values are sample data, not a real offer. After creating matching files/components and
validating the schema, render distinct input files to distinct outputs:

```bash
npx remotion render src/index.ts ProductAd out/shoe.mp4 --props=props/shoe.json --overwrite=false
npx remotion render src/index.ts ProductAd out/jacket.mp4 --props=props/jacket.json --overwrite=false
```

`--props` accepts JSON or a JSON file. Prefer files for shell portability, especially on Windows.
Test a normal item, a long translated title, an invalid price and a missing image. Fail the invalid
item with an actionable error, preserve completed outputs, and do not silently substitute a different
product. A normal render can overwrite an existing file by default, so choose new filenames or
disable overwrite when preserving previous outputs.

Use `calculateMetadata` when dimensions/duration depend on the supplied props or measured media.
Resolve resources there before frames render, return the computed `durationInFrames`, `width`,
`height`, `fps` and any transformed `props`, and pass its `abortSignal` to asynchronous fetches. Add narration delays/tails
and subtract transitions in the duration calculation. Do not fetch changing business data afresh on
each frame. Freeze the data/media version used for the job.

For a catalog, review the input mapping, pricing/currency, asset identity, output naming and batch
size before starting. Render two different items and the difficult layout before authorizing a large
run. Record success/failure per input and resume only unfinished/failed work after correcting the
cause. Do not rerender every successful item following one failure. Create a Python/uv batch helper
only if the user explicitly requests automation. No CSV parser or orchestrator ships with this skill.

## Player and server rendering

`@remotion/player` renders the video component directly in a React application. Pass `component`,
`durationInFrames`, `fps`, `compositionWidth`, `compositionHeight`, `inputProps` and optional
`controls`. Do not wrap its component in `Composition`. Scale the browser presentation with styles
while retaining the intended composition dimensions. Test real autoplay/audio restrictions.

Keep the editable form state outside the video component and pass resolved props to the Player.
Dynamic metadata must also be resolved for the Player instead of assuming the root's
`calculateMetadata` executes automatically there. Match preview props, dimensions and duration to
the server job. An interactive preview is not an encoded MP4 and a button drawn within the video
is not automatically a functioning application control.

For a production Node service, the native rendering sequence is:

1. `bundle` from `@remotion/bundler` produces a serve URL/path for the chosen entrypoint.
2. `selectComposition` from `@remotion/renderer` resolves the ID and metadata with validated props.
3. `renderMedia` receives the same serve URL, resolved composition and **same inputProps**, plus
   codec and a unique output location.
4. Wait for successful completion, inspect the artifact, and expose only the authorized output.

Bundle once per source/assets revision when appropriate and reuse the result across jobs. Bound
concurrency and resource use, authenticate requests, isolate output identities, validate asset access,
and support a useful failed/cancelled state. Keep credentials and private payloads on the server.
Do not put the renderer or AWS secrets in the browser bundle. API/queue integration is native
application code, not a reason to distribute a generic helper inside this descriptive package.

## AWS Lambda: prepare, deploy, render, inspect

Lambda parallelizes frame rendering and stitches the output. It needs account setup and can cost
money beyond function runtime: storage, requests, transfer and license conditions also matter.
Use local rendering unless cloud execution is requested or already authorized. Do not create AWS
resources, change IAM, upload private media or launch a large run merely to test written guidance.

Before deployment, resolve the account, supported region, budget, credentials/role, data handling,
output privacy, concurrency quota and cleanup/retention policy. Read current setup, authentication,
permissions and production-checklist docs linked in [sources](sources.md). Prefer an existing
approved workload-identity/role arrangement when supported. An AWS administrator must supply any
missing policy/trust configuration. Do not broaden permissions to overcome an unexplained denial.

For an authorized setup, proceed in this order:

1. Add version-matched `@remotion/lambda` to the project.
2. Configure the documented Lambda execution role and trust policy, plus the caller's actual
   deployment/render permissions. The setup guide's named role/policy must match that chosen flow.
3. Verify authentication and region, required service quota, S3/bucket policy and asset accessibility.
4. Deploy the render function and record the returned name/version/configuration.
5. Bundle/deploy the site and record its actual serve URL and bucket.
6. Submit a small render with the verified composition and props, monitor it to completion, then
   download and inspect the file before expanding the batch.

Example native operations after the prerequisites are resolved:

```bash
npx remotion lambda functions deploy --region=us-east-1
npx remotion lambda sites create src/index.ts --site-name=product-video --region=us-east-1 --throw-if-site-exists
```

Use the **returned serve URL**, represented here by a required placeholder:

```text
npx remotion lambda render [RETURNED_SERVE_URL] ProductAd out/cloud-ad.mp4 --props=props/shoe.json --region=us-east-1 --privacy=private
```

Keep function and site in the selected region and compatible Remotion version. The default region
is `us-east-1` in the researched baseline, but select deliberately. Render output privacy defaults
to `public`. The other values are `private` and `no-acl`. Use private output when required and verify the site's
and assets' own policies separately. The documented site deployment needs a public serve URL for
the headless browser. Do not upload private source/assets under that setup without authorization
for the exposure. Use a local render or an approved architecture when that boundary is unacceptable.
Private output does not make every uploaded resource private. Reusing a site name normally overwrites
that site. The example refuses an existing site, so resolve intentional redeployment separately.

Record render ID, bucket, function/version and job result. The composition ID and local output path
are optional in the CLI. Without a composition ID it prompts for one, so pass it explicitly in
noninteractive runs. Without an output path the file stays in S3, while a local path downloads it. An interrupted waiting process does not by itself prove
the remote job stopped. Use the version's cancellation support when intended and reconcile existing
job/progress/output before retrying. Avoid duplicate paid jobs after a timeout.

Diagnose permission failures by the denied identity/action/resource. Diagnose render failures by
the specific frame, media fetch, native dependency, disk/memory, quota or version mismatch. Preserve
failed-job evidence and complete local work where possible. Upload, submission, successful cloud
render and verified final media are separate states. Cleanup only resources covered by the user's
authorization, preserving approved results and unrelated infrastructure.
