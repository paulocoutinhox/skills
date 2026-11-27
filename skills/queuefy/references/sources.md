# Queuefy sources

Checked on 2026-11-05 in the upstream repository and checked again on 2026-11-18 against main at
commit `0b2dca4` (`pyproject.toml` version 1.0.3). The README and source on main can differ from a
published wheel. Check the user's actual version before you apply an API example.

| Source | Role |
| --- | --- |
| [README](https://github.com/paulocoutinhox/queuefy/blob/main/README.md) | Intended use, task/run/queue terms, scheduling, and entrypoint imports. |
| [pyproject.toml](https://github.com/paulocoutinhox/queuefy/blob/main/pyproject.toml) | Minimum Python and optional dependency extras. Extras do not choose the application's SQL driver. |
| [Getting started](https://github.com/paulocoutinhox/queuefy/blob/main/docs/getting-started.md) | Setup, registration, enqueue, and worker lifecycle. |
| [Tasks](https://github.com/paulocoutinhox/queuefy/blob/main/docs/tasks.md) | Keys, interval/cron contracts, payloads, priorities, and checks. Checked again on 2026-11-18: workers write only the next upcoming recurring slot. |
| [Workers](https://github.com/paulocoutinhox/queuefy/blob/main/docs/workers.md) | Leases, clock skew, concurrency, shutdown, and limits of sync threads. Checked again on 2026-11-18: `keep` removes settled runs after seven days by default. |
| [Retries](https://github.com/paulocoutinhox/queuefy/blob/main/docs/retries.md) | Retry enum, permanent failure, unknown tasks, timeouts, and at-least-once execution. |
| [Stores](https://github.com/paulocoutinhox/queuefy/blob/main/docs/stores.md) | SQL/Redis/memory limits, Redis Cluster and eviction rules, atomic store contract. Checked again on 2026-11-18: PostgreSQL 14, MySQL 8.0, and Redis 7.0 minimums. |
| [Frameworks](https://github.com/paulocoutinhox/queuefy/blob/main/docs/frameworks.md) | Setup that does not depend on a framework, resource and session ownership, and keeping transactions separate. |
| [Hooks](https://github.com/paulocoutinhox/queuefy/blob/main/docs/hooks.md) | Listener arguments, saved versus logged handler errors, and outcome and owner limits. |
| [FastAPI and Starlette](https://github.com/paulocoutinhox/queuefy/blob/main/docs/fastapi.md) and [ASGI helper](https://github.com/paulocoutinhox/queuefy/blob/main/src/queuefy/asgi.py) | Checked on 2026-11-18. `queuefy.asgi.lifespan_for(worker)` runs setup, starts the worker, then stops and awaits it. It does not dispose of clients. |
| [Application API](https://github.com/paulocoutinhox/queuefy/blob/main/src/queuefy/app.py) and [store contract](https://github.com/paulocoutinhox/queuefy/blob/main/src/queuefy/store/base.py) | The real registration, inspection, and count methods, and cancellation that only works on runs that have not started. Checked again on 2026-11-18: task decorator defaults and the -1000 to 1000 priority range. |
| [Designing Data-Intensive Applications](https://dataintensive.net/) | Professional reading on reliability and distributed-system tradeoffs. Only the author's overview was read, not the full book. |

Read upstream's single-claim descriptions together with its clear discussion of at-least-once
execution. This skill does not promise exactly-once outside effects, database throughput, or a
production deployment. No Queuefy server, database, worker, or failure-injection run was done while
writing this skill.
