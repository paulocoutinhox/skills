# Connection and complete management tool map

## Connection and scope

Official MCP endpoint: `https://developer.playgama.com/api/mcp`. Configure it through the client's supported remote MCP/OAuth workflow. The owner authorizes the real organization. Do not request store passwords or OAuth codes in chat, invent bearer credentials, or imply that creating this skill connected an account.

Call the client's actual server discovery and `tools/list`. Live schemas are strict. Undeclared arguments are rejected. Use only games owned by the connected organization. A missing game and an inaccessible game can produce the same refusal. Confirm organization and list records before deciding to create a duplicate.

The provider marks writes as destructive and some public/advertising operations with `openWorldHint`. These annotations communicate effects, not user authorization. For ordinary authorized preparation, proceed without redundant prompts. Follow the additional explicit provider consent rules for product removals, traffic, and catalog updates.

The descriptive table below covers the 37 tools in the researched public reference. It is not a complete nested runtime JSON Schema. Use the actual discovered tool contract for an authorized operation, without creating a catalog generator or refresh process.

## All researched tools

| Tool | Purpose and operational constraint |
| --- | --- |
| `get_launch_steps` | Ordered progress and next tools for the latest archive. Re-read after each launch step |
| `list_applications` | Paginated organization games. Check before creating or retrying an uncertain create |
| `create_application` | Create a draft and return the game ID. Engine/title use current allowed values |
| `get_application` | Saved form, archive/media metadata, story, active archives and current identities |
| `update_application_form` | Partial scalar save, whole-array replacement. Does not submit review |
| `get_game_categories` | Current developer category taxonomy and selection rules. Read before setting category |
| `get_submission_state` | Eligibility for the specified archive and review type. Does not submit moderation |
| `list_moderation_comments` | Read correspondence. Replies are not exposed on this surface |
| `start_archive_upload` | Reserve archive and presigned upload contract with exact size/name |
| `confirm_archive_upload` | Attach/upload processing, public QA-file effect, repeatable state reconciliation |
| `get_archive_status` | Unpack, build check, Bridge detection, reason and analysis state |
| `start_cover_upload` | Reserve exact square/portrait/landscape media slot and encoding |
| `confirm_cover_upload` | Validate/publicly publish image and replace that saved cover |
| `list_in_app_products` | Full product catalog and current optimistic-concurrency checksum |
| `replace_in_app_products` | Whole-state replacement. Omitted products are deleted, stale checksum refused |
| `list_leaderboards` | Current leaderboard tags and configuration |
| `create_leaderboard` | Add immutable leaderboard tag with numeric/time ranking configuration |
| `update_leaderboard` | Update allowed fields. Does not rename the immutable tag or delete scores |
| `get_archive_qa_tool_link` | Current deployment's QA/certification link for a specific archive |
| `get_local_game_qa_tool_link` | QA harness for a real local/dev URL, optional isolated/persistent session |
| `get_bridge_sdk_docs` | Live module index or chosen page, optionally filtered to the engine binding |
| `get_game_checklist` | Current requirements index/pages and unavailable-source disclosure |
| `get_game_guides` | Current game/engine guidance. Read the relevant returned pages |
| `get_game_telemetry_guide` | Instrumentation, privacy/cardinality contract and interpretation instructions |
| `get_game_telemetry_analytics` | Bounded overview, event inventory, freshness and pagination |
| `get_game_telemetry_event_analytics` | Single-event field summaries/distributions, not raw unlimited export |
| `get_game_telemetry_timeseries` | Paginated 30-minute/daily aggregate counts with supported filters |
| `get_game_telemetry_session_facts` | Filtered pseudonymized sequence facts for a specific product question |
| `get_sandbox_state` | Current public sandbox/revision and archive-specific publication verdict |
| `get_sandbox_share` | Prepared text/links for an existing live sandbox. Does not post anything |
| `publish_sandbox` | Publish the selected eligible archive publicly. Does not obtain moderation approval |
| `get_publications` | Publication records for sandbox/catalog. Reconcile with active archives |
| `get_sandbox_traffic` | Eligibility, bonus/run state and offer information. No spending on read |
| `start_sandbox_traffic` | Irreversible traffic/bonus effect. Requires explicit owner decision |
| `send_playgama_catalog_update` | Update all catalog players without moderation. Requires per-update consent |
| `get_referral_program` | Organization referral invitation and bonus state, read-only |
| `apply_referral_code` | Accept the developer-supplied invitation before eligibility closes. Cannot invent a code |

## Contracts and recovery

Read the selected tool's live schema, required parameters, enum choices, nested fields, ownership, and documented refusal reasons. Many refusals are readable business results rather than protocol failures. Retain the original provider reason and translate/explain it accurately without treating it as success.

Use returned application/archive/media IDs. Do not reconstruct deployment-specific QA URLs. Retry an uncertain create only after checking existing records. Presigned URLs expire and are signed for exact content length/type. Start a corrected upload when size/format differs rather than changing the URL's query parameters.

Do not expose upload URLs in public reports. Record sanitized IDs, payload/file hashes, and final states for resumption. Public archive confirmation, cover confirmation, sandbox publication, traffic, and catalog updates are different operations with different effects.
