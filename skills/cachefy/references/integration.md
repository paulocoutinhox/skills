# Cache integration decisions

## Correctness before optimization

Decide which system owns the truth and whether stale output is acceptable. Prices, permission
grants, balances, and purchase state need clear consistency rules. A cache can speed up a checked
read. It cannot replace a durable transaction or an authorization decision. Cachefy falls back on
purpose at runtime, and that is part of its API contract. It is not a reason to wrap the
application in catch-all exception handling or to hide producer bugs.

For a critical quota, an `incr` that fails cannot be read as zero requests. Choose a quota system
that is the source of truth and has a clear outage policy. Use Cachefy counters only where it is
correct to accept their documented no-success result. Never turn an uncertain compare-and-set
result into a write without a condition.

## Invalidation and resource boundaries

List every writer that affects the cached answer. Invalidation must come after the commit and must
handle producers that started before it. Put a source version in keys only when the application can
look up that version reliably. A new local counter you made up is not a shared invalidation
protocol. TTL is a choice to accept limited staleness, not proof that data is always up to date.

Use short, finite network and pool waits compared to the cost of computing from the source. SQL
query timeout settings depend on the driver. Do not copy an asyncpg connection option into SQLite
or MySQL. Keep each engine and async client on the event loop that owns it. The upstream bridge for
sync frameworks uses one stable loop, not `asyncio.run` around every request. Application sessions
belong inside the producer scope.

## Stores and deployment

Memory does not coordinate processes. Redis needs the current byte-response contract and does not
support Redis Cluster in this implementation. SQLAlchemy needs real async drivers and enough pool
capacity. For local multi-process SQLite, check the WAL and busy-timeout needs, and set up the
schema before workers start at the same time. Do not add raw Redis scripts or SQL behind the space
API to get around the library's ownership and version contract.

Choose prefixes and spaces on purpose when you share infrastructure. Queuefy's Redis queue needs
noeviction, while a normal cache can accept eviction. Prefixes alone do not separate memory policy
or failure domains. Dispose of the resources you own only after janitor and producer work has
stopped.
