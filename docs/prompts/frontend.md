# Frontend applications prompts

Vue and React apps and Tailwind CSS interfaces. Read [how to use the prompts](../task-prompts.md)
before you copy one.

## Vue application

```text
Use vue-app from paulocoutinhox/skills.
Read [SKILLS_ROOT]/vue-app/SKILL.md and the references that apply. Name the path really loaded, or say it is missing.

Create or grow [VUE_APP_OR_FEATURE] in [REPOSITORY].
Language, rendering mode, framework/toolchain, browser targets, and design: [CONTEXT].
User journeys, routes, API contracts, and acceptance criteria: [REQUIREMENTS].

Use focused feature components, composables, services, and domain rules. Make it clear which part
owns route setup, draft, URL, server, and shared state. Add Pinia only where real shared state needs
it. Handle forms, accessible errors and focus, cancellation, stale responses, and cleanup.
Keep code readable, with one component per file. Run the type, lint, component, browser and build
checks that fit. Document the current structure and commands. Report the real results and any
inputs still needed.
```

## React application

```text
Use react-app from paulocoutinhox/skills.
Read [SKILLS_ROOT]/react-app/SKILL.md and the references that apply. Name the path really loaded, or say it is missing.

Create or grow [REACT_APP_OR_FEATURE] in [REPOSITORY].
Language, rendering mode, framework/toolchain, browser targets, and design: [CONTEXT].
User journeys, routes, API contracts, and acceptance criteria: [REQUIREMENTS].

Use focused components, hooks, services, and domain rules. Make it clear which part owns draft, URL,
server, and shared state. Use effects to sync with outside systems, with real cleanup. Do not use
them to copy state that can be computed. Handle accessible forms and errors, stale fetch and save
responses, and safe repeats of an operation where needed. Avoid giant hooks, stores built "just in
case", and extra layers you do not need. Run the type, lint, behavior, browser and build checks that
fit. Document the current structure, commands, and real results.
```

## Tailwind interface

```text
Use tailwind-css from paulocoutinhox/skills.
Read [SKILLS_ROOT]/tailwind-css/SKILL.md and the references that apply. Name the path really loaded, or say it is missing.

Implement [INTERFACE] in [REPOSITORY] with [FRAMEWORK].
Brand/tokens, supported browsers, themes, responsive contexts, and required states: [BRIEF].

Look at how Tailwind is really set up. Use clear semantic tokens, focused components, small fixed
maps of variant classes, and a clear owner for each piece of CSS. Check that production finds every
class and every outside source path. Use semantic HTML, labels, keyboard and focus behavior, and a
readable responsive layout. Check long content, translations, dark mode, zoom, and the production
CSS. Deliver clear code and notes on structure and setup, with real visual, interaction and build
evidence. Use only the current v4 setup.
```
