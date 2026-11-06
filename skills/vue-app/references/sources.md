# Vue sources and decision provenance

Verified on 2026-11-05. Official framework behavior takes precedence over community skill preferences.

| Source | Applied role |
| --- | --- |
| [Vue quick start](https://vuejs.org/guide/quick-start.html) | Current create-vue/Vite workflow and selected language/tool options. |
| [Vue composables](https://vuejs.org/guide/reusability/composables) | Reactive logic reuse, instance ownership, lifecycle and cleanup conventions. |
| [Vue state management](https://vuejs.org/guide/scaling-up/state-management) | Shared-state ownership and the official Pinia recommendation. |
| [Vue performance](https://vuejs.org/guide/best-practices/performance) | Rendering-mode decisions and targeted performance work. |
| [Vue community skill](https://github.com/vuejs-ai/skills/blob/main/skills/vue-best-practices/SKILL.md) | Comparative authoring reference for components, data flow, and composable boundaries. Community instructions are not Vue requirements. No resource is copied or required at runtime. |
| [Fowler: presentation/domain/data](https://martinfowler.com/bliki/PresentationDomainDataLayering.html) | Separation of UI, domain decisions, and data access, applied within coherent features. |
| [A Philosophy of Software Design](https://web.stanford.edu/~ouster/cgi-bin/book.php) | Professional reading on useful module boundaries and reducing complexity. The author's public overview was consulted, not the entire book. |

Folder names, TypeScript preference, one-component files, blank responsibility separators, and
Vite defaults are this collection's working conventions. They are not additional Vue syntax rules.
No generated app, browser run, or framework benchmark was executed during skill authoring.
