# 🎨 Draw.io Struktogramm Extension - README

**Struktuqgramme nach Baden-Württemberg Standard direkt in Draw.io zeichnen!**

## 🚀 Quick Start

### Installation

```bash
# 1. Clone Repository
git clone https://github.com/ChristineJanischek/python-algorithmen-datenstrukturen.git
cd python-algorithmen-datenstrukturen/apps/drawio-extension

# 2. Dependencies installieren
npm install

# 3. Development Server starten
npm run dev
```

### Erste Zeichnung

1. Öffne Draw.io (https://draw.io)
2. Lade die Struktogramm-Extension
3. Öffne die Palette "Struktogramme (BW)"
4. Ziehe Shapes in dein Diagramm

---

## 🧪 Testing (Phase 2-A)

**Neu!** Du kannst die BW-Library jetzt in Draw.io testen - **OHNE npm install**!

📖 **[→ Zum Testing Guide (TESTING_GUIDE.md)](./TESTING_GUIDE.md)**
⚡ **[→ Smoke-Test in 2 Minuten](./TESTING_GUIDE.md#-smoke-test-2-minuten)**

**Was du testen kannst:**
- ✅ 18 BW-Operator-Templates in Draw.io laden (via URL oder lokale Datei)
- ✅ Drag & Drop auf Canvas
- ✅ Text editieren
- ✅ BW-Formen überprüfen (Alternative-Dreieck, umgedrehtes L, Aufruf-Seitenstriche)
- ✅ Export als PNG/SVG

**Warum jetzt testen?**
- Validiert Phase 2-A (Stencil-System)
- Gibt Feedback vor Phase 2-B (Plugin-Code)
- Best Practice: Test early, test often!

**Quick Test:** Öffne [Draw.io](https://app.diagrams.net) → File → Open Library from → URL → Gib ein:
```
https://raw.githubusercontent.com/ChristineJanischek/python-algorithmen-datenstrukturen/main/apps/drawio-extension/library.xml
```

---

## 📋 Was ist dieses Projekt?

Dies ist eine **Draw.io Extension** für Struktogramme nach dem Baden-Württemberg Abitur-Standard.

**Zielgruppe:** Schüler & Lehrer im deutschen Abitur (Informatik)

**Features:**
- ✅ BW-konforme Strukturformen (Anweisung, Alternative, While, For, Aufruf)
- ✅ Operator-Templates gemäß `Operatorenliste-Struktogramme.md`
- ✅ Validierung gegen BW-Standard
- ✅ Export zu XML/SVG
- ✅ Automatic Code Generation (bald)

---

## 🔧 Entwicklung

### Projektstruktur

```
src/
├── renderer/      → SVG & mxGraph Rendering Logic
├── validator/     → XML Validation nach BW-Standard
├── converter/     → Format Conversions (XML ↔ Draw.io)
└── integration/   → Draw.io Plugin Hooks
```

### Build Prozess

```bash
# Development
npm run dev      # Startet Webpack Dev Server

# Production Build
npm run build    # Minimiert & optimiert für Production

# Testing
npm test         # Lädt Jest Tests
npm test:watch   # Watch-Mode für TDD
```

---

## 📚 Dokumentation

### Setup & Installation
- **[Installation Guide](./docs/installation.md)** - Detaillierte Setup-Anleitung
- **[Architecture](./docs/architecture.md)** - Technische Architektur
- **[Dependencies](./DEPENDENCIES.md)** - Alle NPM-Pakete & Version Constraints

### Development & Testing
- **[Testing Guide](./TESTING_GUIDE.md)** - 🆕 BW-Library in Draw.io testen (Phase 2-A)
- **[Stencil Guide](./STENCIL_GUIDE.md)** - Technische Doku zu Shapes & SVG
- **[Developer Guide](./docs/dev-guide.md)** - Wie trägt man Code bei? (coming soon)

### Security & Progress
- **[Security Notes](./SECURITY_NOTES.md)** - Known Vulnerabilities & Mitigation
- **[Phase 1 Progress](./PHASE_1_PROGRESS.md)** - Setup-Phase Dokumentation

---

## 🎯 Roadmap (Phase 1-4)

### ✅ Phase 1: Vorbereitung (COMPLETE)
- ✅ Directory Structure
- ✅ package.json mit allen Dependencies
- ✅ Setup Dokumentation (Installation, Architecture)
- ✅ Security Assessment (Option B: Monitor & Document)

### 🔄 Phase 2: Stencils & Plugin (IN PROGRESS)
- ✅ **Phase 2-A:** BW-Library + Stencil-Basis (Operatoren v2.2) - TESTABLE!
- 🔄 **Phase 2-B:** Plugin Loader Implementation
- 🔄 **Phase 2-C:** Draw.io Palette Integration
- 🔄 **Phase 2-D:** Shape Renderer & Event Handlers
- 🔄 **Phase 2-E:** Complete Testing & Documentation

### 🔜 Phase 3: Konvertierung (Woche 3)
- XML → Draw.io Format Converter
- SVG Export via API
- Backend Integration (FastAPI endpoints)

### 🔜 Phase 4: Dokumentation & UX (Woche 4)
- Komplette Developer Docs
- Schüler-Tutorials mit Screenshots
- Beispiele & Use Cases

---

## 🤝 Contributing

Beiträge sind willkommen! Siehe [Developer Guide](./docs/dev-guide.md) für Details.

**Wichtigste Regeln:**
1. Alle Struktogramme müssen BW-Standard entsprechen
2. Tests für neue Features schreiben
3. Code mit ESLint linting

---

## 📝 Lizenz

MIT License - Siehe LICENSE-Datei

---

## 👤 Autor

Christine Janischek

---

## 🔗 Links

- **Main Repository:** https://github.com/ChristineJanischek/python-algorithmen-datenstrukturen
- **Milestone Plan:** [OPTION3_DRAWIO_EXTENSION.md](../../docs/milestones/OPTION3_DRAWIO_EXTENSION.md)
- **Operatorenliste:** [Struktogramm Operators](../../struktogramme/Operatorenliste-Struktogramme.md)

<!-- CUSTOM_LICENSE_NOTICE_START -->
## License

This repository is licensed under a custom license.

- Attribution required: Christine Janischek - https://emotionalspirit.de
- Non-commercial use only
- Use only within state school systems
- Any other use requires explicit prior written permission
<!-- CUSTOM_LICENSE_NOTICE_END -->
