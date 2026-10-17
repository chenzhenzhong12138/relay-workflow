import tempfile
import unittest
from pathlib import Path

from scripts.install import Entry, InstallError, install, installation_plan


class InstallTests(unittest.TestCase):
    def setUp(self):
        # Fixtures are intentionally retained for inspection; no recursive deletion.
        self.fixture = Path(tempfile.mkdtemp(prefix="relay-workflow-test-"))
        self.source = self.fixture / "source"
        package = self.source / "skills" / "relay-workflow"
        package.mkdir(parents=True)
        (package / "SKILL.md").write_text("---\nname: relay-workflow\n---\n", encoding="utf-8")
        for relative in (
            "agents/relay-planner.md", "agents/relay-implementer.md",
            "agents/relay-tester.md", "commands/relay-workflow.md",
        ):
            target = self.source / "adapters" / "opencode" / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text("adapter\n", encoding="utf-8")
        self.home = self.fixture / "home"

    def plan(self, client="both", **kwargs):
        return installation_plan(client, "user", source_root=self.source, home=self.home, **kwargs)

    def test_both_clients_receive_package_and_opencode_roles(self):
        result = install(self.plan())
        self.assertEqual(result["created"], 6)
        self.assertTrue((self.home / ".codex/skills/relay-workflow/SKILL.md").exists())
        self.assertTrue((self.home / ".config/opencode/commands/relay-workflow.md").exists())

    def test_dry_run_writes_nothing(self):
        result = install(self.plan(), dry_run=True)
        self.assertEqual(result["would_create"], 6)
        self.assertFalse(self.home.exists())

    def test_identical_reinstall_is_a_no_op(self):
        install(self.plan())
        result = install(self.plan())
        self.assertEqual(result["created"], 0)
        self.assertEqual(result["unchanged"], 6)

    def test_conflict_stops_before_any_other_file_is_written(self):
        conflict = self.home / ".config/opencode/commands/relay-workflow.md"
        conflict.parent.mkdir(parents=True)
        conflict.write_text("my command", encoding="utf-8")
        with self.assertRaises(InstallError):
            install(self.plan())
        self.assertEqual(conflict.read_text(), "my command")
        self.assertFalse((self.home / ".codex").exists())

    def test_project_install_does_not_touch_home_or_configuration(self):
        project = self.fixture / "project"
        project.mkdir()
        config = project / "opencode.json"
        config.write_text('{"model":"keep-me"}', encoding="utf-8")
        plan = installation_plan("both", "project", source_root=self.source, project_root=project, home=self.home)
        install(plan)
        self.assertTrue((project / ".agents/skills/relay-workflow/SKILL.md").exists())
        self.assertTrue((project / ".opencode/skills/relay-workflow/SKILL.md").exists())
        self.assertEqual(config.read_text(), '{"model":"keep-me"}')
        self.assertFalse(self.home.exists())

    def test_configured_user_roots_are_respected(self):
        codex = self.fixture / "custom-codex"
        config = self.fixture / "custom-config"
        install(self.plan(codex_home=codex, config_home=config))
        self.assertTrue((codex / "skills/relay-workflow/SKILL.md").exists())
        self.assertTrue((config / "opencode/commands/relay-workflow.md").exists())

    def test_path_escape_is_rejected(self):
        source = self.source / "skills/relay-workflow/SKILL.md"
        with self.assertRaises(InstallError):
            install([Entry(source, self.fixture / "outside.md", self.home)])
        self.assertFalse((self.fixture / "outside.md").exists())

    def test_project_symlink_escape_is_rejected_before_any_write(self):
        project = self.fixture / "linked-project"
        outside = self.fixture / "linked-outside"
        project.mkdir()
        outside.mkdir()
        try:
            (project / ".opencode").symlink_to(outside, target_is_directory=True)
        except OSError:
            self.skipTest("Directory symlink creation is unavailable on this platform.")
        plan = installation_plan("both", "project", source_root=self.source, project_root=project, home=self.home)
        with self.assertRaises(InstallError):
            install(plan)
        self.assertFalse((project / ".agents").exists())
        self.assertEqual(list(outside.iterdir()), [])


if __name__ == "__main__":
    unittest.main()
