# Haylen prompts

Haylen apps, games, plugins and engine upgrades. Read [how to use the prompts](../task-prompts.md)
before you copy one.

## Haylen application

```text
Use haylen-app from paulocoutinhox/skills.
Read [SKILLS_ROOT]/haylen-app/SKILL.md and name the path really loaded. If it is missing, say so.

Create [APPLICATION] in [REPOSITORY] for [PLATFORMS] using [ENGINE_REVISION_AND_LUA_CPP_SCOPE].
Read the current README/features, the matching samples/apps code and the linked guides on app
structure, scenes, UI, lifecycle and distribution. Use one frame GUI for bars and routes, ui.Screen
pages in navigation stacks, tabs and splits, and focused domain and service modules. Define
list/detail navigation, forms, draft and query state, routes and restore. Do not build a normal app
as a simulated game world.
Use physical responsive UI where it fits, stable widget and item IDs, native text input, accessible
focus, clear loading, error and submit states, and work owned by the lifecycle. Handle delayed
navigation, double taps and old async responses on purpose. Put source, content, plugins and the
haylen.json platform settings in the right places. Build and verify the real requested targets, and
test navigation, forms, resize, failure and background/resume. Deliver source, an AGENTS.md that
describes the project as it is now, command and build-file evidence, and clear hardware, signing
and service limits.
To find runtime problems, read references/debugging-and-release-evidence.md. Start the Debug session
through Haylen, look at the real top scene and screen, test native SDK screens with native UI tools,
and check the protected content in the final build file.
```

## Haylen game

```text
Use haylen-app from paulocoutinhox/skills.
Read [SKILLS_ROOT]/haylen-app/SKILL.md and name the path really loaded. If it is missing, say so.

Create [GAME] in [REPOSITORY] for [PLATFORMS] using [ENGINE_REVISION_AND_LUA_CPP_SCOPE].
Read the current README/features, the game sample and the linked guides on game, scene, input,
assets and lifecycle. Build a playable boot, menu, gameplay, pause and results slice. Keep
world/entities/rules, rendering, input handling, retained HUD, saved data and audio settings apart.
Choose a clear timing model, who owns preloading and which device actions are supported. Avoid a
giant scene or layers built "just in case".
Check a full run, pause/resume, replay/save/restart, UI and input conflicts, failed loading,
background and audio interruption and the real requested Debug/Release builds. Deliver focused
source, an AGENTS.md that describes the project as it is now, real build, verify and runtime
evidence, and the hardware or native-service needs that were not run.
```

## Haylen plugin

```text
Use haylen-app from paulocoutinhox/skills.
Read [SKILLS_ROOT]/haylen-app/SKILL.md and name the path really loaded. If it is missing, say so.

Create [PLUGIN_ID] for [REAL_CAPABILITY_OR_SDK] on [PLATFORMS] in [PLUGIN_REPOSITORY], and add
the reviewed version to [APP_REPOSITORY] at [ENGINE_REVISION]. Read the linked plugin guide, the
current template/features and the real SDK contracts. Generate a plugin folder whose name matches
the ID. Define manifest parameters and dependencies, public Lua methods, results and events, and
native handlers. Use the engine's contracts for permissions, dispatch, streams and buffers, and the
native-screen lifecycle. Keep normal app page navigation separate. Document targets that are not
supported and clear denied or error results. Do not present the generated echo behavior as real
provider features. Test registration in a fresh host, repeated calls, cancel and deny, teardown and
that Release builds keep the plugin, on real supported targets. Deliver source, the plugin README,
app settings, an AGENTS.md that describes the project as it is now, build, verify and runtime
evidence, and the account and hardware needs still open. Do not publish without permission or throw
away changes in a plugin copy that is already installed.
```

## Haylen upgrade

```text
Use haylen-app from paulocoutinhox/skills.
Read [SKILLS_ROOT]/haylen-app/SKILL.md and name the path really loaded. If it is missing, say so.

Upgrade [APP_AND_OR_PLUGIN_REPOSITORIES] from [CURRENT_REVISION] to [TARGET_ENGINE_REVISION] for
[PLATFORMS]. Read the linked project and plugin upgrade guidance and the current template and CLI
contracts. Look at the worktree, app kind, haylen.json/haylen.lock, plugin graph and platforms
settings.
Generate separate haylen new/plugin new references of the right kind and compare them with the
project inspect output. Then merge the needed source changes while you keep deliberate changes and
user data.
Update plugin and native protocols and their callers to the final API, with no compatibility shims.
Do not overwrite customized plugins with plugin add, and do not edit generated build/apps/
projects. Rebuild SDKs, build the requested configurations, verify those build files and run the
real app, game and plugin regression paths. Deliver the reviewed source changes, an AGENTS.md that
describes the project as it is now, the exact commands, merge choices and the real gaps in
checking. Do not assume runtime success from a last-build check.
```
