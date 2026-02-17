# Musterlösung & Erwartungshorizont
## Klassenarbeit: Kontrollstrukturen, Arrays und Algorithmen

**Dokumentation für Lehrkräfte**

Grundlage: Inhalte aus [src/niveau/infodateien/L2_1 Information_Algorithmik.docx](src/niveau/infodateien/L2_1%20Information_Algorithmik.docx), [src/niveau/infodateien/L2_2.1 Information_Bubble_Sort.docx](src/niveau/infodateien/L2_2.1%20Information_Bubble_Sort.docx), [src/niveau/infodateien/L2_2.2 Information_Selection_Sort.docx](src/niveau/infodateien/L2_2.2%20Information_Selection_Sort.docx), [src/niveau/infodateien/L2_3.1 Information_Lineare_Suche.docx](src/niveau/infodateien/L2_3.1%20Information_Lineare_Suche.docx), [src/niveau/infodateien/L2_3.2 Information_Binäre_Suche.docx](src/niveau/infodateien/L2_3.2%20Information_Bin%C3%A4re_Suche.docx).

---

## 📌 Übersicht Erwartungshorizont

| Aufgabe | Punkte | Lösungstyp | Bewertung |
|---------|--------|-----------|----------|
| 1 | 3 | Struktogramm + Code | Syntaxfehler -1 Punkt |
| 2 | 3 | Struktogramm + Code | Logikfehler -1 bis -2 Punkte |
| 3 | 3 | Code + Interpretation | Jeder fehlerhafte Teil -1 Punkt |
| 4 | 6 | Struktogramm + Code (3 Varianten) | Pro Teilaufgabe -1 bis -2 Punkte |
| 5 | 8 | Struktogramm + Code + Schreibtischtest | Kritisch: Schreibtischtest korrekt |
| 6 | 7 | Struktogramm + Code + Ausgabe | Swap-Logik ist kritisch |
| **Summe** | **30** | — | — |

---

## ✅ MUSTERLÖSUNGEN MIT BEWERTUNG

### **Aufgabe 1: Verzweigung & Logik (3 Punkte)**

**Erwartetes Struktogramm (BW-Standard - Grafische Notation):**

```
┌────────────────────────────────────────────────────────┐
│ Deklaration und Einlesen: alter als Ganzzahl           │
├────────────────────────────────────────────────────────┤
│                    alter < 18                          │
├────────────────────────────────────────────────────────┤
│ J                              │ N                     │
│                                │                       │
│ Ausgabe: "Jugendlicher"        │ Ausgabe: "Erwachsener"│
│                                │                       │
└────────────────────────────────┴───────────────────────┘
```

**Python-Code (Musterlösung):**
```python
alter = int(input("Geben Sie Ihr Alter ein: "))
if alter < 18:
    print("Jugendlicher")
else:
    print("Erwachsener")
```python

**Bewertung (3 Punkte):**
- ✅ **Struktogramm korrekt formatiert** (1 Punkt)
  - Eingabe oben
  - Raute mit Bedingung
  - Beide Ausgaben sichtbar
- ✅ **Python-Code syntaktisch korrekt** (1 Punkt)
  - `int(input(...))` korrekt
  - Bedingung richtig
- ✅ **Logik funktioniert** (1 Punkt)

**Häufige Fehler & Punkteabzug:**

| Fehler | Abzug |
|--------|-------|
| Struktogramm mit Pfeilen statt Symbolen | -0,5 Punkte |
| `if alter <= 18` statt `< 18` | -0,5 Punkte |
| Fehlende Ausgabe/print() | -1 Punkt |
| Syntaxfehler (z. B. `:` vergessen) | -1 Punkt |

---

### **Aufgabe 2: Schleife mit Bedingung (3 Punkte)**

**Erwartetes Struktogramm (BW-Standard - Grafische Notation):**

```
┌───────────────────────────────────────────────────────────────┐
│ Deklaration und Initialisierung: summe = 0                    │
├───────────────────────────────────────────────────────────────┤
│ Deklaration und Einlesen: zahl als Ganzzahl                   │
├───────────────────────────────────────────────────────────────┤
│ ┌─ Wiederhole solange zahl != -1                              │
│ │                                                             │
│ │    Zuweisung: summe = summe + zahl                          │
│ │                                                             │
│ │    Ausgabe: "Summe: " + summe                               │
│ │                                                             │
│ │    Einlesen: zahl als Ganzzahl                              │
│ │                                                             │
└─┘─────────────────────────────────────────────────────────────┘
├───────────────────────────────────────────────────────────────┤
│ Ausgabe: "Programm beendet."                                  │
└───────────────────────────────────────────────────────────────┘
```

