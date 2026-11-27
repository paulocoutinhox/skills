# Project creation, builds and upgrades

Use the command reference, distribution guide, templates and backend templates in
[sources](sources.md). Work against one chosen engine revision. A newer template is something to
compare against on purpose. It does not give you the right to overwrite unrelated developer changes.

## Prepare the machine and SDKs

```text
haylen doctor
haylen sdk build --target player
haylen sdk build --target ios --target ios-simulator
haylen sdk build --target android
haylen sdk list
```

The launcher needs only uv, which brings the tooling's Python. SDK builds need CMake 3.28+, Ninja
and a C++20 compiler, plus Xcode or the Android SDK for those targets. `doctor` reports tools, SDKs
and what is missing for each target without downloading anything. `sdk build` installs into
`build/sdk/<port>-<configuration>/`. You can build targets of one port together, and building
another target later adds its slice. An app command never compiles the engine. When it stops
because no SDK serves the target, or because the SDK came from other engine sources or another
configuration, run the `sdk build` command it prints and repeat. `--engine-config Debug` is only for
debugging the engine.

## Create the kind you want

```text
haylen new /path/to/my-app --kind lua --name "My App" --identifier com.example.myapp --orientation any
haylen new /path/to/my-native-app --kind cpp --name "My Native App" --identifier com.example.mynativeapp --orientation any
```

The folder must not exist or must be empty. The tool lays down `templates/common` and then
`templates/lua` or `templates/cpp`. It writes `haylen.json`, `content/logo.png`, the starter code,
bridge handlers under `native/apple`, `native/android` and `native/web`, and the app's `.gitignore`,
`.editorconfig` and `.clang-format`. The defaults are kind `lua`, a name from the folder, identifier
`com.example.<folder>` and orientation `landscape`, so set `any` or `portrait` on purpose for an app.

| Kind | Who owns the source |
| --- | --- |
| Lua | `source/main.lua` plus the package. The default target is `player`. |
| C++ | `"kind": "cpp"` with a `cpp` section naming `sources`, `includeDirectories` and `definitions`, starting from `src/App.cpp`. No CMake project. The default target is this machine's `macos`, `windows` or `linux`. |

Keep `haylen.json`, `haylen.lock`, source/content, `native/`, plugin copies and files named by
`platforms` under version control. The generated `.gitignore` excludes `build/`, `dist/` and
`platform/android/keystore/`. Each build generates its native project under
`build/apps/<app>-<hash>/<product>/project/`. It comes out the same every time and you can throw it
away. Never edit it.

## Customize generated projects through haylen.json

Every change to a generated project is a `platforms` key or an app file that such a key names.

| Section | Keys |
| --- | --- |
| `apple` | `sources` (bridge and native folders), `team`, `buildSettings`, `privacy`. |
| `ios`, `catalyst`, `tvos`, `visionos`, `macos` | `infoPlist`, `entitlements`. |
| `android` | `sources`, `applicationClass`, `manifest` with `permissions`, `removedPermissions` and `applicationAttributes`. |
| `web` | `scripts`, loaded after the loader. |
| Every section | `minimumSystemVersion` in the platform's own section, and `files` mapping a generated-project path to an app file or folder. |

Plist, entitlement and privacy keys merge with plugin contributions. If two owners give one key
different values, resolution stops and names both. So a usage description that a plugin takes as a
parameter belongs in that plugin's `parameters`, not in `infoPlist`. Apple `files` may replace only
paths the template holds, such as `Assets.xcassets` or `LaunchScreen.storyboard`. Run
`haylen project inspect <app> --target <target>` to see each final value and where it came from
before you build. The app sets name, identifier, `version`, `build` and orientation only in
`haylen.json`.

## Understand what build, verify and package prove

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

