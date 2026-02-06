# Changelog

Alle wichtigen Änderungen an diesem Projekt werden in dieser Datei dokumentiert.

Das Format basiert auf [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [1.1.0] - 2026-02-05

### ✨ Added
- **E-Learning Content Management System** (`src/utils/elearning_manager.py`)
  - `ELearningManager` für strukturierte Verwaltung von Aufgaben, Informationen und Lösungen
  - Quick-Create-Funktionen für schnelle Content-Erstellung
  - Automatische Index-Generierung
  - Vollständige Metadaten-Verwaltung (Level, Kategorie, Tags, Lernziele)
  - Unterstützung für Struktur: `LX_Y_Z_Thema` (Level_Kategorie_Nummer_Thema)

### 🔧 Changed
- Erweiterte Copilot-Anweisungen für E-Learning-Workflow
- Optimierte Dokumentation für Templates

### 📝 Documentation
- Neuer Guide: `docs/handbuch/ELEARNING_TEMPLATE_GUIDE.md`

---

## [1.0.0] - 2026-01-30

### ✨ Added
- **Struktogramm-System - Vollständige Implementierung**
  - `struktogramme/Operatorenliste-Struktogramme.md` - Offizielle BW-Operatoren
  - `src/utils/struktogramm_helper.py` - Python Helper mit vorgefertigten Patterns
  - Vorhandene Patterns:
    - Array durchlaufen
    - Summe berechnen
    - Maximum/Minimum finden
    - Lineare Suche
    - Binäre Suche
  - `struktogramme/*.stgr` - 40+ Beispiel-Struktogramme

- **GitHub Copilot Instructions** (`.github/copilot-instructions.md`)
  - Umfassender Guide für AI-Assistenten
  - Best Practices für Strukturen und Code
  - Workflow-Dokumentation

- **Dokumentations-Guide** (`docs/handbuch/STRUKTOGRAMM_GUIDE.md`)
  - Praktische Anleitung mit Beispielen
  - BW-Standard-Konformität
  - Pattern-Übersicht für häufige Aufgaben

### 🔧 Changed
- Reorganisierte Dokumentationsstruktur
- Überarbeitete `niveau/`-Materialien
- Aktualisierte Copilot-Anweisungen

### 🐛 Fixed
- Merge-Konflikte in Dokumentation aufgelöst

### 📚 Documentation
- Deutsche Dokumentationsübersicht
- Aktualisierte README.md mit Lehrer-Anleitung

---

## [0.1.0] - 2026-01-01

### ✨ Initial Release
- Projekt-Setup und Basis-Struktur
- Erste Struktogramm-Beispiele
- README.md und Dokumentations-Framework
- Niveau-spezifische Materialien (L1, L2, L3)
- Basis-Aufgabensammlung

---

## Versionierungs-Konvention

Dieses Projekt folgt [Semantic Versioning](https://semver.org/):

- **MAJOR** Version (X.0.0): Breaking Changes in Routinen/APIs
- **MINOR** Version (0.Y.0): Neue Features, rückwärtskompatibel
- **PATCH** Version (0.0.Z): Bugfixes

### Release-Zyklus

- **Stable Releases** (v1.0.0, v1.1.0, ...): `main` branch
- **Development**: `develop` branch
- **Hotfixes**: `hotfix/*` branches
- **Archived Snapshots**: `archive/snapshot-YYYY-MM-DD`

### Kennzeichnungen

- ✨ **Added**: Neue Features
- 🔧 **Changed**: Änderungen an bestehenden Features
- 🐛 **Fixed**: Bugfixes
- ⚠️ **Deprecated**: Veraltete Features
- 🗑️ **Removed**: Entfernte Features
- 🔒 **Security**: Sicherheits-Updates
- 📝 **Documentation**: Dokumentations-Änderungen
- 📚 **Content**: Content-Erweiterungen (Aufgaben, Lösungen, Info)
