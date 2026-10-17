# Repository instructions

This repository packages a reusable Skill. Editing, installing, explaining or reviewing it does not activate its execution workflow. Keep the workflow explicitly invoked.

- Preserve the relay/planner/implementer/single-tester architecture and bounded defaults unless the user explicitly changes them.
- Keep shared rules in the Skill package. Client adapters reference role files and do not maintain divergent copies.
- Do not bulk-delete files or directories, including through loops or scripts. Delete only one explicitly identified file at a time; request manual cleanup when bulk deletion is needed.
- Preserve unrelated edits, existing client settings and permission/model choices.
- Never include credentials, real conversation/run records, personal absolute paths or private project material in public artifacts.
- Run `python scripts/validate.py` and `python -m unittest discover -s tests -v` for relevant package or installer changes. These checks do not establish a live agent run.
