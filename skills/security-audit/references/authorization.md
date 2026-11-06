# Authorization, identifiers, and tenant isolation

## Authoritative controls

Authenticate the caller, derive its identity and tenant from trusted server-side context, and authorize every object and operation. Never trust a client-supplied owner, tenant, role, entitlement, price, or administrator flag. Scope the actual database lookup or policy decision before reading or mutating protected data. Apply property-level write and read rules as well as route-level checks.

Prefer opaque public resource identifiers or stable slugs to exposing internal sequential primary keys when the product requires that policy. A guess-resistant UUID does not prevent access when another user's UUID is known. A readable slug is usually enumerable. Validate authorization in either case.

A resource identifier is not a bearer token. Do not put session tokens, API keys, or long-lived secrets in paths or query strings because logs, browser history, screenshots, referrers, and analytics can retain them. If the product needs a share link, design it as an explicit limited capability with strong randomness, narrow resource/action scope, expiry, revocation, and leak-aware handling. Signed download URLs need similar limitations.

## Test matrix

| Operation | Same owner | Other user, same tenant | Other tenant | Anonymous/expired | Low-role user |
| --- | --- | --- | --- | --- | --- |
| List/search/count | Intended scope only. | No unauthorized rows or counts. | No rows, counts, facets, or cursor leakage. | Denied or documented public scope. | Enforced role/filter. |
| Detail/read | Authorized content only. | Denied unless shared. | Denied. | Denied unless intentionally public. | Sensitive fields filtered. |
| Create | Owner/tenant derived by server. | Cannot impersonate owner. | Cannot choose another tenant. | Denied. | Allowed properties only. |
| Update/delete | Correct policy. | Denied unless explicitly delegated. | Denied. | Denied. | Privileged fields/actions denied. |
| Batch/import/export | Each item authorized. | Mixed-owner payloads handled safely. | No cross-tenant output. | Denied. | Export privilege enforced. |
| File/download/preview | Scoped resource and storage access. | Guessing path does not bypass policy. | Tenant-scoped storage authorization. | Public assets only if deliberate. | Preview follows same policy. |
| Jobs/notifications/websockets | Trusted identity propagation. | No foreign subscription or delivery. | Tenant scope retained through worker. | Subscription/session rechecked. | Event fields filtered. |

Check nested resources where the child exists but belongs to a different parent. Check alternate methods, archived objects, soft-deleted rows, aliases, cache hits, retry paths, GraphQL resolvers, and administrative bulk actions. A permission on the detail screen does not protect a separate update or export endpoint.

## Scope propagation

Include tenant/user dimensions in cache keys and invalidation. Bind pagination cursors to their query and authorization context. Do not cache a privileged response and serve it to an ordinary caller. Validate job ownership at enqueue and execution according to the trust model. Enforce storage and signed-URL policy after access changes where required. Notifications and email previews must not reveal private object data to former members.

Use an explicit sharing model and role policy. Distinguish cross-user sharing within one tenant from cross-tenant access. Administrative access must be deliberate and auditable. Denied requests must not produce side effects before the denial. Return errors consistent with the product's information-disclosure policy without relying on status-code obscurity as the control.
