# React

For a new client-rendered application, use Vite unless the user requests a framework with its own supported toolchain. Keep one component per file. Split components by real responsibility, and put reusable lifecycle behavior in focused hooks. Keep pure computations outside effects, and avoid needless wrappers or abstractions.

Choose the smallest owner for state. Derive values instead of keeping duplicate state in sync. Use stable domain keys for dynamic lists. Treat render as pure. Use effects for synchronization with external systems, with correct dependencies and cleanup. Do not silence hook dependency warnings to hide a lifecycle bug. Block outdated async responses and clean up subscriptions on unmount.

Start with local state and context where they fit. For large shared client state, weigh the project's existing library and a current compatible store such as Redux Toolkit or Zustand against the real needs. There is no universal best store. Use a dedicated query cache when server-state behavior calls for it, instead of copying remote data into several stores.

Avoid unsafe HTML injection, token exposure, direct changes to React state, wrong assumptions about stable callbacks, and heavy memoization without evidence. When the project enables React Compiler, rely on it for new code and keep `useMemo` and `useCallback` as escape hatches. Remove existing manual memoization only with tests that cover the affected behavior. Check accessibility, loading, empty and error states, navigation, and relevant concurrent behavior. Run type checking, lint, a production build, and focused component or integration tests.

## Applied case: derived values and effect ownership

If filtered rows can be computed from current rows and a filter, derive them during rendering or through memoization with a clear reason. A second mutable filtered-rows state plus an effect adds another sync path and can briefly show conflicting data.

Use an effect for an external subscription or request, and return its real cleanup. The extra setup and cleanup cycle in development reveals missing ownership. It does not justify a global flag that blocks a valid remount. Tie async completion to the current inputs and owner. Do not silence dependencies to freeze an outdated closure.

For an editable row list, use a stable domain key so reordering does not attach local edit state to the wrong item. Test reorder and delete while editing, request replacement and unmount. [You Might Not Need an Effect](https://react.dev/learn/you-might-not-need-an-effect) and [Synchronizing with Effects](https://react.dev/learn/synchronizing-with-effects) explain the real React differences used here.
