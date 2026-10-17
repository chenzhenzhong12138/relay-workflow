---
name: relay-workflow
description: Run an explicitly requested, bounded relay workflow with a planner, fresh implementer and independent integrated tester, using frozen evidence and limited repairs. Questions, examples, rule reviews and installation do not start execution.
metadata:
  opencode/autoinvoke: "false"
---

# Relay Workflow

Use only when the current user explicitly requests execution or recovery: Codex `$relay-workflow execute: <request>` / `$relay-workflow 执行：<需求>`, OpenCode `/relay-workflow execute: <request>` / `/relay-workflow 执行：<需求>`, or an explicit instruction to use this skill to execute. Recovery accepts `resume: <absolute run path>; objective: <goal>` or `恢复：<原run绝对路径>；本轮目标：<目标>`. A skill selection followed by an execution/recovery instruction also qualifies. Mentioning the name, quoting an invocation, asking questions or changing the rules does not activate the chain. An active run continues within its existing authorization; a stop request ends dispatch.

## Main is a relay

The main agent forwards user wording unchanged, records paths and actual runtime IDs, and follows fixed branches. It does not interpret requirements, choose scope or dependencies, design, implement, diagnose, test, judge retest impact, monitor progress, or produce a technical summary. It reads only these instructions, the shared contract/limits, the active runtime adapter, `dispatch.json`, compact return metadata and mechanical state. It may relay `user-summary.md` verbatim. It does not read detailed materials, profiles, plans, candidates, manifests or reports.

Read [contract](references/contract.md), [limits](references/limits.md) and the applicable [runtime adapter](references/runtimes.md). Use the actual workroot, never the installed skill directory, for `.relay-workflow/runs/<run_id>/`. Preserve the project's existing authoritative task record. Copy the user request unchanged into the run; record only mechanical events and returned metadata.

## Fixed chain

1. Start a planner with [planner instructions](references/roles/planner.md), raw request and paths. The planner interprets the request, freezes a bounded profile and packages, and writes the next dispatch.
2. Follow `spawn_agent` to create a fresh implementer for each task, or each user-authorized batch. Pass [implementer instructions](references/roles/implementer.md) and planner-selected input paths.
3. After implementation stops and freezes its candidate, follow `spawn_single_tester` exactly once for that task/batch to create a fresh independent tester with [tester instructions](references/roles/tester.md).
4. On `FAIL`, use `followup_task` with the same actual implementer and tester identities. Round 0 is initial acceptance; rounds 1–3 are the maximum actual repair rounds. Never merge PASS evidence from different manifests.
5. Follow `return_to_planner` for accepted results, exhausted repairs, blockers or invalid returns. The original planner updates records, selects an already allowed next package, or closes the run.
6. Follow `relay_to_user` to forward the planner's user summary unchanged.

These operation names are logical labels; use real host APIs from the runtime adapter. Missing required agent tools means `blocked`; main never takes over a role. Children execute only their assigned role and cannot spawn children. No progress polling, directory/log scans, nudges or invented IDs; event waiting follows the runtime adapter.

The default is one main acceptance goal, at most four packages, and batch size one. [Limits](references/limits.md) governs slicing, role budgets, two information supplements and three repairs. [Adaptation](references/adaptation.md) governs task-specific acceptance; [evidence](references/evidence.md) governs freezing and integrated tests. Installing or activating this skill grants no additional filesystem, deletion, external-message, publication, deployment or device-operation permission.
