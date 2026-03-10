"""
Struktogramm Knowledge Base - Zentrale Wissensdatenbank

Dieses Modul enthält DIE zentrale Wissensdatenbank für alle Struktogramm-Standards
nach Baden-Württemberg (Version 2.2). Es dient als Single Source of Truth für:

- Operatorenliste (alle gültigen Operatoren)
- BW-Notation-Standards (Briefumschlag-Alternative, umgedrehtes L, etc.)
- Validierungs-Regeln
- Pattern-Templates für häufige Algorithmen

Diese Wissensdatenbank wird von allen Struktogramm-Tools verwendet:
- struktogramm_helper.py (Erstellung)
- struktogramm_validator.py (Validierung)
- struktogramm_notation_validator.py (Notation)
- apps/drawio-extension (Draw.io Shapes)
- AI-Assistenten (Copilot, etc.)

Autor: Erstellt für python-algorithmen-datenstrukturen
Version: 1.0
Datum: 10.03.2026
Basis: Operatorenliste für Struktogramme v2.2 (Abiturprüfung BW)
"""

from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum


class OperatorKategorie(Enum):
    """Kategorien der Struktogramm-Operatoren"""
    VARIABLEN = "Variablen und Datenstrukturen"
    EIN_AUSGABE = "Ein- und Ausgabe"
    FUNKTIONEN = "Funktionen und Methoden"
    KONTROLLSTRUKTUREN = "Kontrollstrukturen"
    ARRAYS = "Arrays"
    DATENSAETZE = "Datensätze"


@dataclass
class OperatorDefinition:
    """Definition eines Struktogramm-Operators nach BW-Standard"""
    name: str
    syntax: str
    kategorie: OperatorKategorie
    beschreibung: str
    beispiel: str
    xml_typ: str
    hinweise: List[str]
    varianten: Optional[List[str]] = None


