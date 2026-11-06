# Queue integration decisions

## Transaction and side-effect ownership

A task record, the application's business state, and a provider's side effect are separate unless
an actual atomic mechanism joins them. Define the invariant first. For email, use a durable message
record/provider key and accept the provider's documented duplicate boundary. For payment, persist a
payment operation key and reconcile the provider response. For file exports, use a deterministic
artifact identity and atomic publication where the storage supports it. Never describe a queue
claim as a distributed transaction with an external system.

Enqueue after a business commit prevents work from reading uncommitted state but does not recover a
process crash before enqueue. An outbox stores the intent in that business transaction and dispatches
it with repeat-safe keys. Add this only when the delivery requirement justifies it. Do not build a
general workflow framework around one background task.

## Deployment and capacity

- Database: provision the actual async driver, pool capacity, connection timeout, query deadlines,
  schema initialization order, and database persistence. SQLite suits local use, not arbitrary
  distributed replicas sharing a file over network storage.
- Redis: use a supported non-cluster primary, TLS/authentication where appropriate, finite timeouts,
  noeviction, and a deliberate persistence/failover policy. Cache eviction policies cannot be reused
  for durable queue records. Separate prefixes do not separate an instance-wide eviction policy.
- Memory: use only when loss on restart and process-local state are intentional.
- Workers: task modules must be imported consistently. Use separate resource pools when polling and
  application requests would starve each other. Explicitly stop workers before disposing clients.
- Schedules: use aware UTC instants, synchronized host clocks, stable task names, and documented
  recurring-slot rules. Renaming a recurring task changes its identity, not just a display label.

## Operational evidence

Observe pending depth and oldest age, completion/error rates, elapsed time, attempts, lease loss,
unknown tasks, and shutdown drain behavior. Avoid scanning the entire store on every request just
to report depth. Review retained payloads/results/errors for privacy and define expiry independently
of the business audit policy. A custom store must satisfy the current upstream conditional claim,
owner/attempt, atomic mutation/result, and contract-test requirements. Do not improvise a store that
reads a pending record and updates it unconditionally.
