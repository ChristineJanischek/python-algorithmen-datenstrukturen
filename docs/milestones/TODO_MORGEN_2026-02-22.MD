# Reminder: ToDo-Liste für morgen (2026-02-22)

## Priorität 1 (Start)

- [ ] Kurzen Morning-Check machen: `git pull --ff-only` auf `main`
- [ ] Schnelltest laufen lassen: `python3 apps/tools/check_markdown_links.py --include-templates`
- [ ] Doku-DoD prüfen: `python3 apps/tools/check_docs_dod.py`

## Priorität 2 (Qualität)

- [ ] Optionaler Container-Testlauf: `docker compose --profile test run --rm api-tests`
- [ ] Optionaler Frontend-Testlauf: `docker compose --profile test run --rm web-tests`
- [ ] Ergebnisse in `CHANGELOG.md` unter `Unreleased` ergänzen (falls neue Erkenntnisse)

## Priorität 3 (Planung)

- [ ] Nächsten fachlichen Arbeitsblock festlegen (z. B. direkte Aufgabenintegration)
- [ ] Kleine Umsetzungs-Checkliste für den Tag erstellen (3–5 Punkte)
- [ ] Bei neuen Doku-/Code-Änderungen: mini-PR statt Direktänderung auf `main`

## Definition of Done für morgen

- [ ] Tests/Checks ohne kritische Fehler
- [ ] Offene Änderungen committed und auf `origin` gepusht
- [ ] Changelog/Handbuch bei Bedarf synchronisiert
