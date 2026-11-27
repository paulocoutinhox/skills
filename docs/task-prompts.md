# Task prompts

Copy a prompt, replace the inputs in brackets and paste it into the agent doing your task. Set
`[SKILLS_ROOT]` to the full path of the folder that holds this collection's installed packages, or
its local `skills/` folder that the agent can read. Write out `~` as the full path. Reading a
checkout does not install or register a skill. When another package has the same name, check which
path was really loaded.

Each prompt names `paulocoutinhox/skills`, the files to read, the expected results and the checks.
Naming the owner alone does not load the skills or override client permissions. The general
repository rules live in [AGENTS.md](../AGENTS.md). The [README catalog](../README.md#-skills)
links straight to each skill's steps.

| Group | Prompts |
| --- | --- |
| [Software development](prompts/development.md) | [New project](prompts/development.md#new-project), [Implement a feature](prompts/development.md#implement-a-feature), [Fix or refactor](prompts/development.md#fix-or-refactor), [Documentation](prompts/development.md#documentation), [Code review](prompts/development.md#code-review), [Security audit](prompts/development.md#security-audit), [Editor configuration](prompts/development.md#editor-configuration), [Ignore rules](prompts/development.md#ignore-rules), [Git delivery](prompts/development.md#git-delivery), [Git single-root snapshot](prompts/development.md#git-single-root-snapshot) |
| [Libraries](prompts/libraries.md) | [npm library](prompts/libraries.md#npm-library), [Python library](prompts/libraries.md#python-library) |
| [Frontend applications](prompts/frontend.md) | [Vue application](prompts/frontend.md#vue-application), [React application](prompts/frontend.md#react-application), [Tailwind interface](prompts/frontend.md#tailwind-interface) |
| [Frameworks and native cores](prompts/frameworks.md) | [Kaktos site](prompts/frameworks.md#kaktos-site), [Fastkit application](prompts/frameworks.md#fastkit-application), [XPLPC mobile](prompts/frameworks.md#xplpc-mobile) |
| [Haylen](prompts/haylen.md) | [Haylen application](prompts/haylen.md#haylen-application), [Haylen game](prompts/haylen.md#haylen-game), [Haylen plugin](prompts/haylen.md#haylen-plugin), [Haylen upgrade](prompts/haylen.md#haylen-upgrade) |
| [Python services](prompts/python-services.md) | [Python queue](prompts/python-services.md#python-queue), [Python cache](prompts/python-services.md#python-cache) |
| [Testing](prompts/testing.md) | [Web testing](prompts/testing.md#web-testing), [Android testing](prompts/testing.md#android-testing), [Apple testing](prompts/testing.md#apple-testing), [Cloud batch](prompts/testing.md#cloud-batch) |
| [Store release and monetization](prompts/store-release.md) | [Apple app delivery](prompts/store-release.md#apple-app-delivery), [Google Play delivery](prompts/store-release.md#google-play-delivery), [RevenueCat](prompts/store-release.md#revenuecat), [Mobile release with subscriptions](prompts/store-release.md#mobile-release-with-subscriptions), [Playgama](prompts/store-release.md#playgama) |
| [Publications and content](prompts/content.md) | [Book](prompts/content.md#book), [Workbook](prompts/content.md#workbook), [Social post](prompts/content.md#social-post), [Social thumbnail](prompts/content.md#social-thumbnail), [Remotion video](prompts/content.md#remotion-video) |
| [Research](prompts/research.md) | [Reliable information](prompts/research.md#reliable-information) |
| [Planning](prompts/planning.md) | [Markdown Kanban](prompts/planning.md#markdown-kanban) |
| [Skill maintenance](prompts/skill-maintenance.md) | [Create a skill](prompts/skill-maintenance.md#create-a-skill), [Update skill knowledge](prompts/skill-maintenance.md#update-skill-knowledge) |
