"""
Struktogramm Refactorer - Automatische Überarbeitung von Struktogrammen

Dieses Modul provides Funktionen zum automatischen Refactoring von Struktogrammen
in die korrekte Notation nach der Baden-Württemberg Operatorenliste.

Author: GitHub Copilot
Version: 1.0
"""

import re
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass


@dataclass
class RefactoringChange:
    """Dokumentiert eine Änderung während des Refactorings"""
    line: int
    original: str
    refactored: str
    reason: str
    confidence: float  # 0.0 - 1.0


class StruktogrammRefactorer:
    """Automatisches Refactoring von Struktogrammen"""

    # Mapping von häufigen falschen zu korrekten Notationen
    REFACTORING_RULES = [
        # Englische Keywords
        {
            "pattern": r"^\s*while\s+(.+):",
            "replacement": lambda m: f"Wiederhole solange {m.group(1)}",
            "reason": "While-Schleife zu Operatorenliste-Notation",
            "confidence": 0.95
        },
        {
            "pattern": r"^\s*for\s+(\w+)\s+in\s+range\s*\(\s*(\d+)\s*\):",
            "replacement": lambda m: f"Zähle {m.group(1)} von 0 bis {int(m.group(2))-1}, Schrittweite 1",
            "reason": "For-Schleife zu BW-Standard-Notation",
            "confidence": 0.9
        },
        {
            "pattern": r"^\s*if\s+(.+?)\s*:",
            "replacement": lambda m: f"Wenn {m.group(1)}, dann",
            "reason": "If-Statement zu Wenn-Operator",
            "confidence": 0.85
        },
        {
            "pattern": r"^\s*else\s*:",
            "replacement": lambda m: ", sonst",
            "reason": "Else zu Operatorenliste-Notation",
            "confidence": 0.9
        },
        {
            "pattern": r"^\s*return\s+(.+)",
            "replacement": lambda m: f"Rückgabe: {m.group(1)}",
            "reason": "Return zu Rückgabe-Operator",
            "confidence": 0.95
        },
        {
            "pattern": r"^\s*print\s*\(\s*(.+)\s*\)",
            "replacement": lambda m: f"Ausgabe: {m.group(1)}",
            "reason": "Print zu Ausgabe-Operator",
            "confidence": 0.9
        },
        {
            "pattern": r"^\s*input\s*\(\s*(.+?)\s*\)",
            "replacement": lambda m: f"Einlesen: variable",
            "reason": "Input zu Einlesen-Operator",
            "confidence": 0.7
        },
        
        # Deutsche aber falsche Schreibweisen
        {
            "pattern": r"Wiederhole\s+während\s+(.+)",
            "replacement": lambda m: f"Wiederhole solange {m.group(1)}",
            "reason": "Konsistente Notation für while-Schleife",
            "confidence": 0.95
        },
        {
            "pattern": r"Zähle\s+from\s+(.+)",
            "replacement": lambda m: f"Zähle {m.group(1)}",
            "reason": "Entfernen von englischem 'from'",
            "confidence": 0.8
        },

        # Korrektur von optionalen Parametern mit Bindestrichen
        {
            "pattern": r"Anzahl\s+der\s+Elemente\s+von\s+(\w+)",
            "replacement": lambda m: f"Anzahl der Elemente des Arrays {m.group(1)}",
            "reason": "Konsistente Notation für Array-Länge",
            "confidence": 0.9
        },

        # Normalisieren von Leerzeichen
        {
            "pattern": r"Zuweisung:\s{2,}(.+)",
            "replacement": lambda m: f"Zuweisung: {m.group(1)}",
            "reason": "Normalisierung: Extra Leerzeichen entfernt",
            "confidence": 1.0
        },
        {
            "pattern": r"Ausgabe:\s{2,}(.+)",
            "replacement": lambda m: f"Ausgabe: {m.group(1)}",
            "reason": "Normalisierung: Extra Leerzeichen entfernt",
            "confidence": 1.0
        },
    ]

    def __init__(self):
        self.changes: List[RefactoringChange] = []

    def refactor_line(self, line: str, line_number: int) -> Tuple[str, Optional[RefactoringChange]]:
        """
        Refaktoriert eine einzelne Zeile
        
        Args:
            line: Die zu refaktorierende Zeile
            line_number: Zeilennummer (1-basiert)
            
        Returns:
            Tupel (refactored_line, change_info)
        """
        original_line = line
        
        for rule in self.REFACTORING_RULES:
            pattern = rule["pattern"]
            replacement = rule["replacement"]
            
            match = re.match(pattern, line, re.IGNORECASE)
            if match:
                try:
                    new_line = replacement(match)
                    
                    # Bewahre führende Leerzeichen
                    leading_spaces = len(line) - len(line.lstrip())
                    new_line = ' ' * leading_spaces + new_line
                    
                    if new_line != original_line:
                        change = RefactoringChange(
                            line=line_number,
                            original=original_line.strip(),
                            refactored=new_line.strip(),
                            reason=rule["reason"],
                            confidence=rule["confidence"]
                        )
                        self.changes.append(change)
                        return new_line, change
                except Exception as e:
                    # Bei Fehler: Original behalten
                    pass

        return line, None

    def refactor_content(self, content: str) -> Tuple[str, List[RefactoringChange]]:
        """
        Refaktoriert einen gesamten Text
        
        Args:
            content: Der zu refaktorierende Text
            
        Returns:
            Tupel (refactored_content, changes)
        """
        self.changes = []
        lines = content.split('\n')
        refactored_lines = []

        for line_num, line in enumerate(lines, start=1):
            new_line, change = self.refactor_line(line, line_num)
            refactored_lines.append(new_line)

        refactored_content = '\n'.join(refactored_lines)
        return refactored_content, self.changes

    def refactor_file(self, filepath: str, in_place: bool = False) -> Tuple[str, List[RefactoringChange]]:
        """
        Refaktoriert eine Datei
        
        Args:
            filepath: Pfad zur Datei
            in_place: Wenn True, wird die Datei überschrieben
            
        Returns:
            Tupel (refactored_content, changes)
        """
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            refactored_content, changes = self.refactor_content(content)
            
            if in_place and changes:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(refactored_content)
            
            return refactored_content, changes
        except Exception as e:
            raise Exception(f"Fehler beim Refactoring der Datei {filepath}: {str(e)}")

    def get_stats(self) -> Dict[str, any]:
        """
        Gibt Statistiken über das Refactoring
        
        Returns:
            Dictionary mit Statistiken
        """
        if not self.changes:
            return {
                "total_changes": 0,
                "high_confidence": 0,
                "medium_confidence": 0,
                "low_confidence": 0,
                "affected_lines": 0
            }

        high = sum(1 for c in self.changes if c.confidence >= 0.8)
        medium = sum(1 for c in self.changes if 0.5 <= c.confidence < 0.8)
        low = sum(1 for c in self.changes if c.confidence < 0.5)

        return {
            "total_changes": len(self.changes),
            "high_confidence": high,
            "medium_confidence": medium,
            "low_confidence": low,
            "affected_lines": len(set(c.line for c in self.changes))
        }


