# Beispiele - Struktogramm Knowledge Base

Dieses Verzeichnis enthält Beispiel-Scripts zur Verwendung der **zentralen Struktogramm-Wissensdatenbank**.

## Verfügbare Beispiele

### `struktogramm_knowledge_base_beispiele.py`

Umfassendes Demo-Script, das alle Features der Knowledge Base demonstriert:

- ✅ Operatoren-Definitionen abrufen
- ✅ Pattern-Templates verwenden
- ✅ BW-Notation-Regeln (Briefumschlag-Alternative, etc.)
- ✅ Operatoren nach Kategorie filtern
- ✅ Syntax-Validierung
- ✅ Zusammenfassung exportieren

**Ausführung:**

```bash
cd /workspaces/python-algorithmen-datenstrukturen
PYTHONPATH=$PWD:$PYTHONPATH python examples/struktogramm_knowledge_base_beispiele.py
```

## Quick Start

```python
from src.utils.struktogramm_knowledge_base import get_knowledge_base

# Knowledge Base initialisieren
kb = get_knowledge_base()

# Operator abrufen
op = kb.get_operator("deklaration")
print(op.syntax)  # "Deklaration: variable |als datentyp|"

# Pattern-Template abrufen
pattern = kb.get_pattern_template("array_durchlaufen")
print(pattern)

# Notation-Regel abrufen  
regel = kb.get_notation_regel("briefumschlag_alternative")
print(regel['template'])
```

## Weitere Ressourcen

- **Wissensdatenbank:** `src/utils/struktogramm_knowledge_base.py`
- **Guide:** `docs/handbuch/STRUKTOGRAMM_GUIDE.md`
- **Migration-Docs:** `STRUKTOGRAMM_MIGRATION_2026.md`
- **Archiv:** `archiv/struktogramme/` (alte Beispiele)
