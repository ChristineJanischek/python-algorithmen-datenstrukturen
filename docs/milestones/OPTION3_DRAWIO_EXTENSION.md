# 🎯 Milestone: Option 3 - Multi-Purpose Umstrukturierung

## 📅 Start: 18.02.2026
## 🎯 Ziel: Struktogramm Ecosystem mit Draw.io Integration

---

## 📋 Überblick

Dieses Milestone beschreibt die Umstrukturierung des Repos zur Unterstützung einer integrierten Draw.io Extension. Das Repo wird von reinem "Abitur-Inhalts-Repo" zu **"Struktogramm Ecosystem"** - ein Ort für Inhalte, Tools UND Editor-Integration.

**Entscheidungsdatum:** 17.02.2026  
**Entscheidungsrahmen:** Wahl zwischen 3 Optionen (siehe HEAD/)  
**Grund für Option 3:** Single Source of Truth, bessere DX für Schüler, Wiederverwendbarkeit

---

## 🏗️ Projektstruktur nach Abschluss

```
python-algorithmen-datenstrukturen/
├── struktogramme/              ← ZENTRALE Struktur-Definitions-Schicht
│   ├── *.stgr, *.xml           (Struktur-Definitionen)
│   ├── converter/              (Renderer, Validatoren)
│   ├── generated/              (SVG exports, renders)
│   └── Operatorenliste-Struktogramme.md
│
├── apps/
│   ├── api/                    ← Backend (Python/FastAPI)
│   │   └── routes/
│   │       └── struktogramm.py (Validierung, Konvertierung)
│   │
│   ├── tools/                  ← CLI Tools (Python)
│   │
│   ├── web/                    ← Web-UI (bestehend)
│   │
│   └── drawio-extension/       ← NEU: Draw.io Plugin
│       ├── README.md
│       ├── package.json        (NPM Package Def)
│       ├── plugin.js           (Main Entry)
│       ├── stencil.xml         (Shape Definitions)
│       ├── src/
│       │   ├── renderer/       (SVG Rendering)
│       │   ├── validator/      (XML Validation)
│       │   ├── converter/      (Format Conversions)
│       │   └── integration/    (Draw.io API)
│       ├── examples/           (Beispiel-Struktogramme)
│       ├── tests/              (Jest Tests)
│       └── docs/
│           ├── installation.md
│           ├── architecture.md
│           └── dev-guide.md
│
├── docs/
│   ├── aufgaben/
│   ├── loesungen/
│   ├── integration/            ← NEU: Draw.io Integration
│   │   ├── quickstart.md
│   │   ├── installation.md
│   │   └── user-guide.md
│   ├── tutorials/              ← NEU: Schüler-Tutorials
│   │   └── draw-io-editor.md
│   ├── milestones/
│   │   └── OPTION3_DRAWIO_EXTENSION.md (diese Datei)
│   └── ...
```

---

## 📊 Phasen & Aufgaben

### **Phase 1: Vorbereitung & Repo-Umstrukturierung** (Woche 1)

**Ziel:** Repo vorbereiten, Struktur anlegen, Dependencies festlegen

- [ ] **Repo-Struktur analysieren**
  - Bestand aufnehmen: Abhängigkeiten, Imports, Build-Prozesse
  - Dokumentieren, was wo definiert ist

- [ ] **`apps/drawio-extension/` Verzeichnis anlegen**
  - Directory Tree wie oben erstellen
  - Basis-Verzeichnisse: `src/`, `examples/`, `tests/`, `docs/`

- [ ] **`package.json` erstellen**
  - Definiere: `name`, `version`, `main`, `scripts`
  - Dependencies: mxGraph, draw.io SDK, Validatoren

- [ ] **Setup-Dokumentation schreiben**
  - How-to-Build (npm install, build process)
  - How-to-Install (als Draw.io Plugin)
  - How-to-Develop (local testing)

