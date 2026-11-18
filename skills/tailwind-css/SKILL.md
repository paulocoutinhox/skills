---
name: tailwind-css
description: Build maintainable application interfaces with Tailwind CSS. Use for current setup, design tokens, component variants, responsive layouts, dark mode, source detection, accessibility, and production styling verification.
license: MIT
---

# Tailwind CSS

Use Tailwind to implement an intentional visual system with semantic HTML and coherent components.
Tailwind generates CSS utilities. It is not an application framework, accessibility implementation,
component architecture, or permission system. Keep business logic out of class expressions.

## Inspect before configuring

Read project instructions, package/lock files, CSS entrypoints, framework integration, supported
browsers, existing design system, and build scripts. Confirm whether the task creates an application,
adds Tailwind, or improves an existing interface. Respect the selected framework and language.
For a new frontend, prefer Vite where appropriate. Keep framework-specific integration if the chosen
application already supplies it. Never replace a working build simply to match an example.

Read current official documentation for the installed major. The researched baseline uses the v4
CSS-first model. Do not mix v3 initialization/content recipes into a v4 setup or retain parallel
configuration paths for obsolete behavior. Tailwind v4 targets Safari 16.4+, Chrome 111+, and
Firefox 128+. If the product must support older browsers, keep or select v3.4 and follow its own
documentation. Tailwind v4 is not designed for Sass, Less, or Stylus pipelines. Resolve those
requirements before installing.

If a v3 to v4 upgrade is requested, confirm the browser targets first. Run `npx @tailwindcss/upgrade`
(Node 20+) on a clean worktree, review its complete diff, and finish the remaining manual changes.
Implement the final chosen configuration rather than keeping both. Do not silently drop required
older browsers. See [sources](references/sources.md) and [design-system decisions](references/design-system.md).

## Integrate the actual build

For an applicable Vite project, install `tailwindcss` and `@tailwindcss/vite`, add the Tailwind plugin
alongside the existing framework plugins, and import `tailwindcss` in the actual CSS entrypoint.
Import that stylesheet once through the application's established entry/layout.

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
configuration. The CSS entrypoint then contains the import and the product's tokens:

```css
@import "tailwindcss";

@theme {
  --color-brand-600: #4338ca;
  --color-brand-700: #3730a3;
  --font-sans: "Inter", ui-sans-serif, system-ui, sans-serif;
}
```

The font family above does not download Inter. Supply licensed local assets or an intentional loading
strategy, or select the system stack. Define tokens from the actual product brief, not this example's
palette. In non-Vite projects, follow the official supported integration for that environment. A
development CDN is not the default production build. Preserve lockfiles and inspect generated CSS.

## Organize styling by responsibility

| Location | Responsibility |
| --- | --- |
| Global CSS entrypoint | Tailwind import, tokens, intentional base rules, theme strategy. |
| Shared UI component | Reusable semantic interaction and stable variants. |
| Feature component | Feature-specific layout and presentation. |
| Local CSS/module | Styling that is clearer as CSS, scoped to the owner. |
| Domain/service layer | Business behavior, independent of Tailwind utilities. |

Keep one component per source file using the framework's conventions. Match names and filenames.
Group UI by meaningful responsibilities rather than splitting every wrapper into a component.
Do not make a universal component with dozens of unrelated flags to avoid a few clear variants.
Keep class lists readable with the formatter and optional compatible Tailwind sorting plugin. For
Prettier, `prettier-plugin-tailwindcss` sorts classes. On v4, point its `tailwindStylesheet` option at
the CSS entrypoint, resolved relative to the Prettier configuration. Keep or set a wide `printWidth`,
such as 320, so calls and class lists are not wrapped, and join calls a narrower setting split.

```json
{ "printWidth": 320, "plugins": ["prettier-plugin-tailwindcss"], "tailwindStylesheet": "./src/styles/main.css" }
```

Separate logical code blocks with blank lines. Do not add comments to narrate obvious utility classes.

## Build tokens and variants deliberately

Define a restrained scale for spacing, typography, colors, radii, elevation, and content widths.
Separate primitive palette tokens from semantic roles such as surface, text, border, action, danger,
and focus. Theme tokens must reflect the current Tailwind namespaces when utility generation is
intended. Use ordinary CSS custom properties for values that should not create utility families.
Use `@theme inline` when a theme variable references another CSS variable, such as
`--font-sans: var(--font-inter)`, so the utility receives the referenced value. Remove a default
namespace with `--color-*: initial` only when the product deliberately restricts its palette.

Component variants should represent actual product states, such as primary/secondary/destructive
and regular/compact. Map variants to complete static class strings. Validate unknown variants through
the component's contract rather than silently selecting an unrelated style. Do not generate
`bg-${color}-600`: Tailwind scans text and cannot infer those complete class names.

