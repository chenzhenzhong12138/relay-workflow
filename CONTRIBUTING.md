# Contributing

Keep the role chain and its explicit invocation boundary intact. Prefer a focused correction to a new permanent role, another task board, or a larger default budget.

## Local checks

Use Python 3.11 or newer:

```sh
python -m pip install -r requirements-dev.txt
python scripts/validate.py
python -m unittest discover -s tests -v
```

Installer tests use isolated operating-system temporary directories, retain their small fixtures for inspection, and do not touch your installed clients. The checks do not contact a model provider or execute the agent workflow.

For a runtime change, identify the actual client version and tool schema. Explain which operations map to new, continued and completed child conversations. Do not infer a successful run from a tool returning `completed`.

For a workflow change, include a realistic scenario and the expected observable behavior. Distinguish a policy review, a package check, a client loading check and a complete live run. Never invent token savings, benchmark results or hardware observations.

Do not submit credentials, personal absolute paths, real user requests, run directories, customer material or screenshots. Examples should use synthetic inputs. Source provenance belongs in [References](docs/references.md).
