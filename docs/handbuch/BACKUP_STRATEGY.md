# Backup Strategy

Stand: 2026-02-06

## Ziel
Sicherstellen, dass im Template-Repository jederzeit auf eine lauffaehige Version zurueckgegriffen werden kann (Backtracking).

## Grundsaetze
- `main` ist immer lauffaehig und enthaelt nur getestete Aenderungen.
- Jede inhaltliche Aenderung wird versioniert (Commit + Tag oder Release-Branch).
- Es gibt eine eindeutige Ruecksprungmoeglichkeit pro Release/Meilenstein.

## Workflow (kurz)
1. Feature-Branch erstellen und lokal testen.
2. PR/Merge nach `main` nur, wenn Tests/Checks erfolgreich sind.
3. Nach Merge einen Tag setzen und optional einen Release-Branch anlegen.

## Backtracking-Mechanismen
- **Tags pro stabiler Version**
  - Beispiel: `v2026.02.06`
  - Zweck: Schneller Ruecksprung auf bekannte stabile Stande.
- **Release-Branch pro Meilenstein**
  - Beispiel: `release/2026-02-elearning`
  - Zweck: Langfristig wartbare Stabilisierungszweige.
- **Hotfix-Regel**
  - Hotfixes werden von `main` abgezweigt, getestet und zurueckgemergt.

## Konkrete Git-Kommandos
```bash
# Tag nach erfolgreichem Merge

git tag -a v2026.02.06 -m "Stable template"

git push origin v2026.02.06

# Release-Branch erstellen

git switch -c release/2026-02-elearning

git push -u origin release/2026-02-elearning
```

## Kriterien fuer "lauffaehig"
- Keine offenen Fehler in der Standard-Ausfuehrung.
- Struktogramm-Helper und E-Learning-Manager lassen sich ausfuehren.
- Index-Generierung funktioniert.

## Ablage
- Zentrale Referenz in diesem Dokument.
- Tags und Release-Branches sind die eigentlichen Backups.
