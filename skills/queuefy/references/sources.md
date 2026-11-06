# Queuefy sources

Verified on 2026-11-05 through the upstream repository. README and source main can differ from a
published wheel. Inspect the user's actual version before applying an API example.

| Source | Role |
| --- | --- |
| [README](https://github.com/paulocoutinhox/queuefy/blob/main/README.md) | Intended use, task/run/queue vocabulary, scheduling and entrypoint imports. |
| [pyproject.toml](https://github.com/paulocoutinhox/queuefy/blob/main/pyproject.toml) | Python minimum and optional dependency extras. Extras do not select an application SQL driver. |
| [Getting started](https://github.com/paulocoutinhox/queuefy/blob/main/docs/getting-started.md) | Initialization, registration, enqueue, and worker lifecycle. |
| [Tasks](https://github.com/paulocoutinhox/queuefy/blob/main/docs/tasks.md) | Keys, interval/cron contracts, payloads, priorities, and validation. |
| [Workers](https://github.com/paulocoutinhox/queuefy/blob/main/docs/workers.md) | Leases, clock skew, concurrency, shutdown, and synchronous thread limitations. |
| [Retries](https://github.com/paulocoutinhox/queuefy/blob/main/docs/retries.md) | Retry enum, permanent failure, unknown tasks, timeouts, and at-least-once execution. |
| [Stores](https://github.com/paulocoutinhox/queuefy/blob/main/docs/stores.md) | SQL/Redis/memory boundaries, Redis Cluster and eviction restrictions, atomic store contract. |
| [Frameworks](https://github.com/paulocoutinhox/queuefy/blob/main/docs/frameworks.md) | Framework-independent composition, resource/session ownership, and transaction separation. |
| [Hooks](https://github.com/paulocoutinhox/queuefy/blob/main/docs/hooks.md) | Listener arguments, persisted versus logged handler errors, and outcome/owner boundaries. |
| [Application API](https://github.com/paulocoutinhox/queuefy/blob/main/src/queuefy/app.py) and [store contract](https://github.com/paulocoutinhox/queuefy/blob/main/src/queuefy/store/base.py) | Actual registration/inspection/count methods and cancellation limited to not-started runs. |
| [Designing Data-Intensive Applications](https://dataintensive.net/) | Professional reading on reliability and distributed-system tradeoffs. Author's overview was consulted, not a full book review. |

Upstream's single-claim descriptions must be read alongside its explicit at-least-once discussion.
This skill does not certify exactly-once external effects, database throughput, or a production
deployment. No Queuefy server, database, worker, or failure-injection run was executed during authoring.
