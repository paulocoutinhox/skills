# Batches, bundles and the batch runner

Read this when you design a batch, prepare bundles, write the step runner, attach work to a running machine or read results. Everything here comes from real batch runs on Linux, Windows and macOS machines. The commands are the native tools of Git, Ninja, Make, rsync and OpenSSH.

## Never rent a machine for one check

Rent a machine only for a batch. A batch is everything that needs a machine of that kind right now, run in one session, in parallel where memory allows. A typical Linux batch holds:

- every commit of a branch on its own, plus the head;
- both compilers, such as GCC and Clang;
- the sanitizers (ASan with UBSan, TSan);
- the GPU tests, when the machine has a GPU;
- the web and Android builds;
- the fuzzers;
- the benchmarks.

Startup costs minutes every time: launch, waiting for SSH, cloning or fetching, and warming caches. Setting up toolchains from zero costs much longer. So one large machine running several jobs at once is cheaper than several small machines, and a prepared image is cheaper than installing tools at every launch.

When several lines of work (people or agents) are ready at the same time, they share one batch machine. The full CI matrix runs by hand once per block of work, not once per commit. Push CI stays small, such as a format check plus unit tests on two systems.

## Lines of work hand over bundles, not machines

A line of work never rents a machine. When its work is ready for a batch, it leaves a bundle folder with three files:

| File | Content |
| --- | --- |
| `<name>.bundle` | A git bundle with only the commits the remote lacks: `git bundle create <name>.bundle origin/main..<branch>`. |
| `run.py` | Every step of the job, in order, using the batch runner pattern below. |
| `README.md` | The exact command to run, the machine kind it needs, the expected duration and memory, and the logs to send back. Use [the bundle README template](../assets/bundle-readme.md). |

One coordinator runs the shared batch line once or twice a day with every ready bundle. While a batch runs, the lines of work keep working on their next task. Nobody waits idle for a machine.

**Bundles are replaced, not stacked.** When a line of work fixes something after its batch started, the coordinator stops the obsolete run on the shared machine to free capacity and attaches the new bundle. Record the swap in the tracker.

## Build first, rent second

A paid machine never waits while someone writes a script. Prepare everything locally first: bundles, scripts, batch files, signed packages and test lists. Then dry-run every batch locally before it reaches the cloud:

1. Resolve every ref to its commit with `git rev-parse <ref>`, and write the commit into the README.
2. Run `git bundle verify <name>.bundle` on each bundle, inside a clone that has the bundle's base commits.
3. Check that the bundle holds the expected branch with `git bundle list-heads <name>.bundle`.
4. Check the syntax of every script: `uv run --no-project --python 3.11 python -m py_compile run.py` for Python and `bash -n <script>` for an existing shell script.
5. Run the first steps of each job in a temporary folder: clone, fetch the bundle, list the commits. Stop before the long build.

One bundle failed in the cloud after 3 seconds because of a relative path. A dry run would have caught it for free.

## Fresh trees, or the gate is a lie

Copying a tree with `rsync -a` onto an older build folder keeps old modification times. Ninja then decides that nothing changed, does not rebuild, and the gate passes on old objects. This happened and made a gate meaningless.

Every gate builds each commit from a fresh `git worktree`, `git clone` or `git archive`, in a build folder that only that commit ever used. Send commits as git bundles and fetch each bundle into a clone at current main:

```bash
git -C repo fetch "$(realpath ../bundles/feature.bundle)" 'refs/heads/*:refs/remotes/bundle/*'
git -C repo worktree add --detach ../trees/feature-c1 <commit>
```

Always turn the bundle path into an absolute path. `git -C repo fetch <relative path>` resolves the path inside `repo`, not inside the folder you ran it from, and fails. This cost one line of work a whole batch. In Python, use `Path(bundle).resolve()`.

## The batch runner reports failures honestly

A job's runner exits non-zero when any step failed, and the batch summary trusts only that exit status. A script that ended with `echo` or `grep` reported failed runs as PASS twice in practice, because the last command succeeded.

Rules for every runner:

