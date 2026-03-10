# Migration: Struktogramm-Wissensdatenbank

**Datum:** 10.03.2026  
**Branch:** feat/pruefungsmodul-maerz-2026  
**Status:** ✅ Abgeschlossen

## Übersicht

Das Struktogramm-System wurde von einem dateibasierten Archiv in eine **zentrale, wiederverwendbare Wissensdatenbank** migriert.

## Durchgeführte Änderungen

### 1. ✅ Zentrale Wissensdatenbank erstellt

**Datei:** `src/utils/struktogramm_knowledge_base.py`

**Inhalt:**
- ✅ 17 Operatoren nach BW-Standard v2.2 (vollständig)
- ✅ 3 Notation-Regeln (Briefumschlag-Alternative, umgedrehtes L, Aufruf-Seitenstriche)
- ✅ 4 Pattern-Templates (array_durchlaufen, summe_berechnen, maximum_finden, lineare_suche)
- ✅ 4 Grafik-Formen (für Draw.io Integration)
- ✅ Singleton-Pattern für konsistente Nutzung
- ✅ Convenience-Functions für schnellen Zugriff
- ✅ Validierungs-Funktionen
- ✅ Export-Funktionen für Dokumentation

**Operatoren-Kategorien:**
1. **Variablen und Datenstrukturen** (4 Operatoren)
   - Deklaration
   - Initialisierung
   - Deklaration und Initialisierung
   - Zuweisung

2. **Ein- und Ausgabe** (4 Operatoren)
   - Einlesen
   - Deklaration und Einlesen
   - Ausgabe
   - Rückgabe

3. **Funktionen und Methoden** (1 Operator)
   - Aufruf

4. **Kontrollstrukturen** (4 Operatoren)
   - Wenn (Alternative/Verzweigung)
   - Wiederhole solange (While-Schleife)
   - Wiederhole von (For-Schleife Variante 1)
   - Zähle (For-Schleife Variante 2)

5. **Arrays** (4 Operatoren)
   - Array-Deklaration und Initialisierung
   - Array-Element-Zuweisung
   - Anhängen an Array
   - Anzahl der Elemente

### 2. ✅ Archivierung durchgeführt

**Aktion:** `struktogramme/` → `archiv/struktogramme/`

**Archivierte Inhalte:**
- ✅ Alle .stgr-Beispieldateien (ca. 50+ Dateien)
- ✅ Operatorenliste-Struktogramme.md (Original)
- ✅ Converter-Module
- ✅ README.md mit Archiv-Erklärung erstellt

**Neue Struktur:**
```
archiv/
├── README.md                          # Archiv-Dokumentation
└── struktogramme/                     # Archiviertes Verzeichnis
    ├── Operatorenliste-Struktogramme.md  # Original (nur Referenz)
    ├── L1_*.stgr                      # Beispiele Level 1
    ├── L2_*.stgr                      # Beispiele Level 2
    ├── L3_*.stgr                      # Beispiele Level 3
    └── converter/                     # XML-Renderer/Validator
```

### 3. ✅ Copilot-Instructions aktualisiert

**Datei:** `.github/copilot-instructions.md`

**Änderungen:**
- ✅ Verweise auf `struktogramme/Operatorenliste-Struktogramme.md` entfernt
- ✅ Neue zentrale Wissensdatenbank referenziert
- ✅ Beispiele für Knowledge Base Nutzung hinzugefügt
- ✅ Python-Helper Abschnitt erweitert
- ✅ Verzeichnisstruktur aktualisiert
- ✅ Abschnitt "Für AI-Assistenten" aktualisiert mit Code-Beispielen
- ✅ Alle Verweise auf `struktogramme/` → `archiv/struktogramme/` korrigiert

### 4. ✅ AI-Memory erstellt

**Dateien:**
- ✅ `/memories/repo/Struktogramm_Knowledge_Base.md`
  - Vollständige Anleitung zur Nutzung
  - Code-Beispiele
  - Workflow für AI-Assistenten
  
- ✅ `/memories/repo/Archiv_Struktogramme_Migration.md`
  - Migrations-Dokumentation
  - Begründung
  - Vorteile der neuen Struktur

### 5. ✅ Tests und Validierung

**Durchgeführte Tests:**
- ✅ Knowledge Base lädt erfolgreich
- ✅ 17 Operatoren verfügbar
- ✅ 4 Pattern-Templates abrufbar
- ✅ 3 Notation-Regeln funktional
- ✅ Operator-Abruf funktioniert
- ✅ Pattern-Templates funktionieren
- ✅ Notation-Regeln mit Qualitätschecks verfügbar
- ✅ Archiv-Struktur korrekt
- ✅ Alle .stgr-Dateien im Archiv
- ✅ Operatorenliste im Archiv vorhanden

## API-Nutzung

### Wissensdatenbank importieren

```python
from src.utils.struktogramm_knowledge_base import get_knowledge_base

kb = get_knowledge_base()
```

### Operator abrufen

