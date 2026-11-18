# Tailwind sources

Verified on 2026-11-05 unless a row states a later date. Use the installed major's current documentation and compatibility contract.

| Source | Applied role |
| --- | --- |
| [Vite installation](https://tailwindcss.com/docs/installation/using-vite) | Official current plugin and CSS import integration. |
| [Source detection](https://tailwindcss.com/docs/detecting-classes-in-source-files) | Complete static class names, excluded locations, and explicit source registration. Rechecked on 2026-11-18 (documentation labeled v4.3): automatic exclusions, stylesheet-relative `@source`, `@source not`, `source(none)`, and `@source inline()` safelisting. |
| [Theme variables](https://tailwindcss.com/docs/theme) | Verified on 2026-11-18. Namespaces, `@theme inline` for variables that reference other variables, and `--color-*: initial` namespace removal. |
| [Dark mode](https://tailwindcss.com/docs/dark-mode) | Verified on 2026-11-18. Default `prefers-color-scheme`, `@custom-variant dark` class or data-attribute strategies, and the inline head script that avoids a theme flash. |
| [Compatibility](https://tailwindcss.com/docs/compatibility) | Verified on 2026-11-18. v4 browser floor, no Sass/Less/Stylus design, and `@reference` for CSS modules and Vue/Svelte style blocks. |
| [Upgrade guide](https://tailwindcss.com/docs/upgrade-guide) | Verified on 2026-11-18. Older browsers stay on v3.4, and `npx @tailwindcss/upgrade` requires Node 20+. |
| [Prettier plugin](https://github.com/tailwindlabs/prettier-plugin-tailwindcss) | Verified on 2026-11-18. Class sorting and the v4 `tailwindStylesheet` option resolved relative to the Prettier configuration. |
| [Functions and directives](https://tailwindcss.com/docs/functions-and-directives) | CSS-first theme/custom directives and reference context. |
| [Refactoring UI](https://refactoringui.com/) | Author-published design guidance and contents on hierarchy, spacing, type, and color. The public material was consulted, not the paid book in full. |
| [Fowler: presentation/domain/data](https://martinfowler.com/bliki/PresentationDomainDataLayering.html) | Keep business decisions and data access outside visual styling. |
| [A Philosophy of Software Design](https://web.stanford.edu/~ouster/cgi-bin/book.php) | Professional module-design reading. Author overview consulted, not the full text. |

Feature layout, component files, token roles, variant selection, and a wide formatter width are working
recommendations. Tailwind does not mandate this folder structure or supply accessible behavior by itself.
No compiled application, CSS benchmark, or interactive accessibility audit was executed during authoring.
