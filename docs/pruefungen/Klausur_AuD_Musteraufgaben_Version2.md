# Klassenarbeit:  Algorithmen und Datenstrukturen
<!-- DOCX-CODE-STYLING: bg=#F2F2F2, text=#111111, border=#C8C8C8 -->
## Informatik – Berufliches Gymnasium (Jahrgangsstufe 2)
<!-- DOCX-FUSSZEILE: Version 2 -->

---

## 📋 Prüfungsinformationen

| Eigenschaft | Details |
|---|---|
| **Datum** | _________________ |
| **Klasse** | _____________________ |
| **Dauer** | 60 Minuten |
| **Erreichbare Punkte** | 30 Punkte |
| **Hilfsmittel** | Keine (Papier, Stift, digitale Dokumentationsdatei) |
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
> Ein Programm liest eine Ganzzahl `punkte` ein und gibt aus:
> - „Bestanden" wenn `punkte >= 50`
> - „Nicht bestanden" wenn `punkte < 50`

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
> Ein Programm liest Ganzzahlen ein. Nach jeder Eingabe wird die bisherige **Anzahl gültiger Eingaben** ausgegeben.
> Das Programm endet bei Eingabe `-1`.

**Beispiel:**
```
Eingabe: 7
Anzahl: 1
Eingabe: 12
Anzahl: 2
Eingabe: -1
Programm endet
```

```python
# Lösung kommt in die digitale Lösungsdatei oder auf das ausgeteilte Papier!

```

---

### **Aufgabe 3: Array-/Listen-Grundlagen (3 Punkte)**
**Thema:** BPE 7.1 – Arrays (Listen) (Deklaration, Initialisierung, Zugriff)

Gegeben ist die Liste:
`temperaturen = [18, 21, 19, 23, 17, 20, 22, 16]`

**a) Deklaration (1 Punkt)**

Schreibe die Python-Zeile zur Deklaration und Initialisierung.

```python
# Lösung kommt in die digitale Lösungsdatei oder auf das ausgeteilte Papier!

```

**b) Zugriff (1 Punkt)**

Schreibe Python-Code, um:
- das **2. Element** auszugeben
- das **vorletzte Element** auf `25` zu setzen
- die **Länge** auszugeben

```python
# Lösung kommt in die digitale Lösungsdatei oder auf das ausgeteilte Papier!

```

**c) Interpretation (1 Punkt)**

Was bedeutet `temperaturen[4]`?

```
[Lösung kommt in die digitale Lösungsdatei oder auf das ausgeteilte Papier!]
```

---

### **Aufgabe 4: Array (Liste) durchlaufen & filtern (6 Punkte)**
**Thema:** BPE 7.1 – Schleife über Arrays (Listen)

Gegeben ist: `werte = [14, 9, 31, 27, 45, 12, 6, 39]`

**a) Alle Werte ausgeben (2 Punkte)**

Schreibe ein Struktogramm und Python-Code, um alle Werte zeilenweise auszugeben.

**Anforderungen:**
- Struktogramm (1 Punkt):
  - Schleife über Array erkennbar
  - Array-Zugriff mit Index
- Python-Code (1 Punkt):
  - Funktionsfähig und nachvollziehbar

```python
# Lösung kommt in die digitale Lösungsdatei oder auf das ausgeteilte Papier!

```

**b) Elemente filtern (2 Punkte)**

Schreibe Python-Code, um nur Werte auszugeben, die **durch 3 teilbar** sind.

**Anforderungen:**
- Bedingung korrekt formuliert
- Nur passende Werte ausgeben

```python
# Lösung kommt in die digitale Lösungsdatei oder auf das ausgeteilte Papier!

```

**c) Array manipulieren (2 Punkte)**

Schreibe Python-Code, um eine neue Liste `plus_fuenf` zu erzeugen, die jedes Element von `werte` um 5 erhöht enthält.

**Anforderungen:**
- Neue Liste erzeugt und korrekt benannt
- Alle Elemente um 5 erhöht

```python
# Lösung kommt in die digitale Lösungsdatei oder auf das ausgeteilte Papier!

```

---

### **Aufgabe 5: Algorithmen prüfen (8 Punkte)**
**Thema:** BPE 7.2 – Algorithmenanalyse

