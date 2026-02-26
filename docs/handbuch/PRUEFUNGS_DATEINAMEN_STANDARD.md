# Prüfungs-Dateinamen Standard

Stand: 2026-02-25

## Ziel

Prüfungsdateien werden repositoryweit nach einem einheitlichen Schema geführt:

`Klausur_Thema_Musteraufgaben_Version1.md`

bzw.

`Klausur_Thema_Musterloesungen_Version1.md`

## Verbindliches Schema

`Klausur_<Thema>_<Typ>_VersionX.md`

- `Klausur` = statischer Präfix
- `Thema` ∈ `GdP | AuD | RDB | GA`
- `Typ` ∈ `Musteraufgaben | Musterloesungen`
- `VersionX` = `Version1` bis `VersionN`
- Dateiendung immer `.md`

## Implementierte Systemroutine

Zentrale Utility:

- `src/utils/pruefungen_namenskonvention.py`
  - validiert Dateinamen
  - leitet Themen/Typ/Version robust ab
  - normalisiert Dateien konfliktfrei (automatische Versionserhöhung bei Kollision)

CLI für Betrieb und Redaktion:

- `apps/tools/pruefungen_dateinamen_manager.py`

Beispiele:

```bash
# Nur prüfen
python3 apps/tools/pruefungen_dateinamen_manager.py

# Automatisch umbenennen
python3 apps/tools/pruefungen_dateinamen_manager.py --fix
```

## Automatische Qualitätsprüfung

Die Routine ist im bestehenden Markdown-Review integriert:

- `apps/tools/markdown_reviewer.py`
  - meldet nicht-konforme Prüfungsdateien als Fehler

Damit läuft die Prüfung auch im Pre-Push-Workflow, wenn der Reviewer gestartet wird.

## Erweiterbarkeit (Best Practice)

Die Heuristik zur Themenableitung ist zentral gekapselt und kann ohne Redundanz erweitert werden:

- Funktion `_ermittle_thema(...)` in `src/utils/pruefungen_namenskonvention.py`
- neue Themen-/Keyword-Regeln ausschließlich dort ergänzen

## Empfohlener Workflow

1. Neue Prüfungsdatei erstellen
2. `python3 apps/tools/pruefungen_dateinamen_manager.py --fix` ausführen
3. `python3 apps/tools/markdown_reviewer.py` ausführen
4. Danach commit/push
