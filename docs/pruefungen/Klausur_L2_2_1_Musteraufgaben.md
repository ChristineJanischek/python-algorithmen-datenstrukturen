# Klassenarbeit: Kontrollstrukturen, Arrays und Algorithmen
## Informatik – Berufliches Gymnasium (Klasse 2)

---

## 📋 Prüfungsinformationen

| Eigenschaft | Details |
|---|---|
| **Datum** | _________________ |
| **Klasse** | _____________________ |
| **Dauer** | 60 Minuten |
| **Erreichbare Punkte** | 30 Punkte |
| **Bestanden ab** | 15 Punkte (50%) |
| **Hilfsmittel** | Keine (Papier & Stift) |
| **Themen** | Algorithmen (70%): Kontrollstrukturen, Lineare Suche, Bubble Sort <br> Datenstrukturen (30%): Arrays |

---

## 📌 Allgemeine Anweisungen

- Alle Antworten auf diesem Blatt oder auf kariertem Papier eintragen
- Bei Aufgaben mit Struktogrammen: **Struktogramm ist erforderlich**
- Struktogramme **IMMER** in textbasierter Notation nach **Operatorenliste**: `struktogramme/Operatorenliste-Struktogramme.md`
- **BW-Standard:** Operatoren korrekt verwenden
  - ✅ `Deklaration und Einlesen:`, `Zuweisung:`, `Wenn...dann`, `Wiederhole solange`, `Zähle...von...bis`, `Ausgabe:`, `Rückgabe:`
  - ❌ **KEINE** englischen Keywords: `while`, `if`, `else`, `for`, `return`, `print`
- Programmcode muss **eine gültige Python-Syntax** haben
- Bei Algorithmusaufgaben sind **eigene Schleifenlösungen** erwartet (keine eingebauten Such- oder Kurzformen)
- **Alle Zwischenschritte zeigen** – Korrektur erfolgt nach Rechenweg, nicht nur Endergebnis
- Schreibtischtest: **Nachvollziehbares Durchlaufen** des Algorithmus aufschreiben
- Bei Fragen: **Fragen Sie, bevor Sie spekulieren!**

---

## 🎯 Aufgabenübersicht

| Aufgabe | Thema | Punkte | Anforderungsbereich |
|---------|-------|--------|-------------------|
| **1** | Kontrollstrukturen (if-else) | 3 | I – Reproduktion |
| **2** | Schleifen & Logik | 3 | II – Transfer |
| **3** | Arrays: Deklaration & Zugriff | 3 | I – Reproduktion |
| **4** | Arrays durchlaufen & filtern | 6 | II – Transfer |
| **5** | Lineare Suche | 8 | II/III – Transfer & Analyse |
| **6** | Sortieralgorithmus (Bubble Sort) | 7 | III – Kreativität |

**Summe: 30 Punkte**

---

## 📝 AUFGABENBLATT

### **Aufgabe 1: Verzweigung & Logik (3 Punkte)**
**Thema:** BPE 5.2 – Kontrollstrukturen (Alternativen)

Schreibe ein Struktogramm und implementiere in Python:
> Ein Programm liest eine Ganzzahl (Alter) ein und gibt aus:
> - „Jugendlicher" wenn das Alter < 18 ist
> - „Erwachsener" wenn das Alter >= 18 ist

**Anforderungen:**
- Struktogramm mit korrektem Aufbau (3 Punkte)
  - Eingabe darstellen
  - Verzweigung mit Bedingung
  - Ausgaben korrekt positioniert

```python
# Hier Lösung eintragen:


```

---

### **Aufgabe 2: Schleife mit Bedingung (3 Punkte)**
**Thema:** BPE 5.2 – Schleifen & Bedingungen

Schreibe ein Struktogramm und implementiere:
> Ein Programm liest positive Ganzzahlen ein, **solange** der Nutzer möchte.
> Nach jeder Eingabe wird die **Summe aller bisherigen Zahlen** ausgegeben.
> Das Programm endet, wenn die Eingabe **-1** ist.

**Beispiel:**
```
Eingabe: 5
Summe: 5
Eingabe: 3
Summe: 8
Eingabe: -1
Programm endet
```

**Anforderungen:**
- Struktogramm (min. 2 Punkte):
  - Wiederholung korrekt dargestellt
  - Abbruchbedingung erkennbar
- Python-Code (1 Punkt):
  - Funktionsfähig und nachvollziehbar

```python
# Hier Lösung eintragen:


```

---

### **Aufgabe 3: Array-Grundlagen (3 Punkte)**
**Thema:** BPE 7.1 – Arrays (Deklaration, Initialisierung, Zugriff)

**a) Deklaration (1 Punkt)**

Schreibe die Python-Zeile, um folgendes Array zu deklarieren und zu initialisieren:
> Noten: [1, 2, 2, 3, 1, 5, 4, 2]

