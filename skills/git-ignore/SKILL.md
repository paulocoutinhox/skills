---
name: git-ignore
description: Create or audit .gitignore from actual repository outputs and privacy boundaries, preserving source, lockfiles and shared configuration. Use for ignore design, accidental tracking, nested-rule problems, and artifact exposure review.
license: MIT
---

# Git Ignore

Define which untracked local/generated files should stay out of version control. Treat ignore rules as repository hygiene, not access control, secret detection or credential revocation.

## Inventory before excluding

Read the repository's build/package/test tools and inspect tracked, untracked and ignored filenames. Identify real output roots, caches, runtime data, local environment files, credentials, editor state, operating-system artifacts and required reproducibility inputs.

Use [the base template](assets/gitignore) and [stack guidance](references/stacks.md) selectively. A source configuration directory can contain both shared settings and a private local override. Ignore the private path, not the entire directory. A legitimate source asset or fixture must remain visible even if its extension is commonly generated elsewhere.

## Pattern semantics

A slash at the beginning or in the middle anchors the pattern relative to the ignore file's directory. A trailing slash alone restricts matching to directories without anchoring the depth: `build/` matches both `build/` and `apps/web/build/`, while `/build/` matches only the former from a root ignore file. Unqualified names can match below that directory. `**` can span directory levels. Later applicable patterns and nearer ignore files affect the result. A leading `!` can re-include an earlier exclusion only when its parent remains traversable.

For example, ignoring `assets/` and then adding `!assets/logo.svg` does not generally recover the logo because Git stops traversing the excluded parent. Use a scoped content exclusion and explicit directory traversal when that exception is truly required. Test the actual path instead of relying on a plausible-looking pattern.

Repository-wide conventions belong in `.gitignore`. Personal machine choices can belong in `.git/info/exclude` or a global ignore file. Do not impose one contributor's whole editor setup on the team without inspecting existing policy.

## Preserve versus exclude

| Exclude when local/generated | Preserve when part of the project |
| --- | --- |
| Virtual environments and dependency installs | Manifests, chosen lockfiles and typing markers |
| Compiler/build output and caches | Source, migrations, required generated source and wrappers |
| Logs, reports, temporary databases | Reviewed fixtures and sanitized sample datasets |
| User-specific IDE state | Shared project settings and formatter configuration |
| Private environment/signing/cloud files | Verified sanitized examples and public certificates when required |
| OS metadata | Publication source artwork, fonts and production source files |

Do not ignore every JSON/YAML, dotfile, PDF, image, database or archive by extension. Do not exclude all JARs if Gradle's wrapper requires a committed wrapper JAR. Do not discard lockfiles because the output directory is generated. `dist/` can be ignored in Git while deliberately included in an npm package's file allowlist.

Signing material includes `.p8`, private PEM/key files, `.p12`, `.pfx`, `.jks`, keystores and provisioning profiles when those are private job inputs. Review the actual contents and purpose. An extension alone cannot identify every secret, and a sanitized example exception is not permission to retain live values.

Saved browser authentication state is private input, not an ordinary test fixture. The template
excludes Playwright's recommended `playwright/.auth/` directory, including that path in nested app
roots. Ignore a different selected state path explicitly. Do not hide every JSON file or all auth
source modules to protect one credential file. Check tracked files separately.

## Verify actual behavior

Use `git check-ignore -v --no-index -- path` for representative positive and negative cases. The `--no-index` check tests rule intent even for a tracked path. It does not untrack anything.

Inspect `git ls-files` separately. If a tracked log continues changing after a new ignore rule, that is expected Git behavior. Remove only the authorized path from the index while preserving its local copy when requested. Verify the staged deletion and the remaining local file.

Test nested rules and negations using real paths or isolated fixtures. Include source modules, lockfiles, wrapper files, examples and required assets as negative cases. Confirm no broad rule hides a source file that a future contributor needs to add.

## Real exposure requires incident handling

If a real credential entered source/history, avoid echoing it, identify the affected account/key, stop it from entering another delivery, and arrange authorized rotation/revocation. Determine whether logs, artifacts, releases or remote copies also contain it. History remediation and account actions need their actual scope. A new ignore rule or file deletion does not revoke the credential.

A clean scan is useful evidence, not proof that no sensitive data exists. Inspect the staged content as well as filenames. Never promise that ignore rules prevent `git add -f`, copied secret values or leaked logs.

## Delivery and foundations

Deliver focused rules, examples of paths intentionally ignored/retained, verification evidence and any tracked exposure needing action. Do not create a generator, scanner or scheduled updater as part of this descriptive skill.

The [gitignore manual](https://git-scm.com/docs/gitignore) governs precedence and negation. Chacon and Straub's [Pro Git](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository) explains the separate tracked/index state. Apply these models before borrowing ecosystem template lists. See [detailed privacy rules](references/rules.md), [sources](references/sources.md) and [license](LICENSE.md).
