# Python services prompts

Background queues and caching with Queuefy and Cachefy. Read
[how to use the prompts](../task-prompts.md) before you copy one.

## Python queue

```text
Use queuefy from paulocoutinhox/skills.
Read [SKILLS_ROOT]/queuefy/SKILL.md and the references that apply. Name the path really loaded, or say it is missing.

Implement [BACKGROUND_WORK_AND_SCHEDULES] in [PYTHON_REPOSITORY].
Framework, package versions, store, and process layout: [CONTEXT].
Durability, latency, retry, timezone, and side-effect requirements: [CONTRACT].

Keep queue setup, task handlers, business services, and lifecycle apart. Choose a supported store
and async driver, time limits that always end, stable operation keys, explicit retry policies, and a
clean shutdown. Explain where transactions or an outbox end and where outside effects begin. Check
duplicate enqueue, workers running at the same time, interrupted runs, and recovery against the
real backend. Deliver readable changes, setup and structure notes, and real evidence. Do not claim
that a job runs exactly once.
```

## Python cache

```text
Use cachefy from paulocoutinhox/skills.
Read [SKILLS_ROOT]/cachefy/SKILL.md and the references that apply. Name the path really loaded, or say it is missing.

Implement caching for [READS_OR_FUNCTIONS] in [PYTHON_REPOSITORY].
Framework/package versions, source of truth, writers, store, and layout: [CONTEXT].
Allowed staleness, authorization scope, and invalidation requirements: [CONTRACT].

Keep cache setup, producers, business services, and resource lifecycle apart. Define scoped keys,
TTL and freshness, leases, invalidation, time limits that always end for clients and pools, and
what happens when something fails at runtime. Always check authorization and critical quotas
against the source of truth, not the cache. Check a stored None, misses at the same time, stale
refresh, invalidation races, tenant separation, and a store outage. Deliver readable changes,
current structure and setup docs, the real checks, and the limits of consistency. Do not add
execution wrappers or fact-refresh scripts nobody asked for. The requested cache lifecycle stays as
app code.
```
