# Struktogramm-Erstellungs-Guide

**Version:** 1.0  
**Basis:** Operatorenliste für Struktogramme v2.2 (Abiturprüfung Baden-Württemberg)  
**Letzte Aktualisierung:** 05.02.2026

## Zweck dieses Guides

Dieser Guide hilft bei der **Erstellung von Struktogrammen nach den Baden-Württemberg-Abitur-Standards**. Er richtet sich an:
- Lehrkräfte und Studierende
- KI-Assistenten (z.B. GitHub Copilot)
- Alle, die sprachunabhängige Programmlogik darstellen möchten

## Schnellreferenz: Die wichtigsten Operatoren

| Operator | Syntax | Beispiel |
|----------|--------|----------|
| **Deklaration** | `Deklaration: variable \|als datentyp\|` | `Deklaration: alter als Ganzzahl` |
| **Initialisierung** | `Initialisierung: variable = wert` | `Initialisierung: summe = 0` |
| **Dekl. + Init.** | `Deklaration und Initialisierung: variable = wert` | `Deklaration und Initialisierung: zaehler = 1` |
| **Zuweisung** | `Zuweisung: variable = wert` | `Zuweisung: produkt = a * b` |
| **Einlesen** | `Einlesen: variable \|als datentyp\|` | `Einlesen: name als Text` |
| **Ausgabe** | `Ausgabe: inhalt` | `Ausgabe: "Hallo " + name` |
| **Rückgabe** | `Rückgabe: wert` | `Rückgabe: ergebnis` |
| **Aufruf** | `Aufruf: methode(\|parameter\|)` | `Aufruf: berechne(wert)` |
| **Verzweigung** | `Wenn bedingung, dann [...] \|, sonst [...]\|` | `Wenn alter >= 18, dann J [...] , sonst N [...]` |
| **While-Schleife** | `Wiederhole solange bedingung` | `Wiederhole solange i < 10` |
| **For-Schleife (Var. 1)** | `Wiederhole von start solange bedingung, Schrittweite n` | `Wiederhole von i = 0 solange i < 5, Schrittweite 1` |
| **For-Schleife (Var. 2)** | `Zähle var von start bis ende, Schrittweite n` | `Zähle i von 0 bis 4, Schrittweite 1` |

## Textbasierte Struktogramm-Notation

Bei der textbasierten Darstellung verwenden wir Einrückungen und Schlüsselwörter:

### Grundstruktur

```
┌─────────────────────────────────────┐
│ [Operator]:                         │
│ [Details]                           │
└─────────────────────────────────────┘
```

### Verzweigung

```
┌────────────────────────────────────────────────────────┐
│                    [Bedingung]                         │
├────────────────────────────────────────────────────────┤
│ J                              │ N                     │
│                                │                       │
│ [Anweisungen für Ja]           │ [Anweisungen für Nein]│
│                                │                       │
└────────────────────────────────────────────────────────┘
```

### Schleife

```
┌──────────────────────────────────────────────────────┐
│ ┌─ [Schleifenkopf]                                   │
│ │                                                    │
│ │  [Anweisungen im Schleifenkörper]                  │
│ │                                                    │
└──────────────────────────────────────────────────────┘
```

## Schritt-für-Schritt: Struktogramm erstellen

### Schritt 1: Problem analysieren

**Fragen:**
- Was sind die Ein- und Ausgaben?
- Welche Variablen/Arrays werden benötigt?
- Gibt es Bedingungen? (if/else)
- Gibt es Wiederholungen? (Schleifen)
- Werden Funktionen/Methoden aufgerufen?

### Schritt 2: Variablen planen

Alle benötigten Variablen mit Datentyp auflisten:

```
Deklaration und Initialisierung: zaehler als Ganzzahl = 0
Deklaration und Initialisierung: summe als Dezimalzahl = 0.0
Deklaration und Initialisierung: namen als Array = [ ]
```

### Schritt 3: Eingaben definieren

```
Einlesen: alter als Ganzzahl
Einlesen: name als Text
```

### Schritt 4: Logik aufbauen

- **Sequenz:** Anweisungen nacheinander ausführen
- **Verzweigung:** `Wenn ... dann ... sonst`
- **Schleife:** `Wiederhole solange` oder `Zähle ... von ... bis`

