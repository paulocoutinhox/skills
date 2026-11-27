# C++

## Standard and organization

Check the real compiler and the configured standard. Use the best fitting features that standard offers. `C++21` is not an ISO standard name. If a user asks for it, ask whether they mean C++20 or C++23 instead of inventing a compiler flag.

Keep includes direct, minimal, ordered, and complete on their own. Do not rely on transitive includes. Keep header declarations and implementations consistent. Use one class or enum per file. Put application types in named project namespaces. Do not use anonymous namespaces or `using namespace` directives in headers. Under this collection's convention, application functions belong to classes, with static methods where no instance state is needed. Required language entrypoints such as `main`, required operators, or framework hooks are stated exceptions. Do not write unusable C++ to copy a universal class-only rule.

Do not add descriptive method, member, or section comments in headers. Let names and types carry the intent. Required tool directives and license notices keep their exact form.

## Ownership and correctness

Prefer values, RAII, `const`, references, containers, and unique ownership. Use `std::unique_ptr` for exclusive dynamic ownership and `std::shared_ptr` only when ownership is actually shared. Use weak references to break shared cycles. A non-owning raw pointer can express optional observation where the project needs it. Never use unclear raw ownership or manual `new`/`delete` when RAII can express the lifetime.

Avoid C-style casts, unchecked narrowing, pointer arithmetic, macros, and C library patterns when standard C++ alternatives exist. When you integrate a C API, keep it inside a C++ adapter with correct linkage, explicit sizes, ownership, custom deleters, and error translation. Do not cast away constness to satisfy an API.

Check indexing, iterator validity, object lifetime, alignment, initialization, signed overflow, unsigned wrap, numeric conversion, exception safety, and bounds before access. Use checked arithmetic for untrusted sizes. Apply the rule of zero where possible. Do not return dangling references or capture shorter-lived objects by reference in escaping lambdas.

## Concurrency

Choose clear ownership and synchronization. Guard shared mutable state the same way every time, use RAII locks, set a lock order, and avoid calling unknown code while you hold a lock. Join the threads you own and keep objects alive through asynchronous work. Use atomics with a memory model you can justify, not as a replacement for a sound concurrency design. Review data races, deadlocks, reentrancy, cancellation, and partial initialization on purpose.

## Call line breaks and clang-format

Under the owner convention, a function call, its argument list and a string literal stay on one source line. Do not leave continuation lines lined up under an opening parenthesis. Do not split one message into adjacent string literals. The wrong form puts the last argument of a `doorOpened` call on a continuation line lined up under its opening parenthesis, and breaks a `Serial.printf` format message into two adjacent literals on separate lines with its computed argument on a third line.

Write each call on one line. When the arguments are long expressions, name them first so the call stays readable and each value is visible in a debugger:

```cpp
const uint32_t confirmationMs = Settings.get().doorConfirmationMs;
const unsigned long confirmationSeconds = static_cast<unsigned long>(confirmationMs / 1000);

_presenceMachine.doorOpened(doors.lastOpenedAt, confirmationMs, _adminActive);
Serial.printf("[CONTROL] Admin closed without a gesture after an opening: confirm presence within %lu s\n", confirmationSeconds);
```

Such wrapping usually comes from clang-format's column limit, not from the author. The `LLVM`, `Google`, `Chromium` and `Mozilla` presets use an 80-column limit, `GNU` uses 79 and `Microsoft` uses 120. Only `WebKit` has no limit. When a call is wrapped, check the formatter configuration before you edit code:

1. Find the effective configuration. clang-format uses the nearest `.clang-format` or `_clang-format` above the file. Without one, an editor applies its own fallback style, for example the VS Code C/C++ extension's `C_Cpp.clang_format_fallbackStyle`. PlatformIO, Arduino and IDE plugins can also format on save. Note which formatter really changed the file.
2. Set `ColumnLimit: 0` in the repository's `.clang-format`. A zero limit means no column limit, so clang-format does not introduce call wrapping. Keep the rest of the style unchanged. Add a root `.clang-format` when the project has none, so the command line and every editor share one configuration.
3. Join existing wrapped calls by hand once. With `ColumnLimit: 0`, clang-format keeps line breaks already inside a statement, so it does not fix code that an earlier narrow limit wrapped. Merge adjacent string literals into one literal at the same time.
4. Run the project's clang-format version over the changed files, then run it again and confirm the second run produces no diff. Check the result for any remaining continuation lines inside calls.

A minimal configuration that keeps an existing preset looks like this:

```yaml
BasedOnStyle: Google
ColumnLimit: 0
```

Do not add `BreakAdjacentStringLiterals: false`. It is unnecessary once each message is one literal. Do not raise the limit to a large number as the only fix when the owner wants calls never wrapped. A positive limit still wraps longer statements. Do not wrap single calls in `clang-format off` directives to get around a narrow limit. Fix the configuration instead.

A multi-line lambda or block passed as the final argument is not a wrapped argument list. Its call starts on one line, and its body follows the lambda convention below.

## Lambda formatting preference

Wrap the smallest region that holds each lambda in matching formatter directives, and format it clearly by hand. This is an owner preference, not a claim that clang-format cannot format lambdas.

```cpp
// clang-format off
const auto isReady = [](const Task& task) {
    return task.isReady();
};
// clang-format on
```

Keep the surrounding code formatted normally. Do not disable formatting for an entire file to avoid reviewing one expression.

## Verification

Use the declared CMake or other build system, warnings, clang-format with the column policy above, and configured clang-tidy checks. Run AddressSanitizer and UndefinedBehaviorSanitizer for relevant memory and arithmetic paths. Run ThreadSanitizer on its own, where supported, for concurrent changes. Add edge and lifetime tests where they really catch the bug. Report which tools were available and any platform limits. No tool proves that all UB or races are gone.

## Applied case: ownership at a native-library boundary

An adapter that calls a C library must know whether a returned pointer is borrowed or owned, which function frees it, which thread can use it and how errors are reported. Represent owned results with a fitting RAII type or custom deleter. Validate status and lengths before constructing views or copying bytes. Do not retain a pointer into a temporary buffer after the adapter returns.

For shared state, name the exact rule that a mutex protects. Copy or prepare the needed values, release the lock before calling an unknown callback, then bring the state back in line with the real contract. Calling user code while you hold a lock can deadlock or reenter a half-updated object.

Choose features by the configured standard. C++20's `std::jthread` can express scoped joining and cancellation when that is the real target. A C++17 project needs one clear thread owner, not preprocessor branches for every possible standard. Put application types and operations in the named class and namespace structure the owner requires, with required language hooks as stated exceptions.

Test the error and cleanup path, empty and large buffers, the owner being destroyed during work and the relevant concurrency. Address and undefined-behavior sanitizers and a separate supported ThreadSanitizer run answer different questions. The [C++ Core Guidelines](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines) give specific ownership and concurrency rules. They do not promise that choosing a smart pointer removes every lifetime bug.
