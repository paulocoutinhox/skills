# Connection and complete management tool map

## Connection and scope

Official MCP endpoint: `https://developer.playgama.com/api/mcp`. A second official endpoint, `https://developer.playgama.com/api/mcp/openai`, serves the OpenAI plugin directory. Do not take the address from any other listing. The owner authorizes the real organization. Do not ask for store passwords or OAuth codes in chat, invent bearer credentials, or suggest that creating this skill connected an account.

## Log in with OAuth

There is no token to create or copy. The server is an OAuth protected resource:

| Item | Value |
| --- | --- |
| Protected resource metadata | `https://developer.playgama.com/.well-known/oauth-protected-resource`, resource `https://developer.playgama.com/api/mcp`, scope `mcp`, bearer in the `Authorization` header |
| Authorization server metadata | `https://developer.playgama.com/.well-known/oauth-authorization-server` |
| Dynamic client registration | `POST https://developer.playgama.com/api/oauth/register` |
| Authorization | `https://developer.playgama.com/api/oauth/authorize`, response type `code`, PKCE `S256` only |
| Token | `POST https://developer.playgama.com/api/oauth/token`, grants `authorization_code` and `refresh_token`, public clients without a secret (`token_endpoint_auth_method: none`) |
| Revocation | `https://developer.playgama.com/api/oauth/revoke` |

Client setup, from the official MCP page:

- Claude Code: `claude mcp add --transport http playgama-developer-cabinet https://developer.playgama.com/api/mcp`, then `/mcp`, pick `playgama-developer-cabinet` and choose to authenticate. A server added while a session runs loads only in the next session.
- Codex: `codex mcp add playgama-developer-cabinet --url https://developer.playgama.com/api/mcp`, which opens the browser to sign in.
- Cursor (`~/.cursor/mcp.json`) and VS Code (`.vscode/mcp.json`): an `http` server entry with that URL. The file holds no secret.
- Claude app or claude.ai: Settings, Connectors, add a custom connector with the endpoint.

The browser opens a consent page on developer.playgama.com. The owner signs in, checks the account, organization, agent name and return address, and clicks **Allow**. The request is valid for 10 minutes. Deny a page that names an unknown agent or return address. The access token lasts an hour and the client renews it with the refresh token. An agent not used for 30 days must connect again. Connected agents are listed and revoked on `https://developer.playgama.com/mcp`. A 401 on every call means the client must sign in again.

When the client cannot load the server in the running session, the agent can run the same standard flow and call the server directly, without any secret from the owner:

1. Register a public client with a loopback redirect such as `http://127.0.0.1:<port>/callback`, scope `mcp`, grant types `authorization_code` and `refresh_token`.
2. Create a PKCE verifier, its S256 challenge and a random state. Open the authorization URL with `client_id`, `redirect_uri`, `code_challenge`, `code_challenge_method=S256`, `scope=mcp`, `state` and `resource=https://developer.playgama.com/api/mcp`, and listen on the loopback port for the redirect.
3. Tell the owner to approve on the opened page. Check the returned state, exchange the code at the token endpoint with the verifier, and keep the token in a private file of the session, never in the repository or the chat.
4. Speak MCP over Streamable HTTP: `POST` JSON-RPC to the endpoint with `Accept: application/json, text/event-stream` and the bearer. Send `initialize`, keep the returned `Mcp-Session-Id` header for later requests, send `notifications/initialized`, then `tools/list` and `tools/call`. Answers may come as server-sent events whose `data:` line holds the JSON-RPC response. On 401, refresh the token once and try again.

This direct use only changes how messages travel. The same tool contracts, consent rules and owner authorization apply.

## Tools and schemas

Call the client's real server discovery and `tools/list`. Live schemas are strict. Arguments that a schema does not declare are rejected. Use only games owned by the connected organization. A missing game and a game you cannot access can give the same refusal. Confirm the organization and list the records before you decide to create what may be a duplicate.

The provider marks writes as destructive and marks some public and advertising operations with `openWorldHint`. These labels describe effects, not user authorization. For normal authorized preparation, go ahead without extra prompts. Follow the provider's added explicit consent rules for product removals, traffic, and catalog updates.

The table below describes the 37 tools in the public reference checked. It is not a full nested runtime JSON Schema. Use the real tool contract you discover for an authorized operation, without building a catalog generator or refresh process.

