# Klausur-Loesung-Sync-Routine

Ziel dieser Routine ist, Aenderungen in Klausur-Aufgabenblaettern systematisch mit den zugehoerigen Musterloesungen zu synchronisieren.

Die Routine basiert auf:
- `apps/tools/check_pruefungen_solution_sync.py`
- den Dateipaaren `Klausur_AuD_Musteraufgaben_VersionX.md` und `Klausur_AuD_Musterloesungen_VersionX.md`

## Zielbild

Nach jeder Aenderung an einer Aufgabe gilt:
1. Aufgabenblatt und Musterloesung bleiben pro Version konsistent.
2. Diagramm-Referenzen (`DOCX-EMBED-SVG`) bleiben zwischen Aufgabe und Loesung synchron.
3. Ueberschrift und Aufgabenstellung koennen bei Bedarf automatisch in die Loesung uebernommen werden.
4. In Analyseaufgaben vom Typ "Algorithmen pruefen" darf der konkrete Algorithmusname in der Aufgabenstellung nicht vorweggenommen werden.
5. Keine Aufgabe darf in mehreren Musteraufgaben-Dokumenten inhaltlich identisch doppelt vorkommen.

## Betriebsmodi

### 1) Standard-Check (CI-kompatibel)

```bash
python apps/tools/check_pruefungen_solution_sync.py
```

Verhalten:
- Prueft alle gefundenen AuD-Versionspaare.
- Blockiert bei fehlenden Aufgaben oder fehlenden Diagramm-Referenzen.
- Bleibt tolerant gegenueber aelteren Loesungsdateien ohne modernen Aufgabenstellungs-Block.
- Blockiert, wenn in Aufgabe-5-Analyseprompts explizite Algorithmusnamen genannt werden (z. B. Bubble Sort, Selection Sort, Binaere Suche).
- Blockiert bei inhaltlich identischen Aufgaben in mehreren Musteraufgaben-Dateien.

Einsatz:
- CI-Gate (`.github/workflows/app-quality.yml`)
- schneller Repo-Gesamtcheck

### 2) Strikter Text-Sync

```bash
python apps/tools/check_pruefungen_solution_sync.py --strict-task-sync --version 3
```

Verhalten:
- Prueft zusaetzlich pro Aufgabe:
  - Ueberschrift in der Musterloesung
  - Block `**Aufgabenstellung (aus Prüfungsblatt):**`
- Meldet Abweichungen explizit als Fehler.

Einsatz:
- redaktioneller Qualitaetscheck vor Merge
- gezielte Endkontrolle nach groesseren Ueberarbeitungen

### 3) Auto-Sync

```bash
python apps/tools/check_pruefungen_solution_sync.py --apply --version 3
```

Verhalten:
- Synchronisiert in der passenden Musterloesung automatisch:
  - Aufgaben-Ueberschrift
  - zitierten Aufgabenstellungstext aus dem Aufgabenblatt
- bricht bei strukturellen Problemen mit Fehlern ab.

Einsatz:
- nach inhaltlichen Aenderungen an Aufgabenformulierung
- zur Redundanzreduktion bei wiederholten manuellen Copy/Paste-Anpassungen

## Empfohlener Redaktionsworkflow

1. Aufgabe im Aufgabenblatt anpassen, z. B. `docs/pruefungen/Klausur_AuD_Musteraufgaben_Version3.md`.
2. Auto-Sync fuer die betroffene Version ausfuehren.
3. Strikten Check fuer die betroffene Version ausfuehren.
4. Gesamtcheck ohne Zusatzflags ausfuehren.
5. Diff pruefen und fachlich didaktisch gegenlesen.

Beispiel:

```bash
python apps/tools/check_pruefungen_solution_sync.py --apply --version 3
python apps/tools/check_pruefungen_solution_sync.py --strict-task-sync --version 3
python apps/tools/check_pruefungen_solution_sync.py
```

## Was automatisch synchronisiert wird

Automatisch:
- Abschnittsueberschrift einer Aufgabe in der Musterloesung
- Aufgabenstellung im Block `**Aufgabenstellung (aus Prüfungsblatt):**`

Nicht automatisch:
- Python-Mustercode
- Erwartungshorizont/Bewertungstexte
- Struktogramm-Inhalt und SVG-Generierung

Diese drei Punkte bleiben bewusst redaktionelle Verantwortung.

## Typische Fehlermeldungen

`Aufgabe X fehlt`:
- Ursache: Aufgabe existiert im Aufgabenblatt, aber nicht in der Musterloesung.
- Massnahme: Abschnitt in der Loesung anlegen oder Nummerierung bereinigen.

`referenziert Diagramm nicht`:
- Ursache: `DOCX-EMBED-SVG` in Aufgabe nicht in der passenden Loesungsaufgabe vorhanden.
- Massnahme: Diagrammreferenz in der Loesung nachtragen oder Aufgabe korrigieren.

`Ueberschrift weicht ab` (strict):
- Ursache: Titel/Format differiert zwischen Aufgabe und Loesung.
- Massnahme: `--apply` ausfuehren oder manuell angleichen.

`Aufgabenstellung ... nicht mehr synchron` (strict):
- Ursache: Aufgabenstellung wurde geaendert, Loesungszitat nicht nachgezogen.
- Massnahme: `--apply --version X` ausfuehren.

`verraet den Algorithmus in der Aufgabenstellung`:
- Ursache: In "Algorithmen pruefen" wird der konkrete Name im Aufgabentext bereits genannt.
- Massnahme: Formulierung auf algorithmusneutrale Beschreibung umstellen (z. B. "Sortieralgorithmus" statt "Selection Sort").

`Doppelte Aufgabe erkannt`:
- Ursache: Eine Aufgabe wurde in mehreren Klausur-Musteraufgaben inhaltlich identisch verwendet.
- Massnahme: Eine Variante didaktisch gleichwertig neu formulieren (z. B. anderes Datenset, anderer Kontext, gleiche Punktelogik/Kompetenz).

## Best Practices

- Immer versionsbezogen arbeiten (`--version X`), wenn nur eine Klausur angepasst wurde.
- Erst `--apply`, dann `--strict-task-sync` ausfuehren.
- Vor dem Commit den Standard-Check ohne Zusatzflags ausfuehren.
- Automatisch synchronisierte Texte didaktisch gegenpruefen.
- Bei Algorithmuswechseln (z. B. Sortieren zu Suchen) Mustercode und Bewertungshinweise bewusst manuell ueberarbeiten.
- In Aufgabe 5 den Algorithmus nie namentlich nennen, damit Teilaufgabe "Vermuteter Zweck" didaktisch valide bleibt.
- Bei Variantenbildung gleiche Kompetenzstufe beibehalten, aber Wortlaut/Kontext der Aufgabe aktiv differenzieren.

## Wartungshinweise

Technischer Einstiegspunkt:
- `apps/tools/check_pruefungen_solution_sync.py`

Automatisierte Absicherung:
- `tests/test_pruefungen_solution_sync.py`

Wenn neue Dokumenttypen aufgenommen werden sollen, sind folgende Stellen anzupassen:
1. Paar-Findung in `find_pairs()`
2. Abschnittsextraktion in `_extract_sections()`
3. ggf. Markerlogik fuer Aufgabenstellungsbloecke in `_find_solution_statement_block()`
