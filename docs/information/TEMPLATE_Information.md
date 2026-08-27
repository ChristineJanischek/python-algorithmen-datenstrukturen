---
titel: "[TITEL DER INFORMATION]"
level: L1  # L1, L2 oder L3
kategorie: 1  # 1=Grundlagen, 2=Sortieren, 3=Suchen, 4=Vertiefung, etc.
nummer: 1  # Laufende Nummer
autor: "[DEIN NAME]"
datum: 05.02.2026
version: 1.0
themen:
  - [Thema 1]
  - [Thema 2]
voraussetzungen:
  - [Voraussetzung 1]
  - [Voraussetzung 2]
zeitaufwand: "[X] Minuten Lesezeit"
---

# Information: [TITEL DER INFORMATION]

## 📚 Übersicht

- **Level:** [L1/L2/L3]
- **Kategorie:** [Nummer]
- **Lesezeit:** [X Minuten]

**Themen:**
- [Thema 1]
- [Thema 2]

**Voraussetzungen:**
- [Voraussetzung 1]
- [Voraussetzung 2]

## 🎯 Einführung

[Kurze Einführung ins Thema - 2-3 Sätze]

[Was wird der Leser lernen?]

## 📖 Inhalt

### [Unterabschnitt 1]

[Hauptinhalt - erster Teil]

[Erklärungen, Definitionen, Konzepte]

### [Unterabschnitt 2]

[Hauptinhalt - zweiter Teil]

**Wichtige Punkte:**
- [Punkt 1]
- [Punkt 2]
- [Punkt 3]

### [Unterabschnitt 3]

[Hauptinhalt - dritter Teil]

[Diagramme, Tabellen, etc. können hier eingefügt werden]

## 💡 Beispiele

### Beispiel 1: [Titel]

[Beschreibung des ersten Beispiels]

```python
# Python-Code
[Code-Beispiel]
```

**Erklärung:**
[Erklärung des Codes]

### Beispiel 2: [Titel]

[Beschreibung des zweiten Beispiels]

```python
# Python-Code
[Code-Beispiel]
```

**Erklärung:**
[Erklärung des Codes]

## 📝 Zusammenfassung

**Die wichtigsten Punkte:**
- [Punkt 1]
- [Punkt 2]
- [Punkt 3]
- [Punkt 4]

**Merke:**
[Ein prägnanter Satz zum Merken]

## 🔗 Weiterführende Themen

- [Weiterführendes Thema 1]
- [Weiterführendes Thema 2]
- [Weiterführendes Thema 3]

## 📚 Ressourcen

- Titel der Ressource 1: link/pfad/zur/ressource1
- Titel der Ressource 2: link/pfad/zur/ressource2
- Titel der Ressource 3: link/pfad/zur/ressource3

## 🧪 Übungsaufgaben

[Optional: Kleine Übungen zum Selbsttest]

1. [Übungsfrage 1]
2. [Übungsfrage 2]
3. [Übungsfrage 3]

**Lösungen:**
<details>
<summary>Klicke hier für die Lösungen</summary>

1. [Lösung 1]
2. [Lösung 2]
3. [Lösung 3]

</details>

---

*Erstellt am [Datum] von [Autor]*

---

## 📝 Verwendungshinweis

**Dieses Template NICHT direkt verwenden!**

Stattdessen mit Python Manager erstellen:

```python
from src.utils.elearning_manager import *

manager = ELearningManager()

info = create_information_quick(
    titel="Titel der Information",
    level=Level.L1,
    kategorie=1,
    nummer=1,
    einfuehrung="Kurze Einführung...",
    inhalt="Hauptinhalt...",
    autor="Dein Name"
)

# Optional: Details hinzufügen
info.metadata.themen = ["Thema1", "Thema2"]
info.metadata.zeitaufwand = "10 Minuten"
info.beispiele = "..."
info.zusammenfassung = "..."
info.weiterführende_themen = ["Thema A", "Thema B"]
info.ressourcen = [
    ("Titel", "link/pfad"),
    ("Titel2", "link/pfad2")
]

manager.save_information(info)
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
