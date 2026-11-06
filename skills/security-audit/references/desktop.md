# Desktop and native security catalog

Review local process trust as well as network trust. Desktop applications can expose powerful filesystem, shell, device, and credential capabilities. Local malicious input can cross a privilege boundary even when no web server exists.

## Native and operating-system boundaries

- Require the intended user/process identity on IPC, named pipes, local sockets, RPC, plugins, browser/native bridges, and helper services. Authenticate and authorize individual operations.
- Minimize process privileges and isolate privileged helpers. Validate helper inputs and prevent a low-privilege caller from choosing arbitrary file paths or commands.
- Use safe file creation and permissions. Review symlink/hard-link traversal, race-prone temporary files, path canonicalization, archive extraction, and TOCTOU behavior.
- Avoid shell command composition with untrusted strings. Use argument arrays and explicit programs. Validate file associations, URL handlers, and documents opened through the OS.
- Review DLL/shared-library search paths, plugin loading, unsigned extensions, environment-variable injection, and writable directories in executable lookup paths.
- Verify installer/update signatures, publisher identity, transport, downgrade protection where required, atomic update behavior, and rollback policy. HTTPS alone does not establish executable provenance.
- Use platform credential stores instead of plaintext preferences. Audit logs, crash dumps, clipboard, screenshots, memory retention, local caches, and logout behavior for sensitive data.
- Apply secure transport validation, correct cryptography, least-privilege permissions, dependency updates, useful security logging, and explicit error handling.

## Memory and concurrency

Review buffer boundaries, integer overflow, type conversion, initialization, lifetime, ownership, use-after-free, double-free, leaks, iterator invalidation, unsafe FFI, and untrusted binary parsers. Prefer safe containers, RAII, and checked arithmetic where the language supports them.

Inspect shared mutable state, lock ordering, callback reentrancy, thread lifetimes, cancellation, and resource cleanup for races and deadlocks. Use sanitizers, static analysis, fuzzing, and targeted tests where supported. Do not claim no memory defects because the application launches successfully.

## Electron and embedded web runtimes

Keep the framework and embedded browser current. Prefer renderer sandboxing, context isolation, no Node integration for untrusted content, and a small explicit preload API. Do not expose generic filesystem, shell, or evaluation capabilities over the bridge.

Validate IPC sender identity, frame origin, channel, payload, and operation authorization. Validate navigation and window creation. Do not open untrusted URLs with unrestricted external-shell handlers. Keep web security enabled and use a suitable content security policy. Treat remote content and loaded documents as untrusted even if an initial URL was approved.

The same boundary analysis applies to other embedded webview frameworks, but use their actual capability and permission models rather than copying Electron flags into an unrelated toolkit.

## Distribution checks

Inspect release signing, notarization or platform verification where applicable, installer permissions, install/update directories, bundled licenses/dependencies, unneeded debug symbols with sensitive paths, crash-report privacy, and writable application resources. Obfuscation is not a substitute for authorization, key protection, or signed updates.
