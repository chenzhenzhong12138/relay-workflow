# Frozen candidates and integrated evidence

## Freeze before acceptance

The implementer stops candidate edits and all activity capable of modifying it before creating the task's unique manifest. Record task/batch, round, workroot, freeze time, `producer_stopped: true`, files with workroot-relative paths and SHA-256 hashes, relevant input/dependency identities and versions, and permitted test-output locations. Capture files relevant to acceptance, including configuration and input data where needed; a manifest cannot omit a dependency that changes the result. External inputs need a stable digest/version or a documented immutability limitation that prevents overstating acceptance.

Hash the completed manifest itself and return its path/hash as metadata. Candidate changes after freeze invalidate that binding. The tester verifies candidate file hashes and manifest identity before testing and again before final acceptance. Testing writes evidence to separate allowed output locations; generated outputs/caches are explicitly classified and cannot silently change a bound candidate. If a required test must alter the candidate, stop acceptance and obtain a newly frozen candidate rather than claiming the old manifest passed.

No implementer edits or leftover modifying processes may overlap acceptance. The tester is a different fresh agent for each task or authorized batch and never repairs the candidate. It may execute planned checks and create its own report/evidence within the frozen scope.

## One integrated report

Write one integrated report per task per round, with `dimension: integrated` and entries for `functional`, `engineering`, `system`. A batch can share its report file only with distinct task sections and manifest bindings. Each dimension records `PASS`, `FAIL`, `BLOCKED`, `not_run` or preplanned `not_applicable`, its criteria, observed result, exact evidence paths and limitations. Include relevant commands/tool versions, actual exit status, input/environment identity and reproduction steps; distinguish real execution from static review, simulation or inference.

Overall `PASS` requires the current manifest to match, all required checks to pass, and all non-applicable decisions to have been frozen by the planner. A missing mandatory condition yields overall `BLOCKED`, with affected checks `not_run`/`BLOCKED`. A completed check that violates acceptance yields `FAIL`. Do not invent outputs, substitute a mock for required reality, or use the mere existence of a report as proof.

## Repairs and evidence reuse

On `FAIL`, report stable problem IDs, failed criteria, reproduction evidence and the affected retest set. The original implementer repairs within the frozen scope, records actual repair use and freezes a new manifest. The original tester determines the final affected checks and retests them. Only the tester may retain unaffected evidence: explicitly bind each retained result to the new manifest and justify why its relevant inputs/dependencies are unchanged. Never concatenate PASS results from different candidates into an overall PASS. If impact is uncertain, rerun the necessary check or report blocked; main does not make this judgment.

Keep raw artifacts and detailed reports in the run. Return only compact metadata to main. The original planner reads evidence for authoritative task status, handoff and closeout. Implementers record useful task-specific lessons; these do not become automatic global policy.
