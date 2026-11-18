# C++

## Standard and organization

Inspect the actual compiler and configured standard. Use the strongest appropriate facilities available in that standard. `C++21` is not an ISO standard name. If requested, clarify whether C++20 or C++23 is intended rather than inventing a compiler flag.

Keep includes direct, minimal, ordered, and self-sufficient. Do not rely on transitive includes. Keep header declarations and implementations consistent. Use one class or enum per file. Put application types in named project namespaces. Do not use anonymous namespaces or `using namespace` directives in headers. Under this collection's convention, application functions belong to classes, with static methods where no instance state is required. Required language entrypoints such as `main`, mandated operators, or framework hooks are explicit exceptions. Do not create unusable C++ to imitate a universal class-only rule.

Do not add descriptive method, member, or section comments in headers. Make names and types carry intent. Required tooling directives and license notices retain their exact form.

## Ownership and correctness

Prefer values, RAII, `const`, references, containers, and unique ownership. Use `std::unique_ptr` for exclusive dynamic ownership and `std::shared_ptr` only when ownership is actually shared. Use weak references to break shared cycles. A non-owning raw pointer can express optional observation where the project requires it, but never use ambiguous raw ownership or manual `new`/`delete` when RAII can express the lifetime.

Avoid C-style casts, unchecked narrowing, pointer arithmetic, macros, and C library patterns when standard C++ alternatives exist. When integrating a C API, isolate it in a C++ adapter with correct linkage, explicit sizes, ownership, custom deleters, and error translation. Do not cast away constness to satisfy an API.

Check indexing, iterator validity, object lifetime, alignment, initialization, signed overflow, unsigned wrap, numeric conversion, exception safety, and bounds before access. Use checked arithmetic for untrusted sizes. Apply the rule of zero where possible. Do not return dangling references or capture shorter-lived objects by reference in escaping lambdas.

## Concurrency

Choose clear ownership and synchronization. Guard shared mutable state consistently, use RAII locks, establish lock order, and avoid invoking unknown code while holding a lock. Join owned threads and preserve lifetime through asynchronous work. Use atomics with a justified memory model, not as a substitute for a coherent concurrency design. Review data races, deadlocks, reentrancy, cancellation, and partial initialization explicitly.

## Call line breaks and clang-format

Under the owner convention, a function call, its argument list and a string literal stay on one source line. Do not leave continuation lines aligned under an opening parenthesis, and do not split one message into adjacent string literals. This wrapped form is wrong:

```cpp
_presenceMachine.doorOpened(doors.lastOpenedAt, Settings.get().doorConfirmationMs,
                            _adminActive);
Serial.printf("[CONTROL] Admin closed without a gesture after an opening: "
              "confirm presence within %lu s\n",
              static_cast<unsigned long>(Settings.get().doorConfirmationMs / 1000));
```

Write each call on one line. When the arguments are long expressions, name them first so the call remains readable and each value is visible in a debugger:

```cpp
const uint32_t confirmationMs = Settings.get().doorConfirmationMs;
const unsigned long confirmationSeconds = static_cast<unsigned long>(confirmationMs / 1000);

_presenceMachine.doorOpened(doors.lastOpenedAt, confirmationMs, _adminActive);
Serial.printf("[CONTROL] Admin closed without a gesture after an opening: confirm presence within %lu s\n", confirmationSeconds);
```

Such wrapping usually comes from clang-format's column limit, not from the author. The `LLVM`, `Google`, `Chromium` and `Mozilla` presets use an 80-column limit, `GNU` uses 79 and `Microsoft` uses 120. Only `WebKit` has no limit. When a call is wrapped, inspect the formatter configuration before editing code:

1. Find the effective configuration. clang-format uses the nearest `.clang-format` or `_clang-format` above the file. Without one, an editor applies its own fallback style, for example the VS Code C/C++ extension's `C_Cpp.clang_format_fallbackStyle`. PlatformIO, Arduino and IDE plugins can also format on save. Record which formatter actually changed the file.
2. Set `ColumnLimit: 0` in the repository's `.clang-format`. A zero limit means no column limit, so clang-format does not introduce call wrapping. Keep the rest of the style unchanged. Add a root `.clang-format` when the project has none, so the command line and every editor share one configuration.
3. Join existing wrapped calls by hand once. With `ColumnLimit: 0`, clang-format respects line breaks already present inside a statement, so it does not repair code that an earlier narrow limit wrapped. Merge adjacent string literals into one literal at the same time.
4. Run the project's clang-format version over the changed files, then run it again and confirm the second run produces no diff. Inspect the result for any remaining continuation lines inside calls.

A minimal configuration that preserves an existing preset looks like this:

```yaml
BasedOnStyle: Google
ColumnLimit: 0
```

`BreakAdjacentStringLiterals: false` exists since clang-format 18. It is unnecessary once each message is one literal, and an older clang-format fails with an `unknown key` error instead of formatting, so add it only when the pinned version supports it. Do not raise the limit to a large number as the only fix when the owner wants calls never wrapped, because a positive limit still wraps longer statements. Do not wrap individual calls in `clang-format off` directives to escape a narrow limit. Fix the configuration instead.

A multi-line lambda or block passed as the final argument is not a wrapped argument list. Its call starts on one line and its body follows the lambda convention below.

## Lambda formatting preference

Wrap the smallest region containing each lambda in balanced formatter directives, and hand-format it clearly. This is an owner preference, not a claim that clang-format cannot format lambdas.

```cpp
// clang-format off
const auto isReady = [](const Task& task) {
    return task.isReady();
};
// clang-format on
```

Keep the surrounding code formatted normally. Do not disable formatting for an entire file to avoid reviewing one expression.

## Verification

Use the declared CMake or other build system, warnings, clang-format with the column policy above, and configured clang-tidy checks. Run AddressSanitizer and UndefinedBehaviorSanitizer for relevant memory and arithmetic paths. Run ThreadSanitizer separately where supported for concurrent changes. Add boundary and lifetime tests where they meaningfully detect the defect. Tool availability and platform limitations must be reported. No tool proves the absence of all UB or races.

## Applied case: ownership at a native-library boundary

An adapter calling a C library must know whether a returned pointer is borrowed or owned, which function releases it, which thread can use it and how errors are reported. Represent owned results with a suitable RAII type/custom deleter. Validate status and lengths before constructing views or copying bytes. Do not retain a pointer into a temporary buffer after the adapter returns.

For shared state, identify the exact invariant protected by a mutex. Copy/prepare necessary values, release the lock before invoking an unknown callback, then reconcile state according to the actual contract. Calling user code while holding a lock can deadlock or reenter a partially updated object.

Select facilities by the configured standard. C++20's `std::jthread` can express scoped joining/cancellation when that is the real target. A C++17 project requires a coherent explicit thread owner, not preprocessor branches supporting every possible standard. Put application types/operations in the named class/namespace structure required by the owner, with required language hooks as explicit exceptions.

Test the error/cleanup path, empty/large buffer, owner destruction during work and relevant concurrency. Address/undefined-behavior sanitizers and a separate supported ThreadSanitizer run answer different questions. The [C++ Core Guidelines](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines) provide specific ownership/concurrency rules, not a guarantee that selecting a smart pointer eliminates every lifetime defect.
