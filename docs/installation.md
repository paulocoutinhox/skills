# Installation

## Install

Use the [Vercel Skills CLI](https://github.com/vercel-labs/skills/tree/v1.9.0) with Node.js 22.20 or
later and npm. You can run each command directly from your terminal.

Install the whole collection for Codex and Claude Code at user scope (for your user account).

```bash
npx skills@1.9.0 add paulocoutinhox/skills -g -a codex claude-code -s '*'
```

Pick a skill by name and choose a target client. Run this example from your project root. Add
`-g` to install at user scope.

```bash
npx skills@1.9.0 add paulocoutinhox/skills -a claude-code -s code-review
```

| Client | User scope | Project scope |
| --- | --- | --- |
| Codex (`codex`) | `~/.agents/skills/` | `.agents/skills/` |
| Claude Code (`claude-code`) | `~/.claude/skills/` | `.claude/skills/` |

A project install records the source and revision in `skills-lock.json`. Clients that read a
shared skills directory can find the same install.

After you install, use `npx skills@1.9.0 list -g` for user scope or `npx skills@1.9.0 list` for
project scope. Installing a skill can replace a package with the same name in that scope.

## Update installed skills

Update the whole Paulo Skills collection at user scope. This runs the install command again. It
refreshes every installed copy and also installs skills added to the collection since the last
install. Back up any local edits to the installed copies first.

```bash
npx skills@1.9.0 add paulocoutinhox/skills -g -a codex claude-code -s '*'
```

Update every skill the CLI manages at user scope, including skills from other collections.

```bash
npx skills@1.9.0 update -g
```

Update only some skills by passing their names.

```bash
npx skills@1.9.0 update code-review git -g
```

Use `-p` instead of `-g` for a project install, and run the install command without `-g` from the
project root. The CLI cannot filter updates by source. Use the install command to refresh only this
collection. Remove skills that are no longer in the collection yourself, by name.

## Remove installed skills

Remove the skills that came from this collection at user scope.

```bash
npx skills@1.9.0 remove paulocoutinhox/skills -g
```

Leave out `-g` and run from the project root to remove a project install. To remove one skill, use
its installed name in place of `paulocoutinhox/skills`. [Skills CLI command reference](https://github.com/vercel-labs/skills/blob/v1.9.0/docs/commands.md)
