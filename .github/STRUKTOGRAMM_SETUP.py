"""
SETUP-ANLEITUNG: Struktogramm-Validierungssystem
================================================

Dieses System stellt sicher, dass für alle Programmlogik in docs/ ausschließlich
die grafische Struktogramm-Notation verwendet wird.

KOMPONENTEN:
============

1. **struktogramm_validator.py**
   - Überprüft alle Dateien in docs/ auf korrekte Notation
   - Erzeugt einen Validierungsbericht

2. **elearning_manager.py** (erweitert)
   - Neue Methode: validate_struktogramm_usage()
   - Warnt beim Speichern, wenn Validierungsfehler vorhanden sind

3. **Pre-Commit Hook** (.github/hooks/pre-commit-struktogramm)
   - Lädt vor jedem git commit die Validierung
   - Warnt wenn Probleme gefunden werden

4. **Integrations-Guide** (docs/handbuch/STRUKTOGRAMM_INTEGRATION_GUIDE.md)
   - Richtlinien für korrekte Struktur
   - Beispiele für korrekte Notation

MANUAL SETUP:
=============

1. Hook installieren:
   ```bash
   cp .github/hooks/pre-commit-struktogramm .git/hooks/pre-commit
   chmod +x .git/hooks/pre-commit
   ```

2. Validator testen:
   ```bash
   python -m src.utils.struktogramm_validator
   ```

3. Bericht anschauen:
   ```bash
   cat validation_report.md
   ```

VERWENDUNG:
===========

### Für Aufgaben-Autoren (docs/aufgaben/):
```markdown
# Aufgabe: Beispiel

## Problemstellung
[Aufgabenbeschreibung]

## Anforderungen
[Was muss implementiert werden]

## Hinweis zur Lösung
<!-- STRUKTOGRAMM_REQUIRED -->
Die Lösung sollte ein Struktogramm mit grafischer Notation enthalten!
```

### Für Lösungs-Autoren (docs/loesungen/):
```markdown
# Lösung: Beispiel

## 📐 Struktogramm (grafische Notation)

```
┌──────────────────────────────────────┐
│ Deklaration: variable als Ganzzahl   │
├──────────────────────────────────────┤
│ Zuweisung: variable = 5              │
└──────────────────────────────────────┘
```

## 💻 Python-Implementierung

```python
variable = 5
print(variable)
```
```

### Für Prüfungs-Autoren (docs/pruefungen/):
```markdown
**Erwartetes Struktogramm (BW-Standard - Grafische Notation):**

```
┌──────────────────────────────────────┐
│ [Grafische Notation mit ┌ ├ └ │ ─]   │
└──────────────────────────────────────┘
```

**Python-Code (Musterlösung):**
```python
[Python-Code hier]
```
```

GRAFISCHE BOX-ZEICHEN:
======================

▹ ┌  = oben-links
▹ ┐  = oben-rechts
▹ ├  = links-mittig
▹ ┤  = rechts-mittig
▹ ┬  = oben-mittig
▹ ┴  = unten-mittig
▹ │  = senkrecht
▹ ─  = waagrecht
▹ └  = unten-links
▹ ┘  = unten-rechts
▹ ├─ = Verschachtelung nach links (für Schleifen)

HÄUFIGE FEHLER:
===============

❌ FALSCH:
```python
def beispiel():
    for i in range(10):
        print(i)
```

✅ RICHTIG:
```
┌──────────────────────────────────┐
│ ┌─ Zähle i von 0 bis 9           │
│ │                                │
│ │    Ausgabe: i                  │
│ │                                │
└─┘──────────────────────────────────┘
```

AUTOMATISCHE VALIDIERUNG:
=========================

Die Validierung läuft automatisch:
1. Im Pre-Commit Hook (vor git commit)
2. Bei Verwendung von elearning_manager.save_*() methoden
3. Mit `python -m src.utils.struktogramm_validator`

HILFREICHE RESSOURCEN:
======================

▹ docs/handbuch/STRUKTOGRAMM_INTEGRATION_GUIDE.md - Detaillierte Richtlinien
▹ struktogramme/Operatorenliste-Struktogramme.md - Vollständige Operator-Liste  
▹ docs/handbuch/STRUKTOGRAMM_GUIDE.md - Praktische Beispiele
▹ src/utils/struktogramm_validator.py - Source des Validators
▹ src/utils/elearning_manager.py - Manager mit Validierung

FRAGEN & SUPPORT:
=================

Bei Fragen zur Validierung:
1. Überprüfe validation_report.md
2. Siehe STRUKTOGRAMM_INTEGRATION_GUIDE.md
3. Benutze validate_struktogramm_usage() für Details

---

Implementiert: 16.02.2026
Version: 1.0
"""

# IMPLEMENTIERUNGS-SCRIPT
# Führe folgende Befehle aus:

if __name__ == "__main__":
    print(__doc__)
