# Bounded work and stopping rules

These are operational contracts enforced by the agents and available command controls, not claims that a host automatically terminates work. A yield, session ID or early tool return is not an execution timeout.

## Scope

Per user-requested round: one main acceptance goal; at most four formal work packages, including ready and blocked dependency packages; exactly two planning levels, request → package. Each package has one main outcome and at most five semantic implementation steps. Copying a file, recording an ID, hashing a candidate or another mechanical action does not create a package or another agent.

For a larger request, the planner selects the smallest dependency-closed slice that can be accepted within these limits. Record at most three remaining topics without expanding or automatically scheduling them. If no slice can close, deliver only a scope-freezing package identifying the unresolved boundary and required user choice. Do not disguise additional packages as subtasks, batches, new runs, new IDs or successive automatic slices.

Only a current user instruction containing an explicit finite numeric exception can enlarge a scope limit or batch size. Record its exact wording, numeric bound and affected limit; keep other defaults. A vague request to do everything is not an exception. Batch size defaults to one. An explicitly authorized batch larger than one gets one fresh implementer and one fresh integrated tester, with per-task scope, status and repair accounting retained.

## Role invocation budget

Each dispatch or continuation allows at most 30 actual tool calls, 15 minutes for the planner, and 45 minutes for implementer/tester. Count actual underlying tool invocations, including tool calls composed inside a wrapper; a wrapper does not make multiple calls count as one. Check remaining budget before starting work, record elapsed time and calls, and return before exceeding the bound. The planner may freeze a smaller or another finite execution budget with a reason before dispatch; a running role cannot enlarge it itself.

- One problem: at most three targeted search/read rounds. Each round has a stated question and inspects its results before another search.
- A failing command: initial attempt plus at most one retry supported by new evidence. Identical retries or retries after external/API/quota failure are forbidden.
- Two consecutive work cycles without new evidence, a substantive artifact change, a valid verification result or a testable narrowing of the hypothesis: return `BLOCKED` with a recovery condition. Reworded plans, logs, repeated inputs or merely proposing another action do not count as progress.
- Read/search command: at most 60 seconds; local check/simulation: five minutes; long build/export: 30 minutes, unless a different finite command bound was frozen by the planner with a reason.

Use a real timeout and safe termination method available in the host. Preserve useful outputs on timeout. A persistent process must have a bounded lifetime and safe stop method. If those controls cannot be provided, do not start an unbounded command. Missing time/call accounting is a recovery problem, not a reason to reset counters.

## Information supplements versus repairs

Main handles a problem only after a role returns it. Key the ledger by stable `task_id` + `problem_id`. Allow at most two supplemental returns to the responsible role, only when `new_information=true`, evidence paths, a concrete recovery path and an action within frozen scope are all present, and required fields are neither missing nor contradictory. Main applies these field checks mechanically and forwards the supplied wording; it does not solve the problem.

No new information, missing/contradictory fields, or an exhausted supplement count goes directly to the original planner as `blocked`. External missing permission/tool/device/data/user input and API/quota errors also go directly to the planner; do not auto-retry or expand authority. Ownership is fixed: scope/acceptance → planner; implementation → implementer; reproduction/report → tester. Role changes, paraphrases, new task aliases and recovery runs do not reset the same problem's ledger.

Round 0 is initial acceptance. Actual changes made to repair failed acceptance consume rounds 1–3. Before the first repair edit, the implementer records that round as started in its per-task `repair-state.json`; the planner reconciles this into the authoritative task ledger. Empty handoffs, missing prerequisites and supplemental information do not count as actual repair. The tester binds each round's evidence to its newly frozen manifest. After three actual repairs, retain the failed status and return to the planner. An independent follow-on package must stay within the current boundary and cannot reset repairs for the same failed outcome. Supplement counts and repair counts are separate.

## Authorization and files

Resolve the actual workroot and relevant links/junctions; all modifications must remain within the frozen allowed scope and current user authority. Preserve unrelated changes. No batch deletion of files or directories, including through loops, scripts, subprocesses or another agent. A deletion may target only one explicitly named file at a time. If bulk deletion is required, stop that action and ask the user to perform it manually.

Do not infer permission for external messages, publication, deployment, installation, credential access, device writes or unrelated projects from skill activation. Preserve applicable local constraints. Missing required conditions are `blocked`/`not_run`, never PASS. Stop dispatch on a user stop request and provide the actual run recovery path.
