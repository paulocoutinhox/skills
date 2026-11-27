# Bundle: NAME

Line of work: NAME
Prepared on: YYYY-MM-DD HH:MM UTC

## What To Check

- Base commit (main): FULL COMMIT
- Commits in the bundle, oldest first: FULL COMMIT, FULL COMMIT
- Branch inside the bundle: refs/heads/BRANCH

## Machine It Needs

- Kind: such as Linux x86-64 with nested virtualization, Windows desktop session, Mac, GPU
- Peak memory per job: such as 17 GB for an ASan link
- Expected duration: such as 35 minutes, measured on YYYY-MM-DD
- Exclusive use of the machine: yes or no

## Dry Run Done Locally

- [ ] `git bundle verify NAME.bundle`, inside a clone that has the base commit
- [ ] `git bundle list-heads NAME.bundle` shows the branch above
- [ ] `uv run --no-project --python 3.11 python -m py_compile run.py`
- [ ] The first steps (clone, fetch the bundle, list the commits) ran in a temporary folder

## Exact Command

```bash
uv run run.py batch/results/NAME
```

The runner fetches the bundle by its absolute path, builds every commit in a fresh worktree and build folder, writes `summary.txt` and one log per step, and exits non-zero when any step failed.

## Expected Results

- Steps that must pass: LIST
- Steps that must fail (checked the other way): LIST, or none

## Logs To Send Back

- `batch/results/NAME/summary.txt`
- `batch/results/NAME/<step>.log` for every failed step
- Any test artifacts: LIST
