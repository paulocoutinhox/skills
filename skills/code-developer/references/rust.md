# Rust

## Toolchain and organization

Inspect `Cargo.toml`, workspace membership, `rust-toolchain.toml` when present, the selected edition, `rust-version`, target platforms, and feature flags. Use the declared supported compiler and a coherent current dependency set. A language edition and a compiler version are different constraints. Do not silently migrate an edition, raise the minimum compiler, or enable nightly features to complete an unrelated task.

Use Cargo for builds and dependencies, rustfmt for formatting, and Clippy for linting. Keep `Cargo.lock` tracked for reproducible development unless an explicit repository policy says otherwise. Let Cargo update it rather than editing resolutions by hand. Keep `target/` out of Git. For a published library, compatible dependency declarations and the contributor lockfile serve different purposes.

Keep one struct or enum per focused file with related implementations and tests. Rust has structs, enums, traits, and modules rather than classes. Use idiomatic module functions where appropriate instead of inventing a class-like wrapper. Importable module files use `snake_case`, and Cargo entrypoints such as `lib.rs` and `main.rs` keep their required names. The general preference for hyphens does not override module naming.

## Ownership and interfaces

Make ownership and borrowing visible in public signatures. Prefer borrowed input when ownership transfer is unnecessary. Do not add `clone`, `Rc`, `Arc`, `RefCell`, or synchronization merely to bypass an ownership problem. Choose each only when the actual lifetime, shared ownership, or mutation contract requires it. Use RAII and scope-based cleanup for owned resources.

Prefer concrete types and explicit domain models. Add traits and generic parameters for demonstrated variation or a real dependency boundary. Use exhaustive matching for domain states. Do not hide unknown input behind a wildcard default. Keep iterator chains readable and break important intermediate operations into named variables when that improves debugging. Standard derivations are appropriate when they accurately express the intended behavior. Avoid custom procedural macros that obscure ordinary control flow without a concrete benefit.

## Errors, unsafe code, and concurrency

Represent absence with `Option` and expected failures with `Result`. Propagate errors with context through the project's chosen error model. Do not discard a failure with an ignored result, `.ok()`, or an invented empty value. Avoid `unwrap`, `expect`, and panic-based handling for untrusted input or ordinary production failures. A test assertion or a proven internal invariant needs different treatment from a recoverable user error.

Prefer safe Rust. Isolate required `unsafe` and FFI code in the smallest appropriate boundary. Explain each safety invariant, ownership transfer, pointer validity, aliasing, and lifetime obligation in a precise safety comment when necessary. Never add an unsafe implementation merely to silence a compiler error. Validate lengths, conversions, and arithmetic where external values can exceed supported bounds.

Respect `Send` and `Sync` requirements and the selected async runtime. Define task ownership, cancellation, timeouts, and shutdown. Keep blocking I/O off async executor threads where required. Avoid holding synchronous locks across suspension, establish lock ordering, and do not detach work without a deliberate lifetime. Memory safety does not eliminate logical races, deadlocks, resource leaks, or authorization defects.

## Verification

Use the project's supported target and feature combinations. Do not blindly enable all features when some are mutually exclusive. Typical commands for a locked workspace are:

```bash
cargo fmt --all -- --check
cargo check --workspace --all-targets --locked
cargo clippy --workspace --all-targets --locked
cargo test --workspace --locked
```

Apply the repository's warning policy. Current Cargo versions support `build.warnings` or `CARGO_BUILD_WARNINGS` for warning enforcement. Check the selected toolchain before adopting that setting. Do not suppress broad lint groups to hide a defect or impose every optional Clippy lint on an existing project.

Keep documentation tests enabled when public examples are part of the API. Test failure, boundary, and cancellation behavior where affected. Add target builds, consumer checks, Miri, fuzzing, or sanitizers only when relevant and supported. A successful compile is not proof that the application is free from every security or concurrency defect.

## Applied case: cancellation after an external side effect

Dropping a future can cancel local work without undoing a remote charge or uploaded object. Before an external write, establish a durable operation identity and a recoverable state. On an uncertain result, reconcile that operation rather than repeating it merely because the future did not return success.

Use `Result` for ordinary failure and preserve useful context. `Arc` provides shared ownership, not synchronization of arbitrary state. A `Mutex` guard held across an await can cause contention/deadlock or violate executor requirements. Keep the protected state transition short and model the external phase explicitly.

A drop guard can release local resources but cannot generally await remote compensation. Design compensation/reconciliation as an owned operation with its own error contract. Do not disguise a business race as solved by borrow-checker acceptance.

Verify concurrent duplicate requests, cancellation after the remote commit, worker shutdown and later reconciliation. The official [Rust book's concurrency](https://doc.rust-lang.org/book/ch16-00-concurrency.html) and [async chapters](https://doc.rust-lang.org/book/ch17-00-async-await.html) provide the language foundation. Use the actual async runtime's cancellation contract for implementation.
