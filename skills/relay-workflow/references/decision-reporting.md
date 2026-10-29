# Route decisions and understandable progress

This contract applies inside an explicitly started workflow. The original planner owns technical route decisions and user-facing explanations; main checks compact fields and relays text unchanged. Use existing roles, files, operations and budgets. Read [shared control fields and recovery](control-contract.md); it is authoritative for envelopes, cycle ownership, missing returns and diagnostic-stage boundaries.

## Before executing a route

Write each package as an answerable acceptance question or observable deliverable, rather than an open-ended activity such as “research more” or “keep optimizing.” In the existing plan, state the observable goal, confirmed facts, the most important unverified premise, the cheapest relevant check, its predicted result and a result that would change the plan. Distinguish facts, hypotheses and recommendations. The AI supplies and explains these; do not require a novice user to discover the technical premises.

Before creating a replacement, establish the actual current source/configuration, baseline/version, entry point, available results and live blocker from relevant evidence. Record those sources in the existing plan/profile; a stale report or an unused file does not establish the current state. Pure text/configuration work inspects only its relevant inputs.

The original planner is accountable for closing the selected outcome: reconcile component results against the intended use path, consolidate candidates and evidence, name what is usable, and provide one reproducible entry point plus remaining blockers. This responsibility does not transfer to the user when role outputs disagree, and does not permit the planner to implement or waive required testing. Technical details remain with their existing owners.

An evidence-backed negative finding is useful progress. State the demonstrated failure, applicable conditions, evidence and bounded alternative/recovery. A feasibility investigation can close when its question has been answered. An implementation goal remains failed/blocked until its original acceptance is achieved; an unrun check or missing tool is uncertainty, not proof that a route is impossible.

## When to reassess

Set `route_review: true` immediately when evidence contradicts a critical premise, a required interface/model is unverified and invalidates the current inference, or a proposed workaround changes the agreed deliverable or mandatory acceptance. Also trigger after two consecutive work cycles on the same unresolved problem without decision-relevant new evidence.

A cycle is one assigned resolution attempt and its final result, as defined by the control contract. A substantive analysis attempt may end without evidence; ordinary forwarding alone is not a new cycle. Repeated substantive reasoning attempts without new observations count toward the no-evidence limit. New evidence confirms/refutes a premise, locates an interface failure, narrows the cause with an observable result, or proves a changed behavior under relevant acceptance. A useful failed experiment counts. Code edits, a new manifest, another report, repeated identical failures, or multiple AI opinions alone do not count. Record the actual observation and what judgment changed; do not invent a confidence percentage.

Main alone accounts for `no_evidence_cycles` under the stable underlying problem using the deduplicated cycle ledger. The assigned result role reports observations; other roles do not increment the count. Preserve it across repair rounds, handoffs, recovery and aliases. Reset it only from an explained evidence event; unknown history goes to planner reconciliation.

## Routing has priority over automatic repair

An implementer or tester that detects a trigger stops repetitive candidate changes and returns the existing FAIL/BLOCKED status, stable problem record, `route_review: true`, `route_review_path` and `no_evidence_cycles`. Use reason `no_progress` for evidence stagnation and preserve any actual external blocker. The next operation is `return_to_planner`, even when fewer than three repairs have been used. Main does not diagnose the issue.

The planner records the review decision in the existing plan/notes and sets `route_review: false` only on its supported next dispatch; this does not clear history or counters. The planner reads the evidence and decides among: continue with a supported, testable repair; perform a smaller distinguishing experiment; change the technical route within authorized scope; or close as blocked with a recovery condition. Explain the recommendation, alternatives that materially differ, expected benefit, cost/risk and remaining uncertainty. Reversible choices inside existing scope may proceed autonomously. Changing the user's goal, required acceptance, permissions or resource limits requires the corresponding user decision; a route review grants none of these.

When evidence is insufficient, the planner may dispatch one bounded diagnostic stage for that unresolved review episode, using existing roles and remaining budgets. Use the [control contract](control-contract.md) to predeclare the finite checks, question, predictions, stop conditions and evidence required before resuming repairs; several predeclared checks may belong to this one stage. If the diagnostic provides no decision-relevant evidence, close as blocked until relevant evidence or conditions change; do not repeat review/diagnostic dispatches. Preserve all repair, supplement, scope and execution counters. A diagnosis that requires a candidate repair first closes its diagnostic result and follows the control contract into a new tester-owned repair/retest cycle; the actual repair consumes its existing round. Three repairs is a ceiling, not a target.

## Resolve disagreements with action

