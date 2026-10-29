# Codex adapter

Use the actual tools exposed in the current Codex session. Namespaces and schemas vary between desktop and CLI versions; examples below describe the collaboration interface, not every Codex release. A different interface must supply equivalent new-child and same-child continuation capabilities before it is used. Do not invent an `agent_type`, `resume` or `run_in_background` field.

## New role

With the collaboration interface, call `collaboration.spawn_agent` directly:

```json
{
  "task_name": "relay_implement_task_01",
  "fork_turns": "none",
  "message": "Assigned role: implementer. SKILL_ROOT=<actual installed directory>; WORK_ROOT=<actual task directory>; RUN_DIR=<actual run directory>. Read SKILL_ROOT/references/roles/implementer.md. Request, plan/profile and inputs=<planner-selected actual paths>. Task/round/scope/budget=<dispatch metadata>. Do not delegate. Return only compact metadata; write details to files."
}
```

Use planner/tester role instructions for those assignments. Supply absolute role, workroot and run paths plus the user's original wording/path; a clean child cannot infer them from omitted history. Start a fresh implementer and integrated tester for each new task, or the explicit batch defined by the planner. The same tester covers all applicable dimensions.

Copy the tool's real canonical name/ID into main's handle record. Do not strip it, guess a numeric ID or inspect caches for the most recent agent. A child cannot be expected to know an ID that the caller has not received yet.

## Continue a returned role

Use `collaboration.followup_task` with the original recorded handle:

```json
{
  "target": "<actual original implementer handle>",
  "message": "Same task, repair round 1. Original allowed scope and input/report paths=<unchanged dispatch paths>. Read all failed reports, repair within that scope, stop modifications, freeze the new candidate and return retest metadata. Missing external conditions mean BLOCKED."
}
```

The same pattern continues the original tester for retesting and the original planner for updates/closeout. A pure `send_message` is not a replacement for starting a returned idle role's next turn. Do not resume a role from a different task simply to reduce startup cost.

## Wait without monitoring

`collaboration.wait_agent` subscribes to returned events, at most 60,000 ms per wait under this workflow. A normal wait timeout is not a failure, supplement opportunity or reason to probe. No `list_agents` polling, log/directory scans, status inquiries or nudges. Native completion messages are routed according to compact return metadata; main never reads a long report to diagnose a failure. At a recorded invocation deadline or real host error only, [control recovery](../control-contract.md) permits one bounded native status inspection if available, followed by result handling or an unknown-state recovery report. It never permits repeated polling or duplicate dispatch.

Collaboration tools are called directly, outside `functions.exec` or shell programs. Use the current host's ordinary file/command tools for mechanical request/state records, preserving its permission checks. Do not copy those tool names into an OpenCode request.

An actually invalid/unavailable handle goes to file-based recovery. If the current Codex interface lacks required subagents, stop with the missing capability rather than running the specialist work in main.
