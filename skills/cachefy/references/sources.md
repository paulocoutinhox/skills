# Cachefy sources

Checked on 2026-11-05 from upstream and checked again on 2026-11-18 against main at commit
`4d0998c` (`pyproject.toml` version 1.0.0). Match the installed wheel to the API before you write
code.

| Source | Role |
| --- | --- |
| [README](https://github.com/paulocoutinhox/cachefy/blob/main/README.md) | Purpose, terms, supported features, and public import paths. |
| [pyproject.toml](https://github.com/paulocoutinhox/cachefy/blob/main/pyproject.toml) | Python 3.11+ requirement and Redis/SQLAlchemy extras. |
| [Spaces](https://github.com/paulocoutinhox/cachefy/blob/main/docs/spaces.md) | Names, duration types, MISS, bulk reads, conditional writes, counters, and return values. |
| [Memoizing](https://github.com/paulocoutinhox/cachefy/blob/main/docs/memoizing.md) | Argument keys, invalidation and refresh, methods, and how sync producers run. |
| [Stampede](https://github.com/paulocoutinhox/cachefy/blob/main/docs/stampede.md) | Freshness versus TTL, leases, stale reads, and the limit on repeated computation. |
| [Resilience](https://github.com/paulocoutinhox/cachefy/blob/main/docs/resilience.md) | Runtime store failures, caller and startup errors, logging, and finite client timeouts. |
| [Stores](https://github.com/paulocoutinhox/cachefy/blob/main/docs/stores.md) | Which backend fits which use, the Redis Cluster limit, SQL capacity, and memory limits. Checked again on 2026-11-18: `decode_responses` clients are refused, and the suite runs Redis 7, MySQL 8.4, and PostgreSQL 16 without promising older servers. |
| [Frameworks](https://github.com/paulocoutinhox/cachefy/blob/main/docs/frameworks.md) | Lifecycle, stable event loops, janitor integration, and producer scope. |
| [Hooks](https://github.com/paulocoutinhox/cachefy/blob/main/docs/hooks.md) | Checked on 2026-11-18. `on_hit` and `on_miss` receive space and key, `on_error` receives the operation and failure, and a stored `None` is a hit. |
| [Janitor](https://github.com/paulocoutinhox/cachefy/blob/main/docs/janitor.md) and [ASGI helper](https://github.com/paulocoutinhox/cachefy/blob/main/src/cachefy/asgi.py) | Checked on 2026-11-18. `Janitor(app)` sweeps expired entries, and `cachefy.asgi.lifespan_for(janitor)` runs setup, sweeps, and stops it without disposing of clients. |
| [Application source](https://github.com/paulocoutinhox/cachefy/blob/main/src/cachefy/app.py) and [space source](https://github.com/paulocoutinhox/cachefy/blob/main/src/cachefy/space.py) | Refusal of duplicate spaces, space_for lookup, conditional-write returns, freshness, and real producer failure behavior. The source settles an example that seems to declare a space twice. |
| [Queuefy stores](https://github.com/paulocoutinhox/queuefy/blob/main/docs/stores.md) | Checked on 2026-11-18. Queuefy's Redis store needs `maxmemory-policy` `noeviction`, which limits infrastructure shared with a cache. |
| [Designing Data-Intensive Applications](https://dataintensive.net/) | Professional background on consistency, reliability, and distributed tradeoffs. Only the author's public overview was read, not the full book. |

No store deployment, cache benchmark, or distributed failure test was run while writing this skill.
Coverage percentages documented upstream do not prove that this application's integration is
correct.
