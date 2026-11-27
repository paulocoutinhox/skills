# Tailwind design-system decisions

## What should become shared

A reusable button combines semantic interaction, focus/disabled/pending states and a small visual
API. Its variant map owns the complete generated classes. A feature container owns the layout that
fits that feature. Do not extract wrappers that only rename a few classes, unless they hide a stable
product rule. Do not let a global style rewrite every feature element through broad selectors.

Use semantic tokens so a product-wide change happens in one place. Repeated arbitrary colors, widths
and shadows that mean the same thing show a missing shared decision. A one-off chart position is not
a design token just because it exists. Avoid endless variant combinations and choose documented
component contracts. Use class-merging utilities only where override rules need them.

## CSS and utility boundaries

Use framework components for reusable UI responsibilities. Use plain CSS for selector relationships
that fit CSS, external widgets, or custom effects that read better as CSS. Keep token definitions,
generated utilities, base rules and feature overrides apart. Understand cascade layers and
specificity before adding `!important`. Do not use global overrides to make up for a component's
unclear API.

## Production checks

After a production build, check class discovery in shared packages, server-template paths, theme
values and variants, real font availability, dynamic CSS variables, focus visibility, contrast,
overflow and long content. Confirm that the supported browser target meets the v4 minimum.
Screenshot comparison can find layout differences. It cannot prove form labels, tab order or
correct status announcements. Check those interactions separately.
