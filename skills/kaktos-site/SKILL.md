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
integrated Vite/Tailwind frontend. The checkout pins Python 3.13 in `.python-version` and Node 22 in
`.nvmrc`. Inspect those files and `requirements.txt` for the actual checkout. Kaktos has no
`pyproject.toml`, so use uv to create an isolated environment and install `requirements.txt`.
Do not replace the framework's entrypoint with a new runner.

Prepare the environment once from the project root. `uv venv` honors `.python-version`:

```bash
uv venv
uv pip install -r requirements.txt
```

Then run the existing Python CLI inside that environment, always from the project root:

```bash
uv run --no-project python kaktos.py
uv run --no-project python kaktos.py build
uv run --no-project python kaktos.py serve
uv run --no-project python kaktos.py serve 8080
```

These invoke the upstream development, production-build, and built-output-server commands. The
original upstream invocations use `python3 kaktos.py` with the same arguments. `--no-project` uses the
discovered `.venv` without looking for a project file. Verify the interpreter uv selected. The build
runs `npm install` in `frontend/` when `node_modules/vite` is missing and then `vite build`. Do not run a
separate npm/Vite dev server as the default workflow because the Python build owns the frontend step.
If npm is missing or the Node version is too old, stop and report the runtime gap.

Development forces debug mode, rebuilds on changes, and serves `build/` with LiveReload on port 5555.
`build` recreates `build/` in production mode. `serve` serves the existing `build/` on port 5555
unless a port argument is given, so run `build` first and stop the development server or choose
another port. `KAKTOS_DEBUG` set to any non-empty value, including `False` or `0`, forces a debug
build. The build also loads a `.env` file, so check there too. Unset it for a production build rather
than assigning a false-looking value. Confirm actual
terminal output, including `environment mode: production`. A successful server start does not prove
every page froze correctly.

## Place each kind of file correctly

| Path | Owns |
| --- | --- |
| `kaktos.py` | Existing command entrypoint. Keep it small. |
| `modules/config.py` | Site/base URL, content paths, output/template settings, and selected data configuration. |
| `modules/routes.py` | Flask routes for pages, blog, products, categories, sitemap, and robots. |
| `modules/commands/` | Native custom Python command modules. |
| `templates/layouts/` | Shared document/page layouts. |
| `templates/pages/` | Actual page templates. |
| `templates/shared/` | Reusable fragments/macros such as header, navigation, footer, and cards. |
| `frontend/src/` | Processed CSS/JS entries, including Tailwind and interaction code. |
| `frontend/public/` | Assets published under `/static/`, including images. |
| `frontend/raw/` | Files copied unchanged to the site root, such as favicon, CNAME, and the web manifest. |
| `extras/config/` | Supplied YAML/content data examples. Inspect the actual loaders before extending them. |
| `build/` | Generated deployable result. Never hand-edit as the source of truth. |

Keep one meaningful UI fragment per template where responsibility warrants it. Put reusable layout
in base templates and macros, content in data/pages, and substantial transformations in Python
modules. Avoid huge inline scripts or duplicating the same navigation/card markup across pages.
Do not assume a new template is frozen merely because it exists.

## Build routes and assets using framework contracts

Inspect `modules/routes.py` and `system.initialize()`, which creates the Flask app and freezer before
importing the routes. The generic `/<path>/` route renders `templates/pages/<path>.html`, so a simple
page needs only its template and a link. Add a dedicated route only for data-driven pages.

Frozen-Flask writes parameterless routes, static files, and every URL produced by `url_for` while
rendering frozen pages. Link pages with `url_for`, such as `url_for('page', path='about')`, never a
hardcoded path. A page or dynamic URL that no frozen page links to needs a Frozen-Flask generator
registered with `system.freezer_app.register_generator` in the routes module. Enumerate actual
blog/product/category and pagination URLs before freezing.

The upstream `sitemap.xml` route lists every `templates/pages/*.html` outside its exclusion set plus
blog, product, and category data, while `robots.txt` is also a route. A sitemap entry can therefore
name a page that was never frozen. After building, confirm each sitemap URL exists in `build/`.
Files in `frontend/raw/` are copied after freezing and overwrite generated files with the same name,
so do not also add `robots.txt` or `sitemap.xml` there. Links to pages that were never generated are
not valid static navigation even if Flask could serve them during development.

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
Read the current dispatcher before adding arguments. The researched dispatcher always passes an empty
mapping, has no automatic CLI-argument parser, and performs no Fastkit-style name conversion. The
command name is the exact module name, so `modules/commands/content_report.py` runs as
`uv run --no-project python kaktos.py content_report`. Read extra arguments from `sys.argv[2:]`, as
the upstream `serve` command reads its port.

```python
import sys

from modules import content_service


def run(params):
    arguments = sys.argv[2:]
    report = content_service.inspect(arguments)

    print(report)
```

The `content_service` module is application-owned. Keep validation, operation, and reporting
separate. Avoid mutable default dictionaries. The dispatcher reports any `ModuleNotFoundError`,
including a missing import inside the command, as `Command '<name>' not found` and exits with status
10 through pygemstones `log.e`. When that message appears for an existing file, import the module
directly to see the real error. `serve` also exits with status 10 when `build/` is missing. Document the
invocation and result, and preserve useful failures. Do not modify the upstream CLI or create command
wrappers just to show activity. Explain the current extension mechanism and implement a command only
within scope.

Deliver editable site sources, actual local commands, architecture/configuration in AGENTS.md,
build evidence, and unresolved external integrations. This skill contains no generated site or
automation itself. Maintaining the skill's stored facts requires an explicit user request.
