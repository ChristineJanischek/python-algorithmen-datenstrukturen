# Klassenarbeit:  Algorithmen und Datenstrukturen
<!-- DOCX-CODE-STYLING: bg=#F2F2F2, text=#111111, border=#C8C8C8 -->
## Informatik – Berufliches Gymnasium (Jahrgangsstufe 2)
<!-- DOCX-FUSSZEILE: Version 1 (Archiv) -->

---

## 📋 Prüfungsinformationen

| Eigenschaft | Details |
|---|---|
| **Datum** | _________________ |
| **Klasse** | _____________________ |
| **Dauer** | 60 Minuten |
| **Erreichbare Punkte** | 30 Punkte |
| **Hilfsmittel** | Keine (Papier , Stift, digitale Dokumentationsdatei) |
| **Themen** | Algorithmen (70%) und Datenstrukturen (30%) |

---

## 📌 Allgemeine Anweisungen

- Alle Antworten in der digitalen Vorlage dokumentieren. Alternativ das ausgehändigte Papier verwenden.
- Bei Aufgaben mit Struktogrammen: **Struktogramm ist erforderlich**
- **BW-Standard:** Operatorenliste für Struktogramme - in der aktuellsten Version (https://www.schule-bw.de/)
- Programmcode muss **eine gültige Python-Syntax** haben
- Bei Algorithmus-Aufgaben sind **eigene Schleifenlösungen** erwartet (keine eingebauten Such- oder Kurzformen)
- **Alle Zwischenschritte zeigen** – Korrektur erfolgt nach Rechenweg, nicht nur Endergebnis
- Analyseaufgaben: **Zweck und Fehlerursache** klar und nachvollziehbar begründen
- Bei Fragen: **Fragen Sie, bevor Sie spekulieren!**

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
# Lösung kommt in die digitale Lösungsdatei oder auf das ausgeteilte Papier!

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
# Lösung kommt in die digitale Lösungsdatei oder auf das ausgeteilte Papier!

```

---

### **Aufgabe 3: Array-/Listen-Grundlagen (3 Punkte)**
**Thema:** BPE 7.1 – Arrays (Listen) (Deklaration, Initialisierung, Zugriff)

**a) Deklaration (1 Punkt)**

Schreibe die Python-Zeile, um folgendes Array (Liste) zu deklarieren und zu initialisieren:
> Noten: [1, 2, 2, 3, 1, 5, 4, 2]

```python
# Deklaration:

```

**b) Array-/Listen-Zugriff (1 Punkt)**

Schreibe Python-Code, um:
- Das **1. Element** auslesen
- Das **letzte Element** ändern auf `1`
- Die **Länge des Arrays (der Liste)** ausgeben

```python
# Zugriff und Manipulation:

```

**c) Interpretation (1 Punkt)**

Was bedeutet `noten[3]` in Ihrem obigen Array (Liste)?

```
Antwort:
```

---

### **Aufgabe 4: Array (Liste) durchlaufen & filtern (6 Punkte)**
**Thema:** BPE 7.1 – Schleife über Arrays (Listen)

Gegeben ist das Array (Liste): `werte = [12, 45, 23, 67, 8, 34, 56, 11]`

**a) Alle Werte ausgeben (2 Punkte)**

Schreibe ein Struktogramm und Python-Code, um **alle Elemente des Arrays (der Liste)** zeilenweise auszugeben.

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

**c) Array (Liste) manipulieren (2 Punkte)**

Schreibe Python-Code, um **jedes Element zu verdoppeln** und das Ergebnis in einem neuen Array (Liste) zu speichern.

```python
# Hier Lösung:

```

---

### **Aufgabe 5: Algorithmen prüfen (8 Punkte)**
**Thema:** BPE 7.2 – Algorithmenanalyse

Gegeben ist das Array (Liste): `buchstaben = ['A', 'B', 'C', 'D', 'E', 'F', 'G']`

**Aufgabe (Analyse eines fehlerhaften Struktogramms):**

Das folgende Struktogramm wurde mit der BW-Operatorenliste (Draw.io-Library) entworfen und enthält **einen häufigen logischen Fehler**.

![L2_5_Aufgabe5_Algorithmen_pruefen_Fehleranalyse](../../archiv/struktogramme/generated/svg/L2_5_Aufgabe5_Algorithmen_pruefen_Fehleranalyse.svg)
<!-- DOCX-ALT-TEXT: L2_5_Aufgabe5_Algorithmen_pruefen_Fehleranalyse -->
<!-- DOCX-EMBED-SVG: ../../archiv/struktogramme/generated/svg/L2_5_Aufgabe5_Algorithmen_pruefen_Fehleranalyse.svg -->
<!-- DOCX-EMBEDDING-HINT: Dieses Struktogramm wird bei DOCX-Export als eingebettete Grafik dargestellt für bessere Kopierbarkeit und Formatierung. -->

Bearbeite die Teilaufgaben in dieser Reihenfolge:

**a) Vermuteter Zweck (3 Punkte):**

Beschreibe in 2–4 Sätzen, **welchen Zweck** der Algorithmus wahrscheinlich hat.

```
Antwort:
```

**b) Fehleranalyse (3 Punkte):**

Nenne den **logischen Fehler** im Struktogramm und erkläre kurz die Auswirkung auf die Programmausführung.

```
Antwort:
```

**c) Korrekturvorschlag (2 Punkte):**

Formuliere die fehlende/falsch platzierte Anweisung in **BW-konformer Operator-Notation**.

```
Antwort:
```

---

### **Aufgabe 6: Bubble Sort implementieren (7 Punkte)**
**Thema:** BPE 7.2 – Sortieralgorithmen (Bubble Sort)

Gegeben ist das Array (Liste): `zahlen = [5, 2, 8, 1, 9]`

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

Wie sieht das sortierte Array (Liste) aus?

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
- [ ] Fehleranalyse nachvollziehbar begründet
- [ ] Name & Datum oben eingetragen

---

**Viel Erfolg! 🚀**

---

*Klassenstufe:* ________ *Name:* __________________ *Klasse:* __________
