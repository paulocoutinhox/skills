# Libraries prompts

Design, checks and trusted publishing for npm and Python libraries. Read
[how to use the prompts](../task-prompts.md) before you copy one.

## npm library

```text
Use npm-library and code-developer from paulocoutinhox/skills.
Before editing, read these files and the references that apply:
- [SKILLS_ROOT]/npm-library/SKILL.md
- [SKILLS_ROOT]/code-developer/SKILL.md
Briefly list the skill paths you found and report any missing package.

Create or prepare [PACKAGE_NAME] in [REPOSITORY] for [PUBLIC_API_AND_CONSUMERS].
Supported runtimes, module formats, license, and release policy: [CONSTRAINTS].
Registry account/scope and GitHub repository/environment: [NON_SECRET_IDENTIFIERS].

Build the requested API and document how to install and use it. Check the package exports, type
declarations, the files that get published, and an install in a realistic consumer project. Set up
CI checks and automatic release through npm trusted publishing, with the needed OIDC permissions and
matching tools. Explain the exact trust setup on the registry side and what starts a release. Trust
can only be added to a package that already exists, so the owner must publish a new package the
first time. Do not use a long-lived token instead.
Check locally what you can, and keep that apart from account setup and a real publish.
This task prepares the package and workflow. It does not allow publishing to the registry.
```

## Python library

```text
Use pypi-library and code-developer from paulocoutinhox/skills.
Before editing, read these files and the references that apply, including the Python profile:
- [SKILLS_ROOT]/pypi-library/SKILL.md
- [SKILLS_ROOT]/code-developer/SKILL.md
Briefly list the skill paths you found and report any missing package.

Create or prepare [DISTRIBUTION_NAME] in [REPOSITORY] for [PUBLIC_API_AND_CONSUMERS].
Supported Python versions, import name, license, and release policy: [CONSTRAINTS].
PyPI/TestPyPI project and GitHub repository/environment: [NON_SECRET_IDENTIFIERS].

Use uv and the right pyproject/build settings. Keep __init__.py files empty and use Ruff.
Build and inspect the wheel and source distribution. Then check install and imports in a clean
consumer environment. Set up CI checks and automatic publishing through PyPI trusted publishing with
the right OIDC identity and environment. Explain the registry setup that is needed and what starts a
release. Keep local package evidence apart from a real upload to the registry.
This task prepares the package and workflow. It does not allow publishing to the registry.
```
