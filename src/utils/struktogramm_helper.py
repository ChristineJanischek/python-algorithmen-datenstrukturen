"""
Struktogramm Helper für Baden-Württemberg Abitur-Standards

Dieses Modul hilft bei der Erstellung, Validierung und Darstellung von
Struktogrammen nach den BW-Abitur-Standards (Version 2.2).

Autor: Erstellt für python-algorithmen-datenstrukturen
Version: 1.0
Datum: 05.02.2026
"""

import re
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
from enum import Enum


class OperatorType(Enum):
    """Enum für die verschiedenen Operator-Typen"""
    DEKLARATION = "Deklaration"
    INITIALISIERUNG = "Initialisierung"
    DEKL_INIT = "Deklaration und Initialisierung"
    ZUWEISUNG = "Zuweisung"
    EINLESEN = "Einlesen"
    AUSGABE = "Ausgabe"
    RUECKGABE = "Rückgabe"
    AUFRUF = "Aufruf"
    WENN = "Wenn"
    WIEDERHOLE_SOLANGE = "Wiederhole solange"
    ZAEHLE = "Zähle"
    WIEDERHOLE_VON = "Wiederhole von"


@dataclass
class StruktogrammElement:
    """Repräsentiert ein Element im Struktogramm"""
    operator_type: OperatorType
    content: str
    level: int = 0  # Verschachtelungsebene
    branches: Optional[Dict[str, List['StruktogrammElement']]] = None
    
    def __post_init__(self):
        if self.branches is None and self.operator_type == OperatorType.WENN:
            self.branches = {"J": [], "N": []}


class StruktogrammValidator:
    """Validiert Struktogramme nach BW-Standards"""
    
    # Regex-Patterns für verschiedene Operatoren
    PATTERNS = {
        OperatorType.DEKLARATION: r"^Deklaration:\s+\w+(\s+als\s+\w+)?$",
        OperatorType.INITIALISIERUNG: r"^Initialisierung:\s+\w+\s*=\s*.+$",
        OperatorType.DEKL_INIT: r"^Deklaration und Initialisierung:\s+\w+(\s+als\s+\w+)?\s*=\s*.+$",
        OperatorType.ZUWEISUNG: r"^Zuweisung:\s+[\w\[\]]+\s*=\s*.+$",
        OperatorType.EINLESEN: r"^(Deklaration und )?Einlesen:\s+\w+(\s+als\s+\w+)?$",
        OperatorType.AUSGABE: r"^(Zeilenweise )?Ausgabe:\s+.+$",
        OperatorType.RUECKGABE: r"^Rückgabe:\s+.+$",
        OperatorType.AUFRUF: r"^Aufruf:\s+\w+\([^\)]*\)$",
        OperatorType.WENN: r"^Wenn\s+.+,\s+dann$",
        OperatorType.WIEDERHOLE_SOLANGE: r"^Wiederhole solange\s+.+$",
        OperatorType.ZAEHLE: r"^Zähle\s+\w+\s+von\s+.+\s+bis\s+.+,\s+Schrittweite\s+.+$",
        OperatorType.WIEDERHOLE_VON: r"^Wiederhole von\s+.+\s+solange\s+.+,\s+Schrittweite\s+.+$",
    }
    
    @classmethod
    def validate_line(cls, line: str) -> Tuple[bool, Optional[OperatorType], Optional[str]]:
        """
        Validiert eine einzelne Zeile gegen die BW-Standards.
        
        Returns:
            Tuple[bool, Optional[OperatorType], Optional[str]]:
            (ist_gültig, operator_typ, fehlermeldung)
        """
        line = line.strip()
        
        # Leere Zeilen und Kommentare ignorieren
        if not line or line.startswith("#") or line == "(nichts)":
            return (True, None, None)
        
        # Verzweigungsmarkierungen ignorieren (grafische Darstellung)
        if line in ["J", "N", ", sonst"]:
            return (True, None, None)
        
        # Prüfe gegen alle Patterns
        for op_type, pattern in cls.PATTERNS.items():
            if re.match(pattern, line):
                return (True, op_type, None)
        
        # Keine Übereinstimmung gefunden
        return (False, None, f"Zeile entspricht keinem gültigen Operator: '{line}'")
    
    @classmethod
    def validate_struktogramm(cls, lines: List[str]) -> List[str]:
        """
        Validiert ein gesamtes Struktogramm.
        
        Args:
            lines: Liste der Zeilen des Struktogramms
            
        Returns:
            Liste von Fehlermeldungen (leer wenn alles OK)
        """
        errors = []
        indentation_level = 0
        
        for i, line in enumerate(lines, start=1):
            # Einrückung berechnen
            stripped = line.lstrip()
            current_indent = len(line) - len(stripped)
            
            is_valid, op_type, error = cls.validate_line(stripped)
            
            if not is_valid and error:
                errors.append(f"Zeile {i}: {error}")
            
            # Prüfe Einrückung bei Kontrollstrukturen
            if op_type in [OperatorType.WIEDERHOLE_SOLANGE, OperatorType.ZAEHLE, 
                          OperatorType.WIEDERHOLE_VON, OperatorType.WENN]:
                indentation_level += 1
        
        return errors