- Print `START <step> <UTC time>` and `END <step> status <n>` for every step, and write one log file per step.
- Keep running the other steps after a failed step, so one batch reports every error at once instead of one error per paid run.
- Keep building after the first compile error with `ninja -k 0` or `make -k`.
- Order the steps from quick, likely-to-fail checks (format, lint, a syntax check, the unit tests of the changed area) to the long ones. All steps still run.
- Give every step a time limit. When it runs out, the step fails with a sentence that names the limit.
- Check an expected failure the other way. A regression check that must fail with the fix reverted makes the run fail when it passes. A step that timed out or could not start is a failure even when it was expected to fail, since it proved nothing.
- End with `PASSED every step` or `FAILED <steps>`, and exit with status 1 when anything failed.

Write runners in Python and run them with uv. This example shows the pattern. Replace the steps with the project's real commands:

```python
# /// script
# requires-python = ">=3.11"
# ///

import os
import signal
import subprocess
import sys
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path


@dataclass
class Step:
    name: str
    command: list[str]
    timeout_minutes: int
    expect_failure: bool = False


STEPS = [
    Step("format", ["cmake", "--build", "build/gcc", "--target", "check-format"], 10),
    Step("build-gcc", ["ninja", "-C", "build/gcc", "-k", "0"], 60),
    Step("test-gcc", ["ctest", "--test-dir", "build/gcc", "--output-on-failure"], 45),
    Step("regression-without-fix", ["ctest", "--test-dir", "build/reverted", "-R", "regression"], 20, expect_failure=True),
]


def utc_now() -> str:
    return datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")


def report(summary: Path, line: str) -> None:
    print(line, flush=True)

    with summary.open("a") as file:
        file.write(line + "\n")


def stop_tree(process: subprocess.Popen) -> None:
    os.killpg(process.pid, signal.SIGTERM)

    try:
        process.wait(timeout=30)
    except subprocess.TimeoutExpired:
        os.killpg(process.pid, signal.SIGKILL)
        process.wait()


def run_step(step: Step, log_folder: Path, summary: Path) -> bool:
    log_path = log_folder / f"{step.name}.log"
    report(summary, f"START {step.name} {utc_now()}")

    with log_path.open("w") as log:
        try:
            process = subprocess.Popen(step.command, stdout=log, stderr=subprocess.STDOUT, start_new_session=True)
        except OSError as error:
            log.write(f"The step could not start: {error}.\n")
            report(summary, f"END {step.name} status 127")
            return False

        timed_out = False

        try:
            status = process.wait(timeout=step.timeout_minutes * 60)
        except subprocess.TimeoutExpired:
            stop_tree(process)
            log.write(f"The step ran past its limit of {step.timeout_minutes} minutes and was stopped.\n")
            status = 124
            timed_out = True

    report(summary, f"END {step.name} status {status}")

    if timed_out:
        return False

    if step.expect_failure:
        return status != 0

    return status == 0


def main() -> int:
    log_folder = Path(sys.argv[1]).resolve()
    log_folder.mkdir(parents=True, exist_ok=True)
    summary = log_folder / "summary.txt"
    summary.write_text("")
    failed = [step.name for step in STEPS if not run_step(step, log_folder, summary)]

    if failed:
        report(summary, f"FAILED {' '.join(failed)}")
        return 1

    report(summary, "PASSED every step")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

Run it as `uv run run.py batch/results/<run name>`, from the batch user's home folder, which is the folder the minute sync copies. It writes `summary.txt` and one log per step into that folder. The header tells uv which Python to use, whatever Python the machine has. It starts each step in its own process group, so a time limit stops the whole tree of compilers and test programs, not only the first process. A process that ignores the stop signal is killed after 30 seconds. Process groups and `os.killpg` exist on Linux and macOS only. On Windows, start each step with `creationflags=subprocess.CREATE_NEW_PROCESS_GROUP` and stop the tree with `taskkill /T /F /PID <pid>`.

The coordinator reads the step logs, not only the summary. A summary line can hide a skipped suite, a test that never started or a warning that the project treats as an error.

## Memory decides the parallelism, not the cores

Running out of memory kills batches. With 16 compile jobs per build on 32 GB, the machine ran out of memory, and ASan links killed the runners.

Measure the peak memory of each kind of link and size a link pool from the machine's memory. Peaks seen on a large C++ project, as an example to replace with your own measurements:

| Link kind | Peak seen | Budget per link |
| --- | --- | --- |
| ASan with line debug info | about 12 GB | about 17 GB |
| TSan | about 7.6 GB | about 10 GB |
| LTO | about 4.3 GB | about 6 GB |
| Plain link | about 3.4 GB | about 5 GB |

Limit links with a Ninja job pool from CMake, and keep an override variable so a smaller machine can lower it:

```cmake
set(PROJECT_LINK_JOBS 2 CACHE STRING "Links that run at the same time.")
set_property(GLOBAL APPEND PROPERTY JOB_POOLS link_pool=${PROJECT_LINK_JOBS})
set(CMAKE_JOB_POOL_LINK link_pool)
```

A working split on a 32 vCPU, 64 GB machine was about 8 compile jobs per build with 4 builds at once. Sanitizer builds, fuzzers and the Android emulator take the machine one job at a time. Keep about 15 % of memory free. Watch `free -g` and `uptime` while the batch runs. A load average far above the core count means the machine is oversubscribed and every job slows down.

## Sync results every minute

Sync the results folder back to the controller every minute, so a reclaimed spot machine loses only the steps in flight. The session's own known_hosts file is explained in [safety and cleanup](safety-and-cleanup.md#access-to-the-machine):

```bash
rsync -az -e "ssh -i ~/.ssh/<project>-batch-<session> -o UserKnownHostsFile=~/.ssh/<project>-batch-<session>.known_hosts -o StrictHostKeyChecking=accept-new -o BatchMode=yes" batch@<host>:batch/results/ <local results folder>/
```

A Windows host has no rsync, so its sync copies the results folder with `scp -r` over the same SSH options. A spot machine was once reclaimed after 67 minutes, and every unsynced result was lost. Long jobs on spot capacity need checkpoints: split them into steps whose results sync as each step ends.

## Detect a lost machine

When SSH fails, ask the provider for the machine state (`aws ec2 describe-instances`, `az vm get-instance-view`, `gcloud compute instances describe`). A terminated spot machine means the batch lost its in-flight steps: report which steps finished and rerun the rest. If the machine still runs but SSH has failed for 10 minutes, report it to the person. Check first whether the caller's public IP changed, which stops the firewall rule from matching.

## Attach more work to a running machine

New bundles can join a running machine. Give the controller's batch script (the orchestrator) an attach mode, such as `--attach <session> --name <name>`, and give each attached run its own folders, logs and summary.

The batch that launched a machine once deleted it when its own jobs ended, which killed four attached runs. Use one of two fixes:

- The deleting batch waits until no runner of any batch is left on the machine. Check with `pgrep -f '[r]un.py '` over SSH. The bracket stops `pgrep` from matching the SSH shell that runs it.
- Or the first batch launches with a keep option, such as `--keep`, and the coordinator deletes the machine after the last attached run.

When new work joins, extend the shutdown timer with `sudo shutdown -h +<minutes>` on the machine, and record the new time in the tracker. A timer was once too short for work added later and had to be extended in time.

Never edit a script that a batch is running. bash reads a script while it runs it, so an edit changes or breaks that run. zsh buffered the whole script in one test, so an edit there did nothing. Neither behavior is something to rely on. Give each run its own copy of the runner, named after the run, such as `~/<run name>-run.py`, and change the next run instead.

To stop an obsolete run, kill the process tree of that job alone. Walk the children with `pgrep -P <pid>` recursively from the job's runner, then send `kill -TERM` to every process found, children first. Never kill by a broad name that other jobs share.

## Get the code onto the machine

- **A public repository:** the machine clones it from the Git host, since datacenter bandwidth is fast and a home upload is slow. Then it fetches a small bundle that holds only the commits the remote lacks (`git bundle create <name>.bundle origin/main..<branch>`). A 155 MB full-history bundle is never needed.
- **A private repository,** in order of preference:
  - a bundle made from the last commit that the machine's prepared image already holds, so no credential reaches the machine;
  - a read-only deploy key made for the session and removed after it;
  - a fine-grained token with read-only contents access, used once and never stored. The controller sends it through stdin of the SSH command, as for the cache credentials, and the machine runs:

    ```bash
    IFS= read -r GIT_TOKEN
    export GIT_TOKEN
    git -c credential.helper='!f() { echo "username=<account name>"; echo "password=$GIT_TOKEN"; }; f' clone https://github.com/<owner>/<repo>.git repo
    unset GIT_TOKEN
    ```

    The helper prints the token to Git from the environment, so it never appears in a command line or a file.
- **Never bake a credential into an image.**
- Compress big transfers with `zstd`, and send logs back with `rsync -az`, which copies only what changed.

## Machines that sleep, update or reboot

- **The person's Windows laptop:** set the power plan to never sleep while plugged in, pause Windows Update or set active hours for the time of a batch, and give it a fixed address (a DHCP reservation on the router) or a resolvable name, since a home IP changes.
- **The local Mac during long local runs:** `caffeinate -dimsu <command>` keeps it awake for that command only.
- **Linux cloud machines:** stop unattended upgrades during a batch (`sudo systemctl stop unattended-upgrades`), or bake the updates into the image, so a package upgrade or a restart prompt never interferes.
- **The Azure Windows VM:** schedule updates outside batch times, and let it update when it starts between batches.
- **After any reboot:** confirm the shutdown timer is armed again. A systemd unit re-arms it (see [AWS](aws.md#the-self-destruct-timer-on-ubuntu)).

## Flaky tests: prove the cause, never hide it

A test that fails sometimes is never retried until it passes, never loosened and never skipped.

1. **Reproduce under load on the batch machine.** Run the base commit's test many times, such as 30, while the machine is loaded with parallel builds or a CPU stress tool. Then run the fixed commit the same way. In practice, a time-budget test failed 30 of 30 under load on the base and passed 30 of 30 on the fix, which proved its cause. A fix whose base never failed under load stays an analysis, and the report says so plainly.
2. **Find tests that leave state behind.** Add a diagnostic patch, not landed, that logs the files a test still holds open when it ends or when its folder goes away. Check what the temporary folder holds after the run.
3. **Separate the tooling's own leftovers.** A tool can leave files in the temporary folder by itself, as `uv run` leaves a lock file. Run the tooling once with an empty `TMPDIR`, record what it makes alone, and count only what the tests add, as a written rule.

## Benchmarks on rented machines

- Cloud machines share hardware, so their timings are noisy, and spot machines of the same type can land on different CPUs. Compare relative numbers within one session on one machine. Repeat each measurement and report the median and the spread.
- Real GPU and device performance comes from real hardware: a rented GPU machine, a real phone in a device farm, or the person's own devices. Never from a simulator, an emulator, a software rasterizer or headless Chrome, whose GPU times measure the CPU.
- Record the context with every result: the GPU, the driver version, the OS version and the device model.
- Test the oldest supported hardware too. Older GPUs and systems have lower limits. For example, a first-generation Apple TV 4K's GPU allowed only texture indices 0 to 30, and a budget Mali phone had no GPU timers.

## Watch a batch without wasting time or tokens

- Run the batch command in the background and get notified when it ends. Do not poll its output in a loop.
- Let the batch script itself sync results to the controller every minute, so the agent only reads local files.
- Check progress only when needed, by reading the `START` and `END` lines of the synced logs.
- Look at machine health (`free -g`, `uptime`) when attaching more work or when steps slow down.

## Read the results and send them back

The batch summary gives, for each job:

- the steps that passed and the steps that failed;
- the first error of each failing log, with its file and line;
- the names of the tests that failed.

Each line of work gets its own part, with the log paths. Never paste whole logs into messages.

After every batch, the coordinator:

1. reads the summary and the step logs of every job;
2. records pass or fail per job, the failing tests, the duration, the cost, the cache hit rate, the measured durations for the next estimate and the deletion proof in the tracker, right away (see [the tracker procedure](tracker.md));
3. sends each line of work its own findings in its own words, with the paths of the failing logs.

Tests stay strict: fix the root cause of a failure (see [flaky tests](#flaky-tests-prove-the-cause-never-hide-it)). An agent once loosened a test to get a pass, and the gate stopped meaning anything.

## Housekeeping on the controller

- Delete old results, bundles and scratch archives after they are reported. A bundle of a whole history can be over 100 MB.
- Keep one copy of each batch's summary in the tracker's 📜 Batch Log, and drop the bulky logs after a set retention, such as two weeks.
- Remove local worktrees and their build folders once their work has landed.

## Sources

Checked on 2026-11-26: [git bundle](https://git-scm.com/docs/git-bundle), [git worktree](https://git-scm.com/docs/git-worktree), [Ninja manual](https://ninja-build.org/manual.html), [CMake JOB_POOLS](https://cmake.org/cmake/help/latest/prop_gbl/JOB_POOLS.html), [CMAKE_JOB_POOL_LINK](https://cmake.org/cmake/help/latest/variable/CMAKE_JOB_POOL_LINK.html) and [uv scripts](https://docs.astral.sh/uv/guides/scripts/). The failures, memory peaks and durations come from practice. See [sources](sources.md) for the full record.
