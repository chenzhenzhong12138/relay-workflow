# References and provenance

Relay Workflow is an original generalization of a user-defined planning, implementation and acceptance process. Its role boundaries and budgets are design choices, not claims about platform guarantees. No private project files or conversation transcripts are included.

## Client documentation

- [Codex / ChatGPT Skill documentation](https://learn.chatgpt.com/docs/build-skills): Skill packaging and explicit invocation policy.
- [OpenCode Skills](https://opencode.ai/docs/skills/): Skill discovery and automatic-selection metadata. Current documentation can differ from an installed release.
- [OpenCode 2.0.28 subagent source](https://github.com/anomalyco/opencode/blob/v2.0.28/packages/core/src/tool/plugin/subagent.ts): verified input/output names, new child sessions, continuation and parent restrictions.
- [OpenCode 2.0.28 skill tool](https://github.com/anomalyco/opencode/blob/v2.0.28/packages/core/src/tool/plugin/skill.ts) and [frontmatter parser](https://github.com/anomalyco/opencode/blob/v2.0.28/packages/core/src/config/plugin/skill-file.ts): `id` and `opencode/autoinvoke`.
- [OpenCode 2.0.28 command loader](https://github.com/anomalyco/opencode/blob/v2.0.28/packages/core/src/config/plugin/command.ts): command templates and primary-session invocation.

## Presentation references

[Anthropic's Skills repository](https://github.com/anthropics/skills) and [Superpowers](https://github.com/obra/superpowers) informed the documentation layout: a clear purpose, quick start, progressive references and practical examples. Their code and workflow instructions are not vendored here. This project is independent and is not endorsed by those projects or the client vendors.
