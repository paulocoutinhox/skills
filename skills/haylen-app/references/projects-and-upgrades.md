# Project creation, builds and template upgrades

Use the actual layered templates, distribution/upgrading guides and CLI implementation in
[sources](sources.md). Work against one chosen engine revision. A current template is a reference
to merge deliberately, not authority to overwrite unrelated developer changes.

## Create the intended kind

```text
haylen new /path/to/my-app --kind lua --name "My App" --identifier com.example.myapp --orientation any
haylen new /path/to/my-native-app --kind cpp --name "My Native App" --identifier com.example.mynativeapp
```

The tool requires an absent/empty destination and layers `templates/common` before `templates/lua`
or `templates/cpp`. Kind-specific files override common ones. It sets the chosen identity,
orientation and window title in app.json. Landscape is the default orientation, so set `any` or
portrait deliberately for an application. Inspect the current schema before changing design/UI.

| Kind | Generated source/project ownership |
| --- | --- |
| Lua | Package plus developer-owned `platform/apple`, `android`, `web`, `windows` and `linux`. The tool integrates engine artifacts into these hosts. |
| C++ | Package plus root CMake/native app source, with `platform/android` and `platform/web`. CMake builds the other supported targets. Use actual `haylen_add_app` and embedding contracts. |

Keep app.json, source/content, plugin source and developer-owned platform projects under version
control. Ignore output, engine caches, private signing files and IDE user state. Generated native
`haylen/` folders contain integration/includes, not a place to maintain custom source. The tool can
use a cached template host if no owned platform project exists. Do not add one merely to change
generated configuration that already belongs in app.json/plugin.json.

```text
haylen platform add /path/to/my-app android
haylen platform diff /path/to/my-app android
haylen platform xcodegen /path/to/my-app
```

`platform add` creates an owned host from the layered template and refuses an existing one.
It also rejects a template unavailable for that kind, such as Apple for the C++ kind. A normal new
Lua project already has its platform projects. `platform diff` prints read-only file/unified diffs,
excluding generated integration, build products and per-user Xcode state. It does not apply them.
`platform xcodegen <app>` regenerates that app's Apple project from its project.yml. The
`--template` operation instead modifies the engine template and is not a consumer upgrade step.

## Understand build, prepare, check and package evidence

```text
haylen devices
haylen run /path/to/my-app
haylen run /path/to/my-app --platform ios-simulator --device "ACTUAL_DEVICE_NAME"
haylen run /path/to/my-app --platform android --device ACTUAL_DEVICE_SERIAL
haylen run /path/to/my-app --platform web --open
haylen run /path/to/my-app --platform android --config Release --build-only
haylen check /path/to/my-app --platform android --config Release
haylen prepare /path/to/my-app --platform ios --config Release
haylen package /path/to/my-app -o /path/to/my-app.zip
```

| Operation | What it establishes | What remains separate |
| --- | --- | --- |
| `run` with no platform | Desktop player development run of the package. | Actual native app integration and mobile hardware. |
| `run --platform ...` | Build for the destination and launch when requested/possible. | Successful interaction, signing/archive or store approval. |
| `run --build-only` | Build and tool diagnostics without launching a device/server. | Any runtime or visual QA claim. |
| `prepare --platform ...` | Build needed engine artifacts and generate integration for the native IDE/project. For web, prepare the site. | A completed final host build, archive or runtime test. |
| `check --platform ...` | Inspect the **last build** for engine/plugin requirements. Nonzero on a missing requirement. | Compiling a new build or exercising actual SDK/form/navigation behavior. |
| `package ... -o ...` | Package with app.json at its archive root and the supported source/content/plugin subset. | Signed app, Android App Bundle, store upload, review or publication. |

Use the matching platform/configuration throughout. Ordinary `run` checks can report warnings,
where an explicit `check` gives the required failure status. Release has additional protections
and rejects prohibited release content. Apple checking inspects built declarations/linkage/signing
and privacy data. Android checks the merged APK manifest/native libraries. Web checks prepared
configuration/plugin modules, including opener-policy conflicts when requested. Desktop checks
installed outputs/native libraries. These checks cannot validate truthful legal/privacy answers.

Actual run targets include macOS, Catalyst, iOS/iOS Simulator, tvOS/tvOS Simulator,
visionOS/visionOS Simulator, Android, web, Windows and Linux as documented for the revision/host.
Do not infer watchOS or hardware capabilities from that list. Resolve simulator/device IDs with
`devices`. Debug device/server reachability is a deliberate network choice. Keep development
services off public networks and out of release configurations.

For release, inspect protected source/content packaging and required bootstrap/signing from the
current guide. Build the intended archive/artifact, then verify its actual contents and target.
Never ship private signing material, full engine source, logs or debug endpoint access accidentally.
Record the output path reported by the tool instead of inventing a universal artifact filename.

## Upgrade projects through an explicit merge

1. Record current and target engine revisions, app kind, owned platform projects, plugin versions,
   supported targets and toolchain. Inspect worktree changes. Keep developer changes intact and
   scope this operation to the requested repository. Do not create branches or rewrite history
   unless the target project's authorized workflow calls for them.
2. Read current README/features, release notes where available, upgrading guide and templates.
   Distinguish template integration changes from business changes. Identify changed API/toolchain
   contracts and update to their final supported form without a legacy compatibility layer.
