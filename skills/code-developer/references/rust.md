# Rust

## Toolchain and organization

Check `Cargo.toml`, workspace membership, `rust-toolchain.toml` when present, the selected edition, `rust-version`, target platforms, and feature flags. Use the declared supported compiler and a consistent, current set of dependencies. A language edition and a compiler version are different limits. Do not quietly move to a new edition, raise the minimum compiler, or turn on nightly features to finish an unrelated task.

Use Cargo for builds and dependencies, rustfmt for formatting, and Clippy for linting. Keep `Cargo.lock` tracked for reproducible development unless a stated repository policy says otherwise. Let Cargo update it instead of editing resolutions by hand. Keep `target/` out of Git. For a published library, compatible dependency declarations and the contributor lockfile serve different purposes.

Keep one struct or enum per focused file with related implementations and tests. Rust has structs, enums, traits, and modules rather than classes. Use normal Rust module functions where they fit instead of inventing a class-like wrapper. Importable module files use `snake_case`, and Cargo entrypoints such as `lib.rs` and `main.rs` keep their required names. The general preference for hyphens does not override module naming.

## Ownership and interfaces

Make ownership and borrowing visible in public signatures. Prefer borrowed input when you do not need to move ownership. Do not add `clone`, `Rc`, `Arc`, `RefCell`, or synchronization just to get around an ownership problem. Choose each one only when the real lifetime, shared ownership, or mutation contract needs it. Use RAII and scope-based cleanup for owned resources.

Prefer concrete types and clear domain models. Add traits and generic parameters for proven variation or a real dependency boundary. Use exhaustive matching for domain states. Do not hide unknown input behind a wildcard default. Keep iterator chains readable. Put important intermediate steps into named variables when that helps debugging. Standard derives fit when they match the intended behavior. Avoid custom procedural macros that hide ordinary control flow without a concrete benefit.

## Errors, unsafe code, and concurrency

Represent absence with `Option` and expected failures with `Result`. Propagate errors with context through the project's chosen error model. Do not discard a failure with an ignored result, `.ok()`, or an invented empty value. Avoid `unwrap`, `expect`, and panic-based handling for untrusted input or ordinary production failures. A test assertion or a proven internal rule needs different handling than a user error you can recover from.

Prefer safe Rust. Keep required `unsafe` and FFI code inside the smallest fitting boundary. When needed, explain each safety rule, ownership transfer, pointer validity, aliasing, and lifetime duty in a precise safety comment. Never add an unsafe implementation just to silence a compiler error. Validate lengths, conversions, and arithmetic where outside values can go past supported limits.

Respect `Send` and `Sync` requirements and the chosen async runtime. Define task ownership, cancellation, timeouts, and shutdown. Keep blocking I/O off async executor threads where required. Avoid holding synchronous locks across suspension, set a lock order, and do not detach work without a planned lifetime. Memory safety does not remove logic races, deadlocks, resource leaks, or authorization bugs.

## Verification

Use the project's supported target and feature combinations. Do not turn on all features without thinking when some cannot be used together. Typical commands for a locked workspace are:

```bash
cargo fmt --all -- --check
cargo check --workspace --all-targets --locked
cargo clippy --workspace --all-targets --locked
cargo test --workspace --locked
```

rustfmt wraps a call's arguments vertically when they exceed `fn_call_width`, which defaults to 60 percent of `max_width` (100). Under the owner's single-line call convention, set `max_width = 320` and `use_small_heuristics = "Max"` in `rustfmt.toml`, which makes each granular width, including `fn_call_width`, equal to `max_width`. Both options are stable.

Follow the repository's warning policy. Current Cargo versions support `build.warnings` or `CARGO_BUILD_WARNINGS` to enforce warnings. Check the chosen toolchain before you use that setting. Do not silence broad lint groups to hide a bug, and do not force every optional Clippy lint on an existing project.

Keep documentation tests enabled when public examples are part of the API. Test failure, edge, and cancellation behavior where the change affects them. Add target builds, consumer checks, Miri, fuzzing, or sanitizers only when they are relevant and supported. A successful compile does not prove that the application is free of every security or concurrency bug.

## Applied case: cancellation after an external side effect

Dropping a future can cancel local work without undoing a remote charge or uploaded object. Before an external write, set up a durable operation ID and a state you can recover from. When the result is unclear, check that operation's real outcome instead of repeating it just because the future did not return success.

Use `Result` for ordinary failure and keep useful context. `Arc` gives shared ownership, not synchronization of any state. A `Mutex` guard held across an await can cause contention or deadlock, or break executor requirements. Keep the protected state change short and model the external phase clearly.

A drop guard can free local resources, but in general it cannot await a remote undo step. Design the undo or result check as an owned operation with its own error contract. Do not pretend a business race is solved because the borrow checker accepts the code.

Check concurrent duplicate requests, cancellation after the remote commit, worker shutdown and the later result check. The official [Rust book's concurrency](https://doc.rust-lang.org/book/ch16-00-concurrency.html) and [async chapters](https://doc.rust-lang.org/book/ch17-00-async-await.html) give the language basics. Use the real async runtime's cancellation contract for the code.
