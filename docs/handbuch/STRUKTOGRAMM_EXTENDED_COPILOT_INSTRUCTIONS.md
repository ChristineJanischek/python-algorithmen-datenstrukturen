# Erweiterte Copilot-Instructions für Struktogramm-Automatisierung

Diese Datei enthält die erweiterten Instructions, die in `.github/copilot-instructions.md` 
zu Section 1 hinzugefügt werden sollten.

---

## 🎯 Automatische Struktogramm-Validierung (NEUE REGEL)

### AKTIVIERUNG

**Trigger-Stichwort:** "Struktogramm" (in jeglicher Form)

**Kontext:**
- Wenn Sie (KI) ein Struktogramm erstellen
- Wenn Benutzer ein Struktogramm anfordert  
- Wenn Sie Struktogramm-Code überarbeiten

### SOFORTMASSNAHMEN

1. **IMMER** die neueste Operatorenliste konsultieren:
   ```python
   struktogramme/Operatorenliste-Struktogramme.md
   ```

2. **NUR diese Operatoren verwenden:**
   - ✅ `Deklaration:`
   - ✅ `Initialisierung:`
   - ✅ `Deklaration und Initialisierung:`
   - ✅ `Zuweisung:`
   - ✅ `Einlesen:`
   - ✅ `Ausgabe:`
   - ✅ `Rückgabe:`
   - ✅ `Aufruf:`
   - ✅ `Wenn...dann, ...sonst`
   - ✅ `Wiederhole solange`
   - ✅ `Zähle ... von ... bis ..., Schrittweite`
   - ✅ `Anzahl der Elemente des Arrays`

3. **ABSOLUTE VERBOTE:**
   ```
   ❌ while      (verwende stattdessen: Wiederhole solange)
   ❌ if         (verwende stattdessen: Wenn)
   ❌ else       (verwende stattdessen: , sonst)
   ❌ for        (verwende stattdessen: Zähle)
   ❌ return     (verwende stattdessen: Rückgabe:)
   ❌ print      (verwende stattdessen: Ausgabe:)
   ❌ input      (verwende stattdessen: Einlesen:)
   ❌ def        (verwende stattdessen: Aufruf:)
   ❌ |optional| (verwende stattdessen: optional weglassen oder "als datentyp" schreiben)
   ```

### NORMALFORM FÜR STRUKTOGRAMME

```
Deklaration und Initialisierung: variable als Datentyp = wert
Wenn bedingung, dann
    J
        [Aktionen]
    , sonst
    N
        [Aktionen]
```

### TOOLS VERFÜGBAR

Falls verfügbar, verwende die automatischen Werkzeuge:


## 📐 Struktogramm (grafische Notation)

<!-- START_GRAPHIC_STRUKTOGRAMM -->
```
┌────────────────────────────────────────┐
│ [STRUKTOGRAMM HIER HINZUFÜGEN]         │
│                                        │
│ Beispiel-Elemente:                     │
│ • Deklaration                          │
│ • Zuweisung                            │
│ • Schleife (┌─ ... ─┘)                 │
│ • Verzweigung (J/N Zweige)             │
└────────────────────────────────────────┘
```
<!-- END_GRAPHIC_STRUKTOGRAMM -->


```python
from apps.tools.struktogramm_validator import StruktogrammValidator
from apps.tools.struktogramm_refactorer import StruktogrammRefactorer

# Validiere vor Ausgabe
validator = StruktogrammValidator()
results = validator.validate_document(your_struktogramm)

# Automatische Korrektur wenn nötig
if results:
    refactorer = StruktogrammRefactorer()
    corrected, changes = refactorer.refactor_content(your_struktogramm)
    # Nutze corrected für Output
```

### BEISPIELE

#### ❌ FALSCH (Alte Notation)
```
Einlesen: alter |als Ganzzahl|
Wenn alter < 18 dann
    Ausgabe: Jugendlicher
Sonst
    Ausgabe: Erwachsener
```

#### ✅ RICHTIG (BW-Standard)
```
Deklaration und Einlesen: alter als Ganzzahl
Wenn alter < 18, dann
    J
        Ausgabe: "Jugendlicher"
    , sonst
    N
        Ausgabe: "Erwachsener"
```

### HÄUFIGE FEHLER VERMEIDEN

| Fehler | Behebung |
|--------|----------|
| `\|als Typ\|` mit Bindestrichen | Schreibe: `als Typ` (ohne Bindestriche) |
| `Falsch` / `Wahr` großgeschrieben | Schreibe: `falsch` / `wahr` (klein) |
| `Wiederhole während` | Schreibe: `Wiederhole solange` |
| `=` statt `==` in Bedingungen | Schreibe: `==` als Vergleichsoperator |
| Keine `J` und `N` Labels | Schreibe: `J` für Ja-Zweig, `N` für Nein-Zweig |
| Fehlende Komma vor `sonst` | Schreibe: `, sonst` (mit Komma und Leerzeichen) |

### VALIDIERUNGSPROZESS VOR AUSGABE


## 📐 Struktogramm (grafische Notation)

<!-- START_GRAPHIC_STRUKTOGRAMM -->
```
┌────────────────────────────────────────┐
│ [STRUKTOGRAMM HIER HINZUFÜGEN]         │
│                                        │
│ Beispiel-Elemente:                     │
│ • Deklaration                          │
│ • Zuweisung                            │
│ • Schleife (┌─ ... ─┘)                 │
│ • Verzweigung (J/N Zweige)             │
└────────────────────────────────────────┘
```
<!-- END_GRAPHIC_STRUKTOGRAMM -->


