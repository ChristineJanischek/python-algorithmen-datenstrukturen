# E-Learning Template Guide

**Version:** 1.0  
**Letzte Aktualisierung:** 05.02.2026  
**Zweck:** Standardisierte Erstellung von E-Learning-Materialien

## Übersicht

Dieser Guide beschreibt, wie E-Learning-Inhalte (Aufgaben, Informationen, Lösungen) konsistent erstellt und verwaltet werden.

## Automatisches System

### Python E-Learning Manager

Das Repository enthält einen vollautomatischen Manager für E-Learning-Inhalte:

```python
from src.utils.elearning_manager import (
    ELearningManager,
    create_aufgabe_quick,
    create_information_quick,
    create_loesung_quick,
    Level
)
```

**Vorteile:**
- ✅ Automatische Dateinamens-Generierung
- ✅ YAML-Frontmatter für Metadaten
- ✅ Konsistentes Markdown-Format
- ✅ Automatische INDEX-Generierung
- ✅ Validierung vor dem Speichern

---

## Dateistruktur

### Verzeichnisse

```
docs/                                            
├── aufgaben/           # Aufgabenstellungen     
│   ├── L1/            # Grundlagen              
│   ├── L2/            # Fortgeschritten         
│   ├── L3/            # Expert                  
│   └── INDEX.md       # Automatisch generiert   
├── information/        # Informationsmaterialien
│   ├── L1/                                      
│   ├── L2/                                      
│   ├── L3/                                      
│   └── INDEX.md                                 
├── loesungen/          # Lösungen               
│   ├── L1/                                      
│   ├── L2/                                      
│   ├── L3/                                      
│   └── INDEX.md                                 
└── handbuch/           # Guides & Dokumentation 
```

### Namenskonvention

**Format:** `LX_Y_Z_Thema.md`

- **X** = Level (1-3)
  - L1: Grundlagen (Sequenz, einfache Verzweigung/Schleifen)
  - L2: Fortgeschritten (Arrays, Such-/Sortieralgorithmen)
  - L3: Expert (Komplexe Datenstrukturen, Rekursion)

- **Y** = Kategorie
  - 1: Grundlagen
  - 2: Sortieralgorithmen
  - 3: Suchalgorithmen
  - 4: Vertiefung
  - 5: Datenstrukturen
  - etc.

- **Z** = Laufende Nummer innerhalb der Kategorie

- **Thema** = Beschreibender Name (Underscores statt Leerzeichen)

**Beispiele:**
- `L1_1_1_Variablen_und_Datentypen.md`
- `L2_2_1_Bubble_Sort.md`
- `L2_3_2_Binaere_Suche.md`
- `L3_5_1_Verkettete_Listen.md`

---

## Metadaten (YAML Frontmatter)

Jede Datei beginnt mit YAML-Frontmatter:

```yaml
---
titel: "Array-Summe berechnen"
level: L1
kategorie: 3
nummer: 1
autor: "Max Mustermann"
datum: 05.02.2026
version: 1.0
themen:
  - Arrays
  - Schleifen
  - Summierung
lernziele:
  - Array durchlaufen können
  - Summe akkumulieren können
voraussetzungen:
  - Grundlagen Arrays
  - For-Schleifen
zeitaufwand: "15 Minuten"
schwierigkeitsgrad: "Einfach"
---
```

**Pflichtfelder:**
- titel
- level
- kategorie
- nummer
- autor
- datum

**Optionale Felder:**
- version
- themen
- lernziele
- voraussetzungen
- zeitaufwand
- schwierigkeitsgrad

---

## Content-Typen

### 1. Aufgaben

**Struktur einer Aufgabe:**

```markdown
---
[YAML Frontmatter]
---

# Aufgabe: [Titel]

## 📋 Übersicht
- Level, Kategorie, Zeitaufwand
- Themen
- Lernziele
- Voraussetzungen

## 📝 Problemstellung
[Beschreibung der Aufgabe]

## 📊 Struktogramm
```
[Struktogramm nach BW-Standard]
```

## 💡 Hinweise
[Optional: Hilfreiche Tipps]

## 🧪 Beispiel
**Eingabe:**
```
[Beispiel-Eingabe]
```

**Erwartete Ausgabe:**
```
[Beispiel-Ausgabe]
```

## ✅ Testfälle
### Test 1
**Eingabe:** ...
**Ausgabe:** ...

## 🔥 Zusatzaufgaben
1. [Erweiterung 1]
2. [Erweiterung 2]

---
*Erstellt am [Datum] von [Autor]*
```

