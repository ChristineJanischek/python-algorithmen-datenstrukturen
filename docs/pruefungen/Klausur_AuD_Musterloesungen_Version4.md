# Musterlösung & Erwartungshorizont
## Klassenarbeit: Kontrollstrukturen, Arrays (der Liste) und Algorithmen
## Version 4

**Dokumentation für Lehrkräfte**

Bezug: [docs/lehrplan/BPE5_Grundlagen_Programmierung.md](../lehrplan/BPE5_Grundlagen_Programmierung.md) und [docs/lehrplan/BPE7_Algorithmen_Datenstrukturen.md](../lehrplan/BPE7_Algorithmen_Datenstrukturen.md)

SVG-Basis: BW-Formvorlagen aus `apps/drawio-extension/stencil.xml`.

---

## 📌 Bewertungstabelle

| Aufgabe | Punkte | Schwerpunkt |
|---------|--------|-------------|
| 1 | 3 | Alternative (gerade/ungerade) |
| 2 | 3 | Schleife + Maximum |
| 3 | 3 | Array-Zugriff |
| 4 | 6 | Durchlaufen, Filtern, Transformieren |
| 5 | 8 | Fehleranalyse Algorithmus |
| 6 | 7 | Selection Sort |
| **Summe** | **30** | — |

---

## ✅ MUSTERLÖSUNGEN

### Aufgabe 1 (3)
![L2_VarC_Aufgabe1_Gerade_Ungerade](../../struktogramme/generated/svg/L2_VarC_Aufgabe1_Gerade_Ungerade.svg)

```struktogramm
Deklaration und Einlesen: zahl als Ganzzahl
Wenn zahl % 2 == 0, dann
    J
        Ausgabe: "Gerade"
    , sonst
    N
        Ausgabe: "Ungerade"
```

```python
def loese_aufgabe1_gerade_ungerade() -> None:
    zahl = int(input("Zahl: "))
    if zahl % 2 == 0:
        print("Gerade")
    else:
        print("Ungerade")
```

---

### Aufgabe 2 (3)
![L2_VarC_Aufgabe2_Maximum](../../struktogramme/generated/svg/L2_VarC_Aufgabe2_Maximum.svg)

```struktogramm
Deklaration und Initialisierung: maximum = -999999
Deklaration und Einlesen: zahl als Ganzzahl
Wiederhole solange zahl != -1
    Wenn zahl > maximum, dann
        J
            Zuweisung: maximum = zahl
        , sonst
        N
            (keine Anweisung)
    Ausgabe: maximum
    Deklaration und Einlesen: zahl als Ganzzahl
Ausgabe: "Programm endet"
```

```python
def loese_aufgabe2_maximum() -> None:
    maximum = -999999
    zahl = int(input("Zahl (-1 Ende): "))

    while zahl != -1:
        if zahl > maximum:
            maximum = zahl
        print(f"Maximum: {maximum}")
        zahl = int(input("Zahl (-1 Ende): "))

    print("Programm endet")
```

---

### Aufgabe 3 (3)

**a)**
![L2_3a_Aufgabe3_Array_Deklaration](../../struktogramme/generated/svg/L2_3a_Aufgabe3_Array_Deklaration.svg)

```python
noten = [2, 3, 1, 4, 2, 5, 3, 1]
```

**b)**
![L2_3b_Aufgabe3_Array_Zugriff](../../struktogramme/generated/svg/L2_3b_Aufgabe3_Array_Zugriff.svg)

```python
drittes = noten[2]
noten[0] = 1
laenge = len(noten)
print(drittes, laenge)
```

**c)**
`noten[6]` bedeutet: 7. Element, Wert `3`.

---

### Aufgabe 4 (6)

Gegeben: `werte = [11, 28, 35, 40, 53, 64, 79, 82]`

**a)**
![L2_4a_Aufgabe4_Array_Ausgeben_Index](../../struktogramme/generated/svg/L2_4a_Aufgabe4_Array_Ausgeben_Index.svg)

```python
for wert in werte:
    print(wert)
```

**b)**
![L2_4b_Aufgabe4_Array_Filtern](../../struktogramme/generated/svg/L2_4b_Aufgabe4_Array_Filtern.svg)

```python
for wert in werte:
    if wert >= 40:
        print(wert)
```

**c)**
![L2_4c1_Aufgabe4_Array_Verdoppeln_Neue_Liste](../../struktogramme/generated/svg/L2_4c1_Aufgabe4_Array_Verdoppeln_Neue_Liste.svg)

```python
quadriert: list[int] = []
for wert in werte:
    quadriert.append(wert * wert)
print(quadriert)
```

---

### Aufgabe 5 (8)

![L2_5_Aufgabe5_Algorithmen_pruefen_Fehleranalyse](../../struktogramme/generated/svg/L2_5_Aufgabe5_Algorithmen_pruefen_Fehleranalyse.svg)

**a) Zweck (3):**
Lineare Suche in der Zeichenliste nach Eingabe.

**b) Fehler (3):**
Fehlende Indexerhöhung im Nein-Zweig → dasselbe Element wird wiederholt geprüft.

**c) Korrektur (2):**
```struktogramm
Zuweisung: i = i + 1
```

---

### Aufgabe 6: Selection Sort (7)

**a) Struktogramm (3):**

![L2_6_Aufgabe6_Selection_Sort](../../struktogramme/generated/svg/L2_6_Aufgabe6_Selection_Sort.svg)

**BW-Notation (Operatorenliste v2.2):**
```struktogramm
Deklaration und Initialisierung: zahlen = [33, 12, 27, 5, 18]
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


print(loese_aufgabe6_selection_sort([33, 12, 27, 5, 18]))
```

**c) Ausgabe (1):**
`[5, 12, 18, 27, 33]`

---

## ⚠️ Korrekturhinweise

- Teilpunkte bei korrekter Struktur vergeben.
- Aufgabe 2: Maximum muss nur bei größerem Wert aktualisiert werden.
- Aufgabe 6: Häufige Fehler sind falsche Grenzen und fehlender Tausch.

---

**Version:** 1.0
