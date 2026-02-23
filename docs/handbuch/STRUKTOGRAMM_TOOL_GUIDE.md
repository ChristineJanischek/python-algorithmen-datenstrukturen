# Struktogramm-Tools für Baden-Württemberg Abitur

Ein umfassendes Paket zur Validierung und Refactoring von Struktogrammen nach der offiziellen **Baden-Württemberg Operatorenliste**.

---

## 🎯 Features

✅ **Validator** - Prüft Struktogramme gegen BW-Standard  
✅ **Refactorer** - Automatische Konvertierung zu korrekter Notation  
✅ **CLI-Tool** - Kommandozeilen-Interface für Batch-Verarbeitung  
✅ **Analyzer** - Analysiert Struktur und Komplexität  
✅ **Formatter** - Normalisiert Abstände und Konsistenz  
✅ **Render Pipeline** - Erzeugt SVG aus `struktogramm`-Blöcken mit Report-Ausgabe

---

## 📦 Installation

```bash
# Code in apps/tools/
cd apps/tools
pip install colorama  # Für farbigen Output
```

---

## 🚀 Schnelleinstieg

### Als Python-Modul

```python
from struktogramm_validator import StruktogrammValidator
from struktogramm_refactorer import StruktogrammRefactorer

# Validierung
validator = StruktogrammValidator()
results = validator.validate_document(struktogramm_text)

# Refactoring
refactorer = StruktogrammRefactorer()
refactored, changes = refactorer.refactor_content(struktogramm_text)
```

### Kommandozeile

```bash
# Datei validieren
python struktogramm_cli.py validate docs/pruefungen/Klausur_L2_2_1_Verfuegung.md

# Datei refaktorieren (Dry-Run)
python struktogramm_cli.py refactor docs/pruefungen/Klausur_L2_2_1_Verfuegung.md --dry-run

# Datei aktualisieren
python struktogramm_cli.py refactor docs/pruefungen/Klausur_L2_2_1_Verfuegung.md --in-place

# Ganzes Repository prüfen
python struktogramm_cli.py check-repo --pattern "docs/**/*.md"

# Operatoren anzeigen
python struktogramm_cli.py operators

# Datei analysieren
python struktogramm_cli.py analyze docs/pruefungen/Klausur_L2_2_1_Verfuegung.md

# SVG Rendering
python struktogramm_cli.py render docs/pruefungen/Klausur_L2_2_1_Musterloesungen_Variante_A.md --strict

# Rendering mit JSON-Report
python struktogramm_cli.py render-and-validate docs/pruefungen/Klausur_L2_2_1_Musterloesungen_Variante_A.md --report reports/render_report.json
```

---

## 📋 Kommandos

### `validate`

Validiert eine Struktogramm-Datei gegen die Operatorenliste.

```bash
python struktogramm_cli.py validate <file>
```

**Beispiel:**
```bash
cd apps/tools
python struktogramm_cli.py validate ../../../docs/pruefungen/Klausur_L2_2_1_Verfuegung.md
```

**Output:**
```
============================================================
Validiere: docs/pruefungen/Klausur_L2_2_1_Verfuegung.md
============================================================

❌ Fehler gefunden:
  [ERROR] Zeile 45: Englischer Operator 'While' erkannt...
  
⚠️  Warnungen gefunden:
  [WARNING] Zeile 67: Englischer Operator 'If' erkannt...
  💡 Vorschlag: Wenn

Zusammenfassung:
  Fehler: 1
  Warnungen: 2
  Status: ❌ NICHT BESTANDEN
```

---

### `refactor`

Refaktoriert eine Datei zu korrekter Notation.

```bash
python struktogramm_cli.py refactor <file> [--dry-run] [--in-place]
```

**Optionen:**
- `--dry-run` (Standard): Nur Vorschau
- `--in-place`: Datei direkt überschreiben

