# Assoziationen zwischen Person, Messung und BMI-Rechner

## Übersicht

Dieses Dokument beschreibt die Assoziationen zwischen den Klassen `Person`, `Messung` und `Bmirechner` für die BMI-App Version 3.

## Klassendiagramm

```
Person (N) ←──── (1) Messung (N) ────→ (1) Bmirechner
```

## Assoziationen

### 1. Bmirechner (1) - Messung (N)

**Bedeutung**: Ein BMI-Rechner kann mehrere Messungen durchführen, aber jede Messung gehört zu genau einem BMI-Rechner.

**Kardinalität**: 1:N
- Ein `Bmirechner` kann 0 bis N `Messung`-Objekte haben
- Jede `Messung` gehört zu genau einem `Bmirechner`

**Implementierung**:
- `Bmirechner` hat eine Liste von `Messung`-Objekten
- `Messung` hat eine Referenz auf ein `Bmirechner`-Objekt

### 2. Messung (1) - Person (N)

**Bedeutung**: Eine Messung wird für genau eine Person durchgeführt, aber eine Person kann mehrere Messungen haben.

**Kardinalität**: N:1 (oder 1:N von Person aus gesehen)
- Eine `Messung` gehört zu genau einer `Person`
- Eine `Person` kann 0 bis N `Messung`-Objekte haben

**Implementierung**:
- `Person` hat eine Liste von `Messung`-Objekten
- `Messung` hat eine Referenz auf ein `Person`-Objekt

## Klassenverantwortlichkeiten

### Person
- Speichert persönliche Daten (Name, Geburtsdatum, etc.)
- Verwaltet eine Liste eigener Messungen
- Kann neue Messungen hinzufügen
- Kann Messungshistorie anzeigen

### Messung
- Speichert Messdaten (Gewicht, Größe, Datum)
- Referenziert die zugehörige Person
- Referenziert den verwendeten BMI-Rechner
- Kann BMI-Wert berechnen lassen

### Bmirechner
- Führt BMI-Berechnungen durch
- Verwaltet eine Liste durchgeführter Messungen
- Kann Statistiken über alle Messungen erstellen
- Kann BMI-Kategorien zuordnen (Untergewicht, Normalgewicht, etc.)

## Verwendungsbeispiel

```python
# Person erstellen
person = Person("Max Mustermann", "1990-01-01")

# BMI-Rechner erstellen
rechner = Bmirechner("Standard BMI Rechner")

# Messung durchführen
messung = Messung(75.5, 1.80, "2024-02-04", person, rechner)

# Die Assoziationen werden automatisch gesetzt:
# - person.messungen enthält die neue Messung
# - rechner.messungen enthält die neue Messung
```

## Version 3 Erweiterungen

Version 3 baut auf Version 2 auf und fügt die bidirektionalen Assoziationen hinzu:

1. **Version 2**: Einfache Klassen ohne Assoziationen
2. **Version 3**: Vollständige bidirektionale Assoziationen zwischen den Klassen

Die Assoziationen ermöglichen:
- Navigation von Person zu allen ihren Messungen
- Navigation von Messung zur zugehörigen Person
- Navigation von Messung zum verwendeten BMI-Rechner
- Navigation vom BMI-Rechner zu allen durchgeführten Messungen
