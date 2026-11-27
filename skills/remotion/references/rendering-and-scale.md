# Rendering, reusable templates and product integrations

Start with a composition you checked locally and a clear output target. The examples assume the real
entrypoint is `src/index.ts` and a registered `ProductAd` composition exists. Use the paths and IDs
you found in the project. Commands are examples, not proof that a render or deployment ran.

## Choose and check the export

| Output | Decision |
| --- | --- |
| H.264 MP4 | Plays almost everywhere for normal opaque social/web delivery. CRF 18 is one quality starting point |
| H.265 | Files can be smaller, but it plays in fewer places and costs more to encode |
| VP9 WebM | Web delivery when the target player supports it |
| GIF | Short silent loops, limited colors and possibly large files. Lower frame rate/size on purpose |
| VP8/VP9 with alpha | Transparent web overlays with confirmed support in the target player |
| ProRes 4444 with alpha | Handing off for editing/compositing, usually much larger than a delivery MP4 |

For codecs that support CRF, a lower value usually gives better quality and a larger file.
Check the controls the real codec offers. The container extension must match the chosen codec and
audio combination. Renaming MP4 to WebM does not convert it, and H.264 MP4 does not keep alpha.

```bash
npx remotion render src/index.ts ProductAd out/ad.mp4 --codec=h264 --crf=18 --overwrite=false
npx remotion render src/index.ts ProductAd out/ad.gif --codec=gif --every-nth-frame=2 --overwrite=false
```

For a 30fps composition, keeping every second frame gives a 15fps GIF with the same stated duration.
Check the real loop, palette, size and destination support. A GIF has no audio track.

For an existing composition named `Badge`, remove opaque backgrounds and use the checkerboard
preview before you export alpha:

```bash
npx remotion render src/index.ts Badge out/badge.webm --codec=vp8 --image-format=png --pixel-format=yuva420p --overwrite=false
npx remotion render src/index.ts Badge out/badge.mov --codec=prores --prores-profile=4444 --image-format=png --pixel-format=yuva444p10le --overwrite=false
```

JPEG intermediate frames cannot carry alpha. Check transparent areas over contrasting backgrounds
in the real target app. Alpha WebM on parallel Lambda renders has a documented risk of flicker at
chunk boundaries. Prefer a suitable ProRes alpha workflow or a local one-pass WebM render. Fewer
chunk boundaries can reduce the problem but do not prove the output is correct.

Export stills with `npx remotion still` for early layout review and a possible thumbnail. The frame
used for a published cover depends on that service's real upload/selection screen. Check the final
media metadata with the native tools you have, such as FFprobe, and play the encoded output all the
way through.

## Props and validated variants

Keep the visual template separate from per-product data. Define a small Zod schema that works with
the installed Remotion version, infer the component's prop type from it, and pass matching `schema`
and `defaultProps` to `Composition`. Use one contract for Studio, Player and final rendering. Check
current schemas/peer requirements before you copy an older Zod example.

A practical fictional contract has `productName`, `priceLabel`, `accentColor` and `image`.
Check for non-empty text, allowed brand colors, usable file paths and real offer values. Do not
trust outside data. Do not accept any private filesystem path or any URL in a public render
endpoint. Schema controls in Studio do not replace input checks on the server.

Example props file contents for `props/shoe.json`:

```json
{
  "productName": "Cloud Runner",
  "priceLabel": "$129",
  "accentColor": "#22C7B5",
  "image": "img/cloud-runner.png"
}
```

These values are sample data, not a real offer. After you create matching files/components and
validate the schema, render different input files to different outputs:

```bash
npx remotion render src/index.ts ProductAd out/shoe.mp4 --props=props/shoe.json --overwrite=false
npx remotion render src/index.ts ProductAd out/jacket.mp4 --props=props/jacket.json --overwrite=false
```

`--props` accepts JSON or a JSON file. Prefer files because they work the same in every shell,
especially on Windows. Test a normal item, a long translated title, an invalid price and a missing
image. Stop the invalid item with an error that says what to fix, keep finished outputs, and do not
quietly swap in a different product. A normal render can overwrite an existing file by default, so
pick new filenames or turn off overwrite when you need to keep earlier outputs.

Use `calculateMetadata` when dimensions/duration depend on the supplied props or measured media.
Load resources there before frames render, return the computed `durationInFrames`, `width`,
`height`, `fps` and any changed `props`, and pass its `abortSignal` to fetches that run in the
background. Add narration delays/tails and subtract transitions in the duration math. Do not fetch
changing business data again on each frame. Lock the data/media version used for the job.

For a catalog, review the input mapping, pricing/currency, which asset goes with which item, output
names and batch size before you start. Render two different items and the hardest layout before you
approve a large run. Record success/failure for each input, and after you fix the cause, resume only
the unfinished/failed work. Do not render every successful item again after one failure. Create a
Python/uv batch helper only if the user explicitly asks for automation. No CSV parser or
orchestrator ships with this skill.

