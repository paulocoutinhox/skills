# Repository-wide impact analysis

Start from the changed symbol or contract and trace both directions: its dependencies and all known consumers. Use repository search for exact names, exported paths, route strings, schema keys, configuration keys, events, cache prefixes, and persisted fields. Text search alone can miss dynamic routing or generated code, so check registries and framework wiring when relevant.

| Change trigger | Trace and validate |
| --- | --- |
| Function return, argument, or error | Callers, interface implementations, mocks, serializers, UI error handling, CLI status. |
| Model/schema field | Database constraints, migrations, imports/exports, API schema, validation, filters, indexes, jobs, analytics. |
| Authentication or authorization | Login/session lifetime, all resource routes, role policies, tenant scope, exports, files, background jobs, websocket subscriptions. |
| Route or public identifier | Links, frontend routing, deep links, API consumers, redirects, access checks, caches, existing saved references within scope. |
| Event or queue payload | Producers, consumers, retry policy, idempotency, dead-letter processing, deployed worker versions. |
| Cache behavior | Key ownership, tenant/user scope, invalidation, stale data, expiry, consistency under updates. |
| UI state or lifecycle | Navigation, loading/empty/error states, unmount cleanup, stale async responses, accessibility and SSR if used. |
| Dependency/toolchain | Runtime support, plugin peer ranges, lockfile, native ABI, build image, package entrypoints. |
| Release workflow | Event trust, permission grants, publisher identity, version matching, built versus published artifact, secrets. |
| File paths or storage | Traversal, symlinks, permissions, cleanup, retained references, backups, signed downloads. |
| Numeric or time logic | Units, rounding, overflow, currency, timezone, DST, ordering, aggregation and boundary dates. |

Think of deployment as a system. A source change may be correct after all components update but fail during a rollout. Do not add legacy compatibility by default. Find out whether the intended final contract needs a coordinated deployment or a clear migration. Do not treat a request to remove old code as permission to corrupt saved data.

Report concrete affected consumers and the checks that support them. If you cannot check an external consumer, state the contract and the open dependency instead of claiming the whole system was validated. A narrow diff can justify a broad read-only investigation, but not broad code changes.