**Mit Python erstellen:**

```python
from src.utils.elearning_manager import (
    ELearningManager, 
    create_aufgabe_quick,
    Level
)

# Manager initialisieren
manager = ELearningManager()

# Aufgabe erstellen
aufgabe = create_aufgabe_quick(
    titel="Meine Aufgabe",
    level=Level.L1,
    kategorie=3,
    nummer=1,
    problemstellung="Beschreibung...",
    autor="Dein Name"
)

# Optional: Details hinzufügen
aufgabe.metadata.themen = ["Arrays", "Schleifen"]
aufgabe.metadata.lernziele = ["Ziel 1", "Ziel 2"]
aufgabe.metadata.zeitaufwand = "20 Minuten"
aufgabe.struktogramm = "..."
aufgabe.beispiel_eingabe = "..."
aufgabe.beispiel_ausgabe = "..."

# Speichern
manager.save_aufgabe(aufgabe)
```

---

### 2. Informationen

**Struktur einer Information:**

```markdown
---
[YAML Frontmatter]
---

# Information: [Titel]

## 📚 Übersicht
- Level, Kategorie, Lesezeit
- Themen
- Voraussetzungen

## 🎯 Einführung
[Kurze Einführung ins Thema]

## 📖 Inhalt
[Hauptinhalt der Information]

## 💡 Beispiele
[Praktische Beispiele]

## 📝 Zusammenfassung
[Zusammenfassung der wichtigsten Punkte]

## 🔗 Weiterführende Themen
- [Thema 1]
- [Thema 2]

## 📚 Ressourcen
- [Link/Referenz 1]
- [Link/Referenz 2]

---
*Erstellt am [Datum] von [Autor]*
```

**Mit Python erstellen:**

```python
from src.utils.elearning_manager import (
    ELearningManager,
    create_information_quick,
    Level
)

manager = ELearningManager()

info = create_information_quick(
    titel="Meine Information",
    level=Level.L1,
    kategorie=1,
    nummer=1,
    einfuehrung="Einführung...",
    inhalt="Hauptinhalt...",
    autor="Dein Name"
)

# Optional: Details hinzufügen
info.metadata.themen = ["Thema1", "Thema2"]
info.metadata.zeitaufwand = "10 Minuten"
info.beispiele = "..."
info.zusammenfassung = "..."

manager.save_information(info)
```

---

### 3. Lösungen

**Struktur einer Lösung:**

```markdown
---
[YAML Frontmatter]
---

# Lösung: [Titel]

## 📋 Übersicht
- Level, Kategorie
- Komplexität

## 💡 Lösungsansatz
[Beschreibung des Ansatzes]

## 📊 Struktogramm
```
[Struktogramm nach BW-Standard]
```

## 💻 Python-Implementierung
```python
[Python-Code]
```

## 📝 Erklärung
[Detaillierte Erklärung der Lösung]

## ⏱️ Komplexitätsanalyse
[Zeit- und Speicherkomplexität]

## 🔄 Alternative Lösungen
### Alternative 1: [Titel]
```python
[Code]
```

## 💡 Zusätzliche Hinweise
[Weitere Tipps und Hinweise]

---
*Erstellt am [Datum] von [Autor]*
```

**Mit Python erstellen:**

```python
from src.utils.elearning_manager import (
    ELearningManager,
    create_loesung_quick,
    Level
)

manager = ELearningManager()

loesung = create_loesung_quick(
    titel="Meine Lösung",
    level=Level.L1,
    kategorie=3,
    nummer=1,
    loesungsansatz="Ansatz...",
    python_code="def ...",
    autor="Dein Name"
)

# Optional: Details hinzufügen
loesung.struktogramm = "..."
loesung.erklaerung = "..."
loesung.komplexitaet = "O(n)"

manager.save_loesung(loesung)
```

---

## Workflows

### Workflow 1: Neue Aufgabe mit Lösung erstellen

