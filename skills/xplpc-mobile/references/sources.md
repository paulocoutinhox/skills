# XPLPC sources

Verified on 2026-11-05 through upstream main and rechecked on 2026-11-18 against upstream main
commit `377405b256a1cde4c94cdcbc34500d30dd0effb1`. Read the current README/features at operational use.

- [README](https://github.com/xplpc/xplpc/blob/main/README.md): purpose, transport, supported hosts,
  typed requests, callback/waiting forms, and language guide routing.
- [General](https://github.com/xplpc/xplpc/blob/main/docs/general.md): environment and native tooling.
- [C++](https://github.com/xplpc/xplpc/blob/main/docs/cxx.md): C++20, initialization, custom-data build,
  response thread, callSync, DataView, and sanitizer commands.
- [Swift](https://github.com/xplpc/xplpc/blob/main/docs/swift.md): framework lifecycle, actor/callback
  delivery, target slices, SPM archive/checksum, generated sample, and buffer borrow scope.
- [Kotlin](https://github.com/xplpc/xplpc/blob/main/docs/kotlin.md): Android initialization, JNI/AAR,
  coroutine versus callback thread, shared tests, and R8 serialization rules.
- [C++ custom data](https://github.com/xplpc/xplpc/blob/main/docs/cxx.md#how-to-build-the-library-for-c):
  checked 2026-11-18. `XPLPC_CUSTOM_DATA_PATH`, `XPLPC_CUSTOM_DATA_INCLUDE_PATH`, `XPLPC_SRC_FILES`,
  prebuilt AAR/XCFramework sample content, refused calls before `XPLPC::initialize` and sanitizer tasks.
- [Swift packaging](https://github.com/xplpc/xplpc/blob/main/docs/swift.md): checked 2026-11-18.
  `apple` platform slices, Catalyst `vtool -show-build` check and SPM archive/checksum regeneration.
- [Formatting](https://github.com/xplpc/xplpc/blob/main/.clang-format): checked 2026-11-18. The upstream
  C++ style sets `ColumnLimit: 0`. The general guide lists each language's format task.
- [Swift requirements](https://github.com/xplpc/xplpc/blob/main/docs/swift.md#requirements): checked
  2026-11-18. Framework floor iOS 12, tvOS 12, watchOS 5, Mac Catalyst 13.1, macOS 10.15, and the
  higher iOS 13, tvOS 13, watchOS 6 floor of Swift `callAsync`.
- [uv CLI reference](https://docs.astral.sh/uv/reference/cli/): checked 2026-11-18. `uv run --no-project`
  skips project discovery and still runs in an active virtual environment or one found in the current
  or a parent directory, so it uses the checkout's `.venv` created by `uv venv`.
- [Dependency managers](https://github.com/xplpc/xplpc/blob/main/docs/dependency-manager.md): CPM/Conan.
- [Task dispatcher](https://github.com/xplpc/xplpc/blob/main/xplpc.py): actual options and explicit
  task registration. No automatic commands-folder extension is implied.

Owner conventions add separate class/enum/view files, explicit classes/namespaces, readable blocks, and
Python/uv for separately requested glue. These do not change the actual upstream ABI or entrypoints.
No C++/mobile build, simulator, sanitizer, or store publication was executed during authoring.