- [ ] **Dependencies definieren**
  - Node.js Version festlegen
  - NPM Packages auflisten (mxGraph, etc.)
  - Python Dependencies für Konverterer klären

---

### **Phase 2: Stencil & Basis-Plugin** (Woche 2)

**Ziel:** Visuelle Shapes und Plugin-Grundstruktur im Draw.io integrierbar

- [ ] **Shape Stencil Definition erstellen** (`stencil.xml`)
  - Basierend auf: Eure bestehenden XML-Definitionen
  - Format: Draw.io/mxGraph Stencil XML

- [ ] **Alle 4 BW-Standard Formen als Stencils**
  - ✅ Anweisung (Rechteck)
  - ✅ Alternative (Rechteck + Dreieck)
  - ✅ While-Schleife (umgedrehtes L)
  - ✅ For-Schleife (umgedrehtes L variant)

- [ ] **7 Instruction Types als differenzierte Shapes**
  - Deklaration:
  - Deklaration und Initialisierung:
  - Einlesen:
  - Zuweisung:
  - Ausgabe:
  - Rückgabe:
  - Funktionsaufruf

- [ ] **Basis Plugin-Struktur** (`plugin.js`)
  - Draw.io Hook registrieren
  - Palette loader implementieren
  - Shape renderer hook

- [ ] **Draw.io Palette integrieren**
  - Register palette with shapes
  - Gruppierung: Anweisungen, Kontrollstrukturen, Arrays
  - Icons/Thumbnails

---

### **Phase 3: Konvertierung & API Integration** (Woche 3)

**Ziel:** XML ↔ Draw.io Sync, API Endpoints, Export

- [ ] **XML → Draw.io Format Converter**
  - Eure `.xml` Dateien → Draw.io `.drawio` Format
  - Mapping: XML Elements → mxCell Shapes

- [ ] **Draw.io → XML/SVG Export**
  - Zeichnungen als XML speichern (eure Format)
  - SVG automatisch generieren via API

- [ ] **API Integration** (in `apps/api/`)
  - `POST /api/struktogramm/validate` - XML validieren
  - `POST /api/struktogramm/convert` - zu Draw.io Format
  - `GET /api/struktogramm/render/{id}` - SVG rendern
  - `POST /api/struktogramm/export` - Formate konvertieren

- [ ] **SVG Preview in Draw.io Plugin**
  - Live-Preview während Zeichnen
  - Export Button → SVG + XML

- [ ] **Validation via API**
  - Draw.io Plugin linkt zu Backend-Validierung
  - Fehler-Highlighting in Editor

---

### **Phase 4: Dokumentation & Schüler-UX** (Woche 4)

**Ziel:** Alles dokumentiert, Schüler können sofort starten

- [ ] **Developer-Guides schreiben**
  - `docs/drawio-extension/architecture.md` - Wie funktioniert's?
  - `docs/drawio-extension/dev-guide.md` - Wie trägt man Code bei?
  - `docs/drawio-extension/api-reference.md` - Alle API-Endpoints

- [ ] **Schüler-Tutorials**
  - `docs/tutorials/draw-io-editor.md` - "Struktogramme mit Draw.io zeichnen"
  - Step-by-step Anleitung mit Screenshots
  - Häufige Fehler & Lösungen

- [ ] **Beispiele & Use Cases**
  - `apps/drawio-extension/examples/beispiel1.drawio`
  - Typische Strukturen (Summe, Suche, Sort)
  - Export-Beispiele (XML, SVG)

- [ ] **Installation-Instructions**
  - Für Schüler (einfach)
  - Für Entwickler (mit Setup)
  - Troubleshooting FAQ

- [ ] **Integration-Guides**
  - Wie Import/Export in LMS-Systeme?
  - GitHub-Integration?
  - Print-Vorbereitung

---

## 📊 Geschätzter Aufwand

