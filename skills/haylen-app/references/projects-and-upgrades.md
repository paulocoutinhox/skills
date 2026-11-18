# Project creation, builds and upgrades

Use the command reference, distribution and upgrading guides, templates and backend templates in
[sources](sources.md). Work against one chosen engine revision. A newer template is a reference to
compare deliberately, not authority to overwrite unrelated developer changes.

## Prepare the machine and SDKs

```text
haylen doctor
haylen sdk build --target player
haylen sdk build --target ios --target ios-simulator
haylen sdk build --target android
haylen sdk list
```

The launcher needs only uv, which brings the tooling's Python. SDK builds need CMake 3.28+, Ninja and
a C++20 compiler, plus Xcode or the Android SDK for those targets. `doctor` reports tools, SDKs and
what is missing per target without downloading anything. `sdk build` installs into
`build/sdk/<port>-<configuration>/`. Targets of one port can be built together, and building another
target later adds its slice. An app command never compiles the engine. When it stops because no SDK
serves the target, or the SDK came from other engine sources or another configuration, run the
`sdk build` command it prints and repeat. `--engine-config Debug` is only for debugging the engine.

## Create the intended kind

```text
haylen new /path/to/my-app --kind lua --name "My App" --identifier com.example.myapp --orientation any
haylen new /path/to/my-native-app --kind cpp --name "My Native App" --identifier com.example.mynativeapp
```

The folder must be absent or empty. The tool layers `templates/common` and then `templates/lua` or
`templates/cpp`. It writes `haylen.json`, `content/logo.png`, the starter code, bridge handlers under
`native/apple`, `native/android` and `native/web`, and the app's `.gitignore`, `.editorconfig` and
`.clang-format`. Defaults are kind `lua`, a name from the folder, identifier `com.example.<folder>`
and orientation `landscape`, so set `any` or `portrait` deliberately for an application.

| Kind | Source ownership |
| --- | --- |
| Lua | `source/main.lua` plus the package. The default target is `player`. |
| C++ | `"kind": "cpp"` with a `cpp` section naming `sources`, `includeDirectories` and `definitions`, starting from `src/App.cpp`. No CMake project. The default target is this machine's `macos`, `windows` or `linux`. |

Keep `haylen.json`, `haylen.lock`, source/content, `native/`, plugin copies and files named by
`platforms` under version control. The generated `.gitignore` excludes `build/`, `dist/` and
`platform/android/keystore/`. Each build generates its native project under
`build/apps/<app>-<hash>/<product>/project/`. It is deterministic and disposable. Never edit it.

## Customize generated projects through haylen.json

Every change to a generated project is a `platforms` key or a file of the app that such a key names.

| Section | Keys |
| --- | --- |
| `apple` | `sources` (bridge and native folders), `team`, `buildSettings`, `privacy`. |
| `ios`, `catalyst`, `tvos`, `visionos`, `macos` | `infoPlist`, `entitlements`. |
| `android` | `sources`, `applicationClass`, `manifest` with `permissions`, `removedPermissions` and `applicationAttributes`. |
| `web` | `scripts`, loaded after the loader. |
| Every section | `minimumSystemVersion` in the platform's own section, and `files` mapping a generated-project path to an app file or folder. |

Plist, entitlement and privacy keys merge with plugin contributions. Two owners that give one key
different values stop resolution with both named, so a usage description that a plugin takes as a
parameter belongs in that plugin's `parameters`, not in `infoPlist`. Apple `files` may replace only
paths the template holds, such as `Assets.xcassets` or `LaunchScreen.storyboard`. Run
`haylen project inspect <app> --target <target>` to see each resolved value with its origin before
building. The app sets name, identifier, `version`, `build` and orientation only in `haylen.json`.

## Understand build, verify and package evidence

```text
haylen devices
haylen app run /path/to/my-app
haylen app run /path/to/my-app --target ios-simulator --device "ACTUAL_DEVICE_ID"
haylen app run /path/to/my-app --target android --device ACTUAL_DEVICE_SERIAL
haylen app run /path/to/my-app --target web --open
haylen app build /path/to/my-app --target android --config Release
haylen app verify /path/to/my-app --target android --config Release
haylen app prepare /path/to/my-app --target ios --config Release
haylen app package /path/to/my-app --target android --format bundle
haylen app zip /path/to/my-app -o /path/to/my-app.zip
```

| Operation | What it establishes | What remains separate |
| --- | --- | --- |
| `app run` with no target | Desktop player development run of a Lua package with hot reload. | Native app integration and mobile hardware. |
| `app run --target ...` | Prepare, build, verify, then launch and stream the log until `q`. | Successful interaction, signing/archive or store approval. |
| `app build` | Prepare, build with native tools and verify the product, without launching. | Any runtime or visual QA claim. |
| `app prepare` | Generated native project, plus the protected release in Release. The Apple App Store archive is made in Xcode from this project. | A completed final host build, archive or runtime test. |
| `app verify` | Re-examines the **last build** for files, architectures, platform/plugin needs and forbidden release content. Exit code 1 on failure. | Compiling a new build or exercising SDK/form/navigation behavior. |
| `app package --format ...` | Release `installer` (Windows/Linux), `steam`, Android `bundle` or device `apks` in `dist/` or `-o`. | Store upload, review or publication. |
| `app zip` | Development package zip with `haylen.json`, `source/`, `content/` and plugin Lua/manifests. | Signed app, protected release or store artifact. |

