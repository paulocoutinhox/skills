# Tailwind design-system decisions

## What should become shared

A reusable button combines semantic interaction, focus/disabled/pending states, and a bounded visual
API. Its variant map owns complete generated classes. A feature container owns layout appropriate
to that feature. Do not extract wrappers that merely rename a handful of classes unless they hide a
stable product rule. Do not let a global style rewrite every feature element through broad selectors.

Use semantic tokens to make a product-level change local. Repeated arbitrary colors, widths, and
shadows that mean the same thing indicate a missing shared decision. A one-off chart position is not
automatically a design token. Avoid infinite variant combinations and choose documented component
contracts. Apply class-merging utilities only where override semantics need them.

## CSS and utility boundaries

Use framework components for reusable UI responsibilities and ordinary CSS for appropriate selector
relationships, external widgets, or readable bespoke effects. Keep token definitions, generated
utilities, base rules, and feature overrides distinct. Understand cascade layers and specificity before
adding `!important`. Do not use global overrides to compensate for a component's unclear API.

## Production checks

Check shared-package class discovery, server-template paths, theme values and variants, actual font
availability, dynamic CSS variables, focus visibility, contrast, overflow, and long content after a
production build. Confirm the supported browser target against the installed major. Screenshot
comparison can detect layout differences but cannot prove form labels, tab order, or correct status
announcements. Verify those interactions separately.
