---
titel: "Lineare Suche Mitgliedsnummer"
level: L2
kategorie: 3
nummer: 1
autor: "Christine Janischek"
datum: 05.03.2026
version: 1.0
themen:
  - Suchen
  - Listen
  - Lineare Suche
lernziele:
  - Lineare Suche in einer Liste umsetzen
  - Rückgabewert -1 für 'nicht gefunden' korrekt verwenden
  - Zeitkomplexität O(n) begründen
zeitaufwand: "15 Minuten"
schwierigkeitsgrad: "Fortgeschritten"
---

# Lösung: Lineare Suche Mitgliedsnummer

## 📋 Übersicht

- **Level:** L2
- **Kategorie:** 3
- **Komplexität:** Zeit: O(n), Speicher: O(1)

## 💡 Lösungsansatz

Die Liste wird von links nach rechts durchlaufen. Sobald die gesuchte Mitgliedsnummer gefunden wird, wird ihr Index zurückgegeben. Falls kein Treffer vorliegt, liefert die Funktion -1.

## 📊 Struktogramm

```
Deklaration und Initialisierung: gefunden_index als Ganzzahl = -1
Deklaration und Initialisierung: n = Anzahl der Elemente des Arrays mitgliedsnummern
Zähle i von 0 bis n - 1, Schrittweite 1
    Wenn mitgliedsnummern[i] == gesucht, dann
        J
            Zuweisung: gefunden_index = i
        , sonst
        N
            (nichts)
Rückgabe: gefunden_index
```

## 💻 Python-Implementierung

```python
def lineare_suche_mitgliedsnummer(mitgliedsnummern: list[int], gesucht: int) -> int:
    """Sucht eine Mitgliedsnummer linear und gibt den Index oder -1 zurück."""
    for index, nummer in enumerate(mitgliedsnummern):
        if nummer == gesucht:
            return index
    return -1


if __name__ == "__main__":
    daten = [1012, 1034, 1105, 1200]
    print(lineare_suche_mitgliedsnummer(daten, 1105))  # 2
    print(lineare_suche_mitgliedsnummer(daten, 9999))  # -1

```

## 📝 Erklärung

Die lineare Suche prüft jedes Element höchstens einmal. Im besten Fall wird das Ziel direkt am Anfang gefunden, im schlechtesten Fall erst am Ende oder gar nicht.

## ⏱️ Komplexitätsanalyse

Zeit: O(n), Speicher: O(1)

## 💡 Zusätzliche Hinweise

Für unsortierte Listen ist lineare Suche die direkte Standardmethode. Bei sortierten Listen kann alternativ die binäre Suche effizienter sein.

---

*Erstellt am 05.03.2026 von Christine Janischek*
