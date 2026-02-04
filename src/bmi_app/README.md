# BMI App - Body Mass Index Anwendung

## Übersicht

Die BMI App ist eine Python-Anwendung zur Berechnung und Verwaltung von Body Mass Index (BMI) Messungen. Sie demonstriert objektorientierte Programmierung mit Assoziationen zwischen Klassen.

## Versionen

### Version 2 (Baseline)
Grundlegende Implementierung der drei Hauptklassen ohne Assoziationen:
- `Person`: Repräsentiert eine Person mit Namen und Geburtsdatum
- `Messung`: Repräsentiert eine BMI-Messung mit Gewicht und Größe
- `Bmirechner`: Berechnet BMI-Werte und klassifiziert diese

### Version 3 (Mit Assoziationen)
Erweiterte Implementierung mit bidirektionalen Assoziationen:
- **Person (1) ↔ Messung (N)**: Eine Person kann mehrere Messungen haben
- **Bmirechner (1) ↔ Messung (N)**: Ein BMI-Rechner kann mehrere Messungen durchführen
- **Messung (N) → Person (1)**: Jede Messung gehört zu genau einer Person
- **Messung (N) → Bmirechner (1)**: Jede Messung wird von genau einem BMI-Rechner durchgeführt

## Verzeichnisstruktur

```
src/bmi_app/
├── assoziation_person_messung.md  # Dokumentation der Assoziationen
├── version2/                       # Baseline ohne Assoziationen
│   ├── __init__.py
│   ├── person.py
│   ├── messung.py
│   └── bmirechner.py
├── version3/                       # Mit bidirektionalen Assoziationen
│   ├── __init__.py
│   ├── person.py
│   ├── messung.py
│   └── bmirechner.py
└── demo_version3.py               # Demonstrationsskript
```

## Installation

Keine speziellen Abhängigkeiten erforderlich. Die Anwendung benötigt nur Python 3.x.

## Verwendung

### Demo ausführen

```bash
cd src/bmi_app
python demo_version3.py
```

Das Demonstrationsskript zeigt:
1. Erstellung von Personen
2. Erstellung von BMI-Rechnern
3. Erstellung von Messungen mit automatischen Assoziationen
4. Navigation durch die Assoziationen
5. Dynamische Änderung von Assoziationen
6. Anzeige von Statistiken

### Verwendung in eigenem Code (Version 3)

```python
from version3.person import Person
from version3.messung import Messung
from version3.bmirechner import Bmirechner

# Person erstellen
person = Person("Max Mustermann", "1990-01-01")

# BMI-Rechner erstellen
rechner = Bmirechner("Standard BMI Rechner")

# Messung durchführen (Assoziationen werden automatisch gesetzt)
messung = Messung(75.5, 1.80, "2024-02-04", person, rechner)

# Messungshistorie anzeigen
person.zeige_messungshistorie()

# Statistiken anzeigen
rechner.zeige_statistik()
```

## Klassendiagramm

```
┌──────────────┐         ┌──────────────┐         ┌──────────────┐
│   Person     │         │   Messung    │         │ Bmirechner   │
├──────────────┤         ├──────────────┤         ├──────────────┤
│ name         │◄────N───│ gewicht      │───N────►│ name         │
│ geburtsdatum │    1    │ groesse      │    1    │ messungen[]  │
│ messungen[]  │         │ datum        │         ├──────────────┤
├──────────────┤         │ _person      │         │ berechne_bmi()│
│ fuege_       │         │ _bmirechner  │         │ klassifiziere│
│ messung_hinzu│         ├──────────────┤         │ _bmi()       │
│ zeige_       │         │ berechne_bmi()│         │ zeige_       │
│ messungen()  │         │ setze_person()│         │ statistik()  │
└──────────────┘         │ setze_bmirechner()│     └──────────────┘
                         └──────────────┘
```

## BMI-Kategorien

Der BMI-Rechner klassifiziert BMI-Werte nach WHO-Standard:

| BMI-Wert | Kategorie      |
|----------|----------------|
| < 18.5   | Untergewicht   |
| 18.5-24.9| Normalgewicht  |
| 25-29.9  | Übergewicht    |
| ≥ 30     | Adipositas     |

## Features

### Person-Klasse
- Speichert Name und Geburtsdatum
- Verwaltet Liste eigener Messungen
- Zeigt Messungshistorie an

### Messung-Klasse
- Speichert Gewicht, Größe und Datum
- Berechnet BMI-Wert
- Verwaltet bidirektionale Assoziationen zu Person und Bmirechner
- Ermöglicht Änderung der Assoziationen

### Bmirechner-Klasse
- Berechnet BMI-Werte
- Klassifiziert BMI-Werte in Kategorien
- Verwaltet Liste durchgeführter Messungen
- Erstellt Statistiken über alle Messungen (Durchschnitt, Min, Max, Verteilung)

## Didaktische Ziele

Diese Anwendung demonstriert:
- **Objektorientierte Programmierung**: Klassen, Objekte, Kapselung
- **Assoziationen**: Bidirektionale 1:N und N:1 Beziehungen
- **Konsistenz**: Automatische Synchronisation der Assoziationen
- **Navigation**: Traversierung durch Objektstrukturen
- **Datenverarbeitung**: Berechnungen und Statistiken

## Autor

Christine Janischek

## Lizenz

Dieses Projekt ist Teil des Repositories "python-algorithmen-datenstrukturen".