class StruktogrammRenderer:
    """Rendert Struktogramme in verschiedenen Formaten"""
    
    @staticmethod
    def render_box(content: str, width: int = 55) -> str:
        """
        Erstellt eine einfache Box um den Inhalt.
        
        Args:
            content: Der anzuzeigende Text
            width: Breite der Box
            
        Returns:
            Box als String
        """
        lines = content.split('\n')
        padded_lines = []
        
        for line in lines:
            if len(line) < width - 4:
                line = line + ' ' * (width - 4 - len(line))
            padded_lines.append(f"│ {line} │")
        
        top = "┌" + "─" * (width - 2) + "┐"
        bottom = "└" + "─" * (width - 2) + "┘"
        
        return "\n".join([top] + padded_lines + [bottom])
    
    @staticmethod
    def render_branch(condition: str, j_content: str, n_content: str, width: int = 55) -> str:
        """
        Erstellt eine Verzweigung (if-then-else).
        
        Args:
            condition: Die Bedingung
            j_content: Inhalt des Ja-Zweigs
            n_content: Inhalt des Nein-Zweigs
            width: Gesamtbreite
            
        Returns:
            Verzweigung als String
        """
        half_width = width // 2 - 2
        
        # Condition box
        top = "┌" + "─" * (width - 2) + "┐"
        cond_line = f"│ {condition.center(width - 4)} │"
        divider = "├" + "─" * (width - 2) + "┤"
        
        # Split content
        j_lines = j_content.split('\n')
        n_lines = n_content.split('\n')
        max_lines = max(len(j_lines), len(n_lines))
        
        # Pad lines
        while len(j_lines) < max_lines:
            j_lines.append('')
        while len(n_lines) < max_lines:
            n_lines.append('')
        
        # Create branch lines
        branch_lines = ["│ J" + " " * (half_width - 2) + "│ N" + " " * (half_width - 2) + "│"]
        branch_lines.append("│" + " " * half_width + "│" + " " * half_width + "│")
        
        for j_line, n_line in zip(j_lines, n_lines):
            j_padded = j_line.ljust(half_width - 2)
            n_padded = n_line.ljust(half_width - 2)
            branch_lines.append(f"│ {j_padded} │ {n_padded} │")
        
        branch_lines.append("│" + " " * half_width + "│" + " " * half_width + "│")
        bottom = "└" + "─" * half_width + "┴" + "─" * half_width + "┘"
        
        return "\n".join([top, cond_line, divider] + branch_lines + [bottom])
    
    @staticmethod
    def render_loop(condition: str, body: str, width: int = 55) -> str:
        """
        Erstellt eine Schleife.
        
        Args:
            condition: Die Schleifenbedingung
            body: Schleifenkörper
            width: Breite
            
        Returns:
            Schleife als String
        """
        top = "┌" + "─" * (width - 2) + "┐"
        loop_top = f"│ ┌─ {condition}" + " " * (width - len(condition) - 7) + "│"
        
        body_lines = body.split('\n')
        loop_body = []
        for line in body_lines:
            padded = line.ljust(width - 6)
            loop_body.append(f"│ │  {padded}│")
        
        loop_body.append(f"│ │" + " " * (width - 4) + "│")
        bottom = "└─┘" + "─" * (width - 4) + "┘"
        
        return "\n".join([top, loop_top] + loop_body + [bottom])


