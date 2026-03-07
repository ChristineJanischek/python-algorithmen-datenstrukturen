---
# 🎓 AUFGABEN-TEMPLATE: KLAUSUR-STANDARD
# Basierend auf: BW-Abitur Struktur & Musteraufgaben
# Version: 1.0 | Datum: 07.03.2026

titel: "[AUFGABENTITEL]"
level: L1  # L1=Grundlagen, L2=Sortieren/Suchen, L3=Expert
kategorie: 1  # 1=Verzweigung, 2=Schleifen, 3=Arrays, 4=Sortieralgorithmen, 5=Suchalgorithmen, 6=Analyse
nummer: 1  # Laufende Nummer innerhalb Kategorie + Level
autor: "[AUTHOR]"
datum: "07.03.2026"
version: "1.0"

# ========== QUALITÄTSSTANDARDS ==========
# Wird für Varianz-Tracking verwendet

content_variation_hash: "" # SHA-256 des Aufgabentextes (wird auto-generiert)
thema_id: "" # Eindeutige Thema-ID (z.B. "L1_1_Verzweigung")
varianz_index: 0  # Aufgabenvarianz (0=erste, 1=zweite Variante etc.)
inhaltliche_variation:
  - "Kontext: [Beschreibung des Anwendungsfall]"
  - "Datentypen: [int, str, list, etc.]"
  - "Besonderheit: [Was unterscheidet diese vom Standard?]"

themen:
  - "[Hauptthema]"
  - "[Nebenthema]"

lernziele:
  - "[Lernziel 1 - AKTIV: Die Schüler können...]"
  - "[Lernziel 2]"

voraussetzungen:
  - "[Voraussetzung 1]"
  - "[Voraussetzung 2]"

# ========== PUNKTE & UMFANG ==========
punkte:
  gesamt: 3  # Summe aller Teilaufgaben
  gewichtung: "" # BW-Standard: 3pt, 6pt, 8pt etc.
  
umfang:
  zeitaufwand_minuten: 5  # Schätzung für durchschnittlichen Schüler
  schwierigkeitsgrad: "Einfach"  # Einfach / Mittel / Schwer
  unterkategorien: 1  # Anzahl Teilaufgaben (a), b), etc.)

# ========== STRUKTUR ==========
struktur:
  hat_struktogramm: true  # Wird ein Struktogramm benötigt?
  hat_code: true          # Wird Python-Code benötigt?
  hat_analyse: false      # Wird eine Text-Analyse benötigt?
  hat_beispiel: true      # Werden Beispiele/Testfälle gegeben?
---

# 🎯 Aufgabe [NUMMER]: [AUFGABENTITEL]

## 📌 Übersicht

| Eigenschaft | Wert |
|---|---|
| **Level** | [L1/L2/L3] |
| **Kategorie** | [Kategorie] |
| **Punkte** | [X] Punkte |
| **Zeitaufwand** | [X] Minuten |
| **Schwierigkeitsgrad** | Einfach/Mittel/Schwer |

**Themen:**
- [Thema 1]
- [Thema 2]

**Lernziele:**
Schüler können nach dieser Aufgabe:
- [Lernziel 1]
- [Lernziel 2]

**Voraussetzungen:**
- [Voraussetzung 1]
- [Voraussetzung 2]

---

## 📝 Problemstellung

[Kurze Zusammenfassung des Problems in 1-2 Sätzen]

> [Hauptproblemstellung in größerem Kontext]

### Anforderungen:
1. [Anforderung 1]
2. [Anforderung 2]
3. [Anforderung 3]

### Kontext/Anwendungsfall:
[Realweltlicher Kontext - warum ist diese Aufgabe relevant?]

---

## 📊 Teilaufgabe a) [TITEL] ([X] Punkte)

**BW-Thema:** [z.B. BPE 5.2 – Kontrollstrukturen]

[Beschreibung der Teilaufgabe]

**Anforderungen:**
- [Anforderung 1]
- [Anforderung 2]

### Struktogramm (falls erforderlich)
```
[Textbasierte Notation nach BW-Operatorenliste]

Beispiel:
Wenn bedingung, dann
    J
        Ausgabe: "Text"
    , sonst
    N
        Zuweisung: x = 5
```

### Python-Code (falls erforderlich)
```python
# Lösung mit korrekter Syntax
# Verwende Type Hints!

def function_name(parameter: type) -> type:
    """Docstring"""
    # Code hier...
    pass
```

---

## 📊 Teilaufgabe b) [TITEL] ([X] Punkte)

[Analoge Struktur wie Teilaufgabe a)]

---

## 💡 Hinweise

- [Hinweis 1 - optional]
- [Hinweis 2 - optional]
- [Hinweis 3 - optional]

---

## 🧪 Beispiel/Testfall

**Eingabe:**
```
[Beispiel-Eingabe]
```

**Erwartete Ausgabe:**
```
[Beispiel-Ausgabe]
```

**Erklärung:**
[Kurze Erklärung, was hier passiert]

---

## ✅ Akzeptanzkriterien

- [ ] Struktogramm nach BW-Standard (falls erforderlich)
- [ ] Python-Code syntaktisch korrekt
- [ ] Type Hints vorhanden
- [ ] Ausgabe entspricht erwartetem Resultat
- [ ] Logik klar und nachvollziehbar dokumentiert
- [ ] Bei Algorithmen: Eigene Schleifenlösungen (keine Built-ins)

---

## 📚 Lösungsvorlage  

### Lösung a)
[Hier später von System gefüllt]

### Lösung b)
[Hier später von System gefüllt]

---

## 🔗 Verwandte Ressourcen

- **Theoretische Grundlage:** [Link zum Information-Material]
- **Ähnliche Aufgaben:** [Links zu anderen Aufgaben im gleichen Level/Kategorie]
- **Struktogramm-Patterns:** [Link zum Pattern aus Guide]

---

## 📌 Metadaten (für System)

```
Erstellt: [Datum]
Modifiziert: [Datum]
Status: Entwurf / Gültig / Archiviert
E-Learning-ID: [wird vom System generiert]
Komponenten: [aufgabe_l1_1_001.md]
```

---

**Viel Erfolg! 🚀**
