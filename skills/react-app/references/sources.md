# React sources and where decisions come from

Checked on 2026-11-05 unless a row gives a later date. Use the current APIs for the chosen React or framework release.

| Source | How it is used |
| --- | --- |
| [Creating a React app](https://react.dev/learn/creating-a-react-app) | Official framework recommendation, and how it differs from this collection's Vite SPA default. Checked again on 2026-11-18: frameworks are recommended first, and a build tool such as Vite is the documented path for starting from scratch. |
| [Sunsetting Create React App](https://react.dev/blog/2025/02/14/sunsetting-create-react-app) | Checked on 2026-11-18. The React team deprecated Create React App for new apps on 2025-02-14 and recommends a framework or a build tool such as Vite, Parcel, or Rsbuild. |
| [Managing state](https://react.dev/learn/managing-state) | Minimal source-of-truth state, lifting state, and meaningful transitions. |
| [You might not need an effect](https://react.dev/learn/you-might-not-need-an-effect) | Derived values and event actions do not need sync effects. |
| [Synchronizing with effects](https://react.dev/learn/synchronizing-with-effects) | Syncing with external systems, dependencies, cleanup, and remount behavior in development. |
| [React Compiler introduction](https://react.dev/learn/react-compiler/introduction) | Checked on 2026-11-18. The compiler is documented as stable. New code relies on it for memoization, with `useMemo`/`useCallback` as escape hatches. Existing memoization stays unless its removal is tested. |
| [useActionState](https://react.dev/reference/react/useActionState) | Checked on 2026-11-18. Returns state, a dispatch action and `isPending`, and works with plain client functions passed to `<form action>`. |
| [Vercel React skill](https://github.com/vercel-labs/agent-skills/blob/main/skills/react-best-practices/SKILL.md) | Performance reference for comparison: fix waterfalls and bundles before guessing at micro-optimizations. Vendor-specific rules are not universal React APIs. No skill content is copied or needed at runtime. |
| [Fowler: presentation/domain/data](https://martinfowler.com/bliki/PresentationDomainDataLayering.html) | Keeping UI, domain decisions, and transport apart inside well-grouped features. |
| [A Philosophy of Software Design](https://web.stanford.edu/~ouster/cgi-bin/book.php) | Professional reading on module design. The author's public overview was read, not the full text. |

Component files, Vite, language defaults, feature directories, single-line calls with a wide
formatter width, and the store-selection criteria are project conventions and recommendations. No
generated application or browser benchmark was run while writing this skill.