class StruktogrammBuilder:
    """Hilft beim Erstellen von Struktogrammen"""
    
    def __init__(self):
        self.elements: List[str] = []
        self.indent_level = 0
    
    def _indent(self) -> str:
        """Gibt die aktuelle Einrückung zurück"""
        return "    " * self.indent_level
    
    def deklaration(self, variable: str, datentyp: Optional[str] = None) -> 'StruktogrammBuilder':
        """Fügt eine Deklaration hinzu"""
        if datentyp:
            self.elements.append(f"{self._indent()}Deklaration: {variable} als {datentyp}")
        else:
            self.elements.append(f"{self._indent()}Deklaration: {variable}")
        return self
    
    def initialisierung(self, variable: str, wert: str) -> 'StruktogrammBuilder':
        """Fügt eine Initialisierung hinzu"""
        self.elements.append(f"{self._indent()}Initialisierung: {variable} = {wert}")
        return self
    
    def dekl_init(self, variable: str, wert: str, datentyp: Optional[str] = None) -> 'StruktogrammBuilder':
        """Fügt eine kombinierte Deklaration und Initialisierung hinzu"""
        if datentyp:
            self.elements.append(f"{self._indent()}Deklaration und Initialisierung: {variable} als {datentyp} = {wert}")
        else:
            self.elements.append(f"{self._indent()}Deklaration und Initialisierung: {variable} = {wert}")
        return self
    
    def zuweisung(self, variable: str, wert: str) -> 'StruktogrammBuilder':
        """Fügt eine Zuweisung hinzu"""
        self.elements.append(f"{self._indent()}Zuweisung: {variable} = {wert}")
        return self
    
    def einlesen(self, variable: str, datentyp: Optional[str] = None) -> 'StruktogrammBuilder':
        """Fügt ein Einlesen hinzu"""
        if datentyp:
            self.elements.append(f"{self._indent()}Einlesen: {variable} als {datentyp}")
        else:
            self.elements.append(f"{self._indent()}Einlesen: {variable}")
        return self
    
    def ausgabe(self, inhalt: str) -> 'StruktogrammBuilder':
        """Fügt eine Ausgabe hinzu"""
        self.elements.append(f"{self._indent()}Ausgabe: {inhalt}")
        return self
    
    def rueckgabe(self, wert: str) -> 'StruktogrammBuilder':
        """Fügt eine Rückgabe hinzu"""
        self.elements.append(f"{self._indent()}Rückgabe: {wert}")
        return self
    
    def aufruf(self, methode: str, parameter: str = "") -> 'StruktogrammBuilder':
        """Fügt einen Methodenaufruf hinzu"""
        self.elements.append(f"{self._indent()}Aufruf: {methode}({parameter})")
        return self
    
    def wenn_start(self, bedingung: str) -> 'StruktogrammBuilder':
        """Startet eine Wenn-Dann-Verzweigung"""
        self.elements.append(f"{self._indent()}Wenn {bedingung}, dann")
        self.elements.append(f"{self._indent()}    J")
        self.indent_level += 2
        return self
    
    def sonst(self) -> 'StruktogrammBuilder':
        """Fügt einen Sonst-Zweig hinzu"""
        self.indent_level -= 2
        self.elements.append(f"{self._indent()}    , sonst")
        self.elements.append(f"{self._indent()}    N")
        self.indent_level += 2
        return self
    
    def wenn_ende(self) -> 'StruktogrammBuilder':
        """Beendet eine Verzweigung"""
        self.indent_level -= 2
        return self
    
    def wiederhole_solange_start(self, bedingung: str) -> 'StruktogrammBuilder':
        """Startet eine While-Schleife"""
        self.elements.append(f"{self._indent()}Wiederhole solange {bedingung}")
        self.indent_level += 1
        return self
    
    def schleife_ende(self) -> 'StruktogrammBuilder':
        """Beendet eine Schleife"""
        self.indent_level -= 1
        return self
    
    def zaehle_start(self, variable: str, start: str, ende: str, schrittweite: str = "1") -> 'StruktogrammBuilder':
        """Startet eine For-Schleife (Zähle-Variante)"""
        self.elements.append(f"{self._indent()}Zähle {variable} von {start} bis {ende}, Schrittweite {schrittweite}")
        self.indent_level += 1
        return self
    
    def wiederhole_von_start(self, variable: str, start: str, bedingung: str, schrittweite: str = "1") -> 'StruktogrammBuilder':
        """Startet eine For-Schleife (Wiederhole-von-Variante)"""
        self.elements.append(f"{self._indent()}Wiederhole von {variable} = {start} solange {bedingung}, Schrittweite {schrittweite}")
        self.indent_level += 1
        return self
    
    def build(self) -> str:
        """Gibt das fertige Struktogramm zurück"""
        return "\n".join(self.elements)
    
    def validate(self) -> List[str]:
        """Validiert das erstellte Struktogramm"""
        return StruktogrammValidator.validate_struktogramm(self.elements)


