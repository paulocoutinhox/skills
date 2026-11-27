# JavaScript and TypeScript

Use the existing package manager and lockfile. npm 12 blocks dependency lifecycle scripts unless the root package's `allowScripts` policy allows them. When a dependency really needs its install script, review it, record the approval with `npm install-scripts approve`, then run `npm rebuild`. Do not turn off the whole policy. For new frontend React or Vue projects, prefer Vite and current compatible stable dependencies unless the user asks for something else. Check the framework, plugin, runtime, and type definitions together. Use the chosen runtime's native module system. Do not ship a parallel CommonJS version just for old consumers when ESM is the final contract.

For a new typed application, prefer strict TypeScript, explicit public types, exhaustive domain unions, and `unknown` plus validation at untrusted boundaries. Do not hide uncertainty with `any`, non-null assertions, or unchecked casts. Keep transport payloads apart from domain state, and validate runtime input because TypeScript types disappear at runtime.

Keep one class or UI component per file. Use hyphenated module filenames unless a framework requires another convention. Make async lifetimes clear, await the work you own, pass abort signals on where supported, and handle rejected promises. Do not use a catch-all that silently returns empty arrays or success. Clean up subscriptions, timers, event handlers, and object URLs. Avoid hidden side effects on module import.

Choose state tools to fit the problem. Local UI state usually stays local. Server state needs fetching, invalidation, and cancellation behavior. Client state shared across screens needs a store only when ownership calls for one. Do not put every value into a global store or duplicate query results in a second source of truth.

Use the existing formatter and linter, run type checking on its own when the build tool only transpiles, and test the affected behavior. Prettier's default `printWidth` of 80 wraps ordinary calls and function signatures. Under the owner's single-line call convention, set a wide `printWidth`, such as 320, in the repository's Prettier configuration. Prettier treats the width as a target, not a hard limit, and joins calls that fit. By Prettier's design, object literals written with a line break after `{` stay expanded. That is structural nesting, not a wrapped call. Check production builds, exported entrypoints, browser capabilities, keyboard interaction, error states, and unmount cancellation when relevant. Frontend configuration and source maps must never embed private credentials.

## Applied case: runtime input and obsolete requests

A TypeScript interface does not validate JSON returned by a server. Parse the untrusted payload into a known domain shape, and reject required values that are unknown or malformed. Do not use `as SomeType` as the only boundary check. Do not return an empty list both for an invalid response and for a real empty result.

For requests that replace each other, abort outdated I/O where supported, and tie completion to the current request ID. An abort can arrive after the response finished, so who owns the result still matters. Close object URLs, listeners and subscriptions when their owner ends. Avoid floating promises whose errors never reach the caller.

Check out-of-order responses, navigating away, malformed JSON or schema values and real empty data. When library exports change, also test the installed package consumer. Automation is written in Python with uv, and only when the user asks for it. Native application modules and tests use their proper language.
