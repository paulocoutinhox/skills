---
name: tailwind-css
description: Build maintainable application interfaces with Tailwind CSS. Use for current setup, design tokens, component variants, responsive layouts, dark mode, source detection, accessibility, and production styling checks.
license: MIT
---

# Tailwind CSS

Use Tailwind to build a planned visual system with semantic HTML and consistent components.
Tailwind generates CSS utility classes. It is not an application framework, an accessibility
solution, a component architecture or a permission system. Keep business logic out of class
expressions.

## Inspect before configuring

Read the project instructions, package and lock files, CSS entrypoints, framework integration,
supported browsers, existing design system and build scripts. Confirm whether the task creates an
application, adds Tailwind or improves an existing interface. Respect the chosen framework and
language. For a new frontend, prefer Vite where it fits. Keep the framework's own integration if the
chosen application already has one. Never replace a working build just to match an example.

This skill covers Tailwind CSS v4 and its CSS-first model. Read its current official documentation
and use only the v4 setup. Tailwind v4 targets Safari 16.4+, Chrome 111+, and Firefox 128+, and it
is not designed for Sass, Less, or Stylus pipelines. If the required browsers or such a pipeline
fall outside v4 support, or the project uses another Tailwind major version, stop. Report the
conflict to the user for a decision instead of installing or applying v4 recipes.

See [sources](references/sources.md) and [design-system decisions](references/design-system.md).

## Fit into the real build

For a Vite project where this fits, install `tailwindcss` and `@tailwindcss/vite`. Add the Tailwind
plugin next to the existing framework plugins, and import `tailwindcss` in the real CSS entrypoint.
Import that stylesheet once, through the application's existing entry or layout.

```bash
npm install tailwindcss @tailwindcss/vite
```

```js
import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import tailwindcss from "@tailwindcss/vite";

export default defineConfig({ plugins: [vue(), tailwindcss()] });
```

Here `vue()` stands for the project's existing framework plugin, such as `react()`. Keep its other
settings. The CSS entrypoint then contains the import and the product's tokens:

```css
@import "tailwindcss";

@theme {
  --color-brand-600: #4338ca;
  --color-brand-700: #3730a3;
  --font-sans: "Inter", ui-sans-serif, system-ui, sans-serif;
}
```

The font family above does not download Inter. Supply licensed local font files or a planned way to
load the font, or use the system font stack. Define tokens from the real product brief, not from
this example's colors. In non-Vite projects, follow the official supported integration for that
environment. A development CDN is not the default production build. Keep lockfiles and inspect the
generated CSS.

## Organize styling by responsibility

| Location | Responsibility |
| --- | --- |
| Global CSS entrypoint | Tailwind import, tokens, chosen base rules, theme strategy. |
| Shared UI component | Reusable semantic interaction and stable variants. |
| Feature component | Layout and look for one feature. |
| Local CSS/module | Styling that is clearer as CSS, scoped to its owner. |
| Domain/service layer | Business behavior, independent of Tailwind utilities. |

Keep one component per source file, following the framework's conventions. Match names and
filenames. Group UI by real responsibilities instead of turning every wrapper into a component. Do
not make one universal component with dozens of unrelated flags just to avoid a few clear variants.
Keep class lists readable with the formatter and, if you want, a compatible Tailwind sorting plugin.
For Prettier, `prettier-plugin-tailwindcss` sorts classes. On v4, point its `tailwindStylesheet`
option at the CSS entrypoint. The path is resolved relative to the Prettier configuration. Keep or
set a wide `printWidth`, such as 320, so calls and class lists are not wrapped. Join calls that a
narrower setting split.

```json
{ "printWidth": 320, "plugins": ["prettier-plugin-tailwindcss"], "tailwindStylesheet": "./src/styles/main.css" }
```

Separate logical code blocks with blank lines. Do not add comments that explain obvious utility
classes.

## Build tokens and variants on purpose

Define a small scale for spacing, typography, colors, radii, shadows and content widths. Keep raw
palette tokens apart from semantic roles such as surface, text, border, action, danger and focus.
When you want Tailwind to generate utilities from theme tokens, they must use the current Tailwind
namespaces. Use plain CSS custom properties for values that should not create utility families.
Use `@theme inline` when a theme variable points to another CSS variable, such as
`--font-sans: var(--font-inter)`, so the utility gets the referenced value. Remove a default
namespace with `--color-*: initial` only when the product limits its palette on purpose.

Component variants should match real product states, such as primary/secondary/destructive and
regular/compact. Map each variant to a complete static class string. Check unknown variants through
the component's contract instead of quietly picking an unrelated style. Do not generate
`bg-${color}-600`. Tailwind scans text and cannot work out those complete class names.

