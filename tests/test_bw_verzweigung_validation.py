"""Tests fuer BW-konforme Verzweigungsnotation (Wenn/J/, sonst/N)."""

import unittest
import sys
from pathlib import Path

from src.utils.struktogramm_helper import StruktogrammValidator as HelperValidator

TOOLS_PATH = Path(__file__).resolve().parents[1] / "apps" / "tools"
if str(TOOLS_PATH) not in sys.path:
    sys.path.insert(0, str(TOOLS_PATH))

from struktogramm_validator import StruktogrammValidator as CliValidator, ValidationLevel


class TestBwVerzweigungValidation(unittest.TestCase):
    def test_helper_accepts_valid_branch(self) -> None:
        lines = [
            "Wenn x > 0, dann",
            "    J",
            "        Ausgabe: \"positiv\"",
            "    , sonst",
            "    N",
            "        Ausgabe: \"nicht positiv\"",
        ]
        errors = HelperValidator.validate_struktogramm(lines)
        self.assertEqual(errors, [])

    def test_helper_rejects_missing_j(self) -> None:
        lines = [
            "Wenn x > 0, dann",
            "        Ausgabe: \"positiv\"",
        ]
        errors = HelperValidator.validate_struktogramm(lines)
        self.assertTrue(any("'J'" in error and "Wenn" in error for error in errors))

    def test_cli_rejects_wrong_else_indent(self) -> None:
        content = "\n".join([
            "Wenn x > 0, dann",
            "    J",
            "        Ausgabe: \"positiv\"",
            "        , sonst",
            "    N",
            "        Ausgabe: \"nicht positiv\"",
        ])
        results = CliValidator().validate_document(content)
        errors = [r for r in results if r.level == ValidationLevel.ERROR]
        self.assertTrue(any(r.code == "BW_BRANCH_ELSE_INDENT" for r in errors))


if __name__ == "__main__":
    unittest.main()
