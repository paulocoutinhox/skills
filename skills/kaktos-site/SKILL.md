---
name: kaktos-site
description: Create and maintain local static websites with paulocoutinhox/kaktos. Use for Jinja pages, blogs, catalogs, landing pages, built-in frontend assets, frozen routes (pages saved as static files), builds, and custom Python commands.
license: MIT
---

# Kaktos Site

Use [Kaktos](https://github.com/paulocoutinhox/kaktos) for a static site built locally from Python,
Jinja templates, and content data. It fits blogs, portfolios, landing pages, and static catalog or
storefront pages. The built site needs no Python server when people visit it. Payments, accounts,
order processing, private data, and form delivery still need real outside or backend services. A
static site does not make those features free, secure, or already built.

## Inspect the current framework first

Before you change a project, read the current upstream README, requirements, configuration, command
dispatcher, route examples, and frontend manifest. Compare the target checkout with the documented
features, and pin or note the actual revision. If the docs and the code differ, read the related
definition and report the difference. Do not tell the user to run commands that do not exist or
assume old asset paths. See [sources](references/sources.md).

Collect the audience, site type, list of pages and URLs, languages and locales, content source,
design, SEO needs, needed interactions, and whether the work is local only or includes deployment.
Decide whether the output is really static. Do not add a database, server, or SPA framework unless
a real need justifies it.

## Requirements and commands

The researched README needs Python 3.10+ and Node 20.19+ or 22.12+, with Node 24 LTS recommended,
npm on PATH and a built-in Vite/Tailwind frontend. The checkout pins Python 3.14 in
`.python-version` and Node 24 in `.nvmrc`.
Check those files and `requirements.txt` in the actual checkout. Kaktos has no `pyproject.toml`, so
use uv to create a separate environment and install `requirements.txt`. Do not replace the
framework's entrypoint with a new runner.

Set up the environment once from the project root. `uv venv` follows `.python-version`:

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

These run the upstream commands for development, the production build, and serving the built
output. The original upstream commands use `python3 kaktos.py` with the same arguments.
`--no-project` uses the `.venv` it finds without looking for a project file. Check which interpreter
uv picked. The build runs `npm install` in `frontend/` when `node_modules/vite` is missing, and then
`vite build`. Do not run a separate npm/Vite dev server as the default workflow, because the Python
build owns the frontend step. If npm is missing or the Node version is too old, stop and report what
is missing.

Development always uses debug mode, rebuilds on changes, and serves `build/` with LiveReload on port
5555. `build` recreates `build/` in production mode. `serve` serves the existing `build/` on port
5555 unless you give a port argument. So run `build` first, and stop the development server or pick
another port. Setting `KAKTOS_DEBUG` to any non-empty value, including `False` or `0`, forces a
debug build. The build also loads a `.env` file, so check there too. For a production build, unset
it. Do not set it to a value that only looks false. Confirm the real terminal output, including
`environment mode: production`. A server that starts does not prove that every page froze
correctly.

## Place each kind of file correctly

| Path | Owns |
| --- | --- |
| `kaktos.py` | The existing command entrypoint. Keep it small. |
| `modules/config.py` | Site and base URL, content paths, output and template settings, and chosen data settings. |
| `modules/routes.py` | Flask routes for pages, blog, products, categories, sitemap, and robots. |
| `modules/commands/` | Native custom Python command modules. |
| `templates/layouts/` | Shared document and page layouts. |
| `templates/pages/` | The real page templates. |
| `templates/shared/` | Reusable fragments and macros such as header, navigation, footer, and cards. |
| `frontend/src/` | Processed CSS and JS entries, including Tailwind and interaction code. |
| `frontend/public/` | Assets published under `/static/`, including images. |
| `frontend/raw/` | Files copied unchanged to the site root, such as favicon, CNAME, and the web manifest. |
| `extras/config/` | Sample YAML and content data. Read the real loaders before you extend them. |
| `build/` | The generated result you deploy. Never edit it by hand as the source of truth. |

Keep one meaningful UI fragment per template where it has its own job. Put reusable layout in base
templates and macros, content in data and pages, and larger transformations in Python modules.
Avoid huge inline scripts, and do not copy the same navigation or card markup across pages. Do not
assume a new template is frozen just because it exists.

## Build routes and assets using framework contracts

Read `modules/routes.py` and `system.initialize()`, which creates the Flask app and the freezer
before it imports the routes. The generic `/<path>/` route renders `templates/pages/<path>.html`,
so a simple page needs only its template and a link. Add a dedicated route only for pages built from
data.

Frozen-Flask writes routes without parameters, static files, and every URL that `url_for` produces
while frozen pages render. Link pages with `url_for`, such as `url_for('page', path='about')`, never
a hardcoded path. A page or dynamic URL that no frozen page links to needs a Frozen-Flask generator,
registered with `system.freezer_app.register_generator` in the routes module. List the real blog,
product, category, and pagination URLs before freezing.

The upstream `sitemap.xml` route lists every `templates/pages/*.html` outside its exclusion list,
plus blog, product, and category data. `robots.txt` is also a route. So a sitemap entry can name a
page that was never frozen. After the build, confirm that each sitemap URL exists in `build/`.
Files in `frontend/raw/` are copied after freezing and overwrite generated files with the same
name, so do not also add `robots.txt` or `sitemap.xml` there. Links to pages that were never
generated are not valid static links, even if Flask could serve them during development.

Use `kaktos.frontend` in Jinja. Do not use hardcoded hashed names or a second static path system:

```jinja
{{ kaktos.frontend.styles_all() }}
<img src="{{ kaktos.frontend.url('images/cover.png') }}" alt="Publication cover">
<link rel="icon" href="{{ kaktos.frontend.root_url('favicon.ico') }}">
{{ kaktos.frontend.scripts_all() }}
```

`url` finds `frontend/public/` assets. `root_url` finds raw root files. `abs_url` uses the real base
URL for social sharing. `styles_for` and `script_for` for single entries are there for layouts that
are split on purpose. Store YAML asset paths relative to `frontend/public/`, then look them up
through the helper. `frontend/raw/` is copied as it is, so never put secrets, source maps with
private data, environment files, or internal notes there.

## Content, accessibility, and local verification

Create semantic headings, landmarks, labels, clear link text, image alt text, accessible navigation
and focus, responsive layouts, and fitting loading and error states for browser interactions. Keep
the layout readable with translated or long content and images in proportion. Use real page titles,
descriptions, canonical URLs, social image addresses, sitemap and robots, and structured data only
where real content supports them. Confirm the production base URL, HTTPS, paths, trailing slashes,
and any plan to host under a subpath. A static form does not send mail unless a real service is set
up for it.

Run a production build and serve that output. Check every page type, the edges of pagination,
behavior with missing content or images, navigation, keyboard use, narrow and wide layouts, and
browser console and network errors. Confirm that output links and asset references work without
the development server. Do not mistake LiveReload throttling for a missing build. Fix invalid Jinja
or data errors where they come from. If deployment is approved, publish only the intended build
result.

## Add a native command only when requested

Kaktos imports `modules.commands.<command>` and calls its `run` function with a parameter mapping.
So a custom Python command belongs in `modules/commands/`, not in an unrelated shell script. Read
the current dispatcher before you add arguments. The researched dispatcher always passes an empty
mapping, has no automatic CLI argument parser, and does no Fastkit-style name conversion. The
command name is the exact module name, so `modules/commands/content_report.py` runs as
`uv run --no-project python kaktos.py content_report`. Read extra arguments from `sys.argv[2:]`,
the same way the upstream `serve` command reads its port.

```python
import sys

from modules import content_service


def run(params):
    arguments = sys.argv[2:]
    report = content_service.inspect(arguments)

    print(report)
```

The `content_service` module belongs to the application. Keep checks, the operation, and reporting
separate. Avoid mutable default dictionaries. The dispatcher reports any `ModuleNotFoundError`,
including a missing import inside the command, as `Command '<name>' not found`, and exits with
status 10 through pygemstones `log.e`. When that message appears for a file that exists, import the
module directly to see the real error. `serve` also exits with status 10 when `build/` is missing.
Document how to run the command and what it returns, and keep useful failures visible. Do not change
the upstream CLI or create command wrappers just to show activity. Explain the current extension
method, and build a command only when it is in scope.

Deliver editable site sources, the real local commands, architecture and configuration in
AGENTS.md, build evidence, and the outside integrations still open. This skill contains no generated
site or automation itself. Changing the skill's stored facts needs a clear request from the user.
