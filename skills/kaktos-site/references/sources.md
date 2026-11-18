# Kaktos sources

Verified on 2026-11-05 against upstream main and rechecked on 2026-11-18 against main at commit
`6ee4ef8`. Read the current README at operational use, then check the target revision's actual
commands/configuration.

- [README](https://github.com/paulocoutinhox/kaktos/blob/main/README.md): purpose, runtime requirements,
  integrated Vite build, directory placement, frontend helper API, assets, and commands.
- [Entrypoint](https://github.com/paulocoutinhox/kaktos/blob/main/kaktos.py): delegates command handling.
- [System implementation](https://github.com/paulocoutinhox/kaktos/blob/main/modules/system.py): command
  module lookup, empty parameter mapping, route initialization, build order, watches, and local port.
  Rechecked on 2026-11-18: any non-empty `KAKTOS_DEBUG`, including one loaded from `.env`, enables debug, the dispatcher always passes an
  empty mapping and reports any `ModuleNotFoundError` as a missing command, and routes import after
  the freezer exists.
- [Routes](https://github.com/paulocoutinhox/kaktos/blob/main/modules/routes.py): verified on
  2026-11-18. A single routes module with the generic page route, data routes, and the sitemap and
  robots routes. The sitemap lists page templates whether or not they were frozen.
- [Commands](https://github.com/paulocoutinhox/kaktos/tree/main/modules/commands): verified on
  2026-11-18. `build` recreates `build/`, and `serve` reads an optional port from the second argument.
- [Frontend integration](https://github.com/paulocoutinhox/kaktos/blob/main/modules/frontend.py):
  verified on 2026-11-18. npm install runs when `node_modules/vite` is missing, and `frontend/raw/` is
  copied into `build/` after freezing.
- [Frozen-Flask documentation](https://frozen-flask.readthedocs.io/en/latest/): verified on 2026-11-18.
  Parameterless routes, static files, and logged `url_for` results are frozen by default, and
  `register_generator` adds other URLs.
- [uv run reference](https://docs.astral.sh/uv/reference/cli/#uv-run): verified on 2026-11-18.
  `--no-project` skips project discovery but uses a virtual environment found in the current or a
  parent directory.
- [uv Python versions](https://docs.astral.sh/uv/concepts/python-versions/): verified on 2026-11-18.
  uv searches the working directory and its parents for `.python-version`. A local `uv venv` run with
  uv 0.12.19 selected the pinned 3.12 over a newer default interpreter, and `uv run --no-project` then
  used that `.venv`.
- [pygemstones `log.e`](https://github.com/paulocoutinhox/pygemstones/blob/main/pygemstones/util/log.py):
  verified on 2026-11-18 in main and the published 0.0.14 wheel. It prints the error and calls
  `sys.exit(10)` unless `fatal=False`, which the Kaktos dispatcher and `serve` command do not pass.
- [Jinja documentation](https://jinja.palletsprojects.com/en/stable/): governing template engine.

Upstream marketing statements about hosting cost and security are not universal guarantees. This
skill's uv invocation preserves the original Python CLI. No site was built or hosted while authoring.
