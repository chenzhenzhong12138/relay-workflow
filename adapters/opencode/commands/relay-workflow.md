---
description: Explicitly execute or resume Relay Workflow in the current work directory
subagent: false
---

The user selected the /relay-workflow command. Preserve the following arguments verbatim:

$ARGUMENTS

Load the installed relay-workflow Skill with the native skill tool (OpenCode 2.0.28: {"id":"relay-workflow"}). Use the returned directory as SKILL_ROOT. Read SKILL.md and its OpenCode runtime adapter.

Start the role chain only when these arguments explicitly request execute/执行 or resume/恢复. Empty arguments, explanation, comparison, or editing the workflow do not start it. This command runs in the current primary conversation; it must not create another controller as a subagent. Use a primary agent with the required file access, such as Build; do not change permissions or models to work around restrictions.

The primary agent only relays and keeps mechanical records. The planner adapts and decomposes the current task. Pass SKILL_ROOT and actual WORK_ROOT/RUN_DIR to every role. Do not treat the installed Skill directory as the user's work directory.