```text
primary:   bg-brand-600 text-white hover:bg-brand-700
secondary: bg-white text-slate-900 ring-1 ring-slate-300
```

Define every token you use in the real theme, and check the actual colors for contrast. Keep variant
selection apart from event handlers, data access and domain logic. CSS source order and utility
generation decide the cascade, not the order of conflicting classes in the text. Avoid conflicting
utilities. Use a proven, compatible class-merging tool only when consumers really need to override
classes as part of the API.

Do not move every set of utilities into `@apply` classes by habit. Extract a component when behavior
and look repeat together. Use local CSS when selectors, rich content or an external widget make it
clearer. A Vue/Svelte `<style>` block or a CSS module is processed separately and has no theme.
Before `@apply` there, add `@reference "../app.css";` with the real relative path to the CSS
entrypoint, or use theme variables such as `var(--color-brand-600)` directly.

## Source detection is a production contract

Keep full class names in source. Automatic detection starts from the build's working directory and
skips `.gitignore` entries, `node_modules`, binary files, CSS files and lockfiles. Register truly
external or generated locations, such as a component package, with `@source "../node_modules/pkg";`.
Explicit `@source` paths resolve relative to the stylesheet. Use `@source not "path";` to exclude
noise, and `@import "tailwindcss" source(none);` only when you list every source yourself. Check
monorepos, shared packages and server templates. Do not assume every file in the repository is
scanned. For a few classes that are truly chosen at runtime, list them narrowly with
`@source inline("...")`. Do not safelist whole palettes or every possible arbitrary value to hide a
broken content setup.

Put runtime user values in a validated CSS variable or style property where that fits, not in
untrusted arbitrary class strings. Do not let CMS input inject arbitrary CSS, HTML or URLs into the
application. Check the output in the production build. Development examples alone do not prove that
classes from another package are generated.

## Responsive layout, themes, and readable interaction

Start with the content and the smallest usable layout. Use mobile-first breakpoint overrides. Use
container queries when a component's available width, not the whole viewport, decides the layout.
Prefer normal document flow, flex/grid, gap and natural sizing. Keep absolute positioning for planned
overlays. Avoid fixed heights that cut off translated text, zoomed content, errors or input. Use
limited content widths, `min-w-0` where flex/grid overflow needs it, planned truncation, and images
that keep their aspect ratio. Check long words, empty states and many records.

Choose system-based or user-selected dark mode, and use the documented variant strategy. The default
`dark:` variant follows `prefers-color-scheme`. For a user toggle, redefine it once in the CSS
entrypoint with `@custom-variant dark (&:where(.dark, .dark *));`, or a `data-theme` selector. Set
that class from a small inline script in the document head before the first paint. Store only the
user's explicit choice, and remove it when the user goes back to the system setting. Theme setup must
agree with SSR/hydration if you use them. Define both semantic palettes and check contrast in each.
Do not invert colors blindly or flash a different theme before rendering. Handle reduced motion and
forced colors where they matter. Do not override built-in system controls without a good reason.

Semantic buttons, links, inputs, tables and headings come before styling. Keep keyboard focus
visible with `focus-visible` styles. Show disabled, pending, invalid, selected and hover states
without relying on color alone. Use real labels and link errors to their fields. Hiding content
visually is not the same as removing it from the accessibility tree. Read the chosen component
library's focus, dialog and keyboard contracts instead of building behavior from decorative classes.

## Worked feature and quality gate

Build a responsive account form with one owner for the card and form, focused field components where
they help, and a clear submit state. Use semantic labels, a readable width, spacing tokens,
help/error text, and a focus style with measured contrast. Keep fields in one column until the real
width supports a clearer multi-column layout. A long translated error must make the layout taller
without overlapping anything. Make sure a disabled or pending submit looks different, and that the
user's draft survives a request error.

Inspect narrow and wide containers, keyboard navigation, 200% zoom, long localized content, light and
dark themes, loading and error states, and the high-contrast and reduced-motion modes that matter to
the audience. In a production build, check the real generated classes, registered external source
paths, CSS size, font and image loading, and layout shifts. Search the built CSS, such as Vite's
default `dist/assets/` output, for a sample class from each feature and external source. A missing
class is a source-detection bug to fix, not a reason to add a broad safelist. Do not claim that a
screenshot review proves accessible interaction. Run the project's useful lint, build, component and
browser checks. Update the setup notes and the current AGENTS.md with CSS entrypoints, who owns
tokens and variants, the theme strategy and commands. Deliver readable code, rendered evidence where
available, and the specific limits that remain.
