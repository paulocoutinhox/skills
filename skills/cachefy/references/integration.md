# Cache integration decisions

## Correctness before optimization

Define which system owns the truth and whether stale output is acceptable. Prices, permission grants,
balances, and purchase state need explicit consistency rules. A cache can accelerate a verified read
but cannot replace a durable transaction or an authorization decision. Cachefy's deliberate runtime
degradation is part of its API contract, not a reason to add catch-all exception handling around the
application or hide producer bugs.

For a critical quota, an unavailable `incr` cannot be interpreted as zero requests. Choose an
authoritative quota implementation with an explicit outage policy. Use Cachefy counters for scenarios
whose correctness permits its documented no-success result. Never convert an uncertain compare-and-set
result into an unconditional write.

## Invalidation and resource boundaries

Map all writers to the cached answer. Invalidation must follow commit and account for producers that
started before it. Use a source version in keys only when the application can resolve that version
reliably. A newly invented local counter is not a distributed invalidation protocol. TTL is a bounded
staleness choice, not proof of immediate consistency.

Use short finite network/pool waits relative to source computation cost. SQL query timeout settings
are driver-specific. Do not copy an asyncpg connection option into SQLite or MySQL. Keep each engine
and async client on its owning event loop. The upstream synchronous-framework bridge uses a stable
loop, not `asyncio.run` around every request. Application sessions belong inside the producer scope.

## Stores and deployment

Memory does not coordinate processes. Redis requires the current byte-response contract and does
not support Redis Cluster in this implementation. SQLAlchemy requires actual async drivers and
pool capacity. On local multi-process SQLite, inspect WAL/busy-timeout requirements and initialize
schema before concurrent workers. Do not add raw Redis scripts or SQL behind the space API to bypass
the library's ownership/version contract.

Choose prefixes/spaces deliberately when sharing infrastructure. Queuefy's durable queue may require
noeviction, while an ordinary cache can tolerate eviction. Prefixes alone do not isolate memory policy
or failure domains. Dispose owned resources only after janitor/producer lifecycle work has stopped.
