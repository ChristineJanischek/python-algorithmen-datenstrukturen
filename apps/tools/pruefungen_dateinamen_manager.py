#!/usr/bin/env python3
"""CLI für die Namenskonvention von Prüfungsdateien."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Prüft und normalisiert Prüfungsdateien auf das Schema Klausur_<Thema>_<Typ>_VersionX.md",
    )
    parser.add_argument(
        "--path",
        type=Path,
        default=Path("docs/pruefungen"),
        help="Zielpfad relativ zum Repository-Root (Standard: docs/pruefungen)",
    )
    parser.add_argument(
        "--fix",
        action="store_true",
        help="Nicht nur prüfen, sondern Dateien automatisch umbenennen",
    )
    return parser.parse_args()


def main() -> int:
    repo_root = _repo_root()
    if str(repo_root) not in sys.path:
        sys.path.insert(0, str(repo_root))

    from src.utils.pruefungen_namenskonvention import normalisiere_pruefungsdateien

    args = _parse_args()
    basis_pfad = (repo_root / args.path).resolve()
    if not basis_pfad.exists():
        print(f"❌ Pfad nicht gefunden: {basis_pfad}")
        return 2

    ergebnis = normalisiere_pruefungsdateien(basis_verzeichnis=basis_pfad, dry_run=not args.fix)

    print("\n📋 Prüfungs-Dateinamen-Check")
    print(f"Geprüft: {ergebnis.geprueft}")
    print(f"Bereits konform: {ergebnis.konform}")
    print(f"Umbenennungen notwendig: {len(ergebnis.umbenennungen)}")

    if ergebnis.umbenennungen:
        print("\nBetroffene Dateien:")
        for eintrag in ergebnis.umbenennungen:
            quelle = eintrag.quelle.relative_to(repo_root)
            ziel = eintrag.ziel.relative_to(repo_root)
            print(f"  - {quelle}  →  {ziel}")

    if args.fix:
        print("\n✅ Umbenennung abgeschlossen.")
        return 0

    if ergebnis.umbenennungen:
        print("\n❌ Es gibt nicht-konforme Dateinamen. Nutze --fix zur Korrektur.")
        return 1

    print("\n✅ Alle Dateinamen sind konform.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
