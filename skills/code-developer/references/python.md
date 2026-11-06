# Python

## Layout and dependencies

Use the project's declared Python target. For a new project, verify the current supported stable version and dependency compatibility before pinning it. Use `pyproject.toml`, uv for dependency and environment management, and Ruff for linting and formatting. Use a `src/` layout for distributable packages when appropriate. Commit `uv.lock` for reproducible development. Libraries declare compatible dependency ranges separately from the locked development environment.

Importable module and package names use underscores because hyphens are not valid identifiers. Give
each class and enum its own named file, including support/helper classes. Every `__init__.py` must
be completely empty, without comments, docstrings, reexports, version declarations, or initialization
code. Put public definitions and version constants in explicit modules. Do not use `TYPE_CHECKING`
or `if TYPE_CHECKING`. Resolve import cycles by correcting dependencies and separating shared types.
Use supported deferred or quoted annotations when needed by the selected runtime.

## Implementation

Use type annotations for meaningful interfaces. Prefer dataclasses or ordinary classes for explicit state and immutable value objects when appropriate. Avoid broad `Any`, mutable default arguments, global mutable configuration, dynamic imports, wildcard imports, and runtime annotation tricks. Use `pathlib`, context managers, parameterized database queries, and explicit text encodings. Keep exceptions specific and include useful context without secrets.

Async code must avoid blocking the event loop. Use structured task ownership, propagate cancellation, close clients and generators, and bound concurrency. Offload genuinely blocking work through the chosen framework's supported mechanism. Do not catch `BaseException` to hide cancellation or interpreter exit. Use argument arrays rather than shell concatenation for subprocesses and set timeouts for external operations.

## Tooling

```bash
uv sync --locked
uv run ruff check .
uv run ruff format --check .
uv run python -m unittest discover -s tests
```

Use pytest or a type checker when already adopted or justified by the project. Run tests against installed artifacts for packaging changes. Ruff is a linter and formatter, not a dependency manager or a type checker. Do not add every optional tool automatically.

## Applied case: concurrent fulfillment

For a purchase-delivery method, separate parsing/authentication, product lookup, idempotency decision, durable grant and acknowledgment. A preceding `exists()` query does not protect two simultaneous requests. Put the unique purchase identity and state transition under the actual database constraint/transaction. Return the existing verified delivery only when that is the deliberate idempotency contract, not as a catch-all for database failure.

Keep network work outside a database lock unless the consistency design requires it. A timeout after an external operation can leave an uncertain outcome, so retain its correlation identity and reconcile before repeating it. Use `asyncio.TaskGroup` or the actual framework's structured equivalent for related owned work. If cancellation is caught for cleanup, propagate it after restoring the invariant. Do not turn cancellation into an ordinary empty result.

For an explicitly requested standalone script, use Python with uv and declare its actual dependencies and version. Keep importable initializers empty. The repository's descriptive skills do not bundle domain scripts.

Verify duplicate delivery, one worker failing before commit, another arriving after commit, and cancellation during an external wait. Assertions should concern one durable benefit and correct observed status, not internal call counts alone. The selected Python version's [task/cancellation contract](https://docs.python.org/3/library/asyncio-task.html) governs the exact behavior.
