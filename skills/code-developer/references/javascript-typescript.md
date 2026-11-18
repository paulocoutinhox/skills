# JavaScript and TypeScript

Use the existing package manager and lockfile. npm 12 blocks dependency lifecycle scripts unless the root package's `allowScripts` policy allows them. When a dependency genuinely needs its install script, review it, record the approval with `npm install-scripts approve`, then run `npm rebuild`. Do not disable the policy wholesale. For new frontend React or Vue projects, prefer Vite and current compatible stable dependencies unless the user specifies otherwise. Verify framework, plugin, runtime, and type definitions together. Use the selected runtime's native module system. Do not ship a parallel CommonJS implementation merely for old consumers when ESM is the final contract.

Prefer strict TypeScript for a new typed application, explicit public types, exhaustive domain unions, and `unknown` plus validation at untrusted boundaries. Do not conceal uncertainty with `any`, non-null assertions, or unchecked casts. Separate transport payloads from domain state and validate runtime input because TypeScript types disappear at runtime.

Keep one class or UI component per file. Use hyphenated module filenames unless a framework requires another convention. Make async lifetimes explicit, await owned work, propagate abort signals where supported, and handle rejected promises. Do not use a catch-all that silently returns empty arrays or success. Clean up subscriptions, timers, event handlers, and object URLs. Avoid hidden side effects on module import.

Choose state tools according to the problem. Local UI state usually stays local. Server state needs fetching, invalidation, and cancellation semantics. Cross-screen client state needs a store only when ownership warrants it. Do not put every value into a global store or duplicate query results in a second source of truth.

Use the established formatter and linter, run type checking separately when the build tool only transpiles, and test affected behavior. Prettier's default `printWidth` of 80 wraps ordinary calls and function signatures. Under the owner's single-line call convention, set a wide `printWidth`, such as 320, in the repository's Prettier configuration. Prettier treats the width as a target rather than a hard limit and reflows calls that fit. Object literals written with a line break after `{` stay expanded by Prettier's design, which is structural nesting rather than a wrapped call. Verify production builds, exported entrypoints, browser capabilities, keyboard interaction, error states, and unmount cancellation when relevant. Frontend configuration and source maps must never embed private credentials.

## Applied case: runtime input and obsolete requests

A TypeScript interface does not validate JSON returned by a server. Parse the untrusted payload into a known domain shape and reject unknown/malformed required values. Do not use `as SomeType` as the only boundary control or return an empty list for both an invalid response and a legitimate empty result.

For replacement requests, abort obsolete I/O where supported and bind completion to the current request identity. An abort can arrive after response completion, so ownership of the result still matters. Close object URLs/listeners/subscriptions when their owner ends and avoid floating promises whose errors never reach the caller.

Verify out-of-order responses, navigation away, malformed JSON/schema values and real empty data. When library exports change, also test the installed package consumer. Generated automation is Python/uv only when explicitly requested, while native application modules and tests use their proper implementation language.
