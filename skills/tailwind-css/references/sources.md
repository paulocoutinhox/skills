# Tailwind sources

Checked on 2026-11-05 unless a row gives a later date. The skill covers Tailwind CSS v4 and its current documentation and compatibility contract.

| Source | How it is used |
| --- | --- |
| [Vite installation](https://tailwindcss.com/docs/installation/using-vite) | Official current plugin and CSS import integration. |
| [Source detection](https://tailwindcss.com/docs/detecting-classes-in-source-files) | Complete static class names, excluded locations, and explicit source registration. Checked again on 2026-11-18 (documentation labeled v4.3): automatic exclusions, stylesheet-relative `@source`, `@source not`, `source(none)`, and `@source inline()` safelisting. |
| [Theme variables](https://tailwindcss.com/docs/theme) | Checked on 2026-11-18. Namespaces, `@theme inline` for variables that point to other variables, and `--color-*: initial` namespace removal. |
| [Dark mode](https://tailwindcss.com/docs/dark-mode) | Checked on 2026-11-18. Default `prefers-color-scheme`, `@custom-variant dark` class or data-attribute strategies, and the inline head script that avoids a theme flash. |
| [Compatibility](https://tailwindcss.com/docs/compatibility) | Checked on 2026-11-18. v4 browser minimum of Safari 16.4+, Chrome 111+ and Firefox 128+, not designed for Sass/Less/Stylus, and `@reference` for CSS modules and Vue/Svelte style blocks. |
| [Prettier plugin](https://github.com/tailwindlabs/prettier-plugin-tailwindcss) | Checked on 2026-11-18. Class sorting and the v4 `tailwindStylesheet` option, resolved relative to the Prettier configuration. |
| [Functions and directives](https://tailwindcss.com/docs/functions-and-directives) | CSS-first theme and custom directives, and reference context. |
| [Refactoring UI](https://refactoringui.com/) | Design guidance and contents published by the authors on hierarchy, spacing, type, and color. The public material was read, not the full paid book. |
| [Fowler: presentation/domain/data](https://martinfowler.com/bliki/PresentationDomainDataLayering.html) | Keep business decisions and data access outside visual styling. |
| [A Philosophy of Software Design](https://web.stanford.edu/~ouster/cgi-bin/book.php) | Professional reading on module design. The author's overview was read, not the full text. |

Feature layout, component files, token roles, variant selection and a wide formatter width are
working recommendations. Tailwind does not require this folder structure, and it does not provide
accessible behavior by itself. No compiled application, CSS benchmark or interactive accessibility
audit was run while writing this skill.