**Python-Code (Musterlösung):**
```python
summe = 0
zahl = int(input("Geben Sie eine Zahl ein (oder -1 zum Beenden): "))

while zahl != -1:
    summe = summe + zahl
    print(f"Summe: {summe}")
    zahl = int(input("Geben Sie eine Zahl ein (oder -1 zum Beenden): "))

print("Programm beendet.")
```python

**Bewertung (3 Punkte):**
- ✅ **Struktogramm korrekt** (2 Punkte)
  - Initalisierung erkennbar (summe = 0)
  - while-Schleife mit Bedingung
  - Schleifenkörper mit Summe-Update und Ausgabe
  - Schleife wiederholt Eingabe
- ✅ **Python-Code funktionsfähig** (1 Punkt)
  - `while` mit korrekter Bedingung
  - Summe wird aktualisiert

**Häufige Fehler & Punkteabzug:**

| Fehler / Variante | Abzug |
|-----------|-------|
| for-Schleife statt while (nicht flexibel) | -1 Punkt |
| Bedingung falsch (`zahl == -1`) | -1 Punkt |
| Summe wird nicht initialisiert | -0,5 Punkte |
| Print nicht in Schleife | -0,5 Punkte |
| Eingabe wird nur einmal gelesen | -1 Punkt |

**Alternative Akzeptabel:**
## 📐 Struktogramm (grafische Notation)

<!-- START_GRAPHIC_STRUKTOGRAMM -->
```
┌────────────────────────────────────────┐
│ Wiederhole solange wahr                │
│   Wenn zahl == -1, dann                │
│     J                                  │
│       Abbruch                           │
│     , sonst                            │
│     N                                  │
│       summe = summe + zahl             │
│       Ausgabe: Summe                   │
└────────────────────────────────────────┘
```
<!-- END_GRAPHIC_STRUKTOGRAMM -->

```python
while True:
    zahl = int(input("Zahl: "))
    if zahl == -1:
        break
    summe += zahl
    print(f"Summe: {summe}")
```
→ Volle Punkte (alternative Kontrollflussvariante)

---

### **Aufgabe 3: Array-Grundlagen (3 Punkte)**

**a) Deklaration (1 Punkt)**

**Musterlösung:**

## 📐 Struktogramm (grafische Notation)

<!-- START_GRAPHIC_STRUKTOGRAMM -->
```
┌────────────────────────────────────────┐
│ [STRUKTOGRAMM HIER HINZUFÜGEN]         │
│                                        │
│ Beispiel-Elemente:                     │
│ • Deklaration                          │
│ • Zuweisung                            │
│ • Schleife (┌─ ... ─┘)                 │
│ • Verzweigung (J/N Zweige)             │
└────────────────────────────────────────┘
```
<!-- END_GRAPHIC_STRUKTOGRAMM -->


```python
noten = [1, 2, 2, 3, 1, 5, 4, 2]
```

**Bewertung:**
- ✅ Exakte oder äquivalente Syntax = 1 Punkt
- ❌ Fehler (z. B. `noten [1, 2, ...]` oder `noten = {1,2,...}`) = 0 Punkte

---

**b) Array-Zugriff (1 Punkt)**

**Musterlösung:**

## 📐 Struktogramm (grafische Notation)

<!-- START_GRAPHIC_STRUKTOGRAMM -->
```
┌────────────────────────────────────────┐
│ [STRUKTOGRAMM HIER HINZUFÜGEN]         │
│                                        │
│ Beispiel-Elemente:                     │
│ • Deklaration                          │
│ • Zuweisung                            │
│ • Schleife (┌─ ... ─┘)                 │
│ • Verzweigung (J/N Zweige)             │
└────────────────────────────────────────┘
```
<!-- END_GRAPHIC_STRUKTOGRAMM -->


```python
erstes = noten[0]          # 1. Element = 1
noten[-1] = 1              # Letztes Element auf 1 setzen
laenge = len(noten)        # Länge = 8
print(erstes, laenge)
```

**Bewertung (1 Punkt, alles oder nichts):**
- ✅ `noten[0]` (oder `noten[1]` als "1. Position") = 0,3 Punkte
- ✅ `noten[-1] = 1` (oder `noten[7] = 1`) = 0,3 Punkte
- ✅ `len(noten)` = 0,3 Punkte
- ❌ Syntaxfehler in einem Punkt = -0,5

---

**c) Interpretation (1 Punkt)**

**Musterlösung:**
```
noten[3] = 3 (das Element an Index 3 = 4. Position = Note 3)
```

**Alternativ akzeptabel:**
```
Das 4. Element des Arrays, dessen Wert 3 ist.
```

**Bewertung:**
- ✅ Korrekte Interpretation (Index 3 = 4. Position) = 1 Punkt
- ⚠️ Nur Wertangabe ohne Index-Erklärung = 0,5 Punkte
- ❌ Falsche Interpretation = 0 Punkte

---

### **Aufgabe 4: Array durchlaufen & filtern (6 Punkte)**

**Gegeben:** `werte = [12, 45, 23, 67, 8, 34, 56, 11]`

---

**a) Alle Werte ausgeben (2 Punkte)**

**Struktogramm (1 Punkt):**
```struktogramm
Zähle i von 0 bis Anzahl der Elemente des Arrays werte - 1, Schrittweite 1
    Ausgabe: werte[i]
```

**Python-Code (1 Punkt):**

**Musterlösung 1 (for-Schleife mit Index):**
## 📐 Struktogramm (grafische Notation)

<!-- START_GRAPHIC_STRUKTOGRAMM -->
```
┌────────────────────────────────────────┐
│ Zähle i von 0 bis Anzahl der Elemente  │
│ des Arrays werte - 1, Schrittweite 1   │
│   Ausgabe: werte[i]                    │
└────────────────────────────────────────┘
```
<!-- END_GRAPHIC_STRUKTOGRAMM -->

```python
for i in range(len(werte)):
    print(werte[i])
```

**Musterlösung 2 (for-Schleife mit Element):**
## 📐 Struktogramm (grafische Notation)

<!-- START_GRAPHIC_STRUKTOGRAMM -->
```
┌────────────────────────────────────────┐
│ Zähle element in werte                 │
│   Ausgabe: element                     │
└────────────────────────────────────────┘
```
<!-- END_GRAPHIC_STRUKTOGRAMM -->

```python
for wert in werte:
    print(wert)
```

**Musterlösung 3 (while-Schleife):**

## 📐 Struktogramm (grafische Notation)

<!-- START_GRAPHIC_STRUKTOGRAMM -->
```
┌────────────────────────────────────────┐
│ [STRUKTOGRAMM HIER HINZUFÜGEN]         │
│                                        │
│ Beispiel-Elemente:                     │
│ • Deklaration                          │
│ • Zuweisung                            │
│ • Schleife (┌─ ... ─┘)                 │
│ • Verzweigung (J/N Zweige)             │
└────────────────────────────────────────┘
```
<!-- END_GRAPHIC_STRUKTOGRAMM -->


```python
i = 0
while i < len(werte):
    print(werte[i])
    i += 1
```

**Bewertung:**
- ✅ Jede Variante (1-3) = volle 2 Punkte
- ⚠️ `print(werte)` (gibt ganzes Array aus) = 1 Punkt
- ❌ Keine Schleife, nur Einzelausgaben = 0 Punkte

---

**b) Elemente filtern (2 Punkte)**

**Musterlösung:**

## 📐 Struktogramm (grafische Notation)

<!-- START_GRAPHIC_STRUKTOGRAMM -->
```
┌────────────────────────────────────────┐
│ [STRUKTOGRAMM HIER HINZUFÜGEN]         │
│                                        │
│ Beispiel-Elemente:                     │
│ • Deklaration                          │
│ • Zuweisung                            │
│ • Schleife (┌─ ... ─┘)                 │
│ • Verzweigung (J/N Zweige)             │
└────────────────────────────────────────┘
```
<!-- END_GRAPHIC_STRUKTOGRAMM -->


```python
for wert in werte:
    if wert > 30:
        print(wert)
```

**Alternative:**

## 📐 Struktogramm (grafische Notation)

<!-- START_GRAPHIC_STRUKTOGRAMM -->
```
┌────────────────────────────────────────┐
│ [STRUKTOGRAMM HIER HINZUFÜGEN]         │
│                                        │
│ Beispiel-Elemente:                     │
│ • Deklaration                          │
│ • Zuweisung                            │
│ • Schleife (┌─ ... ─┘)                 │
│ • Verzweigung (J/N Zweige)             │
└────────────────────────────────────────┘
```
<!-- END_GRAPHIC_STRUKTOGRAMM -->


```python
for i in range(len(werte)):
    if werte[i] > 30:
        print(werte[i])
```python

**Bewertung (2 Punkte):**
- ✅ Schleife + if-Bedingung korrekt = 2 Punkte
- ⚠️ Nur Bedingung ohne Schleife = 1 Punkt
- ⚠️ Schleife aber Bedingung falsch (`if wert < 30`) = 1 Punkt
- ❌ Keine Lösung = 0 Punkte

**Erwartete Ausgabe:**
```
45
67
34
56
```

---

**c) Array manipulieren (2 Punkte)**

**Musterlösung 1 (neue Liste mit Schleife):**

## 📐 Struktogramm (grafische Notation)

<!-- START_GRAPHIC_STRUKTOGRAMM -->
```
┌────────────────────────────────────────┐
│ [STRUKTOGRAMM HIER HINZUFÜGEN]         │
│                                        │
│ Beispiel-Elemente:                     │
│ • Deklaration                          │
│ • Zuweisung                            │
│ • Schleife (┌─ ... ─┘)                 │
│ • Verzweigung (J/N Zweige)             │
└────────────────────────────────────────┘
```
<!-- END_GRAPHIC_STRUKTOGRAMM -->


```python
verdoppelt = []
for wert in werte:
    verdoppelt.append(wert * 2)
print(verdoppelt)  # [24, 90, 46, 134, 16, 68, 112, 22]
```

**Musterlösung 2 (modifizieren im Original):**

## 📐 Struktogramm (grafische Notation)

<!-- START_GRAPHIC_STRUKTOGRAMM -->
```
┌────────────────────────────────────────┐
│ [STRUKTOGRAMM HIER HINZUFÜGEN]         │
│                                        │
│ Beispiel-Elemente:                     │
│ • Deklaration                          │
│ • Zuweisung                            │
│ • Schleife (┌─ ... ─┘)                 │
│ • Verzweigung (J/N Zweige)             │
└────────────────────────────────────────┘
```
<!-- END_GRAPHIC_STRUKTOGRAMM -->


```python
for i in range(len(werte)):
    werte[i] = werte[i] * 2
```

**Bewertung (2 Punkte):**
- ✅ Schleife mit append() oder Index-Zugriff = 2 Punkte
- ⚠️ Nur Berechnung ohne Speicherung = 1 Punkt
- ❌ Falsch strukturiert = 0 Punkte

---

### **Aufgabe 5: Lineare Suche (8 Punkte)**

**Gegeben:** `buchstaben = ['A', 'B', 'C', 'D', 'E', 'F', 'G']`

---

**a) Struktogramm (3 Punkte)**

**Erwartete Struktur:**

```struktogramm
Deklaration und Einlesen: such als Zeichenkette
Deklaration und Initialisierung: gefunden als Wahrheitswert = falsch
Deklaration und Initialisierung: i als Ganzzahl = 0
Wiederhole solange i < Anzahl der Elemente des Arrays buchstaben AND NOT gefunden
    Wenn buchstaben[i] == such, dann
        J
            Zuweisung: gefunden = wahr
        , sonst
        N
            Zuweisung: i = i + 1
Wenn gefunden, dann
    J
        Ausgabe: "Gefunden! Index: " + i
    , sonst
    N
        Ausgabe: "Nicht gefunden"

## 📐 Struktogramm (grafische Notation)

<!-- START_GRAPHIC_STRUKTOGRAMM -->
```
┌────────────────────────────────────────┐
│ [STRUKTOGRAMM HIER HINZUFÜGEN]         │
│                                        │
│ Beispiel-Elemente:                     │
│ • Deklaration                          │
│ • Zuweisung                            │
│ • Schleife (┌─ ... ─┘)                 │
│ • Verzweigung (J/N Zweige)             │
└────────────────────────────────────────┘
```
<!-- END_GRAPHIC_STRUKTOGRAMM -->


```python

**Bewertung Struktogramm (3 Punkte):**
- ✅ Eingabe & Variableninitialisierung (0,5 Punkte)
- ✅ Wiederholung (for oder while mit Bedingung) (1 Punkt)
- ✅ Vergleich im Schleifenkörper (0,75 Punkte)
- ✅ Verzweigung (gefunden/nicht gefunden) (0,75 Punkte)

**Häufige Fehler:**
| Fehler | Abzug |
|--------|-------|
| Ohne Initialisierung `gefunden = False` | -0,5 |
| Schleifenbedingung unvollständig | -0,5 |
| Abbruchbedingung fehlend | -1 Punkt |
| Ausgabe nicht klar positioniert | -0,5 |

---

**b) Python-Code (4 Punkte)**

**Musterlösung 1 (while-Schleife mit Flag):**
```python
such = input("Buchstabe suchen: ").upper()
buchstaben = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
gefunden = False
i = 0

while i < len(buchstaben) and not gefunden:
    if buchstaben[i] == such:
        print(f"Gefunden! Index: {i}")
        gefunden = True
    else:
        i += 1

if not gefunden:
    print("Nicht gefunden")
```

**Musterlösung 2 (for-Schleife mit break):**

## 📐 Struktogramm (grafische Notation)

<!-- START_GRAPHIC_STRUKTOGRAMM -->
```
┌────────────────────────────────────────┐
│ [STRUKTOGRAMM HIER HINZUFÜGEN]         │
│                                        │
│ Beispiel-Elemente:                     │
│ • Deklaration                          │
│ • Zuweisung                            │
│ • Schleife (┌─ ... ─┘)                 │
│ • Verzweigung (J/N Zweige)             │
└────────────────────────────────────────┘
```
<!-- END_GRAPHIC_STRUKTOGRAMM -->


```python
such = input("Buchstabe suchen: ").upper()
buchstaben = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
gefunden = False

for i in range(len(buchstaben)):
    if buchstaben[i] == such:
        print(f"Gefunden! Index: {i}")
        gefunden = True
        break

if not gefunden:
    print("Nicht gefunden")
```

**Bewertung (4 Punkte):**
- ✅ Schleife mit Vergleich = 2 Punkte
- ✅ Korrekte Ausgabe = 1 Punkt
- ✅ Abbruch bei Fund = 1 Punkt
- ❌ Syntax-Fehler = -0,5 Punkte pro Fehler

---

**c) Schreibtischtest (1 Punkt)**

**Eingabe:** "D"

**Musterlösung (Beispiel mit Musterlösung 1):**

```
Schritt 1: i=0, gefunden=False
           buchstaben[0]='A', 'A' ≠ 'D' → i=1

Schritt 2: i=1, gefunden=False
           buchstaben[1]='B', 'B' ≠ 'D' → i=2

Schritt 3: i=2, gefunden=False
           buchstaben[2]='C', 'C' ≠ 'D' → i=3

Schritt 4: i=3, gefunden=False
           buchstaben[3]='D', 'D' ≠ 'D'? NEIN! → gefunden=True
           AUSGABE: "Gefunden! Index: 3"
           
Schritt 5: Schleife beendet (gefunden=True)
           Keine weitere Ausgabe
```

**Bewertung (1 Punkt):**
- ✅ Mindestens 3 Schritte nachvollziehbar = 1 Punkt
- ⚠️ Nur Anfang oder Ende = 0,5 Punkte
- ❌ Vollständig falsch oder gar nicht = 0 Punkte

---

### **Aufgabe 6: Bubble Sort implementieren (7 Punkte)**

**Gegeben:** `zahlen = [5, 2, 8, 1, 9]`

---

**a) Struktogramm (3 Punkte)**

**Erwartete Struktur (BW-Standard nach Operatorenliste):**

```struktogramm
Deklaration und Initialisierung: n als Ganzzahl = Anzahl der Elemente des Arrays zahlen
Zähle i von 0 bis n - 2, Schrittweite 1
    Zähle j von 0 bis n - 2 - i, Schrittweite 1
        Wenn zahlen[j] > zahlen[j + 1], dann
            J
                Zuweisung: temp = zahlen[j]
                Zuweisung: zahlen[j] = zahlen[j + 1]
                Zuweisung: zahlen[j + 1] = temp
            , sonst
            N
                (keine Aktion)
```

**Bewertung Struktogramm (3 Punkte):**
- ✅ Äußere Schleife (for/while) (1 Punkt)
- ✅ Innere Schleife verschachtelt (1 Punkt)
- ✅ Vergleich und Tausch-Logik (1 Punkt)

**Häufige Fehler:**
| Fehler | Abzug |
|--------|-------|
| Schleifen nicht verschachtelt | -1 Punkt |
| Swap-Bedingung falsch (< statt >) | -0,5 |
| Schleifengrenzen falsch | -0,5 |
| Keine swap-Logik erkennbar | -0,75 |

---

**b) Python-Code (3 Punkte)**

**Musterlösung 1 (klassisch mit temp):**
## 📐 Struktogramm (grafische Notation)

<!-- START_GRAPHIC_STRUKTOGRAMM -->
```
┌────────────────────────────────────────┐
│ Deklaration: n = Anzahl Elemente       │
│ Zähle i von 0 bis n - 2, Schrittweite  │
│   Zähle j von 0 bis n - 2 - i, Schrittw│
│   eite 1                               │
│     Wenn zahlen[j] > zahlen[j + 1],    │
│     dann                               │
│       J                                │
│         Tausch mit temp                │
│       , sonst                          │
│       N                                │
│         (keine Aktion)                 │
└────────────────────────────────────────┘
```
<!-- END_GRAPHIC_STRUKTOGRAMM -->

```python
zahlen = [5, 2, 8, 1, 9]
n = len(zahlen)

for i in range(n - 1):
    for j in range(n - 1 - i):
        if zahlen[j] > zahlen[j + 1]:
            # Tausch
            temp = zahlen[j]
            zahlen[j] = zahlen[j + 1]
            zahlen[j + 1] = temp

print(zahlen)  # [1, 2, 5, 8, 9]
```

**Musterlösung 2 (mit Python-Tuple-Swap):**

## 📐 Struktogramm (grafische Notation)

<!-- START_GRAPHIC_STRUKTOGRAMM -->
```
┌────────────────────────────────────────┐
│ [STRUKTOGRAMM HIER HINZUFÜGEN]         │
│                                        │
│ Beispiel-Elemente:                     │
│ • Deklaration                          │
│ • Zuweisung                            │
│ • Schleife (┌─ ... ─┘)                 │
│ • Verzweigung (J/N Zweige)             │
└────────────────────────────────────────┘
```
<!-- END_GRAPHIC_STRUKTOGRAMM -->


```python
zahlen = [5, 2, 8, 1, 9]

for i in range(len(zahlen) - 1):
    for j in range(len(zahlen) - 1 - i):
        if zahlen[j] > zahlen[j + 1]:
            zahlen[j], zahlen[j + 1] = zahlen[j + 1], zahlen[j]

print(zahlen)
```

**Bewertung (3 Punkte):**
- ✅ Verschachtelte Schleifen mit Grenzen = 1,5 Punkte
- ✅ Swap-Logik korrekt = 1 Punkt
- ✅ Syntax korrekt = 0,5 Punkte
- ⚠️ Äußere Schleife falsch (z.B. `range(n)` statt `range(n-1)`) = -0,5
- ⚠️ Swap-Bedingung falsch = -0,75
- ❌ Keine Schleifenverschachtelung = 0 Punkte

---

**c) Ausgabe (1 Punkt)**

**Musterlösung:**
```
[1, 2, 5, 8, 9]
```

oder

```
1 2 5 8 9
```

**Bewertung (1 Punkt):**
- ✅ Korrekt sortiert = 1 Punkt
- ⚠️ Falsch sortiert, aber Code logisch = 0 Punkte (Fehler im Code)
- ❌ Nicht ausgefüllt = 0 Punkte

---

## 📊 ZUSAMMENFASSUNG ERWARTUNGSHORIZONT

| Aufgabe | Maximal | Anforderungsbereich | Kritische Felder |
|---------|---------|-------------------|------------------|
| **1** | 3 | I | Struktogramm-Syntax |
| **2** | 3 | II | Schleife + Bedingung korrekt |
| **3** | 3 | I | Array-Index, Zugriff |
| **4** | 6 | II | Schleife durchläuft korrekt |
| **5** | 8 | II/III | **Schreibtischtest nachvollziehbar** |
| **6** | 7 | III | **Swap-Logik korrekt** |
| **Summe** | **30** | — | — |

---

## ⚠️ KORREKTURHINWEISE FÜR LEHRER

### Allgemeine Prinzipien

1. **Struktogramme:** Struktur ist wichtiger als Perfektionismus
   - Handgezeichnet OK
   - Symbole müssen erkennbar sein (nicht einfach Pfeile)

2. **Schreibtische:** Nachvollziehbarkeit zählt
   - Jeder Schritt muss lesbar sein
   - Nicht Wert nach Wert, sondern Zustandsverlauf

3. **Logik vor Syntax**
   - Minore Syntaxfehler: -0,25 bis -0,5 Punkte
   - Logikfehler: -1 bis -2 Punkte

4. **Teilpunkte vergeben** (nicht alles-oder-nichts)
   - **2-Punkte-Aufgabe:** 2 oder 1 oder 0
   - **3-Punkte-Aufgabe:** 3, 2, 1, oder 0
    - **Komplexe Aufgaben (7-8 Punkte):** Feinere Abstufung möglich

### Häufige Schüler-Fehler akzeptieren

✅ **Akzeptabel auch wenn nicht optimal:**
- `for i in range(len(array))` vs. `for element in array` – beide OK
- while-Schleife statt for-Schleife bei Arrays – OK
- Tausch mit temp vs. Tuple-Swap – beide OK
- `if not gefunden` vs. `if gefunden == False` – beide OK
- Deutsche Variablennamen (z.B. `zaehler`) – OK

❌ **Nicht akzeptabel:**
- Struktogramm ist Flussdiagramm
- Array wird als Dictionary behandelt: `werte = {'0': 12, '1': 45}`
- Schleife wird nicht beendet
- Swap erfolgt falsch (`zahlen[j] = zahlen[j+1]` ohne temp)
- Index Out of Range (z.B. `zahlen[j+1]` wenn `j = len(zahlen)-1`)

### Besondere Hinweise zu Aufgaben

**Aufgabe 5 (Lineare Suche):**
- Der Schreibtischtest ist wichtig! Zeigt, ob Schüler den Algorithmus versteht
- Auch wenn Code fehlerhaft, kann Schreibtischtest +1 Punkt sein

**Aufgabe 6 (Bubble Sort):**
- Kontrollieren Sie die Swap-Bedingung genau
- Häufiger Fehler: `if zahlen[j] < zahlen[j+1]` (falsch herum)
- Schleifengrenzen (`range(n-1-i)`) sind kritisch

### Notenfelder

Bei 30 Punkten:
- **Note 1:** 27–30 (90%)
- **Note 2:** 24–26 (80%)
- **Note 3:** 21–23 (70%)
- **Note 4:** 18–20 (60%)
- **Note 5:** 15–17 (50%)
- **Note 6:** < 15 (< 50%)

---

## 🔍 LÖSUNGSÜBERPRÜFUNG – SCHNELLE CHECKLISTE

### Aufgabe 1
- [ ] Struktogramm zeigt if-else
- [ ] Code nutzt `if` und `else`
- [ ] Bedingung ist richtig (< 18, nicht <= 18)

### Aufgabe 2
- [ ] While-Schleife mit Bedingung != -1
- [ ] summe wird initialisiert
- [ ] summe wird in Schleife aktualisiert
- [ ] Ausgabe erfolgt in Schleife

### Aufgabe 3
- [ ] Array wird mit [ ] deklariert
- [ ] Indexing benutzt [0] für erstes Element
- [ ] len() zeigt Array-Länge

### Aufgabe 4
- [ ] a) Schleife durchläuft alle 8 Elemente
- [ ] b) Bedingung > 30 ist erfüllt, Ausgabe: 4 Werte
- [ ] c) Neues Array mit verdoppelten Werten

### Aufgabe 5
- [ ] Struktogramm zeigt Wiederholung + Verzweigung
- [ ] Code sucht korrekt (Index findet D bei Index 3)
- [ ] Schreibtischtest zeigt 4 Schritte bis zum Fund

### Aufgabe 6
- [ ] Äußere Schleife: `for i in range(n-1)`
- [ ] Innere Schleife: `for j in range(n-1-i)`
- [ ] Swap erfolgt bei `zahlen[j] > zahlen[j+1]`
- [ ] Ausgabe: [1, 2, 5, 8, 9]

---

**Version:** 1.0  
**Gültig für:** Klasse 2 (Informatik BG, 2-jährig & 3-jährig)  
**Erstellt:** 06.02.2026
