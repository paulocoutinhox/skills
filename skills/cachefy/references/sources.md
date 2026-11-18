# Cachefy sources

Verified on 2026-11-05 from upstream and rechecked on 2026-11-18 against main at commit `4d0998c`
(`pyproject.toml` version 1.0.0). Match the installed wheel to the API before implementation.

| Source | Role |
| --- | --- |
| [README](https://github.com/paulocoutinhox/cachefy/blob/main/README.md) | Purpose, vocabulary, supported features, and public import paths. |
| [pyproject.toml](https://github.com/paulocoutinhox/cachefy/blob/main/pyproject.toml) | Python 3.11+ requirement and Redis/SQLAlchemy extras. |
| [Spaces](https://github.com/paulocoutinhox/cachefy/blob/main/docs/spaces.md) | Names, duration types, MISS, bulk reads, conditional writes, counters, and return values. |
| [Memoizing](https://github.com/paulocoutinhox/cachefy/blob/main/docs/memoizing.md) | Argument keys, invalidation/refresh, methods, and synchronous producer execution. |
| [Stampede](https://github.com/paulocoutinhox/cachefy/blob/main/docs/stampede.md) | Freshness versus TTL, leases, stale reads, and repeat-computation boundary. |
| [Resilience](https://github.com/paulocoutinhox/cachefy/blob/main/docs/resilience.md) | Runtime store failures, caller/startup errors, logging, and finite client timeouts. |
| [Stores](https://github.com/paulocoutinhox/cachefy/blob/main/docs/stores.md) | Backend suitability, Redis Cluster restriction, SQL capacity, and memory boundaries. Rechecked on 2026-11-18: `decode_responses` clients are refused, and the suite runs Redis 7, MySQL 8.4, and PostgreSQL 16 without promising older servers. |
| [Frameworks](https://github.com/paulocoutinhox/cachefy/blob/main/docs/frameworks.md) | Lifecycle, stable event loops, janitor integration, and producer scope. |
| [Hooks](https://github.com/paulocoutinhox/cachefy/blob/main/docs/hooks.md) | Verified on 2026-11-18. `on_hit` and `on_miss` receive space and key, `on_error` receives the operation and failure, and a stored `None` is a hit. |
| [Janitor](https://github.com/paulocoutinhox/cachefy/blob/main/docs/janitor.md) and [ASGI helper](https://github.com/paulocoutinhox/cachefy/blob/main/src/cachefy/asgi.py) | Verified on 2026-11-18. `Janitor(app)` sweeps expired entries, and `cachefy.asgi.lifespan_for(janitor)` runs setup, sweeps, and stops it without disposing clients. |
| [Application source](https://github.com/paulocoutinhox/cachefy/blob/main/src/cachefy/app.py) and [space source](https://github.com/paulocoutinhox/cachefy/blob/main/src/cachefy/space.py) | Duplicate-space refusal, space_for lookup, conditional-write returns, freshness, and actual producer failure behavior. Source resolves an example that appears to redeclare a space. |
| [Queuefy stores](https://github.com/paulocoutinhox/queuefy/blob/main/docs/stores.md) | Verified on 2026-11-18. Queuefy's Redis store requires `maxmemory-policy` `noeviction`, which constrains infrastructure shared with a cache. |
| [Designing Data-Intensive Applications](https://dataintensive.net/) | Professional context for consistency, reliability, and distributed tradeoffs. Author's public overview was consulted, not the full book. |

No store deployment, cache benchmark, or distributed failure test was executed during authoring.
Documented upstream coverage percentages do not establish this application's integration correctness.
