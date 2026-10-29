# Freeze the task profile before dispatch

The planner writes and freezes `profile.md` for each run before formal dispatch, using the user's actual goal, local project constraints and task type. Repair rounds retain this frozen acceptance profile. The profile is the source of task-specific acceptance; the skill does not impose a particular language, industry, device or artifact format.

Include:

- Actual workroot, authoritative task-record path, allowed write/read areas, preserved unrelated changes and existing user authority.
- One main acceptance goal, selected dependency-closed slice, package IDs/order, batch size and any exact finite user exceptions.
- Intended users/use context, required input sources, deliverable formats, candidate boundaries and dependency/interface assumptions.
- The answerable acceptance question or observable outcome; the actual baseline/version, active configuration/entry point and evidence paths establishing the current state. The original planner owns outcome reconciliation and closeout.
- A brief effort rationale: necessary roles under the explicitly selected chain, proportionate package/check scope, reusable evidence and the reason for the finite budget. Evidence-backed infeasibility answers retain their limited scope; they do not complete an unfinished implementation goal.
- A mapping from acceptance criteria to all three dimensions, concrete checks/thresholds, evidence locations and any predeclared non-applicable dimension with a reason.
- Required tools, data, accounts, devices, environments and external conditions; which are available and which block acceptance.
- Role and command budgets, real timeout/safe-stop methods, output locations, stop/rollback conditions and recovery requirements.

Dimension keys are stable across domains: `functional` means correctness against the request; `engineering` means deliverable quality, reproducibility and applicable professional constraints; `system` means use/integration in the intended context. These are three checklists for one tester, not three agents.

Choose checks proportional to the actual outcome. Examples are prompts for selection, not blanket requirements:

| Task type | Functional | Engineering | System |
| --- | --- | --- | --- |
| Software | Required behavior, meaningful edge cases | Relevant checks, maintainability, security or performance constraints | Actual interfaces and deployment/use environment |
| Documents | Content accuracy and requested coverage | Structure, formatting, rendered layout and accessibility as required | Opens/exports correctly for the intended reader/tool |
| Data/research | Correct transformations, claims and source coverage | Provenance, methods, uncertainty and reproducibility | Downstream consumption, formats and conclusions in context |
| Design | User requirements and intended interactions | Visual consistency, accessibility and export fidelity | Intended device, viewport or handoff use |
| Hardware | Behavior under stated inputs | Applicable timing, resources, electrical/build constraints | Required real device, interfaces, recovery and stability |

Raise necessary checks or reduce the package for high-risk work; do not add standing roles or remove domain gates to save tokens. Missing real-device, timing, source, permission or other required evidence remains `BLOCKED`/`not_run`. Simulated, mocked or offline evidence must retain that label and cannot prove a parent live-system requirement. A dimension is `not_applicable` only when the planner explained it before implementation; the tester cannot invent the exception after a failure.

Scope or acceptance changes return to the original planner before implementation continues and must retain an explicit change record. Never relax a criterion or threshold simply to make a failed candidate pass. The main neither reads this profile nor decides whether a gate applies. Publish only a concise routing/status summary for main.
