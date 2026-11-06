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
configuration paths for obsolete behavior. If an upgrade is requested, implement the final chosen
configuration and verify the real browser requirements. Do not silently drop required older browsers.
See [sources](references/sources.md) and [design-system decisions](references/design-system.md).

## Integrate the actual build

For an applicable Vite project, install `tailwindcss` and `@tailwindcss/vite`, add the Tailwind plugin
alongside the existing framework plugins, and import `tailwindcss` in the actual CSS entrypoint.
Import that stylesheet once through the application's established entry/layout.

```bash
npm install tailwindcss @tailwindcss/vite
```

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
Keep class lists readable with the formatter and optional compatible Tailwind sorting plugin.
Separate logical code blocks with blank lines. Do not add comments to narrate obvious utility classes.

## Build tokens and variants deliberately

Define a restrained scale for spacing, typography, colors, radii, elevation, and content widths.
Separate primitive palette tokens from semantic roles such as surface, text, border, action, danger,
and focus. Theme tokens must reflect the current Tailwind namespaces when utility generation is
intended. Use ordinary CSS custom properties for values that should not create utility families.
Use `@theme inline` when the current documented variable-resolution behavior calls for it.

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
make it clearer. In scoped Vue styles/CSS modules, read the current `@reference` contract before
using Tailwind directives that require shared theme context.

## Source detection is a production contract

Keep full class names in source. Register genuinely external/generated-source locations with the
documented `@source` syntax when automatic detection excludes them. Paths are relative to the
stylesheet for explicit source declarations, and build working directory can affect automatic
discovery. Check monorepos, shared packages, and server templates rather than assuming every file
under the repository is scanned. Use narrow explicit inclusion only when needed. Do not safelist
entire palettes or every possible arbitrary value to hide a broken content model.

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
font/image loading, and layout shifts. Do not claim screenshot review proves accessible interaction.
Run the project's meaningful lint/build/component/browser checks. Update setup and current AGENTS.md
with CSS entrypoints, token/variant ownership, theme strategy, and commands. Deliver readable code,
rendered evidence where available, and specific remaining limits.
