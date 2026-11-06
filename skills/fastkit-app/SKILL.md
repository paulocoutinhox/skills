---
name: fastkit-app
description: Build web applications with paulocoutinhox/fastkit using its actual site, admin, API, tenant, service, resource, billing, queue/cache, configuration, and manage.py contracts.
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
The researched baseline advertises Python 3.13/3.14. The actual manifest/lockfile governs execution.

## Commands and local bootstrap

Use the existing Python entrypoint through uv:

```bash
uv run manage.py
uv run manage.py site-deps
uv run manage.py admin-deps
uv run manage.py site-build
uv run manage.py admin-build
uv run manage.py start
```

The root help lists actual commands. `uv run manage.py help <command>` lists options. The researched
local site/API/admin share port 8000, with `/docs` for API documentation. Inspect actual configuration.
`uv run manage.py seed --yes` rebuilds a local database and populates sample data. Run it only against
an approved disposable environment. The demo admin/admin account is development-only, not deployment
configuration. `migrate` creates the declared schema under the current implementation. Do not assume
it performs arbitrary safe destructive schema evolution or data migrations.

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
| `templates/` | Site and email Jinja templates. |
| `webapps/` | Existing site/admin frontend packages. |
| `locale/` | Actual API/site translation dictionaries. |
| `config/` | Selected Python environment configuration. |
| `commands/` | Native manage.py extension commands. |

The upstream groups several symbols by domain. The owner's preference is one class/enum/
component per application-owned file. Apply that preference coherently to new code and update imports
and discovery when splitting affected files. Do not misrepresent the upstream layout as already using
that rule or rename framework modules without checking every caller. Keep views, services, transport,
models, and actual reusable helpers separate without adding speculative architecture layers.

## Implement a resource through its real contracts

Inspect a current analogous model, schema, service, route registration, and admin resource definition.
Add the table/constraints and the appropriate schemas. Extend the correct service base and declare
only supported attributes: model, roles, search/text-search/filter/ordering fields, relations, labels,
position, dependencies, markup/file fields, and localized key behavior when applicable.
The CRUD factory and admin derive behavior from those declarations. A model alone does not make an
authorized listing, a working route, or a complete admin form.

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

`APP_ENV` selects the environment file. Preserve Fastkit's real settings architecture instead of
silently adding a second `.env` system. Published config shapes contain placeholders, not deployable
production secrets. Supply secrets through the authorized deployment/configuration process and
exclude real private material from Git and build artifacts. Do not change an environment merely
because a help/example uses production.

The site uses signed-cookie sessions. Admin/API use their documented bearer-token contract.
Understand revocation/password-change behavior, CSRF for cookie-authenticated mutations, tenant
resolution, account lifecycle, and role checks. Do not invent token expiry behavior that the current
project does not implement. Keep request and background resource scopes separate.

Queuefy and Cachefy use the application database in the researched architecture. Reuse their existing
composition/lifespan and job declarations. Do not add a broker, scheduler daemon, Redis service, or
second cache by default. Queue claims do not make business effects exactly once. Define durable
operation identities for delivery/payment. Fastkit's current assembled-answer cache uses expiry,
not automatic invalidation on every admin write. Verify acceptable staleness before changing it.

For billing, distinguish plans, entitlements, benefits, grants, products, purchases, currencies,
gateway integrations, and actual provider identities. Follow existing gateway contracts and
idempotency/reconciliation. Use explicit provider selection, no unknown-provider catch-all. Check
authentication, webhook authenticity, duplicate/out-of-order events, refund/revocation, and tenant
boundaries. Do not treat creating an integration as publishing a store subscription.

## Add custom commands through manage.py

Create a focused Python module in `commands/` with the documented `Command(BaseCommand)` class.
Implement `add_arguments` where needed and synchronous/async `handle` under the actual interface.
Raise `CommandError` for expected refusal and use the provided output interface. A module such as
`inspect_catalog.py` becomes `inspect-catalog`. Do not add shell/JavaScript command wrappers.

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

Run applicable format/build checks and inspect actual source/installed assets. Test negative tenant
access, role enforcement, input bounds, paging, file ownership, locale selection, background work,
cache visibility, and affected site/admin/API consumers. Database acceptance on SQLite alone does
not prove MySQL/PostgreSQL numeric/collation/concurrency behavior. Preserve finite external deadlines
and observable error contracts. Do not claim upstream coverage proves this new feature.

Deliver code, resource/configuration changes, current architecture/commands in AGENTS.md, actual
local evidence, and external setup boundaries. Build and deployment are separate authorized stages.
The skill is descriptive. Only the user requests updates to its stored framework knowledge.
