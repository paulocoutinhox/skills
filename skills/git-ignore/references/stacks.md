# Stack-specific patterns

Use only blocks that match the actual repository. Adjust roots and exceptions to its build system. These are original working presets informed by common ecosystem templates.

| Stack | Common generated or local paths | Preserve or inspect carefully |
| --- | --- | --- |
| Python | `__pycache__/`, `*.py[cod]`, `.venv/`, `venv/`, `*.egg-info/`, `.pytest_cache/`, `.mypy_cache/`, `.ruff_cache/`, `.tox/`, `.nox/`, `.coverage*`, `htmlcov/`, `build/`, `dist/`. | Source packages, `pyproject.toml`, lockfile, typing markers, migrations. Scope `.coverage*` if named fixtures exist. |
| Node/frontend | `node_modules/`, `.npm/`, `.pnpm-store/`, `.yarn/cache/` if not deliberately versioned, `dist/`, `coverage/`, `.vite/`, `.next/`, `.nuxt/`, `.output/`, `.angular/cache/`, `*.tsbuildinfo`, Playwright reports. | Lockfiles, public assets, workspace config, intentionally versioned Yarn releases and zero-install cache. |
| Swift/Xcode | `.build/`, `.swiftpm/` local state as applicable, `DerivedData/`, `xcuserdata/`, `*.xcuserstate`, `*.ipa`, `*.dSYM/`, archives. | `.xcodeproj` and `.xcworkspace` shared metadata, package manifests and resolved dependencies according to project policy. |
| Kotlin/Android/Java | `.gradle/`, `.kotlin/`, `build/`, `out/`, `local.properties`, `*.apk`, `*.aab`, signing stores, local heap dumps. | Gradle wrapper, version catalogs, manifests, resources, shared IDE code styles when tracked. |
| C/C++ | `cmake-build-*/`, `CMakeFiles/`, `CMakeCache.txt`, generated build trees, `*.o`, `*.obj`, `*.a`, `*.so`, `*.dylib`, `*.dll`, `*.exe`, compiler/debug output. | Vendored binaries or fixtures when deliberately required, source headers, build presets. |
| Rust | `target/`. | Cargo manifests and the repository's Cargo.lock policy. |
| Go | Specific `bin/`, coverage, temporary test binaries, generated executable paths. | `go.mod`, `go.sum`, required generated source. Do not hide every vendor tree without checking policy. |
| .NET | `bin/`, `obj/`, `.vs/`, test results, package archives, local user project files. | Solution/project files, lockfiles when used, required tools. |
| PHP | `vendor/` when dependencies are installed, PHPUnit caches and reports, local environment files. | Composer manifests/lockfile according to policy and app source. |
| Ruby | `.bundle/`, local `vendor/bundle/`, coverage, temporary/log output. | Gemfile, lockfile policy, gemspec, application assets. |
| Dart/Flutter | `.dart_tool/`, `.pub-cache/`, `build/`, local plugin metadata and generated ephemeral directories. | Source, platform project files, pubspec, lockfile according to application/library policy. |
| Data and notebooks | `.ipynb_checkpoints/`, local databases, dumps, and generated exports identified by the project. | Reviewed sample datasets and notebooks. Never blindly ignore every database or CSV extension. |
| IaC and containers | `.terraform/`, `*.tfstate`, `*.tfstate.*`, local plans, private variable files, local overrides. | Terraform configuration and `.terraform.lock.hcl`, Dockerfiles, sanitized examples. |

Signing stores, cloud credentials, private keys, API tokens, access logs, database snapshots, crash dumps, and production connection strings deserve explicit review. Exclude known private paths such as `.aws/`, `.ssh/`, `secrets/`, `.env*`, and service-account credentials, while keeping sanitized templates visible. Do not exclude an entire source configuration directory just because a local environment file is private.

For Playwright suites, exclude saved authenticated state such as `playwright/.auth/`, including the
corresponding path in each frontend package. Use the actual chosen path when different. Cookies and
headers in that state can authenticate as the test user. Preserve sanitized auth-response fixtures
and application auth modules. Ignoring reports alone does not protect a separate storage-state file.
