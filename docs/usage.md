# Using Relay Workflow

[English overview](../README.md) · [中文完整入门](../README.zh-CN.md) · [Examples](../examples/README.md)

Relay Workflow is a Skill package with native client adapters. The installer copies the package; the client supplies the agent tools. There is no separate workflow runner to start.

## Install once, choose the working directory each time

Run these commands from a clone of this repository with Python 3.11+:

```sh
python scripts/install.py --client both --scope user --dry-run
python scripts/install.py --client both --scope user
```

The default `user` scope makes the explicit entry available across your working directories. To restrict installation to an existing project:

```sh
python scripts/install.py --client both --scope project --project-root "C:/work/catalog" --dry-run
python scripts/install.py --client both --scope project --project-root "C:/work/catalog"
```

Use `--client codex` or `--client opencode` to select one client. `--json` changes the installer result to JSON; it is useful with `--dry-run`. `--project-root` is required for project scope and must name an existing directory.

| Client | User scope, default location | Project scope |
| --- | --- | --- |
| Codex | `~/.codex/skills/relay-workflow/` | `<project>/.agents/skills/relay-workflow/` |
| OpenCode | `~/.config/opencode/skills/relay-workflow/` | `<project>/.opencode/skills/relay-workflow/` |

Codex user scope honors `CODEX_HOME`; OpenCode user scope honors `XDG_CONFIG_HOME`. OpenCode also receives the three `relay-*` role files under `agents/` and the `relay-workflow.md` entry under `commands/` in its corresponding client directory.

Installation uses the same source package for both clients. Every destination is checked before the first write. Existing identical content is unchanged; a differing file or unsafe destination stops the installation. The installer does not delete files, overwrite different content, or edit existing `AGENTS.md`, model settings, permissions, or global configuration files. It has no force, upgrade, or uninstall option. Review reported conflicts before deciding how to reconcile your existing files.

Reopen or restart the client if the entry has not appeared. OpenCode's command belongs in the current primary conversation; use an agent with the necessary file access, such as Build. Do not change permissions or models to bypass unavailable capabilities. See [compatibility](compatibility.md) for the precise validation boundary.

## Invoke explicitly

Open the actual directory where the task should happen. The installed Skill directory is **not** the task's workroot. Use one of these forms in the client conversation:

| Client | Execute | Recover |
| --- | --- | --- |
| Codex | `$relay-workflow execute: <request>` | `$relay-workflow resume: <absolute run path>; objective: <goal>` |
| OpenCode | `/relay-workflow execute: <request>` | `/relay-workflow resume: <absolute run path>; objective: <goal>` |

Chinese equivalents:

```text
$relay-workflow 执行：<本轮需求>
$relay-workflow 恢复：<原 run 绝对路径>；本轮目标：<目标>

/relay-workflow 执行：<本轮需求>
/relay-workflow 恢复：<原 run 绝对路径>；本轮目标：<目标>
```

Explicitly asking to use the Skill to execute or recover, or selecting the Skill and then giving such an instruction, also qualifies. Mentioning its name, quoting these examples, asking how it works, installing it, or editing its rules does not start the role chain. An active run continues within its existing authorized scope; a user stop request stops further dispatch.

A useful request states one outcome, relevant inputs, allowed changes, and what would count as success. For example:

```text
$relay-workflow execute: In this repository, add --output to the existing CSV summary CLI. Preserve stdout when the flag is absent. Accept a writable file path, return a useful error for invalid paths, cover both behaviors, and update the usage section. Do not add dependencies or change other commands.
```

Installation or invocation does not authorize publication, deployment, external messages, credential access, device writes, or unrelated filesystem changes. Existing local instructions and permissions continue to apply. Bulk deletion is prohibited, including deletion hidden inside loops or subprocesses.

## What happens in a run

The main records the exact request and real runtime handles. It forwards paths and follows fixed routing branches. It does not inspect detailed source materials, plans, candidates, or reports; it does not monitor progress or solve technical problems.

The planner reads the relevant materials and freezes `profile.md` for this task: actual workroot, allowed scope, available prerequisites, one acceptance goal, bounded packages, concrete checks and thresholds, evidence locations, budgets, and stop/recovery conditions. The planner selects the checks appropriate to software, documents, research, design, hardware, or another task type. You do not need to alter the installed Skill for that adaptation.

