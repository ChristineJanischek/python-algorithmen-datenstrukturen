#!/usr/bin/env python3
"""
CLI-Tool: DOCX Markdown Optimizer

Befehl zum Optimieren von Markdown-Dokumenten für DOCX-Export.

Beispiele:
    # Alle Prüfungsdokumente optimieren (Standard)
    python scripts/optimize_docx.py
    
    # Mit vollständiger Ausgabe
    python scripts/optimize_docx.py --verbose
    
    # Spezifisches Verzeichnis
    python scripts/optimize_docx.py --dir /path/to/docs
    
    # Mit Konfigurationsdatei
    python scripts/optimize_docx.py --config config/docx.json

Autor: python-algorithmen-datenstrukturen
Version: 1.0
"""

import sys
import json
import argparse
from pathlib import Path
from typing import Optional

# Füge src zum Python-Pfad hinzu für Importe
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.utils.docx_markdown_optimizer import (
    DocxOptimizer,
    DocxMetadata,
    optimize_pruefungen_directory,
)


def load_config(config_file: Path) -> Optional[dict]:
    """Lädt DOCX-Konfiguration aus JSON-Datei."""
    try:
        with open(config_file) as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"⚠️  Konfigurationsdatei nicht gefunden: {config_file}")
        return None
    except json.JSONDecodeError as e:
        print(f"❌ Fehler beim Parsen der Konfiguation: {e}")
        return None


def main():
    """Haupteinstiegspunkt für CLI-Tool."""
    
    parser = argparse.ArgumentParser(
        description="Optimiert Markdown-Dokumente für DOCX-Export",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Beispiele:
  %(prog)s                           # Alle Prüfungsdokumente optimieren
  %(prog)s --verbose                 # Mit ausführlicher Ausgabe
  %(prog)s --dir docs/aufgaben       # Spezifisches Verzeichnis
  %(prog)s --config config/docx.json # Mit Konfigurationsdatei
        """
    )
    
    parser.add_argument(
        "--dir",
        type=Path,
        default=None,
        help="Zielverzeichnis (default: docs/pruefungen)"
    )
    
    parser.add_argument(
        "--config",
        type=Path,
        default=None,
        help="Pfad zur Konfigurationsdatei (JSON)"
    )
    
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Ausführliche Ausgabe"
    )
    
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Keine Änderungen durchführen, nur anzeigen"
    )
    
    args = parser.parse_args()
    
    # Konfiguration laden
    metadata = DocxMetadata(verbose=args.verbose)
    
    if args.config:
        config_dict = load_config(args.config)
        if config_dict:
            metadata = DocxMetadata.from_dict(config_dict)
            metadata.verbose = args.verbose
    
    print("=" * 70)
    print("🔧 DOCX Markdown Optimizer")
    print("=" * 70)
    print(f"📁 Verzeichnis: {args.dir or 'docs/pruefungen (default)'}")
    print(f"⚙️  Verbose: {args.verbose}")
    print(f"🎭 Dry-Run: {args.dry_run}")
    print("=" * 70)
    
    # Für Dry-Run: Nur Metadaten anzeigen ohne zu schreiben
    if args.dry_run:
        print("\n⚠️  DRY-RUN MODE - Keine Änderungen werden durchgeführt\n")
    
    # Optimierung durchführen
    if args.dir:
        # Spezifisches Verzeichnis
        if not args.dir.exists():
            print(f"❌ Verzeichnis nicht gefunden: {args.dir}")
            return 1
        
        optimizer = DocxOptimizer(metadata)
        results = optimizer.optimize_directory(args.dir)
    else:
        # Standard: Prüfungsdokumente
        result_dict = optimize_pruefungen_directory(metadata=metadata, verbose=args.verbose)
        results = result_dict["results"]
    
    # Ergebnisse ausgeben
    print("\n📋 Verarbeitete Dateien:\n")
    
    successful_count = 0
    changed_count = 0
    
    for result in results:
        status = "✅" if result.success else "❌"
        rel_path = result.file_path.relative_to(Path.cwd())
        
        if result.success:
            successful_count += 1
            if result.changes_count > 0:
                changed_count += 1
                print(f"{status} {rel_path}")
                print(f"   → {result.message}")
            else:
                if args.verbose:
                    print(f"{status} {rel_path}")
                    print(f"   → {result.message}")
        else:
            print(f"{status} {rel_path}")
            print(f"   → {result.message}")
    
    # Zusammenfassung
    print("\n" + "=" * 70)
    print("📊 ZUSAMMENFASSUNG")
    print("=" * 70)
    print(f"Gesamt verarbeitet: {successful_count} Dateien")
    print(f"Mit Änderungen: {changed_count} Dateien")
    
    if args.dir:
        total_changes = sum(r.changes_count for r in results if r.success)
    else:
        total_changes = result_dict["summary"]["total_optimizations"]
    
    print(f"Gesamt Optimierungen: {total_changes}")
    print("=" * 70)
    
    if args.dry_run:
        print("\n✅ Dry-Run abgeschlossen (keine Änderungen durchgeführt)")
    elif changed_count > 0:
        print(f"\n✅ {changed_count} Dateien optimiert!")
    else:
        print("\n ℹ️  Alle Dateien sind bereits optimiert.")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
