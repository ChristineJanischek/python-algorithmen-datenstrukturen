# GitHub Copilot Instructions

## Repository-Kontext

Dies ist ein Python-Repository für **Algorithmen und Datenstrukturen** im Kontext des **Beruflichen Gymnasiums Baden-Württemberg** (Informatik und Wirtschaftsinformatik).

## Wichtige Standards

### 1. Struktogramme (HÖCHSTE PRIORITÄT)

**⚠️ WICHTIG:** Alle Programmlogik muss nach den **Baden-Württemberg Abitur-Standards** dargestellt werden.

#### Wenn Programmlogik gefragt ist:

1. **IMMER** Struktogramme verwenden (keine Flussdiagramme!)
2. **IMMER** die Operatorenliste beachten: `struktogramme/Operatorenliste-Struktogramme.md`
3. **IMMER** den Guide verwenden: `docs/handbuch/STRUKTOGRAMM_GUIDE.md`
4. **IMMER** textbasierte Notation verwenden

#### Verfügbare Operatoren (Kurzübersicht):

```
# Variablen
Deklaration: variable |als datentyp|
Initialisierung: variable = wert
Deklaration und Initialisierung: variable |als datentyp| = wert
Zuweisung: variable = wert

# Ein-/Ausgabe
Einlesen: variable |als datentyp|
Ausgabe: inhalt
Rückgabe: wert

# Kontrollstrukturen
Wenn bedingung, dann
    J
        [Anweisungen]
    , sonst
    N
        [Anweisungen]

Wiederhole solange bedingung
    [Anweisungen]

Zähle variable von start bis ende, Schrittweite n
    [Anweisungen]

# Arrays
Deklaration und Initialisierung: array = [wert1, wert2, ...]
Zuweisung: array[index] = wert
Anzahl der Elemente des Arrays array
```

#### Häufige Patterns (aus Guide verwenden):

- Array durchlaufen
- Summe berechnen
- Maximum/Minimum finden
- Lineare Suche
- Bubble Sort
- Eingabe validieren

#### Python-Helper verfügbar:

```python
from src.utils.struktogramm_helper import (
    StruktogrammBuilder,
    StruktogrammValidator,
    StruktogrammRenderer,
    pattern_array_durchlaufen,
    pattern_summe_berechnen,
    pattern_maximum_finden,
    pattern_lineare_suche
)
```

### 2. Code-Struktur

#### Verzeichnisstruktur:

```
src/
├── niveau/           # Niveau-spezifische Materialien
│   ├── infodateien/  # Informationsmaterialien
│   ├── ka_template/  # Klassenarbeits-Templates
│   ├── myKa/         # Klassenarbeiten
│   └── pruefdateien/ # Prüfungsmaterialien
├── utils/            # Hilfs-Module (inkl. struktogramm_helper.py)
docs/
├── aufgaben/         # Aufgabenstellungen
├── loesungen/        # Lösungen
├── handbuch/         # Handbücher und Guides
struktogramme/        # Struktogramm-Dateien (.stgr)
```

#### Python-Code:

- **Type Hints verwenden:** Alle Funktionen mit Type Hints versehen
- **Docstrings:** Google-Style Docstrings für alle öffentlichen Funktionen
- **Naming:** Deutsche Variablennamen OK (Kontext: deutsches Abitur)
- **Tests:** Wo sinnvoll unittest oder pytest verwenden

Beispiel:
```python
def berechne_summe(zahlen: list[int]) -> int:
    """
    Berechnet die Summe aller Zahlen in der Liste.
    
    Args:
        zahlen: Liste der zu summierenden Zahlen
        
    Returns:
        Die Summe aller Zahlen
    """
    summe = 0
    for zahl in zahlen:
        summe += zahl
    return summe
```

### 3. E-Learning Aufgaben

Wenn E-Learning-Aufgaben erstellt werden:

1. **Struktogramm erstellen** (Pflicht!)
2. **Python-Code erstellen**
3. **Testfälle definieren**
4. **Musterlösung bereitstellen**

Template:
```markdown
# Aufgabe: [Titel]

## Problemstellung
[Beschreibung]

## Struktogramm
\`\`\`
[Struktogramm nach BW-Standard]
\`\`\`

## Implementierung
\`\`\`python
[Python-Code]
\`\`\`

## Tests
\`\`\`python
[Testfälle]
\`\`\`
```

### 4. Sortier- und Suchalgorithmen

Bei Sortier-/Suchalgorithmen:

1. **ZUERST** Struktogramm nach BW-Standard
2. **DANN** Python-Implementierung
3. **Immer** Komplexität angeben (O-Notation)
4. **Optional** Visualisierung

Beispiel verfügbar in: `struktogramme/L2_2_1_3_Struktogramm_Bubble_Sort.stgr`

### 5. Datenstrukturen

Bevorzugte Python-Strukturen:

