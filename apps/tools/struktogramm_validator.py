"""
Struktogramm Validator - Validiert Struktogramme gegen die Baden-Württemberg Operatorenliste

Dieses Modul provides Funktionen zur automatischen Validierung von Struktogrammen
gegen die Operatorenliste (struktogramme/Operatorenliste-Struktogramme.md).

Author: GitHub Copilot
Version: 1.0
"""

import re
import sys
from pathlib import Path
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
from enum import Enum

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from src.utils.bw_branch_validation import validate_bw_branch_structure


class ValidationLevel(Enum):
    """Validierungsstufen"""
    ERROR = "error"  # Kritischer Fehler
    WARNING = "warning"  # Warnung
    INFO = "info"  # Information


@dataclass
class ValidationResult:
    """Ergebnis einer Validierungsprüfung"""
    level: ValidationLevel
    line: int
    column: int
    message: str
    code: str
    suggested_fix: Optional[str] = None

    def __str__(self) -> str:
        return f"[{self.level.value.upper()}] Zeile {self.line}: {self.message}"


class StruktogrammValidator:
    """Validator für Struktogramme nach BW-Standard"""

    # Operatoren nach Operatorenliste
    OPERATORS = {
        # Variablen
        "deklaration": {
            "pattern": r"Deklaration:\s*(\w+)\s*\|?als\s*(\w+)\|?",
            "example": "Deklaration: variable als datentyp"
        },
        "initialisierung": {
            "pattern": r"Initialisierung:\s*(\w+)\s*=\s*(.+)",
            "example": "Initialisierung: variable = wert"
        },
        "deklaration_und_initialisierung": {
            "pattern": r"Deklaration und Initialisierung:\s*(\w+)\s*\|?als\s*(\w+)\|?\s*=\s*(.+)",
            "example": "Deklaration und Initialisierung: variable als datentyp = wert"
        },
        "zuweisung": {
            "pattern": r"Zuweisung:\s*(.+?)\s*=\s*(.+)",
            "example": "Zuweisung: element = wert"
        },
        
        # Ein-/Ausgabe
        "einlesen": {
            "pattern": r"Einlesen:\s*(\w+)\s*\|?als\s*(\w+)\|?",
            "example": "Einlesen: variable als datentyp"
        },
        "ausgabe": {
            "pattern": r"Ausgabe:\s*(.+)",
            "example": "Ausgabe: inhalt"
        },
        "rueckgabe": {
            "pattern": r"Rückgabe:\s*(.+)",
            "example": "Rückgabe: wert"
        },
        
        # Funktionen
        "aufruf": {
            "pattern": r"Aufruf:\s*(\w+)\s*\(([^)]*)\)",
            "example": "Aufruf: methode(parameter)"
        },
        
        # Kontrollstrukturen
        "wenn": {
            "pattern": r"Wenn\s+(.+?),\s*dann",
            "example": "Wenn bedingung, dann"
        },
        "sonst": {
            "pattern": r",\s*sonst",
            "example": ", sonst"
        },
        "wiederhole_solange": {
            "pattern": r"Wiederhole\s+solange\s+(.+)",
            "example": "Wiederhole solange bedingung"
        },
        "zaehle": {
            "pattern": r"Zähle\s+(\w+)\s+von\s+(.+?)\s+bis\s+(.+?),\s*Schrittweite\s+(\d+)",
            "example": "Zähle variable von start bis ende, Schrittweite n"
        },
        
        # Arrays
        "array_anzahl": {
            "pattern": r"Anzahl\s+der\s+Elemente\s+des\s+Arrays\s+(\w+)",
            "example": "Anzahl der Elemente des Arrays array"
        },
    }

    # Häufige Fehler und ihre Korrektionen
    COMMON_MISTAKES = {
        "While": "Wiederhole solange",
        "For": "Zähle",
        "If": "Wenn",
        "Else": ", sonst",
        "Return": "Rückgabe",
        "Print": "Ausgabe",
        "Input": "Einlesen",
    }

    def __init__(self, operator_list_path: Optional[str] = None):
        """
        Initialisiert den Validator
        
        Args:
            operator_list_path: Pfad zur Operatorenliste (optional)
        """
        self.operator_list_path = operator_list_path

    def validate_line(self, line: str, line_number: int) -> List[ValidationResult]:
        """
        Validiert eine einzelne Zeile
        
        Args:
            line: Die zu validierende Zeile
            line_number: Zeilennummer (1-basiert)
            
        Returns:
            Liste von ValidationResult
        """
        results: List[ValidationResult] = []
        line = line.strip()
        
        if not line or line.startswith("#"):
            return results

        # Prüfe auf häufige Fehler (Englische Keywords)
        for english, german in self.COMMON_MISTAKES.items():
            if english in line and line.startswith(english):
                results.append(ValidationResult(
                    level=ValidationLevel.WARNING,
                    line=line_number,
                    column=1,
                    message=f"Englischer Operator '{english}' erkannt. Verwende stattdessen: '{german}'",
                    code="BW_OPERATOR_ENGLISH",
                    suggested_fix=german
                ))

        # Prüfe ob mindestens ein bekannter Operator erkannt wird (sofern keine Kommentarzeile)
        if not any(op_name in line for op_name in ["Deklaration", "Initialisierung", "Zuweisung", 
                                                      "Einlesen", "Ausgabe", "Wenn", "Wiederhole", 
                                                      "Zähle", "Aufruf", "Rückgabe", "Anzahl"]):
            # Könnte ein unbekannter Operator oder einfach nur Text sein
            pass

        return results

    def validate_document(self, content: str) -> List[ValidationResult]:
        """
        Validiert ein gesamtes Dokument
        
        Args:
            content: Der zu validierende Dokumentinhalt
            
        Returns:
            Liste von ValidationResult
        """
        results: List[ValidationResult] = []
        lines = content.split('\n')
        
        for line_num, line in enumerate(lines, start=1):
            line_results = self.validate_line(line, line_num)
            results.extend(line_results)

        # Strikte Strukturprüfung für BW-Verzweigungen ergänzen.
        for issue in validate_bw_branch_structure(lines):
            results.append(ValidationResult(
                level=ValidationLevel.ERROR,
                line=issue.line,
                column=1,
                message=issue.message,
                code=issue.code,
                suggested_fix=issue.suggested_fix,
            ))

        return results

    def check_notation_consistency(self, text: str) -> List[Tuple[str, List[str]]]:
        """
        Prüft die Konsistenz der Operatorenlisten-Notation
        
        Args:
            text: Der zu analysierende Text
            
        Returns:
            Liste von (Operator, Matches) Tupeln
        """
        findings: List[Tuple[str, List[str]]] = []
        
        for op_name, op_data in self.OPERATORS.items():
            pattern = op_data["pattern"]
            matches = re.findall(pattern, text, re.IGNORECASE)
            if matches:
                findings.append((op_name, matches))

        return findings

    def suggest_fixes(self, results: List[ValidationResult]) -> Dict[str, str]:
        """
        Generiert Verbesserungsvorschläge
        
        Args:
            results: Validierungsergebnisse
            
        Returns:
            Dictionary mit Vorschlägen
        """
        suggestions: Dict[str, str] = {}
        
        for result in results:
            if result.suggested_fix:
                suggestions[result.code] = result.suggested_fix

        return suggestions

    def get_operator_examples(self) -> Dict[str, str]:
        """
        Gibt Beispiele aller Operatoren
        
        Returns:
            Dictionary mit Operatoren und Beispielen
        """
        return {name: data["example"] for name, data in self.OPERATORS.items()}


