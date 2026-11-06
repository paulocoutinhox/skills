import subprocess
import unittest
from unittest.mock import patch

from module_helper import ModuleHelper


class SkillValidationTest(unittest.TestCase):
    MODULE = ModuleHelper.load("validate-skills.py")

    def test_failing_reference_validator_stops_with_its_exit_status(self):
        results = [subprocess.CompletedProcess([], 0), subprocess.CompletedProcess([], 7)]

        with patch.object(self.MODULE.shutil, "which", return_value="skills-ref"):
            with patch.object(self.MODULE.subprocess, "run", side_effect=results) as runner:
                status = self.MODULE.SkillValidationHelper.run()

        self.assertEqual(status, 7)
        self.assertEqual(runner.call_count, 2)

    def test_missing_reference_validator_does_not_report_success(self):
        with patch.object(self.MODULE.shutil, "which", return_value=None):
            with self.assertRaises(SystemExit):
                self.MODULE.SkillValidationHelper.run()