```python
def validate_before_output(struktogramm_text):
    """
    Prüfe Struktogramm vor der Ausgabe
    """
    # 1. Prüfe auf englische Keywords
    forbidden = ['while', 'if', 'else', 'for', 'return', 'def']
    for word in forbidden:
        if word in struktogramm_text.lower():
            # Fehler! Korrigiere automatisch
            return correct_and_retry(struktogramm_text)
    
    # 2. Prüfe auf korrekte Operatoren
    validator = StruktogrammValidator()
    results = validator.validate_document(struktogramm_text)
    if results:
        # Warnung - aber trotzdem ausgeben mit Vermerk
        return add_warning(struktogramm_text, results)
    
    # 3. OK - Gib aus
    return struktogramm_text
```

### RESPONSE-FORMAT

Bei Struktogramm-Antworten:

```markdown
# [Aufgabentitel]

## Struktogramm (BW-Standard nach Operatorenliste)

\`\`\`struktogramm
[KORREKTE NOTATION HIER]
\`\`\`

## Erklärung

[Optional: Text der das Struktogramm erklärt]

## Python-Code (OPTIONAL)

\`\`\`python
[Python-Implementierung - GGF. unterscheidet sich vom Struktogramm]
\`\`\`
```

### TESTCASES

Diese Testfälle sollten IMMER korrekt refaktoriert sein:

```struktogramm
# Test 1: While-Schleife
Wiederhole solange zaehler < 10
    Zuweisung: zaehler = zaehler + 1
    Ausgabe: zaehler

# Test 2: Verzweigung
Wenn alter >= 18, dann
    J
        Ausgabe: "Erwachsen"
    , sonst
    N
        Ausgabe: "Jugendlich"

# Test 3: Array-Durchlauf
Deklaration und Initialisierung: n als Ganzzahl = Anzahl der Elemente des Arrays werte
Zähle i von 0 bis n - 1, Schrittweite 1
    Ausgabe: werte[i]

# Test 4: Komplexes Beispiel
Deklaration und Initialisierung: summe als Ganzzahl = 0
Deklaration und Initialisierung: i als Ganzzahl = 0
Wiederhole solange i < 10
    Zuweisung: summe = summe + i
    Zuweisung: i = i + 1
Ausgabe: "Summe: " + summe
```

### BEWERTUNG VON SCHÜLER-STRUKTOGRAMMEN

Wenn Sie Schüler-Struktogramme bewerten:

```markdown
**Bewertung Struktogramm [Aufgabennummer]:**

✅ Positive Aspekte:
- [Operator korrekt]
- [Struktur logisch]
- ...

⚠️ Verbesserungen möglich:
- [Operator falsch - sollte sein: ...]
- [Format nicht konsistent]
- ...

❌ Kritische Fehler:
- [Englische Keywords gefunden]
- [Struktur logisch falsch]
- ...

**Gesamt:** X / Y Punkte
**Feedback:** [Spezifisches Feedback basierend auf Operatorenliste]
```

### NOTFALL-FALLBACK

Falls Sie unsicher sind:

1. Schaue in: `struktogramme/Operatorenliste-Struktogramme.md`
2. Nutze den Validator: `cd apps/tools && python struktogramm_cli.py validate <file>`
3. Im Zweifelsfall: Nutze Refactorer im Dry-Run: `cd apps/tools && python struktogramm_cli.py refactor <file> --dry-run`

---

## INTEGRATION IN COPILOT-INSTRUCTIONS

Diese gesamte Sektion sollte in `.github/copilot-instructions.md` nach 
Abschnitt 1.1 (Struktogramme - HÖCHSTE PRIORITÄT) eingefügt werden.

**Platzierung:**
```markdown
# GitHub Copilot Instructions

## Repository-Kontext
...

## Wichtige Standards

### 1. Struktogramme (HÖCHSTE PRIORITÄT)
**⚠️ WICHTIG:** Alle...
[BESTEHENDER Text...]

### 1.1 AUTOMATISCHE STRUKTOGRAMM-VALIDIERUNG (NEU)
[DIESER TEXT - vollständig einfügen]
```

---

## AUTOMATISIERUNG TESTEN

### Test 1: Prompt mit "Struktogramm"
```
Benutzer: "Erstelle ein Struktogramm für eine for-Schleife"
Copilot: [AUTOMATISCH aktiviert]
→ Nutzt BW-Notation statt "for"
```

### Test 2: Refactoring-Prompt
```
Benutzer: "Fix diese Struktogramm-Fehler: [...]"
Copilot: [AUTOMATISCH aktiviert]
→ Erkennt & korrigiert Fehler
```

### Test 3: Schüler-Feedback
```
Benutzer: "Bewerte dieses Struktogramm: [...]"
Copilot: [AUTOMATISCH aktiviert]
→ Nutzt BW-Standard als Bewertungskriterium
```

---

## DOCUMENTATION IN REPO

Alle diese Dokumente sind im Repo gespeichert:

- `.github/copilot-instructions.md` - Master-Instructions
- `docs/handbuch/STRUKTOGRAMM_TOOLS.md` - Main Tool-Dokumentation
- `docs/handbuch/STRUKTOGRAMM_TOOL_GUIDE.md` - Ausführlicher Guide
- `docs/handbuch/STRUKTOGRAMM_COPILOT_INTEGRATION.md` - Integrations-Anleitung
- `struktogramme/Operatorenliste-Struktogramme.md` - Die Quelle der Wahrheit

---

**Erstellt:** Februar 2026  
**Version:** 1.0  
**Status:** Produktionsreif