### Schritt 5: Ausgaben definieren

```
Ausgabe: "Das Ergebnis ist: " + ergebnis
```

### Schritt 6: Für Funktionen: Rückgabe

```
Rückgabe: ergebnis
```

## Typische Patterns für häufige Aufgaben

### Pattern 1: Array durchlaufen (alle Elemente)

```
Deklaration und Initialisierung: daten = [10, 20, 30, 40, 50]
Deklaration und Initialisierung: n = Anzahl der Elemente des Arrays daten
Zähle i von 0 bis n - 1, Schrittweite 1
    Ausgabe: daten[i]
```

**Grafisch:**
```
┌─────────────────────────────────────────────────────┐
│ Deklaration und Initialisierung:                    │
│ daten = [10, 20, 30, 40, 50]                        │
├─────────────────────────────────────────────────────┤
│ Deklaration und Initialisierung:                    │
│ n = Anzahl der Elemente des Arrays daten            │
├─────────────────────────────────────────────────────┤
│ ┌─ Zähle i von 0 bis n - 1, Schrittweite 1          │
│ │                                                   │
│ │    Ausgabe:                                       │
││ daten[i]                                           │
│ │                                                   │
└─────────────────────────────────────────────────────┘
```

---

### Pattern 2: Summe berechnen

```
Deklaration und Initialisierung: summe = 0
Deklaration und Initialisierung: zahlen = [5, 10, 15, 20]
Deklaration und Initialisierung: n = Anzahl der Elemente des Arrays zahlen
Zähle i von 0 bis n - 1, Schrittweite 1
    Zuweisung: summe = summe + zahlen[i]
Ausgabe: "Summe: " + summe
```

**Grafisch:**
```
┌─────────────────────────────────────────────────────┐
│ Deklaration und Initialisierung:                    │
│ summe = 0                                           │
├─────────────────────────────────────────────────────┤
│ Deklaration und Initialisierung:                    │
│ zahlen = [5, 10, 15, 20]                            │
├─────────────────────────────────────────────────────┤
│ Deklaration und Initialisierung:                    │
│ n = Anzahl der Elemente des Arrays zahlen           │
├─────────────────────────────────────────────────────┤
│ ┌─ Zähle i von 0 bis n - 1, Schrittweite 1          │
│ │                                                   │
│ │    Zuweisung:                                     │
││ summe = summe + zahlen[i]                          │
│ │                                                   │
└─────────────────────────────────────────────────────┘
│ Ausgabe:                                            │
│ "Summe: " + summe                                   │
└─────────────────────────────────────────────────────┘
```

---

### Pattern 3: Maximum finden

```
Deklaration und Initialisierung: zahlen = [3, 7, 2, 9, 1]
Deklaration und Initialisierung: max = zahlen[0]
Deklaration und Initialisierung: n = Anzahl der Elemente des Arrays zahlen
Zähle i von 1 bis n - 1, Schrittweite 1
    Wenn zahlen[i] > max, dann
        J
            Zuweisung: max = zahlen[i]
        , sonst
        N
            (nichts)
Ausgabe: "Maximum: " + max
```

**Grafisch:**
```
┌───────────────────────────────────────────────────────┐
│ Deklaration und Initialisierung:                      │
│ zahlen = [3, 7, 2, 9, 1]                              │
├───────────────────────────────────────────────────────┤
│ Deklaration und Initialisierung:                      │
│ max = zahlen[0]                                       │
├───────────────────────────────────────────────────────┤
│ Deklaration und Initialisierung:                      │
│ n = Anzahl der Elemente des Arrays zahlen             │
├───────────────────────────────────────────────────────┤
│ ┌─ Zähle i von 1 bis n - 1, Schrittweite 1            │
│ │                                                     │
│ │  ┌─────────────────────────────────────────────┐    │
│ │  │           zahlen[i] > max                   │    │
│ │  ├─────────────────────────────────────────────┤    │
│ │  │ J                    │ N                    │    │
│ │  │                      │                      │    │
│ │  │ Zuweisung:           │ (nichts)             │    │
│ │  │ max = zahlen[i]      │                      │    │
│ │  │                      │                      │    │
│ │  └──────────────────────┴──────────────────────┘    │
│ │                                                     │
└───────────────────────────────────────────────────────┘
│ Ausgabe:                                              │
│ "Maximum: " + max                                     │
└───────────────────────────────────────────────────────┘
```

