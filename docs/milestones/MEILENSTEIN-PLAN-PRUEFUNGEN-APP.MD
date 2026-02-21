# Marschplan: Prüfungsmodul „prüfungen“

## 1) Zielbild (Produktvision)

Ein integriertes Prüfungsmodul für BW-konforme Informatik-/Wirtschaftsinformatik-Prüfungen (Sek II), mit:

1. Erstellung und Versionierung kompletter Klausuren
2. Aufgabenverwaltung (tauschen, bearbeiten, KI-gestützt generieren)
3. Konfigurierbaren Parametern (Niveau, Anforderungsbereiche, Verteilungsschlüssel, Themen, Erwartungshorizont)
4. Automatisch erzeugten, getesteten und aktualisierten Lösungsdokumenten (BW-konform)
5. One-Click-Export in `.md`, `.docx`, `.pdf`, `.xml`, `.html`
6. One-Click-Einbettung in ein modernes E-Learning-System (Codeboxen, Validierung, Auswertung)

---

## 2) Präzise Ist-Analyse (Stand Repository)

### 2.1 Bereits vorhanden (wichtig für schnelle Umsetzung)

- **API-Grundlage vorhanden:** `apps/api/app/main.py` mit FastAPI-Endpunkten (`/api/health`, `/api/themes`, `/api/milestones`, `/api/tasks`, `/api/operatorenliste`)
- **BW-konforme Struktogramm-Basis vorhanden:**
  - `src/utils/struktogramm_helper.py`
  - `src/utils/struktogramm_validator.py`
  - `src/utils/struktogramm_notation_validator.py`
- **E-Learning-Content-Management vorhanden:** `src/utils/elearning_manager.py`
- **Draw.io/XML-Ökosystem vorhanden:** `apps/drawio-extension/` inkl. XML/SVG-Konverter- und Validator-Dokumentation
- **Fachliche Inhalte vorhanden:** Aufgaben/Informationen/Lösungen/Prüfungen in `docs/` sowie Struktogrammdateien in `struktogramme/`

### 2.2 Noch nicht vorhanden (Lücken)

- Kein dediziertes **Prüfungsdomain-Modell** (Prüfung, Aufgabe, Erwartungshorizont, Bewertungsschema)
- Kein Editor-Workflow für **Aufgaben tauschen/bearbeiten** im Web-Frontend
- Keine integrierte **KI-Generierungspipeline** für Aufgaben mit Qualitäts-Gate
- Keine durchgängige **Auto-Generierung + Auto-Tests** für Lösungsvorschläge als Produktfunktion
- Kein produktiver One-Click-Export-Stack für `.docx`, `.pdf`, `.html` (XML/SVG-Bausteine sind vorhanden)
- Keine direkte produktive **LMS-Einbettung auf Klick** (z. B. LTI/SCORM/xAPI-Adapter)

### 2.3 Machbarkeit (Kurzfazit)

**Sehr gut machbar**, weil zentrale Basismodule bereits existieren. Kritisch ist nicht „ob“, sondern die saubere Orchestrierung von:

- BW-Konformität (Operatorenliste + Struktogrammregeln)
- KI-Qualitätssicherung (Halluzinations- und Niveaukontrolle)
- Revisionssicherem Dokumenten- und Exportprozess

---

## 3) Zielarchitektur (empfohlen)

## 3.1 Fachmodule

1. **Prüfungs-Builder**
   - Prüfung anlegen
   - Aufgabenpool auswählen
   - Aufgabenreihenfolge, Punkte, Zeit, Anforderungsbereiche konfigurieren

2. **Aufgaben-Engine**
   - CRUD + Austausch von Aufgaben
   - Variantenbildung (A/B-Versionen)
   - KI-Assistenz für Generierung/Umformulierung

3. **Konfigurations-Engine**
   - Niveauprofile (L1/L2/L3, AB I/II/III)
   - Verteilungsschlüssel und Themengewichtung
   - Erwartungshorizont-Template pro Aufgabentyp

