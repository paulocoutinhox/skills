---
name: git-ignore
description: Create or audit .gitignore from the repository's real outputs and privacy boundaries, keeping source, lockfiles and shared configuration. Use for ignore design, files tracked by mistake, nested-rule problems, and reviewing exposed build output or private files.
license: MIT
---

# Git Ignore

Decide which untracked local or generated files should stay out of version control. Treat ignore rules as repository housekeeping, not access control, secret detection or credential revocation. Whitespace and encoding conventions belong in `.editorconfig`. Staging, committing and cleaning up history belong to the repository's Git workflow.

## Inventory before excluding

Read the repository's build, package and test tools, and check tracked, untracked and ignored filenames. Find the real output roots, caches, runtime data, local environment files, credentials, editor state, operating-system files and the inputs needed to rebuild the project the same way.

Use only the parts of [the base template](assets/gitignore) and [stack guidance](references/stacks.md) that fit. A source configuration directory can hold both shared settings and a private local override. Ignore the private path, not the whole directory. A valid source asset or fixture must stay visible even if files with its extension are often generated elsewhere.

## Pattern semantics

A slash at the beginning or in the middle anchors (ties) the pattern to the ignore file's directory. A trailing slash alone limits matching to directories without tying it to a depth: `build/` matches both `build/` and `apps/web/build/`, while `/build/` matches only the former from a root ignore file. Unqualified names can match below that directory. `**` can span directory levels. Later applicable patterns and nearer ignore files affect the result. A leading `!` can bring back an earlier exclusion only when Git can still enter its parent directory.

For example, ignoring `assets/` and then adding `!assets/logo.svg` does not bring back the logo, because Git does not enter the excluded parent. When that exception is truly needed, exclude the directory's contents with `assets/*` and then add `!assets/logo.svg`. For a deeper file, bring back each directory in between, one at a time, for example `assets/*`, `!assets/brand/`, `assets/brand/*` and `!assets/brand/logo.svg`. Test the real path instead of trusting a pattern that looks right.

Repository-wide conventions belong in `.gitignore`. Personal machine choices can belong in `.git/info/exclude` or a global ignore file. Do not force one contributor's whole editor setup on the team without checking the existing policy.

## Preserve versus exclude

| Exclude when local/generated | Preserve when part of the project |
| --- | --- |
| Virtual environments and dependency installs | Manifests, chosen lockfiles and typing markers |
| Compiler/build output and caches | Source, migrations, required generated source and wrappers |
| Logs, reports, temporary databases | Reviewed fixtures and sanitized sample datasets |
| User-specific IDE state | Shared project settings and formatter configuration |
| Private environment/signing/cloud files | Verified sanitized examples and public certificates when required |
| OS metadata | Publication source artwork, fonts and production source files |

Do not ignore every JSON/YAML, dotfile, PDF, image, database or archive by extension. Do not exclude all JARs if Gradle's wrapper requires a committed wrapper JAR. Do not drop lockfiles because the output directory is generated. `dist/` can be ignored in Git and still be included on purpose in an npm package's file allowlist.

Signing material includes `.p8`, private PEM/key files, `.p12`, `.pfx`, `.jks`, keystores and provisioning profiles when those are private job inputs. Review the real contents and purpose. An extension alone cannot find every secret, and an exception for a sanitized example is not permission to keep live values.

Saved browser authentication state is private input, not an ordinary test fixture. The template
excludes Playwright's recommended `playwright/.auth/` directory, including that path in nested app
roots. Ignore a different chosen state path explicitly. Do not hide every JSON file or all auth
source modules to protect one credential file. Check tracked files separately.

## Check real behavior

Use `git check-ignore -v --no-index -- path` for typical paths that should and should not match. The `--no-index` check tests what the rule intends even for a tracked path. It does not untrack anything.

Check `git ls-files` separately. If a tracked log keeps changing after a new ignore rule, that is normal Git behavior. When the user asks to untrack a file, run `git rm --cached -- <path>` for only the authorized path. This stages its removal and keeps the local copy. Verify the staged deletion with `git diff --cached --name-status` and confirm the local file still exists. Committing that change follows the repository's ordinary Git workflow.

Test nested rules and negations with real paths or isolated fixtures. Include source modules, lockfiles, wrapper files, examples and required assets as paths that must not match. Confirm no broad rule hides a source file that a future contributor needs to add.

## Real exposure requires incident handling

If a real credential got into source or history, do not print it, find the affected account or key, stop it from entering another delivery, and arrange authorized rotation or revocation. Find out whether logs, build files, releases or remote copies also hold it. History cleanup and account actions need their real scope. A new ignore rule or file deletion does not revoke the credential.

A clean scan is useful evidence, not proof that no sensitive data exists. Check the staged content as well as filenames. Never promise that ignore rules prevent `git add -f`, copied secret values or leaked logs.

## Delivery and foundations

Deliver focused rules, examples of paths that are ignored or kept on purpose, verification evidence and any tracked exposure that needs action. Do not create a generator, scanner or scheduled updater as part of this descriptive skill.

The [gitignore manual](https://git-scm.com/docs/gitignore) defines precedence and negation. Chacon and Straub's [Pro Git](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository) explains the separate tracked and index state. Apply these models before you borrow template lists from other ecosystems. See [detailed privacy rules](references/rules.md), [sources](references/sources.md) and [license](LICENSE.md).
