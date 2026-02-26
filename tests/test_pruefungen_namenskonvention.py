from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from src.utils.pruefungen_namenskonvention import (
    analysiere_pruefungsdatei,
    ist_konformer_dateiname,
    normalisiere_pruefungsdateien,
)


class TestPruefungenNamenskonvention(unittest.TestCase):
    def test_ist_konformer_dateiname(self) -> None:
        self.assertTrue(ist_konformer_dateiname("Klausur_AuD_Musteraufgaben_Version1.md"))
        self.assertTrue(ist_konformer_dateiname("Klausur_GdP_Musterloesungen_Version12.md"))
        self.assertFalse(ist_konformer_dateiname("Klausur_L2_2_1_Musteraufgaben.md"))

    def test_analysiere_legacy_datei(self) -> None:
        datei = Path("Klausur_L2_2_1_Musteraufgaben_Variante_B.md")
        befund = analysiere_pruefungsdatei(datei)
        self.assertFalse(befund.ist_konform)
        self.assertEqual(befund.vorgeschlagener_name, "Klausur_AuD_Musteraufgaben_Version3.md")

    def test_normalisierung_mit_kollision(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            basis = Path(temp_dir)
            (basis / "Klausur_AuD_Musteraufgaben_Version1.md").write_text("x", encoding="utf-8")
            (basis / "Klausur_L2_2_1_Musteraufgaben.md").write_text("x", encoding="utf-8")

            ergebnis = normalisiere_pruefungsdateien(basis, dry_run=True)

            self.assertEqual(ergebnis.geprueft, 2)
            self.assertEqual(len(ergebnis.umbenennungen), 1)
            self.assertEqual(
                ergebnis.umbenennungen[0].ziel.name,
                "Klausur_AuD_Musteraufgaben_Version2.md",
            )

    def test_normalisierung_fix_rename(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            basis = Path(temp_dir)
            legacy = basis / "Klausur_L2_2_1_Musterloesungen_Variante_A.md"
            legacy.write_text("inhalt", encoding="utf-8")

            ergebnis = normalisiere_pruefungsdateien(basis, dry_run=False)

            self.assertEqual(len(ergebnis.umbenennungen), 1)
            self.assertFalse(legacy.exists())
            self.assertTrue((basis / "Klausur_AuD_Musterloesungen_Version2.md").exists())


if __name__ == "__main__":
    unittest.main()
