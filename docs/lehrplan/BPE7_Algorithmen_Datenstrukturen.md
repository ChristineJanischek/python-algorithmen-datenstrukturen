# BPE 7: Algorithmen und Datenstrukturen

**Zeitrichtwert:** 30 Stunden

## Übergeordnete Ziele

Die Schülerinnen und Schüler beschreiben die Datenstrukturen Array, verkettete Liste, Stapelspeicher, Warteschlange und Baum. Unter Verwendung einer Programmiersprache am Gerät implementieren die Schülerinnen und Schüler Arrays und wenden Such- und Sortieralgorithmen zur Problemlösung an.

---

## BPE 7.1: Arrays (Eindimensionale Felder)

**Lernziel:** Die Schülerinnen und Schüler beschreiben und implementieren eindimensionale Arrays. Sie entwerfen mit der Datenstruktur Array Algorithmen zur Problemlösung in einer Programmiersprache.

### Themen

| Thema | Inhalt |
|-------|--------|
| **Grundlagen von Arrays** | Deklaration und Initialisierung eines Arrays |
| | Länge des Arrays (z. B.) |
| **Zugriff auf Array-Felder** | – Index-Operator |
| | – Zugriff über Schleife |

### Lernziele

- ✅ Arrays deklarieren und initialisieren
- ✅ Auf Array-Elemente via Index zugreifen
- ✅ Array-Elemente über Schleifen verarbeiten
- ✅ Länge eines Arrays bestimmen
- ✅ Einfache Array-Algorithmen implementieren

---

## BPE 7.2: Such- und Sortieralgorithmen

**Lernziel:** Die Schülerinnen und Schüler erläutern Sortier- und Suchalgorithmen anhand der Datenstruktur Array. Sie wenden die Sortier- und Suchalgorithmen zur Lösung von Problemstellungen an und implementieren diese.

### Sortieralgorithmen

| Algorithmus | Beschreibung |
|-------------|------------|
| **Selection Sort** | Wählt das Minimum und tauscht es an die richtige Position |
| **Bubble Sort** | Benachbarte Elemente werden verglichen und getauscht |

### Suchalgorithmen

| Algorithmus | Beschreibung | Voraussetzung |
|-------------|------------|--------------|
| **Lineare Suche** | Durchsucht Array von Anfang bis Ende | – |
| **Binäre Suche** | Halbiert Suchbereich schrittweise | Array muss sortiert sein |

### Lernziele

- ✅ Funktionsweise von Sortieralgorithmen verstehen
- ✅ Selection Sort und Bubble Sort implementieren
- ✅ Lineare Suche korrekt anwenden
- ✅ Binäre Suche verstehen (schneller bei großen Mengen)
- ✅ Algorithmen-Komplexität abschätzen
- ✅ Geeigneten Algorithmus für Problemstellung wählen

---

## BPE 7.3: Dynamische Datenstrukturen

**Lernziel:** Die Schülerinnen und Schüler beschreiben und modellieren die dynamischen Datenstrukturen verkettete Liste, Stapelspeicher, Warteschlange und Baum sowie deren zentrale Bestandteile.

### Listen (Verkettete Listen)

| Konzept | Beschreibung |
|---------|------------|
| **Eigenschaften** | Anker, Knoten, Daten, Zeiger |
| **Operationen** | Einfügen, Löschen |

### Stapelspeicher (Stack)

| Konzept | Beschreibung |
|---------|------------|
| **Prinzip** | LIFO (Last-In-First-Out) |
| **Operationen** | push, pop |
| **Beispiele** | Undo-Funktion, Funktionsaufrufe |

### Warteschlange (Queue)

| Konzept | Beschreibung |
|---------|------------|
| **Prinzip** | FIFO (First-In-First-Out) |
| **Operationen** | enqueue, dequeue |
| **Beispiele** | Druckerwarteschlange, Ticketsystem |

### Bäume

| Konzept | Beschreibung |
|---------|------------|
| **Aufbau von Bäumen** | – Geordnet |
| | – Voll |
| | – Vollständig |
| **Modellierung** | Stammbaum, Organigramm (z. B.) |
| **Binärbäume** | Eigenschaften eines Binärbaums (z. B.) |

### Lernziele

- ✅ Unterschiede zwischen statischen und dynamischen Datenstrukturen verstehen
- ✅ Verkettete Listen implementieren und nutzen
- ✅ Stack und Queue in praktischen Szenarien anwenden
- ✅ Baumstrukturen modellieren und implementieren
- ✅ Vor- und Nachteile der verschiedenen Datenstrukturen kennen
- ✅ Geeignete Datenstruktur für Problem auswählen

---

## Hinweise zur Unterrichtsgestaltung

### Praktische Umsetzung

- **Array-Implementierung:** In einer tatsächlichen Programmiersprache (z. B. Python, Java, C++)
- **Algorithmus-Visualisierung:** Visuell darstellen (z. B. mit Animationen)
- **Schreibtischtests:** Von Hand durchspielen zur Verständnis-Überprüfung
- **Komplexitätsanalyse:** O-Notation einführen und anwenden

### Didaktisches Vorgehen

1. **Arrays verstehen** (BPE 7.1)
   - Variablen → Arrays (Erweiterung)
   - Index-Konzept gut erklären
   
2. **Suchalgorithmen** (BPE 7.2)
   - In dieser Reihenfolge:
     1. Lineare Suche (intuitiv)
     2. Selection Sort (verstehen vor Bubble Sort)
     3. Bubble Sort (ähnlich wie Selection, aber andere Strategie)
     4. Binäre Suche (erst nach verstanden, dass Sortieren wichtig ist)

3. **Dynamische Strukturen** (BPE 7.3)
   - Vereinfached: Mit Visualisierungen starten
   - Dann: Modellierung mit Konzept-Skizzen
   - Am Ende: Evtl. nur konzeptionelle Beschreibung (nicht Implementierung aller)

### Zeitbudget pro Thema

- **Arrays (7.1):** ~6 Stunden (Verständnis + kleine Projekte)
- **Such-/Sortieren (7.2):** ~14 Stunden (Implementierung aller vier Algorithmen)
- **Dynamische Strukturen (7.3):** ~10 Stunden (Konzepte + Modellierung)

---

## Beziehung zu anderen BPEs

- **BPE 5:** Kontrollstrukturen sind essentiell für Such-/Sortieralgorithmen
- **BPE 8:** Graphen bauen auf Baum-Konzepten auf
- **Unterrichtspraxis:** Arrays/Sortieren gehören zu den häufigsten Aufgaben im Informatik-Unterricht

---

## Zusammenfassung der zu erwerbenden Kompetenzen

| Kompetenz | Niveau |
|-----------|--------|
| Array-Handling | Implementierung |
| Sortieren (Selection/Bubble) | Implementierung |
| Suchen (Linear/Binär) | Implementierung |
| Listen/Stack/Queue | Konzeptuelles Verständnis |
| Bäume | Modellierung + Konzepte |

---

*Quelle: Lehrplan Informatik – Berufliches Gymnasium Baden-Württemberg (Abitur 2021)*  
*Stand: 12.04.2019*