**Beispiel (Dry-Run):**
```bash
cd apps/tools
python struktogramm_cli.py refactor ../../../docs/pruefungen/Klausur_L2_2_1_Verfuegung.md --dry-run
```

**Output:**
```
📝 Refactoring-Bericht
============================================================

Änderungen: 12

📍 Zeile 45:
   Englischer Operator zu BW-Standard
   ❌ Original: while zahl != -1:
   ✅ Neu:     Wiederhole solange zahl != -1
   🎯 Genauigkeit: 95%

📍 Zeile 67:
   If-Statement zu Wenn-Operator
   ❌ Original: if alter > 18:
   ✅ Neu:     Wenn alter > 18, dann
   🎯 Genauigkeit: 85%

Statistiken:
  Insgesamt: 12 Änderungen
  🎯 Hohe Genauigkeit (≥80%): 10
  🟡 Mittlere Genauigkeit (50-80%): 2
  🔴 Niedrige Genauigkeit (<50%): 0
```

---

### `check-repo`

Prüft alle Struktogramme im Repository.

```bash
python struktogramm_cli.py check-repo [--pattern "**/*.md"] [--base-path "."]
```

**Beispiel:**
```bash
cd apps/tools
python struktogramm_cli.py check-repo --pattern "docs/**/*.md"
```

---

### `operators`

Zeigt alle verfügbaren Operatoren nach BW-Standard.

```bash
cd apps/tools
python struktogramm_cli.py operators
```

---

### `analyze`

Analysiert ein Struktogramm.

```bash
cd apps/tools
python struktogramm_cli.py analyze <file>
```

### `render`

Rendert `struktogramm`-Codeblöcke einer Markdown-Datei zu SVG-Dateien.

```bash
python struktogramm_cli.py render <file> [--output-dir "..."] [--prefix "..."] [--strict] [--report "..."]
```

### `render-and-validate`

Kombiniert Rendering und Validierungsreport in einem Lauf.

```bash
python struktogramm_cli.py render-and-validate <file> [--output-dir "..."] [--prefix "..."] [--strict] [--report "..."]
```

---

## 📖 Python API

Siehe [STRUKTOGRAMM_TOOLS.md](STRUKTOGRAMM_TOOLS.md) für ausführliche API-Dokumentation.

---

## 🔧 Refactoring-Regeln

Das Tool wendet folgende automatische Refactorings an:

| Original | Refaktoriert | Genauigkeit |
|----------|--------------|------------|
| `while zahl != -1:` | `Wiederhole solange zahl != -1` | 95% |
| `for i in range(5):` | `Zähle i von 0 bis 4, Schrittweite 1` | 90% |
| `if alter > 18:` | `Wenn alter > 18, dann` | 85% |
| `else:` | `, sonst` | 90% |
| `return wert` | `Rückgabe: wert` | 95% |
| `print(...)` | `Ausgabe: ...` | 90% |
| `input(...)` | `Einlesen: variable` | 70% |

---

## 🎓 Integration mit Copilot

Siehe [STRUKTOGRAMM_COPILOT_INTEGRATION.md](STRUKTOGRAMM_COPILOT_INTEGRATION.md) für Details.

---

## 📚 Referenzen

- **Code:** `apps/tools/`
- **Operatorenliste:** `struktogramme/Operatorenliste-Struktogramme.md`
- **Struct ogramm-Guide:** `docs/handbuch/STRUKTOGRAMM_GUIDE.md`
- **E-Learning Template:** `docs/handbuch/ELEARNING_TEMPLATE_GUIDE.md`
- **Main Tool Guide:** `docs/handbuch/STRUKTOGRAMM_TOOLS.md`
- **Render Pipeline:** `docs/handbuch/STRUKTOGRAMM_RENDER_PIPELINE.md`

---

**Erstellt von:** GitHub Copilot  
**Version:** 1.0  
**Zuletzt aktualisiert:** February 2026