class StruktogrammKnowledgeBase:
    """
    Zentrale Wissensdatenbank für Struktogramm-Standards (BW v2.2)
    
    Diese Klasse ist das "Gedächtnis" für alle Struktogramm-Regeln,
    Operatoren und Notationen. Sie stellt sicher, dass ALLE Tools
    im System die gleichen Standards verwenden.
    """
    
    VERSION = "2.2"
    QUELLE = "Abiturprüfung Baden-Württemberg"
    DATUM = "01.09.2024"
    
    def __init__(self):
        """Initialisiert die Wissensdatenbank mit allen BW-Standard-Operatoren"""
        self._operatoren = self._initialisiere_operatoren()
        self._notation_regeln = self._initialisiere_notation_regeln()
        self._pattern_templates = self._initialisiere_pattern_templates()
        self._grafik_formen = self._initialisiere_grafik_formen()
    
    def _initialisiere_operatoren(self) -> Dict[str, OperatorDefinition]:
        """Initialisiert alle gültigen Operatoren nach BW-Standard"""
        operatoren = {}
        
        # ===== 1. VARIABLEN UND DATENSTRUKTUREN =====
        
        operatoren["deklaration"] = OperatorDefinition(
            name="Deklaration",
            syntax="Deklaration: variable |als datentyp|",
            kategorie=OperatorKategorie.VARIABLEN,
            beschreibung="Deklaration einer Variablen, optionale Angabe des Datentyps",
            beispiel="Deklaration: alter als Ganzzahl",
            xml_typ="deklaration",
            hinweise=[
                "Variable wird bekannt gemacht und reserviert Speicherplatz",
                "Datentyp ist optional, aber empfohlen für bessere Lesbarkeit",
                "Häufige Datentypen: Ganzzahl, Dezimalzahl, Text, Wahrheitswert"
            ]
        )
        
        operatoren["initialisierung"] = OperatorDefinition(
            name="Initialisierung",
            syntax="Initialisierung: variable = wert",
            kategorie=OperatorKategorie.VARIABLEN,
            beschreibung="Initialisierung einer Variablen mit einem Ausgangswert",
            beispiel="Initialisierung: guthaben = 10",
            xml_typ="zuweisung",
            hinweise=[
                "Wird selten isoliert verwendet",
                "Meist kombiniert mit Deklaration (siehe Deklaration und Initialisierung)"
            ]
        )
        
        operatoren["deklaration_und_initialisierung"] = OperatorDefinition(
            name="Deklaration und Initialisierung",
            syntax="Deklaration und Initialisierung: variable |als datentyp| = wert",
            kategorie=OperatorKategorie.VARIABLEN,
            beschreibung="Kombination von Deklaration und Initialisierung",
            beispiel="Deklaration und Initialisierung: anzahl als Ganzzahl = 0",
            xml_typ="deklaration_und_initialisierung",
            hinweise=[
                "Häufigste Form bei Variablenerstellung",
                "Variable ist sofort einsatzbereit"
            ]
        )
        
        operatoren["zuweisung"] = OperatorDefinition(
            name="Zuweisung",
            syntax="Zuweisung: element = wert",
            kategorie=OperatorKategorie.VARIABLEN,
            beschreibung="Zuweisung eines Wertes zu einem bereits existierenden Element",
            beispiel="Zuweisung: qm = laenge * breite",
            xml_typ="zuweisung",
            hinweise=[
                "Variable muss bereits existieren",
                "Kann mehrfach vorkommen (Wertänderung während Laufzeit)"
            ]
        )
        
        # ===== 2. EIN- UND AUSGABE =====
        
        operatoren["einlesen"] = OperatorDefinition(
            name="Einlesen",
            syntax="Einlesen: variable |als datentyp|",
            kategorie=OperatorKategorie.EIN_AUSGABE,
            beschreibung="Einlesen einer Eingabe (z.B. aus Eingabefeld, Kommandozeile)",
            beispiel="Einlesen: betrag",
            xml_typ="einlesen",
            hinweise=[
                "Variable existiert bereits",
                "Datentyp ist bekannt"
            ],
            varianten=["Deklaration und Einlesen: variable |als datentyp|"]
        )
        
        operatoren["deklaration_und_einlesen"] = OperatorDefinition(
            name="Deklaration und Einlesen",
            syntax="Deklaration und Einlesen: variable |als datentyp|",
            kategorie=OperatorKategorie.EIN_AUSGABE,
            beschreibung="Variable wird gleichzeitig deklariert und Wert wird eingelesen",
            beispiel="Deklaration und Einlesen: betrag als Dezimalzahl",
            xml_typ="deklaration_und_einlesen",
            hinweise=[
                "Häufig in Aufgaben, da Eingaben erwartet werden"
            ]
        )
        
        operatoren["ausgabe"] = OperatorDefinition(
            name="Ausgabe",
            syntax="Ausgabe: inhalt",
            kategorie=OperatorKategorie.EIN_AUSGABE,
            beschreibung="Ausgabe von Variablen, Arrays, Text oder Kombinationen",
            beispiel='Ausgabe: "Die Fläche beträgt " + qm + " Quadratmeter."',
            xml_typ="ausgabe",
            hinweise=[
                "Kann einzelne Variablen ausgeben: Ausgabe: ergebnis",
                "Kann Kombinationen ausgeben: Ausgabe: 'Ergebnis: ' + x",
                "Kann Arrays ausgeben: Ausgabe: werte[i]",
                "Mit Zeilenumbruch: Ausgabe: 'Hallo!' + Zeilenumbruch"
            ]
        )
        
        operatoren["rueckgabe"] = OperatorDefinition(
            name="Rückgabe",
            syntax="Rückgabe: wert",
            kategorie=OperatorKategorie.EIN_AUSGABE,
            beschreibung="Rückgabe eines Wertes innerhalb einer Funktion/Methode",
            beispiel="Rückgabe: strecke",
            xml_typ="rueckgabe",
            hinweise=[
                "Beendet die Funktionsausführung sofort",
                "Wert kann Variable, Ausdruck oder Konstante sein",
                "Wird oft am Ende von Funktionen verwendet"
            ]
        )
        
        # ===== 3. FUNKTIONEN UND METHODEN =====
        
        operatoren["aufruf"] = OperatorDefinition(
            name="Aufruf",
            syntax="Aufruf: methode/unterprogramm(|parameter|)",
            kategorie=OperatorKategorie.FUNKTIONEN,
            beschreibung="Aufruf einer Funktion/Methode/Prozedur/Unterprogramm",
            beispiel="Aufruf: berechne(x, y, z)",
            xml_typ="aufruf",
            hinweise=[
                "Wiederverwendung von bestehendem Code",
                "Modularisierung von Programmen",
                "Grafische Kennzeichnung: Rechteck mit vertikalen Strichen an den Seiten",
                "Mit Rückgabewert: Zuweisung: ergebnis = berechne(wert)"
            ],
            varianten=[
                "Aufruf: sortiereListe()",
                "Aufruf: einzahlen(betrag)",
                "Aufruf: berechne(x, y, z)"
            ]
        )
        
        # ===== 4. KONTROLLSTRUKTUREN =====
        
        operatoren["wenn"] = OperatorDefinition(
            name="Wenn",
            syntax="Wenn bedingung, dann […] |, sonst […]|",
            kategorie=OperatorKategorie.KONTROLLSTRUKTUREN,
            beschreibung="Verzweigungs- bzw. Mehrfachauswahlbedingung (Alternative)",
            beispiel="Wenn alter >= 18, dann J [...] , sonst N [...]",
            xml_typ="alternative",
            hinweise=[
                "WICHTIG: Briefumschlag-Form nach BW-Standard!",
                "Grafisch: Rechteck mit eingebettetem gleichschenkligem Dreieck",
                "Dreieck: Spitze nach unten, Bedingung im Dreieck",
                "J-Zweig: Links ('Ja'-Anweisungen)",
                "N-Zweig: Rechts ('Nein'-Anweisungen)",
                "Sonst-Zweig ist optional",
                "Vergleichsoperatoren: ==, !=, <, <=, >, >=",
                "Logische Operatoren: AND, OR, NOT",
                "Leere Zweige als [keine Anweisung] kennzeichnen"
            ]
        )
        
        operatoren["wiederhole_solange"] = OperatorDefinition(
            name="Wiederhole solange",
            syntax="Wiederhole solange bedingung",
            kategorie=OperatorKategorie.KONTROLLSTRUKTUREN,
            beschreibung="While-Schleife mit vorausgehender Bedingungsprüfung",
            beispiel="Wiederhole solange i < 10",
            xml_typ="while",
            hinweise=[
                "Bedingung wird VOR jedem Durchlauf geprüft",
                "Bei falscher Anfangsbedingung: 0 Durchläufe",
                "Grafisch: umgedrehtes L (horizontal gespiegelt)",
                "Schleifenkopf: Horizontaler Kasten oben",
                "Vertikale Linie: Links vom Kopf nach unten",
                "WICHTIG: Im Körper muss die Bedingung irgendwann falsch werden!"
            ]
        )
        
        operatoren["wiederhole_von"] = OperatorDefinition(
            name="Wiederhole von",
            syntax="Wiederhole von startwert solange bedingung, Schrittweite schrittweite",
            kategorie=OperatorKategorie.KONTROLLSTRUKTUREN,
            beschreibung="For-Schleife (Variante 1: ähnlich while mit Init und Schrittweite)",
            beispiel="Wiederhole von i = 0 solange i < 5, Schrittweite 1",
            xml_typ="for",
            hinweise=[
                "Ähnelt while-Schleife mit expliziter Initialisierung",
                "Grafisch: umgedrehtes L (wie While-Schleife)",
                "Endwert ist exklusiv bei '<' (i < 5 → 0,1,2,3,4)"
            ]
        )
        
        operatoren["zaehle"] = OperatorDefinition(
            name="Zähle",
            syntax="Zähle zählvariable von startwert bis endwert, Schrittweite schrittweite",
            kategorie=OperatorKategorie.KONTROLLSTRUKTUREN,
            beschreibung="For-Schleife (Variante 2: kompakte Form mit 'bis', Endwert inklusiv)",
            beispiel="Zähle i von 0 bis 4, Schrittweite 1",
            xml_typ="for",
            hinweise=[
                "Kompaktere Form als 'Wiederhole von'",
                "Endwert ist INKLUSIV (bis 4 → 0,1,2,3,4)",
                "Grafisch: umgedrehtes L",
                "Schrittweite kann positiv (hoch) oder negativ (runter) sein",
                "Bei Schrittweite 1 oft weggelassen (implizit)"
            ]
        )
        
        # ===== 5. ARRAYS =====
        
        operatoren["array_deklaration_initialisierung"] = OperatorDefinition(
            name="Array-Deklaration und Initialisierung",
            syntax="Deklaration und Initialisierung: array = [wert1, wert2, ...]",
            kategorie=OperatorKategorie.ARRAYS,
            beschreibung="Array deklarieren und mit Werten initialisieren",
            beispiel="Deklaration und Initialisierung: zahlen = [10, 20, 30, 40, 50]",
            xml_typ="array_deklaration_initialisierung",
            hinweise=[
                "Elemente werden über Index angesprochen (meist ab 0)",
                "Können gleiche oder verschiedene Datentypen enthalten"
            ]
        )
        
        operatoren["array_zuweisung"] = OperatorDefinition(
            name="Array-Element-Zuweisung",
            syntax="Zuweisung: array[index] = wert",
            kategorie=OperatorKategorie.ARRAYS,
            beschreibung="Zuweisung eines Wertes zu einem Array-Element",
            beispiel="Zuweisung: zahlen[2] = 99",
            xml_typ="zuweisung",
            hinweise=[
                "Index beginnt meist bei 0",
                "Array muss bereits existieren"
            ]
        )
        
        operatoren["array_anhaengen"] = OperatorDefinition(
            name="Anhängen an Array",
            syntax="Anhängen: array.anhängen(wert)",
            kategorie=OperatorKategorie.ARRAYS,
            beschreibung="Anhängen eines Elements am Ende des Arrays",
            beispiel="Anhängen: zahlen.anhängen(60)",
            xml_typ="anhaengen",
            hinweise=[
                "Vergrößert das Array dynamisch",
                "Neues Element wird am Ende eingefügt"
            ]
        )
        
        operatoren["array_anzahl_elemente"] = OperatorDefinition(
            name="Anzahl der Elemente",
            syntax="Anzahl der Elemente des Arrays array",
            kategorie=OperatorKategorie.ARRAYS,
            beschreibung="Gibt die Anzahl der Elemente im Array zurück",
            beispiel="Ausgabe: Anzahl der Elemente des Arrays zahlen",
            xml_typ="array_laenge",
            hinweise=[
                "Wird oft in Schleifen verwendet",
                "Beispiel: Zähle i von 0 bis Anzahl der Elemente - 1"
            ]
        )
        
        return operatoren
    
    def _initialisiere_notation_regeln(self) -> Dict[str, dict]:
        """Initialisiert die BW-Notation-Regeln"""
        return {
            "briefumschlag_alternative": {
                "name": "Briefumschlag-Alternative (verbindlich)",
                "beschreibung": "Standard-Form für Verzweigungen im BW-Abitur",
                "regeln": [
                    "Bedingung oben mittig: 'Wenn bedingung, dann'",
                    "Ja-Fall links: Zeile 'J', darunter Ja-Anweisungen",
                    "Nein-Fall rechts: Zeilen ', sonst' und 'N', darunter Nein-Anweisungen",
                    "KEINE Kurzschreibweise wie 'Wenn ... / J / N'",
                    "Leere Zweige als '[keine Anweisung]' kennzeichnen"
                ],
                "template": """Wenn bedingung, dann
     J
          [Anweisungen Ja]
     , sonst
     N
          [Anweisungen Nein oder [keine Anweisung]]""",
                "grafik": "Rechteck mit gleichschenkligem Dreieck (Spitze unten)",
                "qualitaetscheck": [
                    "Enthält 'Wenn ..., dann'?",
                    "Ist 'J' vorhanden und eingerückt?",
                    "Sind ', sonst' und 'N' vorhanden?",
                    "Sind leere Zweige als '[keine Anweisung]' markiert?"
                ]
            },
            "umgedrehtes_l": {
                "name": "Umgedrehtes L (Schleifen)",
                "beschreibung": "Standard-Form für while- und for-Schleifen",
                "regeln": [
                    "Schleifenkopf: Horizontaler Kasten oben mit Bedingung",
                    "Vertikale Linie: Links vom Kopf nach unten",
                    "Schleifenkörper: Darunter eingerückt"
                ],
                "grafik": "Umgedrehtes L (horizontal gespiegelt)",
                "anwendung": ["While-Schleife", "For-Schleife (beide Varianten)"]
            },
            "aufruf_seitenstriche": {
                "name": "Aufruf mit Seitenstrichen",
                "beschreibung": "Kennzeichnung von Funktionsaufrufen",
                "regeln": [
                    "Rechteck mit vertikalen Strichen an beiden Seiten",
                    "Inhalt: Aufruf: methodenname(parameter)"
                ],
                "grafik": "Rechteck mit vertikalen Randlinien"
            }
        }
    
    def _initialisiere_pattern_templates(self) -> Dict[str, str]:
        """Initialisiert wiederverwendbare Pattern-Templates"""
        return {
            "array_durchlaufen": """Zähle i von 0 bis Anzahl der Elemente des Arrays array - 1, Schrittweite 1
     [Verarbeitung mit array[i]]""",
            
            "summe_berechnen": """Deklaration und Initialisierung: summe = 0
Zähle i von 0 bis Anzahl der Elemente des Arrays zahlen - 1, Schrittweite 1
     Zuweisung: summe = summe + zahlen[i]
Ausgabe: summe""",
            
            "maximum_finden": """Zuweisung: maximum = array[0]
Zähle i von 1 bis Anzahl der Elemente des Arrays array - 1, Schrittweite 1
     Wenn array[i] > maximum, dann
          J
               Zuweisung: maximum = array[i]
          , sonst
          N
               [keine Anweisung]
Rückgabe: maximum""",
            
            "lineare_suche": """Deklaration und Initialisierung: gefunden = Falsch
Deklaration und Initialisierung: index = 0
Wiederhole solange index < Anzahl der Elemente des Arrays array AND NOT gefunden
     Wenn array[index] == suchWert, dann
          J
               Zuweisung: gefunden = Wahr
          , sonst
          N
               Zuweisung: index = index + 1
Wenn gefunden, dann
     J
          Ausgabe: "Gefunden an Position " + index
     , sonst
     N
          Ausgabe: "Nicht gefunden" """
        }
    
    def _initialisiere_grafik_formen(self) -> Dict[str, dict]:
        """Initialisiert die grafischen Formen für Draw.io"""
        return {
            "anweisung": {
                "name": "Anweisung (Prozess)",
                "shape": "rectangle",
                "beschreibung": "Rechteck für Anweisungen",
                "verwendung": ["Deklaration", "Zuweisung", "Ausgabe", "etc."]
            },
            "alternative": {
                "name": "Alternative (Verzweigung)",
                "shape": "triangle_in_rectangle",
                "beschreibung": "Rechteck mit eingebettetem gleichschenkligem Dreieck",
                "details": {
                    "dreieck": "Spitze nach unten, Hypotenuse oben",
                    "bedingung": "Im Dreieck angebracht",
                    "j_zweig": "Links unten nach Dreieck",
                    "n_zweig": "Rechts unten nach Dreieck"
                }
            },
            "schleife": {
                "name": "Schleife (While/For)",
                "shape": "inverted_l",
                "beschreibung": "Umgedrehtes L (horizontal gespiegelt)",
                "details": {
                    "kopf": "Horizontaler Kasten oben",
                    "linie": "Vertikale Linie links vom Kopf",
                    "koerper": "Darunter eingerückt"
                }
            },
            "aufruf": {
                "name": "Aufruf (Funktionsaufruf)",
                "shape": "rectangle_with_sidebars",
                "beschreibung": "Rechteck mit vertikalen Strichen an den Seiten",
                "details": {
                    "kennzeichnung": "Vertikale Striche links und rechts"
                }
            }
        }
    
    # ===== PUBLIC API =====
    
    def get_operator(self, name: str) -> Optional[OperatorDefinition]:
        """Gibt die Definition eines Operators zurück"""
        return self._operatoren.get(name.lower().replace(" ", "_"))
    
    def get_all_operators(self) -> Dict[str, OperatorDefinition]:
        """Gibt alle Operator-Definitionen zurück"""
        return self._operatoren.copy()
    
    def get_operators_by_kategorie(self, kategorie: OperatorKategorie) -> List[OperatorDefinition]:
        """Gibt alle Operatoren einer Kategorie zurück"""
        return [op for op in self._operatoren.values() if op.kategorie == kategorie]
    
    def get_notation_regel(self, name: str) -> Optional[dict]:
        """Gibt eine Notation-Regel zurück"""
        return self._notation_regeln.get(name)
    
    def get_all_notation_regeln(self) -> Dict[str, dict]:
        """Gibt alle Notation-Regeln zurück"""
        return self._notation_regeln.copy()
    
    def get_pattern_template(self, name: str) -> Optional[str]:
        """Gibt ein Pattern-Template zurück"""
        return self._pattern_templates.get(name)
    
    def get_all_pattern_templates(self) -> Dict[str, str]:
        """Gibt alle Pattern-Templates zurück"""
        return self._pattern_templates.copy()
    
    def get_grafik_form(self, name: str) -> Optional[dict]:
        """Gibt die Definition einer grafischen Form zurück"""
        return self._grafik_formen.get(name)
    
    def get_all_grafik_formen(self) -> Dict[str, dict]:
        """Gibt alle grafischen Formen zurück"""
        return self._grafik_formen.copy()
    
    def validate_operator_syntax(self, operator_name: str, syntax_string: str) -> Tuple[bool, Optional[str]]:
        """
        Validiert, ob eine Syntax-String einem Operator entspricht
        
        Args:
            operator_name: Name des Operators (z.B. "deklaration")
            syntax_string: Zu validierende Syntax (z.B. "Deklaration: alter als Ganzzahl")
        
        Returns:
            (ist_gültig, fehler_nachricht)
        """
        operator = self.get_operator(operator_name)
        if not operator:
            return False, f"Unbekannter Operator: {operator_name}"
        
        # Einfache Validierung: prüfe ob der Operator-Name im String vorkommt
        if operator.name in syntax_string:
            return True, None
        else:
            return False, f"Syntax entspricht nicht dem Operator '{operator.name}'"
    
    def get_beispiel_struktogramm(self, pattern_name: str) -> Optional[str]:
        """
        Gibt ein vollständiges Beispiel-Struktogramm für ein Pattern zurück
        
        Args:
            pattern_name: Name des Patterns (z.B. "array_durchlaufen")
        
        Returns:
            Struktogramm-Code oder None
        """
        return self.get_pattern_template(pattern_name)
    
    def export_knowledge_summary(self) -> str:
        """
        Exportiert eine Zusammenfassung der gesamten Wissensdatenbank
        
        Returns:
            Markdown-formatierte Zusammenfassung
        """
        summary = f"""# Struktogramm Knowledge Base - Zusammenfassung

**Version:** {self.VERSION}
**Quelle:** {self.QUELLE}
**Stand:** {self.DATUM}

## Statistik

- **Operatoren:** {len(self._operatoren)}
- **Notation-Regeln:** {len(self._notation_regeln)}
- **Pattern-Templates:** {len(self._pattern_templates)}
- **Grafik-Formen:** {len(self._grafik_formen)}

## Operatoren nach Kategorien

"""
        for kategorie in OperatorKategorie:
            ops = self.get_operators_by_kategorie(kategorie)
            summary += f"### {kategorie.value} ({len(ops)})\n\n"
            for op in ops:
                summary += f"- **{op.name}**: `{op.syntax}`\n"
            summary += "\n"
        
        summary += "## Notation-Regeln\n\n"
        for name, regel in self._notation_regeln.items():
            summary += f"- **{regel['name']}**\n"
        
        summary += "\n## Pattern-Templates\n\n"
        for name in self._pattern_templates.keys():
            summary += f"- {name}\n"
        
        return summary