4. **Lösungs-Engine (BW-konform)**
   - Automatische Lösungsentwürfe
   - Validierung gegen Operatorenliste/Notation
   - Testläufe (mind. Fachregeln + formale Checks)

5. **Export-Engine**
   - `.md` als Primärformat
   - `.html` aus Markdown
   - `.docx` aus Markdown
   - `.pdf` aus HTML/Docx
   - `.xml` (strukturierte Prüfungsrepräsentation + Struktogrammbezug)

6. **LMS-Connector**
   - One-Click-Paketierung
   - Start mit „Export-kompatibel“ (CSV/JSON/API)
   - Optional später LTI 1.3 / SCORM 2004 / xAPI

### 3.2 Technische Schichten

- **Backend:** FastAPI (`apps/api`) als zentrale Orchestrierung
- **Frontend:** `apps/web` als Authoring- und Prüfungs-UI
- **Validierung:** bestehende BW-Validatoren + neue Prüfungsregeln
- **Datei-/Artefakt-Layer:** versionierte Quellen in `docs/pruefungen/` + `docs/loesungen/` + `struktogramme/`
- **Automation:** CI-Checks für Konsistenz, Exporte, Regressionstests

---

## 4) Chancen und Risiken

### 4.1 Chancen

- Hohe Zeitersparnis in der Prüfungserstellung
- Einheitliche BW-konforme Qualität
- Wiederverwendbarer Aufgabenpool mit Varianten
- Schnellere Iteration durch KI-Unterstützung
- Direkte Anschlussfähigkeit an E-Learning-Szenarien

### 4.2 Risiken

1. **KI-Qualitätsrisiko**
   - Falsche Schwierigkeitszuordnung
   - Fachlich unpräzise Musterlösungen

2. **Compliance-Risiko (BW-Standard)**
   - Abweichungen von Operatorenliste und Erwartungshorizont-Standards

3. **Export-Risiko**
   - Formatdrift zwischen `.md`, `.docx`, `.pdf`

4. **Betriebsrisiko**
   - Zu viele manuelle Sonderfälle bei Versionierung/Updates

### 4.3 Gegenmaßnahmen

- „Human-in-the-loop“-Freigabe für KI-generierte Inhalte
- Pflicht-Validierung vor Veröffentlichung
- Golden-Tests für Exportgleichheit (Inhalt/Struktur)
- Versions- und Freigabeprozess mit Status: `Draft -> Review -> Freigegeben`

---

## 5) Marschplan (Milestones)

## M0 – Scope + Datenmodell (1 Woche)

**Ziel:** Klare Spezifikation als belastbare Basis.

**Ergebnisse:**
- Domänenmodell für `Pruefung`, `Aufgabe`, `Erwartungshorizont`, `Verteilungsschluessel`
- JSON-/Markdown-Schema für Prüfungsartefakte
- Definition der Qualitätskriterien (BW, Niveau, Export, Vollständigkeit)

**Abnahmekriterien:**
- Modell dokumentiert und mit 2 Beispielklausuren getestet

## M1 – Prüfungs-Builder MVP (2 Wochen)

**Ziel:** Klausuren manuell zusammenstellen und speichern.

**Ergebnisse:**
- UI in `apps/web` für Prüfungsanlage
- API-Endpunkte in `apps/api` für CRUD auf Prüfungen
- Aufgaben tauschen/verschieben/bearbeiten

**Abnahmekriterien:**
- Vollständige Klausur kann ohne manuelle Dateiedits erzeugt und erneut geladen werden

## M2 – Konfigurations-Engine (1–2 Wochen)

**Ziel:** Niveau und Bewertungslogik parametrisieren.

**Ergebnisse:**
- Konfigurierbare AB-Verteilung (I/II/III)
- Themen- und Punkteschlüssel
- Erwartungshorizont-Templates

**Abnahmekriterien:**
- Konfiguration beeinflusst Ausgabe und Bewertungsraster nachvollziehbar

