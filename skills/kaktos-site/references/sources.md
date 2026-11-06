# Kaktos sources

Verified on 2026-11-05 against upstream main. Read the current README at operational use, then check
the target revision's actual commands/configuration.

- [README](https://github.com/paulocoutinhox/kaktos/blob/main/README.md): purpose, runtime requirements,
  integrated Vite build, directory placement, frontend helper API, assets, and commands.
- [Entrypoint](https://github.com/paulocoutinhox/kaktos/blob/main/kaktos.py): delegates command handling.
- [System implementation](https://github.com/paulocoutinhox/kaktos/blob/main/modules/system.py): command
  module lookup, empty parameter mapping, route initialization, build order, watches, and local port.
- [Jinja documentation](https://jinja.palletsprojects.com/en/stable/): governing template engine.

Upstream marketing statements about hosting cost and security are not universal guarantees. This
skill's uv invocation preserves the original Python CLI. No site was built or hosted while authoring.
