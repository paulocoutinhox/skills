---
name: kaktos-site
description: Create and maintain local static websites with paulocoutinhox/kaktos. Use for Jinja pages, blogs, catalogs, landing pages, integrated frontend assets, frozen routes, builds, and custom Python commands.
license: MIT
---

# Kaktos Site

Use [Kaktos](https://github.com/paulocoutinhox/kaktos) for a static site generated locally from
Python, Jinja templates, and content data. It fits blogs, portfolios, landing pages, and static
catalog/storefront presentation. The generated site needs no Python server at request time.
Payments, accounts, order processing, private data, and form delivery still need real external or
backend services. Static output does not make those capabilities free, secure, or already implemented.

## Inspect the current framework first

Read the current upstream README, requirements, configuration, command dispatcher, route examples,
and frontend manifest before changing a project. Compare the target checkout with the documented
features and pin/record the actual revision. If docs and code differ, inspect the relevant definition
and report the difference. Do not tell the user to run imaginary commands or assume old asset paths.
See [sources](references/sources.md).

Collect audience, site type, page/URL inventory, language/locales, content source, design, SEO needs,
required interactions, and local-versus-deployment scope. Decide whether the output is truly static.
Do not introduce a database/server or SPA framework without a requirement that justifies it.

## Requirements and commands

The researched README specifies Python 3.9+ and Node 20.19+ or 22.12+, with npm on PATH and an
integrated Vite/Tailwind frontend. Inspect current pinned runtime files and requirements for the
actual checkout. Use uv to create an isolated Python environment and install `requirements.txt`.
Do not replace the framework's entrypoint with a new runner.

Run the existing Python CLI inside that environment:

```bash
uv run --no-project python kaktos.py
uv run --no-project python kaktos.py build
uv run --no-project python kaktos.py serve
```

These invoke the upstream development, production-build, and built-output-server commands through
uv. First create `.venv` with `uv venv` and install dependencies with
`uv pip install -r requirements.txt`. Verify the interpreter/environment selected by uv. The original
upstream invocations use `python3 kaktos.py` with the same arguments. Do not run a separate npm/Vite
dev server as the default workflow because the Python build owns the frontend step.

Development forces debug mode and serves the generated site with LiveReload. Production writes
`build/`. `KAKTOS_DEBUG` changes build behavior, so inspect the effective environment rather than
accidentally producing a debug deployment. The researched local server uses port 5555. Confirm actual
terminal output. A successful server start does not prove every page froze correctly.

## Place each kind of file correctly

| Path | Owns |
| --- | --- |
| `kaktos.py` | Existing command entrypoint. Keep it small. |
| `modules/config.py` | Site/base URL, content paths, output/template settings, and selected data configuration. |
| `modules/routes/` | Flask route enumeration used during freezing, following current examples. |
| `modules/commands/` | Native custom Python command modules. |
| `templates/layouts/` | Shared document/page layouts. |
| `templates/pages/` | Actual page templates. |
| `templates/shared/` | Reusable fragments/macros such as header, navigation, footer, and cards. |
| `frontend/src/` | Processed CSS/JS entries, including Tailwind and interaction code. |
| `frontend/public/` | Assets published under `/static/`, including images. |
| `frontend/raw/` | Files copied unchanged to the site root, such as robots, favicon, and CNAME. |
| `extras/config/` | Supplied YAML/content data examples. Inspect the actual loaders before extending them. |
| `build/` | Generated deployable result. Never hand-edit as the source of truth. |

Keep one meaningful UI fragment per template where responsibility warrants it. Put reusable layout
in base templates and macros, content in data/pages, and substantial transformations in Python
modules. Avoid huge inline scripts or duplicating the same navigation/card markup across pages.
Do not assume a new template is discoverable without a route/freezer generator.

## Build routes and assets using framework contracts

Inspect the current route modules and their initialization. Add each static route and required
dynamic URL generator in the established registration path. Enumerate actual blog/product/category
and pagination URLs before freezing. Links to pages that were never generated are not valid static
navigation even if Flask could serve them during development.

Use `kaktos.frontend` in Jinja instead of hardcoded hashed names or a second static path system:

```jinja
{{ kaktos.frontend.styles_all() }}
<img src="{{ kaktos.frontend.url('images/cover.png') }}" alt="Publication cover">
<link rel="icon" href="{{ kaktos.frontend.root_url('favicon.ico') }}">
{{ kaktos.frontend.scripts_all() }}
```

`url` resolves `frontend/public/` assets. `root_url` resolves raw root files. `abs_url` uses the actual
base URL for social sharing. Per-entry `styles_for` and `script_for` are available for intentional
split layouts. Store YAML asset paths relative to `frontend/public/`, then resolve them through the
helper. `frontend/raw/` is copied as-is, so never place secrets, source maps with private data,
environment files, or internal notes there.

## Content, accessibility, and local verification

Create semantic headings, landmarks, labels, descriptive links, image alternatives, accessible
navigation/focus, responsive layouts, and appropriate loading/error states for browser interactions.
Keep layout readable with localized/long content and proportional images. Use actual page titles,
descriptions, canonical URLs, social image addresses, sitemap/robots, and structured data only where
supported by real content. Confirm production base URL, HTTPS, paths, trailing slashes, and any
subpath hosting assumptions. A static form does not send mail without an explicit service contract.

Run a production build and serve that output. Inspect every page type, pagination boundary, missing
content/image behavior, navigation, keyboard usage, narrow/wide layouts, and browser console/network
errors. Confirm output links and asset references resolve independently of the development server.
Do not mistake LiveReload throttling for a missing build. Invalid Jinja or data errors need fixing
at their source. Publish only the intended build result if deployment is authorized.

## Add a native command only when requested

Kaktos imports `modules.commands.<command>` and calls its `run` function with a parameter mapping.
A custom Python command therefore belongs in `modules/commands/`, not an unrelated shell script.
Read the current dispatcher before adding arguments. The researched dispatcher passes a mapping
but does not provide a general automatic CLI-argument parser or Fastkit-style name conversion.

```python
def run(params):
    report = content_service.inspect(params)

    print(report)
```

The service is application-owned. Keep validation, operation, and reporting separate. Avoid mutable
default dictionaries. Use actual module naming/dispatch rules, document the invocation and result,
and preserve useful failures. Do not modify the upstream CLI or create command wrappers just to
show activity. Explain the current extension mechanism and implement a command only within scope.

Deliver editable site sources, actual local commands, architecture/configuration in AGENTS.md,
build evidence, and unresolved external integrations. This skill contains no generated site or
automation itself. Maintaining the skill's stored facts requires an explicit user request.
