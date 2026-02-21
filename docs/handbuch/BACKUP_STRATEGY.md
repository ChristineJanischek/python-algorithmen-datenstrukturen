# Backup-, Recovery- und Security-Strategie

Stand: 2026-02-21

## Ziel

Sicherstellen, dass das System fachlich, technisch und organisatorisch robust bleibt:

- Wiederherstellbarkeit nach Fehlern
- Nachvollziehbarkeit aller Änderungen
- Schutz sensibler Inhalte
- Stabiler Betrieb für Prüfungszyklen

---

## 1) Schutzziele

1. **Verfügbarkeit**: Prüfungen und Lösungen müssen zuverlässig bereitstehen.
2. **Integrität**: Inhalte dürfen nicht unbemerkt verändert werden.
3. **Vertraulichkeit**: Prüfungsinhalte vor Veröffentlichung schützen.
4. **Nachvollziehbarkeit**: Jede Änderung muss auditierbar sein.

---

## 2) Backup-Objekte

Sicherungspflichtig sind mindestens:

- Git-Repository (Code + Dokumentation + Inhalte)
- Artefakte aus Exportpipelines (docx/pdf/html/xml)
- Konfigurationsdateien und Templates
- Betriebsdaten (Logs, Audit-Logs, Job-Historie)
- Secrets/Schlüsselmaterial (in geeigneter Secret-Lösung, nicht im Repo)

---

## 3) RPO/RTO-Ziele

- **RPO (max. Datenverlust):** 24h für reguläre Inhalte, 1h für produktive Betriebsdaten
- **RTO (Wiederanlaufzeit):** 4h für Kernfunktionen, 24h für erweiterte Export-/LMS-Funktionen

Diese Ziele sind Startwerte und werden nach Pilotbetrieb angepasst.

---

## 4) Sicherungsstrategie (Best Practice)

### 4.1 Git-basierte Sicherung

- `main` bleibt stabil und deploybar
- Feature-Branches + PR-Pflicht
- Tags für freigegebene Stände (`vYYYY.MM.DD`)
- Release-Branches pro Meilenstein

### 4.2 Technische Backups

- **Täglich inkrementell** (Inhalte, Konfiguration, Artefakte)
- **Wöchentlich Vollbackup**
- **Monatlich unveränderliches Archiv** (immutable/offsite)
- Backup-Verschlüsselung im Ruhezustand und bei Transfer

### 4.3 3-2-1-Regel

- 3 Kopien
- 2 unterschiedliche Speicherklassen
- 1 Kopie extern/offsite

---

## 5) Recovery-Prozess

1. Incident klassifizieren (Datenverlust, Sicherheitsvorfall, Defekt)
2. Betroffene Komponenten isolieren
3. Letzten konsistenten Stand wiederherstellen
4. Integrität prüfen (Checksummen, Tests, Smoke-Tests)
5. Freigabe dokumentieren und Betrieb wieder aufnehmen

### Pflicht: Restore-Tests

- Monatlicher Test-Restore in isolierter Umgebung
- Quartalsweise Notfallübung mit Zeitmessung gegen RTO

---

## 6) Security-Baseline für den Betrieb

### Zugriff und Identität

- RBAC (mindestens Rollen: Autor, Review, Freigabe, Admin)
- MFA für privilegierte Konten
- Least-Privilege-Prinzip

### Anwendungssicherheit

- OWASP-orientierte Absicherung (Input Validation, XSS/CSRF/Injection-Schutz)
- Rate Limiting für sensible Endpunkte (KI, Export, Login)
- Sicherheitsheader und TLS-only Betrieb

### Supply-Chain-Sicherheit

- Automatisierte Dependency-Scans (Python/Node)
- Regelmäßige Updates + CVE-Bewertung
- Signierte Releases/Artefakte, wo möglich

### Audit und Forensik

- Unveränderliche Audit-Logs für Prüfungsänderungen
- Protokollierung von Freigaben, Exporten, Rechten
- Aufbewahrungsfristen gemäß internen Vorgaben

---

## 7) Dokumentationssicherung (vollständig)

Jede relevante Änderung muss enthalten:

1. Änderungsbeschreibung (was/warum)
2. Betroffene Komponenten
3. Migrations-/Rollback-Hinweis
4. Test- und Abnahmeergebnis
5. Security-Auswirkung

Pflichtorte:

- Changelog
- Milestone-Dokumentation
- Handbuch (Architektur/Betrieb)

---

## 8) Konkreter Standard-Workflow

1. Feature-Branch erstellen
2. Entwicklung + Tests + Doku
3. PR mit Security- und Backup-Auswirkungscheck
4. Merge nach `main` bei grünen Checks
5. Tag setzen und ggf. Release-Branch aktualisieren
6. Backup-Lauf und Artefaktprüfung automatisch ausführen

---

## 9) Minimale Betriebs-Checkliste vor Release

- Alle Tests grün
- Security-Scan ohne kritische Findings
- Export-Regression für Referenzklausuren erfolgreich
- Backup erfolgreich gelaufen
- Restore-Test zuletzt innerhalb 30 Tage nachweisbar