## All researched tools

| Tool | Purpose and operational constraint |
| --- | --- |
| `get_launch_steps` | Ordered progress and next tools for the latest archive. Read again after each launch step |
| `list_applications` | Organization games, in pages. Check before creating, or before retrying a create whose result was unclear |
| `create_application` | Create a draft and return the game ID. Engine and title use current allowed values. Optional `agent`/`model`/`modelId` declarations come only from confirmed facts |
| `get_application` | Saved form, archive and media metadata, story, active archives and current identities |
| `update_application_form` | Saves some scalar fields and replaces whole arrays. Does not submit for review |
| `get_game_categories` | Current developer category list and selection rules. Read before setting the category |
| `get_submission_state` | Eligibility for the named archive and review type. Does not submit to moderation |
| `list_moderation_comments` | Read messages. Replies are not available here |
| `start_archive_upload` | Reserve the archive and a presigned upload contract with exact size and name |
| `confirm_archive_upload` | Attach the upload and start processing, make QA files public, safe to repeat to check state |
| `get_archive_status` | Unpack, build check, Bridge detection, reason and analysis state |
| `start_cover_upload` | Reserve the exact square, portrait or landscape media slot and encoding |
| `confirm_cover_upload` | Check and publicly publish the image and replace that saved cover |
| `list_in_app_products` | Full product catalog and the current checksum that blocks overwriting newer changes |
| `replace_in_app_products` | Replaces the whole list. Products left out are deleted, an outdated checksum is refused |
| `list_leaderboards` | Current leaderboard tags and settings |
| `create_leaderboard` | Add a fixed leaderboard tag with numeric or time ranking settings |
| `update_leaderboard` | Update allowed fields. Does not rename the fixed tag or delete scores |
| `get_archive_qa_tool_link` | The current deployment's QA and certification link for a specific archive |
| `get_local_game_qa_tool_link` | QA harness for a real local or dev URL, with an optional isolated or persistent session |
| `get_bridge_sdk_docs` | Live module index or a chosen page, optionally filtered to the engine binding |
| `get_game_checklist` | Current requirements index and pages, and notice of sources that are unavailable |
| `get_game_guides` | Current game and engine guidance. Read the relevant returned pages |
| `get_game_telemetry_guide` | Event setup, privacy and distinct-value rules, and how to read the results |
| `get_game_telemetry_analytics` | Limited overview, event list, data freshness and pages |
| `get_game_telemetry_event_analytics` | Field summaries and distributions for one event, not an unlimited raw export |
| `get_game_telemetry_timeseries` | 30-minute or daily total counts in pages, with supported filters |
| `get_game_telemetry_session_facts` | Filtered, pseudonymized event sequences for a specific product question |
| `get_sandbox_state` | Current public sandbox and revision, and the publication verdict for an archive |
| `get_sandbox_share` | Prepared text and links for an existing live sandbox. Does not post anything |
| `publish_sandbox` | Publish the chosen eligible archive publicly. Does not get moderation approval |
| `get_publications` | Publication records for sandbox and catalog. Check them against active archives |
| `get_sandbox_traffic` | Eligibility, bonus and run state, and offer information. Reading spends nothing |
| `start_sandbox_traffic` | Spends traffic or bonus and cannot be undone. Needs an explicit owner decision |
| `send_playgama_catalog_update` | Update all catalog players without moderation. Needs consent for each update |
| `get_referral_program` | Organization referral invitation and bonus state, read-only |
| `apply_referral_code` | Accept the invitation the developer gives before eligibility closes. Cannot invent a code |

## Contracts and recovery

Read the chosen tool's live schema, required parameters, enum choices, nested fields, ownership, and documented refusal reasons. Many refusals are readable business results, not protocol failures. Keep the provider's original reason and translate or explain it accurately, without treating it as success.

Use the returned application, archive and media IDs. Do not rebuild QA URLs that depend on the deployment. Retry an unclear create only after checking existing records. Presigned URLs expire and are signed for an exact content length and type. When the size or format changes, start a new upload rather than editing the URL's query parameters.

Do not show upload URLs in public reports. Record cleaned IDs, payload and file hashes, and final states so work can resume. Public archive confirmation, cover confirmation, sandbox publication, traffic, and catalog updates are different operations with different effects.