Use the matching target/configuration throughout. Release ships only the protected release with the
app bootstrap, and verification fails on Lua sources, unprotected package files, symbols or keys in
the product. `app sign --target android` creates the upload key in `platform/android/keystore/`.
Raise `build` in `haylen.json` above every number a store already received before each upload.

Run targets are `player`, `macos`, `catalyst`, `ios`/`ios-simulator`, `tvos`/`tvos-simulator`,
`visionos`/`visionos-simulator`, `android`, `web`, `windows` and `linux`, each buildable only on its
documented host. Do not infer watchOS or hardware capabilities from that list. Keep development
servers on loopback unless a device on the local network needs them, and never in release.

For release, inspect protected content packaging and signing from the current guide. Build the
intended artifact, then verify its actual contents and target. Never ship private signing material,
engine source, logs or debug access accidentally. Record the output path reported by the tool.

## Upgrade an app from the earlier layout

An app with `app.json`, `platform/<template>/` projects, a CMake C++ app or an old-shape
`plugin.json` uses the earlier layout. The current tooling refuses those files, so move each piece
once, following the upstream upgrading guide:

1. Record current and target engine revisions, app kind, plugins, targets and toolchain. Commit or
   set aside existing changes so the upgrade is one reviewable diff. Do not create branches or
   rewrite history unless the target project's authorized workflow calls for them.
2. Update the engine checkout, build the SDKs of the shipped targets and run `haylen doctor`.
3. Make scratch references with `haylen new` using the same kind, name, identifier and orientation,
   and `haylen plugin new` for each plugin ID. Delete them at the end.
4. Rename `app.json` to `haylen.json`. Runtime keys keep their names. Move plugin values under
   `parameters`. Add `kind`/`cpp` for a C++ app. Set `build` above the last store build number.
5. For each `platform/<template>/` difference, drop parts of the old template and values that
   `haylen.json` already owns, and move each developer choice into a `platforms` key, a file named
   by `files`, or a plugin contribution. Move bridge sources to `native/<platform>/`. Then delete the
   folder, keeping only `platform/android/keystore/`.
6. Convert each `plugin.json` key by key to `interface`, `implementations`, `dependencies` and typed
   `contributions`, keeping every parameter and default. Pin git plugins with `haylen plugin update`.
7. Map old commands: `run` → `app run`, `--platform` → `--target`, `--build-only` → `app build`,
   `prepare` → `app prepare`, `check` → `app verify`, `package` → `app zip`. `platform diff`,
   `platform add` and `platform xcodegen` have no replacement because every build generates its
   project, and `project inspect` shows what that project receives.
8. Run `project inspect`, then build and verify every shipped target in Debug and Release. Treat each
   error as the list of remaining work, fixed where its sentence points. Run each plugin feature on
   the real targets. Report every moved developer choice and its new location.

## Upgrade to a later engine revision

Compare the app with a fresh `haylen new` reference from the **target revision** and with the
backend templates under `tools/haylen/platforms/<backend>/template/`. Copy a template file into the
app and name it in `files` only to change it deliberately. When that template file changes
upstream, merge the upstream change into the app's copy and keep the intended edits. Update changed API contracts to their
final form without a legacy compatibility layer. Rebuild SDKs, then build, verify and run each target.
A previous build's successful `app verify` is not proof of the new source.

## Upgrade a plugin without overwriting its implementation

Separate a maintained plugin source (folder or repository) from an installed copy at
`plugins/<id>/`. Determine which is authoritative before editing. `plugin add` replaces an earlier
copy without merging local modifications. `plugin add --reference` lists the folder or repository
instead, deleting an earlier copy and pinning a repository in `haylen.lock`.

```text
haylen plugin new /path/to/upgrade-reference/device-kit
haylen plugin list --app /path/to/my-app
haylen plugin update device-kit --app /path/to/my-app
```

The reference folder's basename is the default ID, so name it after the plugin ID. Compare
`plugin.json`, public Lua API, Apple/Android/web/native source, `build.gradle.kts` versions and the
`.gitignore`/`.editorconfig`/`.clang-format` against that reference and the plugin guide. Keep real
SDK integration and configuration. Do not copy placeholder echo logic over production handlers.
Update public methods/results and all app callers together if their contract changes.

`plugin update <id>` pins the commit that a referenced git plugin's branch or tag names now. A
Release build refuses an unpinned git plugin. Read back `haylen.json`, `haylen.lock` and the installed
files to confirm values, including newly required parameters that `plugin add` lists as empty text.
Build and verify fresh hosts for claimed targets and exercise registration, repeated calls,
permission denial, cancellation, activity/window recreation and Release packaging.

## Final-artifact parity

Preparation, final native build, last-build verification and protected-content verification are
separate checks. The `build` and `version` of `haylen.json` feed every platform's build number.
Verify the actual IPA/AAB metadata and the protected release embedded in that artifact, not only a
prepared folder. See [debugging and release evidence](debugging-and-release-evidence.md#verify-both-preparation-and-the-final-shipped-content)
for `haylen content verify <app> --target <target> --release <extracted-folder>`.
