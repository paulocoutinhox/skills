# XPLPC sources

Verified on 2026-11-05 through upstream main. Read the current README/features at operational use.

- [README](https://github.com/xplpc/xplpc/blob/main/README.md): purpose, transport, supported hosts,
  typed requests, callback/waiting forms, and language guide routing.
- [General](https://github.com/xplpc/xplpc/blob/main/docs/general.md): environment and native tooling.
- [C++](https://github.com/xplpc/xplpc/blob/main/docs/cxx.md): C++20, initialization, custom-data build,
  response thread, callSync, DataView, and sanitizer commands.
- [Swift](https://github.com/xplpc/xplpc/blob/main/docs/swift.md): framework lifecycle, actor/callback
  delivery, target slices, SPM archive/checksum, generated sample, and buffer borrow scope.
- [Kotlin](https://github.com/xplpc/xplpc/blob/main/docs/kotlin.md): Android initialization, JNI/AAR,
  coroutine versus callback thread, shared tests, and R8 serialization rules.
- [Dependency managers](https://github.com/xplpc/xplpc/blob/main/docs/dependency-manager.md): CPM/Conan.
- [Task dispatcher](https://github.com/xplpc/xplpc/blob/main/xplpc.py): actual options and explicit
  task registration. No automatic commands-folder extension is implied.

Owner conventions add separate class/enum/view files, explicit classes/namespaces, readable blocks, and
Python/uv for separately requested glue. These do not change the actual upstream ABI or entrypoints.
No C++/mobile build, simulator, sanitizer, or store publication was executed during authoring.
