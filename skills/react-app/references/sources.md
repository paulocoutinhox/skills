# React sources and decision provenance

Verified on 2026-11-05. Apply current APIs for the selected React/framework release.

| Source | Applied role |
| --- | --- |
| [Creating a React app](https://react.dev/learn/creating-a-react-app) | Official framework recommendation and distinction from this collection's Vite SPA default. |
| [Managing state](https://react.dev/learn/managing-state) | Minimal authoritative state, lifting state, and meaningful transitions. |
| [You might not need an effect](https://react.dev/learn/you-might-not-need-an-effect) | Derived values and event actions do not need synchronization effects. |
| [Synchronizing with effects](https://react.dev/learn/synchronizing-with-effects) | External synchronization, dependencies, cleanup, and development remount behavior. |
| [Vercel React skill](https://github.com/vercel-labs/agent-skills/blob/main/skills/react-best-practices/SKILL.md) | Comparative performance reference: waterfalls and bundles before speculative micro-optimization. Vendor-specific rules are not universal React APIs. No skill content is copied or required at runtime. |
| [Fowler: presentation/domain/data](https://martinfowler.com/bliki/PresentationDomainDataLayering.html) | Separation of UI, domain decisions, and transport within cohesive features. |
| [A Philosophy of Software Design](https://web.stanford.edu/~ouster/cgi-bin/book.php) | Professional module-design reading. The author's public overview was consulted, not the full text. |

Component files, Vite, language defaults, feature directories, and store-selection criteria are project
conventions/recommendations. No generated application or browser benchmark was executed at authoring.
