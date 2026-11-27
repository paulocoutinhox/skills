# Telemetry, verification, and maintenance

Read `get_game_telemetry_guide` before adding events or reading analytics. Use the required Bridge analytics path rather than third-party analytics that the current game rules ban. Keep event names and fields limited, leave out personal data (PII) and secrets, and follow the current guidance on performance sampling and the number of distinct values. Telemetry guidance is not automatically a publication gate.

Some destinations ban external calls, including built-in analytics. Read the chosen destination's current limits and its supported adapter or configuration before sending events. Bridge's general analytics support does not override a partner ban. Do not invent a switch or claim the destination is ready while banned requests remain.

## Query strategy

Start with `get_game_telemetry_analytics` for a focused range of at most 31 days, counting both ends. Check data freshness, volume, the list of events, and sample size. Request only the next pages you need. Go deeper into one event with `get_game_telemetry_event_analytics` for questions about fields, types or distributions. Use `get_game_telemetry_timeseries` for the supported total buckets and filters, not as a stand-in for an FPS distribution.

For a question about a sequence of product events, use `get_game_telemetry_session_facts` with at least one required narrowing filter such as event, field, session reference, or user reference. The current tool leaves out repetitive core and performance events from that view on purpose. Pseudonymized facts are not a full personal history. Do not join every page into a raw player export nobody authorized.

Keep observed data apart from your reading of it. Record the date range and time zone, freshness, filters, sample sizes, distribution, and uncertainty. Compare matching build and audience windows before claiming changes in performance or retention. A small successful sandbox run does not prove the game is ready for production scale.

## Live verification

Compare `get_publications`, `get_application.activeArchives`, and the real sandbox or catalog destination. Missing past publication records do not prove that a destination was never published. Confirm which archive players get now, then test startup, controls, progress, language, layout on different screens, audio and pause, correct ad rewards, purchases and restore, and links on the real destination.

Keep build changes and product catalog changes traceable on their own. A new archive can keep old products, while a separate catalog replacement changes purchasing right away. Read checksums and keep existing items during later updates. Find out what players will notice before you turn off a service or change purchase behavior.

## Delivery record

Record the organization and game ID, source revision, archive version, ID, hash and bytes, engine and Bridge versions, the checklist numbers that apply and their evidence, form revision, why you chose the category, media IDs and dimensions, product catalog checksum, leaderboard IDs, QA results, moderation eligibility and status, the active sandbox and catalog archive, current publication IDs and links, and remaining owner actions.

Remove OAuth credentials, presigned upload links, private player data, payment verification payloads, and internal-only values. Keep local checks apart from live platform checks, and reviewed publication apart from sandbox exposure. Do not claim you checked a checklist source that was not available.
