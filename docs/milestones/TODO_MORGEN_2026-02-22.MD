# Reminder: ToDo-Liste für morgen (2026-02-22)

## Priorität 1 (Start)

- [x] Kurzen Morning-Check machen: `git pull --ff-only` auf `main`
- [x] Schnelltest laufen lassen: `python3 apps/tools/check_markdown_links.py --include-templates`
- [x] Doku-DoD prüfen: `python3 apps/tools/check_docs_dod.py`

## Priorität 2 (Qualität)

- [ ] Optionaler Container-Testlauf: `docker compose --profile test run --rm api-tests` (derzeit blockiert: Docker in dieser Dev-Umgebung nicht installiert)
- [ ] Optionaler Frontend-Testlauf: `docker compose --profile test run --rm web-tests` (derzeit blockiert: Docker in dieser Dev-Umgebung nicht installiert)
- [x] Ergebnisse in `CHANGELOG.md` unter `Unreleased` ergänzen (falls neue Erkenntnisse)

## Priorität 3 (Planung)

- [x] Nächsten fachlichen Arbeitsblock festlegen (z. B. direkte Aufgabenintegration)
- [x] Kleine Umsetzungs-Checkliste für den Tag erstellen (3-5 Punkte)
- [x] Bei neuen Doku-/Code-Änderungen: mini-PR statt Direktänderung auf `main`

### Festgelegter Arbeitsblock

- Thema: Direkte Aufgabenintegration L2 (Aufgabe + Loesung + Struktogramm konsistent)
- Ziel: Eine L2-Aufgabe vollstaendig nach BW-Standard durchziehen und testbar dokumentieren

### Tages-Checkliste (5 Punkte)

- [x] Konkrete L2-Aufgabe ausgewaehlt: `L2_3_1_1` (Lineare Suche Mitgliedsnummer, Basis: `struktogramme/L2_3_1_1_Struktogramm_Lineare_Suche_Mitgliedsnummer.stgr`)
- [x] Struktogramm auf BW-Operatoren und Reihenfolge geprueft (Soll-Sequenz fuer `L2_3_1_1`: Deklaration/Initialisierung -> Wiederhole/Zaehle -> Wenn -> Zuweisung -> Rueckgabe; Operatorenfokus laut Meilenstein: Wiederhole, Wenn, Zuweisung, Rueckgabe)
- [x] Python-Loesung mit Type Hints und kurzer Komplexitaetsangabe abgeglichen (`docs/loesungen/L2/L2_3_1_Lineare_Suche_Mitgliedsnummer.md`)
- [x] Doku-Checks laufen gelassen (`check_markdown_links.py`, `check_docs_dod.py`)
- Aenderungen als mini-PR auf Feature-Branch einreichen

## Definition of Done für morgen

- [x] Tests/Checks ohne kritische Fehler (im aktuellen Baseline-Rahmen)
- [x] Offene Änderungen committed und auf `origin` gepusht
- [x] Changelog/Handbuch bei Bedarf synchronisiert