```python
from src.utils.elearning_manager import *

manager = ELearningManager()

# 1. Aufgabe erstellen
aufgabe = create_aufgabe_quick(
    titel="Maximum finden",
    level=Level.L1,
    kategorie=3,
    nummer=5,
    problemstellung="Finde das größte Element in einem Array.",
    autor="Dein Name",
    struktogramm="..."  # Aus Pattern oder manuell
)

aufgabe.metadata.themen = ["Arrays", "Maximum"]
aufgabe.metadata.lernziele = ["Maximum-Suche implementieren"]
aufgabe.beispiel_eingabe = "[3, 7, 2, 9, 1]"
aufgabe.beispiel_ausgabe = "Maximum: 9"

manager.save_aufgabe(aufgabe)

# 2. Lösung erstellen (gleiche Metadaten)
loesung = create_loesung_quick(
    titel="Maximum finden",
    level=Level.L1,
    kategorie=3,
    nummer=5,
    loesungsansatz="Initialisiere max mit erstem Element, vergleiche mit allen anderen.",
    python_code="""def finde_maximum(zahlen):
    max_wert = zahlen[0]
    for zahl in zahlen[1:]:
        if zahl > max_wert:
            max_wert = zahl
    return max_wert""",
    autor="Dein Name",
    struktogramm="..."
)

loesung.komplexitaet = "O(n) - Lineare Zeitkomplexität"

manager.save_loesung(loesung)

# 3. Indices aktualisieren
manager.generate_all_indices()
```

---

### Workflow 2: Information mit verknüpften Aufgaben

```python
# 1. Information erstellen
info = create_information_quick(
    titel="Bubble Sort",
    level=Level.L2,
    kategorie=2,
    nummer=1,
    einfuehrung="Bubble Sort ist ein einfacher Sortieralgorithmus...",
    inhalt="...",
    autor="Dein Name"
)

info.metadata.themen = ["Sortieren", "Algorithmen"]
info.weiterführende_themen = [
    "Selection Sort",
    "Komplexität von Sortieralgorithmen"
]
info.ressourcen = [
    ("Struktogramm", "../../struktogramme/L2_2_1_3_Struktogramm_Bubble_Sort.stgr"),
    ("Aufgabe Bubble Sort", "../aufgaben/L2/L2_2_1_Bubble_Sort.md")
]

manager.save_information(info)
```

---

## INDEX-Dateien

INDEX-Dateien werden automatisch generiert und sollten nicht manuell bearbeitet werden.

**Automatische Generierung:**

```python
from src.utils.elearning_manager import ELearningManager, ContentType, Level

manager = ELearningManager()

# Alle Indices generieren
manager.generate_all_indices()

# Oder spezifisch
manager.generate_index(ContentType.AUFGABE)
manager.generate_index(ContentType.AUFGABE, Level.L1)
```

**INDEX-Struktur:**

```markdown
# Aufgaben - L1

*Automatisch generiert am 05.02.2026 14:30*

**Anzahl Dateien:** 15

## L1

- L1_3_1_Array-Summe_berechnen (L1/L1_3_1_Array-Summe_berechnen.md)
- INDEX (L1/INDEX.md)
...
```

---

## Best Practices

### ✅ DO

1. **Immer Python Manager verwenden** für neue Inhalte
2. **Metadaten vollständig ausfüllen** (mindestens Pflichtfelder)
3. **Struktogramme nach BW-Standard** einbinden
4. **Konsistente Namenskonvention** einhalten
5. **Beispiele und Testfälle** bereitstellen
6. **Indices nach Änderungen** regenerieren
7. **Lernziele konkret** formulieren
8. **Zeitaufwand realistisch** schätzen

### ❌ DON'T

1. **Nicht manuell** Dateinamen vergeben
2. **Nicht ohne Frontmatter** speichern
3. **Nicht INDEX-Dateien** manuell editieren
4. **Nicht inkonsistente Formate** verwenden
5. **Nicht Level/Kategorie/Nummer** falsch zuordnen
6. **Nicht ohne Struktogramm** (bei Logik-Aufgaben)
7. **Nicht unverständliche** Problemstellungen

---

## Validierung

Vor dem Commit validieren:

```python
from src.utils.elearning_manager import ELearningManager
from pathlib import Path

manager = ELearningManager()

# Einzelne Datei validieren
errors = manager.validate_content(
    Path("docs/aufgaben/L1/L1_3_1_Array-Summe_berechnen.md")
)

if errors:
    print("Fehler gefunden:")
    for error in errors:
        print(f"  - {error}")
else:
    print("✅ Datei ist valide")
```

---

## Templates

Templates sind verfügbar unter:
- `docs/aufgaben/TEMPLATE_Aufgabe.md`
- `docs/information/TEMPLATE_Information.md`
- `docs/loesungen/TEMPLATE_Loesung.md`

