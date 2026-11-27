# An explicitly authorized single-root snapshot

Use this only when the user or the repository contract that applies clearly asks for a repository
with one parentless commit. A request to make one commit for today's change usually means an
ordinary commit on existing history. It does not imply this procedure, force-push permission or
branch deletion.

## Confirm scope and preserve the complete tree

Record the exact repository, branch, local tip, remote URL and tip, configured human author and
whether authorization covers local rewriting, the named remote branch or both. Respect an existing
standing authorization that applies. Do not ask again for a step that is already authorized. A
history instruction for one repository does not authorize rewriting a sibling app or skills
repository.

Check tracked, untracked, staged, unstaged and ignored paths. Review valid owner changes under
the real delivery scope. Stage explicit reviewed paths and scan the exact index for signing files,
credentials, runtime data, caches and generated output added by mistake. Report only suspicious
filenames or rule IDs. A secret-field name in a sanitized example is not itself a leaked
credential.

Compare the complete planned tree with the original. Explain intended removals and keep all
unaffected source, file modes, submodules, licenses and native projects. Deleting a publishing tool
means finding its README/AGENTS references, scripts, CI hooks, examples, dependencies and ignored
outputs. Do not delete valid app configuration, SDK integration or a native host just because its
filename contains 'release', 'review' or 'store'. Validate the real remaining build workflow.

Do not remove `.git` to erase history. That also loses repository configuration, refs, hooks and
recovery information. Record the original tip for recovery through the existing reflog or an
approved private receipt. Do not create backup branches or tags when repository policy forbids them.

## Build the reviewed root commit with care

For an existing parentless tip, an authorized amend can keep the one-root structure through the
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

These are separate operations with returned IDs, not literal angle-bracket arguments or a script
that runs on its own. No `-p` argument means no parent. `commit-tree` does not run normal commit
hooks. Use only the workflow the project allows, pass its required checks and hooks, and do not use
plumbing to get around a failed hook. Check that the count is one, the tree is the reviewed index,
and the author and message meet the repository contract before you move the ref. Use the
expected-old local tip to catch concurrent edits.

If a local ref update fails, read the state again instead of deleting locks or overwriting another
writer. Do not change the checked-out branch, reset the working tree or throw away unstaged owner
changes just to finish the rewrite. Report any index or worktree differences from the delivered
snapshot.

## Publish only the authorized branch with an explicit lease

Read or fetch and check the real remote tip before rewriting. An unexpected remote change needs
review and must be kept. Record the observed SHA on its own, not from a tracking ref that updates in
the background, for example from `git ls-remote <remote> refs/heads/<branch>` immediately before
constructing the root. If that SHA differs from the last reviewed remote tip, check the incoming
commits with `git fetch <remote>` and `git log <old-remote-sha>..<observed-remote-sha>` and carry
valid changes into the reviewed tree before you continue. For an authorized publication of that
exact branch:

```text
git push --force-with-lease=refs/heads/<branch>:<observed-remote-sha> <remote> refs/heads/<branch>:refs/heads/<branch>
git ls-remote <remote> refs/heads/<branch>
```

The explicit expected remote SHA is the protection. Do not quietly move it forward after a
rejection, or use unconditional `--force`. A failed push can leave the reviewed new root local while
the remote stays unchanged. Check both states before you retry. Do not add a PR or feature branch to
a main-only workflow.

Check that the local and remote tips match, the reachable branch count is one and the worktree has
only remaining changes you understand. Check the real CI run for that SHA and tell pending, failed
and passed apart. On GitHub with an authenticated GitHub CLI, `gh run list --commit <new-root-id>`
lists the runs for that commit and `gh run watch <run-id> --exit-status` waits for one and fails
when it fails. Report pending when the run has not finished. Without CLI or API access, name the CI
page the owner must check. Do not report a green run from the replaced commit. Rewriting branch
ancestry does not erase other refs, reflogs, hosting retention or leaked credentials. Credential
rotation is a separate operation.

If an execution approval rejects the rewrite, keep the reviewed result and cite the exact action and
the stated reason. Check the authorization that applies and the evidence that the tree was kept. Do
not hide the same denied change behind another tool. Ask for any approval that is truly missing only
after the concrete result is ready and the independent authorized work is done.
