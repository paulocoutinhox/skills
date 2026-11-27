# Vue sources and where decisions come from

Checked on 2026-11-05 unless a row gives a later date. Official framework behavior comes before community skill preferences.

| Source | How it is used |
| --- | --- |
| [Vue quick start](https://vuejs.org/guide/quick-start.html) | Current create-vue/Vite workflow and the language and tool options to pick. |
| [Vue composables](https://vuejs.org/guide/reusability/composables) | Reusing reactive logic, instance ownership, lifecycle and cleanup conventions. |
| [Vue state management](https://vuejs.org/guide/scaling-up/state-management) | Who owns shared state, and the official Pinia recommendation. |
| [Vue performance](https://vuejs.org/guide/best-practices/performance) | Rendering-mode decisions and targeted performance work. |
| [Vue watchers](https://vuejs.org/guide/essentials/watchers.html) | Checked on 2026-11-18. `onWatcherCleanup` cannot come after an `await`. The `onCleanup` callback argument has no such synchronous limit. |
| [Component v-model](https://vuejs.org/guide/components/v-model.html) | Checked on 2026-11-18. `defineModel()` is the recommended two-way binding. |
| [Vue community skill](https://github.com/vuejs-ai/skills/blob/main/skills/vue-best-practices/SKILL.md) | Writing reference for comparison on components, data flow, and composable boundaries. Community instructions are not Vue requirements. No resource is copied or needed at runtime. |
| [Fowler: presentation/domain/data](https://martinfowler.com/bliki/PresentationDomainDataLayering.html) | Keeping UI, domain decisions, and data access apart, inside well-grouped features. |
| [A Philosophy of Software Design](https://web.stanford.edu/~ouster/cgi-bin/book.php) | Professional reading on useful module boundaries and reducing complexity. The author's public overview was read, not the whole book. |

Folder names, the TypeScript preference, one component per file, blank lines between
responsibilities, single-line calls with a wide formatter width, and Vite defaults are this
collection's working conventions. They are not extra Vue syntax rules. No generated app, browser run
or framework benchmark was run while writing this skill.
