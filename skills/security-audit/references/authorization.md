# Authorization, identifiers, and tenant isolation

## Controls that decide access

Authenticate the caller, take its identity and tenant from trusted server-side context, and authorize every object and operation. Never trust a client-supplied owner, tenant, role, entitlement, price, or administrator flag. Limit the real database lookup or policy decision to the right scope before you read or change protected data. Apply property-level write and read rules as well as route-level checks.

When the product needs that policy, prefer opaque public resource IDs or stable slugs over exposing internal sequential primary keys. A hard-to-guess UUID does not block access when someone knows another user's UUID. A readable slug is usually easy to list or guess. Validate authorization in either case.

A resource ID is not a bearer token. Do not put session tokens, API keys, or long-lived secrets in paths or query strings because logs, browser history, screenshots, referrers, and analytics can retain them. If the product needs a share link, design it as a clear, limited capability with strong randomness, a narrow resource and action scope, expiry, revocation, and handling that expects leaks. Signed download URLs need similar limits.

## Test matrix

| Operation | Same owner | Other user, same tenant | Other tenant | Anonymous/expired | Low-role user |
| --- | --- | --- | --- | --- | --- |
| List/search/count | Intended scope only. | No unauthorized rows or counts. | No rows, counts, facets, or cursor leakage. | Denied or documented public scope. | Enforced role/filter. |
| Detail/read | Authorized content only. | Denied unless shared. | Denied. | Denied unless intentionally public. | Sensitive fields filtered. |
| Create | Owner/tenant derived by server. | Cannot impersonate owner. | Cannot choose another tenant. | Denied. | Allowed properties only. |
| Update/delete | Correct policy. | Denied unless access was clearly delegated. | Denied. | Denied. | Privileged fields/actions denied. |
| Batch/import/export | Each item authorized. | Mixed-owner payloads handled safely. | No cross-tenant output. | Denied. | Export privilege enforced. |
| File/download/preview | Scoped resource and storage access. | Guessing path does not bypass policy. | Tenant-scoped storage authorization. | Public assets only if intended. | Preview follows same policy. |
| Jobs/notifications/websockets | Trusted identity propagation. | No foreign subscription or delivery. | Tenant scope retained through worker. | Subscription/session rechecked. | Event fields filtered. |

Check nested resources where the child exists but belongs to a different parent. Check alternate methods, archived objects, soft-deleted rows, aliases, cache hits, retry paths, GraphQL resolvers, and administrative bulk actions. A permission on the detail screen does not protect a separate update or export endpoint.

## Scope propagation

Include tenant and user in cache keys and invalidation. Bind pagination cursors to their query and authorization context. Do not cache a privileged response and serve it to an ordinary caller. Check job ownership when the job is queued and when it runs, as the trust model requires. Enforce storage and signed-URL policy after access changes where needed. Notifications and email previews must not reveal private object data to former members.

Use a clear sharing model and role policy. Keep sharing between users in one tenant apart from access across tenants. Admin access must be intended and auditable. Denied requests must not cause side effects before the denial. Return errors that match the product's information-disclosure policy, without relying on vague status codes as the control.
