from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
import sys

TOOLS_PATH = Path(__file__).resolve().parents[1] / "apps" / "tools"
if str(TOOLS_PATH) not in sys.path:
    sys.path.insert(0, str(TOOLS_PATH))

from check_pruefungen_solution_sync import check_pair, check_no_duplicate_tasks


class TestPruefungenSolutionSync(unittest.TestCase):
    def _write_pair(self, basis: Path, aufgaben: str, loesung: str) -> tuple[Path, Path]:
        aufgaben_path = basis / "Klausur_AuD_Musteraufgaben_Version99.md"
        loesung_path = basis / "Klausur_AuD_Musterloesungen_Version99.md"
        aufgaben_path.write_text(aufgaben, encoding="utf-8")
        loesung_path.write_text(loesung, encoding="utf-8")
        return aufgaben_path, loesung_path

    def test_default_mode_keeps_legacy_text_flexible(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            basis = Path(tmp_dir)
            aufgaben, loesung = self._sample_docs()
            aufgaben_path, loesung_path = self._write_pair(basis, aufgaben, loesung)

            errors = check_pair(aufgaben_path, loesung_path)
            self.assertEqual(errors, [])

    def test_strict_mode_detects_text_mismatch(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            basis = Path(tmp_dir)
            aufgaben, loesung = self._sample_docs()
            aufgaben_path, loesung_path = self._write_pair(basis, aufgaben, loesung)

            errors = check_pair(aufgaben_path, loesung_path, enforce_text_sync=True)
            self.assertTrue(any("Ueberschrift weicht ab" in e for e in errors))
            self.assertTrue(any("Aufgabenstellung" in e for e in errors))

    def test_apply_mode_updates_solution_text(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            basis = Path(tmp_dir)
            aufgaben, loesung = self._sample_docs()
            aufgaben_path, loesung_path = self._write_pair(basis, aufgaben, loesung)

            errors = check_pair(aufgaben_path, loesung_path, apply=True)
            self.assertEqual(errors, [])

            updated = loesung_path.read_text(encoding="utf-8")
            self.assertIn("### Aufgabe 1: Lineare Suche (3 Punkte)", updated)
            self.assertIn("> Gegeben: `werte = [9, 4, 2]` und `ziel = 4`", updated)
            self.assertIn("> Implementiere eine lineare Suche.", updated)

    def test_detects_algorithm_name_leak_in_aufgabe5_prompt(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            basis = Path(tmp_dir)
            aufgaben = """### **Aufgabe 5: Algorithmen prüfen (8 Punkte)**
**Thema:** BPE 7.2 – Algorithmenanalyse

Das folgende Struktogramm enthält einen Fehler in einer Bubble Sort.

**a) Vermuteter Zweck (3 Punkte)**
"""
            loesung = """### Aufgabe 5 (8)

**Aufgabenstellung (aus Prüfungsblatt):**
> Dummy
"""
            aufgaben_path, loesung_path = self._write_pair(basis, aufgaben, loesung)

            errors = check_pair(aufgaben_path, loesung_path)
            self.assertTrue(any("verraet den Algorithmus" in e for e in errors))

    def test_detects_duplicate_tasks_across_documents(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            basis = Path(tmp_dir)
            content = """### **Aufgabe 1: Testaufgabe (3 Punkte)**
Gib die Zahl 1 aus.
"""

            f1 = basis / "Klausur_AuD_Musteraufgaben_Version1.md"
            f2 = basis / "Klausur_AuD_Musteraufgaben_Version2.md"
            f1.write_text(content, encoding="utf-8")
            f2.write_text(content, encoding="utf-8")

            errors = check_no_duplicate_tasks([f1, f2])
            self.assertTrue(any("Doppelte Aufgabe erkannt" in e for e in errors))

    @staticmethod
    def _sample_docs() -> tuple[str, str]:
        aufgaben = """### **Aufgabe 1: Lineare Suche (3 Punkte)**
**Thema:** BPE 7.2 – Suchalgorithmen

Gegeben: `werte = [9, 4, 2]` und `ziel = 4`
Implementiere eine lineare Suche.

<!-- DOCX-EMBED-SVG: ../../struktogramme/generated/svg/L2_demo.svg -->

**a) Teilaufgabe (3 Punkte)**
"""

        loesung = """### Aufgabe 1 (3)

**Aufgabenstellung (aus Prüfungsblatt):**
> Gegeben: `werte = [1, 2, 3]` und `ziel = 2`
> Implementiere eine Suche.

<!-- DOCX-EMBED-SVG: ../../struktogramme/generated/svg/L2_demo.svg -->
"""
        return aufgaben, loesung


if __name__ == "__main__":
    unittest.main()
