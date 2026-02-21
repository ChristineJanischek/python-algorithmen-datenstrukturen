#!/usr/bin/env python3
"""Prüft relative Markdown-Links in Dokumentationsverzeichnissen."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STANDARD_VERZEICHNISSE = [
    "docs/aufgaben",
    "docs/information",
    "docs/loesungen",
    "docs/handbuch",
]
LINK_REGEX = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


class LinkFund:
    """Repräsentiert einen defekten Linkfund."""

    def __init__(self, datei: Path, ziel: str, grund: str) -> None:
        self.datei = datei
        self.ziel = ziel
        self.grund = grund


def parse_args() -> argparse.Namespace:
    """Liest Kommandozeilenargumente ein.

    Returns:
        Geparste Argumente.
    """
    parser = argparse.ArgumentParser(
        description="Prüft relative Markdown-Links auf existierende Ziele.",
    )
    parser.add_argument(
        "--dirs",
        nargs="+",
        default=STANDARD_VERZEICHNISSE,
        help="Zu prüfende Verzeichnisse relativ zum Repository-Root.",
    )
    parser.add_argument(
        "--include-templates",
        action="store_true",
        help="Template-Dateien (TEMPLATE_*.md) ebenfalls prüfen.",
    )
    parser.add_argument(
        "--max-details",
        type=int,
        default=100,
        help="Maximale Anzahl ausgegebener Fehlerdetails.",
    )
    return parser.parse_args()


def ist_externer_link(ziel: str) -> bool:
    """Prüft, ob ein Link extern ist und ignoriert werden soll.

    Args:
        ziel: Linkziel aus Markdown.

    Returns:
        True, wenn der Link extern ist.
    """
    return ziel.startswith(("http://", "https://", "mailto:", "#"))


def sammle_markdown_dateien(verzeichnis: Path, include_templates: bool) -> list[Path]:
    """Sammelt Markdown-Dateien rekursiv in einem Verzeichnis.

    Args:
        verzeichnis: Basisverzeichnis.
        include_templates: Ob Template-Dateien einbezogen werden.

    Returns:
        Liste von Markdown-Dateien.
    """
    dateien = list(verzeichnis.rglob("*.md")) + list(verzeichnis.rglob("*.MD"))
    if include_templates:
        return sorted(dateien)
    return sorted(datei for datei in dateien if "TEMPLATE_" not in datei.name.upper())


def pruefe_datei(markdown_datei: Path) -> list[LinkFund]:
    """Prüft alle relativen Links in einer Markdown-Datei.

    Args:
        markdown_datei: Zu prüfende Datei.

    Returns:
        Liste gefundener Probleme.
    """
    inhalt = markdown_datei.read_text(encoding="utf-8", errors="ignore")
    fehler: list[LinkFund] = []

    for ziel_raw in LINK_REGEX.findall(inhalt):
        ziel = ziel_raw.strip()
        if not ziel or ist_externer_link(ziel):
            continue

        ziel_ohne_anchor = ziel.split("#", 1)[0].strip()
        if not ziel_ohne_anchor:
            continue

        aufgeloest = (markdown_datei.parent / ziel_ohne_anchor).resolve()

        try:
            aufgeloest.relative_to(ROOT.resolve())
        except ValueError:
            fehler.append(LinkFund(markdown_datei, ziel_raw, "outside-repo"))
            continue

        if not aufgeloest.exists():
            fehler.append(LinkFund(markdown_datei, ziel_raw, "missing"))

    return fehler


def main() -> int:
    """Führt den Link-Check aus.

    Returns:
        Exit-Code 0 bei Erfolg, sonst 1.
    """
    args = parse_args()

    gesamt_dateien = 0
    gesamt_fehler: list[LinkFund] = []

    for rel_pfad in args.dirs:
        basis = (ROOT / rel_pfad).resolve()
        if not basis.exists():
            print(f"⚠️  Verzeichnis nicht gefunden: {rel_pfad}")
            continue

        dateien = sammle_markdown_dateien(basis, args.include_templates)
        gesamt_dateien += len(dateien)

        for datei in dateien:
            gesamt_fehler.extend(pruefe_datei(datei))

    print(
        "📎 Markdown-Linkcheck: "
        f"Dateien={gesamt_dateien}, Fehler={len(gesamt_fehler)}, "
        f"Templates={'ja' if args.include_templates else 'nein'}"
    )

    if not gesamt_fehler:
        print("✅ Keine defekten relativen Markdown-Links gefunden.")
        return 0

    print("❌ Defekte Links gefunden:")
    for fund in gesamt_fehler[: max(0, args.max_details)]:
        rel = fund.datei.relative_to(ROOT).as_posix()
        print(f"- {rel} -> {fund.ziel} [{fund.grund}]")

    if len(gesamt_fehler) > args.max_details:
        rest = len(gesamt_fehler) - args.max_details
        print(f"… {rest} weitere Funde nicht angezeigt.")

    return 1


if __name__ == "__main__":
    sys.exit(main())