```python
# Vollständige Operator-Definition
deklaration = kb.get_operator("deklaration")
print(deklaration.syntax)     # "Deklaration: variable |als datentyp|"
print(deklaration.beispiel)   # "Deklaration: alter als Ganzzahl"
print(deklaration.hinweise)   # Liste von Hinweisen

# Schnellzugriff nur Syntax
from src.utils.struktogramm_knowledge_base import get_operator_syntax
syntax = get_operator_syntax("deklaration")
```

### Pattern-Template abrufen

```python
# Vollständige Pattern-Templates
pattern = kb.get_pattern_template("array_durchlaufen")
pattern = kb.get_pattern_template("summe_berechnen")
pattern = kb.get_pattern_template("maximum_finden")
pattern = kb.get_pattern_template("lineare_suche")

# Schnellzugriff
from src.utils.struktogramm_knowledge_base import get_pattern
pattern = get_pattern("summe_berechnen")
```

### Notation-Regel abrufen

```python
# BW-Briefumschlag-Alternative (VERBINDLICH!)
regel = kb.get_notation_regel("briefumschlag_alternative")
print(regel['template'])         # Template-Code
print(regel['qualitaetscheck'])  # Liste von Checks

# Weitere Regeln
regel = kb.get_notation_regel("umgedrehtes_l")
regel = kb.get_notation_regel("aufruf_seitenstriche")
```

### Validierung

```python
from src.utils.struktogramm_knowledge_base import validate_bw_notation

# Syntax gegen BW-Standard prüfen
is_valid = validate_bw_notation("Deklaration: x", "deklaration")
```

### Alle Operatoren einer Kategorie

```python
from src.utils.struktogramm_knowledge_base import OperatorKategorie

# Alle Array-Operatoren
array_ops = kb.get_operators_by_kategorie(OperatorKategorie.ARRAYS)
for op in array_ops:
    print(f"{op.name}: {op.syntax}")
```

## Vorteile

### ✅ Zentral
- Eine einzige Quelle für alle Struktogramm-Standards
- Keine Duplikate oder widersprüchliche Informationen

### ✅ Konsistent
- Alle Tools verwenden dieselben Definitionen
- Automatische Synchronisation zwischen Helper, Validator, Draw.io Extension

### ✅ Wartbar
- Änderungen nur an einer Stelle notwendig
- Klar strukturierter Code mit Dataclasses

### ✅ Automatisiert
- AI-Assistenten (Copilot) können strukturierte Daten nutzen
- Programmgesteuerte Validierung
- Automatische Code-Generierung möglich

### ✅ Validiert
- Automatische Überprüfung gegen BW-Standards
- Qualitätschecks integriert

## Integration mit bestehenden Tools

### Draw.io Extension
Die Draw.io Extension (`apps/drawio-extension/`) nutzt die gleichen Standards:
- Shapes basieren auf den Grafik-Formen der Knowledge Base
- `library.xml` und `stencil.xml` sind BW-konform

### Struktogramm Helper
Das bestehende Modul `src/utils/struktogramm_helper.py` kann die Knowledge Base nutzen:
```python
from src.utils.struktogramm_knowledge_base import get_knowledge_base
from src.utils.struktogramm_helper import StruktogrammBuilder

kb = get_knowledge_base()
builder = StruktogrammBuilder()

# Operator aus KB verwenden
op = kb.get_operator("deklaration")
builder.add_element(op.syntax)
```

### E-Learning Manager
Der E-Learning Manager kann Pattern-Templates aus der Knowledge Base verwenden:
```python
from src.utils.struktogramm_knowledge_base import get_pattern
from src.utils.elearning_manager import create_aufgabe_quick

pattern = get_pattern("array_durchlaufen")
aufgabe = create_aufgabe_quick(
    titel="Array durchlaufen",
    struktogramm=pattern,
    # ... weitere Parameter
)
```

## Weitere Ressourcen

- **Guide:** `docs/handbuch/STRUKTOGRAMM_GUIDE.md` (unverändert)
- **Archiv:** `archiv/README.md` (neue Dokumentation)
- **Memory:** `/memories/repo/Struktogramm_Knowledge_Base.md`
- **Copilot:** `.github/copilot-instructions.md` (aktualisiert)

## Nächste Schritte (Optional)

**Mögliche Erweiterungen:**
1. ✨ Struktogramm-Renderer basierend auf Knowledge Base
2. ✨ Automatische Draw.io XML-Generierung
3. ✨ Erweiterte Validierungsmechanismen
4. ✨ Interaktive Beispiele/Tutorials
5. ✨ Export-Funktionen (PDF, SVG, etc.)

## Änderungs-Log

| Datum      | Änderung                                    | Status |
|------------|---------------------------------------------|--------|
| 10.03.2026 | Wissensdatenbank erstellt                   | ✅      |
| 10.03.2026 | Archivierung durchgeführt                   | ✅      |
| 10.03.2026 | Copilot-Instructions aktualisiert           | ✅      |
| 10.03.2026 | AI-Memory erstellt                          | ✅      |
| 10.03.2026 | Tests und Validierung erfolgreich           | ✅      |

---

**Migration abgeschlossen am:** 10.03.2026  
**Erstellt von:** GitHub Copilot Agent  
**Version:** 1.0