---

### Pattern 4: Lineare Suche

```
Deklaration und Initialisierung: namen = ["Anna", "Ben", "Clara"]
Einlesen: suchName als Text
Deklaration und Initialisierung: gefunden = falsch
Deklaration und Initialisierung: position = -1
Deklaration und Initialisierung: n = Anzahl der Elemente des Arrays namen
Zähle i von 0 bis n - 1, Schrittweite 1
    Wenn namen[i] == suchName, dann
        J
            Zuweisung: gefunden = wahr
            Zuweisung: position = i
        , sonst
        N
            (nichts)
Wenn gefunden == wahr, dann
    J
        Ausgabe: "Gefunden an Position: " + position
    , sonst
    N
        Ausgabe: "Nicht gefunden"
```

---

### Pattern 5: Bubble Sort (aufsteigend)

```
Deklaration und Initialisierung: zahlen = [5, 2, 8, 1, 9]
Deklaration und Initialisierung: n = Anzahl der Elemente des Arrays zahlen
Zähle i von 0 bis n - 2, Schrittweite 1
    Zähle j von 0 bis n - i - 2, Schrittweite 1
        Wenn zahlen[j] > zahlen[j + 1], dann
            J
                Deklaration und Initialisierung: temp = zahlen[j]
                Zuweisung: zahlen[j] = zahlen[j + 1]
                Zuweisung: zahlen[j + 1] = temp
            , sonst
            N
                (nichts)
Ausgabe: zahlen
```

**Grafisch:**
```
┌───────────────────────────────────────────────────────┐
│ Deklaration und Initialisierung:                      │
│ zahlen = [5, 2, 8, 1, 9]                              │
├───────────────────────────────────────────────────────┤
│ Deklaration und Initialisierung:                      │
│ n = Anzahl der Elemente des Arrays zahlen             │
├───────────────────────────────────────────────────────┤
│ ┌─ Zähle i von 0 bis n - 2, Schrittweite 1            │
│ │                                                     │
│ │  ┌─ Zähle j von 0 bis n - i - 2, Schrittweite 1     │
│ │  │                                                  │
│ │  │  ┌───────────────────────────────────────────┐   │
│ │  │  │      zahlen[j] > zahlen[j + 1]           │    │
│ │  │  ├───────────────────────────────────────────┤   │
│ │  │  │ J                 │ N                     │   │
│ │  │  │                   │                       │   │
│ │  │  │ Dekl. und Init.:  │ (nichts)              │   │
│ │  │  │ temp = zahlen[j]  │                       │   │
│ │  │  │                   │                       │   │
│ │  │  │ Zuweisung:        │                       │   │
│ │  │  │ zahlen[j] =       │                       │   │
│ │  │  │ zahlen[j + 1]     │                       │   │
│ │  │  │                   │                       │   │
│ │  │  │ Zuweisung:        │                       │   │
│ │  │  │ zahlen[j + 1] =   │                       │   │
│ │  │  │ temp              │                       │   │
│ │  │  │                   │                       │   │
│ │  │  └───────────────────┴───────────────────────┘   │
│ │  │                                                  │
│ │  └─────────────────────────────────────────────────┘ 
│ │                                                     │
└───────────────────────────────────────────────────────┘
│ Ausgabe:                                              │
│ zahlen                                                │
└───────────────────────────────────────────────────────┘
```

---

### Pattern 6: Zählen von Elementen mit Bedingung

```
Deklaration und Initialisierung: noten = [1, 2, 1, 3, 2, 1, 4]
Deklaration und Initialisierung: anzahlEinsen = 0
Deklaration und Initialisierung: n = Anzahl der Elemente des Arrays noten
Zähle i von 0 bis n - 1, Schrittweite 1
    Wenn noten[i] == 1, dann
        J
            Zuweisung: anzahlEinsen = anzahlEinsen + 1
        , sonst
        N
            (nichts)
Ausgabe: "Anzahl der Einsen: " + anzahlEinsen
```

---

### Pattern 7: Array filtern (neue Liste erstellen)

