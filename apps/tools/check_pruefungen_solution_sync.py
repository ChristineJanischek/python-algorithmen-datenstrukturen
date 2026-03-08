#!/usr/bin/env python3
"""Prueft die Konsistenz zwischen Klausur-Aufgaben und Musterloesungen.

Routine-Ziel:
- Bei Aenderungen in `Klausur_AuD_Musteraufgaben_VersionX.md` sicherstellen,
  dass die zugehoerige `Klausur_AuD_Musterloesungen_VersionX.md` konsistent ist.
- Als CI-Gate ausfuehren, um vergessene Loesungsupdates frueh zu blockieren.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PRUEFUNGEN_DIR = ROOT / "docs" / "pruefungen"


@dataclass
class Section:
    nummer: int
    text: str


def _extract_sections(content: str) -> dict[int, Section]:
    header_pattern = re.compile(r"^###\s+\*\*Aufgabe\s+(\d+)", re.MULTILINE)
    matches = list(header_pattern.finditer(content))
    sections: dict[int, Section] = {}

    for idx, match in enumerate(matches):
        nummer = int(match.group(1))
        start = match.start()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(content)
        sections[nummer] = Section(nummer=nummer, text=content[start:end])

    return sections


def _extract_embed_svgs(section_text: str) -> list[str]:
    return re.findall(r"DOCX-EMBED-SVG:\s*(.+)", section_text)


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def check_pair(aufgaben_path: Path, loesung_path: Path) -> list[str]:
    errors: list[str] = []

    aufgaben_content = _read(aufgaben_path)
    loesung_content = _read(loesung_path)

    aufgaben_sections = _extract_sections(aufgaben_content)
    loesung_sections = _extract_sections(loesung_content)

    # Legacy-Dateien ohne strukturierte Abschnittsueberschriften werden nicht hart geblockt.
    if not aufgaben_sections or not loesung_sections:
        return errors

    for nummer, aufgabe in aufgaben_sections.items():
        if nummer not in loesung_sections:
            errors.append(
                f"{loesung_path.relative_to(ROOT)}: Aufgabe {nummer} fehlt (existiert in {aufgaben_path.name})."
            )
            continue

        loesung = loesung_sections[nummer]

        # 1) Diagramm-Referenzen muessen in der Loesung ebenfalls auftauchen.
        for svg_ref in _extract_embed_svgs(aufgabe.text):
            if svg_ref not in loesung.text:
                errors.append(
                    f"{loesung_path.relative_to(ROOT)}: Aufgabe {nummer} referenziert Diagramm nicht: {svg_ref}"
                )

    return errors


def find_pairs() -> list[tuple[Path, Path]]:
    pairs: list[tuple[Path, Path]] = []
    for aufgaben_path in sorted(PRUEFUNGEN_DIR.glob("Klausur_AuD_Musteraufgaben_Version*.md")):
        version = aufgaben_path.stem.replace("Klausur_AuD_Musteraufgaben_", "")
        loesung_path = PRUEFUNGEN_DIR / f"Klausur_AuD_Musterloesungen_{version}.md"
        if loesung_path.exists():
            pairs.append((aufgaben_path, loesung_path))
    return pairs


def main() -> int:
    all_errors: list[str] = []
    pairs = find_pairs()

    if not pairs:
        print("⚠️ Keine Aufgaben/Loesungs-Paare gefunden.")
        return 0

    for aufgaben_path, loesung_path in pairs:
        all_errors.extend(check_pair(aufgaben_path, loesung_path))

    if all_errors:
        print("❌ Aufgaben/Loesungs-Sync fehlgeschlagen:")
        for err in all_errors:
            print(f"- {err}")
        return 1

    print("✅ Aufgaben/Loesungs-Sync ist konsistent.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
