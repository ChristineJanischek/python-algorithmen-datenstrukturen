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

## 📋 Was ist dieses Projekt?

Dies ist eine **Draw.io Extension** für Struktogramme nach dem Baden-Württemberg Abitur-Standard.

**Zielgruppe:** Schüler & Lehrer im deutschen Abitur (Informatik)

**Features:**
- ✅ 4 Strukturformen (Anweisung, Alternative, While, For)
- ✅ 7 verschiedene Anweisungstypen
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

- **[Installation Guide](./docs/installation.md)** - Detaillierte Setup-Anleitung
- **[Architecture](./docs/architecture.md)** - Technische Architektur
- **[Developer Guide](./docs/dev-guide.md)** - Wie trägt man Code bei?
- **[API Reference](./docs/api-reference.md)** - Alle Functionen & Hooks

---

## 🎯 Roadmap (Phase 1-4)

### ✅ Phase 1: Vorbereitung (Diese Woche)
- Directory Structure
- package.json
- Setup Dokumentation

### 🔄 Phase 2: Stencils & Plugin (Nächste Woche)
- Stencil XML Definition
- Draw.io Palette Integration
- Basic Plugin Loader

### 🔄 Phase 3: Konvertierung (Woche 3)
- XML → Draw.io Format Converter
- SVG Export
- API Integration

### 🔄 Phase 4: Dokumentation & Tests (Woche 4)
- Komplette Developer Docs
- Schüler-Tutorials
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
