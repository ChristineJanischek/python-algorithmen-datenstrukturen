#!/usr/bin/env python3
"""Prüft eine minimale Definition-of-Done für zentrale Projektdokumentation."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]

REQUIRED_FILES = [
    ROOT / "CHANGELOG.md",
    ROOT / "docs" / "handbuch" / "INDEX.md",
    ROOT / "docs" / "handbuch" / "ARCHITECTURE.MD",
    ROOT / "docs" / "handbuch" / "BACKUP_STRATEGY.md",
    ROOT / "docs" / "milestones" / "INDEX.md",
    ROOT / "docs" / "milestones" / "ENTWICKLUNGSSCHRITTE.MD",
]

HAND_BUCH_LINKS = [
    "ARCHITECTURE.MD",
    "BACKUP_STRATEGY.md",
    "ARCHITEKTUR_AUDIT_REPO_2026-02-21.MD",
]

MILESTONE_LINKS = [
    "ENTWICKLUNGSSCHRITTE.MD",
    "M0_STATUS_DASHBOARD_",
]


def _read_text(datei: Path) -> str:
    return datei.read_text(encoding="utf-8")


def pruefe_dateiexistenz() -> list[str]:
    """Prüft, ob alle verpflichtenden Kern-Dateien vorhanden sind.

    Returns:
        Liste mit Fehlermeldungen.
    """
    fehler: list[str] = []
    for datei in REQUIRED_FILES:
        if not datei.exists():
            fehler.append(f"Fehlende Pflichtdatei: {datei.relative_to(ROOT)}")

    dashboard_dateien = list((ROOT / "docs" / "milestones").glob("M0_STATUS_DASHBOARD_*.MD"))
    if not dashboard_dateien:
        fehler.append("Fehlende M0-Dashboard-Datei: docs/milestones/M0_STATUS_DASHBOARD_*.MD")

    return fehler


def pruefe_inhaltsanforderungen() -> list[str]:
    """Prüft zentrale Inhaltsanforderungen für Changelog und Indizes.

    Returns:
        Liste mit Fehlermeldungen.
    """
    fehler: list[str] = []

    changelog_text = _read_text(ROOT / "CHANGELOG.md")
    if "## [Unreleased]" not in changelog_text:
        fehler.append("CHANGELOG.md enthält keine Sektion '## [Unreleased]'.")
    if "### Nächste Schritte:" not in changelog_text:
        fehler.append("CHANGELOG.md enthält keine Sektion '### Nächste Schritte:'.")

    index_handbuch = _read_text(ROOT / "docs" / "handbuch" / "INDEX.md")
    for link in HAND_BUCH_LINKS:
        if link not in index_handbuch:
            fehler.append(f"docs/handbuch/INDEX.md verlinkt '{link}' nicht.")

    index_milestones = _read_text(ROOT / "docs" / "milestones" / "INDEX.md")
    for link in MILESTONE_LINKS:
        if link not in index_milestones:
            fehler.append(f"docs/milestones/INDEX.md enthält keinen Verweis auf '{link}'.")

    return fehler


def pruefe_platzhalter() -> list[str]:
    """Prüft auf offene Platzhalter in Kern-Dokumenten.

    Returns:
        Liste mit Fehlermeldungen.
    """
    fehler: list[str] = []
    muster = re.compile(r"\b(TODO|TBD|FIXME)\b", re.IGNORECASE)

    kern_dateien = [
        ROOT / "CHANGELOG.md",
        ROOT / "docs" / "handbuch" / "INDEX.md",
        ROOT / "docs" / "milestones" / "INDEX.md",
    ]

    for datei in kern_dateien:
        text = _read_text(datei)
        if muster.search(text):
            fehler.append(f"Offener Platzhalter in {datei.relative_to(ROOT)} gefunden (TODO/TBD/FIXME).")

    return fehler


def main() -> int:
    """Führt alle DoD-Prüfungen aus.

    Returns:
        Exit-Code: 0 bei Erfolg, 1 bei Fehlern.
    """
    fehler = []
    fehler.extend(pruefe_dateiexistenz())
    fehler.extend(pruefe_inhaltsanforderungen())
    fehler.extend(pruefe_platzhalter())

    if fehler:
        print("❌ Doku-DoD nicht erfüllt:")
        for eintrag in fehler:
            print(f"- {eintrag}")
        return 1

    print("✅ Doku-DoD erfüllt.")
    return 0


if __name__ == "__main__":
    sys.exit(main())