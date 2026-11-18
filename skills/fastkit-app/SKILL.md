---
name: fastkit-app
description: Build web applications with paulocoutinhox/fastkit using its actual site, admin, API, tenant, service, resource, billing, queue/cache, configuration, and manage.py contracts. Use when creating, extending, or verifying a Fastkit project.
license: MIT
---

# Fastkit App

Use [Fastkit](https://github.com/paulocoutinhox/fastkit) for a Python/FastAPI application combining
a server-rendered public site, resource-driven admin, and API, with shared accounts, tenant scope,
content, commerce/subscriptions, jobs, and storage. It is a specific application foundation, not a
generic instruction to create a separate React frontend and independent worker stack.

## Read the real project before extending it

Read the current upstream README, `docs/architecture.md`, configuration/deployment guides, selected
domain guides, `pyproject.toml`, and `manage.py` help. Match the actual checkout/lockfile and record
consequential differences. Read updated features from the README on every new operational task.
Do not blindly copy an older Fastkit architecture or promise an absent integration. See
[sources](references/sources.md).

Confirm product journeys, selected surfaces, tenant/global ownership, roles, locales/markets,
monetization, file/media needs, external gateways, and deployment scope. Determine which capabilities
already exist and extend them. Do not rebuild login, queue, cache, or the resource system in parallel.
The researched `pyproject.toml` requires Python 3.13 or later, and the README advertises 3.13 and 3.14.
The actual manifest/lockfile governs execution.

## Commands and local bootstrap

Use the existing Python entrypoint through uv. `uv run` installs the locked Python dependencies, so
the Python side needs no separate install step. Bootstrap a disposable local checkout in this order:

```bash
uv run manage.py
uv run manage.py site-deps
uv run manage.py admin-deps
uv run manage.py seed --yes
uv run manage.py site-build
uv run manage.py admin-build
uv run manage.py start
```

The root help lists actual commands. `uv run manage.py help <command>` lists options. The researched
site answers at `http://localhost:8000`, the admin at `/admin`, the API under `/api`, and API
documentation at `/docs`. Inspect actual configuration. Report PDF export needs WeasyPrint's Pango
libraries on the host. If they are missing, report that system dependency rather than changing code.

`seed --yes` rebuilds the local database and populates sample data. Run it only against an approved
disposable environment, never an existing database without explicit confirmation. The demo admin/admin
account is development-only, not deployment configuration. `migrate` creates missing tables and leaves
existing tables untouched, so it never adds a column to a populated table. For that change, run
`schema-diff` against an authorized database or dump, review the generated proposal, and hand the
DDL to the owner of that environment. Do not assume Fastkit performs data migrations.

## Use the existing responsibility map

| Layer/path | Responsibility |
| --- | --- |
| `routes/`, `routes/site/` | HTTP/session input and response delegation, or site rendering. |
| `schemas/` | Boundary validation, request/response shapes, camelCase/snake_case mapping. |
| `services/` | Domain operations, tenant/role rules, resource declarations. No HTTPException/header access. |
| `models/` | Tables, indexes, relationships. |
| `enums/` | Closed domain/provider sets. |
| `helpers/` | Actual shared database/auth/storage/site infrastructure. |
| `jobs/` | Declared scheduled/background operations. |
| `reports/` | One admin report per file, registered in `reports/registry.py`. |
| `templates/` | Site and email Jinja templates. |
| `webapps/` | Existing site/admin frontend packages. |
| `locale/` | Actual API/site translation dictionaries. |
| `config/` | Selected Python environment configuration. |
| `commands/` | Native manage.py extension commands. |

The researched upstream gives every application class and enum its own `snake_case` module, such as
`models/product.py`, `schemas/product_schema.py`, and `services/product_service.py`. Imports name the
defining module directly, and package `__init__.py` files stay empty. Routes stay grouped by HTTP
surface, each command has its own module, and each Vue component/view has its own file. Follow that
rule in new code. Before splitting an older multi-class file in the target checkout, update every
import and discovery path. Keep views, services, transport, models, and actual reusable helpers
separate without adding speculative architecture layers.

## Implement a resource through its real contracts

Inspect a current analogous model, schema, service, route registration, and admin resource definition.
The researched upstream checklist adds a resource in this order:

1. A new enum in `enums/<enum_name>.py`, alone in its module.
2. The table in `models/<model_name>.py`, then its import and `__all__` entry in `models/registry.py`.
   Without that registry entry, the table is never created.
3. Separate schema modules in `schemas/` for the read schema, `Create`, and `Update` shapes.
4. The service in `services/<model_name>_service.py`, extending the correct base, with its instance
   at the end of the module.
5. Routes in `routes/<module>.py` through `build_router(...)`, registered in `helpers/router.py`.
6. The admin definition in `webapps/admin/src/resources/<section>.js`, registered in its `index.js`.
7. Labels in all API/site catalogs under `locale/` and all admin catalogs under
   `webapps/admin/src/i18n/`, then route and service tests plus admin tests for changed behavior.

Declare only supported service attributes: model, roles, search/text-search/filter/ordering fields,
relations, labels, position, dependents, markup/file fields, and localized key behavior when
applicable. The CRUD factory and admin derive behavior from those declarations. A model alone does
not make an authorized listing, a working route, or a complete admin form. If the target checkout's
own AGENTS.md or analogous resource differs from this list, follow the checkout and report the difference.

Trace resource registration rather than inventing a filename or decorator. Reuse actual upload
purposes, storage key ownership, localized reader schemas, and client URL resolution. Public clients
receive intended UUIDs/resolved asset addresses under the documented contract. Opaque IDs do not
replace object/tenant authorization. Verify list/detail/lookup/update/delete/reorder across users,
roles, tenants, global rows, and locale fallback. A hidden admin button does not secure its endpoint.

For example, a localized customer-facing gallery needs its model and valid upload purpose, admin
schema/service/resource registration, a reader schema with resolved image URLs, route access,
translation labels, and tests for tenant/language precedence. Do not add another hand-built admin
screen if the resource model already supports the requirement.

## Configuration, sessions, jobs, and commerce

`APP_ENV`, `dev` by default, selects the Python configuration module `config/<env>.py`. Nothing under
`config/` reads other environment variables. Preserve that settings architecture instead of silently
adding a `.env` system. Published `stage` and `prod` modules contain placeholder secrets, and
production refuses to start while a `change-me` marker remains. Fill real secrets into the private
installation's configuration through the authorized deployment process, and exclude that material
from Git and build artifacts. Do not change an environment merely
because a help/example uses production.

The site keeps its signed session token in an `httponly` cookie. Admin/API send it as a bearer token.
In the researched implementation the token does not expire on its own. Account status ends access,
and a password change ends the other sessions. Understand CSRF for cookie-authenticated mutations,
tenant resolution, account lifecycle, and role checks. Do not add or promise token expiry that the
current project does not implement. Keep request and background resource scopes separate.

Queuefy and Cachefy use the application database in the researched architecture. Workers run inside
the application process, with no broker, worker process, or scheduler daemon. Reuse the existing
composition/lifespan and job declarations. `uv run manage.py run-delivery` runs one delivery pass by
hand. Do not add a broker, scheduler daemon, Redis service, or second cache by default. Queue claims
do not make business effects exactly once. Define durable operation identities for delivery/payment.
Development leaves the cache off, so local runs do not exercise cache staleness. Stage and production
cache assembled answers with expiry as the only invalidation rule, not automatic invalidation on
every admin write. Verify acceptable staleness before changing it.

For billing, distinguish plans, entitlements, benefits, grants, products, purchases, currencies,
gateway integrations, and actual provider identities. Follow existing gateway contracts and
idempotency/reconciliation. Use explicit provider selection, no unknown-provider catch-all. Check
authentication, webhook authenticity, duplicate/out-of-order events, refund/revocation, and tenant
boundaries. Do not treat creating an integration as publishing a store subscription.

## Add custom commands through manage.py

Create a focused Python module in `commands/` with the documented `Command(BaseCommand)` class,
importing `BaseCommand` from `helpers.base_command` and `CommandError` from `helpers.command_error`.
Implement `add_arguments(parser)` where needed and a synchronous or `async` `handle(**options)`.
Raise `CommandError` for expected refusal, which exits with an error status, and write output through
`self.stdout.write`. A module such as `inspect_catalog.py` becomes `inspect-catalog`, and every
command also accepts `--verbosity` and `--traceback`. Do not add shell/JavaScript command wrappers.

Read existing harmless commands before implementing. Keep parsing, validation, operation, and
reporting clear. Destructive commands must identify the environment and require the actual explicit
confirmation contract. Do not execute seeding, table recreation, key rotation, or live reconciliation
as a side effect of discovering commands. Document options, output, failure status, and authorization.

## Verify the complete feature

Use the real commands selected by help, including:

```bash
uv run manage.py test --coverage
uv run manage.py test -- -k customer
uv run manage.py admin-test
uv run manage.py site-test
```

Run `uv run manage.py lint` to check the backend without writing, and `uv run manage.py format` to
format the backend and both front ends with Ruff and Prettier. Keep the project's configured wide
line width, which the researched checkout sets to 320 for Ruff and Prettier. Do not narrow it, keep
each call on one line, and join wrapped calls. Run applicable build checks and inspect actual
source/installed assets. A failing check blocks completion. Fix its cause or report the exact
failure. Test negative tenant access, role enforcement, input bounds, paging, file ownership, locale selection, background work,
cache visibility, and affected site/admin/API consumers. Database acceptance on SQLite alone does
not prove MySQL/PostgreSQL numeric/collation/concurrency behavior. Preserve finite external deadlines
and observable error contracts. Do not claim upstream coverage proves this new feature.

Deliver code, resource/configuration changes, current architecture/commands in AGENTS.md, actual
local evidence, and external setup boundaries. Build and deployment are separate authorized stages.
The skill is descriptive. Only the user requests updates to its stored framework knowledge.
