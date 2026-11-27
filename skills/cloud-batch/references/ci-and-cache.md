# CI and the remote compiler cache

Read this when you set up the compiler cache for batch machines, CI and local worktrees, or when you make CI faster and cheaper. sccache, Cloudflare R2 and CMake facts were checked on **2026-11-26** (see [sources](sources.md)).

## The remote compiler cache

Use sccache with an S3-compatible bucket, so batch machines, CI and local builds share compiled objects. A short session then spends its time testing instead of compiling dependencies. Cloudflare R2 suits this well because it charges no egress.

**R2 prices seen on 2026-11-26** (Standard class): US$0.015 per GB-month, US$4.50 per million Class A operations (writes), US$0.36 per million Class B operations (reads). The free tier covers 10 GB-month, 1 million Class A and 10 million Class B operations a month. Check the [R2 pricing page](https://developers.cloudflare.com/r2/pricing/) again before a plan.

**Lifecycle rules** on the bucket, created only with the person's go:

- expire objects after 30 days (`Expiration` with `Days: 30`);
- abort incomplete multipart uploads after 1 day (`AbortIncompleteMultipartUpload` with `DaysAfterInitiation: 1`). Every R2 bucket has a default rule of 7 days, and 1 day is tighter.

**sccache settings** inside the build's environment only:

| Variable | Value |
| --- | --- |
| `SCCACHE_BUCKET` | The bucket name |
| `SCCACHE_ENDPOINT` | `https://<account id>.r2.cloudflarestorage.com` |
| `SCCACHE_REGION` | `auto` for R2 |
| `SCCACHE_S3_KEY_PREFIX` | `sccache/`, so other cache layers can share the bucket under other prefixes |
| `SCCACHE_S3_USE_SSL` | `true` |
| `SCCACHE_IDLE_TIMEOUT` | `0`, so the server runs until it is stopped |
| `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY` | The R2 token's key pair, mapped from the project's own variables |

In CMake, set `CMAKE_C_COMPILER_LAUNCHER=sccache` and `CMAKE_CXX_COMPILER_LAUNCHER=sccache`. The launcher works with the Makefile and Ninja generators only, not with the Xcode or Visual Studio generators, so use Ninja for cached builds.

**Remote machines get the cache credentials through stdin** of the SSH command, read with `IFS= read -r` and kept only in the job's environment. They are never written to disk:

```bash
printf '%s\n%s\n' "$PROJECT_R2_KEY_ID" "$PROJECT_R2_SECRET" | ssh -i ~/.ssh/<project>-batch-<session> -o UserKnownHostsFile=~/.ssh/<project>-batch-<session>.known_hosts -o StrictHostKeyChecking=accept-new -o BatchMode=yes batch@<host> 'IFS= read -r AWS_ACCESS_KEY_ID; IFS= read -r AWS_SECRET_ACCESS_KEY; export AWS_ACCESS_KEY_ID AWS_SECRET_ACCESS_KEY; uv run ~/<run name>-run.py batch/results/<run name>'
```

`printf` is a shell builtin, so the secrets do not appear in the process list. In a Python orchestrator, pass them as the `input` of `subprocess.run`, never as arguments. The other sccache variables hold no secret, so `run.py` or the prepared image sets them.

### Share objects across folders

- Set `SCCACHE_BASEDIRS` (sccache 0.14.0 and later) to the tree root, or to every worktree root, separated by `:` (`;` on Windows). Paths must be absolute. Objects then hash without absolute paths, and different folders share them. The longest matching prefix wins.
- The server reads its base folders when it starts. So start one server per build with its own port (`SCCACHE_SERVER_PORT`), or stop the server before you change the variable.
- Put the clone at the same path as the CI runners, such as `/home/runner/work/<repo>/<repo>` for GitHub-hosted Linux runners, so CI and batch machines share objects even without base folders.
- Add path prefix maps to the compile flags (`-ffile-prefix-map=<tree root>=.`, which also covers `-fmacro-prefix-map`), so paths inside objects and debug info do not depend on the checkout folder.

### What goes in the bucket

- The bucket holds compiler objects, dependency sources, prebuilt third-party packages and tools. It never holds the project's own linked libraries or binaries, so every run links the project fresh from cached objects.
- Use keys that change with everything they depend on: compiler version, flags, dependency versions, the lock file.
- Report the hit rate after every batch: `sccache --show-stats` prints a `Cache hits rate` line. Run `sccache --zero-stats` before the build so the number covers that build alone.

## Keep CI fast and cheap

**Two levels:**

- Every push runs a small set that answers in about 10 to 15 minutes, such as format, lint and unit tests on two systems. Superseded push runs may cancel themselves.
- Every other job runs only when started by hand (`workflow_dispatch` on GitHub Actions): the full matrix, once at the end of a block of work, with its failures fixed together. A run started by hand always finishes. Never cancel one.

**The full matrix:**

- builds exactly what ships, every architecture the releases hold, and tests the common platforms;
- has no job that repeats what another job proves;
- gives every job and step a short fixed name.

**Build each artifact once per run.** Jobs hand built SDKs or binaries to each other as run artifacts with a short retention, such as 1 day. The slices of a multi-platform package build in parallel jobs, and one job joins them.

**Shard the longest suites,** such as sanitizers and long integration suites, so that together they run every test once, through a shard index and count, such as `--shard <i>/<n>`.

**The cache in CI:**

- Use the same bucket as the batch machines, with repository secrets of the same names as the local variables.
- Pull requests from forks get no secrets, so they build without the cache. That is expected.
- Every job that compiles ends with a step that prints the cache hit counts.

**Every cache in layers,** each under its own prefix in the bucket:

- compiler objects;
- dependency sources;
- prebuilt dependency packages, such as OpenSSL;
- Gradle dependencies;
- downloaded tools, such as a shader compiler, the Emscripten SDK and Gradle itself.

Each layer is an archive under a key that changes with everything it depends on. One job saves each layer, only on the default branch, and only when it succeeded with a key the bucket lacks. All other jobs only read. The bucket expires every object after 30 days.

**Smaller debug info:** CI's Debug trees keep only file and line information (`-g1`, or the project's equivalent), so cache objects stay small and links use less memory. Release builds keep full debug info for crash reports.

