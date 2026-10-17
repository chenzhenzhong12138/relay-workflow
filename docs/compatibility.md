# Compatibility and validation boundaries

| Component | Supported contract | What a check establishes |
| --- | --- | --- |
| Skill package | `SKILL.md`, references, explicit invocation metadata | Packaging and link/format consistency |
| Codex | Native resumable subagents; collaboration interface documented | Explicit-only configuration and role instructions; actual tools must be available |
| OpenCode | v2.0.28 `skill(id)` / `subagent(agent, description, prompt, sessionID?)` | Thin native agent/command definitions and source-verified mapping |
| Installer | Python 3.11+, Windows/macOS/Linux paths | Offline file installation, preflight conflicts, idempotence and scope |
| CI | Windows and Linux offline validation | Package, installer and documentation checks; no paid provider calls |

OpenCode v1 `task/task_id` and future unknown tool schemas are not claimed as tested. No client configuration is changed to enable missing features. Run the workflow only in an environment that actually provides the necessary native tools and permitted file access.

The rule set is a set of role instructions, not a background agent daemon. Its time/tool budgets are self-stop and native-command-control contracts. It cannot guarantee forceful platform termination, a wake-up from an indefinitely lost child, or a fixed token saving.

Three different claims must remain separate:

1. **Package checks:** valid metadata/JSON, links, role references and safe installation behavior.
2. **Client loading checks:** the current client actually discovers the Skill or loads a native role definition.
3. **Live workflow checks:** a real request traverses the planned role chain, including any repair and recovery.

The initial release includes offline automated checks and local configuration loading checks where available. It does not claim exhaustive live multi-client execution or task-domain acceptance. Illustrative examples are labeled as such. A successful installer or a child returning `completed` is not evidence that a user's actual task passed.

Installed user-scope copies come from the same versioned source package; they are not separately maintained rule sets. Task-specific changes belong in the run profile. A reinstallation with identical bytes is a no-op; different existing files are preserved and reported as conflicts. There is no force-overwrite or automatic cleanup command.