| Operation | What it proves | What stays separate |
| --- | --- | --- |
| `app run` with no target | Desktop player development run of a Lua package with hot reload. | Native app integration and mobile hardware. |
| `app run --target ...` | Prepare, build, verify, then launch and stream the log until `q`. | Successful interaction, signing/archive or store approval. |
| `app build` | Prepare, build with native tools and verify the product, without launching. | Any runtime or visual QA claim. |
| `app prepare` | Generated native project, plus the protected release in Release. The Apple App Store archive is made in Xcode from this project. | A finished final host build, archive or runtime test. |
| `app verify` | Checks the **last build** again for files, architectures, platform/plugin needs and forbidden release content. Exit code 1 on failure. | Compiling a new build or trying SDK/form/navigation behavior. |
| `app package --format ...` | Release `installer` (Windows/Linux), `steam`, Android `bundle` or device `apks` in `dist/` or `-o`. | Store upload, review or publishing. |
| `app zip` | Development package zip with `haylen.json`, `source/`, `content/` and plugin Lua/manifests. | Signed app, protected release or store package. |

Use the matching target/configuration the whole way. Release ships only the protected release with
the app bootstrap, and verification fails on Lua sources, unprotected package files, symbols or keys
in the product. `app sign --target android` creates the upload key in `platform/android/keystore/`.
Before each upload, raise `build` in `haylen.json` above every number a store already received.

Run targets are `player`, `macos`, `catalyst`, `ios`/`ios-simulator`, `tvos`/`tvos-simulator`,
`visionos`/`visionos-simulator`, `android`, `web`, `windows` and `linux`. Each one builds only on its
documented host. Do not guess watchOS or hardware support from that list. Keep development servers
on loopback unless a device on the local network needs them, and never in release.

For release, check protected content packaging and signing in the current guide. Build the package
you intend to ship, then check its real contents and target. Never ship private signing material,
engine source, logs or debug access by mistake. Record the output path the tool reports.

## Upgrade to a later engine revision

Compare the app with a fresh `haylen new` reference from the **target revision** and with the
backend templates under `tools/haylen/platforms/<backend>/template/`. Copy a template file into the
app and name it in `files` only when you mean to change it. When that template file changes
upstream, merge the upstream change into the app's copy and keep the edits you meant to make.
Update changed API contracts to their final form. Rebuild SDKs, then build, verify and run each
target. A successful `app verify` from an earlier build does not prove the new source.

## Upgrade a plugin without overwriting its implementation

Keep a maintained plugin source (folder or repository) apart from an installed copy at
`plugins/<id>/`. Decide which one is the source of truth before you edit. `plugin add` replaces an
earlier copy without merging local changes. `plugin add --reference` lists the folder or repository
instead, deletes an earlier copy and pins a repository in `haylen.lock`.

```text
haylen plugin new /path/to/upgrade-reference/device-kit
haylen plugin list --app /path/to/my-app
haylen plugin update device-kit --app /path/to/my-app
```

The reference folder's basename is the default ID, so name it after the plugin ID. Compare
`plugin.json`, the public Lua API, Apple/Android/web/native source, `build.gradle.kts` versions and
the `.gitignore`/`.editorconfig`/`.clang-format` against that reference and the plugin guide. Keep
the real SDK integration and configuration. Do not copy placeholder echo logic over production
handlers. If the contract of public methods/results changes, update them and all app callers
together.

`plugin update <id>` pins the commit that a referenced git plugin's branch or tag names now. A
Release build refuses an unpinned git plugin. Read back `haylen.json`, `haylen.lock` and the
installed files to confirm values, including newly required parameters that `plugin add` lists as
empty text. Build and verify fresh hosts for the targets you claim, and try registration, repeated
calls, permission denial, cancel, activity/window recreation and Release packaging.

## Final-artifact parity

Preparation, final native build, last-build verification and protected-content verification are
separate checks. The `build` and `version` of `haylen.json` feed every platform's build number.
Check the real IPA/AAB metadata and the protected release inside that package, not only a prepared
folder. See [debugging and release evidence](debugging-and-release-evidence.md#verify-both-preparation-and-the-final-shipped-content)
for `haylen content verify <app> --target <target> --release <extracted-folder>`.
