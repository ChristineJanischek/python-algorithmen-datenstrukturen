# 🏗️ Architecture & Technical Design

## Überblick

Das Draw.io Struktogramm Extension System besteht aus **4 Hauptkomponenten**:

```
┌─────────────────────────────────────────────┐
│           Draw.io Interface                 │
│        (User zeichnet Diagramme)            │
└────────────┬────────────────────────────────┘
             │
             ▼
┌─────────────────────────────────────────────┐
│      Integration Layer (integration/)       │
│  - Plugin Loader                            │
│  - Palette Registration                     │
│  - Event Handlers                           │
└────────────┬────────────────────────────────┘
             │
    ┌────────┴────────┬───────────────┐
    ▼                 ▼               ▼
┌─────────┐    ┌───────────┐    ┌──────────┐
│Renderer │    │ Validator │    │ Converter│
│(SVG Gen)│    │ (Regeln)  │    │(Formate) │
└─────────┘    └───────────┘    └──────────┘
    │              │                  │
    └──────────────┴──────────────────┘
             │
             ▼
┌─────────────────────────────────────────────┐
│         Core Domain Logic                   │
│  - Struktogramm Model                       │
│  - BW-Standard Rules                        │
│  - Shape Definitions                        │
└─────────────────────────────────────────────┘
```

---

## 📁 Verzeichnis-Struktur

### `src/integration/`
**Zweck:** Drew.io Plugin Integration  
**Enthält:**
- `plugin.js` - Haupt-Entry Point
- `palette-loader.js` - Registriert Shapes in Palette
- `event-handlers.js` - Kommunikation mit Draw.io

### `src/renderer/`
**Zweck:** SVG Generation & Visual Rendering  
**Enthält:**
- `svg-generator.js` - Konvertiert Shapes zu SVG
- `shape-factory.js` - Erstellt mxGraph Cells
- `styling.js` - CSS/Styling für Shapes

### `src/validator/`
**Zweck:** Validierung gegen BW-Standard  
**Enthält:**
- `schema-validator.js` - Überprüft Struktur-Konformität
- `operator-validator.js` - Validiert Operatoren-Syntax
- `bw-rules.js` - BW-Standard Regeln als Code

### `src/converter/`
**Zweck:** Format-Konvertierungen  
**Enthält:**
- `xml-to-drawio.js` - `.xml` → Draw.io Format
- `drawio-to-xml.js` - Draw.io Format → `.xml`
- `xml-to-svg.js` - `.xml` → `.svg`

---

## 🔄 Data Flow

### Szenario 1: Benutzerin zeichnet ein Struktogramm

```
1. User zieht Shape in Canvas
   ↓
2. Draw.io feuert "cellAdded" Event
   ↓
3. integration/event-handlers.js fängt das
   ↓
4. renderer/shape-factory.js erzeugt mxCell
   ↓
5. validator/schema-validator.js überprüft
   ↓
6. Fehlerhaft? → Error-Highlighting
   Korrekt? → Shapes wird angezeigt
```

### Szenario 2: Benutzerin exportiert zu XML

```
1. User klickt "Export as XML"
   ↓
2. integration/export-handler.js aufgerufen
   ↓
3. converter/drawio-to-xml.js konvertiert
   ↓
4. validator/schema-validator.js prüft final
   ↓
5. File wird heruntergeladen
```

### Szenario 3: SVG wird generiert

```
1. Struktogramm finalisiert
   ↓
2. converter/xml-to-svg.js wird ausgeführt
   ↓
3. renderer/svg-generator.js zeichnet alle Elemente
   ↓
4. SVG wird hochgeladen / angezeigt
```

---

## 🔌 Key Interfaces & APIs

### Shape Object

```javascript
{
  type: "anweisung" | "alternative" | "while" | "for",
  id: "shape-123",
  label: "variable = wert",
  x: 100,
  y: 200,
  width: 200,
  height: 60,
  children: [Shape], // Verschachtelte Shapes
  style: {
    fill: "#ffffff",
    stroke: "#000000"
  }
}
```

### Validation Result

```javascript
{
  isValid: true | false,
  errors: [
    {
      type: "OPERATOR_INVALID",
      message: "Unbekannter Operator: 'xyz'",
      location: { shapeId: "shape-5" }
    }
  ],
  warnings: [...]
}
```

### Converter Options

```javascript
{
  format: "xml" | "json" | "svg",
  includeMetadata: true,
  validateOnConvert: true,
  beautify: true
}
```

---

## 🧩 Dependencies & Abhängigkeiten

| Paket | Version | Zweck |
|-------|---------|-------|
| `mxgraph` | ^4.2.2 | Draw.io Engine & Shapes |
| `fast-xml-parser` | ^4.4.0 | XML Parsing & Generation |
| `lodash` | ^4.17.21 | Utility Functions |
| `jest` | ^29.7.0 | Unit Testing |
| `webpack` | ^5.90.0 | Bundling & Build |

---

## 🔐 Sicherheitsüberlegungen

1. **XML Parser:** Verwendet `fast-xml-parser` statt `xml2js` (schneller & sicherer)
2. **SVG Output:** Saniert User Input vor SVG Generation
3. **Validation:** Whitelist-Ansatz - nur bekannte Operatoren erlaubt

---

## 📊 Performance-Targets

| Metrik | Target |
|--------|--------|
| Shapes laden | < 100ms |
| Shape rendern | < 50ms |
| XML Validation | < 200ms |
| SVG Export | < 500ms |

---

## 🚀 Erweiterungspunkte (Future)

1. **Custom Validators** - Plugin-System für zusätzliche Regeln
2. **Theme Support** - Verschiedene Farbschemen
3. **Collaboration** - Echtzeitbearbeitung mit anderen
4. **AI Assistant** - Code-Generierung aus Struktogrammen
5. **Mobile Support** - Responsive Design

---

## 📚 Weitere Lektüre

- [Installation Guide](./installation.md)
- [Developer Guide](./dev-guide.md)
- [API Reference](./api-reference.md)
- Main Repo: [OPTION3_DRAWIO_EXTENSION.md](../../../docs/milestones/OPTION3_DRAWIO_EXTENSION.md)

<!-- CUSTOM_LICENSE_NOTICE_START -->
## License

This repository is licensed under a custom license.

- Attribution required: Christine Janischek - https://emotionalspirit.de
- Non-commercial use only
- Use only within state school systems
- Any other use requires explicit prior written permission
<!-- CUSTOM_LICENSE_NOTICE_END -->
