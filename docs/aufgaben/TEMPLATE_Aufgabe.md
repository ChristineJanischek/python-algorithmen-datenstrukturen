---
titel: "[TITEL DER AUFGABE]"
level: L1  # L1, L2 oder L3
kategorie: 1  # 1=Grundlagen, 2=Sortieren, 3=Suchen, 4=Vertiefung, etc.
nummer: 1  # Laufende Nummer
autor: "[DEIN NAME]"
datum: 05.02.2026
version: 1.0
themen:
  - [Thema 1]
  - [Thema 2]
lernziele:
  - [Lernziel 1]
  - [Lernziel 2]
voraussetzungen:
  - [Voraussetzung 1]
  - [Voraussetzung 2]
zeitaufwand: "[X] Minuten"
schwierigkeitsgrad: "Einfach/Mittel/Schwer"
---

# Aufgabe: [TITEL DER AUFGABE]

## 📋 Übersicht

- **Level:** [L1/L2/L3]
- **Kategorie:** [Nummer]
- **Zeitaufwand:** [X Minuten]
- **Schwierigkeitsgrad:** [Einfach/Mittel/Schwer]

**Themen:**
- [Thema 1]
- [Thema 2]

**Lernziele:**
- [Lernziel 1]
- [Lernziel 2]

**Voraussetzungen:**
- [Voraussetzung 1]
- [Voraussetzung 2]

## 📝 Problemstellung

[Hier die Problemstellung beschreiben. Was soll das Programm tun?]

[Detaillierte Beschreibung mit konkreten Anforderungen:]
1. [Anforderung 1]
2. [Anforderung 2]
3. [Anforderung 3]

## 📊 Struktogramm

```
[Hier das Struktogramm nach BW-Standard einfügen]
[Verwende struktogramm_helper.py oder erstelle manuell]

Beispiel:
Deklaration und Initialisierung: summe = 0
Zähle i von 0 bis n - 1, Schrittweite 1
    Zuweisung: summe = summe + zahlen[i]
Ausgabe: "Summe: " + summe
```

## 💡 Hinweise

[Optional: Hilfreiche Tipps für die Lösung]
- [Hinweis 1]
- [Hinweis 2]
- [Hinweis 3]

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
**Eingabe:**
```
[Test-Eingabe 1]
```

**Erwartete Ausgabe:**
```
[Test-Ausgabe 1]
```

### Test 2
**Eingabe:**
```
[Test-Eingabe 2]
```

**Erwartete Ausgabe:**
```
[Test-Ausgabe 2]
```

### Test 3
**Eingabe:**
```
[Test-Eingabe 3]
```

**Erwartete Ausgabe:**
```
[Test-Ausgabe 3]
```

## 🔥 Zusatzaufgaben

[Optional: Erweiterungen und Herausforderungen]
1. [Zusatzaufgabe 1]
2. [Zusatzaufgabe 2]
3. [Zusatzaufgabe 3]

---

*Erstellt am [Datum] von [Autor]*

---

## 📝 Verwendungshinweis

**Dieses Template NICHT direkt verwenden!**

Stattdessen mit Python Manager erstellen:

```python
from src.utils.elearning_manager import *

manager = ELearningManager()

aufgabe = create_aufgabe_quick(
    titel="Titel der Aufgabe",
    level=Level.L1,
    kategorie=1,
    nummer=1,
    problemstellung="...",
    autor="Dein Name"
)

# Optional: Details hinzufügen
aufgabe.metadata.themen = ["Thema1", "Thema2"]
aufgabe.metadata.lernziele = ["Ziel1", "Ziel2"]
aufgabe.struktogramm = "..."
aufgabe.beispiel_eingabe = "..."
aufgabe.beispiel_ausgabe = "..."

manager.save_aufgabe(aufgabe)
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
