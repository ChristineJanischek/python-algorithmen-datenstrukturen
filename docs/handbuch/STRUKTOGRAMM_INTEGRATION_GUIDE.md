"""
Marker für Struktogramm-Bereiche in Markdown-Dateien

Diese Dokumentation erklärt, wie Programmlogik in docs/-Dateien standardisiert werden sollte.
"""

# ============================================================================
# RICHTLINIEN FÜR STRUKTOGRAMM-NOTATION IN DOCS/
# ============================================================================

# Für AUFGABEN (docs/aufgaben/):
# ────────────────────────────────────────────────────────────────────────
#
# Struktur:
# 1. Problemstellung
# 2. Anforderungen
# 3. <!-- STRUKTOGRAMM_REQUIRED -->
#    (Hier sollte das Struktogramm in GRAFISCHER Notation stehen)
# 4. Lösungsanforderungen
#
# Beispiel Flag:
# <!-- STRUKTOGRAMM_REQUIRED: Zeige die Lösung mit grafischem Struktogramm -->


# Für LÖSUNGEN (docs/loesungen/):
# ────────────────────────────────────────────────────────────────────────
#
# Struktur:
# 1. Übersicht
# 2. Lösungsansatz (kurze textliche Erklärung)
# 3. ## 📐 Struktogramm (grafische Notation)
#    ```
#    ┌──────────────────────┐
#    │ [Grafisches Struktogramm]
#    └──────────────────────┘
#    ```
# 4. ## 💻 Python-Implementierung
#    ```python
#    [Python-Code]
#    ```
# 5. Erklärung & Analyse


# Für PRÜFUNGEN (docs/pruefungen/):
# ────────────────────────────────────────────────────────────────────────
#
# Struktur:
# **Erwartetes Struktogramm (BW-Standard - Grafische Notation):**
# ```
# ┌──────────────────────┐
# │ [Grafisches Struktogramm]
# └──────────────────────┘
# ```
# **Python-Code (Musterlösung):**
# ```python
# [Python-Code]
# ```


# ============================================================================
# VALIDIERUNGS-REGELN
# ============================================================================

RULES = {
    "loesungen": {
        "required_sections": [
            "## 💻 Python-Implementierung",  # Python-Code muss NACH Struktogramm kommen
        ],
        "pattern_check": {
            "python_code_before_struktogramm": False,  # Fehler
            "graphic_struktogramm_before_code": True,   # Erforderlich
        },
    },
    "pruefungen": {
        "required_before_python": [
            "Grafische Notation",
            "Struktogramm",
            "┌",  # Grafische Box-Zeichnungselemente
        ],
        "pattern_check": {
            "python_must_have_struktogramm_before": True,
        },
    },
}

# ============================================================================
# IMPLEMENTIERUNG: Markieren von Bereichen mit Kommentaren
# ============================================================================

STRUKTOGRAMM_MARKERS = {
    "start_graphic": "<!-- START_GRAPHIC_STRUKTOGRAMM -->",
    "end_graphic": "<!-- END_GRAPHIC_STRUKTOGRAMM -->",
    "needs_review": "<!-- NEEDS_STRUKTOGRAMM_REVIEW -->",
    "approved": "<!-- STRUKTOGRAMM_APPROVED -->",
}

# ============================================================================
# BEISPIEL FÜR KORREKTE STRUKTUR (FÜR LÖSUNGEN)
# ============================================================================

TEMPLATE_SOLUTION = """
---
titel: "Beispiel-Lösung"
level: L1
kategorie: 1
nummer: 1
---

# Lösung: Beispiel

## 📋 Übersicht
- **Level:** L1
- Kurze Beschreibung

## 💡 Lösungsansatz

Wir verwenden eine Schleife, um...

## 📐 Struktogramm (grafische Notation)

<!-- START_GRAPHIC_STRUKTOGRAMM -->
```
┌────────────────────────────────────────┐
│ Deklaration:                           │
│ variable als Ganzzahl                  │
├────────────────────────────────────────┤
│ ┌─ Zähle i von 0 bis n - 1             │
│ │  Ausgabe:                            │
││ i                                     │
└────────────────────────────────────────┘
```
<!-- END_GRAPHIC_STRUKTOGRAMM -->

## 💻 Python-Implementierung

```python
def example():
    for i in range(n):
        print(i)
```

## 📝 Erklärung

Die Lösung funktioniert wie folgt:
1. ...
2. ...
"""