For each task, the main dispatches a fresh implementer. The implementer finishes the candidate, stops all activity capable of modifying it, and freezes a manifest containing candidate identities and hashes. Only then does the main dispatch that task's one fresh independent tester. The tester checks the frozen candidate across all three dimensions:

- `functional`: correctness against the requested outcome.
- `engineering`: deliverable quality, reproducibility, and applicable professional constraints.
- `system`: use or integration in the intended context.

These are checklists for one role. A dimension may be `not_applicable` only when the planner documented the reason before implementation. Static, mocked, simulated, and real-system checks retain their evidence labels. Required reality cannot be replaced by a simulation.

On `PASS`, the original planner updates the authoritative task record and dispatches another already allowed package or closes the run. On `FAIL`, the same implementer repairs and freezes again, then the same tester retests. The tester binds evidence to the new manifest; the main does not decide which checks remain valid. On a blocker or exhausted repairs, the original planner records the condition and the recovery path. The main forwards the planner's user summary unchanged.

## Files are the recovery boundary

Runs default to `<workroot>/.relay-workflow/runs/<run_id>/`. The project's existing authoritative task record remains authoritative; the run does not introduce a competing global board.

| Artifact | Purpose and owner |
| --- | --- |
| `request.md`, `main-state.json` | Exact request and mechanical routing/identity history; main |
| `profile.md`, `plan.md`, `dispatch.json` | Frozen acceptance, selected packages, and next action; planner |
| Candidate manifests, repair notes, `lessons.md` | Frozen identities, implementation history, and lessons; implementer |
| Integrated reports and evidence | One report per task per acceptance round, bound to the current manifest; tester |
| `handoff.md`, `final-summary.md`, `user-summary.md` | Recovery context, closeout, and the summary relayed to the user; planner |

Detailed file layouts and metadata fields are defined in the [contract](../skills/relay-workflow/references/contract.md) and [templates](../skills/relay-workflow/templates/README.md). A run summary may truthfully close as blocked or failed; completion requires the selected goal's required acceptance.

## Bounds and honest stopping

Default scope is one main acceptance goal, at most four packages, two planning levels, and at most five semantic implementation steps per package. Batch size is one. Larger requests become a dependency-closed slice, with at most three unscheduled follow-on topics. A current explicit finite numeric user exception can change the specified scope or batch limit; vague instructions to do everything cannot.

Each dispatch or continuation allows at most 30 actual underlying tool calls. The planner has 15 minutes; implementer and tester each have 45 minutes. Reads/searches have a 60-second command limit, local checks five minutes, and long builds/exports 30 minutes unless the planner froze another finite bound with a reason. These require actual timeout and safe-stop controls; a tool yielding early is not a timeout. They are operating contracts rather than platform-enforced hard limits.

Two separate ledgers matter:

- **Actual repairs:** round 0 is initial acceptance. Edits to repair failed acceptance consume rounds 1–3. Empty handoffs or missing prerequisites do not consume an actual repair.
- **Problem supplements:** at most two for the same stable task/problem, and only with qualifying new information, evidence, and a recovery action inside the frozen scope. Renaming a problem or changing sessions does not reset the count.

Stop after two consecutive steps without progress. A problem gets at most three targeted search/read rounds. A failing command gets its first attempt and at most one retry supported by new evidence. Missing external conditions, permission, tools, devices, data, user input, and API/quota errors return blocked directly; no automatic retry or authority expansion follows. See [limits](../skills/relay-workflow/references/limits.md) for the full rules.

## Recover without inventing a session

Keep the original run directory. Supply its absolute path and a concrete objective:

```text
$relay-workflow resume: C:/work/catalog/.relay-workflow/runs/example-run; objective: Complete the remaining acceptance checks within the original scope.
```

```text
/relay-workflow 恢复：C:/work/catalog/.relay-workflow/runs/example-run；本轮目标：在原冻结范围内完成剩余验收。
```

Within a valid existing runtime, continuation uses the recorded original role handles. When moving between clients, changing parent sessions, or encountering an observed invalid handle, recovery uses the run files and an explicit old-to-new identity mapping. New roles read the preserved state and state what they restored. That is file-based recovery, not a successful resumption of the old runtime session. Scope, repair, supplement, and budget history survive recovery.

If required agent tools or recovery inputs are unavailable, the result is blocked. The main does not assume another role, fabricate an ID, reset counters, or probe sessions preventively. Consult the [runtime adapters](../skills/relay-workflow/references/runtimes.md) for host-specific calls and the [compatibility notes](compatibility.md) for tested coverage.