Gegeben: `codes = ['K1', 'K2', 'K3', 'K4', 'K5', 'K6', 'K7']` (sortiert)

Das folgende Struktogramm wurde mit der BW-Operatorenliste (Draw.io-Library) entworfen und enthält **einen häufigen logischen Fehler** in einem Suchalgorithmus.

![L2_5_Aufgabe5_Algorithmen_pruefen_Fehleranalyse](../../struktogramme/generated/svg/L2_5_Aufgabe5_Binaere_Suche_Fehleranalyse.svg)
<!-- DOCX-ALT-TEXT: L2_5_Aufgabe5_Algorithmen_pruefen_Fehleranalyse -->
<!-- DOCX-EMBED-SVG: ../../struktogramme/generated/svg/L2_5_Aufgabe5_Binaere_Suche_Fehleranalyse.svg -->
<!-- DOCX-EMBEDDING-HINT: Dieses Struktogramm wird bei DOCX-Export als eingebettete Grafik dargestellt für bessere Kopierbarkeit und Formatierung. -->

Bearbeite die Teilaufgaben in dieser Reihenfolge:

**a) Vermuteter Zweck (3 Punkte)**

Beschreibe in 2–4 Sätzen, **welchen Zweck** der Algorithmus wahrscheinlich hat.

**Anforderungen:**
- Klare und nachvollziehbare Beschreibung
- Bezug auf Suchstrategie und Ablaufstruktur im Struktogramm

```
[Lösung kommt in die digitale Lösungsdatei oder auf das ausgeteilte Papier!]
```

**b) Fehleranalyse (3 Punkte)**

Nenne den **logischen Fehler** im Struktogramm und erkläre kurz die Auswirkung auf die Programmausführung.

**Anforderungen:**
- Fehler klar identifiziert
- Auswirkung auf Suchbereich und Ergebnis nachvollziehbar erklärt

```
[Lösung kommt in die digitale Lösungsdatei oder auf das ausgeteilte Papier!]
```

**c) BW-konformer Korrekturvorschlag (2 Punkte)**

Formuliere die falsch gesetzten Anweisungen im Vergleichszweig in **BW-konformer Operator-Notation** korrekt.

**Anforderungen:**
- Korrekte Notation nach Operatorenliste
- Lösung ist für den vorliegenden Suchalgorithmus logisch korrekt

```
[Lösung kommt in die digitale Lösungsdatei oder auf das ausgeteilte Papier!]
```

---

### **Aufgabe 6: Selection Sort implementieren (7 Punkte)**
**Thema:** BPE 7.2 – Sortieralgorithmen (Selection Sort)

Gegeben: `zahlen = [29, 14, 37, 10, 18]`

Schreibe ein Struktogramm und implementiere **Selection Sort aufsteigend**.

**a) Struktogramm (3 Punkte)**

**Anforderungen:**
- Äußere Schleife (Position `i`)
- Innerer Vergleich (Minimum finden)
- Tausch an Position `i`
- Korrekte Verschachtelung

```struktogramm
[Lösung kommt in die digitale Lösungsdatei oder auf das ausgeteilte Papier!]
```

**b) Python-Code (3 Punkte)**

**Anforderungen:**
- Verschachtelte Schleifen
- Klare Tauschlogik
- Sortierung aufsteigend

```python
# Lösung kommt in die digitale Lösungsdatei oder auf das ausgeteilte Papier!

```

**c) Ausgabe (1 Punkt)**

Wie sieht die sortierte Liste aus?

```
[Lösung kommt in die digitale Lösungsdatei oder auf das ausgeteilte Papier!]
```

---

## ✅ Checkliste vor Abgabe

- [ ] Alle Aufgaben bearbeitet
- [ ] Struktogramme lesbar und vollständig
- [ ] Python-Code syntaktisch korrekt (soweit möglich)
- [ ] Bei Algorithmusaufgaben nur Schleifenlösungen verwendet
- [ ] Alle Zwischenschritte zeigen – Korrektur erfolgt nach Rechenweg
- [ ] Fehleranalyse nachvollziehbar begründet
- [ ] Name & Datum oben eingetragen

---

**Viel Erfolg! 🚀**