# Hilfs-Funktionen für häufige Patterns

def pattern_array_durchlaufen(array_name: str, index_var: str = "i") -> str:
    """
    Erstellt das Pattern für Array-Durchlauf.
    
    Args:
        array_name: Name des Arrays
        index_var: Name der Index-Variable
        
    Returns:
        Struktogramm als String
    """
    builder = StruktogrammBuilder()
    builder.dekl_init("n", f"Anzahl der Elemente des Arrays {array_name}")
    builder.zaehle_start(index_var, "0", "n - 1")
    builder.ausgabe(f"{array_name}[{index_var}]")
    builder.schleife_ende()
    return builder.build()


def pattern_summe_berechnen(array_name: str, summe_var: str = "summe") -> str:
    """
    Erstellt das Pattern für Summenberechnung.
    
    Args:
        array_name: Name des Arrays
        summe_var: Name der Summen-Variable
        
    Returns:
        Struktogramm als String
    """
    builder = StruktogrammBuilder()
    builder.dekl_init(summe_var, "0")
    builder.dekl_init("n", f"Anzahl der Elemente des Arrays {array_name}")
    builder.zaehle_start("i", "0", "n - 1")
    builder.zuweisung(summe_var, f"{summe_var} + {array_name}[i]")
    builder.schleife_ende()
    builder.ausgabe(f'"{summe_var.capitalize()}: " + {summe_var}')
    return builder.build()


def pattern_maximum_finden(array_name: str) -> str:
    """
    Erstellt das Pattern für Maximum-Suche.
    
    Args:
        array_name: Name des Arrays
        
    Returns:
        Struktogramm als String
    """
    builder = StruktogrammBuilder()
    builder.dekl_init("max", f"{array_name}[0]")
    builder.dekl_init("n", f"Anzahl der Elemente des Arrays {array_name}")
    builder.zaehle_start("i", "1", "n - 1")
    builder.wenn_start(f"{array_name}[i] > max")
    builder.zuweisung("max", f"{array_name}[i]")
    builder.sonst()
    builder.elements.append(f"{builder._indent()}(nichts)")
    builder.wenn_ende()
    builder.schleife_ende()
    builder.ausgabe('"Maximum: " + max')
    return builder.build()