```
Deklaration und Initialisierung: zahlen = [10, 5, 20, 15, 30]
Deklaration und Initialisierung: groeßerAls10 = [ ]
Deklaration und Initialisierung: n = Anzahl der Elemente des Arrays zahlen
Deklaration und Initialisierung: indexNeu = 0
Zähle i von 0 bis n - 1, Schrittweite 1
    Wenn zahlen[i] > 10, dann
        J
            Zuweisung: groeßerAls10[indexNeu] = zahlen[i]
            Zuweisung: indexNeu = indexNeu + 1
        , sonst
        N
            (nichts)
Ausgabe: groeßerAls10
```

---

### Pattern 8: Eingabe validieren (mit Wiederholung)

```
Deklaration und Initialisierung: gueltig = falsch
Wiederhole solange gueltig == falsch
    Einlesen: alter als Ganzzahl
    Wenn alter >= 0 AND alter <= 120, dann
        J
            Zuweisung: gueltig = wahr
        , sonst
        N
            Ausgabe: "Ungültige Eingabe! Bitte erneut eingeben."
Ausgabe: "Eingegebenes Alter: " + alter
```

---

## Best Practices

### ✅ DO

- **Klare Bezeichner verwenden:** `summeAllerWerte` statt `s`
- **Datentypen angeben:** Erhöht die Lesbarkeit
- **Initialisierungen durchführen:** Variablen vor Verwendung initialisieren
- **Kommentare in komplexen Bereichen:** Bei verschachtelten Strukturen
- **Konsistente Notation:** Immer die gleichen Operatoren verwenden

### ❌ DON'T

- **Variablen ohne Deklaration verwenden**
- **Zu lange Bedingungen:** Besser auf mehrere Zeilen aufteilen
- **Überflüssige Verzweigungen:** `Wenn x == wahr, dann ...` statt `Wenn x, dann ...`
- **Unklare Schleifenabbrüche:** Immer klar definieren
- **Globale Variablen ohne Not:** Nur wenn wirklich benötigt

---

## Operatoren-Details

### Vergleichsoperatoren
- `==` gleich
- `!=` ungleich
- `<` kleiner als
- `<=` kleiner oder gleich
- `>` größer als
- `>=` größer oder gleich

### Logische Operatoren
- `AND` beide Bedingungen müssen wahr sein
- `OR` mindestens eine Bedingung muss wahr sein
- `NOT` Negation (kehrt Wahrheitswert um)

### Arithmetische Operatoren
- `+` Addition
- `-` Subtraktion
- `*` Multiplikation
- `/` Division
- `%` Modulo (Rest der Division)

---

## Häufige Fehler und Lösungen

### Fehler 1: Array-Index außerhalb des Bereichs

**Problem:**
```
Zähle i von 0 bis n, Schrittweite 1  // FALSCH: n ist außerhalb!
    Ausgabe: zahlen[i]
```

**Lösung:**
```
Zähle i von 0 bis n - 1, Schrittweite 1  // RICHTIG
    Ausgabe: zahlen[i]
```

### Fehler 2: Endlosschleife

**Problem:**
```
Deklaration und Initialisierung: i = 0
Wiederhole solange i < 10
    Ausgabe: i  // i wird nie erhöht!
```

**Lösung:**
```
Deklaration und Initialisierung: i = 0
Wiederhole solange i < 10
    Ausgabe: i
    Zuweisung: i = i + 1  // Zähler erhöhen!
```

### Fehler 3: Variable nicht initialisiert

**Problem:**
```
Deklaration: summe
Zuweisung: summe = summe + 10  // summe hat keinen Startwert!
```

**Lösung:**
```
Deklaration und Initialisierung: summe = 0
Zuweisung: summe = summe + 10
```

---

## Komplexes Beispiel: Notenverwaltung

**Aufgabe:** Erstelle ein Struktogramm für ein Programm, das:
1. Noten einliest (bis -1 eingegeben wird)
2. Den Durchschnitt berechnet
3. Die beste und schlechteste Note ermittelt
4. Die Anzahl der Noten über dem Durchschnitt ausgibt

**Lösung:**

