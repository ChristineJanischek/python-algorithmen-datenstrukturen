---
titel: "[TITEL DER LÖSUNG]"
level: L1  # L1, L2 oder L3
kategorie: 1  # 1=Grundlagen, 2=Sortieren, 3=Suchen, 4=Vertiefung, etc.
nummer: 1  # Laufende Nummer (muss mit Aufgabe übereinstimmen)
autor: "[DEIN NAME]"
datum: 05.02.2026
version: 1.0
---

# Lösung: [TITEL DER LÖSUNG]

## 📋 Übersicht

- **Level:** [L1/L2/L3]
- **Kategorie:** [Nummer]
- **Komplexität:** [O-Notation]

## 💡 Lösungsansatz

[Beschreibung des Lösungsansatzes - wie gehen wir vor?]

**Strategie:**
1. [Schritt 1]
2. [Schritt 2]
3. [Schritt 3]
4. [Schritt 4]

[Warum ist dieser Ansatz sinnvoll?]

## 📊 Struktogramm

```
[Hier das Struktogramm nach BW-Standard einfügen]
[Sollte identisch oder ähnlich zur Aufgabe sein]

Beispiel:
Deklaration und Initialisierung: summe = 0
Deklaration und Initialisierung: n = Anzahl der Elemente des Arrays zahlen
Zähle i von 0 bis n - 1, Schrittweite 1
    Zuweisung: summe = summe + zahlen[i]
Ausgabe: "Summe: " + summe
```

## 💻 Python-Implementierung

### Vollständige Lösung

```python
def <funktionsname>(parameter_typ) -> rückgabetyp:
    """
    [Docstring - Beschreibung der Funktion]
    
    Args:
        parameter: [Beschreibung]
        
    Returns:
        [Beschreibung des Rückgabewerts]
    """
    # [Implementierung]
    [Code]
    
    return [ergebnis]


# Hauptprogramm
if __name__ == "__main__":
    # Test der Funktion
    [Test-Code]
```

### Schrittweise Erklärung

**Schritt 1: [Beschreibung]**
```python
[Code für Schritt 1]
```
[Erklärung]

**Schritt 2: [Beschreibung]**
```python
[Code für Schritt 2]
```
[Erklärung]

**Schritt 3: [Beschreibung]**
```python
[Code für Schritt 3]
```
[Erklärung]

## 📝 Erklärung

### Wie funktioniert die Lösung?

[Detaillierte Erklärung der Logik]

### Wichtige Code-Stellen

**[Code-Stelle 1]:**
```python
[Code-Ausschnitt]
```
[Erklärung was hier passiert]

**[Code-Stelle 2]:**
```python
[Code-Ausschnitt]
```
[Erklärung was hier passiert]

### Besonderheiten

- [Besonderheit 1]
- [Besonderheit 2]
- [Besonderheit 3]

## ⏱️ Komplexitätsanalyse

### Zeitkomplexität

**Best Case:** O([notation])
- [Beschreibung wann das auftritt]

**Average Case:** O([notation])
- [Beschreibung des durchschnittlichen Falls]

**Worst Case:** O([notation])
- [Beschreibung wann das auftritt]

### Speicherkomplexität

**O([notation])**
- [Erklärung des Speicherbedarfs]

### Zusammenfassung

[Gesamtbewertung der Komplexität]

## ✅ Test-Ausgaben

### Test 1
**Eingabe:**
```
[Eingabe]
```
**Ausgabe:**
```
[Ausgabe]
```
✅ Erfolgreich

### Test 2
**Eingabe:**
```
[Eingabe]
```
**Ausgabe:**
```
[Ausgabe]
```
✅ Erfolgreich

### Test 3
**Eingabe:**
```
[Eingabe]
```
**Ausgabe:**
```
[Ausgabe]
```
✅ Erfolgreich

## 🔄 Alternative Lösungen

### Alternative 1: [Titel]

[Beschreibung des alternativen Ansatzes]

```python
def <alternative_funktion>(parameter):
    [alternativer Code]
    return [ergebnis]
```

**Vorteile:**
- [Vorteil 1]
- [Vorteil 2]

**Nachteile:**
- [Nachteil 1]
- [Nachteil 2]

**Komplexität:** O([notation])

### Alternative 2: [Titel]

[Beschreibung des zweiten alternativen Ansatzes]

```python
def <alternative_funktion2>(parameter):
    [alternativer Code]
    return [ergebnis]
```

**Vorteile:**
- [Vorteil 1]
- [Vorteil 2]

**Nachteile:**
- [Nachteil 1]
- [Nachteil 2]

**Komplexität:** O([notation])

## 💡 Zusätzliche Hinweise

### Häufige Fehler

❌ **Fehler 1:** [Beschreibung]
```python
[Falscher Code]
```
✅ **Richtig:**
```python
[Richtiger Code]
```

❌ **Fehler 2:** [Beschreibung]
```python
[Falscher Code]
```
✅ **Richtig:**
```python
[Richtiger Code]
```

### Verbesserungsmöglichkeiten

- [Verbesserung 1]
- [Verbesserung 2]
- [Verbesserung 3]

### Best Practices

- [Best Practice 1]
- [Best Practice 2]
- [Best Practice 3]

## 🔗 Verwandte Themen

- [Verwandtes Thema 1]
- [Verwandtes Thema 2]
- [Verwandtes Thema 3]

## 📚 Weiterführende Ressourcen

- Link zur Aufgabe: ../aufgaben/<Level>/<Dateiname>.md
- Link zur Information: ../information/<Level>/<Dateiname>.md
- Struktogramm: ../../struktogramme/<Dateiname>.stgr

---

*Erstellt am [Datum] von [Autor]*

---

## 📝 Verwendungshinweis

**Dieses Template NICHT direkt verwenden!**

Stattdessen mit Python Manager erstellen:

```python
from src.utils.elearning_manager import *

manager = ELearningManager()

loesung = create_loesung_quick(
    titel="Titel der Lösung",
    level=Level.L1,
    kategorie=1,
    nummer=1,
    loesungsansatz="Beschreibung...",
    python_code="def ...",
    autor="Dein Name"
)

# Optional: Details hinzufügen
loesung.struktogramm = "..."
loesung.erklaerung = "..."
loesung.komplexitaet = "O(n)"
loesung.alternative_loesungen = [
    ("Alternative 1", "code..."),
    ("Alternative 2", "code...")
]
loesung.hinweise = "..."

manager.save_loesung(loesung)
```

Siehe: `docs/handbuch/ELEARNING_TEMPLATE_GUIDE.md`

<!-- CUSTOM_LICENSE_NOTICE_START -->
## License

This repository is licensed under a custom license.

- Attribution required: Christine Janischek - https://emotionalspirit.de
- Non-commercial use only
- Use only within state school systems
- Any other use requires explicit prior written permission
<!-- CUSTOM_LICENSE_NOTICE_END -->
