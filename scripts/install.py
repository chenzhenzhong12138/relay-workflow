#!/usr/bin/env python3
"""Install Relay Workflow without deleting or overwriting existing user files."""
from __future__ import annotations

import argparse
import json
import os
from dataclasses import dataclass
from pathlib import Path

REPOSITORY = Path(__file__).resolve().parents[1]
SKILL_NAME = "relay-workflow"


class InstallError(Exception):
    pass


@dataclass(frozen=True)
class Entry:
    source: Path
    destination: Path
    boundary: Path


def installation_plan(
    client: str,
    scope: str,
    *,
    source_root: Path = REPOSITORY,
    project_root: Path | None = None,
    home: Path | None = None,
    codex_home: Path | None = None,
    config_home: Path | None = None,
) -> list[Entry]:
    home = home or Path.home()
    source_root = source_root.resolve()
    package = source_root / "skills" / SKILL_NAME
    if not (package / "SKILL.md").is_file():
        raise InstallError("The source Skill package is incomplete.")
    files = sorted(p for p in package.rglob("*") if p.is_file())
    if any(p.is_symlink() for p in package.rglob("*")):
        raise InstallError("Skill source symlinks are not installed.")
    if scope == "project":
        if project_root is None:
            raise InstallError("--project-root is required for project installation.")
        if not project_root.is_dir():
            raise InstallError("The project root must be an existing directory.")
        boundary = project_root.resolve()
        bases = {"codex": boundary / ".agents", "opencode": boundary / ".opencode"}
    else:
        bases = {
            "codex": (codex_home or home / ".codex").resolve(),
            "opencode": ((config_home or home / ".config") / "opencode").resolve(),
        }
    selected = ("codex", "opencode") if client == "both" else (client,)
    result: list[Entry] = []
    for selected_client in selected:
        base = bases[selected_client]
        allowed = boundary if scope == "project" else base
        destination = base / "skills" / SKILL_NAME
        result.extend(Entry(p, destination / p.relative_to(package), allowed) for p in files)
        if selected_client == "opencode":
            adapter = source_root / "adapters" / "opencode"
            for relative in (
                "agents/relay-planner.md",
                "agents/relay-implementer.md",
                "agents/relay-tester.md",
                "commands/relay-workflow.md",
            ):
                result.append(Entry(adapter / relative, base / relative, allowed))
    return result


def preflight(entries: list[Entry]) -> list[tuple[Entry, str]]:
    """Check every destination before the first directory or file is created."""
    checked: list[tuple[Entry, str]] = []
    for entry in entries:
        if not entry.source.is_file() or entry.source.is_symlink():
            raise InstallError(f"Missing or linked source: {entry.source}")
        if not entry.destination.resolve().is_relative_to(entry.boundary.resolve()):
            raise InstallError(f"Destination escapes its install boundary: {entry.destination}")
        if entry.destination.is_symlink():
            raise InstallError(f"Linked destination is not overwritten: {entry.destination}")
        if entry.destination.exists():
            if not entry.destination.is_file() or entry.destination.read_bytes() != entry.source.read_bytes():
                raise InstallError(f"Existing content differs; nothing installed: {entry.destination}")
            checked.append((entry, "unchanged"))
        else:
            checked.append((entry, "create"))
    return checked


def install(entries: list[Entry], *, dry_run: bool = False) -> dict:
    checked = preflight(entries)
    created = 0
    for entry, state in checked:
        if state != "create" or dry_run:
            continue
        entry.destination.parent.mkdir(parents=True, exist_ok=True)
        # Exclusive creation also protects a file created after preflight.
        with entry.destination.open("xb") as output:
            output.write(entry.source.read_bytes())
        created += 1
    return {
        "dry_run": dry_run,
        "created": created,
        "would_create": sum(state == "create" for _, state in checked),
        "unchanged": sum(state == "unchanged" for _, state in checked),
        "destinations": [str(entry.destination) for entry, _ in checked],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--client", choices=("codex", "opencode", "both"), default="both")
    parser.add_argument("--scope", choices=("user", "project"), default="user")
    parser.add_argument("--project-root", type=Path)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--json", action="store_true", help="Print the installation result as JSON.")
    args = parser.parse_args(argv)
    try:
        plan = installation_plan(
            args.client,
            args.scope,
            project_root=args.project_root,
            codex_home=Path(os.environ["CODEX_HOME"]) if os.environ.get("CODEX_HOME") else None,
            config_home=Path(os.environ["XDG_CONFIG_HOME"]) if os.environ.get("XDG_CONFIG_HOME") else None,
        )
        result = install(plan, dry_run=args.dry_run)
    except (InstallError, OSError) as error:
        parser.exit(2, f"Installation stopped: {error}\n")
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        verb = "Would create" if args.dry_run else "Created"
        count = result["would_create"] if args.dry_run else result["created"]
        print(f"{verb} {count} files; {result['unchanged']} unchanged.")
        for destination in result["destinations"]:
            print(f"  {destination}")
        print("Restart or reopen your client if the explicit entry is not visible yet.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
