#!/usr/bin/env python3
"""
Struktogramm CLI Tool - Kommandozeilen-Tool für Struktogramm-Verwaltung

Dieses Tool provides Funktionen zur Validierung und Refactoring von Struktogrammen
nach der Baden-Württemberg Operatorenliste direkt aus der Kommandozeile.

Usage:
    python struktogramm_cli.py validate <file>
    python struktogramm_cli.py refactor <file> [--dry-run] [--in-place]
    python struktogramm_cli.py check-repo [--pattern "*.md"]
    python struktogramm_cli.py operators [--list]

Author: GitHub Copilot
Version: 1.0
"""

import sys
import argparse
import os
from pathlib import Path
from typing import List, Optional
from colorama import Fore, Back, Style, init

from struktogramm_validator import (
    StruktogrammValidator,
    StruktogrammAnalyzer,
    ValidationLevel,
    validate_file,
    create_validation_report
)
from struktogramm_refactorer import (
    StruktogrammRefactorer,
    create_refactoring_report,
    apply_refactoring_batch
)


# Farben initialisieren (für Windows-Kompatibilität)
init(autoreset=True)


class StruktogrammCLI:
    """Kommandozeilen-Interface für Struktogramm-Tools"""

    def __init__(self, verbose: bool = False):
        """
        Initialisiert das CLI
        
        Args:
            verbose: Verbose-Modus aktivieren
        """
        self.verbose = verbose
        self.validator = StruktogrammValidator()
        self.analyzer = StruktogrammAnalyzer()
        self.refactorer = StruktogrammRefactorer()

    def print_header(self, text: str):
        """Druckt Kopfzeile"""
        print(f"\n{Fore.CYAN}{'='*60}")
        print(f"{text}")
        print(f"{'='*60}{Style.RESET_ALL}\n")

    def print_success(self, text: str):
        """Druckt Erfolgsmeldung"""
        print(f"{Fore.GREEN}✅ {text}{Style.RESET_ALL}")

    def print_error(self, text: str):
        """Druckt Fehlermeldung"""
        print(f"{Fore.RED}❌ {text}{Style.RESET_ALL}")

    def print_warning(self, text: str):
        """Druckt Warnung"""
        print(f"{Fore.YELLOW}⚠️  {text}{Style.RESET_ALL}")

    def print_info(self, text: str):
        """Druckt Information"""
        print(f"{Fore.BLUE}ℹ️  {text}{Style.RESET_ALL}")

    def cmd_validate(self, filepath: str):
        """
        Validiert eine Struktogramm-Datei
        
        Args:
            filepath: Pfad zur Datei
        """
        self.print_header(f"Validiere: {filepath}")

        if not os.path.exists(filepath):
            self.print_error(f"Datei nicht gefunden: {filepath}")
            return

        is_valid, results = validate_file(filepath)

        if not results:
            self.print_success("Keine Fehler oder Warnungen gefunden!")
            return

        # Sortiere Ergebnisse nach Severity
        errors = [r for r in results if r.level == ValidationLevel.ERROR]
        warnings = [r for r in results if r.level == ValidationLevel.WARNING]

        if errors:
            self.print_error(f"{len(errors)} Fehler gefunden:")
            for error in errors:
                print(f"  {error}")

        if warnings:
            self.print_warning(f"{len(warnings)} Warnungen gefunden:")
            for warning in warnings:
                print(f"  {warning}")
                if warning.suggested_fix:
                    self.print_info(f"Vorschlag: {warning.suggested_fix}")

        # Zusammenfassung
        print(f"\n{Fore.CYAN}Zusammenfassung:{Style.RESET_ALL}")
        print(f"  Fehler: {len(errors)}")
        print(f"  Warnungen: {len(warnings)}")
        print(f"  Status: {'✅ BESTANDEN' if is_valid else '❌ NICHT BESTANDEN'}")

    def cmd_refactor(self, filepath: str, dry_run: bool = True, in_place: bool = False):
        """
        Refaktoriert eine Struktogramm-Datei
        
        Args:
            filepath: Pfad zur Datei
            dry_run: Nur Vorschau zeigen
            in_place: Datei direkt überschreiben
        """
        self.print_header(f"Refactore: {filepath}")

        if not os.path.exists(filepath):
            self.print_error(f"Datei nicht gefunden: {filepath}")
            return

        try:
            refactored_content, changes = self.refactorer.refactor_file(
                filepath, 
                in_place=in_place and not dry_run
            )

            if not changes:
                self.print_success("Keine Änderungen notwendig!")
                return

            # Zeige Änderungen
            print(create_refactoring_report(changes))

            # Statistiken
            stats = self.refactorer.get_stats()
            print(f"\n{Fore.CYAN}Statistiken:{Style.RESET_ALL}")
            print(f"  Insgesamt: {stats['total_changes']} Änderungen")
            print(f"  🎯 Hohe Genauigkeit (≥80%): {stats['high_confidence']}")
            print(f"  🟡 Mittlere Genauigkeit (50-80%): {stats['medium_confidence']}")
            print(f"  🔴 Niedrige Genauigkeit (<50%): {stats['low_confidence']}")

            if dry_run:
                self.print_info("Dry-Run Modus - Datei wurde nicht verändert")
                self.print_info("Verwende --in-place um Änderungen zu speichern")
            elif in_place:
                self.print_success(f"Datei aktualisiert: {filepath}")

        except Exception as e:
            self.print_error(f"Fehler beim Refactoring: {str(e)}")

    def cmd_check_repo(self, pattern: str = "**/*.md", base_path: str = "."):
        """
        Prüft alle Struktogramme im Repository
        
        Args:
            pattern: Dateimuster (glob)
            base_path: Basis-Verzeichnis
        """
        self.print_header(f"Prüfe Repository: {base_path}")

        found_files = list(Path(base_path).glob(pattern))
        if not found_files:
            self.print_warning(f"Keine Dateien gefunden mit Pattern: {pattern}")
            return

        self.print_info(f"Gefunden: {len(found_files)} Dateien")

        total_errors = 0
        total_warnings = 0
        problematic_files = []

        for filepath in found_files:
            is_valid, results = validate_file(str(filepath))
            
            errors = [r for r in results if r.level == ValidationLevel.ERROR]
            warnings = [r for r in results if r.level == ValidationLevel.WARNING]

            if errors or warnings:
                problematic_files.append((str(filepath), len(errors), len(warnings)))
                total_errors += len(errors)
                total_warnings += len(warnings)

        if not problematic_files:
            self.print_success(f"Alle {len(found_files)} Dateien sind konform!")
            return

        self.print_warning(f"{len(problematic_files)} Dateien haben Probleme:")
        for filepath, errors, warnings in problematic_files:
            rel_path = os.path.relpath(filepath, base_path)
            print(f"  {rel_path}: {errors} Fehler, {warnings} Warnungen")

        print(f"\n{Fore.CYAN}Zusammenfassung:{Style.RESET_ALL}")
        print(f"  Geprüfte Dateien: {len(found_files)}")
        print(f"  Fehler gesamt: {total_errors}")
        print(f"  Warnungen gesamt: {total_warnings}")

    def cmd_operators(self, list_all: bool = False):
        """
        Zeigt verfügbare Operatoren
        
        Args:
            list_all: Alle Operatoren anzeigen
        """
        self.print_header("Verfügbare Operatoren (BW-Standard)")

        operators = self.validator.get_operator_examples()

        # Gruppiere nach Kategorie
        categories = {
            "Variablen": ["deklaration", "initialisierung", "deklaration_und_initialisierung", "zuweisung"],
            "Ein-/Ausgabe": ["einlesen", "ausgabe", "rueckgabe"],
            "Funktionen": ["aufruf"],
            "Kontrollstrukturen": ["wenn", "sonst", "wiederhole_solange", "zaehle"],
            "Arrays": ["array_anzahl"],
        }

        for category, ops in categories.items():
            print(f"\n{Fore.CYAN}{category}:{Style.RESET_ALL}")
            for op_name in ops:
                if op_name in operators:
                    print(f"  • {operators[op_name]}")

    def cmd_analyze(self, filepath: str):
        """
        Analysiert ein Struktogramm
        
        Args:
            filepath: Pfad zur Datei
        """
        self.print_header(f"Analysiere: {filepath}")

        if not os.path.exists(filepath):
            self.print_error(f"Datei nicht gefunden: {filepath}")
            return

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            # Extrahiere Operatoren
            operators = self.analyzer.extract_operators(content)
            
            # Berechne Komplexität
            complexity = self.analyzer.get_complexity_analysis(content)

            print(f"{Fore.CYAN}Operatoren:{Style.RESET_ALL}")
            if operators:
                for op in operators:
                    print(f"  • {op['operator']}: {op['content']}")
            else:
                print("  Keine Operatoren gefunden")

            print(f"\n{Fore.CYAN}Komplexitätsmetriken:{Style.RESET_ALL}")
            print(f"  Zeilen: {complexity['lines']}")
            print(f"  Variablen: {complexity['variables']}")
            print(f"  Bedingungen: {complexity['conditions']}")
            print(f"  Schleifen: {complexity['loops']}")
            print(f"  Arrays: {complexity['arrays']}")

        except Exception as e:
            self.print_error(f"Fehler bei Analyse: {str(e)}")


