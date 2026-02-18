# Installation & Setup Guide

## 📋 Voraussetzungen

- **Node.js:** ≥ 18.0.0
- **npm:** ≥ 9.0.0
- **Git:** Für Repository Cloning
- **Draw.io:** Instalierte Version oder https://draw.io

Überprüfe deine Versionen:
```bash
node --version    # Sollte v18.x oder höher sein
npm --version     # Sollte 9.x oder höher sein
git --version
```

---

## 🚀 Installation Schritt-für-Schritt

### 1. Repository Klonen

```bash
git clone https://github.com/ChristineJanischek/python-algorithmen-datenstrukturen.git
cd python-algorithmen-datenstrukturen/apps/drawio-extension
```

### 2. Dependencies installieren

```bash
npm install
```

Das installiert alle im `package.json` definierten Pakete:
- `mxgraph` - Die Draw.io Engine
- `fast-xml-parser` - Für XML-Verarbeitung
- `jest` - Testing Framework
- Und viele mehr...

**Erwartet bitte 2-3 Minuten.**

### 3. Development Server starten

```bash
npm run dev
```

Du solltest sehen:
```
✓ Webpack Dev Server läuft auf http://localhost:8080
✓ Live Reload aktiviert
✓ Struktogramm Plugin geladen
```

---

## 🎨 Integration mit Draw.io

### Option A: Lokal (für Entwicklung)

1. Öffne https://draw.io in deinem Browser
2. Gehe zu: `File → Preferences → Apps`
3. Klicke "Add Custom App"
4. Gib ein: `http://localhost:8080/plugin.js`
5. Reload Draw.io

### Option B: Mit lokaler Draw.io Instanz

```bash
# Clone & Build Draw.io
git clone https://github.com/jgraph/drawio.git
cd drawio
npm install
npm run start

# Öffne dann http://localhost:8080
```

---

## ✅ Verifizieren der Installation

### 1. Projekt kompiliert

```bash
npm run build
```

Sollte ohne Fehler durchlaufen.

### 2. Tests bestanden

```bash
npm test
```

Sollte alle Tests grün zeigen (später wenn Tests geschrieben sind).

### 3. Extension laden

Öffne Draw.io und überprüfe:
- ✅ Ist die Palette "Struktogramme (BW)" sichtbar?
- ✅ Kannst du ein Shape in den Canvas ziehen?
- ✅ Wird das JSON-Panel auf der rechten Seite aktualisiert?

---

## 🔧 Häufige Probleme & Lösungen

### Problem: `npm install` schlägt fehl

**Symptom:** Fehler wie `ERR! code ERESOLVE`

**Lösung:**
```bash
npm install --legacy-peer-deps
```

### Problem: Port 8080 ist bereits in Benutzung

**Symptom:** `Error: listen EADDRINUSE :::8080`

**Lösung:**
```bash
# Finde Prozess auf Port 8080
lsof -i :8080

# Beende ihn
kill -9 <PID>

# Oder nutze anderen Port
npm run dev -- --port 3000
```

### Problem: Extension wird nicht geladen

**Symptom:** Palette erscheint nicht in Draw.io

**Lösung:**
1. Überprüfe Browser-Konsole (F12): Gibt es Fehler?
2. Stelle sicher, dass Dev Server läuft: `npm run dev`
3. Leere Draw.io Cache: `CTRL+SHIFT+DEL`
4. Versuche neu zu laden

---

## 📚 Nächste Schritte

Nach erfolgreichem Setup:

1. **Lese die Architektur:** [architecture.md](./architecture.md)
2. **Schreib deinen ersten Shape:** [dev-guide.md](./dev-guide.md)
3. **Schau dir Beispiele an:** `examples/`

---

## 🎯 Development Workflow

### Für tägliche Entwicklung:

```bash
# Terminal 1: Dev Server
npm run dev

# Terminal 2: Tests (Watch-Mode)
npm test -- --watch

# Terminal 3: Dein Editor
code .
```

### Code schreiben → Testen → Builden

```bash
# Nach Änderungen sofort testen
npm test

# Wenn alles grün ist, builden
npm run build

# Und commiten
git add .
git commit -m "Feature: xyz"
```

---

## 💾 Speiciern von Änderungen

### Git Workflow

```bash
# Siehe welche Dateien geändert wurden
git status

# Stagen der Änderungen
git add .

# Commit mit Nachricht
git commit -m "docs: Add installation guide"

# Push zu GitHub
git push origin main
```

---

## 🚀 Ready to Code?

Weiter gehts mit dem [Developer Guide](./dev-guide.md)!
