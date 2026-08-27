# 📋 Markdown Reviewer - Automatische Konsistenz-Überprüfung

Sie können die automatische Überprüfung aller Markdown-Dateien bei jedem `git push` aktivieren.

## 🎯 Was wird überprüft?

1. **Ungültige Datei-Referenzen** - Links auf nicht existente Dateien
2. **Tote Links & Verwaiste Dateien** - Dateien, die nirgends verlinkt sind
3. **Struktur-Konsistenz** - Fehlende Einträge in INDEX.md Dateien
4. **Dokumentations-Sync** - Neue Module ohne Dokumentation

## 🚀 Installation

```bash
# Setup-Skript ausführen (einmalig)
python3 apps/tools/setup_markdown_reviewer.py

# Oder manuell:
chmod +x .git/hooks/pre-push
```

## 📝 Verwendung

### Normaler Git Workflow
```bash
git add .
git commit -m "Meine Änderungen"
git push  # <-- Hook fragt nach Review
```

### Manual Review (ohne Push)
```bash
python3 apps/tools/markdown_reviewer.py
```

### Schneller Link-Check (neu)
```bash
# Standard: prüft docs/aufgaben, docs/information, docs/loesungen, docs/handbuch
python3 apps/tools/check_markdown_links.py

# Optional inkl. Template-Dateien
python3 apps/tools/check_markdown_links.py --include-templates

# Eigene Verzeichnisse angeben
python3 apps/tools/check_markdown_links.py --dirs docs/handbuch docs/aufgaben
```

## 🔧 Hook-Verhalten

Beim `git push` wird interaktiv gefragt:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 GIT PRE-PUSH HOOK - Markdown Review
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Möchtest Du die Markdown-Dateien überprüfen lassen?
  ✓ Ungültige Datei-Referenzen
  ✓ Tote Links / Verwaiste Dateien
  ✓ Struktur-Konsistenz (fehlende INDEX-Einträge)
  ✓ Dokumentations-Synchronisation

Review durchführen? (ja/Ja/j/J oder Enter zum Überspringen):
```

### Optionen
- **ja/Ja/j/J** - Review starten
- **Enter** - Review überspringen (schneller Push)
- **Bei Fehlern:**
  - Kann trotzdem gepusht werden (mit Bestätigung)
  - Oder abhrechen und Fehler beheben

## 📊 Report-Ausgabe

Nach dem Review erscheint ein Report mit:

```
❌ FEHLER (47)    - Müssen behoben werden
⚠️  WARNUNGEN (5) - Sollten überprüft werden
ℹ️  INFO (0)      - Nur Information
```

Der Report wird auch als JSON gespeichert:
```
.github/markdown_review_report.json
```

## 🛠️ Deaktivierung

Falls Sie den Hook temporär deaktivieren möchten:

```bash
# Mit --no-verify pushen (Hook wird ignoriert)
git push --no-verify

# Hook komplett entfernen
rm .git/hooks/pre-push
```

## 📝 Beispiele

### Beispiel 1: Erfolgreicher Review
```
🔍 Überprüfe Markdown-Dateien on Konsistenz...

✅ Review erfolgreich - keine kritischen Fehler
(Warnungen sollten trotzdem überprüft werden)

Mit Push fortfahren? (Enter=Ja / n=Nein): [Enter]
▶ Push wird fortgesetzt...
```

### Beispiel 2: Fehler gefunden
```
❌ Markdown-Fehler gefunden!
  • [invalid_reference] docs/aufgaben/L1_1_1.md
    → Ungültige Referenz: docs/handbuch/missing_file.md

Trotzdem pushen? (Enter=Nein / y=Ja): [n]
⊘ Push wurde abgebrochen
```

### Beispiel 3: Review überspringen
```
Review durchführen? (ja/Ja/j/J oder Enter zum Überspringen): [Enter]
⊘ Review übersprungen - Push wird fortgesetzt
```

## 📚 Zusätzliche Ressourcen

- [markdown_reviewer.py](markdown_reviewer.py) - Python-Script für Reviews
- [.git/hooks/pre-push](.git/hooks/pre-push) - Git Hook
- [setup_markdown_reviewer.py](setup_markdown_reviewer.py) - Setup-Anleitung

## 🤔 Häufig gestellte Fragen

### Warum fragt der Hook nach jedem Push?
Das ist gewünscht - es soll sicherstellen, dass Markdown-Änderungen vor jedem Push validiert werden.

### Kann ich den Hook deaktivieren?
Ja, mit `git push --no-verify` oder durch Löschen des `.git/hooks/pre-push` Skripts.

### Was sind die meisten Fehler/Warnungen?
Hauptsächlich referenzierte Dateien, die nicht existieren oder Dateien, wurden nicht in INDEX.md eingetragen.

### Muss ich den Hook installieren?
Nein, er wird automatisch ausgeführt. Installation ist nur für die initialen Kommandos nötig.

---

**Version:** 1.0  
**Datum:** Februar 2025  
**Autor:** GitHub Copilot Automation System

<!-- CUSTOM_LICENSE_NOTICE_START -->
## License

This repository is licensed under a custom license.

- Attribution required: Christine Janischek - https://emotionalspirit.de
- Non-commercial use only
- Use only within state school systems
- Any other use requires explicit prior written permission
<!-- CUSTOM_LICENSE_NOTICE_END -->
