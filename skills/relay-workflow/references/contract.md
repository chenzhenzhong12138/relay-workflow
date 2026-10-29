# Shared relay contract

## Ownership and files

`workroot` is the actual current task's directory, including projectless work. The default run is `<workroot>/.relay-workflow/runs/<run_id>/`; the installed skill location is never the run root. A requested resume path must resolve to the original run and its actual workroot. Relative run artifact paths below are resolved against that run; candidate paths are resolved against `workroot`. Validate path boundaries and authorization mechanically before tool execution.

The main creates `request.md` from the user's exact words and `main-state.json` containing runtime handles, branch events and counters copied from role returns. The planner owns `profile.md`, `plan.md`, `dispatch.json`, `handoff.md`, `final-summary.md`, `user-summary.md` and the project-authoritative task updates. A run may keep a reference/copy of task metadata but must not create a competing global task board. Implementers own candidate manifests, per-task `repair-state.json`, change/repair notes and `lessons.md`; they do not edit a planner-owned project task board. Testers own integrated reports and test evidence. Detailed outputs stay in files, outside main's context.

Before a repair's first candidate edit, the implementer persists its actual round as started in the task's `repair-state.json` within the allowed run paths. The planner reconciles this record into the authoritative task history on return or recovery. A crash or session change does not erase a started repair; missing or conflicting records require reconciliation, not a fresh count. Main copies compact counters from returns without interpreting repair details.

All role invocations receive the assigned role document, raw request path, run/workroot paths, the planner's selected input paths, frozen allowed scope/budgets and the relevant task/round. They return only compact metadata as described below. Roles may read details needed by their assignment. They never recursively delegate, spawn children or invoke the main chain.

## Decision and explanation contract

All roles read [route decisions and progress explanations](decision-reporting.md). Route-review returns take priority over the ordinary FAIL/repair branch. Main may read and relay only the supplied plain-language summary, without interpreting the technical evidence.

## Dispatch

`dispatch.json` contains exactly one next action. The planner authors semantic dispatch choices and preauthorizes the fixed freeze/test/repair transitions for the selected task; roles may emit those prescribed transitions by copying the planner's template and filling returned metadata. Main copies runtime IDs and other mechanical results without editing scope. `instructions_path` is relative to the installed skill root; other run-artifact paths are relative to the run. Required fields:

| Field | Meaning |
| --- | --- |
| `schema_version` | Integer `1` |
| `operation` | `spawn_agent`, `spawn_single_tester`, `followup_task`, `return_to_planner`, or `relay_to_user` |
| `role` | `planner`, `implementer`, `tester`, or `main` for user relay |
| `task_id`, `batch_id` | Stable task ID and nullable batch ID; planner startup may use `task_id: null` |
| `round` | Acceptance round `0`–`3`; task ledger is authoritative for actual repairs |
| `runtime`, `runtime_id` | Actual host and returned role handle, or null before a new spawn |
| `input_paths` | Paths to forward, not detailed contents main should inspect |
| `output_path` | Expected compact return metadata path, nullable for user relay |
| `budget` | Finite `tool_calls`, `wall_minutes` and command timeout values |
| `problem` | Null or the problem record below |

`spawn_agent` starts a new implementer (or initial/recovered planner as the runtime adapter specifies). `spawn_single_tester` starts the task's one new tester after freeze. `followup_task` targets a recorded actual role ID; it never creates a replacement task silently. `return_to_planner` targets the original planner. `relay_to_user` forwards the planner-authored `user-summary.md` unchanged. A dispatch can supply `instructions_path` or `summary_path` as appropriate. The active [runtime adapter](runtimes.md) translates labels into actual APIs; these labels are not tool names.

On implementer `frozen`, main mechanically dispatches the one tester. Tester `PASS` → original planner. `route_review: true` → original planner before repair. Tester `FAIL` with repair capacity and `route_review: false` → same implementer, then same tester. `BLOCKED`, exhausted repairs, malformed returns or invalid sessions → original planner/recovery route. Main never chooses a technical recovery, new package or retest set. The planner must provide the relevant dispatch in advance or on return; missing dispatch fields are a contract problem.

## Compact return metadata

Every return contains `schema_version`, `role`, `task_id`, `batch_id`, `round`, `status`, `runtime`, `runtime_id`, `artifact_paths`, `next_dispatch_path`, `problem`, and `usage` (`tool_calls`, `elapsed_seconds`). Use actual returned handles; never fabricate or infer them from cache directories. If a child cannot observe its assigned ID, it returns null; main fills the envelope from the actual spawn result before any continuation. `status` is one of `ready`, `frozen`, `PASS`, `FAIL`, `BLOCKED`, `complete` or `stopped` as appropriate to the role. A tester additionally returns `dimension: "integrated"`, `dimensions` with `functional`, `engineering`, `system`, `manifest_path` and `manifest_sha256`. An implementer returns freeze/manifest paths, `producer_stopped`, and `repair_performed`. Metadata is a pointer and assertion for routing, not the acceptance evidence itself. Every new return also includes `route_review` (boolean), `route_review_path` (path or null), `no_evidence_cycles` (nonnegative integer for the current stable problem), and `stage_summary_path` (plain-language evidence paragraph or null). A true review flag requires the stable problem record and an existing evidence/review path. Preserve these fields in dispatches that route the issue. For old runs with missing fields, the planner reconciles the reports and ledger; do not silently assume false or zero.

For batches, include compact `task_results` with each task's stable ID, round, status, manifest binding and repair count. A batch aggregate cannot conceal a failed/blocked task or replace per-task ledgers. Main forwards these fields mechanically.

The planner reads full reports, updates authoritative task records and writes the next dispatch. `complete` requires the selected goal's required acceptance to be achieved; an offline child result cannot mark an unfinished parent integration or hardware outcome done. A bounded run may close as blocked or failed with a truthful user summary.

## Problem record

Required keys: `problem_id` (stable for the same underlying blocker), `category` (`scope`, `implementation`, `reproduction`, `contract`, `external`), `reason`, `owner_role`, `new_information` (boolean), `evidence_paths` (array), `missing_fields` (array), `contradiction` (boolean), `recovery_path` (string or null), `requested_action` (string), `within_frozen_scope` (boolean), `supplement_count` (0–2).

`reason` is one of `scope_unclosed`, `acceptance_failure`, `missing_tool`, `missing_data`, `missing_device`, `missing_permission`, `missing_user_input`, `api_error`, `quota`, `invalid_session`, `invalid_manifest`, `budget`, `no_progress`, `malformed_return`, `other_external`. Do not set `new_information=true` merely because text was rewritten. Main forwards the returned condition to its owner using [limits](limits.md); the planner reconciles contradictory or incomplete records without inventing results.

## Recovery and identity

Persist each handle with its `runtime`, role, task/batch, parent context and original handle. Cross-host execution, a different parent session or an observed invalid handle requires file-based recovery and an explicit old→new mapping. A new role reads the run ledger, profile, frozen inputs and relevant reports, then declares what it restored. This is recovery, not resumption of the old runtime session. Preserve round, supplement, scope and budget history. Do not probe handles preventively, reset counters or invent a successful resume. If agent tools or necessary recovery inputs are unavailable, return blocked; main does not assume the work.
