# Kaktos sources

Checked on 2026-11-05 against upstream main, on 2026-11-18 against main at commit `6ee4ef8`, and on
2026-11-25 against main at commit `02f8781`. That last check covered the dependency and version
update: Python 3.10+ in the README, Python 3.14 in `.python-version`, Node 24 in `.nvmrc`, Vite 8.3
and Tailwind CSS 4.3 in `frontend/package.json`. The code under `modules/` did not change, and the
frontend helpers are `styles_for`, `script_for`, `styles_all` and `scripts_all`. When you use Kaktos for a real task, read the current README, then check the real
commands and configuration in the target revision.

- [README](https://github.com/paulocoutinhox/kaktos/blob/main/README.md): purpose, runtime needs,
  built-in Vite build, where files go, frontend helper API, assets, and commands.
- [Entrypoint](https://github.com/paulocoutinhox/kaktos/blob/main/kaktos.py): hands off command handling.
- [System implementation](https://github.com/paulocoutinhox/kaktos/blob/main/modules/system.py): command
  module lookup, empty parameter mapping, route setup, build order, watches, and local port.
  Checked again on 2026-11-18: any non-empty `KAKTOS_DEBUG`, including one loaded from `.env`,
  turns on debug, the dispatcher always passes an empty mapping and reports any
  `ModuleNotFoundError` as a missing command, and routes are imported after the freezer exists.
- [Routes](https://github.com/paulocoutinhox/kaktos/blob/main/modules/routes.py): checked on
  2026-11-18. A single routes module with the generic page route, data routes, and the sitemap and
  robots routes. The sitemap lists page templates whether or not they were frozen.
- [Commands](https://github.com/paulocoutinhox/kaktos/tree/main/modules/commands): checked on
  2026-11-18. `build` recreates `build/`, and `serve` reads an optional port from the second argument.
- [Frontend integration](https://github.com/paulocoutinhox/kaktos/blob/main/modules/frontend.py):
  checked on 2026-11-18. npm install runs when `node_modules/vite` is missing, and `frontend/raw/` is
  copied into `build/` after freezing.
- [Frozen-Flask documentation](https://frozen-flask.readthedocs.io/en/latest/): checked on 2026-11-18.
  Routes without parameters, static files, and logged `url_for` results are frozen by default, and
  `register_generator` adds other URLs.
- [uv run reference](https://docs.astral.sh/uv/reference/cli/#uv-run): checked on 2026-11-18.
  `--no-project` skips looking for a project, but uses a virtual environment found in the current
  directory or a parent.
- [uv Python versions](https://docs.astral.sh/uv/concepts/python-versions/): checked on 2026-11-18.
  uv searches the working directory and its parents for `.python-version`. A local `uv venv` run with
  uv 0.12.19 picked the pinned interpreter over a newer default, and `uv run --no-project` then
  used that `.venv`.
- [pygemstones `log.e`](https://github.com/paulocoutinhox/pygemstones/blob/main/pygemstones/util/log.py):
  checked on 2026-11-18 in main and the published 0.0.14 wheel. It prints the error and calls
  `sys.exit(10)` unless `fatal=False`, which the Kaktos dispatcher and `serve` command do not pass.
- [Jinja documentation](https://jinja.palletsprojects.com/en/stable/): the template engine in use.

Upstream marketing claims about hosting cost and security are not promises that hold everywhere.
This skill's uv command keeps the original Python CLI. No site was built or hosted while writing
this skill.
