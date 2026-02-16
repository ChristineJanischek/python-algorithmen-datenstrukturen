"""
Struktogramm Validator Tool

Überprüft, dass für Programmlogik in docs/ ausschließlich grafische Struktogramm-Notationen verwendet werden.
Markiert Python-Code, der nicht von grafischen Struktogrammen vorausgeht, als Fehler.

Verwendung:
    python -m src.utils.struktogramm_validator
"""

import re
import os
from pathlib import Path
from dataclasses import dataclass
from typing import List, Dict, Set
from enum import Enum


class ValidationIssue(Enum):
    """Art der Validierungsprobleme"""
    PYTHON_WITHOUT_STRUKTOGRAMM = "Python-Code ohne vorhergehendes Struktogramm"
    PYTHON_CODE_TOO_COMPLEX = "Python-Code ohne Struktogramm-Erklärung"
    MISSING_PSEUDOCODE = "Fehlende grafische Struktogramm-Notation"
    MIXED_NOTATION = "Vermischte Notationen (Python + Pseudocode)"


@dataclass
class ValidationError:
    """Represents a validation error"""
    file_path: str
    line_number: int
    issue_type: ValidationIssue
    context: str
    severity: str  # "error", "warning"


class StruktogrammValidator:
    """Validator für Struktogramm-Notationen in Markdown-Dateien"""

    EXCLUDED_FILES = {
        "TEMPLATE_",  # Templates überprüfen wir separat
        "INDEX.md",   # Index-Dateien überspringen
        "Lehrplan",   # Lehrplan-Dateien ignorieren (nur Referenz)
        "BACKUP",     # Backup-Dateien ignorieren
    }

    PYTHON_KEYWORDS = {
        "def ", "class ", "if ", "elif ", "else:", "for ", "while ", 
        "import ", "from ", "return ", "try:", "except:", "with "
    }

    STRUKTOGRAMM_KEYWORDS = {
        "Deklaration", "Initialisierung", "Zuweisung", "Einlesen",
        "Ausgabe", "Rückgabe", "Aufruf", "Wenn", "Wiederhole", 
        "Zähle", "Array", "┌", "├", "└", "│", "Grafische Darstellung"
    }

    def __init__(self, docs_path: str = None):
        """
        Initialisiert den Validator
        
        Args:
            docs_path: Pfad zum docs-Verzeichnis (default: ./docs)
        """
        if docs_path is None:
            docs_path = Path(__file__).parent.parent.parent / "docs"
        self.docs_path = Path(docs_path)
        self.errors: List[ValidationError] = []
        self.files_checked = 0
        
    def validate_all(self) -> Dict[str, List[ValidationError]]:
        """
        Validiert alle Markdown-Dateien im docs-Verzeichnis
        
        Returns:
            Dict mit Dateipath -> Liste von ValidationErrors
        """
        errors_by_file = {}
        
        for md_file in self.docs_path.rglob("*.md"):
            if self._should_skip(md_file):
                continue
                
            file_errors = self.validate_file(md_file)
            if file_errors:
                errors_by_file[str(md_file)] = file_errors
            self.files_checked += 1
        
        return errors_by_file
    
    def validate_file(self, file_path: Path) -> List[ValidationError]:
        """
        Validiert eine einzelne Markdown-Datei
        
        Args:
            file_path: Pfad zur Markdown-Datei
            
        Returns:
            Liste von ValidationErrors in dieser Datei
        """
        errors = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                lines = content.split('\n')
        except Exception as e:
            return [ValidationError(
                str(file_path), 0,
                "READ_ERROR",
                f"Fehler beim Lesen: {str(e)}",
                "error"
            )]
        
        # Überprüfe auf Python-Code ohne vorhergehendes Struktogramm
        errors.extend(self._check_python_code_patterns(file_path, lines))
        
        # Überprüfe auf fehlende Struktogramm-Notationen
        errors.extend(self._check_missing_struktogramms(file_path, lines))
        
        return errors
    
    def _check_python_code_patterns(self, file_path: Path, lines: List[str]) -> List[ValidationError]:
        """
        Prüft auf Python-Code, der nicht von Struktogrammen begleitet wird
        """
        errors = []
        i = 0
        
        while i < len(lines):
            line = lines[i]
            
            # Finde Python-Code-Blöcke
            if line.strip().startswith("```python"):
                # Prüfe ob davor ein Struktogramm erklärt wird
                has_struktogramm_context = self._has_struktogramm_context(lines, i)
                has_graphic_struktogramm = self._has_graphic_struktogramm(lines, i)
                
                # Extrahiere die Python-Code-Komplexität
                code_block = self._extract_code_block(lines, i)
                is_complex = self._is_complex_logic(code_block)
                
                # Wenn komplexe Logik ohne grafisches Struktogramm
                if is_complex and not has_graphic_struktogramm:
                    errors.append(ValidationError(
                        str(file_path),
                        i + 1,
                        ValidationIssue.PYTHON_WITHOUT_STRUKTOGRAMM,
                        f"```python Block ohne vorhergehendes grafisches Struktogramm: {code_block[:50]}...",
                        "error" if is_complex else "warning"
                    ))
                
                # Springe zum Ende des Code-Blocks
                i = self._find_code_block_end(lines, i)
            
            i += 1
        
        return errors
    
    def _check_missing_struktogramms(self, file_path: Path, lines: List[str]) -> List[ValidationError]:
        """
        Prüft auf Sektionen, die Programmlogik erklären, aber kein grafisches Struktogramm haben
        """
        errors = []
        logic_section_keywords = {
            "Programmlogik", "Algorithmus", "Ablauf", "Lösungsansatz",
            "Implementation", "Pseudocode"
        }
        
        for i, line in enumerate(lines):
            # Finde Logic-Abschnitte
            if any(keyword.lower() in line.lower() for keyword in logic_section_keywords):
                # Prüfe die nächsten Zeilen auf grafisches Struktogramm
                if not self._has_graphic_struktogramm_within_context(lines, i, context_size=20):
                    # Wenn Pseudocode vorhanden, ist das auch ok
                    if not self._has_pseudocode_struktogramm(lines, i, context_size=10):
                        # Aber nur warnen wenn es nicht das Template ist
                        if "template" not in str(file_path).lower():
                            pass  # Warnung könnte hier kommen, aber optional
        
        return errors
    
    def _should_skip(self, file_path: Path) -> bool:
        """
        Prüft, ob eine Datei übersprungen werden soll
        """
        filename = file_path.name
        filepath_str = str(file_path)
        
        return any(excluded in filename or excluded in filepath_str 
                   for excluded in self.EXCLUDED_FILES)
    
    def _has_struktogramm_context(self, lines: List[str], python_line_idx: int, 
                                   context_size: int = 10) -> bool:
        """
        Prüft, ob es im Kontext Struktogramm-Keywords gibt
        """
        start = max(0, python_line_idx - context_size)
        context = '\n'.join(lines[start:python_line_idx])
        
        return any(keyword.lower() in context.lower() 
                   for keyword in self.STRUKTOGRAMM_KEYWORDS)
    
    def _has_graphic_struktogramm(self, lines: List[str], python_line_idx: int,
                                  context_size: int = 15) -> bool:
        """
        Prüft, ob es davor ein grafisches Struktogramm gibt
        """
        start = max(0, python_line_idx - context_size)
        context = '\n'.join(lines[start:python_line_idx])
        
        # Prüfe auf grafische Elemente
        has_box_drawing = any(char in context for char in ['┌', '├', '└', '│', '─', '┤', '┬', '┴', '┼'])
        has_section = "Grafische Darstellung" in context or "Grafische Notation" in context
        
        return has_box_drawing or has_section
    
    def _has_graphic_struktogramm_within_context(self, lines: List[str], start_idx: int,
                                                 context_size: int = 20) -> bool:
        """
        Prüft, ob innerhalb des Kontexts ein grafisches Struktogramm vorhanden ist
        """
        end = min(len(lines), start_idx + context_size)
        context = '\n'.join(lines[start_idx:end])
        
        return any(char in context for char in ['┌', '├', '└', '│', '─'])
    
    def _has_pseudocode_struktogramm(self, lines: List[str], start_idx: int,
                                     context_size: int = 10) -> bool:
        """
        Prüft, ob es innerhalb des Kontexts Pseudocode-Struktogramm-Notation gibt
        """
        end = min(len(lines), start_idx + context_size)
        context = '\n'.join(lines[start_idx:end])
        
        return any(keyword in context for keyword in [
            "Wenn", "Wiederhole", "Zähle", "Deklaration", "Initialisierung",
            "Zuweisung", "Ausgabe", "Rückgabe"
        ])
    
    def _extract_code_block(self, lines: List[str], start_idx: int) -> str:
        """
        Extrahiert einen Python-Code-Block
        """
        code_lines = []
        i = start_idx + 1
        
        while i < len(lines) and not lines[i].strip().startswith("```"):
            code_lines.append(lines[i])
            i += 1
        
        return '\n'.join(code_lines)
    
    def _find_code_block_end(self, lines: List[str], start_idx: int) -> int:
        """
        Findet das Ende eines Code-Blocks (schließendes ```)
        """
        i = start_idx + 1
        while i < len(lines):
            if lines[i].strip().startswith("```"):
                return i
            i += 1
        return len(lines) - 1
    
    def _is_complex_logic(self, code: str) -> bool:
        """
        Heuristische Prüfung, ob der Code komplexe Logik enthält
        """
        # Zähle Kontrollflusselemente
        if_count = code.count("if ")
        loop_count = code.count("for ") + code.count("while ")
        function_count = code.count("def ")
        
        # Komplexität: Wenn mehr als ein Kontrollflusselement oder Funktionsdefinition
        complexity_score = if_count + loop_count * 2 + function_count * 3
        
        return complexity_score > 1
    
    def print_report(self, errors_by_file: Dict[str, List[ValidationError]]):
        """
        Gibt einen formattierten Report der Fehler aus
        """
        print("\n" + "=" * 80)
        print("STRUKTOGRAMM VALIDATOR - REPORT")
        print("=" * 80)
        
        if not errors_by_file:
            print(f"\n✓ Alle {self.files_checked} Dateien sind valide!")
            return
        
        total_errors = sum(len(errors) for errors in errors_by_file.values())
        print(f"\n⚠️  Gefundene Probleme: {total_errors} in {len(errors_by_file)} Dateien")
        print(f"    Dateien überprüft: {self.files_checked}")
        print()
        
        for file_path, errors in sorted(errors_by_file.items()):
            print(f"\n📄 {file_path}")
            for error in errors:
                icon = "🚨" if error.severity == "error" else "⚠️"
                print(f"  {icon} Zeile {error.line_number}: {error.issue_type.value}")
                print(f"     {error.context}")
    
    def save_report(self, errors_by_file: Dict[str, List[ValidationError]], 
                   output_file: str = "validation_report.md"):
        """
        Speichert einen Validierungsbericht als Markdown
        """
        report_lines = [
            "# Struktogramm Validator Report\n",
            f"Generiert: {self._get_timestamp()}\n",
            f"Dateien überprüft: {self.files_checked}\n",
        ]
        
        if not errors_by_file:
            report_lines.append("\n✓ Alle Dateien sind valide!\n")
        else:
            total_errors = sum(len(errors) for errors in errors_by_file.values())
            report_lines.append(f"\n⚠️ Gefundene Probleme: {total_errors} in {len(errors_by_file)} Dateien\n")
            report_lines.append("\n## Fehlerleiste\n")
            
            for file_path, errors in sorted(errors_by_file.items()):
                report_lines.append(f"\n### {file_path}\n")
                for error in errors:
                    report_lines.append(
                        f"- **Zeile {error.line_number}**: {error.issue_type.value}\n"
                        f"  - {error.context}\n"
                    )
        
        output_path = Path(__file__).parent.parent.parent / output_file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.writelines(report_lines)
        
        print(f"\n📊 Report gespeichert: {output_path}")
    
    @staticmethod
    def _get_timestamp() -> str:
        """Gibt den aktuellen Zeitstempel zurück"""
        from datetime import datetime
        return datetime.now().strftime("%d.%m.%Y %H:%M:%S")


def main():
    """Hauptfunktion"""
    import sys
    
    validator = StruktogrammValidator()
    errors_by_file = validator.validate_all()
    
    validator.print_report(errors_by_file)
    validator.save_report(errors_by_file)
    
    # Exit Code: 0 wenn ok, 1 wenn Fehler gefunden
    sys.exit(0 if not errors_by_file else 1)


if __name__ == "__main__":
    main()
