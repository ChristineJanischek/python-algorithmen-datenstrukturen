# Archiv-Verzeichnis

**Datum:** 10.03.2026  
**Zweck:** Archivierung von historischen Dateien und Referenzen

## Inhalt

### `/struktogramme/` (archiviert am 10.03.2026)

Dieses Verzeichnis enthält die **ursprünglichen Struktogramm-Beispieldateien** (.stgr-Format) und die **Operatorenliste**.

**Warum archiviert?**

Die Struktogramm-Kenntnisse wurden in eine **zentrale, wiederverwendbare Wissensdatenbank** überführt:

- 📦 **Python-Modul**: `src/utils/struktogramm_knowledge_base.py`
  - Enthält ALLE Operatoren nach BW-Standard v2.2
  - Notation-Regeln (Briefumschlag-Alternative, umgedrehtes L, etc.)
  - Pattern-Templates für häufige Algorithmen
  - Grafik-Formen für Draw.io Integration
  - Single Source of Truth für alle Struktogramm-Tools

- 📚 **Handbuch**: `docs/handbuch/STRUKTOGRAMM_GUIDE.md`
  - Praktischer Guide für Erstellung
  - Schritt-für-Schritt-Anleitungen
  - Beispiele und Best Practices

- 🎨 **Draw.io Extension**: `apps/drawio-extension/`
  - BW-konforme Shapes basierend auf der Wissensdatenbank
  - `library.xml` und `stencil.xml` mit validierten Formen

**Vorteile der neuen Struktur:**

✅ **Zentral**: Eine einzige Quelle für alle Struktogramm-Standards  
✅ **Konsistent**: Alle Tools verwenden die gleichen Definitionen  
✅ **Wartbar**: Änderungen nur an einer Stelle notwendig  
✅ **Automatisiert**: AI-Assistenten (Copilot) greifen auf strukturierte Daten zu  
✅ **Validiert**: Automatische Überprüfung gegen BW-Standards  

**Wann dieses Archiv verwenden?**

- ✔️ Referenz für alte Beispiel-Struktogramme (.stgr-Dateien)
- ✔️ Historische Nachvollziehbarkeit
- ✔️ Vergleich mit neuer Implementierung

**Wann NICHT verwenden?**

- ❌ Für neue Struktogramme (nutze `struktogramm_knowledge_base.py`)
- ❌ Für Operatoren-Syntax (nutze `get_knowledge_base()`)
- ❌ Für Pattern-Templates (nutze `kb.get_pattern_template()`)

## Nutzung der neuen Wissensdatenbank

### Python-Code

```python
from src.utils.struktogramm_knowledge_base import get_knowledge_base

# Wissensdatenbank abrufen
kb = get_knowledge_base()

# Operator-Definition abrufen
deklaration = kb.get_operator("deklaration")
print(deklaration.syntax)  # "Deklaration: variable |als datentyp|"

# Pattern-Template abrufen
pattern = kb.get_pattern_template("array_durchlaufen")
print(pattern)

# Notation-Regel abrufen
regel = kb.get_notation_regel("briefumschlag_alternative")
print(regel['template'])
```

### Für AI-Assistenten (Copilot, etc.)

Die Wissensdatenbank ist in den Copilot-Instructions hinterlegt:

```python
from src.utils.struktogramm_knowledge_base import (
    get_knowledge_base,
    get_operator_syntax,
    get_pattern,
    validate_bw_notation
)

# Schnellzugriff
syntax = get_operator_syntax("deklaration")
pattern = get_pattern("summe_berechnen")
is_valid = validate_bw_notation("Deklaration: x", "deklaration")
```

## Migration abgeschlossen

✅ Archiv erstellt: 10.03.2026  
✅ Wissensdatenbank implementiert: `struktogramm_knowledge_base.py`  
✅ Copilot-Instructions aktualisiert  
✅ AI-Memory konfiguriert  

---

*Bei Fragen zur neuen Struktur siehe: `/docs/handbuch/STRUKTOGRAMM_GUIDE.md`*
