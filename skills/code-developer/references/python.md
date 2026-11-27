# Python

## Layout and dependencies

Use the project's declared Python target. For a new project, check the current supported stable version and dependency compatibility before you pin it. Use `pyproject.toml`, uv for dependency and environment management, and Ruff for linting and formatting. Use a `src/` layout for packages you distribute when it fits. Commit `uv.lock` for reproducible development. Libraries declare compatible dependency ranges apart from the locked development environment.

Importable module and package names use underscores because hyphens are not valid identifiers. Give
each class and enum its own named file, including support and helper classes. Every `__init__.py`
must be completely empty, without comments, docstrings, reexports, version declarations, or
initialization code. Put public definitions and version constants in explicit modules. Do not use
`TYPE_CHECKING` or `if TYPE_CHECKING`. Fix import cycles by correcting dependencies and moving
shared types apart. Use supported deferred or quoted annotations when the chosen runtime needs them.

## Implementation

Use type annotations for important interfaces. Prefer dataclasses or ordinary classes for clear state and immutable value objects when they fit. Avoid broad `Any`, mutable default arguments, global mutable configuration, dynamic imports, wildcard imports, and runtime annotation tricks. Use `pathlib`, context managers, parameterized database queries, and explicit text encodings. Keep exceptions specific and include useful context without secrets.

Async code must not block the event loop. Give each task a clear owner, pass cancellation on, close clients and generators, and limit concurrency. Move truly blocking work off the loop through the chosen framework's supported method. Do not catch `BaseException` to hide cancellation or interpreter exit. Use argument arrays instead of joined shell strings for subprocesses, and set timeouts for external operations.

## Tooling

```bash
uv sync --locked
uv run ruff check .
uv run ruff format --check .
uv run python -m unittest discover -s tests
```

Ruff's default `line-length` of 88 wraps ordinary calls. Under the owner's single-line call convention, set a wide width and turn off the magic trailing comma. Otherwise it keeps a call split into one argument per line even when it fits:

```toml
[tool.ruff]
line-length = 320

[tool.ruff.format]
skip-magic-trailing-comma = true

[tool.ruff.lint.isort]
split-on-trailing-comma = false
```

The isort setting avoids Ruff's incompatibility warning. Ruff then joins calls that were wrapped before by itself. Keep each message in one string literal instead of implicit joining of adjacent literals.

Use pytest or a type checker when the project already uses one or has a reason for it. Run tests against installed artifacts for packaging changes. Ruff is a linter and formatter, not a dependency manager or a type checker. Do not add every optional tool by default.

## Applied case: concurrent fulfillment

For a purchase-delivery method, keep parsing and authentication, product lookup, the idempotency decision, the durable grant and the acknowledgment apart. An `exists()` query run first does not protect two requests that arrive at the same time. Put the unique purchase ID and the state change under the real database constraint or transaction. Return the existing verified delivery only when that is the chosen idempotency contract, not as a catch-all for database failure.

Keep network work outside a database lock unless the consistency design needs it. A timeout after an external operation can leave the outcome unknown. Keep its correlation ID and check the real result before you repeat it. Use `asyncio.TaskGroup` or the real framework's structured equivalent for related work that the code owns. If you catch cancellation for cleanup, raise it again after you restore the rule. Do not turn cancellation into an ordinary empty result.

For a standalone script the user asks for, use Python with uv and declare its real dependencies and version. Keep importable initializers empty. The repository's descriptive skills do not bundle domain scripts.

Check duplicate delivery, one worker failing before commit, another arriving after commit, and cancellation during an external wait. Assertions should check one durable benefit and the correct observed status, not only internal call counts. The chosen Python version's [task/cancellation contract](https://docs.python.org/3/library/asyncio-task.html) defines the exact behavior.
