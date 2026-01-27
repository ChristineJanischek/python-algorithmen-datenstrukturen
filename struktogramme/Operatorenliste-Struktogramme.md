# Operatorenliste für Struktogramme

Version 2.2 vom 01.09.2024  
Abiturprüfung Baden-Württemberg

## Wichtige Hinweise

- **Kursive Ausdrücke** sind allgemeine Platzhalter (z. B. `variable`, `datentyp`, `wert`, `bedingung`)
- **Optionale Erweiterungen** stehen in senkrechten Strichen `| |` und können weggelassen werden
- **Kontrollstrukturen** (des gleichen oder unterschiedlichen Typs) können miteinander verschachtelt werden
- Die Notation im Struktogramm folgt einer standardisierten Form für die Abiturprüfung Baden-Württemberg

---

## 1. Variablen und Datenstrukturen

### 1.1 Deklaration

**Operator:** `Deklaration: variable |als datentyp|`

**Beschreibung:** Deklaration einer Variablen, optionale Angabe des Datentyps

**Zweck:** Eine Variable wird bekannt gemacht und reserviert Speicherplatz. Der Datentyp ist optional, kann aber zur besseren Lesbarkeit angegeben werden.

**Häufige Datentypen:**
- Ganzzahl (Integer)
- Dezimalzahl (Float/Double)
- Text/Zeichenkette (String)
- Wahrheitswert (Boolean)

**Beispiel:**
```
Deklaration: alter als Ganzzahl
```

**Grafische Darstellung im Struktogramm:**
```
┌─────────────────────────────────────┐
│ Deklaration: alter als Ganzzahl     │
└─────────────────────────────────────┘
```

---

### 1.2 Initialisierung

**Operator:** `Initialisierung: variable = wert`

**Beschreibung:** Initialisierung einer Variablen mit einem Ausgangswert (oder dem Ergebnis einer Berechnung o. ä.)

**Beispiel:**
```
Initialisierung: guthaben = 10
```

**Grafische Darstellung im Struktogramm:**
```
┌─────────────────────────────────────┐
│ Initialisierung: guthaben = 10      │
└─────────────────────────────────────┘
```

---

### 1.3 Deklaration und Initialisierung

**Operator:** `Deklaration und Initialisierung: variable |als datentyp| = wert`

**Beschreibung:** Kombination von Deklaration und Initialisierung

**Beispiel:**
```
Deklaration und Initialisierung: anzahl als Ganzzahl = 0
```

**Grafische Darstellung im Struktogramm:**
```
┌───────────────────────────────────────────────────────┐
│ Deklaration und Initialisierung:                      │
│ anzahl als Ganzzahl = 0                               │
└───────────────────────────────────────────────────────┘
```

---

### 1.4 Zuweisung

**Operator:** `Zuweisung: element = wert`

**Beschreibung:** Zuweisung eines Wertes (oder des Ergebnisses einer Berechnung o. ä.) zu einem Element, das eine Variable oder ein anderes Element (z. B. ein Ausgabefeld) sein kann

**Beispiel:**
```
Zuweisung: qm = laenge * breite
```

**Grafische Darstellung im Struktogramm:**
```
┌─────────────────────────────────────┐
│ Zuweisung: qm = laenge * breite     │
└─────────────────────────────────────┘
```

---

## 2. Ein- und Ausgabe

### 2.1 Einlesen

**Operator:** `Einlesen: variable |als datentyp|`

**Beschreibung:** Einlesen einer Eingabe, z. B. aus einem Eingabefeld, einer Kommandozeile, …; auch in Kombination mit Deklaration möglich

**Beispiel:**
```
Deklaration und Einlesen: betrag als Dezimalzahl
```

**Grafische Darstellung im Struktogramm:**
```
┌────────────────────────────────────────────────┐
│ Deklaration und Einlesen:                      │
│ betrag als Dezimalzahl                         │
└────────────────────────────────────────────────┘
```

---

### 2.2 Ausgabe

**Operator:** `Ausgabe: inhalt`