**Verwendung:**
1. Template kopieren
2. Platzhalter ersetzen
3. Mit Python Manager speichern (für korrekte Metadaten)

---

## Kategorien-Übersicht

| Kategorie | Beschreibung | Beispiele |
|-----------|--------------|-----------|
| 1 | Grundlagen | Variablen, Datentypen, I/O |
| 2 | Sortieralgorithmen | Bubble Sort, Selection Sort |
| 3 | Suchalgorithmen | Lineare Suche, Binäre Suche |
| 4 | Vertiefung | Komplexe Aufgaben, Kombinationen |
| 5 | Datenstrukturen | Listen, Stacks, Queues |
| 6 | Rekursion | Rekursive Algorithmen |
| 7 | Objektorientierung | Klassen, Objekte |

---

## Beispiel: Komplette Aufgabe

```python
from src.utils.elearning_manager import *
from src.utils.struktogramm_helper import pattern_lineare_suche

# Manager initialisieren
manager = ELearningManager()

# Struktogramm aus Pattern
struktogramm = pattern_lineare_suche("namen", "suchName")

# Aufgabe erstellen
aufgabe = ELearningAufgabe(
    metadata=ELearningMetadata(
        titel="Lineare Suche in Namen-Array",
        level=Level.L2,
        kategorie=3,
        nummer=1,
        autor="Max Mustermann",
        themen=["Lineare Suche", "Arrays", "Strings"],
        lernziele=[
            "Lineare Suche implementieren können",
            "Mit String-Arrays arbeiten können",
            "Rückgabewerte interpretieren können"
        ],
        voraussetzungen=[
            "Arrays durchlaufen können",
            "Verzweigungen verstehen"
        ],
        zeitaufwand="20 Minuten",
        schwierigkeitsgrad="Mittel"
    ),
    problemstellung="""Implementiere eine lineare Suche, die in einem Array von Namen
nach einem bestimmten Namen sucht.

Das Programm soll:
1. Ein Array mit Namen enthalten
2. Den Benutzer nach einem Suchnamen fragen
3. Linear durch das Array suchen
4. Die Position ausgeben (oder -1 wenn nicht gefunden)""",
    struktogramm=struktogramm,
    hinweise="""- Verwende eine Schleife zum Durchlaufen
- Vergleiche mit == für String-Vergleich
- Denke an den Fall "nicht gefunden" """,
    beispiel_eingabe="Clara",
    beispiel_ausgabe="Gefunden an Position: 2",
    testfaelle=[
        ("Anna", "Gefunden an Position: 0"),
        ("David", "Nicht gefunden"),
        ("Clara", "Gefunden an Position: 2")
    ],
    zusatzaufgaben=[
        "Erweitere die Suche um Groß-/Kleinschreibung zu ignorieren",
        "Zähle wie viele Vergleiche notwendig waren"
    ]
)

# Speichern
manager.save_aufgabe(aufgabe)

# Lösung erstellen
loesung = ELearningLoesung(
    metadata=aufgabe.metadata,  # Gleiche Metadaten
    loesungsansatz="""Wir durchlaufen das Array sequenziell und vergleichen
jedes Element mit dem gesuchten Namen. Sobald eine Übereinstimmung gefunden wird,
geben wir die Position zurück.""",
    struktogramm=struktogramm,
    python_code="""def lineare_suche(namen, such_name):
    for i in range(len(namen)):
        if namen[i] == such_name:
            return i
    return -1

# Test
namen = ["Anna", "Ben", "Clara", "David"]
such_name = input("Name eingeben: ")
position = lineare_suche(namen, such_name)

if position != -1:
    print(f"Gefunden an Position: {position}")
else:
    print("Nicht gefunden")""",
    erklaerung="""Die Funktion durchläuft das Array mit einer for-Schleife.
Bei jeder Iteration wird das aktuelle Element mit dem gesuchten Namen verglichen.
Wenn eine Übereinstimmung gefunden wird, wird sofort die Position (Index) zurückgegeben.
Falls die Schleife komplett durchlaufen wird ohne Fund, wird -1 zurückgegeben.""",
    komplexitaet="""**Zeitkomplexität:** O(n)
- Best Case: O(1) - Element am Anfang
- Average Case: O(n/2) ≈ O(n)
- Worst Case: O(n) - Element am Ende oder nicht vorhanden

**Speicherkomplexität:** O(1) - Konstanter zusätzlicher Speicher"""
)

# Speichern
manager.save_loesung(loesung)

# Indices aktualisieren
manager.generate_all_indices()

print("✅ Aufgabe und Lösung erfolgreich erstellt!")
```