## Player and server rendering

`@remotion/player` renders the video component directly in a React app. Pass `component`,
`durationInFrames`, `fps`, `compositionWidth`, `compositionHeight`, `inputProps` and optional
`controls`. Do not wrap its component in `Composition`. Scale how it shows in the browser with
styles while keeping the intended composition dimensions. Test real autoplay/audio limits.

Keep the editable form state outside the video component and pass the final props to the Player.
Work out dynamic metadata for the Player too. Do not assume the root's `calculateMetadata` runs
there automatically. Match preview props, dimensions and duration to the server job. An interactive
preview is not an encoded MP4, and a button drawn inside the video is not a working app control.

For a production Node service, the native rendering steps are:

1. `bundle` from `@remotion/bundler` produces a serve URL/path for the chosen entrypoint.
2. `selectComposition` from `@remotion/renderer` looks up the ID and metadata with validated props.
3. `renderMedia` receives the same serve URL, the looked-up composition and the **same inputProps**,
   plus codec and a unique output location.
4. Wait until it finishes successfully, check the file, and expose only the allowed output.

When it makes sense, bundle once per source/assets revision and reuse the result across jobs. Limit
concurrency and resource use, authenticate requests, keep each job's output separate, check asset
access, and support a useful failed/cancelled state. Keep credentials and private data on the
server. Do not put the renderer or AWS secrets in the browser bundle. API/queue integration is
native app code. It is not a reason to ship a generic helper inside this descriptive package.

## AWS Lambda: prepare, deploy, render, inspect

Lambda renders frames in parallel and joins the output. It needs account setup and can cost money
beyond function runtime: storage, requests, transfer and license terms also matter. Use local
rendering unless the user asks for cloud rendering or already allowed it. Do not create AWS
resources, change IAM, upload private media or start a large run just to test written guidance.

Before deployment, settle the account, supported region, budget, credentials/role, data handling,
output privacy, concurrency quota and cleanup/retention policy. Read the current setup,
authentication, permissions and production-checklist docs linked in [sources](sources.md). Prefer an
existing approved workload-identity/role setup when it is supported. An AWS administrator must
provide any missing policy/trust configuration. Do not widen permissions to get past a denial you
cannot explain.

For an approved setup, go in this order:

1. Add `@remotion/lambda` at the matching version to the project.
2. Configure the documented Lambda execution role and trust policy, plus the caller's real
   deployment/render permissions. The setup guide's named role/policy must match that chosen flow.
3. Check authentication and region, the needed service quota, S3/bucket policy and asset access.
4. Deploy the render function and record the returned name/version/configuration.
5. Bundle/deploy the site and record its real serve URL and bucket.
6. Submit a small render with the checked composition and props, watch it until it finishes, then
   download and check the file before you grow the batch.

Example native operations once the prerequisites are settled:

```bash
npx remotion lambda functions deploy --region=us-east-1
npx remotion lambda sites create src/index.ts --site-name=product-video --region=us-east-1 --throw-if-site-exists
```

Use the **returned serve URL**, shown here by a required placeholder:

```text
npx remotion lambda render [RETURNED_SERVE_URL] ProductAd out/cloud-ad.mp4 --props=props/shoe.json --region=us-east-1 --privacy=private
```

Keep the function and site in the chosen region and on a compatible Remotion version. The default
region is `us-east-1` in the checked baseline, but choose on purpose. Render output privacy defaults
to `public`. The other values are `private` and `no-acl`. Use private output when required, and
check the site's and assets' own policies separately. The documented site deployment needs a public
serve URL for the headless browser. Do not upload private source/assets under that setup without
permission for that exposure. Use a local render or an approved setup when that limit is not
acceptable. Private output does not make every uploaded resource private. Reusing a site name
normally overwrites that site. The example refuses an existing site, so handle a planned
redeploy separately.

Record the render ID, bucket, function/version and job result. The composition ID and local output
path are optional in the CLI. Without a composition ID it asks for one, so pass it explicitly in
non-interactive runs. Without an output path the file stays in S3, while a local path downloads it.
A waiting process that was interrupted does not prove on its own that the remote job stopped. Use
the version's cancellation support when you mean to cancel, and check the existing
job/progress/output before you retry. Avoid duplicate paid jobs after a timeout.

Find the cause of permission failures from the denied identity/action/resource. Find the cause of
render failures from the specific frame, media fetch, native dependency, disk/memory, quota or
version mismatch. Keep evidence from failed jobs and finish local work where you can. Upload,
submission, successful cloud render and checked final media are separate states. Clean up only
resources the user's permission covers, and keep approved results and unrelated infrastructure.
