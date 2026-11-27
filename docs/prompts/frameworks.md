# Frameworks and native cores prompts

Kaktos sites, Fastkit apps and XPLPC mobile apps. Read [how to use the prompts](../task-prompts.md)
before you copy one.

## Kaktos site

```text
Use kaktos-site from paulocoutinhox/skills.
Read [SKILLS_ROOT]/kaktos-site/SKILL.md and name the path really loaded. If it is missing, say so.

Create [SITE_AND_PAGES] in [KAKTOS_CHECKOUT] for [AUDIENCE_LANGUAGES_AND_DESIGN].
First read the current Kaktos README/features, the command dispatcher, modules/config.py and
modules/routes.py. Put Jinja layouts/pages/fragments, Python modules/data, processed frontend
assets, and raw root files in the right places. Link pages with url_for. Register Frozen-Flask
generators for dynamic URLs that no frozen page links to. Use the built-in build/dev/serve commands.
Explain any outside form or shop service the brief needs. Add custom Python commands only if asked,
through the real dispatcher. Check production links and assets, SEO metadata, responsive and
keyboard behavior, and the real build output. Deliver the source, current AGENTS.md instructions,
checks, and any integrations still open.
```

## Fastkit application

```text
Use fastkit-app from paulocoutinhox/skills.
Read [SKILLS_ROOT]/fastkit-app/SKILL.md and name the path really loaded. If it is missing, say so.

Implement [FEATURE] in [FASTKIT_CHECKOUT] for [SURFACES_TENANTS_ROLES_AND_LOCALES].
Read the current README/features, architecture, domain guides, and manage.py help. Confirm the
Python version the manifest requires. Extend the real models/schemas/services/routes/resource
definitions instead of rebuilding systems that already exist. Reuse the real queue/cache, upload,
account, and gateway contracts. Give each class and enum its own module and keep code modular and
readable.
Be explicit about which environment you use and about any seeding that deletes data. If needed,
add a Python command only through the documented extension method. Check authorization, tenant
separation, locale behavior, background and cached effects, and the site/admin/API consumers.
Deliver code, the current structure and commands, real test evidence, and any outside setup still
needed.
```

## XPLPC mobile

```text
Use xplpc-mobile from paulocoutinhox/skills.
Read [SKILLS_ROOT]/xplpc-mobile/SKILL.md and name the path really loaded. If it is missing, say so.

Implement [APP_AND_SHARED_CPP_FEATURE] in [REPOSITORY] for [NATIVE_PLATFORMS_AND_TOOLCHAINS].
Read the current upstream README, the language and target guides, and the task help. Keep views and
view models, bridge adapters, native mappings, and C++ domain services apart. Define parameters,
results and errors, startup, the callback thread, owner lifetime, cancellation, and who owns each
buffer. Use the real native build and package tasks. Check delayed calls, teardown, invalid
responses, DTO serialization in release builds, and the platform slices in each artifact. Deliver
readable code, mapping and structure docs, current commands, real evidence, and hardware and signing
limits. Do not make up bridge APIs.
```
