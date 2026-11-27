# Python package architecture

Use a `src/<import_name>/` layout where it fits, one class or enum per module, and explicit public module paths. Distribution names can contain hyphens. Import names use underscores. Empty `__init__.py` files cannot act as re-export or version modules. So document imports from the real defining modules, and put the version in a dedicated source if needed.

## Metadata and dependencies

Choose a supported build backend and declare its build requirements. Fill in the project name, version or documented dynamic source, description, README content type, Python requirement, license expression and the license files the backend supports, authors, project URLs, and the real dependencies. Expose a CLI through an explicit entrypoint if asked. Add `py.typed` when shipping inline typing, and make sure it is included in the built artifacts.

Keep runtime dependency ranges apart from locked development tools. Commit `uv.lock` so CI and contributors get the same results. Do not publish the local virtual environment or paths from the developer's machine. Avoid dynamic imports and compatibility branches for old runtimes unless they are explicitly required. Fix circular imports through architecture and shared types, not `if TYPE_CHECKING`.

## Build and consumer verification

Use a release dependency group with a pinned, compatible build frontend, a backend where needed, and Twine for checking metadata. Run lint, formatting, and tests before building. Build a source distribution and a wheel. Inspect every filename in the archives for missing modules, unexpected credentials, caches, logs, private fixtures, and generated junk.

Install the wheel into a fresh temporary environment outside the repository, and import public modules from there, so the source checkout cannot hide packaging errors. Run typical features, and the CLI if there is one. When the frontend builds the wheel straight from the checkout, also build and install a wheel from the source distribution. Check the resulting package behavior, typing data, assets, and license. A wheel that works only because the current directory contains `src/` is broken.

Test real installed-consumer behavior in a temporary environment, not just a check that the archive exists. Do not create a smoke-test script unless the user explicitly asks for that automation. If asked, it must use Python and uv. Use platform-specific wheels and a suitable build matrix when native extensions exist. A single pure-Python wheel does not promise support for native platforms.

Document installation, public imports, API examples, errors, the supported runtime, contributor commands, and release behavior. Keep `AGENTS.md` describing the current architecture and commands, not implementation history.
