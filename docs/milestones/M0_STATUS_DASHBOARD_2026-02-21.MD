# M0 Status-Dashboard (Architektur-Governance)

Stand: 2026-02-21
Status: In Umsetzung

## Zielbild M0

Das Repository soll von Beginn an:

- lauffähig,
- testbar,
- transparent dokumentiert,
- und funktionsorientiert erweiterbar (Core + Plugins)

sein.

---

## Fortschritt (aktuell)

### ✅ Erreicht

1. API-v1 als Standard für neue Produktfunktionen
   - Prüfungsmodul-Endpunkte vorhanden
   - Plugin-Registry-Endpunkte vorhanden

2. Einheitliches Fehlerformat + TraceId
   - Fehlerobjekt: `code`, `message`, `details`, `traceId`
   - Globale Handler aktiv

3. RBAC + Audit-Basis
   - Rollen über Header (`X-Role`, `X-User-Id`)
   - Audit-Log (`audit_log_v1.jsonl`) aktiv

4. Plugin-Architektur produktiv gestartet
   - Plugin-Katalog (`plugins_v1.json`)
   - Plugin-Activation-Policy (Admin)
   - Plugin-Status im Frontend sichtbar

5. Test-/Build-Basis
   - Backend-Unittest-Suite aktiv
   - Frontend-Test + Build aktiv
   - CI-Workflow `app-quality.yml` für API/Web aktiv

### 🟡 Teilweise erreicht

1. CI-Gates vollständig
   - Vorhanden: Backend-Tests, Frontend-Tests, Frontend-Build
   - Offen: Security-Scans, OpenAPI-Drift-Check, Doku-DoD als Gate

2. Frontend-Architekturziel
   - Vorhanden: Plugin-Sichtbarkeit + Basiskomponenten
   - Offen: vollständige Feature-Slice-Umstellung + zentraler API-Client

### 🔴 Offen (nächste Priorität)

1. Security-Härtung
   - OIDC/JWT-Integration statt Header-Only-Rollen
   - feinere Autorisierungsregeln

2. Governance-Automation
   - Security-Scan-Workflow
   - Doku-Konsistenz-/DoD-Checks als CI-Blocker

3. Export-/Prozess-Härtung
   - Job-Queue für Export/Lösungsjobs
   - Snapshot-Workflow bei `freigegeben`

---

## Risiken (aktiv)

1. Header-basierte Rollensteuerung ist nur Übergangslösung.
2. Fehlende Security-Gates in CI können Quality-Drift zulassen.
3. Doku kann bei hohem Tempo auseinanderlaufen, wenn kein Doku-Gate aktiv ist.

---

## Nächster sinnvoller Implementierungsblock

1. CI erweitern: Security-Scan + Doku-DoD-Check
2. Frontend: zentraler API-Client einführen
3. Backend: Auth-Schicht vorbereiten (JWT/OIDC-fähig)

---

## Verweise

- [Meilenstein M0](MEILENSTEIN-M0-ARCHITEKTUR-GOVERNANCE-AUTOMATISIERUNG.MD)
- [Architektur-Audit](../handbuch/ARCHITEKTUR_AUDIT_REPO_2026-02-21.MD)
- [Technische Umsetzungsvorlage](../handbuch/TECHNISCHE_UMSETZUNGSVORLAGE_PRUEFUNGEN.MD)
- [Zeitplan Core + Plugins](ZEITPLAN-FUNKTIONSORIENTIERTER-PROTOTYP-PLUGINS.MD)