```text
primary:   bg-brand-600 text-white hover:bg-brand-700
secondary: bg-white text-slate-900 ring-1 ring-slate-300
```

Define every referenced token in the real theme and check actual colors for contrast. Keep variant selection separate
from event handlers, data access, and domain branching. CSS source order and utility generation, not
the textual order of conflicting class tokens, determine the cascade. Avoid conflicting utilities.
Use a proven compatible class-merging tool only when consumer overrides are a real API requirement.

Do not mechanically extract all utilities into `@apply` classes. Extract a component when behavior
and presentation repeat together. Use local CSS when selectors, rich content, or an external widget
make it clearer. A Vue/Svelte `<style>` block or CSS module is processed separately and has no theme.
Before `@apply` there, add `@reference "../app.css";` with the real relative path to the CSS
entrypoint, or use theme variables such as `var(--color-brand-600)` directly.

## Source detection is a production contract

Keep full class names in source. Automatic detection starts from the build's working directory and
skips `.gitignore` entries, `node_modules`, binary files, CSS files, and lockfiles. Register genuinely
external or generated locations, such as a component package, with `@source "../node_modules/pkg";`.
Explicit `@source` paths resolve relative to the stylesheet. Use `@source not "path";` to exclude
noise, and `@import "tailwindcss" source(none);` only when every source is listed explicitly.
Check monorepos, shared packages, and server templates rather than assuming every file under the
repository is scanned. For a few genuinely runtime-selected classes, list them narrowly with
`@source inline("...")`. Do not safelist entire palettes or every possible arbitrary value to hide a
broken content model.

Runtime user values belong in a validated CSS variable/style property where appropriate, not in
untrusted arbitrary class strings. Do not let CMS input inject arbitrary CSS, HTML, or URLs into the
application. Verify output in the production build because development examples alone do not prove
that classes from another package are generated.

## Responsive layout, themes, and readable interaction

Start with content and the smallest usable layout. Use mobile-first breakpoint overrides and
container queries when a component's available width, not the entire viewport, determines layout.
Prefer normal document flow, flex/grid, gap, and intrinsic sizing. Reserve absolute positioning for
intentional overlays. Avoid fixed heights that crop translated text, zoomed content, errors, or input.
Use bounded content widths, `min-w-0` where flex/grid overflow requires it, deliberate truncation,
and images with preserved aspect ratio. Check long words, empty states, and many records.

Choose system-based or explicitly selected dark mode and implement the documented variant strategy.
The default `dark:` variant follows `prefers-color-scheme`. For a user toggle, redefine it once in the
CSS entrypoint with `@custom-variant dark (&:where(.dark, .dark *));`, or a `data-theme` selector, and
set that class from a small inline script in the document head before first paint. Persist only the
explicit choice, and remove it when the user returns to the system preference.
Theme initialization must agree with SSR/hydration if used. Define both semantic palettes and verify
contrast in each. Do not invert colors indiscriminately or flash a different theme before rendering.
Handle reduced motion and forced colors where relevant. Do not override system affordances casually.

Semantic buttons, links, inputs, tables, and headings come before styling. Preserve keyboard focus
with visible `focus-visible` treatment. Show disabled, pending, invalid, selected, and hover states
without relying on color alone. Use real labels and error associations. Hiding content visually is
different from removing it from the accessibility tree. Read the selected component library's focus,
dialog, and keyboard contracts rather than implementing behavior with decorative classes.

## Worked feature and quality gate

Build a responsive account form with one card/form owner, focused field components where warranted,
and explicit submit state. Use semantic labels, a readable width, spacing tokens, help/error text,
and a focus treatment with measured contrast. Keep one-column fields until actual width supports a
clearer multi-column layout. A long translated error must increase layout height without overlap.
Ensure a disabled/pending submit is distinguishable and the user's draft survives a request error.

Inspect narrow/wide containers, keyboard navigation, 200% zoom, long localized content, light/dark
themes, loading/error states, and high-contrast/reduced-motion modes relevant to the audience.
Verify real generated classes in a production build, registered external source paths, CSS payload,
font/image loading, and layout shifts. Search the built CSS, such as Vite's default `dist/assets/`
output, for a representative class from each feature and external source. A missing class is a
source-detection defect to fix, not a reason to add a broad safelist. Do not claim screenshot review proves accessible interaction.
Run the project's meaningful lint/build/component/browser checks. Update setup and current AGENTS.md
with CSS entrypoints, token/variant ownership, theme strategy, and commands. Deliver readable code,
rendered evidence where available, and specific remaining limits.