```python
# Deklaration:


```

**b) Array-Zugriff (1 Punkt)**

Schreibe Python-Code, um:
- Das **1. Element** auslesen
- Das **letzte Element** ändern auf `1`
- Die **Länge des Arrays** ausgeben

```python
# Zugriff und Manipulation:


```

**c) Interpretation (1 Punkt)**

Was bedeutet `noten[3]` in Ihrem obigen Array?

```
Antwort:
```

---

### **Aufgabe 4: Array durchlaufen & filtern (6 Punkte)**
**Thema:** BPE 7.1 – Schleife über Arrays

Gegeben ist das Array: `werte = [12, 45, 23, 67, 8, 34, 56, 11]`

**a) Alle Werte ausgeben (2 Punkte)**

Schreibe ein Struktogramm und Python-Code, um **alle Elemente des Arrays** zeilenweise auszugeben.

Struktogramm (textbasierte Notation nach Operatorenliste):
```struktogramm
[Hier Struktogramm eintragen]
```

Python-Code:

**b) Elemente filtern (2 Punkte)**

Schreibe Python-Code, um **nur die Werte > 30** auszugeben.

```python
# Hier Lösung:


```

**c) Array manipulieren (2 Punkte)**

Schreibe Python-Code, um **jedes Element zu verdoppeln** und das Ergebnis in einem neuen Array zu speichern.

```python
# Hier Lösung:


```

---

### **Aufgabe 5: Lineare Suche (8 Punkte)**
**Thema:** BPE 7.2 – Suchalgorithmen

Gegeben ist das Array: `buchstaben = ['A', 'B', 'C', 'D', 'E', 'F', 'G']`

**Aufgabe:**

Schreibe ein Struktogramm und implementiere einen Python-Algorithmus, der:
1. **Einen Buchstaben vom Nutzer einliest**
2. **Diese Buchstabe im Array sucht** (Lineare Suche)
3. **Bei Fund:** Den Index (Position) ausgibt
4. **Bei Nicht-Fund:** „Nicht gefunden" ausgibt

**Anforderungen:**

**a) Struktogramm (3 Punkte):**
- Eingabe darstellen
- Wiederholung (for oder while) mit Abbruch
- Verzweigung (gefunden/nicht gefunden)
- Ausgabe

```struktogramm
[Hier Struktogramm eintragen]
```

**b) Python-Code (4 Punkte):**
- Hinweis: Verwende eine **eigene Schleife**, keine eingebauten Suchmethoden.
```python
# Lineare Suche implementieren:


```

**c) Schreibtischtest (1 Punkt):**

Führe Deinen Algorithmus mit der Eingabe „D" durch. Schreibe jeden Schritt auf!

```
Schritt 1: Index 0, Wert = A ≠ D
Schritt 2: ...
```

---

### **Aufgabe 6: Bubble Sort implementieren (7 Punkte)**
**Thema:** BPE 7.2 – Sortieralgorithmen (Bubble Sort)

Gegeben ist das Array: `zahlen = [5, 2, 8, 1, 9]`

**Aufgabe:**

Schreibe ein Struktogramm und implementiere **Bubble Sort** in Python.

**Anforderungen:**

**a) Struktogramm (3 Punkte):**
- Äußere Schleife (Durchläufe)
- Innere Schleife (Vergleiche & Tausch)
- Swap-Bedingung erkennbar
- Korrekte Verschachtelung

```struktogramm
[Hier Struktogramm eintragen]
```

**b) Python-Code (3 Punkte):**
- Hinweis: Verwende **verschachtelte Schleifen** und eine klare Tauschlogik.
```python
# Bubble Sort implementieren:


```

**c) Ausgabe (1 Punkt):**

Wie sieht das sortierte Array aus?

```
Antwort: _______________
```

---

## ✅ Checkliste vor Abgabe

- [ ] Alle Aufgaben bearbeitet
- [ ] Struktogramme lesbar und vollständig
- [ ] Python-Code syntaktisch korrekt (soweit möglich)
- [ ] Bei Algorithmusaufgaben nur Schleifenloesungen verwendet
- [ ] Alle Zwischenschritte erklärt
- [ ] Schreibtischtest nachvollziehbar
- [ ] Name & Datum oben eingetragen

---

## 📊 Bewertungsmaßstab

| Erreichte Punkte | % | Note | Kommentar |
|---|---|---|---|
| 27–30 | 90–100 | 1 | Sehr gut |
| 24–26 | 80–89 | 2 | Gut |
| 21–23 | 70–79 | 3 | Befriedigend |
| 18–20 | 60–69 | 4 | Ausreichend |
| 15–17 | 50–59 | 5 | Mangelhaft |
| < 15 | < 50 | 6 | Ungenügend |

---

**Viel Erfolg! 🚀**

---

*Klassenstufe:* ________ *Name:* __________________ *Klasse:* __________
