# Meilenstein M0 – Architektur-Governance & Automatisierung

Stand: 2026-02-21
Status: Geplant (Start-Meilenstein für strukturierte Umsetzung)

## Ziel

Vor der fachlichen Ausbauphase wird eine verbindliche technische Basis geschaffen, damit das Prüfungsmodul von Beginn an:

- klar strukturiert,
- sicher,
- auditierbar,
- ohne Redundanzen,
- und hoch automatisierbar betrieben werden kann.

## Scope

Dieser Meilenstein umfasst **nicht** die vollständige Feature-Umsetzung, sondern die Leitplanken und Betriebsgrundlagen für alle Folge-Meilensteine.

## Deliverables

1. **Verbindliche Zielstruktur (Backend/Frontend)**
   - Modulgrenzen und Verantwortlichkeiten festgelegt
   - API-, Service- und Repository-Trennung standardisiert
   - Frontend-Feature-Slice-Struktur als Standard etabliert

2. **API- und Qualitäts-Governance**
   - API-Prefix `api/v1` als Standard
   - Einheitliches Fehlerformat + Tracing-Konzept
   - OpenAPI als Vertragsquelle verbindlich

3. **Security- und Audit-Basis**
   - Rollenmodell (Autor, Review, Freigabe, Admin)
   - Audit-Log-Strategie für kritische Inhaltsänderungen
   - Mindestanforderungen für Auth, Input-Validation, Secrets

4. **Automatisierung administrativer Prozesse**
   - CI-Gates für Linting, Tests, Security-Checks
   - Pflichtprüfung der Dokumentations-Vollständigkeit
   - Export-Regressionstest auf Referenzprüfung
   - Standardisierter Freigabeworkflow (`draft -> review -> freigegeben`)

5. **Dokumentationsstandard verbindlich umgesetzt**
   - Architekturleitbild aktualisiert
   - Backup/Recovery/Security-Strategie aktualisiert
   - Technische Umsetzungsvorlage als operative Referenz ergänzt

## Abnahmekriterien

M0 gilt als erfolgreich, wenn:

1. Die Zielstruktur in den zentralen Dokumenten eindeutig beschrieben ist.
2. Für neue Features eine überprüfbare Definition of Done existiert.
3. Security-, Audit- und Backup-Vorgaben im Prozess verankert sind.
4. Mindestens ein durchgängiger Referenzworkflow dokumentiert ist:
   - Prüfung anlegen -> Aufgabe bearbeiten/tauschen -> Lösung generieren -> Export starten.

## Risiken und Gegenmaßnahmen

- **Risiko:** Zu viele Sonderwege trotz Leitplanken.
  - **Maßnahme:** PR-Checkliste + verpflichtende Architektur-/Doku-Checks.

- **Risiko:** Sicherheit wird bei MVP-Tempo umgangen.
  - **Maßnahme:** Security-Gates in CI blockierend schalten.

- **Risiko:** Reibungsverlust durch unklare Zuständigkeiten.
  - **Maßnahme:** Klare Ownership pro Modul und pro Prozessschritt.

## Verweise

- [Technische Umsetzungsvorlage](../handbuch/TECHNISCHE_UMSETZUNGSVORLAGE_PRUEFUNGEN.MD)
- [Architekturleitbild](../handbuch/ARCHITECTURE.MD)
- [Backup-, Recovery- und Security-Strategie](../handbuch/BACKUP_STRATEGY.md)
- [Marschplan Prüfungsmodul](MEILENSTEIN-PLAN-PRUEFUNGEN-APP.MD)
