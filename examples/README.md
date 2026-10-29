# Example requests and handoffs

[English overview](../README.md) · [中文入门](../README.zh-CN.md) · [Usage](../docs/usage.md)

These are **illustrative requests and expected routing**, not logs of completed runs or benchmark results. File names describe example working directories; replace them with inputs that actually exist in your task. The planner must inspect those inputs and freeze the real scope and acceptance profile before execution.

## 1. Software: a converter and its usage guide

This request explicitly defines two dependent acceptance packages within one small goal:

```text
$relay-workflow execute: Deliver a small CSV-to-JSONL command in this Python repository, using the standard library only. Use two ordered work packages: (1) implement the converter and relevant tests; (2) document and verify its usage against the accepted converter. Treat the first CSV row as field names and preserve field values as strings. Read UTF-8 input, emit one JSON object per data row, and report malformed row widths with a nonzero exit code. Do not overwrite existing output unless the user selects an unused path. Document a successful example and a malformed-input example in README.md. Keep changes within the converter, its tests, and that usage section; do not publish a package.
```

The planner can freeze package A for converter behavior and package B for documented use. B depends on A's accepted interface. The following shows a possible route, without claiming that these outcomes occurred:

| Step | Role handoff | Expected artifact or return |
| --- | --- | --- |
| Plan | Main → planner | Profile, A → B dependency, bounded dispatch |
| A implementation | Main → fresh implementer A | Stopped producer, frozen converter manifest |
| A acceptance | Main → fresh tester A | One integrated report for A's manifest |
| If A fails without a route-review trigger | Same implementer A → same tester A | Actual repair count increments; new manifest and retest |
| Next package | Original planner → fresh implementer B | Documentation based on accepted A |
| B acceptance | Main → fresh tester B | Examples checked against A; integrated report for B |
| Closeout | Original planner → main → user | Authoritative statuses and verbatim user summary |

For A, functional checks cover row values and errors; engineering checks cover relevant tests and reproducibility; system checks exercise the command as a user would. For B, checks cover accurate instructions, readable structure, and reproducible commands. Actual checks and evidence are selected in the profile. A blocker prevents a false PASS and returns to the original planner.

## 2. Documents: a release note from local sources

```text
/relay-workflow execute: Turn CHANGELOG.md and docs/migration.md into a concise docs/release-note.md for users upgrading this release. Include the supported changes, breaking changes, migration steps, and known limitations found in those files. Preserve exact command and option names. Flag contradictions or missing version information instead of inventing facts. Only edit docs/release-note.md. Acceptance requires every factual claim to trace to a local source, links to resolve, and the Markdown to read cleanly in the repository viewer. Do not publish or send the note.
```

Expected closure: a frozen release note and one integrated report covering source accuracy, structure and links, and the intended reader/viewer. If a source contradiction prevents accurate guidance, the planner receives a blocker with the required clarification. No unrelated hardware or application build is required merely because the workflow has a system dimension.

## 3. Data: a reproducible local summary

```text
$relay-workflow 执行：根据当前目录 data/orders.csv 生成 analysis/order-summary.csv 和 analysis/method.md。输入应包含 order_id、region、quantity、unit_price；先确认字段和单位。按 region 汇总订单数、总数量和金额，金额使用十进制定点计算。缺失、重复 order_id、非法数量或价格须记录处理规则和计数，不得静默丢弃；无法确定规则时返回所需澄清。只写 analysis/，保留原数据。验收要求汇总可由原始输入复算，方法记录输入指纹、规则、检查结果及局限，并确认输出可被普通 CSV 读取器读取。不访问外部服务，不上传数据。
```

Expected closure: a frozen output and method, with evidence for arithmetic and reconciliation, provenance and reproducibility, and downstream CSV use. The profile resolves what counts as an order and how invalid records are handled before implementation. Missing columns or unresolved units cannot become a passing analysis.

## 4. Hardware: a deliberately offline counter task

```text
/relay-workflow 执行：在当前 RTL 项目新增一个参数化无符号计数器和自检仿真，用作离线教学示例。位宽参数至少为 1；上升沿同步高有效复位为 0；enable 为 1 时加一并按位宽回绕，否则保持。沿用项目语言和已有仿真工具，仅写新模块、对应 testbench 和简短说明。验收覆盖复位优先、保持、连续计数、回绕以及位宽 1 和 8，保存真实仿真命令和结果。本轮只交付离线 RTL 与仿真证据，不包含板级集成目标，不下载位流、不写 Flash、不操作设备；缺少仿真工具则返回 blocked。
```

Expected closure: a frozen RTL candidate, real simulator evidence, and an integrated report whose offline scope is explicit. The planner chooses applicable engineering and integration checks for this teaching artifact. Passing this package would not establish timing closure, board operation, or acceptance of a larger hardware system.

## 5. Route reassessment and candidate convergence

These are synthetic policy scenarios and expected behavior, not claims of completed executions.

- **Repeated repairs without evidence:** two source-changing repairs still export zero bytes, with no new interface observation and one repair remaining. Return `route_review: true` to the original planner before a third repair; retain the two used repairs. One bounded diagnostic may distinguish causes within remaining authority and budget. If it yields no decision-relevant evidence, close as blocked with a recovery condition.
- **A testable disagreement:** two roles disagree about byte order on the same frozen input, and an independent decoder with known vectors is available and authorized. The assigned tester executes the distinguishing check and reports the real observation and its scope; another reasoning-only review is not verification.
- **Conflicting candidates:** a baseline supports only old functionality; candidate A passes functionality but fails timing, and candidate B passes timing but fails functionality. State that the new goal has no qualified candidate. Keep the baseline's limited fallback scope explicit, record each candidate's status, and recommend one evidence-supported next action without combining A and B into a PASS.

The user summary answers what is usable, what was verified, which unknowns changed, and why the next step is worthwhile. A feasibility question answered negatively may close its investigation; an unfinished implementation goal retains its failed or blocked status.

## Recovery example

Use the path returned by a real run; `example-run` below is a placeholder:

```text
$relay-workflow resume: C:/work/catalog/.relay-workflow/runs/example-run; objective: Finish the remaining checks within the frozen scope after the required tool becomes available.
```

For OpenCode, replace `$relay-workflow` with `/relay-workflow`. File-based recovery preserves task, repair, supplement, and budget history and records any old-to-new runtime ID mapping. It does not reset a failed outcome's repair allowance. See the [usage guide](../docs/usage.md) for all invocation forms.