**Beschreibung:** Verwendung einer Ausgabeoption (z. B. Meldungsfenster, Konsole), die eine Variable, einen Array, einen Text oder eine Kombination aus diesen ausgibt

**Beispiel:**
```
Ausgabe: "Die Fläche beträgt " + qm + " Quadratmeter."
```

**Grafische Darstellung im Struktogramm:**
```
┌─────────────────────────────────────────────────────┐
│ Ausgabe: "Die Fläche beträgt " + qm +               │
│          " Quadratmeter."                           │
└─────────────────────────────────────────────────────┘
```

---

### 2.3 Zeilenweise Ausgabe

**Operator:** `Zeilenweise Ausgabe: inhalt`

**Beschreibung:** Ausgabe mit Zeilenumbruch

**Beispiel:**
```
Ausgabe: "Hallo!" + Zeilenumbruch
```

---

### 2.4 Rückgabe

**Operator:** `Rückgabe: wert`

**Beschreibung:** Anweisung zur Rückgabe eines Wertes innerhalb einer Funktion/Methode/Prozedur

**Beispiel:**
```
Rückgabe: strecke
```

**Grafische Darstellung im Struktogramm:**
```
┌─────────────────────────────────────┐
│ Rückgabe: strecke                   │
└─────────────────────────────────────┘
```

---

## 3. Funktionen und Methoden

### 3.1 Aufruf

**Operator:** `Aufruf: methode/unterprogramm(|parameter|)`

**Beschreibung:** Aufruf einer Funktion/Methode/Prozedur/Unterprogramm, auch in Kombination mit anderen Operatoren (wie Zuweisungen oder Bedingungen), wenn Rückgabewerte verwendet werden sollen

**Beispiele:**
```
Aufruf: sortiereListe()
```
```
Aufruf: einzahlen(betrag)
```

**Grafische Darstellung im Struktogramm:**
```
┌─────────────────────────────────────┐
│ Aufruf: sortiereListe()             │
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│ Aufruf: einzahlen(betrag)           │
└─────────────────────────────────────┘
```

---

## 4. Kontrollstrukturen

### 4.1 Bedingte Anweisung (Verzweigung)

**Operator:** `Wenn bedingung, dann […] |, sonst […] |`

**Beschreibung:** Verzweigungs- bzw. Mehrfachauswahlbedingung

**Zweck:** Ermöglicht die bedingte Ausführung von Code. Der „sonst"-Zweig ist optional.

**Vergleichsoperatoren:** 
- `==` (gleich)
- `!=` (ungleich)
- `<` (kleiner als)
- `<=` (kleiner oder gleich)
- `>` (größer als)
- `>=` (größer oder gleich)

**Logische Operatoren:** 
- `AND` (logisches UND - beide Bedingungen müssen wahr sein)
- `OR` (logisches ODER - mindestens eine Bedingung muss wahr sein)
- `NOT` (logische Negation - kehrt den Wahrheitswert um)

**Beispiel:**
```
Wenn alter > 18 AND geschlecht == "w", dann
    J (Ja-Zweig)
        …
    , sonst
    N (Nein-Zweig)
        …
```

**Grafische Darstellung im Struktogramm:**
```
┌───────────────────────────────────────────────────────┐
│           alter > 18 AND geschlecht == "w"            │
├───────────────────────────────────────────────────────┤
│ J                        │ N                          │
│                          │                            │
│ (Anweisungen für Ja)     │ (Anweisungen für Nein)     │
│                          │                            │
└──────────────────────────┴────────────────────────────┘
```

**Hinweis:** Die Zweige werden oft mit `J` (Ja) und `N` (Nein) gekennzeichnet

---

### 4.2 Wiederhole-solange-Schleife (while-Schleife)

**Operator:** `Wiederhole solange bedingung`