For a repeated objection, identify the disputed claim, the shared candidate/version, evidence each side uses and the observation that would distinguish them. First reconcile differing inputs or acceptance. For a testable factual dispute with an authorized, feasible check, the assigned implementer/tester executes the smallest relevant check and reports its actual result in the same work cycle; the planner dispatches that action when it owns only planning. A proposed command, another opinion or a restated concern does not complete verification. Missing tools, data, device, authority or budget require a concrete blocker and recovery condition.

Use the existing owner and independent tester. An objection should cite a concrete trigger/source and a falsifiable criterion or feasible check; an unverified concern stays a hypothesis. Record the result and whether the claim is supported, refuted or still unresolved. A design tradeoff that evidence cannot decide returns once to the planner for a recommendation based on the user's goal. If mandatory acceptance is satisfied, speculative concerns alone do not demand unlimited additional proof. Explain material residual uncertainty; apply route-review/cycle limits to repeated discussion. Do not create extra reviewers just to obtain agreement.

Before an additional read, review, build or variant, name the unresolved question and how its result can change the next decision. Reuse applicable existing evidence. Perform required, meaningful verification; omit activity that cannot affect acceptance or a live decision. A short purpose in existing notes or the work-cycle explanation suffices; do not create a document or approval exchange for each tool call. This rule does not waive independent testing or mandatory gates.

## Converge candidates into a usable result

For each main acceptance outcome, maintain one current integration candidate and a known working fallback when one exists. A controlled comparison may use isolated variants derived from identified inputs. Explain what question a new variant answers; inspect and reuse relevant existing candidates before generating another revision. Independent tasks may still proceed within their separate allowed scopes.

The implementer records a new variant's purpose, exact source/manifest, relation to the baseline and observed result in existing notes. The tester binds conclusions to the actual candidate. The planner consolidates selection in the existing task record/plan and handoff: candidate path/version, role (fallback/current/comparison), verified coverage, failed or untested gates, and selected/retained/superseded status with reason. Use indexing and clear entry points; preserve history and applicable deletion restrictions, without creating another task board or silently overwriting other work.

Every package closeout includes a **Current choice** statement: the usable version and its proven scope, or explicitly no qualified candidate for the current goal; the one recommended next candidate/action and why; and the location of the full candidate/evidence index. “Recommended for further testing” is distinct from “accepted for use.” Select using the agreed gates and relevant evidence, not revision numbers or a mixture of different candidates' PASS results. A working fallback may cover only old functionality. Consolidating the result and its reproducible entry point is part of delivery; leaving a list of unexplained alternatives is incomplete closeout.

## Reuse documents without weakening evidence

Preserve frozen acceptance, candidate identity and independent reports. Unchanged input indexes, interface guides or acceptance definitions may be referenced by exact version/hash from the current plan; new copies are required only for changed inputs or contracts. Keep one authoritative technical closeout in the handoff. A separate final summary may be a short pointer when it adds no distinct information; the user summary remains concise and self-contained. Dispatch supplies the actual readable paths, so roles do not require duplicate documents merely for conventional filenames. Update relevant differences rather than rewriting unchanged history.

## Progress explanations

Write a concise, self-contained plain-language summary after acceptance of a package, when blocked, when the route changes and at closeout. The planner owns `user-summary.md`; main relays it unchanged. For an event requiring immediate explanation, an implementer/tester may supply a plain-language evidence paragraph with its return, which main relays unchanged before the prescribed continuation. This does not create a new agent, a monitoring loop or a planning round for every minor action.

The explanation contains, in a natural paragraph or short list:

1. **Actual result:** what now works, remains failed or has not been tested, in relation to the user's goal.
2. **Basis and boundary:** the few decisive observations, the method/source and useful links to evidence and candidate version. Explain what they prove and what remains outside their coverage. Label reused evidence and advice that was not executed.
3. **Judgment:** the supported conclusion and the important remaining hypothesis. Include contradictory evidence; distinguish the result from its explanation.
4. **Next step:** the recommended action and why it is worth doing. For a meaningful route choice, explain the cost/risk and what result would change it. Label estimates and unknown costs honestly.
5. **User decision, when needed:** the precise tradeoff, recommended option and why the current authority cannot settle it. Omit this item when work can continue within existing authorization.

Use the user's language and explain necessary terms on first use. Prefer concrete outcomes to task IDs or internal status jargon; keep detailed commands and hashes behind evidence links. Do not substitute an unsupported completion percentage, “almost done” or “only one step left” for a known remaining scope. A local PASS cannot establish production integration, real-device behavior or long-term performance. Scale the explanation to the task; a small change may need only a short paragraph.

Before sending, the existing summary must answer four questions: what is usable now; what was actually verified in this segment; which unknowns were reduced and which remain; and why the next action is worth doing. Say unknown or not_run where applicable. Check that each completion claim has evidence and each important limitation is visible. Add a short reusable lesson when a resolved cause changes future decisions; reuse existing lessons notes rather than creating another reporting system.
