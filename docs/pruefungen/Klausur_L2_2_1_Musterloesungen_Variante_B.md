# Musterlösung & Erwartungshorizont
## Klassenarbeit: Kontrollstrukturen, Arrays (der Liste) und Algorithmen
## Variante B

**Dokumentation für Lehrkräfte**

Bezug: [docs/lehrplan/BPE5_Grundlagen_Programmierung.md](../lehrplan/BPE5_Grundlagen_Programmierung.md) und [docs/lehrplan/BPE7_Algorithmen_Datenstrukturen.md](../lehrplan/BPE7_Algorithmen_Datenstrukturen.md)

---

## 📌 Übersicht Erwartungshorizont

| Aufgabe | Punkte | Lösungstyp | Kritisch |
|---------|--------|-----------|----------|
| 1 | 3 | Struktogramm + Code | Bedingung korrekt |
| 2 | 3 | Struktogramm + Code | Schleifenabbruch |
| 3 | 3 | Grundlagen Arrays | Indexverständnis |
| 4 | 6 | Array-Algorithmen | Filter + neue Liste |
| 5 | 8 | Fehleranalyse | Ursache + Wirkung |
| 6 | 7 | Bubble Sort | Swap-Logik + Grenzen |
| **Summe** | **30** | — | — |

---

## ✅ MUSTERLÖSUNGEN MIT BEWERTUNG

### Aufgabe 1 (3)
```struktogramm
Deklaration und Einlesen: alter |als Ganzzahl|
Wenn alter >= 18, dann
    J
        Ausgabe: "Volljährig"
    , sonst
    N
        Ausgabe: "Minderjährig"
```

```python
def loese_aufgabe1_volljaehrig() -> None:
    alter = int(input("Alter: "))
    if alter >= 18:
        print("Volljährig")
    else:
        print("Minderjährig")
```

---

### Aufgabe 2 (3)
```struktogramm
Deklaration und Initialisierung: summe = 0
Deklaration und Einlesen: zahl |als Ganzzahl|
Wiederhole solange zahl != -1
    Zuweisung: summe = summe + zahl
    Ausgabe: summe
    Deklaration und Einlesen: zahl |als Ganzzahl|
Ausgabe: "Programm endet"
```

```python
def loese_aufgabe2_laufende_summe() -> None:
    summe = 0
    zahl = int(input("Zahl (-1 Ende): "))
    while zahl != -1:
        summe += zahl
        print(f"Summe: {summe}")
        zahl = int(input("Zahl (-1 Ende): "))
    print("Programm endet")
```

---

### Aufgabe 3 (3)

**a)**
```python
lager = [4, 7, 2, 9, 5, 1, 8, 3]
```

**b)**
```python
erstes = lager[0]
lager[-1] = 10
laenge = len(lager)
print(erstes, laenge)
```

**c)**
`lager[5]` = 6. Element, hier Wert `1`.

---

### Aufgabe 4 (6)

**a) Alle Werte ausgeben (2):**
```python
for wert in werte:
    print(wert)
```

**b) Nur gerade Werte (2):**
```python
for wert in werte:
    if wert % 2 == 0:
        print(wert)
```

**c) Liste halbiert (2):**
```python
halbiert: list[int] = []
for wert in werte:
    halbiert.append(wert // 2)
print(halbiert)
```

---

### Aufgabe 5 (8)

![L2_5_Aufgabe5_Algorithmen_pruefen_Fehleranalyse](../../struktogramme/generated/svg/L2_5_Aufgabe5_Algorithmen_pruefen_Fehleranalyse.svg)

- **a) Zweck (3):** lineare Suche in einer Liste.
- **b) Fehler (3):** Indexerhöhung im Nein-Zweig fehlt → kein Fortschritt, mögliche Endlosschleife.
- **c) Korrektur (2):**
```struktogramm
Zuweisung: i = i + 1
```

---

### Aufgabe 6: Bubble Sort (7)

**a) Struktogramm (3):**

![L2_6_Aufgabe6_Bubble_Sort](../../struktogramme/generated/svg/L2_6_Aufgabe6_Bubble_Sort.svg)

**b) Python (3):**
```python
def loese_aufgabe6_bubble_sort(zahlen: list[int]) -> list[int]:
    sortierte = zahlen.copy()
    n = len(sortierte)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if sortierte[j] > sortierte[j + 1]:
                temp = sortierte[j]
                sortierte[j] = sortierte[j + 1]
                sortierte[j + 1] = temp

    return sortierte


print(loese_aufgabe6_bubble_sort([42, 7, 19, 3, 25]))
```

**c) Ausgabe (1):**
`[3, 7, 19, 25, 42]`

---

## ⚠️ Korrekturhinweise

- Teilpunkte bei korrekter Schleifenstruktur vergeben.
- Bei Aufgabe 6 ist `if a[j] > a[j+1]` die zentrale Bedingung.
- Bei Aufgabe 5 reicht ein präziser, korrekter Fehlerhinweis für hohe Teilpunktzahl.

---

**Version:** 1.0
