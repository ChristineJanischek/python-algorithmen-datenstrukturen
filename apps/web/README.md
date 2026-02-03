# Projektübersicht

Dieses Projekt enthält verschiedene Algorithmen und Datenstrukturen, die in Python implementiert sind. Ziel ist es, Lernenden und Entwicklern einen praktischen Zugang zu grundlegenden Konzepten der Informatik zu bieten.

## Installationsanleitung

Um das Projekt lokal auszuführen, folgen Sie bitte diesen Schritten:

1. Klonen Sie das Repository:
   ```bash
   git clone https://github.com/ChristineJanischek/python-algorithmen-datenstrukturen.git
   ```
2. Navigieren Sie in das Verzeichnis:
   ```bash
   cd python-algorithmen-datenstrukturen
   ```
3. Installieren Sie die erforderlichen Abhängigkeiten:
   ```bash
   pip install -r requirements.txt
   ```

## Verwendung

Um einen bestimmten Algorithmus oder eine Datenstruktur zu verwenden, importieren Sie die entsprechende Datei in Ihr Python-Skript. Hier ein Beispiel:

```python
from algorithms.sorting import bubble_sort

# Liste, die sortiert werden soll
numbers = [64, 34, 25, 12, 22, 11, 90]

# Sortieren der Liste
sorted_numbers = bubble_sort(numbers)
print(sorted_numbers)
```

## Beitrag

Beiträge sind willkommen! Bitte öffnen Sie ein Issue oder einen Pull-Request, um zu den Verbesserungen des Projekts beizutragen.

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert.