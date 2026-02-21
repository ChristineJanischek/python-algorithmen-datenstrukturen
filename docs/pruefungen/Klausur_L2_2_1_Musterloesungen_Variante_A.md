# Musterlösung & Erwartungshorizont
## Klassenarbeit: Kontrollstrukturen, Arrays (der Liste) und Algorithmen
## Variante A

**Dokumentation für Lehrkräfte**

Bezug: [docs/lehrplan/BPE5_Grundlagen_Programmierung.md](../lehrplan/BPE5_Grundlagen_Programmierung.md) und [docs/lehrplan/BPE7_Algorithmen_Datenstrukturen.md](../lehrplan/BPE7_Algorithmen_Datenstrukturen.md)

---

## 📌 Übersicht Erwartungshorizont

| Aufgabe | Punkte | Lösungstyp | Bewertung |
|---------|--------|-----------|----------|
| 1 | 3 | Struktogramm + Code | Bedingung + Ausgaben korrekt |
| 2 | 3 | Struktogramm + Code | Schleifenlogik + Abbruch |
| 3 | 3 | Deklaration/Zugriff/Interpretation | Indizes korrekt |
| 4 | 6 | Array-Algorithmen | je Teilaufgabe 2 Punkte |
| 5 | 8 | Fehleranalyse | Ursache + Auswirkung + Korrektur |
| 6 | 7 | Selection Sort | Min-Suche + Tauschlogik |
| **Summe** | **30** | — | — |

---

## ✅ MUSTERLÖSUNGEN MIT BEWERTUNG

### **Aufgabe 1 (3 Punkte)**

**Muster-Struktogramm (textbasiert):**
```struktogramm
Deklaration und Einlesen: punkte |als Ganzzahl|
Wenn punkte >= 50, dann
    J
        Ausgabe: "Bestanden"
    , sonst
    N
        Ausgabe: "Nicht bestanden"
```

**Python-Musterlösung:**
```python
def loese_aufgabe1_bestanden() -> None:
    punkte = int(input("Punkte: "))
    if punkte >= 50:
        print("Bestanden")
    else:
        print("Nicht bestanden")
```

**Bewertung (3):**
- Struktogramm korrekt (1)
- Python-Syntax korrekt (1)
- Logik korrekt (1)

---

### **Aufgabe 2 (3 Punkte)**

**Muster-Struktogramm (textbasiert):**
```struktogramm
Deklaration und Initialisierung: anzahl = 0
Deklaration und Einlesen: zahl |als Ganzzahl|
Wiederhole solange zahl != -1
    Zuweisung: anzahl = anzahl + 1
    Ausgabe: anzahl
    Deklaration und Einlesen: zahl |als Ganzzahl|
Ausgabe: "Programm endet"
```

**Python-Musterlösung:**
```python
def loese_aufgabe2_anzahl() -> None:
    anzahl = 0
    zahl = int(input("Zahl (-1 zum Ende): "))
    while zahl != -1:
        anzahl += 1
        print(f"Anzahl: {anzahl}")
        zahl = int(input("Zahl (-1 zum Ende): "))
    print("Programm endet")
```

**Bewertung (3):**
- Schleifenstruktur (2)
- Funktionierender Code (1)

---

### **Aufgabe 3 (3 Punkte)**

**a) Deklaration (1):**
```python
temperaturen = [18, 21, 19, 23, 17, 20, 22, 16]
```

**b) Zugriff (1):**
```python
zweites = temperaturen[1]
temperaturen[-2] = 25
laenge = len(temperaturen)
print(zweites, laenge)
```

**c) Interpretation (1):**
`temperaturen[4]` ist das 5. Element (Wert: `17`).

---

### **Aufgabe 4 (6 Punkte)**

Gegeben: `werte = [14, 9, 31, 27, 45, 12, 6, 39]`

**a) Alle Werte ausgeben (2):**
```python
for wert in werte:
    print(wert)
```

**b) Durch 3 teilbar (2):**
```python
for wert in werte:
    if wert % 3 == 0:
        print(wert)
```

**c) Neue Liste plus_fuenf (2):**
```python
plus_fuenf: list[int] = []
for wert in werte:
    plus_fuenf.append(wert + 5)
print(plus_fuenf)
```

---

### **Aufgabe 5 (8 Punkte)**

**Fehlerhaftes Struktogramm:**

![L2_5_Aufgabe5_Algorithmen_pruefen_Fehleranalyse](../../struktogramme/generated/svg/L2_5_Aufgabe5_Algorithmen_pruefen_Fehleranalyse.svg)

**a) Zweck (3):**
Lineare Suche in einem Array/einer Liste nach einem eingegebenen Wert.

**b) Fehleranalyse (3):**
Im Nein-Zweig fehlt die Fortschrittsanweisung `i = i + 1`; dadurch kann eine Endlosschleife entstehen.

**c) Korrektur (2):**
```struktogramm
Zuweisung: i = i + 1
```

---

### **Aufgabe 6: Selection Sort (7 Punkte)**

**a) Struktogramm (3, textbasiert):**
```struktogramm
Deklaration und Initialisierung: zahlen = [29, 14, 37, 10, 18]
Deklaration und Initialisierung: n = Anzahl der Elemente des Arrays zahlen
Zähle i von 0 bis n - 2, Schrittweite 1
    Deklaration und Initialisierung: min_index = i
    Zähle j von i + 1 bis n - 1, Schrittweite 1
        Wenn zahlen[j] < zahlen[min_index], dann
            J
                Zuweisung: min_index = j
    Wenn min_index != i, dann
        J
            Deklaration und Initialisierung: temp = zahlen[i]
            Zuweisung: zahlen[i] = zahlen[min_index]
            Zuweisung: zahlen[min_index] = temp
Ausgabe: zahlen
```

**b) Python-Code (3):**
```python
def loese_aufgabe6_selection_sort(zahlen: list[int]) -> list[int]:
    sortierte = zahlen.copy()
    n = len(sortierte)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if sortierte[j] < sortierte[min_index]:
                min_index = j
        if min_index != i:
            temp = sortierte[i]
            sortierte[i] = sortierte[min_index]
            sortierte[min_index] = temp
    return sortierte


print(loese_aufgabe6_selection_sort([29, 14, 37, 10, 18]))
```

**c) Ausgabe (1):**
`[10, 14, 18, 29, 37]`

---

## 📊 Kurzbewertung

- **Kritisch bei Aufgabe 5:** Fehlerursache muss korrekt benannt sein.
- **Kritisch bei Aufgabe 6:** Minimum-Suche + Tausch an Position `i`.
- **Teilpunkte** bei nachvollziehbarer Zwischenlogik vergeben.

---

**Version:** 1.0
