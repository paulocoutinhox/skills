# Python package architecture

Use a `src/<import_name>/` layout where appropriate, one class or enum per module, and explicit public module paths. Distribution names can contain hyphens. Import identifiers use underscores. Empty `__init__.py` files cannot serve as reexport or version modules, so document imports from the actual defining modules and put the version in a dedicated source if needed.

## Metadata and dependencies

Choose a supported build backend and declare its build requirements. Populate project name, version or documented dynamic source, description, README content type, Python requirement, license expression and license files supported by the backend, authors, project URLs, and actual dependencies. Expose a CLI through an explicit entrypoint if requested. Add `py.typed` when distributing inline typing and ensure it is included in built artifacts.

Separate runtime dependency ranges from locked development tooling. Commit `uv.lock` for CI and contributor reproducibility. Do not publish the local virtual environment or developer machine paths. Avoid dynamic imports and compatibility branches for old runtimes unless explicitly required. Resolve circular imports through architecture and shared types rather than `if TYPE_CHECKING`.

## Build and consumer verification

Use a release dependency group containing a pinned compatible build frontend, backend where needed, and Twine for metadata checking. Run lint, formatting, and tests before building. Build a source distribution and wheel. Inspect every archived filename for missing modules, unexpected credentials, caches, logs, private fixtures, and generated junk.

Install the wheel into a fresh temporary environment outside the repository and import public modules from there so the source checkout cannot mask packaging errors. Exercise representative functionality and the CLI if present. Build and install a wheel from the source distribution as a separate check. Verify the resulting package behavior, typing data, assets, and license. A wheel that works only because the current directory contains `src/` is broken.

Use actual installed-consumer behavior in a temporary environment, rather than an archive-exists assertion. Do not create a smoke-test script unless the user explicitly requests that automation. If requested, it must use Python and uv. Use platform-specific wheels and a suitable build matrix when native extensions exist. A single pure-Python wheel is not a promise of native-platform support.

Document installation, public imports, API examples, errors, supported runtime, contributing commands, and release behavior. Keep `AGENTS.md` descriptive of current architecture and commands rather than implementation history.
