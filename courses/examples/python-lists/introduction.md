# Python-Listen: Einführung

## Was ist eine Liste?

Eine **Liste** in Python ist eine geordnete Sammlung von Werten.
Sie kann Werte unterschiedlicher Typen enthalten und kann jederzeit verändert werden.

```python
# Leere Liste erstellen
zahlen = []

# Liste mit Anfangswerten
namen = ["Anna", "Bernd", "Clara"]
```

## Zugriff auf Elemente

Der **Index** gibt an, an welcher Position sich ein Element befindet.
In Python beginnt der Index immer bei **0**.

```python
namen = ["Anna", "Bernd", "Clara"]
print(namen[0])  # Ausgabe: Anna
print(namen[2])  # Ausgabe: Clara
```

## Wichtige Methoden

| Methode | Beschreibung | Beispiel |
|---------|-------------|---------|
| `append(x)` | Fügt `x` am Ende hinzu | `zahlen.append(5)` |
| `len(liste)` | Gibt die Anzahl der Elemente zurück | `len(zahlen)` |
| `remove(x)` | Entfernt das erste Vorkommen von `x` | `zahlen.remove(3)` |

## Vergleich: PHP und Python

Wer PHP kennt, wird Ähnlichkeiten erkennen:

| PHP | Python |
|-----|--------|
| `$zahlen = [];` | `zahlen = []` |
| `array_push($zahlen, 5)` | `zahlen.append(5)` |
| `count($zahlen)` | `len(zahlen)` |

> **Hinweis:** In Python ist `append()` eine Methode der Liste selbst.
> Sie wird direkt auf die Liste aufgerufen: `meine_liste.append(wert)`.