class StruktogrammAnalyzer:
    """Analysiert Struktogramme und extrahiert Struktur"""

    def __init__(self):
        self.validator = StruktogrammValidator()

    def extract_operators(self, text: str) -> List[Dict[str, any]]:
        """
        Extrahiert alle Operatoren aus einem Text
        
        Args:
            text: Der zu analysierende Text
            
        Returns:
            Liste mit extrahierten Operatoren
        """
        operators: List[Dict[str, any]] = []
        findings = self.validator.check_notation_consistency(text)
        
        for op_name, matches in findings:
            for match in matches:
                operators.append({
                    "operator": op_name,
                    "content": match if isinstance(match, str) else match[0]
                })

        return operators

    def get_complexity_analysis(self, text: str) -> Dict[str, int]:
        """
        Analysiert die Komplexität eines Struktogramms
        
        Args:
            text: Der zu analysierende Text
            
        Returns:
            Komplexitätsmetriken
        """
        metrics = {
            "lines": len(text.split('\n')),
            "variables": len(re.findall(r"Deklaration", text)),
            "conditions": len(re.findall(r"Wenn", text)),
            "loops": len(re.findall(r"(Wiederhole|Zähle)", text)),
            "arrays": len(re.findall(r"Array", text)),
        }
        return metrics


# Hilffunktionen
def validate_file(filepath: str) -> Tuple[bool, List[ValidationResult]]:
    """
    Validiert eine Datei
    
    Args:
        filepath: Pfad zur Datei
        
    Returns:
        Tupel (is_valid, results)
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        validator = StruktogrammValidator()
        results = validator.validate_document(content)
        
        is_valid = all(r.level != ValidationLevel.ERROR for r in results)
        return is_valid, results
    except Exception as e:
        return False, [ValidationResult(
            level=ValidationLevel.ERROR,
            line=0,
            column=0,
            message=f"Fehler beim Lesen der Datei: {str(e)}",
            code="FILE_READ_ERROR"
        )]


def create_validation_report(results: List[ValidationResult]) -> str:
    """
    Erstellt einen Validierungsbericht
    
    Args:
        results: Validierungsergebnisse
        
    Returns:
        Formatierter Bericht
    """
    if not results:
        return "✅ Keine Fehler oder Warnungen gefunden!"

    errors = [r for r in results if r.level == ValidationLevel.ERROR]
    warnings = [r for r in results if r.level == ValidationLevel.WARNING]

    report = f"""
📊 Validierungsbericht
{'='*60}

❌ Fehler: {len(errors)}
⚠️  Warnungen: {len(warnings)}

"""

    if errors:
        report += "FEHLER:\n"
        for error in errors:
            report += f"  - {error}\n"
        report += "\n"

    if warnings:
        report += "WARNUNGEN:\n"
        for warning in warnings:
            report += f"  - {warning}\n"
            if warning.suggested_fix:
                report += f"    💡 Vorschlag: {warning.suggested_fix}\n"

    return report
