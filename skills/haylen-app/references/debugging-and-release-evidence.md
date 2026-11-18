# Debug sessions and evidence for native releases

Read this when investigating a running Haylen app, automating a development journey or proving which
content reached the final native artifact. Inspected against engine revision
`c8061996311d301dd5dc9b90e93a1113bf04f247`. Recheck the actual app's engine revision before acting.

## Start the development session that owns the debugger

The Lua debugger belongs to Haylen's development session. The app must be launched by
`haylen app run` in the Debug configuration, which passes the development-server arguments, not
merely installed or started with `simctl launch`/ADB. The engine SDK configuration
(`--engine-config`, `Release` by default) is separate from the app's Debug/Release configuration. A
Release app, a shipped app and a protected release have no debugger.

```text
haylen devices
haylen app run "$APP_PATH" --target ios-simulator --device "$SIMULATOR_ID" --config Debug --debugger-port 4712
```

Use a real listed destination and an available selected port. Retain the run process/session and
read the debugger port printed in the run summary. The documented default is 4711, but do not
assume it when multiple runs exist. `app build` cannot establish a live debugger. The run reaches
simulators, emulators, devices on the local network and web pages through its own connection, so
no manual port forwarding is needed.
Do not expose the development server publicly or publish its connection tokens/URLs in reports.

Attach a DAP client to `127.0.0.1` and that port with the `attach` request and no program to launch.
If an explicitly requested diagnostic requires protocol-level interaction, follow DAP framing and the
adapter's capabilities:

1. Send `initialize` and inspect the response and asynchronous events.
2. Send `attach` for the already launched app. Handle `initialized`, any supported configuration
   requests and `configurationDone` in the adapter's actual sequence.
3. Use bounded requests with sequence/request correlation. A response may be interleaved with events.
   Do not treat a TCP line or first packet as a complete framed JSON message.
4. Evaluate only the intended diagnostic expression. Record the result and actual observed app state.
5. Disconnect without terminating the debuggee when preserving the session is intended. Stop the
   owned development run after the investigation and invalidate its temporary server access.

A raw DAP `evaluate` is execution inside the development app, not a read-only inspection API. Scope
mutations to the authorized test data. It does not authorize a real purchase, customer-data mutation,
credential extraction or a production entitlement grant.

## Inspect the active scene and respect evaluation limits

The documented debugger evaluates expressions on a separate coroutine, with a one-second limit in
the inspected revision. Awaiting long asynchronous work inside an evaluation is not a way to run the app's event loop while
it is halted. Resume the app and schedule legitimate asynchronous work through its normal owned
lifecycle, then observe completion. Use public service/screen APIs rather than writing private state.

Inspect the top scene with `scene.top()` or the current stack semantics of
`scene.at(scene.size())`. `scene.list()[1]` is the bottom scene. A covered scene's `update` is not
called, and unloading cancels owned tasks/listeners. Do not bind an action to a stale home scene or
wait forever for its covered update callback. Owned work does not universally stop just because a
scene is covered. Diagnose the specific callback/task and owner lifetime instead.

A small diagnostic that reads the current Lua scene identity is:

```lua
local scene = require('haylen.scene')
local top = scene.top()
return type(top) == 'table' and top.name or nil
```

A C++-owned or absent top scene may not supply a Lua table. Do not fabricate an owner. In an app built
on the navigation, the top scene is usually the shell scene, and the visible page is the top screen
of its stack or selected tab. Check a screen with `ui.screenState(screen)` before acting on it, and
wait for `appeared` or completed scene changes before using new UI. The debugger can help navigate
real content. It cannot prove native SDK button hit targets or completed transactions.
Use supported native UI tests and genuine screenshots for those boundaries. Keep any explicit developer
content mode clearly separate from real subscription/customer information.

## Verify both preparation and the final shipped content

Inspect tool-reported paths, `haylen.json`/plugin parameters, app `native/` sources and the generated
project separately. `version` and `build` in `haylen.json` are the only source of platform version and
build numbers, so do not override them in a native project or CI script. Re-prepare/build after final
source changes and inspect version/build in the actual IPA/AAB. Do not introduce a publisher wrapper or store YAML
just to run native release commands when the app's chosen workflow excludes that tooling.

Keep these checks separate:

| Check | Establishes | Does not establish |
| --- | --- | --- |
| `haylen app verify` on the built target/configuration | Product files, architectures, engine/plugin needs and forbidden release content of the last build | Final file parity, UI correctness or store approval |
| Protected-content verification | Manifest/shard signatures, digests and authenticated file reads | Correct entitlement or store-backed purchase |
| Comparison with intended final source/prepared release | Whether the tested artifact embeds the intended content/configuration | Runtime correctness on every device |
| Reinstall/restart of that artifact | The process actually runs the selected final binary | A transaction or hardware feature that was not exercised |

For protected content extracted from the real signed artifact, discover the release folder that
holds the two manifests and their shards. Preserve its files unchanged, then use the actual source
app and target with the documented CLI syntax:

```text
haylen content verify "$APP_PATH" --target ios --release "$EXTRACTED_RELEASE_DIRECTORY"
```

The positional path is the source app, which supplies the keys, and `--release` selects the
extracted protected folder. Without `--release` the command checks the last release built for that
target's content profile. It authenticates every manifest, shard and chunk. Passing
the IPA or `.app` as though it were the source app is not equivalent. Verification needs the app's
approved content keys. Keep them in their original key store. Do not demand plaintext Lua/plugin JSON
inside a protected Apple binary to claim its configuration is present. Inspect through the supported
content tooling or compare authenticated release outputs. Record the scope actually verified.

## Stop, retain and report

Stop only owned development servers, test devices and temporary runners. Keep final screenshots,
signed artifacts, hashes and matching symbols needed for release support. Remove scratch captures,
private connection logs, test adapters and temporary fixtures from the app repository. Do not delete
original credentials or global caches. Deliver exact commands/configuration, source/engine revision,
artifact paths, checks, native UI evidence and unexecuted integrations as separate facts.