---

## Integration mit Struktogrammen

Struktogramme automatisch einbinden:

```python
from src.utils.struktogramm_helper import (
    pattern_array_durchlaufen,
    pattern_summe_berechnen,
    pattern_maximum_finden,
    pattern_lineare_suche
)

# Struktogramm aus Pattern verwenden
struktogramm = pattern_summe_berechnen("zahlen", "summe")

aufgabe = create_aufgabe_quick(
    titel="...",
    # ...
    struktogramm=struktogramm
)
```

Oder StruktogrammBuilder verwenden:

```python
from src.utils.struktogramm_helper import StruktogrammBuilder

builder = StruktogrammBuilder()
builder.dekl_init("summe", "0")
builder.zaehle_start("i", "0", "n-1")
builder.zuweisung("summe", "summe + zahlen[i]")
builder.schleife_ende()

struktogramm = builder.build()
```

---

## Für andere Lehrkräfte

### Schnellstart

1. **Repository klonen/pullen**

2. **Python-Umgebung aktivieren**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # oder
   venv\Scripts\activate  # Windows
   ```

3. **Beispiel-Skript erstellen** (`meine_aufgabe.py`)
   ```python
   from src.utils.elearning_manager import *
   
   manager = ELearningManager()
   
   aufgabe = create_aufgabe_quick(
       titel="Meine erste Aufgabe",
       level=Level.L1,
       kategorie=1,
       nummer=1,
       problemstellung="...",
       autor="Dein Name"
   )
   
   manager.save_aufgabe(aufgabe)
   manager.generate_all_indices()
   ```

4. **Ausführen**
   ```bash
   python meine_aufgabe.py
   ```

5. **Ergebnis prüfen**
   ```bash
   ls docs/aufgaben/L1/
   cat docs/aufgaben/INDEX.md
   ```

6. **Committen**
   ```bash
   git add docs/
   git commit -m "Add: Meine erste Aufgabe"
   git push
   ```

---

## FAQ

**Q: Kann ich Markdown-Dateien manuell erstellen?**  
A: Ja, aber verwende den Python Manager für konsistente Metadaten und Dateinamen.

**Q: Wie ändere ich eine bestehende Datei?**  
A: Bearbeite die Markdown-Datei direkt oder lade sie, ändere das Objekt und speichere neu.

**Q: Was passiert wenn ich die Namenskonvention nicht einhalte?**  
A: Validierung schlägt fehl, INDEX-Generierung könnte Probleme haben.

**Q: Müssen Struktogramme immer dabei sein?**  
A: Bei Logik-Aufgaben ja (BW-Abitur-Standard), bei reinen Informationen nein.

**Q: Wie verlinke ich zwischen Dateien?**  
A: Verwende relative Pfade: `[Link](../aufgaben/L1/L1_3_1_Array-Summe_berechnen.md)`

---

## Checkliste: Neue Aufgabe erstellen

- [ ] Python Manager importiert
- [ ] Metadaten vollständig (Titel, Level, Kategorie, Nummer, Autor)
- [ ] Problemstellung klar formuliert
- [ ] Struktogramm erstellt (nach BW-Standard)
- [ ] Themen und Lernziele definiert
- [ ] Beispiel-Ein-/Ausgabe vorhanden
- [ ] Testfälle formuliert
- [ ] Mit Manager gespeichert
- [ ] Lösung erstellt (gleiche Metadaten)
- [ ] Indices regeneriert
- [ ] Validierung erfolgreich
- [ ] Committed und gepusht

---

## Ressourcen

- **Python Manager:** `src/utils/elearning_manager.py`
- **Struktogramm Helper:** `src/utils/struktogramm_helper.py`
- **Struktogramm Guide:** `docs/handbuch/STRUKTOGRAMM_GUIDE.md`
- **Operatorenliste:** `struktogramme/Operatorenliste-Struktogramme.md`

---

*Für Fragen und Feedback bitte ein Issue im Repository erstellen.*

<!-- CUSTOM_LICENSE_NOTICE_START -->
## License

This repository is licensed under a custom license.

- Attribution required: Christine Janischek - https://emotionalspirit.de
- Non-commercial use only
- Use only within state school systems
- Any other use requires explicit prior written permission
<!-- CUSTOM_LICENSE_NOTICE_END -->