```
Deklaration und Initialisierung: noten als Array = [ ]
Deklaration und Initialisierung: anzahl = 0
Deklaration und Initialisierung: eingabe = 0

Ausgabe: "Gib Noten ein (1-6), beende mit -1:"

Wiederhole solange eingabe != -1
    Einlesen: eingabe als Ganzzahl
    Wenn eingabe != -1 AND eingabe >= 1 AND eingabe <= 6, dann
        J
            Zuweisung: noten[anzahl] = eingabe
            Zuweisung: anzahl = anzahl + 1
        , sonst
        N
            Wenn eingabe != -1, dann
                J
                    Ausgabe: "Ungültige Note!"
                , sonst
                N
                    (nichts)

Wenn anzahl > 0, dann
    J
        Deklaration und Initialisierung: summe = 0
        Zähle i von 0 bis anzahl - 1, Schrittweite 1
            Zuweisung: summe = summe + noten[i]
        
        Deklaration und Initialisierung: durchschnitt = summe / anzahl
        Ausgabe: "Durchschnitt: " + durchschnitt
        
        Deklaration und Initialisierung: beste = noten[0]
        Deklaration und Initialisierung: schlechteste = noten[0]
        
        Zähle i von 1 bis anzahl - 1, Schrittweite 1
            Wenn noten[i] < beste, dann
                J
                    Zuweisung: beste = noten[i]
                , sonst
                N
                    (nichts)
            Wenn noten[i] > schlechteste, dann
                J
                    Zuweisung: schlechteste = noten[i]
                , sonst
                N
                    (nichts)
        
        Ausgabe: "Beste Note: " + beste
        Ausgabe: "Schlechteste Note: " + schlechteste
        
        Deklaration und Initialisierung: uberDurchschnitt = 0
        Zähle i von 0 bis anzahl - 1, Schrittweite 1
            Wenn noten[i] < durchschnitt, dann
                J
                    Zuweisung: uberDurchschnitt = uberDurchschnitt + 1
                , sonst
                N
                    (nichts)
        
        Ausgabe: "Noten über Durchschnitt: " + uberDurchschnitt
    , sonst
    N
        Ausgabe: "Keine Noten eingegeben!"
```

---

## Integration in e-Learning-Aufgaben

### Template für Aufgaben

Bei jeder neuen Aufgabe:

1. **Problemstellung klar formulieren**
   - Was soll das Programm tun?
   - Welche Ein- und Ausgaben gibt es?

2. **Struktogramm erstellen**
   - Schrittweise nach diesem Guide vorgehen
   - Patterns anwenden wo möglich

3. **Python-Code erstellen**
   - Struktogramm in Code übersetzen
   - Validierung mit `struktogramm_helper.py`

4. **Tests durchführen**
   - Schreibtischtest mit Beispieldaten
   - Code ausführen und prüfen

---

## Für KI-Assistenten

### Wichtige Hinweise

Wenn du als KI-Assistent eine Aufgabe bekommst, die Programmlogik darstellen soll:

1. **Immer Struktogramme nach BW-Standard verwenden**
2. **Verwende die exakten Operatoren aus der Operatorenliste**
3. **Nutze die Patterns aus diesem Guide**
4. **Erstelle zuerst textbasierte Version, dann grafische wenn gewünscht**
5. **Referenziere: `struktogramme/Operatorenliste-Struktogramme.md`**

### Workflow für KI

```
Aufgabe erhalten
    ↓
Problem analysieren
    ↓
Passende Patterns identifizieren
    ↓
Struktogramm textbasiert erstellen
    ↓
Bei Bedarf: grafische Darstellung
    ↓
Python-Code generieren (optional)
```

---

## Ressourcen

- **Vollständige Operatorenliste:** [`struktogramme/Operatorenliste-Struktogramme.md`](../../struktogramme/Operatorenliste-Struktogramme.md)
- **PDF-Version:** [`struktogramme/operatorenliste-fuer-struktogramme-v2-2.pdf`](../../struktogramme/operatorenliste-fuer-struktogramme-v2-2.pdf)
- **Beispiele:** Alle `.stgr`-Dateien im `struktogramme/`-Verzeichnis
- **Python-Helper:** [`src/utils/struktogramm_helper.py`](../../src/utils/struktogramm_helper.py)

---

## Fragen & Feedback

Bei Fragen oder Verbesserungsvorschlägen bitte ein Issue im Repository erstellen oder direkt an die Lehrkraft wenden.

---

*Basierend auf: Operatorenliste für Struktogramme Version 2.2 vom 01.09.2024, Abiturprüfung Baden-Württemberg*