# ===== SINGLETON INSTANCE =====
# Diese Instanz sollte im gesamten Projekt verwendet werden
_knowledge_base_instance = None

def get_knowledge_base() -> StruktogrammKnowledgeBase:
    """
    Gibt die Singleton-Instanz der Wissensdatenbank zurück
    
    Returns:
        StruktogrammKnowledgeBase-Instanz
    """
    global _knowledge_base_instance
    if _knowledge_base_instance is None:
        _knowledge_base_instance = StruktogrammKnowledgeBase()
    return _knowledge_base_instance


# ===== CONVENIENCE FUNCTIONS =====

def get_operator_syntax(operator_name: str) -> Optional[str]:
    """Schnellzugriff: Syntax eines Operators"""
    kb = get_knowledge_base()
    op = kb.get_operator(operator_name)
    return op.syntax if op else None


def get_pattern(pattern_name: str) -> Optional[str]:
    """Schnellzugriff: Pattern-Template"""
    kb = get_knowledge_base()
    return kb.get_pattern_template(pattern_name)


def validate_bw_notation(syntax_string: str, expected_operator: str) -> bool:
    """Schnellzugriff: Validierung gegen BW-Standard"""
    kb = get_knowledge_base()
    is_valid, _ = kb.validate_operator_syntax(expected_operator, syntax_string)
    return is_valid


# ===== BEISPIEL-VERWENDUNG =====
if __name__ == "__main__":
    # Beispiel: Wissensdatenbank verwenden
    kb = get_knowledge_base()
    
    # Operator abrufen
    deklaration = kb.get_operator("deklaration")
    print(f"Operator: {deklaration.name}")
    print(f"Syntax: {deklaration.syntax}")
    print(f"Beispiel: {deklaration.beispiel}")
    print()
    
    # Pattern-Template abrufen
    pattern = kb.get_pattern_template("array_durchlaufen")
    print("Pattern 'Array durchlaufen':")
    print(pattern)
    print()
    
    # Notation-Regel abrufen
    regel = kb.get_notation_regel("briefumschlag_alternative")
    print(f"Notation: {regel['name']}")
    print("Template:")
    print(regel['template'])
    print()
    
    # Zusammenfassung exportieren
    summary = kb.export_knowledge_summary()
    print(summary)
