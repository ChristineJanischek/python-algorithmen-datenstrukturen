# Meilenstein 1 – Aufgabenpaket: Listen, Sortier- und Suchalgorithmen

## Ziel
Schüler trainieren das Lesen von Struktogrammen und setzen diese in lauffähigen Quellcode um. Fokus: Listen/Arrays, Sortieren, Suchen. Es werden **nur** die Notationsmöglichkeiten aus der Operatorenliste genutzt; alle weiteren Funktionen müssen selbst programmiert und in einem Struktogramm mit verfügbarer Notation dargestellt werden.

## Rahmenbedingungen (verbindlich)
- Operatorenliste als Hilfestellung: [struktogramme/Operatorenliste-Struktogramme.md](struktogramme/Operatorenliste-Struktogramme.md)
- Es sind nur Operatoren aus der Operatorenliste zulässig.
- Keine eingebauten Sortier-/Suchfunktionen.
- Keine fremden Hilfsfunktionen, außer sie sind im Struktogramm ausdrücklich definiert.
- Alle Aufgaben sind so gestaltet, dass sie direkt mit Struktogrammen aus dem Verzeichnis struktogramme umgesetzt werden können.

## Einstieg (Struktogramm → Code)
Die folgenden Aufgaben basieren auf existierenden Struktogrammen, um das Lesen zu trainieren:

1. **Lineare Suche (Mitgliedsnummer)**
   - Struktogramm: L2_3_1_1_Struktogramm_Lineare_Suche_Mitgliedsnummer.stgr
   - Ziel: Index oder „nicht gefunden“ zurückgeben.
   - Operatorenfokus: Wiederhole, Wenn, Zuweisung, Rückgabe.

2. **Binäre Suche (Losnummer)**
   - Struktogramm: L2_3_2_1_Struktogramm_Binaere_Suche_Losnummer.stgr
   - Ziel: Elementposition ermitteln oder „nicht gefunden“.
   - Operatorenfokus: Wiederhole, Wenn, Zuweisung, Berechnungen.

3. **Bubble Sort (Zahlenreihe)**
   - Struktogramm: L2_2_1_2_Struktogramm_Bubble_Sort_Zahlenreihe.stgr
   - Ziel: Aufsteigend sortieren.
   - Operatorenfokus: Verschachtelte Schleifen, Vertauschung.

4. **Selection Sort (absteigend)**
   - Struktogramm: L2_2_2_3_Struktogramm_Selection_Sort_absteigend.stgr
   - Ziel: Absteigend sortieren.
   - Operatorenfokus: Minimum/Maximum bestimmen, Zuweisungen.

5. **Listelemente einfügen und entfernen**
   - Struktogramme:
     - L2_3_5_1_Struktogramm_Volleyball_Spieler_einfuegen.stgr
     - L2_3_6_Struktogramm_Volleyball_Spieler_entfernen.stgr
   - Ziel: Einfügen an Position, Entfernen an Position.
   - Operatorenfokus: Indizes, Zuweisungen, Schleifen.

## Vertiefung (übertragen & testen)
6. **Sortierung einer Gewinnziehung**
   - Struktogramm: L2_2_3_1 Struktogramm_Sortierung_Gewinnziehung.stgr
   - Ziel: Zahlenreihe sortieren und anzeigen.

7. **Volleyball-Spieler suchen**
   - Struktogramm: L2_3_1_3_Struktogramm_Volleyball_Spieler_suchen.stgr
   - Ziel: Suche nach Name/Position mit passender Rückgabe.

## Lernerfolgskontrolle (minimal)
- Jeder Quellcode muss das Struktogramm 1:1 abbilden.
- Jede Aufgabe hat mindestens 3 Testfälle:
  - Normalfall
  - Randfall (leere Liste, nicht gefunden)
  - Sonderfall (Duplikate)

## Abgabeformat
- Quellcode pro Aufgabe
- Kurzprotokoll (2–5 Sätze): Welche Operatoren wurden eingesetzt? Welche Stelle war kritisch?