def pattern_lineare_suche(array_name: str, such_var: str = "suchWert") -> str:
    """
    Erstellt das Pattern für lineare Suche.
    
    Args:
        array_name: Name des Arrays
        such_var: Name der Such-Variable
        
    Returns:
        Struktogramm als String
    """
    builder = StruktogrammBuilder()
    builder.einlesen(such_var, "Text")
    builder.dekl_init("gefunden", "falsch")
    builder.dekl_init("position", "-1")
    builder.dekl_init("n", f"Anzahl der Elemente des Arrays {array_name}")
    builder.zaehle_start("i", "0", "n - 1")
    builder.wenn_start(f"{array_name}[i] == {such_var}")
    builder.zuweisung("gefunden", "wahr")
    builder.zuweisung("position", "i")
    builder.sonst()
    builder.elements.append(f"{builder._indent()}(nichts)")
    builder.wenn_ende()
    builder.schleife_ende()
    builder.wenn_start("gefunden == wahr")
    builder.ausgabe('"Gefunden an Position: " + position')
    builder.sonst()
    builder.ausgabe('"Nicht gefunden"')
    builder.wenn_ende()
    return builder.build()


# Utility-Funktionen

def load_struktogramm_from_file(filepath: str) -> List[str]:
    """
    Lädt ein Struktogramm aus einer Textdatei.
    
    Args:
        filepath: Pfad zur Datei
        
    Returns:
        Liste der Zeilen
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        return [line.rstrip() for line in f.readlines()]


def save_struktogramm_to_file(filepath: str, content: str):
    """
    Speichert ein Struktogramm in eine Textdatei.
    
    Args:
        filepath: Pfad zur Zieldatei
        content: Struktogramm-Inhalt
    """
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)


def print_validation_results(errors: List[str]):
    """
    Gibt Validierungsergebnisse formatiert aus.
    
    Args:
        errors: Liste der Fehler
    """
    if not errors:
        print("✅ Struktogramm ist valide!")
    else:
        print(f"❌ {len(errors)} Fehler gefunden:")
        for error in errors:
            print(f"  - {error}")


# Beispiel-Verwendung
if __name__ == "__main__":
    print("=== Struktogramm Helper Demo ===\n")
    
    # Beispiel 1: Builder verwenden
    print("1. Beispiel: Array-Summe berechnen")
    print("-" * 60)
    builder = StruktogrammBuilder()
    builder.dekl_init("zahlen", "[5, 10, 15, 20]")
    builder.dekl_init("summe", "0")
    builder.dekl_init("n", "Anzahl der Elemente des Arrays zahlen")
    builder.zaehle_start("i", "0", "n - 1")
    builder.zuweisung("summe", "summe + zahlen[i]")
    builder.schleife_ende()
    builder.ausgabe('"Summe: " + summe')
    
    struktogramm1 = builder.build()
    print(struktogramm1)
    print()
    
    # Validierung
    errors = builder.validate()
    print_validation_results(errors)
    print("\n")
    
    # Beispiel 2: Pattern verwenden
    print("2. Beispiel: Pattern für Maximum finden")
    print("-" * 60)
    struktogramm2 = pattern_maximum_finden("werte")
    print(struktogramm2)
    print()
    
    # Validierung
    errors = StruktogrammValidator.validate_struktogramm(struktogramm2.split('\n'))
    print_validation_results(errors)
    print("\n")
    
    # Beispiel 3: Grafische Darstellung
    print("3. Beispiel: Grafische Box-Darstellung")
    print("-" * 60)
    renderer = StruktogrammRenderer()
    box = renderer.render_box("Deklaration und Initialisierung: summe = 0")
    print(box)
    print()
    
    # Beispiel 4: Verzweigung darstellen
    print("4. Beispiel: Verzweigung darstellen")
    print("-" * 60)
    branch = renderer.render_branch(
        "alter >= 18",
        'Ausgabe: "Volljährig"',
        'Ausgabe: "Minderjährig"'
    )
    print(branch)
    print()
    
    # Beispiel 5: Schleife darstellen
    print("5. Beispiel: Schleife darstellen")
    print("-" * 60)
    loop = renderer.render_loop(
        "Wiederhole solange i < 10",
        'Ausgabe: i\nZuweisung: i = i + 1'
    )
    print(loop)
