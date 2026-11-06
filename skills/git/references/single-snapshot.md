# An explicitly authorized single-root snapshot

Use this only when the user or applicable repository contract explicitly requests a repository with
one parentless commit. A request to make one commit for today's change normally means an ordinary
commit on existing history. It does not imply this procedure, force-push permission or branch deletion.

## Confirm scope and preserve the complete tree

Record the exact repository, branch, local tip, remote URL/tip, configured human author and whether
authorization covers local rewriting, the named remote branch or both. Honor an existing applicable
standing authorization. Do not ask again for an already authorized step. A history instruction for
one repository does not authorize rewriting a sibling app or skills repository.

Inspect tracked, untracked, staged, unstaged and ignored paths. Review legitimate owner changes under
the actual delivery scope. Stage explicit reviewed paths and scan the exact index for signing files,
credentials, runtime data, caches and accidental generated outputs. Report only suspicious filenames/
rule identifiers. A secret-field name in a sanitized example is not itself a leaked credential.

Compare the complete prospective tree with the original. Explain intended removals and preserve all
unaffected source, file modes, submodules, licenses and native projects. Deleting a publishing tool
requires finding its README/AGENTS references, scripts, CI hooks, examples, dependencies and ignored
outputs. Do not delete valid app configuration, SDK integration or a native host merely because its
filename contains 'release', 'review' or 'store'. Validate the actual remaining build workflow.

Do not remove `.git` to erase history. That also loses repository configuration, refs, hooks and
recovery information. Record the original tip for recovery through the existing reflog or an approved
restricted receipt. Do not create backup branches/tags when repository policy forbids them.

## Construct the reviewed root deliberately

For an existing parentless tip, an authorized amend can preserve the one-root structure through the
normal commit workflow. For an explicit root replacement from a reviewed index, Git's plumbing can
create a parentless commit:

```text
git write-tree
git commit-tree <reviewed-tree-id> -m "<required-short-human-subject>"
git rev-list --count <new-root-id>
git show -s --format=fuller <new-root-id>
git diff --stat <old-tip-id> <new-root-id>
git update-ref refs/heads/<branch> <new-root-id> <expected-old-local-tip>
```

These are separate operations with returned IDs, not literal angle-bracket arguments or an unattended
script. No `-p` argument means no parent. `commit-tree` does not run normal commit hooks. Use only the
project-permitted workflow, satisfy its required checks/hooks and do not use plumbing to bypass a
failed hook. Verify the count is one, the tree is the reviewed index, and author/message satisfy the
repository contract before moving the ref. Use the expected-old local tip to detect concurrent edits.

If a local ref update fails, re-read state rather than deleting locks or overwriting another writer.
Do not change the checked-out branch, reset the working tree or discard unstaged owner changes just
to complete the rewrite. Report any index/worktree differences from the delivered snapshot.

## Publish only the authorized branch with an explicit lease

Read/fetch and inspect the actual remote tip before rewriting. An unexpected remote change needs
review and preservation. Record the observed SHA independently of a background-updated tracking ref.
For an authorized publication of that exact branch:

```text
git push --force-with-lease=refs/heads/<branch>:<observed-remote-sha> <remote> refs/heads/<branch>:refs/heads/<branch>
git ls-remote <remote> refs/heads/<branch>
```

The explicit expected remote SHA is the protection. Do not silently advance it after rejection or use
unconditional `--force`. A failed push can leave the reviewed new root local while the remote remains
unchanged. Inspect both states before retrying. Do not add a PR/feature branch to a main-only workflow.

Verify local/remote tips match, reachable branch count is one and the worktree has only understood
remaining changes. Inspect the actual CI run for that SHA and distinguish pending, failed and passed.
Do not report a green run from the replaced commit. Rewriting branch ancestry does not erase other
refs, reflogs, hosting retention or leaked credentials. Credential rotation is a separate operation.

If an execution approval rejects the rewrite, preserve the reviewed result and cite the exact action
and stated reason. Check applicable authorization and tree-preservation evidence. Do not disguise the
same denied mutation through another tool. Request any genuinely missing approval only after the
concrete result is ready and independent authorized work is complete.