3. Generate an isolated reference app from the **target revision**, in a new empty scratch folder,
   matching kind, identifier, name and orientation. It is not a replacement app or live-data copy.
   Compare its root/configuration/native startup files as well as platform projects.
4. Run `platform diff <app> <template>` for each owned template available to that kind. Treat changes
   as template-only, developer-only or conflicting. Adopt needed integration changes, retain intended
   customization and resolve real conflicts explicitly. Never copy a whole fresh platform folder
   over signing/flavors/icons/resources/custom source just because its template is newer.
5. Apply the per-platform source changes below. Update app.json/plugin.json for generated settings.
   Remove obsolete integration and callers together. Do not maintain duplicate old/new bootstrap
   paths or edit generated output to hide a missing declaration.
6. Update plugins by the separate procedure below. Re-run preparation/build so generated `haylen/`
   reflects the selected engine and plugin graph. Regenerate Xcode from source when needed.
7. Build and check each supported requested configuration, then actually run its relevant workflows.
   A previous build's successful `check` is not proof of the new source. Resolve real compiler,
   manifest, permission, linkage, lifecycle and runtime failures at their source.
8. Inspect final diffs, artifact contents, UI/navigation/data preservation and release behavior.
   Update present-state AGENTS.md with engine/tool ownership and exact reproducible commands.
   Report unexecuted hardware/SDK/signing tasks explicitly. Do not delete arbitrary user caches or
   clear real app data just to make a test pass.

## Platform-specific merge rules

| Source | Deliberate upgrade procedure |
| --- | --- |
| Apple | Merge `platform/apple/project.yml`, xcconfig, bootstrap and bridging-source changes. Preserve own targets/signing/capabilities/icons/resources and usage strings. Include current generated `haylen/project.yml` target templates and Haylen xcconfig as prescribed. Regenerate App.xcodeproj with `platform xcodegen`. Reconcile manual project-file edits into the source definition rather than losing them. Do not maintain pbxproj as the primary integration source. |
| Android | Compare settings/root/app Gradle files, wrapper/version/checksum pins, bootstrap Activity/application, manifests, resources and plugin-library registration. Preserve deliberate flavors, signing, repositories and restrictions. Read actual merged manifest and required copied files. Do not re-add a deliberately removed permission without a product decision. |
| Web | Compare index.html, loader.js, loader.css and app.js with the current template. Preserve branding and app-owned behavior, following the template's app.js extension boundary. Update runtime/worker/module integration together and verify headers, module registration, browser permission/gesture and native-screen popup behavior. |
| Windows/Linux Lua host | Compare CMake/source/bootstrap/resource integration, including the generated `haylen/haylen.cmake` and current host helper. Preserve actual native dependencies and installer/signing resources. Follow the Lua host's helper, not the C++ consumer helper by assumption. |
| Root C++ consumer | Compare CMake engine acquisition/package wiring, `haylen_add_app`, application/bridge sources and public headers. Update to the target API without retaining obsolete include/link glue. Preserve real application C++ responsibilities and platform-specific ownership. |

## Upgrade a plugin without overwriting its implementation

There is no documented general plugin upgrade subcommand. Separate a maintained plugin source
repository from the installed copy at `app/plugins/<id>`. Determine which is authoritative before
editing. `plugin add` is a copy/replacement operation, not a merge of local modifications.

```text
haylen plugin new /path/to/upgrade-reference/device-kit --id device-kit --with camera,microphone
haylen plugin list --app /path/to/my-app
```

The reference folder **must end in `device-kit`**, matching the ID. A differently named scratch
folder with `--id device-kit` fails the current CLI's validation. Choose the plugin's actual feature
set for comparison. A bare echo scaffold alone does not show camera/microphone feature changes.

Compare plugin.json, public Lua API, Apple/Android/web/native source, build files and README against
that fresh reference and the target native guide. Merge changes to contexts/protocols, permissions,
dependencies, native-screen lifecycle and stream/buffer ownership. Keep real SDK integration and
configuration intact. Do not copy placeholder echo/sample logic over production handlers.
Update public methods/results and all app callers together if their final contract changes.

Validate parameter types/defaults, dependencies, platform declarations and source/file paths.
Merge plugin source changes in its maintained location, then deliberately install the reviewed copy
or pinned repository revision. Read back app.json and the installed files to confirm correct values,
including any newly required parameters. If local installed modifications existed, reconcile them
before replacement. Do not silently discard them or invent a fallback implementation.

Build/check fresh hosts for claimed targets and exercise actual native method registration, repeated
calls, permission denial, cancellation, activity/window recreation and release packaging. Preserve
account/user data through the defined upgrade path. Record native/provider/version limitations.
Do not claim universal SDK functionality from a successful echo call or static manifest validation.

## Final-artifact parity

Preparation, final native build, last-build inspection and protected-content verification are separate
checks. Native version-number command overrides must be consumed by the real project. Verify the
actual IPA/AAB metadata and the protected release embedded in that artifact, not only a prepared
folder. See [debugging and release evidence](debugging-and-release-evidence.md#verify-both-preparation-and-the-final-shipped-content)
for the inspected `content verify <source-app> --platform ... --release <extracted-folder>` contract.
Do not add publishing YAML/helpers or ZIP packaging when excluded by the requested app workflow.
