# Telemetry, verification, and maintenance

Read `get_game_telemetry_guide` before instrumenting or interpreting analytics. Use the required Bridge analytics pathway rather than third-party analytics prohibited by current game rules. Keep event names/fields bounded, avoid user PII/secrets, and follow current performance-sampling and cardinality guidance. Telemetry guidance is not automatically a publication gate.

Some destinations prohibit external calls including built-in analytics. Read the selected destination's current restrictions and supported adapter/configuration before enabling emission. Bridge's general analytics availability does not override a partner prohibition. Do not invent a switch or claim destination readiness while forbidden requests remain.

## Query strategy

Start with `get_game_telemetry_analytics` for a focused inclusive range of at most 31 days, checking freshness, volume, event inventory, and sample reach. Request only relevant next pages. Drill down into one event through `get_game_telemetry_event_analytics` for field/type/distribution questions. Use `get_game_telemetry_timeseries` for supported aggregate buckets and filters, not as an FPS distribution substitute.

For a product sequence question, use `get_game_telemetry_session_facts` with at least one required narrowing filter such as event, field, session reference, or user reference. The current tool intentionally excludes repetitive core/performance events from that view. Pseudonymized facts are not a complete individual history. Do not combine every page into an unauthorized raw-player export.

Separate observed data from interpretation. Record date range/time zone, freshness, filters, sample sizes, distribution, and uncertainty. Compare equivalent build/audience windows before claiming performance or retention changes. A small successful sandbox run does not establish production scale readiness.

## Live verification

Compare `get_publications`, `get_application.activeArchives`, and the actual sandbox/catalog destination. Missing historical publication records do not prove a destination was never published. Confirm which archive players currently receive, then test startup, controls, progress, language, responsive rendering, audio/pause, ad reward correctness, purchases/restore, and links on the actual destination.

Keep build and product catalog changes independently traceable. A new archive can preserve old products while a separate catalog replacement affects purchasing immediately. Read checksums and preserve existing items during later updates. Identify user-facing consequences before deactivating a service or changing purchase behavior.

## Delivery record

Record organization/game ID, source revision, archive version/ID/hash/bytes, engine/Bridge versions, applicable checklist numbers and evidence, form revision, category rationale, media IDs/dimensions, product catalog checksum, leaderboard IDs, QA results, moderation eligibility/status, sandbox/catalog active archive, current publication IDs/links, and outstanding owner actions.

Redact OAuth credentials, presigned upload links, private player data, payment verification payloads, and internal-only values. Distinguish local verification from live platform validation and reviewed publication from sandbox exposure. Do not claim an unavailable checklist source was checked.
