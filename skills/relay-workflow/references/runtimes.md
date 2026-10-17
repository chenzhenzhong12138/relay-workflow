# Select one real runtime adapter

Keep the Skill, roles, dispatch/return formats and counters identical across clients. Resolve `SKILL_ROOT` from the actual loaded package and `WORK_ROOT` from the current user's task directory. Never use an installation, cache or previous project's directory as the workroot.

| Available environment | Read only this adapter |
| --- | --- |
| Codex with resumable native subagents | [Codex](runtimes/codex.md) |
| OpenCode 2.0.28 native `subagent` | [OpenCode v2](runtimes/opencode-v2.md) |
| Other names or schemas | Verify the real API before dispatch; unavailable required capabilities mean `BLOCKED` |

`spawn_agent`, `spawn_single_tester`, `followup_task`, `return_to_planner` and `relay_to_user` in dispatch files are stable operation labels, not a promise that a host has tools with those names. Translate only the operation, never the task's scope, acceptance or counts. `spawn_single_tester` creates exactly one tester child; it never expands into three dimension agents.

Use the configured model unless the user explicitly requests another. Do not create a shell shim that pretends to be an agent tool. Installers do not enable missing multi-agent features or change permission policy.

Record real handles together with runtime, role, task/batch and parent context. The native tool's handle is authoritative; a new child may return `runtime_id: null` before main fills it from the tool result. Completion is transport state, not acceptance. Across hosts or parent sessions use the original run files and an explicit old-to-new mapping, preserving counters; do not claim native continuation succeeded.

No adapter adds progress polling, monitors, schedules, external messages or permission bypasses. Missing tools, quota/API failures and required external conditions follow the existing blocked route without automatic retries or main taking over.