## M3 – KI-gestützte Aufgaben-Engine (2 Wochen)

**Ziel:** Aufgaben generieren/überarbeiten lassen.

**Ergebnisse:**
- Prompt-Templates je Aufgabentyp
- Guardrails (Niveau, Thema, Operatoren)
- Review-Workflow mit Diff-Ansicht

**Abnahmekriterien:**
- 80% der generierten Aufgaben bestehen den Qualitätscheck ohne manuelle Grundkorrektur

## M4 – Lösungsautomation BW-konform (2 Wochen)

**Ziel:** Lösungsdokumente automatisch erzeugen + validieren.

**Ergebnisse:**
- Auto-Generierung von Lösungstext + Python-Code + Struktogrammreferenz
- Validierung gegen BW-Regeln
- Regressionstests für bestehende Referenzprüfungen

**Abnahmekriterien:**
- Jede veröffentlichte Prüfung hat automatisch geprüfte Lösungsversion

## M5 – One-Click-Export (1–2 Wochen)

**Ziel:** Export in alle Ziel-Formate auf Knopfdruck.

**Ergebnisse:**
- Export-Pipeline: `.md` -> `.html` / `.docx` / `.pdf`
- XML-Export für strukturierte Weiterverarbeitung
- Download/Batch-Export im UI

**Abnahmekriterien:**
- Identischer Kerninhalt in allen Zielformaten bei Referenzklausur

## M6 – E-Learning-Einbettung (2 Wochen)

**Ziel:** Aufgaben direkt in Lernplattform nutzbar machen.

**Ergebnisse:**
- Adapter „Exportpaket für LMS“
- Code-Box-freundliche Aufgabenstruktur
- Ergebnis-/Validierungsrückgabe (mindestens API-basiert)

**Abnahmekriterien:**
- Referenzaufgabe in Ziel-LMS importiert und automatisch ausgewertet

## M7 – Hardening + Pilotbetrieb (1–2 Wochen)

**Ziel:** Betriebsreife für echten Unterricht.

**Ergebnisse:**
- Rollen/Rechte (Autor, Review, Freigabe)
- Audit-Log und Versionierung
- Dokumentation + Schulungsleitfaden

**Abnahmekriterien:**
- Pilotklasse kann 1 Klausurzyklus vollständig durchlaufen

---

## 6) Empfohlene Prioritäten (wichtig)

1. **Zuerst M0-M2**, damit Struktur und Bewertungslogik stabil sind
2. **Dann M4 vor M3**, wenn BW-Konformität höchste Priorität hat
3. **Export und LMS erst nach stabilen Inhalten**, sonst hohe Nacharbeitskosten

---

## 7) Konkreter Startplan (nächste 10 Arbeitstage)

### Tag 1–2
- Domänenmodell finalisieren
- 2 Referenzklausuren als Goldstandard definieren

### Tag 3–5
- CRUD-API und Basis-UI für Prüfungs-Builder
- Aufgabenreihenfolge + Tauschfunktion implementieren

### Tag 6–7
- AB-/Niveau-Konfiguration integrieren
- Erwartungshorizont-Template anbinden

### Tag 8–10
- Erste Auto-Lösungs-Pipeline mit BW-Validierung
- Snapshot-Tests für 1 Referenzklausur

---

## 8) KPI/Erfolgsmessung

- Erstellzeit pro Klausur (Soll: -40%)
- Anteil BW-konformer Auto-Lösungen (Soll: >= 95% nach Review)
- Export-Fehlerrate je Format (Soll: < 2%)
- Wiederverwendungsrate von Aufgaben (Soll: >= 60%)

---

## 9) Entscheidungsvorlage (kurz)

**Empfehlung:** Umsetzung starten, aber mit strikter Reihenfolge:

1. Datenmodell + Builder + Konfiguration
2. BW-konforme Lösungsautomation
3. KI-Generierung und Export/LMS-Ausbau

So minimierst du Risiko, behältst didaktische Qualität und kommst schnell zu einem nutzbaren MVP.
