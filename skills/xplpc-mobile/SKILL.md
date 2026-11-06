---
name: xplpc-mobile
description: Build native mobile applications with a shared C++ core and xplpc/xplpc. Use for in-process cross-language calls, mappings, Swift/Kotlin integration, native artifacts, ownership, threading, and release verification.
license: MIT
---

# XPLPC Mobile

Use [XPLPC](https://github.com/xplpc/xplpc) when native apps should call a shared C++ implementation
or native platform capabilities through serialized in-process procedure calls. It uses device memory,
not an HTTP server. It is a language/platform bridge, not a UI framework, network backend, app-store
publisher, or a replacement for platform permissions.

## Read current purpose, features, and source contracts

Read the current README and the C++, Swift, Kotlin, general, and dependency-manager guides relevant
to the selected targets. Inspect the actual checkout's task help, target definitions, CMake settings,
proxy implementations, and corresponding sample before designing integration. The researched C++
public headers require C++20. Do not assume the standard or platform floor from an older release.
See [sources](references/sources.md).

Ask for targets, native UI framework, existing application architecture, C++ responsibilities,
supported OS/toolchain, data sizes, operation latency, and packaging needs. Use MVVM for a new
Swift/Kotlin UI when no architecture is selected. Keep views, view models, native platform services,
bridge adapters, and C++ domain services distinct. Do not put all business logic in mapping callbacks.

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

Inspect the exact target tree instead of inventing application files inside library internals.
For an app, own shared C++ services and mapping registration in its native integration module,
Swift/Kotlin adapters in their platform project, and views/view models/models in separate focused
files. Keep one class/enum/view per application source file. Use named C++ namespaces,
class-owned operations, RAII, explicit ownership, and no anonymous namespaces under owner conventions.
Do not wrap required platform entrypoints in invalid abstractions merely to imitate another language.

## Initialize before registering and calling

Understand each host's actual initialization. A C++ host prepares its native proxy, initializes and
appends it to the proxy list, then calls `XPLPC::initialize`. Custom C++ integration supplies
`NativePlatformProxy::initializePlatform` and registers mappings there. Omitting it causes a real
link/integration failure, not a reason for a dummy no-op implementation.

The researched Swift framework initializes on load. Android's AAR declares its initialization content
provider. Kotlin desktop needs its explicit initializer. Do not copy one host's startup sequence into
another. Mappings must be registered under stable operation names before calls can reach them.

`XPLPC_ADD_CUSTOM_DATA` refers to the repository's sample integration. Do not ship sample mappings
or assume a prebuilt sample artifact contains application-specific native procedures. For a custom
native build, use the documented `XPLPC_CUSTOM_DATA_PATH` and include-path settings and a CMake module
that contributes actual application sources. Inspect source/target ownership before enabling it.

## Design explicit mapping contracts

Define each operation's stable name, typed parameters, result shape, absent/error behavior, executing
thread, owner lifetime, and side effects. Keep validation at the actual native boundary and delegate
business operations to C++ services. A missing result must not silently become a successful empty
string, zero balance, or anonymous user. The bridge's optional response and diagnostics need an
application-level contract where distinct error states matter.

For example, `catalog.product-summary` accepts product ID, locale, and authenticated application
context, then returns a documented product value or explicit domain failure. The view model handles
loading/empty/failure and publishes UI updates on its UI actor/dispatcher. Do not use a `sample.login`
demonstration with hardcoded credentials as a production authentication design.

`Request` and `Param` describe the operation and fields. `Client::call<T>` / `Client.call` deliver
callback responses. The waiting form is `callAsync` in C++/Swift/Kotlin. The current `callSync` reads
only a response produced synchronously before the mapping returns. It is not a blocking wait for
arbitrary asynchronous work. A deferred mapping can therefore return absent from `callSync` and must
not be retried as though the operation never happened.

## Threading, buffers, and lifetime

Mappings must return promptly. Slow work belongs in an owned worker/async operation with a bounded
lifetime. Do not copy a detached-thread demo into production without shutdown/error/resource
ownership. Callback delivery runs on the responding thread. Dispatch UI changes to the proper main
actor/dispatcher. Swift/Kotlin awaited calls preserve their documented actor/coroutine context,
while C++ coroutine continuation resumes on the responding thread unless the app schedules it.

Copy/own callback state that outlives the initiating frame. Avoid raw `this` capture when its owner
can disappear. Define late responses after view teardown, logout, and cancellation. Cancelling a UI
await does not prove native work stopped or a side effect was rolled back. Bound pending calls and
reconcile side effects through a durable application operation identity where relevant.

`DataView` borrows an address and byte count. The owner must retain stable storage for the full
cross-language access period. A stack buffer, moved vector, temporary Swift pointer closure, or
released JNI array is not valid after its scope ends. Prefer owned serialized/copying data until
the zero-copy lifetime is actually proven. The allocating side owns release. Never free a borrowed
buffer from the other language or treat a pointer as a persistent/file/network identifier.

## Use the real Python build tasks

Create an isolated uv environment and install the checkout's `requirements.txt`. Existing tasks
run through `uv run --no-project python xplpc.py ...` after environment setup. Native tools still
need their real installation: CMake/compiler, Xcode/SDKs on macOS, and the documented Android JDK/NDK.
Inspect `-h` and the current dependency manager. CPM is the researched default, with Conan supported.

```bash
uv run --no-project python xplpc.py -h
uv run --no-project python xplpc.py cxx-test
uv run --no-project python xplpc.py swift-build --platform=apple
uv run --no-project python xplpc.py swift-build-xcframework --platform=apple
uv run --no-project python xplpc.py kotlin-build-aar --platform android
```

Use only selected target commands. An Android AAR is not a signed distributable app. An XCFramework
must contain actual required device/simulator/platform slices and matching headers. Verify Catalyst
as Catalyst, not a renamed macOS binary. SPM binary archives must match their published URL/checksum.
Do not rewrite generated Xcode projects when their `project.yml` is the source of truth.

The upstream task dispatcher explicitly maps tasks in `xplpc.py` to Python implementations under
`core/`. A custom CLI task requires an intentional parser/help/dispatch change and a focused Python
implementation. There is no advertised automatic drop-in `commands/` directory. Add such extensions
only when requested, preserve real failure status, and use uv. App-level bridge mappings are a
different extension point and do not require altering the build CLI.

## Verify cross-language behavior and release artifacts

Run relevant native, Swift, and Kotlin tests after rebuilding changed native libraries. Kotlin test
tasks do not necessarily rebuild C++ themselves. Test missing mappings, invalid payloads, absent/
error responses, delayed callbacks, owner teardown, concurrent calls, repeated initialization,
large buffers, and actual UI-thread publication. Use supported sanitizers separately for memory,
undefined behavior, and data races rather than assuming one run proves all three.

Build Android release variants and verify serialization of actual DTOs after R8 shrinking. Library
consumer rules do not automatically keep application DTO field names. Use precise documented keep
rules, not blanket disabling of optimization. Verify Apple framework slices, deployment targets,
signing, device/simulator behavior, and installed app interaction. Do not claim watchOS/visionOS or
another target merely because the host is macOS. Read actual supported target definitions.

Deliver focused native/app changes, mapping contracts, actual commands/artifacts, current AGENTS.md
architecture, tests performed, and unresolved platform/account requirements. This skill contains no
bundled compiler, build automation, or autonomous documentation refresher.
