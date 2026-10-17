# Template use

These are valid JSON starter records, not evidence of an executed run. Fill them from actual tool results and frozen task inputs; never treat sample IDs or paths as runtime identities.

- `dispatch.json`: one planner-authorized action; runtime and role names are translated by the active runtime adapter.
- `return.json`: a safe blocked-return example. An actual tester return needs its real handle and relevant evidence. Null manifest fields are valid only before acceptance can start.
- `manifest.json`: an unfrozen starter. Acceptance requires a real workroot/time, `producer_stopped: true`, and all relevant files as `{ "path": "deliverable.txt", "sha256": "actual SHA-256 digest" }`. Inputs/dependencies need stable identities; outputs use workroot-relative paths. Do not accept an empty starter as a frozen candidate.
- `task-record.json`: run-local metadata or a projection of the existing project source, never a competing global task board. Store each handle as `{ "runtime": "codex", "runtime_id": "actual returned ID", "parent_context": "actual parent", "role": "implementer" }`. Keep repair history and stable problem ledgers when recovering.