class StruktogrammFormatter:
    """Formatiert Struktogramme nach BW-Standard"""

    @staticmethod
    def normalize_spacing(text: str) -> str:
        """
        Normalisiert Abstände in Struktogrammen
        
        Args:
            text: Der zu normalisierende Text
            
        Returns:
            Normalisierter Text
        """
        # Normalisiere Abstände nach Operatoren
        text = re.sub(r'Deklaration:\s+', 'Deklaration: ', text)
        text = re.sub(r'Initialisierung:\s+', 'Initialisierung: ', text)
        text = re.sub(r'Zuweisung:\s+', 'Zuweisung: ', text)
        text = re.sub(r'Ausgabe:\s+', 'Ausgabe: ', text)
        text = re.sub(r'Einlesen:\s+', 'Einlesen: ', text)
        text = re.sub(r'Rückgabe:\s+', 'Rückgabe: ', text)
        
        return text

    @staticmethod
    def ensure_operator_consistency(text: str) -> str:
        """
        Stellt sicher, dass Operatoren konsistent verwendet werden
        
        Args:
            text: Der zu konvertierende Text
            
        Returns:
            Text mit konsistenten Operatoren
        """
        replacements = [
            (r'Deklaration\s+und\s+Deklaration', 'Deklaration und Initialisierung'),
            (r'Zahl\s+von', 'Zähle'),
            (r'While\s+solange', 'Wiederhole solange'),
        ]
        
        result = text
        for pattern, replacement in replacements:
            result = re.sub(pattern, replacement, result, flags=re.IGNORECASE)
        
        return result


def create_refactoring_report(changes: List[RefactoringChange]) -> str:
    """
    Erstellt einen Refactoring-Bericht
    
    Args:
        changes: Liste der durchgeführten Änderungen
        
    Returns:
        Formatierter Bericht
    """
    if not changes:
        return "✅ Keine Änderungen notwendig - Text ist bereits konform!"

    report = f"""
📝 Refactoring-Bericht
{'='*60}

Änderungen: {len(changes)}

"""

    for change in changes:
        report += f"\n📍 Zeile {change.line}:\n"
        report += f"   {change.reason}\n"
        report += f"   ❌ Original: {change.original}\n"
        report += f"   ✅ Neu:     {change.refactored}\n"
        report += f"   🎯 Genauigkeit: {change.confidence*100:.0f}%\n"

    return report


def apply_refactoring_batch(file_paths: List[str], dry_run: bool = True) -> Dict[str, Tuple[int, List[RefactoringChange]]]:
    """
    Wendet Refactoring auf mehrere Dateien an
    
    Args:
        file_paths: Liste mit Dateipfaden
        dry_run: Wenn True, nur vorschaugen (keine Änderungen)
        
    Returns:
        Dictionary mit Ergebnissen pro Datei
    """
    results = {}
    refactorer = StruktogrammRefactorer()

    for filepath in file_paths:
        try:
            if dry_run:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                _, changes = refactorer.refactor_content(content)
            else:
                _, changes = refactorer.refactor_file(filepath, in_place=True)
            
            results[filepath] = (len(changes), changes)
        except Exception as e:
            print(f"⚠️  Fehler bei {filepath}: {str(e)}")

    return results
