#!/usr/bin/env python3
"""Offline checks for the distributable Skill, adapters and documentation."""
import json
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "skills" / "relay-workflow"


def frontmatter(path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"Missing YAML frontmatter: {path.relative_to(ROOT)}")
    return yaml.safe_load(text.split("---", 2)[1])


def validate():
    skill = frontmatter(PACKAGE / "SKILL.md")
    assert skill["name"] == "relay-workflow"
    assert 1 <= len(skill["description"]) <= 1024
    assert skill["metadata"]["opencode/autoinvoke"] == "false"
    ui = yaml.safe_load((PACKAGE / "agents/openai.yaml").read_text(encoding="utf-8"))
    assert ui["policy"]["allow_implicit_invocation"] is False
    for role in ("planner", "implementer", "tester"):
        assert (PACKAGE / "references/roles" / f"{role}.md").is_file()
        adapter = ROOT / "adapters/opencode/agents" / f"relay-{role}.md"
        config = frontmatter(adapter)
        assert config["mode"] == "subagent"
        assert config["permissions"] == [{"action": "subagent", "resource": "*", "effect": "deny"}]
        assert f"references/roles/{role}.md" in adapter.read_text(encoding="utf-8")
        assert "model" not in config
    command = frontmatter(ROOT / "adapters/opencode/commands/relay-workflow.md")
    assert command["subagent"] is False
    assert "model" not in command
    checked = 0
    home_segments = [re.escape("/" + name + "/") + r"[^\s/]+" for name in ("Users", "home")]
    private_path = re.compile(r"(?i)(?:[a-z]:[\\/]+Users[\\/]+[^\s/\\]+|" + "|".join(home_segments) + ")")
    secret = re.compile(r"(?:gh[pousr]_[A-Za-z0-9]{30,}|sk-proj-[A-Za-z0-9_-]{30,})")
    ignored = {".git", ".venv", "__pycache__", ".relay-workflow", "local-validation"}
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or any(part in ignored for part in path.relative_to(ROOT).parts):
            continue
        if path.suffix.lower() not in {".md", ".py", ".json", ".yaml", ".yml", ".txt", ".svg"}:
            continue
        text = path.read_text(encoding="utf-8")
        assert not private_path.search(text), f"Personal absolute path in {path.relative_to(ROOT)}"
        assert not secret.search(text), f"Possible credential in {path.relative_to(ROOT)}"
        if path.suffix == ".json":
            json.loads(text)
        if path.suffix == ".md":
            for target in re.findall(r"\]\(([^)]+)\)", text):
                if "://" in target or target.startswith("#"):
                    continue
                target_path = target.split("#", 1)[0]
                if target_path:
                    assert (path.parent / target_path).exists(), f"Broken link in {path.relative_to(ROOT)}: {target}"
        checked += 1
    print(f"PASS: {checked} text files; explicit invocation, three roles, adapters, JSON, links and privacy checks.")


if __name__ == "__main__":
    validate()