**Two repository habits to offer, which the person decides:** deleting the CI runs of deleted branches so the runs list stays readable, and letting no bot open pull requests, dependency updaters included, since a pull request stays in the history for good.

**Self-hosted runners never serve a public repository,** since a pull request from a fork could run code on them.

## GitHub-hosted runners

Seen on 2026-11-26. Check the runner list and prices again before a plan.

| Runner | Labels | Hardware | Price per minute in private repositories |
| --- | --- | --- | --- |
| Standard macOS, Apple silicon | `macos-latest`, `macos-15`, `macos-26` | 3 CPU, 7 GB, 14 GB SSD | US$0.062 |
| Standard macOS, Intel | `macos-15-intel`, `macos-26-intel` | 4 CPU, 14 GB | US$0.062 |
| Larger macOS, Intel | `macos-26-large` | 12 CPU, 30 GB | US$0.077 |
| Larger macOS, Apple silicon | `macos-26-xlarge` | 5 CPU with GPU acceleration, 14 GB | US$0.102 |
| Standard Linux x64, 2 cores | `ubuntu-latest` | 2 CPU | US$0.006 |

- Standard runners are free for public repositories. Larger runners always bill.
- Each plan includes a monthly amount in dollars for private repositories, such as US$12 on Free and US$18 on Pro or Team.
- A job runs at most 6 hours.
- Free, Pro and Team accounts run at most 5 macOS jobs at once.
- Each macOS image carries one major Xcode version with several minor versions, listed in the [runner-images](https://github.com/actions/runner-images) README. Select the Xcode the project needs with `sudo xcode-select -s /Applications/Xcode_<version>.app`, and check that the version exists in the image.
- Nested virtualization does not work on Apple silicon macOS runners, so the Android emulator gets no hardware acceleration there. Run emulator tests on a Linux machine with KVM (see [Android emulator](android-emulator.md)).
- Hosted runners are virtual machines. Do not take GPU timings from them.

**Start and watch the full matrix by hand:** `gh workflow run <workflow> --ref main`, then `gh run watch <run id>` in the background, or `gh run view <run id> --json status,conclusion` every several minutes, not every few seconds.

## Sources

Checked on 2026-11-26: [sccache S3](https://github.com/mozilla/sccache/blob/main/docs/S3.md), [sccache configuration](https://github.com/mozilla/sccache/blob/main/docs/Configuration.md), [sccache v0.14.0](https://github.com/mozilla/sccache/releases/tag/v0.14.0), [R2 pricing](https://developers.cloudflare.com/r2/pricing/), [R2 lifecycles](https://developers.cloudflare.com/r2/buckets/object-lifecycles/), [R2 S3 API](https://developers.cloudflare.com/r2/api/s3/api/), [CMAKE_LANG_COMPILER_LAUNCHER](https://cmake.org/cmake/help/latest/variable/CMAKE_LANG_COMPILER_LAUNCHER.html), [GCC options for code generation](https://gcc.gnu.org/onlinedocs/gcc/Overall-Options.html), [workflow_dispatch](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows), [secure use of GitHub Actions](https://docs.github.com/en/actions/reference/security/secure-use) and [gh run](https://cli.github.com/manual/gh_run). See [sources](sources.md) for the full record.
