# Dependencies & Version Constraints

Dieses Dokument dokumentiert alle Abhängigkeiten und deren Versionsanforderungen.

---

## 🔧 Produktions-Dependencies

### Build & Runtime

| Paket | Version | Zweck | Status |
|-------|---------|-------|--------|
| **mxgraph** | ^4.2.2 | Draw.io Vector Graphics Engine | ✅ kritisch |
| **fast-xml-parser** | ^4.4.0 | High-performance XML Parser | ✅ kritisch |
| **lodash** | ^4.17.21 | JavaScript Utility Library | ✅ wichtig |

**Installation:**
```bash
npm install mxgraph fast-xml-parser lodash
```

---

## 🧪 Entwicklungs-Dependencies

### Testing Framework

| Paket | Version | Zweck |
|-------|---------|-------|
| **jest** | ^29.7.0 | Unit Testing Framework |
| **@testing-library/jest-dom** | ^6.1.5 | Jest DOM Matchers |
| **babel-jest** | ^29.7.0 | Jest with Babel Support |

### Build Tools

| Paket | Version | Zweck |
|-------|---------|-------|
| **webpack** | ^5.90.0 | Module Bundler |
| **webpack-cli** | ^5.1.4 | CLI für Webpack |
| **webpack-dev-server** | ^4.15.2 | Development Server |
| **babel-core** | ^7.24.0 | JavaScript Compiler |
| **@babel/preset-env** | ^7.24.0 | Babel Preset für modern JS |

### Code Quality

| Paket | Version | Zweck |
|-------|---------|-------|
| **eslint** | ^8.56.0 | JavaScript Linter |
| **prettier** | ^3.1.1 | Code Formatter |

---

## 🤖 Automatische Updates

Diese Dependencies werden mit `npm update` aktualisiert:

```bash
# Patch updates (1.2.3 → 1.2.4)
npm update

# Minor updates (1.2.3 → 1.3.0)
npm update --minor

# Major updates (1.2.3 → 2.0.0) - VORSICHT!
npm update --major
```

---

## ✅ Kompatibilität

### Node.js & npm

```
Node.js:  ≥18.0.0  (LTS, stabil)
npm:      ≥9.0.0   (mit Workspace support)
```

Überprüfung:
```bash
node --version   # v18.x.x
npm --version    # 9.x.x
```

### Browser Kompatibilität

Durch Babel wird modernes JavaScript (ES2020) zu ES5 transpiliert.

**Unterstützte Browser:**
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

---

## 🔒 Security Updates

Regelmäßig überprüfen:

```bash
# Zeige veraltete Pakete
npm outdated

# Überprüfe auf Sicherheitslücken
npm audit

# Behebe automatisch
npm audit fix
```

---

## 📦 Abhängigkeits-Graph

```
@struktogramm/drawio-extension
├── mxgraph (Kernel Graphics)
├── fast-xml-parser (Data Format)
├── lodash (Utilities)
└── [devDependencies nur für build time]
    ├── webpack → kompiliert alles zu plugin.js
    ├── babel → transpiliert JS
    └── jest → testet Code
```

---

## 💾 Lock File

Wichtig: **package-lock.json** in Git committen!

Dies stellt sicher, dass alle Team-Member die gleichen Versionen erhalten.

```bash
git add package-lock.json
git commit -m "chore: lock dependencies"
```

---

## 🎯 Nächste Schritte

1. npm install durchführen
2. package-lock.json commiten
3. Mit Phase 2 (Stencils) beginnen

Siehe: [Milestone Plan](../../../docs/milestones/OPTION3_DRAWIO_EXTENSION.md)

<!-- CUSTOM_LICENSE_NOTICE_START -->
## License

This repository is licensed under a custom license.

- Attribution required: Christine Janischek - https://emotionalspirit.de
- Non-commercial use only
- Use only within state school systems
- Any other use requires explicit prior written permission
<!-- CUSTOM_LICENSE_NOTICE_END -->