- **Listen** statt Arrays (aber im Struktogramm "Array" nennen)
- **Dictionaries** für Key-Value-Paare
- **Sets** für eindeutige Elemente
- **Tuples** für unveränderbare Sequenzen

### 6. Kommentare und Dokumentation

- **Deutsch** für Kommentare (Zielgruppe: deutsche Schüler)
- **Struktogramme** für Logik-Dokumentation
- **Docstrings** auf Deutsch oder Englisch (einheitlich im Projekt)

### 7. Best Practices

#### DO:
✅ Struktogramme nach BW-Standard verwenden
✅ Type Hints verwenden
✅ Aussagekräftige Variablennamen (deutsch OK)
✅ Tests schreiben
✅ Patterns aus dem Guide wiederverwenden
✅ Code kommentieren

#### DON'T:
❌ Flussdiagramme statt Struktogramme
❌ Von BW-Standards abweichen
❌ Englische Fachbegriffe ohne Erklärung (Zielgruppe: Schüler)
❌ Code ohne Struktogramm (bei Logik-Aufgaben)
❌ Komplexe Algorithmen ohne Komplexitätsangabe

### 8. Spezielle Hinweise für Aufgabenerstellung

#### Schwierigkeitsgrade:

- **L1_x**: Grundlagen (Sequenz, einfache Verzweigung/Schleifen)
- **L2_x**: Fortgeschritten (Arrays, Such-/Sortieralgorithmen)
- **L3_x**: Expert (Komplexe Datenstrukturen, Rekursion)

#### Bezeichnung:

Format: `LX_Y_Z_Thema`
- `X`: Level (1-3)
- `Y`: Kategorie (1=Grundlagen, 2=Sortieren, 3=Suchen, 4=Vertiefung, ...)
- `Z`: Aufgabennummer

### 9. Ressourcen im Repository

**Wichtigste Dateien:**

- 📄 `struktogramme/Operatorenliste-Struktogramme.md` - Die Bibel für Struktogramme!
- 📄 `docs/handbuch/STRUKTOGRAMM_GUIDE.md` - Praktischer Guide mit Patterns
- 🐍 `src/utils/struktogramm_helper.py` - Python-Helper für Struktogramme
- 📄 `.github/copilot-instructions.md` - Diese Datei

**Beispiele:**

- `struktogramme/*.stgr` - Fertige Struktogramm-Beispiele
- `src/niveau/infodateien/` - Informationsmaterialien

### 10. Workflow für neue Aufgaben

```
1. Problem analysieren
   ↓
2. Struktogramm erstellen (BW-Standard!)
   ├─ Guide konsultieren
   ├─ Patterns verwenden
   └─ Validieren mit struktogramm_helper.py
   ↓
3. Python-Code implementieren
   ├─ Type Hints
   └─ Docstrings
   ↓
4. Tests schreiben
   ↓
5. Dokumentieren
   └─ Aufgabenstellung + Lösung
```

### 11. Typische Abitur-Themen (BW)

**Die wichtigsten:**

1. **Arrays/Listen**
   - Durchlaufen, Manipulieren, Suchen, Sortieren
   
2. **Sortieralgorithmen**
   - Bubble Sort, Selection Sort
   
3. **Suchalgorithmen**
   - Lineare Suche, Binäre Suche
   
4. **Kontrollstrukturen**
   - Verzweigungen (einfach, mehrfach, geschachtelt)
   - Schleifen (while, for)
   
5. **Funktionen/Methoden**
   - Parameter, Rückgabewerte
   
6. **Komplexität**
   - O-Notation verstehen und anwenden

### 12. Schnell-Checkliste

Wenn du Code/Aufgaben für dieses Repository erstellst:

- [ ] Brauche ich ein Struktogramm? (Ja, bei Logik-Aufgaben!)
- [ ] Entspricht es den BW-Standards? (Guide checken!)
- [ ] Habe ich Type Hints verwendet?
- [ ] Sind die Variablennamen verständlich?
- [ ] Gibt es Tests?
- [ ] Ist die Komplexität dokumentiert? (bei Algorithmen)
- [ ] Ist alles auf Deutsch kommentiert?

---

## Für AI-Assistenten

**Wenn du ein AI-Assistent bist der in diesem Repository arbeitet:**

1. **LIES ZUERST:** `docs/handbuch/STRUKTOGRAMM_GUIDE.md`
2. **BEI STRUKTOGRAMMEN:** Verwende IMMER die Operatorenliste
3. **BEI PATTERNS:** Nutze die vorgefertigten Patterns aus dem Guide
4. **BEI UNSICHERHEIT:** Validiere mit `struktogramm_helper.py`
5. **DENKE DARAN:** Dies ist für Schüler im Abitur - klar und verständlich!

---

*Letzte Aktualisierung: 05.02.2026*
*Version: 1.0*