| Phase | Duration | Dev | Docs | Tools |
|-------|----------|-----|------|-------|
| 1: Vorbereitung | 3-4 Tage | 40% | 60% | Setup |
| 2: Stencil & Plugin | 3-5 Tage | 70% | 30% | SVG Gen |
| 3: Konvertierung | 4-5 Tage | 80% | 20% | APIs |
| 4: Docs & UX | 3-5 Tage | 20% | 80% | Guides |
| **TOTAL** | **~4 Wochen** | **60%** | **40%** | |

---

## 🎯 Success Criteria

✅ **Phase 1 erfolgreich, wenn:**
- `apps/drawio-extension/` existiert mit allen Subdirs
- `package.json` vollständig
- Setup Docs sind lauffähig

✅ **Phase 2 erfolgreich, wenn:**
- Stencil im Draw.io loaded
- Alle 4 Formen + 7 Types zeichnebar
- Plugin funktioniert in lokaler Draw.io Instance

✅ **Phase 3 erfolgreich, wenn:**
- Beispiel-XML → Draw.io Format → SVG round-trip funktioniert
- API Endpoints alle testbar
- Export quality ist akzeptabel

✅ **Phase 4 erfolgreich, wenn:**
- Schüler können ohne Support zeichnen
- Alle Tutorials getestet
- Dokumentation ist vollständig (Spellcheck bestanden)

---

## 🔗 Abhängigkeiten

**Muss vorher fertig sein:**
- ✅ Operatorenliste Refinements (bis 17.02.2026)
- ✅ XML/SVG Renderer optimiert
- ✅ GitHub Actions Pipeline läuft

**Parallel möglich:**
- PR #2 (GitHub Actions) → Kann weiterlaufen
- Abitur-Content updates → Unabhängig

---

## 💡 Zusätzliche Opportunitäten

Nach Abschluss könnten folgende Features hinzukommen (nicht in diesem Milestone):

1. **NPM Package Publishing**
   - `@struktogramm/drawio-extension` auf npm publishen
   - Für andere Schulen/Projekte nutzbar

2. **Draw.io Marketplace Integration**
   - Im offizellen Draw.io Plugin Marketplace listen
   - Breitere Adoption

3. **LMS Integration**
   - Moodle Plugin für Struct ogramm-Zeichnungen
   - Canvas/Blackboard Support

4. **Echtzeit-Collaboration**
   - Live-Drawing für Klassen
   - Feedback-Features

5. **AI-Assistent**
   - "Zeichne einen Bubble Sort"
   - Struktur auto-generieren

---

## 📝 Notizen

**Besonderheiten dieses Projekts:**
- Ihre XML/SVG Strukturen sind bereits optimal aufgebaut
- Multi-Stack (Python + Node.js) ist schon etabliert
- API-Infrastruktur existiert bereits teilweise
- Könnten sehr schnell sichtbare Results erreichen

**Wichtigste Insights:**
- Phase 2 wird wahrscheinlich länger (Drawing-API ist knifflig)
- Phase 4 (Docs) ist für Schüler-Adoption kritisch
- Regelmäßiges Testen mit echten Schülern wird empfohlen

---

## 🚀 Ready to Start?

**Nächster Schritt (18.02.2026 Morgen):**
1. Repo-Struktur mit Checklist analysieren
2. `apps/drawio-extension/` anlegen
3. Phase 1 kanban-Board aufmachen
4. Erste `package.json` schreiben

**Kontakt für Fragen:**
- [Architecture Docs](../handbuch/STRUKTOGRAMM_GUIDE.md)
- GitHub Issues für Blocking Items

---

*Status: READY FOR KICKOFF 🚀*  
*Erstellt: 17.02.2026*  
*Letztes Update: 17.02.2026*

<!-- CUSTOM_LICENSE_NOTICE_START -->
## License

This repository is licensed under a custom license.

- Attribution required: Christine Janischek - https://emotionalspirit.de
- Non-commercial use only
- Use only within state school systems
- Any other use requires explicit prior written permission
<!-- CUSTOM_LICENSE_NOTICE_END -->
