# Debug sessions and evidence for native releases

Read this when you look into a running Haylen app, automate a development journey or prove which
content reached the final native package. Checked against engine revision
`c8061996311d301dd5dc9b90e93a1113bf04f247`. Check the real app's engine revision again before you
act.

## Start the development session that owns the debugger

The Lua debugger belongs to Haylen's development session. The app must be launched by
`haylen app run` in the Debug configuration, which passes the development-server arguments. Just
installing it or starting it with `simctl launch`/ADB is not enough. The engine SDK configuration
(`--engine-config`, `Release` by default) is separate from the app's Debug/Release configuration. A
Release app, a shipped app and a protected release have no debugger.

```text
haylen devices
haylen app run "$APP_PATH" --target ios-simulator --device "$SIMULATOR_ID" --config Debug --debugger-port 4712
```

Use a real listed destination and a free port you chose. Keep the run process/session and read the
debugger port printed in the run summary. The documented default is 4711, but do not assume it when
several runs exist. `app build` cannot give you a live debugger. The run reaches simulators,
emulators, devices on the local network and web pages through its own connection, so you do not
need to forward ports by hand. Do not expose the development server publicly or publish its
connection tokens/URLs in reports.

Attach a DAP client to `127.0.0.1` and that port with the `attach` request and no program to launch.
If a diagnostic the user explicitly asked for needs protocol-level interaction, follow DAP framing
and the adapter's capabilities:

1. Send `initialize` and read the response and the events that arrive on their own.
2. Send `attach` for the app that is already running. Handle `initialized`, any supported
   configuration requests and `configurationDone` in the adapter's real order.
3. Use requests with limits, and match each response to its request by sequence number. A response
   may arrive mixed in with events. Do not treat a TCP line or first packet as a complete framed
   JSON message.
4. Evaluate only the diagnostic expression you mean to run. Record the result and the app state you
   really saw.
5. When you want to keep the session, disconnect without ending the debuggee. Stop the development
   run you own after the investigation and cancel its temporary server access.

A raw DAP `evaluate` runs code inside the development app. It is not a read-only inspection API.
Limit changes to the test data you are allowed to use. It does not allow a real purchase, changing
customer data, pulling out credentials or granting a production entitlement.

## Inspect the active scene and respect evaluation limits

The documented debugger evaluates expressions on a separate coroutine, with a one-second limit in
the checked revision. Awaiting long async work inside an evaluation does not run the app's event
loop while it is halted. Resume the app and schedule real async work through its normal owned
lifecycle, then watch it finish. Use public service/screen APIs instead of writing private state.

Inspect the top scene with `scene.top()` or the current stack meaning of
`scene.at(scene.size())`. `scene.list()[1]` is the bottom scene. A covered scene's `update` is not
called, and unloading cancels owned tasks/listeners. Do not bind an action to an old home scene or
wait forever for its covered update callback. Owned work does not always stop just because a scene
is covered. Look at the specific callback/task and how long its owner lives instead.

A small diagnostic that reads the current Lua scene identity is:

```lua
local scene = require('haylen.scene')
local top = scene.top()
return type(top) == 'table' and top.name or nil
```

A top scene owned by C++, or no top scene, may not give a Lua table. Do not make up an owner. In an
app built on the navigation, the top scene is usually the shell scene, and the visible page is the
top screen of its stack or selected tab. Check a screen with `ui.screenState(screen)` before you act
on it, and wait for `appeared` or for scene changes to finish before you use new UI. The debugger
can help you move through real content. It cannot prove native SDK button hit targets or finished
transactions. Use supported native UI tests and real screenshots for those limits. Keep any explicit
developer content mode clearly apart from real subscription/customer information.

## Verify both preparation and the final shipped content

Check tool-reported paths, `haylen.json`/plugin parameters, app `native/` sources and the generated
project separately. `version` and `build` in `haylen.json` are the only source of platform version
and build numbers, so do not override them in a native project or CI script. Prepare/build again
after the final source changes and check version/build in the real IPA/AAB. Do not add a publisher
wrapper or store YAML just to run native release commands when the app's chosen workflow leaves that
tooling out.

Keep these checks separate:

| Check | Proves | Does not prove |
| --- | --- | --- |
| `haylen app verify` on the built target/configuration | Product files, architectures, engine/plugin needs and forbidden release content of the last build | That final files match, UI correctness or store approval |
| Protected-content verification | Manifest/shard signatures, digests and authenticated file reads | Correct entitlement or store-backed purchase |
| Comparison with intended final source/prepared release | Whether the tested package holds the intended content/configuration | Runtime correctness on every device |
| Reinstall/restart of that package | The process really runs the chosen final binary | A transaction or hardware feature that was not tried |

For protected content pulled out of the real signed package, find the release folder that holds the
two manifests and their shards. Keep its files unchanged, then use the real source app and target
with the documented CLI syntax:

```text
haylen content verify "$APP_PATH" --target ios --release "$EXTRACTED_RELEASE_DIRECTORY"
```

The positional path is the source app, which supplies the keys, and `--release` picks the extracted
protected folder. Without `--release` the command checks the last release built for that target's
content profile. It authenticates every manifest, shard and chunk. Passing the IPA or `.app` as if
it were the source app does not do the same thing. Verification needs the app's approved content
keys. Keep them in their original key store. Do not demand plain-text Lua/plugin JSON inside a
protected Apple binary to claim its configuration is there. Check through the supported content
tooling or compare authenticated release outputs. Record what you really checked.

## Stop, keep and report

Stop only the development servers, test devices and temporary runners you own. Keep final
screenshots, signed packages, hashes and matching symbols needed for release support. Remove scratch
captures, private connection logs, test adapters and temporary fixtures from the app repository. Do
not delete original credentials or global caches. Deliver the exact commands/configuration,
source/engine revision, package paths, checks, native UI evidence and integrations that were not run
as separate facts.
