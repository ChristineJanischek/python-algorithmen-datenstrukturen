# Scripts - Automatisierungstools

Dieses Verzeichnis enthält ausführbare Skripte für automatisierte Aufgaben im Repository.

## 📋 Verfügbare Skripte

### `optimize_docx.py`

Optimiert Markdown-Dokumente für DOCX-Export mit Fokus auf:
- Struktogramm-Einbettung in Word-Dokumenten
- Code-Block-Styling und Formatierung
- Versionsverwaltung in Fußzeilen

**Verwendung:**
```bash
python scripts/optimize_docx.py [OPTIONS]
```

**Optionen:**
```
--dir DIRECTORY           Zielverzeichnis (default: docs/pruefungen)
--config FILE            Konfigurationsdatei (JSON)
--verbose, -v            Ausführliche Ausgabe
--dry-run                Keine Änderungen durchführen
--help, -h               Hilfe anzeigen
```

**Beispiele:**
```bash
# Alle Prüfungsdokumente optimieren
python scripts/optimize_docx.py

# Mit ausführlicher Ausgabe
python scripts/optimize_docx.py --verbose

# Spezifisches Verzeichnis
python scripts/optimize_docx.py --dir docs/aufgaben

# Dry-Run (keine Änderungen)
python scripts/optimize_docx.py --dry-run --verbose

# Mit Konfigurationsdatei
python scripts/optimize_docx.py --config config/docx_config.json
```

## 🔧 Technische Details

Alle Skripte verwenden die utilities aus `src/utils/`:

| Script | Verwendet |
|--------|-----------|
| `optimize_docx.py` | `docx_markdown_optimizer.py` |

## 📚 Vollständige Dokumentation

Siehe [`docs/handbuch/DOCX_OPTIMIZER_GUIDE.md`](../docs/handbuch/DOCX_OPTIMIZER_GUIDE.md) für:
- Architektur und Design
- Python-API Beispiele
- Konfigurationsoptionen
- Integration mit anderen Tools
- Troubleshooting

## 🚀 Schnellstart

```bash
# 1. Virtual Environment aktivieren
source .venv/bin/activate

# 2. Optimierungen durchführen
python scripts/optimize_docx.py --verbose

# 3. Ergebnisse überprüfen
git diff docs/pruefungen/
```

## 🤝 Contributing

Neue Skripte sollten:
- ✅ Im `scripts/` Verzeichnis liegen
- ✅ Mit `#!/usr/bin/env python3` Shebang beginnen
- ✅ Ausführbar sein (`chmod +x`)
- ✅ Vollständige Hilfe mit `--help` bieten
- ✅ Dokumentiert sein in diesem README

---

**Repository:** [`python-algorithmen-datenstrukturen`](https://github.com/ChristineJanischek/python-algorithmen-datenstrukturen)  
**Letzte Aktualisierung:** 2026-03-03
