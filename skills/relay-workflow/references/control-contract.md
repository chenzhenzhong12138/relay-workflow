# Shared control fields and bounded recovery

This is the single definition of the control envelope. Role-specific return lists add fields; they never replace this envelope. It adds no role, execution allowance or run-wide budget. Existing numeric limits remain unchanged.

## Return and dispatch envelope

Every role return includes `route_review` (boolean), `route_review_path` (path or null), `no_evidence_cycles` (the last supplied ledger count), `stage_summary_path` (path or null), `cycle_id` (assigned ID or null before an attempt), and `progress_event` (the final observation below, or null). Existing role/status/manifest/usage fields remain required. Main applies a final event, then forwards the updated count; roles do not independently increment it. Old or conflicting history goes to the planner for reconciliation, never to an assumed zero.

An attempt dispatch supplies `cycle_id` and `progress_owner` (the one assigned result role). Cycle IDs are unique within the run; the planner supplies them or preauthorizes main to allocate a monotonic suffix for fixed repair transitions. They are logical record IDs, not invented native runtime handles. Main records a distinct invocation ID, real start time, deadline derived from that invocation's existing budget, actual runtime handle and whether recovery inspection has been used. Planner startup may have null cycle fields. No timestamp or handle may be invented.

## One writer and one event per cycle

Main alone writes the run's `main-state.json` progress ledger; task-board records and human logs reference that ledger rather than maintaining independent counters. The planner owns technical reconciliation and decisions, not a competing runtime counter. This single-writer rule concerns no-evidence cycles; existing repair-state and supplement counters retain their documented ownership and separate accounting.

A cycle is one assigned resolution attempt. An implementation freeze and its independent acceptance share one cycle ID: the implementer returns `progress_event: null`, and the tester closes the cycle. Each subsequent repair/retest uses a new cycle ID while retaining the same underlying problem ID. A diagnostic stage, or an analysis attempt that ends without acceptance, names its original assigned result owner in dispatch. Ordinary forwarding, waiting, formatting corrections and individual diagnostic commands do not create additional cycles.

The result owner emits at most one final event:

```json
{
  "cycle_id": "task-01-r1",
  "problem_id": "task-01-export-empty",
  "outcome": "no_evidence",
  "evidence_paths": ["tasks/task-01/round-1/report.md"],
  "observation": "Output remains empty; the cause was not narrowed."
}
```

`outcome` is `evidence` or `no_evidence`. The owner explains the actual observation; the tester/planner judges its technical validity. Main only checks identity, field completeness and the prescribed arithmetic. The event must match the active cycle, stable problem and assigned owner.

For a new final event, main updates both the processed-cycle record and the stable problem's counter in one replacement of the exact state file: evidence resets the consecutive count, no_evidence increments it. An identical repeat is ignored; a different payload for an already processed cycle is a reconciliation problem. An interrupted/inconsistent update is reconciled before further accounting. At count two or higher, main mechanically routes to the planner with `route_review: true`, even if repair capacity remains. A separately reported critical-premise review flag remains true until the planner resolves it.

Execution errors or an unknown running state do not finish a cycle, increment the no-evidence count or reset history. Preserve any previously recorded events. A missing prerequisite without a valid technical observation remains blocked with `progress_event: null`; it is not a completed technical experiment. An actual partial observation may be reported as evidence while the separate prerequisite blocker remains explicit.

## Missing-return recovery without normal polling

Before delegation, main records the invocation window using the existing role budget. Ordinary wait timeouts do not trigger status probes. An actual host error, or an expired recorded deadline when the host gives control back, permits at most one bounded native status inspection for that exact invocation/handle, if the host exposes it. Reserve the inspection marker in the invocation record before calling the native tool; an interrupted/failed inspection still consumes this one opportunity. Do not scan source/log directories, query repeatedly, nudge, or launch a replacement to find out what happened.

Consume a real returned result normally. If the role is still running, status cannot be established, the handle is invalid or no inspection exists, record `execution_state: unknown` with the actual reason, pause dependent dispatch and report the exact recovery entry/required condition. This is execution uncertainty, not a DUT failure or a passed acceptance. Preserve counters and frozen inputs. Main may issue this mechanical execution-status notice without waiting for a missing planner-authored summary; it does not diagnose technical root cause.

Resume the recorded invocation only through supported native capabilities. Replacing an executor requires evidence that the original execution and candidate-modifying processes ended; then use the existing planner-led recovery and old-to-new handle mapping. Never kill unrelated work or run two writers against the same candidate. Provider/quota failures retain the existing no-automatic-retry rule.

If a foreground host never returns control, these instructions cannot enforce cancellation or an automatic deadline response. Recovery then requires the host/user to restore control. Do not claim a hard watchdog.

## A diagnostic is a stage, not one command

The planner records `diagnostic` in the existing dispatch/plan: stable `episode_id`, the single question, a finite list of `checks` with inputs and distinguishing predictions, stop conditions and `resume_evidence`. It names the result owner and uses the existing remaining invocation/scope budgets. No new total-budget rule is introduced.

One allowed diagnostic stage may run several of those checks. Stop as soon as the question is answered, a prerequisite is missing or the existing budget ends. One uninformative check may be followed by the next predeclared distinguishing check; do not start another diagnostic episode merely to bypass a failed stage. A stage with an actual technical outcome emits one final progress event; stopping solely for a missing prerequisite without a valid technical observation returns `progress_event: null`. If the completed checks add no decision-relevant evidence, return blocked with its recovery condition and a no_evidence event.

Use frozen/read-only candidate inputs and isolated test outputs by default. When diagnosis supports a candidate repair, stop the diagnostic and return its observation before editing the candidate. Main settles that diagnostic cycle once and returns to the original planner, which assigns a new repair/retest cycle with the tester as result owner and continues the original implementer. Record the existing repair round before its first edit, then freeze and obtain independent acceptance. The diagnostic owner cannot also settle the repair cycle. A diagnostic never resets repair, supplement or no-evidence history.