def main():
    """Hauptfunktion"""
    parser = argparse.ArgumentParser(
        description="Struktogramm-Tool für Baden-Württemberg Abitur-Standards",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Beispiele:
  %(prog)s validate docs/pruefungen/Klausur_L2_2_1_Verfuegung.md
  %(prog)s refactor docs/pruefungen/Klausur_L2_2_1_Verfuegung.md --dry-run
  %(prog)s check-repo --pattern "**/*.md"
  %(prog)s operators --list
  %(prog)s analyze docs/pruefungen/Klausur_L2_2_1_Verfuegung.md

Dokumentation: https://github.com/ChristineJanischek/python-algorithmen-datenstrukturen
        """
    )

    # Globale Optionen
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose-Modus")

    # Subcommands
    subparsers = parser.add_subparsers(dest="command", help="Verfügbare Kommandos")

    # validate
    validate_parser = subparsers.add_parser("validate", help="Validiere eine Datei")
    validate_parser.add_argument("file", help="Datei zum Validieren")

    # refactor
    refactor_parser = subparsers.add_parser("refactor", help="Refaktoriere eine Datei")
    refactor_parser.add_argument("file", help="Datei zum Refaktorieren")
    refactor_parser.add_argument("--dry-run", action="store_true", help="Nur Vorschau (Standard)")
    refactor_parser.add_argument("--in-place", action="store_true", help="Datei direkt überschreiben")

    # check-repo
    check_parser = subparsers.add_parser("check-repo", help="Prüfe ganzes Repository")
    check_parser.add_argument("--pattern", default="**/*.md", help="Dateimuster (glob)")
    check_parser.add_argument("--base-path", default=".", help="Basis-Verzeichnis")

    # operators
    operators_parser = subparsers.add_parser("operators", help="Zeige Operatoren")
    operators_parser.add_argument("--list", action="store_true", help="Liste anzeigen")

    # analyze
    analyze_parser = subparsers.add_parser("analyze", help="Analysiere ein Struktogramm")
    analyze_parser.add_argument("file", help="Datei zum Analysieren")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    # Erstelle CLI-Instance
    cli = StruktogrammCLI(verbose=args.verbose)

    # Dispatch zu Command-Handler
    if args.command == "validate":
        cli.cmd_validate(args.file)
    elif args.command == "refactor":
        cli.cmd_refactor(args.file, dry_run=not args.in_place, in_place=args.in_place)
    elif args.command == "check-repo":
        cli.cmd_check_repo(args.pattern, args.base_path)
    elif args.command == "operators":
        cli.cmd_operators(args.list)
    elif args.command == "analyze":
        cli.cmd_analyze(args.file)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}Abgebrochen durch Benutzer{Style.RESET_ALL}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Fore.RED}Fehler: {str(e)}{Style.RESET_ALL}")
        sys.exit(1)
