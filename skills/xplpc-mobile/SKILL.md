---
name: xplpc-mobile
description: Build native mobile applications with a shared C++ core and xplpc/xplpc. Use for in-process cross-language calls, mappings, Swift/Kotlin integration, native artifacts, ownership, threading, and release checks.
license: MIT
---

# XPLPC Mobile

Use [XPLPC](https://github.com/xplpc/xplpc) when native apps should call shared C++ code, or native
platform features, through serialized procedure calls inside the same process. It uses device
memory, not an HTTP server. It is a bridge between languages and platforms. It is not a UI
framework, a network backend, an app-store publisher, or a replacement for platform permissions.

## Read current purpose, features, and source contracts

Read the current README and the C++, Swift, Kotlin, general and dependency-manager guides for the
chosen targets. Before designing the integration, inspect the real checkout's task help, target
definitions, CMake settings, proxy implementations and matching sample. The C++ public headers
checked for this skill require C++20. Do not assume the language standard or minimum platform from
an older release. See [sources](references/sources.md).

Ask for the targets, native UI framework, existing app architecture, C++ responsibilities, supported
OS and toolchain, data sizes, operation latency and packaging needs. Use MVVM for a new Swift/Kotlin
UI when no architecture is chosen. Keep views, view models, native platform services, bridge
adapters and C++ domain services apart. Do not put all business logic in mapping callbacks.

## Layout and build ownership

| Existing upstream area | Purpose |
| --- | --- |
| `cxx/` | C++ core and public interface. |
| `cxx/custom/` | Worked custom-data/mapping integration, not production application behavior. |
| `swift/`, `swift/sample/` | Swift bridge, packaging, native sample and generated project specification. |
| `kotlin/`, `kotlin/android/lib/` | Kotlin/JNI integration and Android library build. |
| `kotlin/shared/tests/` | Shared Kotlin test contracts. |
| `core/`, `core/targets/` | Python build tasks, configuration, target definitions. |
| `cmake/`, root CMake files | Native target/dependency configuration. |
| `build/` | Generated outputs. Do not edit them as source. |

The checkout also has C, WebAssembly, Flutter, Python, Objective-C and JNI host areas. Read their
own guides only when the user chooses those hosts. This skill covers the Swift/Kotlin mobile path.

Inspect the exact target tree instead of inventing app files inside library internals. In an app,
put the shared C++ services and mapping registration in its native integration module. Put the
Swift/Kotlin adapters in their platform project, and views, view models and models in separate
focused files. Keep one class, enum or view per app source file. Under the owner's conventions, use
named C++ namespaces, operations owned by classes, RAII, explicit ownership, and no anonymous
namespaces. Do not wrap required platform entrypoints in invalid abstractions just to copy another
language's style.

## Initialize before registering and calling

Learn how each host really starts up. A C++ host prepares its native proxy, initializes it, adds it
to the proxy list, then calls `XPLPC::initialize`. A custom C++ integration supplies
`NativePlatformProxy::initializePlatform` and registers mappings there. Leaving it out causes a real
link or integration failure. That is not a reason to add an empty dummy implementation.

The Swift framework checked for this skill initializes on load. Android's AAR declares its own
initialization content provider. Kotlin desktop calls `PlatformInitializer.initialize()` before the
first call. Do not copy one host's startup steps into another. Mappings must be registered under
stable operation names before calls can reach them. Until `XPLPC::initialize` has run, every call is
refused and reported.

`XPLPC_ADD_CUSTOM_DATA` is off by default. When it is off, the build compiles the repository's own
sample `initializePlatform` and `sample.*` mappings. The upstream-built AAR and XCFramework carry
that sample code, so they never contain app-specific native procedures. For app mappings, build
with `-DXPLPC_ADD_CUSTOM_DATA=ON`, `-DXPLPC_CUSTOM_DATA_PATH=<dir>` and
`-DXPLPC_CUSTOM_DATA_INCLUDE_PATH=<dir>/include`. That directory's `CMakeLists.txt` adds the app
sources to `XPLPC_SRC_FILES`, and one of them defines `initializePlatform`. Use `cxx/custom` as the
worked layout. Inspect who owns which sources and targets before turning it on.

## Design explicit mapping contracts

For each operation, define its stable name, typed parameters, result shape, behavior when the result
is missing or an error occurs, the thread it runs on, the owner's lifetime and its side effects. Keep
validation at the real native boundary, and hand business operations to C++ services. A missing
result must not quietly become a successful empty string, zero balance or anonymous user. Where
separate error states matter, the bridge's optional response and diagnostics need an app-level
contract.

For example, `catalog.product-summary` takes a product ID, a locale and the signed-in app context.
It returns a documented product value or an explicit domain failure. The view model handles loading,
empty and failure states, and publishes UI updates on its UI actor or dispatcher. Do not use the
`sample.login` demo with hardcoded credentials as a production login design.

`Request` and `Param` describe the operation and fields. `Client::call<T>` / `Client.call` deliver
responses through a callback. The waiting form is `callAsync` in C++/Swift/Kotlin. Swift `callAsync`
requires iOS 13, tvOS 13 or watchOS 6. Use `call` with its callback when the app's deployment target
is lower. `callSync` reads only a response produced synchronously before the mapping returns. It does
not block and wait for any async work. So a deferred mapping can return nothing from `callSync`. Do
not retry it as if the operation never happened.

## Threading, buffers, and lifetime

Mappings must return quickly. Slow work belongs in an owned worker or async operation with a limited
lifetime. Do not copy a detached-thread demo into production without handling shutdown, errors and
resource ownership. Callbacks run on the thread that responds. Send UI changes to the right main
actor or dispatcher. Swift/Kotlin awaited calls keep their documented actor or coroutine context. A
C++ coroutine resumes on the responding thread unless the app schedules it elsewhere.

Copy or own any callback state that outlives the frame that started the call. Avoid capturing raw
`this` when its owner can disappear. Define what happens to late responses after view teardown,
logout and cancellation. Cancelling a UI await does not prove that native work stopped or that a side
effect was rolled back. Limit pending calls. Where it matters, match up side effects through a
durable app operation ID.

`DataView` borrows an address and a byte count. The owner must keep that storage stable for the
whole time the other language reads it. A stack buffer, a moved vector, a temporary Swift pointer
closure or a released JNI array is not valid after its scope ends. Prefer owned, serialized or copied
data until the zero-copy lifetime is really proven. The side that allocates the memory releases it.
Never free a borrowed buffer from the other language, and never treat a pointer as a lasting, file
or network ID.

## Use the real Python build tasks

Upstream documents `python3 -m venv` plus pip. Under the owner's conventions, run the same tasks
through uv from the checkout root: `uv venv`, then `uv pip install -r requirements.txt`, then
`uv run --no-project python xplpc.py -h`. A help listing of tasks confirms the environment works.
Native tools still need a real install: CMake and a compiler, Xcode and SDKs on macOS, and the
documented Android JDK/NDK. `--dependency-tool=cpm|conan` chooses how dependencies are fetched. CPM
is the default found during research.

```bash
uv run --no-project python xplpc.py -h
uv run --no-project python xplpc.py cxx-test
uv run --no-project python xplpc.py swift-build --platform=apple
uv run --no-project python xplpc.py swift-build-xcframework --platform=apple
uv run --no-project python xplpc.py kotlin-build-aar --platform android
```

Use only the commands for the chosen targets. `--platform=apple` builds every Apple slice for one
SPM binary target. `ios` or `macos` alone produce partial XCFrameworks. An Android AAR is not a
signed app you can distribute. An XCFramework must contain the real device, simulator and platform
slices it needs, with matching headers. Check Catalyst with `vtool -show-build` and expect
`MACCATALYST`, not a renamed macOS binary. `swift-generate-spm-package --url=<archive-url>` writes
`Package.swift` with the archive checksum. Publish the archive at exactly that URL, and regenerate
both after any change. Do not rewrite generated Xcode projects when their `project.yml` is the
source of truth.

The upstream task dispatcher in `xplpc.py` maps each task by name to a Python implementation under
`core/`. A custom CLI task needs a deliberate parser, help and dispatch change, plus a focused Python
implementation. There is no documented `commands/` folder where new tasks are picked up
automatically. Add such extensions only when asked, keep the real failure status, and use uv. App
bridge mappings are a different extension point and do not require changing the build CLI.

## Format code without wrapped calls

Under the collection owner's convention, keep each function or method call on one line. When
arguments are complex, pull out named intermediate values instead of continuation lines lined up
under the open parenthesis. Do not split one string literal into adjacent literals. The upstream
`.clang-format` already uses `ColumnLimit: 0`, and an app's own C++ `.clang-format` must use
`ColumnLimit: 0` too. That setting never adds call wrapping, but it keeps existing line breaks. So
join already wrapped calls by hand once before running `cxx-format` or `clang-format`. Swift and
Kotlin follow the checkout's SwiftFormat and Ktlint configuration, with the same one-line call rule.

## Verify cross-language behavior and release artifacts

After rebuilding changed native libraries, run the relevant native, Swift and Kotlin tests. Kotlin
test tasks do not always rebuild C++ themselves. Test missing mappings, invalid payloads, missing or
error responses, delayed callbacks, owner teardown, concurrent calls, repeated initialization, large
buffers and real publishing on the UI thread. Use the supported sanitizers separately for memory,
undefined behavior and data races. Do not assume one run proves all three. For example, run
`cxx-test --sanitizer address`, then `thread`, then `undefined`. Leak detection with the address
sanitizer works on Linux only. A failing task exit status means the step failed. Report it with the
log instead of retrying with changed flags until it passes.

Build Android release variants, and check that real DTOs still serialize after R8 shrinking. Library
consumer rules do not keep app DTO field names for you. Use exact documented keep rules such as
`-keepclassmembers class com.yourapp.model.** { <fields>; }`, not a blanket switch that turns off
optimization. Check Apple framework slices, deployment targets, signing, device and simulator
behavior, and the installed app's interaction. Do not claim watchOS, visionOS or another target just
because the host is macOS. Read the real supported target definitions.

Deliver focused native and app changes, mapping contracts, the real commands and artifacts, current
AGENTS.md architecture, the tests you ran, and the platform or account requirements still open. This
skill contains no bundled compiler, build automation or automatic documentation refresher.
