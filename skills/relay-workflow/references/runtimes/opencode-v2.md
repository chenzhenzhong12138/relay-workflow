# OpenCode v2 adapter

Baseline: OpenCode **2.0.28**. Its real tools differ from older `task` examples: Skill loading uses `skill({"id":"relay-workflow"})`, and delegation uses `subagent`. Inspect the actual schema if the installed release differs. This adapter does not claim support for an unverified v1 `task` API.

The installer places the same Skill package in OpenCode's native skills directory and installs four thin Markdown adapters: one primary-session `/relay-workflow` command and the `relay-planner`, `relay-implementer`, `relay-tester` subagents. They reference this package's role documents. Native agent permissions deny further `subagent` calls; inherited file/command permissions and models remain unchanged.

## New role

Call the native **subagent** tool, not a shell command:

```json
{
  "agent": "relay-planner",
  "description": "Plan this bounded request",
  "prompt": "Assigned planner. SKILL_ROOT=<actual loaded Skill directory>; WORK_ROOT=<actual task directory>; RUN_DIR=<actual run directory>. Read SKILL_ROOT/references/roles/planner.md. Original request and selected inputs=<actual paths>. Keep the current user's constraints; return compact dispatch/status metadata only. Do not delegate.",
  "background": false
}
```

New roles omit `sessionID`; this creates a fresh child with clean context. Use `agent: "relay-implementer"` for implementation and `agent: "relay-tester"` only after its candidate is frozen and modifications stopped. Pass SKILL_ROOT, WORK_ROOT, RUN_DIR and the role's actual paths every time. Do not send full chat histories or specify a new `model` without the user's request.

The result contains `sessionID`, `status` and `output`. Record that actual sessionID with its runtime/role/task/parent context. `status: "completed"` means the child finished; it does not mean the child passed acceptance. Route the structured metadata in `output` using the shared contract.

## Continue the same role

After the child has returned, call `subagent` again with its original sessionID:

```json
{
  "agent": "relay-implementer",
  "description": "Repair this task round one",
  "sessionID": "<actual original implementer sessionID>",
  "prompt": "Same task and allowed scope. Repair round 1. Failed report/input paths=<actual planner-selected paths>. Read reports, repair, update lessons, stop modifications and freeze a new manifest. Return compact retest metadata; missing conditions mean BLOCKED.",
  "background": false
}
```

Keep the role name unchanged when continuing it. Continue the original planner/tester in the same way. Do not switch one child between implementation and independent testing. The logical `spawn_single_tester` operation is exactly one new `relay-tester` call without sessionID.

## Waiting and recovery

Default foreground `subagent` waits for the final response; main does not need a separate waiting tool. There is no Codex `wait_agent`, `followup_task`, `fork_turns` or pure `send_message` parameter to transplant here. Do not add a fictional `timeout_ms` to this tool. Foreground waiting is not an execution timeout; specialists retain their own command and stop budgets.

If a real tool result says `running`, accept only native completion notification: do not sleep, poll sessions/logs, request status or duplicate the task. Supplements and repairs are dispatched only after the original role returns. Without a final return, never invent a status or guarantee platform termination.

OpenCode only continues children of the current parent session. A different primary conversation or a Codex run needs file-based recovery with new actual handles and a recorded mapping; retain task scope and counters. Do not probe or pass foreign IDs as if they could resume.

Permission, provider/quota and missing-tool errors use the shared blocked route. Do not change global configuration, raise permissions or replace a missing native subagent with a shell-launched model. Detailed reports stay in files and main only handles compact routing metadata.

Source contracts: [subagent](https://github.com/anomalyco/opencode/blob/v2.0.28/packages/core/src/tool/plugin/subagent.ts), [skill](https://github.com/anomalyco/opencode/blob/v2.0.28/packages/core/src/tool/plugin/skill.ts), [command loader](https://github.com/anomalyco/opencode/blob/v2.0.28/packages/core/src/config/plugin/command.ts).
