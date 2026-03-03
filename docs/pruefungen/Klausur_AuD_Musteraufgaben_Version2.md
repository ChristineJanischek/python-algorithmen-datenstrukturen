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
> Ein Programm liest eine Ganzzahl `punkte` ein und gibt aus:
> - „Bestanden" wenn `punkte >= 50`
> - „Nicht bestanden" wenn `punkte < 50`

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
**Thema:** BPE 7.1 – Arrays (Listen)

Gegeben ist die Liste:
`temperaturen = [18, 21, 19, 23, 17, 20, 22, 16]`

**a) Deklaration (1 Punkt)**

Schreibe die Python-Zeile zur Deklaration und Initialisierung.

```python
# Deklaration:

```

**b) Zugriff (1 Punkt)**

Schreibe Python-Code, um:
- das **2. Element** auszugeben,
- das **vorletzte Element** auf `25` zu setzen,
- die **Länge** auszugeben.

```python
# Zugriff und Manipulation:

```

**c) Interpretation (1 Punkt)**

Was bedeutet `temperaturen[4]`?

```
Antwort:
```

---

### **Aufgabe 4: Array (Liste) durchlaufen & filtern (6 Punkte)**
**Thema:** BPE 7.1 – Schleife über Arrays (Listen)

Gegeben ist: `werte = [14, 9, 31, 27, 45, 12, 6, 39]`

**a) Alle Werte ausgeben (2 Punkte)**

Schreibe Struktogramm + Python-Code, um alle Werte zeilenweise auszugeben.

**b) Elemente filtern (2 Punkte)**

Gib nur Werte aus, die **durch 3 teilbar** sind.

**c) Array manipulieren (2 Punkte)**

Erzeuge eine neue Liste `plus_fuenf`, die jedes Element von `werte` um 5 erhöht enthält.

```python
# Lösung kommt in die digitale Lösungsdatei oder auf das ausgeteilte Papier!

```

---

### **Aufgabe 5: Algorithmen prüfen (8 Punkte)**
**Thema:** BPE 7.2 – Algorithmenanalyse

Gegeben: `codes = ['K1', 'K2', 'K3', 'K4', 'K5', 'K6', 'K7']`

Das folgende Struktogramm enthält einen logischen Fehler:

![L2_5_Aufgabe5_Algorithmen_pruefen_Fehleranalyse](../../struktogramme/generated/svg/L2_5_Aufgabe5_Algorithmen_pruefen_Fehleranalyse.svg)
<!-- DOCX-ALT-TEXT: L2_5_Aufgabe5_Algorithmen_pruefen_Fehleranalyse -->
<!-- DOCX-EMBED-SVG: ../../struktogramme/generated/svg/L2_5_Aufgabe5_Algorithmen_pruefen_Fehleranalyse.svg -->
<!-- DOCX-EMBEDDING-HINT: Dieses Struktogramm wird bei DOCX-Export als eingebettete Grafik dargestellt für bessere Kopierbarkeit und Formatierung. -->

Bearbeite:

**a) Vermuteter Zweck (3 Punkte)**

**b) Fehleranalyse (3 Punkte)**

**c) BW-konformer Korrekturvorschlag (2 Punkte)**

---

### **Aufgabe 6: Selection Sort implementieren (7 Punkte)**
**Thema:** BPE 7.2 – Sortieralgorithmen (Selection Sort)

Gegeben: `zahlen = [29, 14, 37, 10, 18]`

Schreibe ein Struktogramm und implementiere **Selection Sort aufsteigend**.

**a) Struktogramm (3 Punkte)**
- äußere Schleife (Position `i`)
- innerer Vergleich (Minimum finden)
- Tausch an Position `i`

**b) Python-Code (3 Punkte)**

**c) Ausgabe (1 Punkt)**

Wie sieht die sortierte Liste aus?

```
Antwort: __________________
```

---

## ✅ Checkliste vor Abgabe

- [ ] Alle Aufgaben bearbeitet
- [ ] Struktogramme lesbar und vollständig
- [ ] Python-Code syntaktisch korrekt (soweit möglich)
- [ ] Bei Algorithmusaufgaben nur Schleifenlösungen verwendet
- [ ] Fehleranalyse nachvollziehbar begründet

---

**Viel Erfolg! 🚀**
