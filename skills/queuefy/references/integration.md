# Queue integration decisions

## Transaction and side-effect ownership

A task record, the application's business state, and a provider's side effect are separate unless
a real atomic mechanism joins them. Define the rule first. For email, use a durable message record
or provider key, and accept the duplicate limit the provider documents. For payment, save a payment
operation key and check the provider response against it. For file exports, use a fixed file
identity and atomic publishing where the storage supports it. Never describe a queue claim as a
distributed transaction with an outside system.

Enqueue after a business commit stops work from reading uncommitted state. It does not recover from
a process crash before the enqueue. An outbox saves the intent in that business transaction and
sends it later with keys that are safe to repeat. Add this only when the delivery need justifies
it. Do not build a general workflow framework around one background task.

## Deployment and capacity

- Database: set up the actual async driver, pool size, connection timeout, query deadlines, schema
  setup order, and database persistence. SQLite fits local use. It does not fit many distributed
  copies sharing one file over network storage.
- Redis: use a supported non-cluster primary, TLS and authentication where needed, finite timeouts,
  noeviction, and a chosen persistence and failover policy. Cache eviction policies cannot be reused
  for durable queue records. Separate prefixes do not separate an eviction policy that covers the
  whole instance.
- Memory: use it only when losing data on restart and keeping state in one process are intended.
- Workers: import task modules the same way everywhere. Use separate resource pools when polling
  and application requests would block each other. Stop workers on purpose before you dispose of
  clients.
- Schedules: use aware UTC instants, synced host clocks, stable task names, and documented
  recurring-slot rules. Renaming a recurring task changes its identity, not just a display label.

## Operational evidence

Watch pending depth and oldest age, completion and error rates, elapsed time, attempts, lost
leases, unknown tasks, and how shutdown drains work. Do not scan the whole store on every request
just to report depth. Review kept payloads, results, and errors for privacy, and set their expiry
apart from the business audit policy. A custom store must meet the current upstream requirements
for conditional claims, owner and attempt tracking, atomic changes and results, and contract tests.
Do not make up a store that reads a pending record and then updates it without a condition.
