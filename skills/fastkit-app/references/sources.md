# Fastkit sources

Verified on 2026-11-05 through upstream main and rechecked on 2026-11-18 against main at commit
`e1a2f99`.

- [README](https://github.com/paulocoutinhox/fastkit/blob/main/README.md): product purpose, current
  features, site/admin/API surfaces, bootstrap, manage.py commands, native command extension, and
  configuration/deployment prerequisites.
- [Architecture](https://github.com/paulocoutinhox/fastkit/blob/main/docs/architecture.md): route/schema/
  service/model boundaries, resource declarations, tenant/localization, queue/cache, providers,
  external deadlines, request limits, audit, and current domain-file organization. Rechecked on
  2026-11-18: one `snake_case` module per application class and enum, one process with no worker
  process or scheduler daemon, and a cache that development leaves off and that expires without
  write invalidation.
- [Upstream AGENTS.md](https://github.com/paulocoutinhox/fastkit/blob/main/AGENTS.md): verified on
  2026-11-18. The ordered new-resource checklist covering enum, model, `models/registry.py`, schemas,
  service, `build_router` routes in `helpers/router.py`, admin resource, catalogs, and tests.
- [pyproject.toml](https://github.com/paulocoutinhox/fastkit/blob/main/pyproject.toml): verified on
  2026-11-18. `requires-python >=3.13` and Ruff line length 320. The admin and site `.prettierrc`
  files set `printWidth` 320.
- [Configuration](https://github.com/paulocoutinhox/fastkit/blob/main/docs/configuration.md) and
  [settings loader](https://github.com/paulocoutinhox/fastkit/blob/main/helpers/settings.py): verified
  on 2026-11-18. `APP_ENV`, default `dev`, imports `config.<env>`, nothing under `config/` reads other
  environment variables, published stage/prod secrets are placeholders, and production refuses to
  start while `change-me` remains.
- [Accounts](https://github.com/paulocoutinhox/fastkit/blob/main/docs/accounts.md): verified on
  2026-11-18. The token is carried as a bearer header or `httponly` site cookie, does not expire on its
  own, and password changes end other sessions.
- [Jobs](https://github.com/paulocoutinhox/fastkit/blob/main/docs/jobs.md) and
  [Deploy](https://github.com/paulocoutinhox/fastkit/blob/main/docs/deploy.md): verified on 2026-11-18.
  `run-delivery` runs one delivery pass by hand, `migrate` never alters an existing table, and
  `schema-diff` writes the missing DDL for review.

At operational use, follow the relevant README-linked account, site, admin, commerce, subscription,
gateway, job, configuration, and deployment guides for the selected feature. Do not claim those guides
were executed or that published tests certify the new application. The researched upstream already
uses one module per class and enum, which matches the collection owner's convention. An older target
checkout can still group symbols, so inspect it before splitting files.
No Fastkit app, database migration, billing operation, or deployment was executed during authoring.