**Beschreibung:** Schleife mit vorausgehender Bedingungsprüfung („while-Schleife")

**Zweck:** Der Code im Schleifenkörper wird wiederholt ausgeführt, solange die Bedingung wahr ist. Die Bedingung wird **vor** jedem Durchlauf geprüft.

**Wichtig:** 
- Wenn die Bedingung von Anfang an falsch ist, wird der Schleifenkörper gar nicht ausgeführt
- Es muss im Schleifenkörper etwas geschehen, das die Bedingung irgendwann falsch macht, sonst entsteht eine Endlosschleife

**Beispiel:**
```
Wiederhole solange inhalt > 10
    …
```

**Grafische Darstellung im Struktogramm:**
```
┌─────────────────────────────────────────────────────┐
│ ┌─ Wiederhole solange inhalt > 10                   │
│ │                                                   │
│ │  (Anweisungen im Schleifenkörper)                 │
│ │                                                   │
└─┘───────────────────────────────────────────────────┘
```

---

### 4.3 Zählergesteuerte Schleife (for-Schleife)

**Beschreibung:** Zählergesteuerte Schleife („for-Schleife")

**Zweck:** Eine Schleife, die eine bestimmte Anzahl von Durchläufen ausführt. Sie verwendet eine Zählvariable, die bei jedem Durchlauf um die Schrittweite erhöht (oder verringert) wird.

**Wichtig:**
- Die Schrittweite kann positiv (Hochzählen) oder negativ (Runterzählen) sein
- Bei Schrittweite 1 kann sie oft weggelassen werden (implizit)

#### Alternative Darstellung 1

**Operator:** `Wiederhole von startwert solange bedingung, Schrittweite schrittweite`

**Hinweis:** Diese Form ähnelt einer while-Schleife mit expliziter Initialisierung und Schrittweite

**Beispiel:**
```
Wiederhole von i = 0 solange i < 5, Schrittweite 1
    …
```

**Grafische Darstellung im Struktogramm:**
```
┌─────────────────────────────────────────────────────┐
│ ┌─ Wiederhole von i = 0 solange i < 5,              │
│ │  Schrittweite 1                                   │
│ │                                                   │
│ │  (Anweisungen im Schleifenkörper)                 │
│ │                                                   │
└─┘───────────────────────────────────────────────────┘
```

#### Alternative Darstellung 2

**Operator:** `Zähle zählvariable von startwert bis endwert, Schrittweite schrittweite`

**Hinweis:** Diese Form ist kompakter und verwendet `bis` statt `solange`. Der Endwert ist inklusiv.

**Beispiel:**
```
Zähle i von 0 bis 4, Schrittweite 1
    …
```

**Grafische Darstellung im Struktogramm:**
```
┌─────────────────────────────────────────────────────┐
│ ┌─ Zähle i von 0 bis 4, Schrittweite 1              │
│ │                                                   │
│ │  (Anweisungen im Schleifenkörper)                 │
│ │                                                   │
└─┘───────────────────────────────────────────────────┘
```

**Unterschied zwischen beiden Darstellungen:**
- Darstellung 1: `i < 5` (Bedingung wird geprüft, 5 ist exklusiv)
- Darstellung 2: `bis 4` (4 ist inklusiv, ergibt die gleichen Werte 0, 1, 2, 3, 4)

---

## 5. Arrays

**Allgemeine Erklärung zu Arrays:**
- Ein Array ist eine geordnete Sammlung von Elementen des gleichen oder verschiedener Datentypen
- Die Elemente werden über einen Index (Feldindex) angesprochen
- Die Indizierung beginnt in der Regel bei 0 (erstes Element hat Index 0)
- Arrays haben eine feste oder dynamische Länge

### 5.1 Array-Deklaration und Initialisierung

**Operator:** `Deklaration und Initialisierung: array |als Array| = [Arrayelement1, Arrayelement2, …]`

**Beschreibung:** Kombination aus Deklaration und Initialisierung eines Arrays

**Beispiel mit Werten:**
```
Deklaration und Initialisierung: personen = ["Sven", "Tina", "Anja"]
```

**Grafische Darstellung im Struktogramm:**
```
┌─────────────────────────────────────────────────────┐
│ Deklaration und Initialisierung:                    │
│ personen = ["Sven", "Tina", "Anja"]                 │
└─────────────────────────────────────────────────────┘
```

**Beispiel leerer Array:**
```
Deklaration und Initialisierung: zahlen als Array = [ ]
```

**Grafische Darstellung im Struktogramm:**
```
┌─────────────────────────────────────────────────────┐
│ Deklaration und Initialisierung:                    │
│ zahlen als Array = [ ]                              │
└─────────────────────────────────────────────────────┘
```

---

### 5.2 Array-Element-Zuweisung

**Operator:** `Zuweisung: array[feldindex] = wert`

**Beschreibung:** Zuweisung eines Wertes (oder des Ergebnisses einer Berechnung o. ä.) zu einem Arrayelement, dessen Index in den eckigen Klammern angegeben wird

**Wichtig:** Der Index muss bereits existieren (das Array muss an dieser Position schon ein Element haben)

**Beispiele:**
```
Zuweisung: personen[2] = "Kay"
```
*Ersetzt das Element am Index 2 (drittes Element) durch "Kay"*

```
Zuweisung: zahlen[0] = 5
```
*Setzt das erste Element des Arrays auf 5*

---

### 5.3 Anhängen an ein Array

**Operator:** `Zuweisung: array[feldindex] = wert`

**Beschreibung:** Anhängen eines Arrayelements an einen Array, indem ein Wert einem Index zugeordnet wird, der noch nicht existiert

**Wichtig:** Dies erweitert das Array um ein neues Element am Ende

**Beispiel:**
```
Zuweisung: personen[3] = "Milo"
```
*Wenn das Array `personen` vorher die Indizes 0, 1, 2 hatte, fügt dies "Milo" am Index 3 hinzu*

**Unterschied zu 5.2:** 
- Bei 5.2 wird ein **bestehendes** Element überschrieben
- Bei 5.3 wird ein **neues** Element am Ende hinzugefügt

---

### 5.4 Anzahl der Elemente eines Arrays

**Operator:** `Anzahl der Elemente eines Arrays array`

**Beschreibung:** Zuweisung der Anzahl der Arrayelemente zu einer Variablen. Auch in Kombination (bspw. mit Schleifen und Ausgaben) möglich

**Zweck:** Ermittelt die Länge eines Arrays, was besonders nützlich für Schleifen ist

**Beispiel:**
```
Deklaration und Initialisierung: laenge = Anzahl der Elemente des Arrays personen
```

**Typische Verwendung in Schleifen:**
```
Deklaration und Initialisierung: n = Anzahl der Elemente des Arrays zahlen
Zähle i von 0 bis n - 1, Schrittweite 1
    Ausgabe: zahlen[i]
```
*Gibt alle Elemente des Arrays aus*

---

### 5.5 Array-Element-Ausgabe

**Operator:** `Ausgabe: array[feldindex]`

**Beschreibung:** Ausgabe einzelner Arrayelemente. Der gewünschte Index kann direkt, durch eine Berechnung oder durch eine Variable angegeben werden

**Beispiele:**
```
Ausgabe: zahlen[1]
```
```
Deklaration und Initialisierung: i = 0
Ausgabe: personen[i]
```
```
Ausgabe: personen[i + 2]
```

**Grafische Darstellung im Struktogramm:**
```
┌─────────────────────────────────────┐
│ Ausgabe: zahlen[1]                  │
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│ Deklaration und Initialisierung:    │
│ i = 0                               │
├─────────────────────────────────────┤
│ Ausgabe: personen[i]                │
└─────────────────────────────────────┘
```

---

### 5.6 Gesamten Array ausgeben

**Operator:** `Ausgabe: zahlen`

**Beschreibung:** Ausgabe eines Arrays. Der ganze Array kann über den Namen ausgegeben werden.

**Beispiel:**
```
Ausgabe: zahlen
```

**Grafische Darstellung im Struktogramm:**
```
┌─────────────────────────────────────┐
│ Ausgabe: zahlen                     │
└─────────────────────────────────────┘
```

---

## Zusammenfassung der wichtigsten Konzepte

### Variablenoperationen
- **Deklaration**: Variable bekannt machen (mit oder ohne Datentyp)
- **Initialisierung**: Variable einen Startwert zuweisen
- **Zuweisung**: Einer bereits deklarierten Variable einen (neuen) Wert zuweisen
- **Einlesen**: Benutzereingabe in eine Variable einlesen

### Kontrollfluss
- **Verzweigung**: Bedingte Ausführung von Code basierend auf einer Bedingung
  - Kann mit `sonst`-Zweig oder ohne verwendet werden
  - Mehrere Bedingungen können mit `AND`, `OR`, `NOT` verknüpft werden
- **Schleifen**: Wiederholte Ausführung von Code
  - **While-Schleife**: Bedingung wird vor jedem Durchlauf geprüft
  - **For-Schleife**: Zählergesteuerte Schleife mit fester Anzahl von Durchläufen
    - Zwei alternative Darstellungsformen möglich

### Datenstrukturen
- **Arrays**: Geordnete Sammlung von Elementen
  - Zugriff über Index (beginnt bei 0)
  - Können leer initialisiert oder mit Werten gefüllt werden
  - Elemente können überschrieben oder angehängt werden
  - Die Länge kann mit `Anzahl der Elemente` ermittelt werden

### Funktionen
- **Aufruf**: Ausführung einer Funktion/Methode/Prozedur
  - Mit oder ohne Parameter möglich
  - Rückgabewerte können in Zuweisungen verwendet werden
- **Rückgabe**: Gibt einen Wert aus einer Funktion zurück

### Operatoren
- **Vergleichsoperatoren**: `==`, `!=`, `<`, `<=`, `>`, `>=`
- **Logische Operatoren**: `AND`, `OR`, `NOT`
- **Arithmetische Operatoren**: `+`, `-`, `*`, `/` (implizit in Berechnungen)

### Notation
- **Platzhalter** in kursiv: `variable`, `wert`, `bedingung`, etc.
- **Optionale Teile** in `| |`: können weggelassen werden
- **`…`**: Platzhalter für weiteren Code im Struktogramm

---

## Praktische Hinweise für die Verwendung

### Typische Strukturen in Struktogrammen

**Beispiel 1: Eingabe verarbeiten und ausgeben**
```
Einlesen: wert als Ganzzahl
Zuweisung: ergebnis = wert * 2
Ausgabe: "Das Ergebnis ist: " + ergebnis
```

**Grafische Darstellung:**
```
┌─────────────────────────────────────────────────────────┐
│ Einlesen: wert als Ganzzahl                             │
├─────────────────────────────────────────────────────────┤
│ Zuweisung: ergebnis = wert * 2                          │
├─────────────────────────────────────────────────────────┤
│ Ausgabe: "Das Ergebnis ist: " + ergebnis                │
└─────────────────────────────────────────────────────────┘
```

---

**Beispiel 2: Array durchlaufen**
```
Deklaration und Initialisierung: zahlen = [1, 2, 3, 4, 5]
Deklaration und Initialisierung: n = Anzahl der Elemente des Arrays zahlen
Zähle i von 0 bis n - 1, Schrittweite 1
    Ausgabe: zahlen[i]
```

**Grafische Darstellung:**
```
┌─────────────────────────────────────────────────────────┐
│ Deklaration und Initialisierung:                        │
│ zahlen = [1, 2, 3, 4, 5]                                │
├─────────────────────────────────────────────────────────┤
│ Deklaration und Initialisierung:                        │
│ n = Anzahl der Elemente des Arrays zahlen               │
├─────────────────────────────────────────────────────────┤
│ ┌─ Zähle i von 0 bis n - 1, Schrittweite 1              │
│ │                                                       │
│ │    Ausgabe: zahlen[i]                                 │
│ │                                                       │
└─┘───────────────────────────────────────────────────────┘
```

---

**Beispiel 3: Bedingte Verarbeitung**
```
Einlesen: alter als Ganzzahl
Wenn alter >= 18, dann
    J
        Ausgabe: "Volljährig"
    , sonst
    N
        Ausgabe: "Minderjährig"
```

**Grafische Darstellung:**
```
┌───────────────────────────────────────────────────────────┐
│ Einlesen: alter als Ganzzahl                              │
├───────────────────────────────────────────────────────────┤
│                    alter >= 18                            │
├───────────────────────────────────────────────────────────┤
│ J                              │ N                        │
│                                │                          │
│ Ausgabe: "Volljährig"          │ Ausgabe: "Minderjährig"  │
│                                │                          │
└────────────────────────────────┴──────────────────────────┘
```

---

**Beispiel 4: Schleife mit Bedingung (Summe berechnen)**
```
Deklaration und Initialisierung: summe = 0
Deklaration und Initialisierung: zaehler = 1
Wiederhole solange zaehler <= 10
    Zuweisung: summe = summe + zaehler
    Zuweisung: zaehler = zaehler + 1
Ausgabe: "Summe: " + summe
```

**Grafische Darstellung:**
```
┌─────────────────────────────────────────────────────────┐
│ Deklaration und Initialisierung: summe = 0              │
├─────────────────────────────────────────────────────────┤
│ Deklaration und Initialisierung: zaehler = 1            │
├─────────────────────────────────────────────────────────┤
│ ┌─ Wiederhole solange zaehler <= 10, Schrittweite 1     │
│ │                                                       │
│ │    Zuweisung: summe = summe + zaehler                 │
│ │                                                       │
│ │    Zuweisung: zaehler = zaehler + 1                   │
│ │                                                       │
└─┘───────────────────────────────────────────────────────┘
│ Ausgabe: "Summe: " + summe                              │
└─────────────────────────────────────────────────────────┘
```

---

**Beispiel 5: Verschachtelte Strukturen (Array-Suche)**
```
Deklaration und Initialisierung: namen = ["Anna", "Ben", "Clara"]
Einlesen: suchName als Text
Deklaration und Initialisierung: gefunden = falsch
Deklaration und Initialisierung: n = Anzahl der Elemente des Arrays namen
Zähle i von 0 bis n - 1, Schrittweite 1
    Wenn namen[i] == suchName, dann
        J
            Zuweisung: gefunden = wahr
        , sonst
        N
            (nichts)
Wenn gefunden == wahr, dann
    J
        Ausgabe: "Name gefunden!"
    , sonst
    N
        Ausgabe: "Name nicht gefunden!"
```

**Grafische Darstellung:**
```
┌───────────────────────────────────────────────────────────┐
│ Deklaration und Initialisierung:                          │
│ namen = ["Anna", "Ben", "Clara"]                          │
├───────────────────────────────────────────────────────────┤
│ Einlesen: suchName als Text                               │
├───────────────────────────────────────────────────────────┤
│ Deklaration und Initialisierung: gefunden = falsch        │
├───────────────────────────────────────────────────────────┤
│ Deklaration und Initialisierung:                          │
│ n = Anzahl der Elemente des Arrays namen                  │
├───────────────────────────────────────────────────────────┤
│ ┌─ Zähle i von 0 bis n - 1, Schrittweite 1                │
│ │                                                         │
│ │  ┌───────────────────────────────────────────────────┐  │
│ │  │           namen[i] == suchName                    │  │
│ │  ├───────────────────────────────────────────────────┤  │
│ │  │ J                      │ N                        │  │
│ │  │                        │                          │  │
│ │  │ Zuweisung:             │ (nichts)                 │  │
│ │  │ gefunden = wahr        │                          │  │
│ │  │                        │                          │  │
│ │  └────────────────────────┴──────────────────────────┘  │
│ │                                                         │
└─┘─────────────────────────────────────────────────────────┘
│                  gefunden == wahr                         │
├───────────────────────────────────────────────────────────┤
│ J                              │ N                        │
│                                │                          │
│ Ausgabe:                       │ Ausgabe:                 │
│ "Name gefunden!"               │ "Name nicht gefunden!"   │
│                                │                          │
└────────────────────────────────┴──────────────────────────┘
```

---

*Quelle: Abiturprüfung Baden-Württemberg, Version 2.2 vom 01.09.2024*
