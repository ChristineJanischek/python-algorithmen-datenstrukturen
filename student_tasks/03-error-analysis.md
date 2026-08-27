# Aufgabe 03: Fehlerklassifikation

**Typ:** Erweiterungsaufgabe  
**Schwierigkeit:** ⭐⭐⭐  
**Empfohlener Branch:** `feature/aufgabe-03-error-analysis`

---

## Ausgangssituation

Der Lernagent nimmt Eingaben entgegen, prüft sie aber nur auf Sicherheitsprobleme.
Er unterscheidet noch nicht, ob eine Eingabe eine Frage, ein Lösungsversuch oder
ein fehlerhafter Codeabschnitt ist.

Eine bessere Klassifikation ermöglicht gezieltere didaktische Reaktionen.

## Lernziel

Du kannst Texteingaben automatisch klassifizieren und auf Basis dieser Klassifikation
unterschiedliche Antwortstrategien auswählen.

## Fachlicher Hintergrund

In der Lernforschung werden Fehler in verschiedene Kategorien eingeteilt:

- **Syntaxfehler:** Grammatikalisch falscher Code (fehlendes `:`, falsche Einrückung)
- **Verständnisfehler:** Das Konzept wurde falsch verstanden (z.B. Index beginnt bei 1)
- **Strategiefehler:** Der richtige Ansatz fehlt (falscher Algorithmus gewählt)

Für jeden Fehlertyp ist eine andere Reaktion sinnvoll.

## Aufgabe

**Neue Datei:** `src/learning_agent/learning/error_classifier.py`

Implementiere folgende Klassen und Funktionen:

```python
from enum import Enum

class EingabeTyp(Enum):
    FRAGE = "frage"           # Enthält ein Fragezeichen oder Fragewörter
    CODE_VERSUCH = "code"     # Enthält Python-Code-Elemente
    RATLOSIGKEIT = "ratlos"   # Signale der Ratlosigkeit
    SONSTIGES = "sonstiges"

class FehlerTyp(Enum):
    SYNTAX = "syntax"
    VERSTAENDNIS = "verstaendnis"
    STRATEGIE = "strategie"
    KEIN_FEHLER = "kein_fehler"

def klassifiziere_eingabe(text: str) -> EingabeTyp:
    """Klassifiziert die Art der Eingabe.
    
    TODO: Implementiere die Klassifikation anhand von Schlüsselwörtern.
    Eingabe: text (str)
    Ausgabe: EingabeTyp
    
    Hinweis: Schlüsselwörter für FRAGE: "wie", "was", "warum", "?"
    Hinweis: Schlüsselwörter für CODE: "def", "for", "if", "=", "print"
    Hinweis: Schlüsselwörter für RATLOSIGKEIT: "weiß nicht", "keine ahnung"
    """
    raise NotImplementedError("TODO: Aufgabe 03")

def erkenne_fehlertyp(code_text: str) -> FehlerTyp:
    """Erkennt den Typ eines Fehlers in einer Code-Eingabe.
    
    TODO: Implementiere einfache Heuristiken:
    - Fehlende Doppelpunkte nach if/for/while → SYNTAX
    - Index-Zugriff mit 1 als erstes Element → VERSTAENDNIS
    - Bubble Sort auf eine Suche angewendet → STRATEGIE
    
    Eingabe: code_text (str) – ein Code-Versuch als Text
    Ausgabe: FehlerTyp
    """
    raise NotImplementedError("TODO: Aufgabe 03")
```

## Betroffene Dateien

- `src/learning_agent/learning/error_classifier.py` (neu anlegen)
- `tests/learning_agent/test_error_classifier.py` (neu anlegen)

## Technische Anforderungen

- Beide Funktionen müssen vollständig implementiert sein.
- Mindestens 6 Testfälle.
- Die Klassifikation darf nur auf Text-Analyse basieren (kein KI-Aufruf).

## Akzeptanzkriterien

- [ ] `EingabeTyp` und `FehlerTyp` sind als Enums definiert.
- [ ] `klassifiziere_eingabe` erkennt alle vier Typen.
- [ ] `erkenne_fehlertyp` erkennt mindestens zwei Fehlertypen.
- [ ] Alle Tests bestehen.
- [ ] Neue Typen sind im `__init__.py` des `learning`-Pakets exportiert.

## Reflexionsfragen

1. Welche Grenzen hat eine rein keyword-basierte Fehlerklassifikation?
2. Wie könnten mehr Schüler-Eingaben gesammelt werden, um die Klassifikation zu verbessern?
3. Welche ethischen Aspekte muss man bedenken, wenn Fehler automatisch klassifiziert werden?

## Optionale Erweiterung

Verbinde die Fehlerklassifikation mit dem Agenten: Wenn ein Syntaxfehler erkannt wird,
soll der Agent automatisch Hilfestufe 2 verwenden und den Fehlertyp benennen.
