---
name: fastkit-app
description: Build web applications with paulocoutinhox/fastkit using its actual site, admin, API, tenant, service, resource, billing, queue/cache, configuration, and manage.py contracts. Use when creating, extending, or verifying a Fastkit project.
license: MIT
---

# Fastkit App

Use [Fastkit](https://github.com/paulocoutinhox/fastkit) for a Python/FastAPI application that
combines a server-rendered public site, an admin built from resources, and an API. These share
accounts, tenant scope, content, commerce and subscriptions, jobs, and storage. It is a specific
application base. It is not a general instruction to build a separate React frontend and a separate
worker stack.

## Read the real project before extending it

Read the current upstream README, `docs/architecture.md`, the configuration and deployment guides,
the guides for the chosen domain, `pyproject.toml`, and the `manage.py` help. Match the actual
checkout and lockfile, and note important differences. On every new task, read the README for
updated features. Do not blindly copy an older Fastkit architecture or promise an integration that
does not exist. See [sources](references/sources.md).

Confirm the product journeys, chosen surfaces, tenant or global ownership, roles, locales and
markets, how it makes money, file and media needs, outside gateways, and deployment scope. Find out
what already exists and extend it. Do not build a second login, queue, cache, or resource system
next to the existing one. The researched `pyproject.toml` needs Python 3.13 or later, and the README
lists 3.13 and 3.14. The actual manifest and lockfile decide what runs.

## Commands and local bootstrap

Use the existing Python entrypoint through uv. `uv run` installs the locked Python dependencies, so
the Python side needs no separate install step. Set up a throwaway local checkout in this order:

```bash
uv run manage.py
uv run manage.py site-deps
uv run manage.py admin-deps
uv run manage.py seed --yes
uv run manage.py site-build
uv run manage.py admin-build
uv run manage.py start
```

The root help lists the real commands. `uv run manage.py help <command>` lists options. In the
researched setup, the site answers at `http://localhost:8000`, the admin at `/admin`, the API under
`/api`, and the API docs at `/docs`. Check the actual configuration. Report PDF export needs
WeasyPrint's Pango libraries on the host. If they are missing, report that system dependency instead
of changing code.

`seed --yes` rebuilds the local database and fills it with sample data. Run it only in an approved
throwaway environment. Never run it against an existing database without clear confirmation. The
demo admin/admin account is for development only, not for deployment settings. `migrate` creates
missing tables and leaves existing tables alone, so it never adds a column to an existing table.
For that change, run `schema-diff` against a database or dump you are allowed to use, review the
proposal it generates, and give the DDL to the owner of that environment. Do not assume Fastkit
does data migrations.

## Use the existing responsibility map

| Layer/path | Responsibility |
| --- | --- |
| `routes/`, `routes/site/` | HTTP and session input and passing responses on, or site rendering. |
| `schemas/` | Input checks at the boundary, request and response shapes, camelCase/snake_case mapping. |
| `services/` | Domain operations, tenant and role rules, resource declarations. No HTTPException or header access. |
| `models/` | Tables, indexes, relationships. |
| `enums/` | Fixed sets of domain or provider values. |
| `helpers/` | Real shared database, auth, storage, and site infrastructure. |
| `jobs/` | Declared scheduled and background operations. |
| `reports/` | One admin report per file, registered in `reports/registry.py`. |
| `templates/` | Site and email Jinja templates. |
| `webapps/` | Existing site and admin frontend packages. |
| `locale/` | Real API and site translation dictionaries. |
| `config/` | Chosen Python environment configuration. |
| `commands/` | Native manage.py extension commands. |

The researched upstream gives every application class and enum its own `snake_case` module, such as
`models/product.py`, `schemas/product_schema.py`, and `services/product_service.py`. Imports name the
module that defines the item, and package `__init__.py` files stay empty. Routes stay grouped by
HTTP surface, each command has its own module, and each Vue component or view has its own file.
Follow that rule in new code. Before you split a file with many classes in the target checkout,
update every import and discovery path. Keep views, services, transport, models, and real reusable
helpers separate, without adding architecture layers you do not need yet.

## Implement a resource through its real contracts

Look at a current similar model, schema, service, route registration, and admin resource definition.
The researched upstream checklist adds a resource in this order:

1. A new enum in `enums/<enum_name>.py`, alone in its module.
2. The table in `models/<model_name>.py`, then its import and `__all__` entry in `models/registry.py`.
   Without that registry entry, the table is never created.
3. Separate schema modules in `schemas/` for the read schema, `Create`, and `Update` shapes.
4. The service in `services/<model_name>_service.py`, extending the correct base, with its instance
   at the end of the module.
5. Routes in `routes/<module>.py` through `build_router(...)`, registered in `helpers/router.py`.
6. The admin definition in `webapps/admin/src/resources/<section>.js`, registered in its `index.js`.
7. Labels in all API and site catalogs under `locale/` and all admin catalogs under
   `webapps/admin/src/i18n/`, then route and service tests plus admin tests for changed behavior.

Declare only supported service attributes: model, roles, search, text-search, filter, and ordering
fields, relations, labels, position, dependents, markup and file fields, and localized key behavior
when it applies. The CRUD factory and admin build their behavior from those declarations. A model
alone does not give you an authorized listing, a working route, or a complete admin form. If the
target checkout's own AGENTS.md or a similar resource differs from this list, follow the checkout
and report the difference.

Trace how resources are registered. Do not make up a filename or decorator. Reuse the real upload
purposes, storage key ownership, localized reader schemas, and client URL lookup. Public clients get
the intended UUIDs and resolved asset addresses under the documented contract. Opaque IDs do not
replace object and tenant authorization. Check list, detail, lookup, update, delete, and reorder
across users, roles, tenants, global rows, and locale fallback. Hiding an admin button does not
secure its endpoint.

For example, a localized gallery for customers needs its model and a valid upload purpose, admin
schema, service, and resource registration, a reader schema with resolved image URLs, route access,
translation labels, and tests for which tenant and language win. Do not add another hand-built admin
screen if the resource model already supports the need.

## Configuration, sessions, jobs, and commerce

`APP_ENV`, `dev` by default, chooses the Python configuration module `config/<env>.py`. Nothing
under `config/` reads other environment variables. Keep that settings design. Do not quietly add a
`.env` system. The published `stage` and `prod` modules contain placeholder secrets, and production
refuses to start while a `change-me` marker is still there. Put real secrets into the private
installation's configuration through the approved deployment process, and keep that material out of
Git and build output. Do not change an environment just because a help text or example uses
production.

The site keeps its signed session token in an `httponly` cookie. Admin and API send it as a bearer
token. In the researched code the token does not expire on its own. Account status ends access, and
a password change ends the other sessions. Understand CSRF for changes made with cookie login,
tenant lookup, account lifecycle, and role checks. Do not add or promise token expiry that the
current project does not have. Keep request and background resource scopes separate.

In the researched architecture, Queuefy and Cachefy use the application database. Workers run
inside the application process, with no broker, worker process, or scheduler daemon. Reuse the
existing setup, lifespan, and job declarations. `uv run manage.py run-delivery` runs one delivery
pass by hand. Do not add a broker, scheduler daemon, Redis service, or second cache by default.
Queue claims do not make business effects happen exactly once. Define durable operation IDs for
delivery and payment. Development leaves the cache off, so local runs do not test cache staleness.
In stage and production, cached results are cleared only when they expire. An admin write does not
clear them. Check how much staleness is acceptable before you
change it.

For billing, tell apart plans, entitlements, benefits, grants, products, purchases, currencies,
gateway integrations, and real provider identities. Follow the existing gateway contracts and their
handling of duplicate requests and checks against provider records. Choose providers explicitly,
with no catch-all for unknown providers. Check authentication, webhook authenticity, duplicate and
out-of-order events, refunds and revocation, and tenant boundaries. Creating an integration is not
the same as publishing a store subscription.

## Add custom commands through manage.py

Create a focused Python module in `commands/` with the documented `Command(BaseCommand)` class.
Import `BaseCommand` from `helpers.base_command` and `CommandError` from `helpers.command_error`.
Implement `add_arguments(parser)` where needed, and a sync or `async` `handle(**options)`. Raise
`CommandError` for an expected refusal, which exits with an error status, and write output through
`self.stdout.write`. A module such as `inspect_catalog.py` becomes `inspect-catalog`, and every
command also accepts `--verbosity` and `--traceback`. Do not add shell or JavaScript command
wrappers.

Read existing harmless commands before you build one. Keep parsing, checks, the operation, and
reporting clear. Destructive commands must name the environment and require the real, explicit
confirmation step. Do not run seeding, table recreation, key rotation, or live reconciliation as a
side effect of finding commands. Document options, output, failure status, and authorization.

## Verify the complete feature

Use the real commands that help shows, including:

```bash
uv run manage.py test --coverage
uv run manage.py test -- -k customer
uv run manage.py admin-test
uv run manage.py site-test
```

Run `uv run manage.py lint` to check the backend without writing, and `uv run manage.py format` to
format the backend and both front ends with Ruff and Prettier. Keep the project's wide line width,
which the researched checkout sets to 320 for Ruff and Prettier. Do not make it narrower. Keep each
call on one line, and join wrapped calls. Run the build checks that apply, and look at the real
source and installed assets. A failing check blocks completion. Fix its cause or report the exact
failure. Test denied access from other tenants, role checks, input limits, paging, file ownership,
locale choice, background work, cache visibility, and the site, admin, and API code affected. A
database test that passes on SQLite alone does not prove MySQL/PostgreSQL behavior for numbers,
collation, or concurrency. Keep finite outside deadlines and visible error contracts. Do not claim
that upstream coverage proves this new feature.

Deliver code, resource and configuration changes, the current architecture and commands in
AGENTS.md, real local evidence, and what still needs outside setup. Build and deployment are
separate stages that each need approval. The skill is descriptive. Change its stored framework
knowledge only when the user asks.
