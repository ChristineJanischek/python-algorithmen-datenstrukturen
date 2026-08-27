# 🧪 Testing Guide - BW Library in Draw.io laden

**Version:** 0.1.0  
**Phase:** 2-A Testing  
**Ziel:** Validieren, dass `library.xml` mit BW-Operator-Templates in Draw.io korrekt geladen wird

---

## 🎯 Was testen wir?

Nach Phase 2-A haben wir `library.xml` mit BW-konformen Operator-Templates erstellt. Jetzt überprüfen wir:

- ✅ Library kann in Draw.io geladen werden
- ✅ Alle BW-Operator-Templates werden angezeigt
- ✅ Shapes können in Canvas gezogen werden
- ✅ Formen entsprechen BW-Standard (Alternative-Dreieck, umgedrehtes L, Aufruf-Seitenstriche)
- ✅ Text kann editiert werden

---

## 📋 Voraussetzungen

**Du brauchst:**
- ✅ Web-Browser (Chrome, Firefox, Edge)
- ✅ Internet-Verbindung
- ✅ Die Datei `library.xml` (bereits vorhanden in `apps/drawio-extension/`)
- ⚠️ **KEIN** npm install nötig für diesen Test!

**Zeit:** ~10-15 Minuten

---

## ⚡ Smoke-Test (2 Minuten)

Für Blog/Quick-Check ohne komplette Testsession:

1. Öffne **https://app.diagrams.net** und erstelle ein leeres Diagramm.
2. Klicke **File → Open Library from → URL...**.
3. Füge ein:
   ```
   https://raw.githubusercontent.com/ChristineJanischek/python-algorithmen-datenstrukturen/main/apps/drawio-extension/library.xml
   ```
4. Ziehe diese 4 Shapes auf den Canvas: **Wenn ... dann ... sonst**, **While**, **For**, **Aufruf**.
5. Prüfe kurz:
   - Alternative = Rechteck mit eingebettetem Dreieck + J/N
   - While/For = umgedrehtes L
   - Aufruf = Rechteck mit zwei vertikalen Seitenstrichen

Wenn das passt, ist die BW-Notation im Kern korrekt eingebunden.

---

## 🚀 Methode 1: Draw.io Online (EINFACHSTE Methode)

### Schritt 1: Draw.io öffnen

1. Öffne deinen Browser
2. Gehe zu: **https://app.diagrams.net** (oder https://draw.io)
3. Wähle "Create New Diagram"
4. Wähle "Blank Diagram" → OK

Du siehst jetzt einen leeren Canvas mit der Shape-Palette links.

---

### Schritt 2: Library-Datei vorbereiten

Die `library.xml` muss für Draw.io als Bibliotheksdatei zugänglich sein:

**Option A: Via GitHub Raw URL** (wenn schon gepusht)
```
https://raw.githubusercontent.com/ChristineJanischek/python-algorithmen-datenstrukturen/main/apps/drawio-extension/library.xml
```

**Option B: Lokale Datei** (später laden)
- Kopiere `library.xml` auf deinen Desktop
- Oder merke dir den Pfad: `apps/drawio-extension/library.xml`

---

### Schritt 3: Custom BW Library laden

#### Via URL (wenn GitHub):

1. In Draw.io: Klicke **File** → **Open Library from** → **URL...**
2. Gib die GitHub Raw URL ein:
   ```
   https://raw.githubusercontent.com/ChristineJanischek/python-algorithmen-datenstrukturen/main/apps/drawio-extension/library.xml
   ```
3. Klicke **OK**

#### Via lokale Datei:

1. In Draw.io: Klicke **File** → **Open Library from** → **Device...**
2. Wähle `library.xml` aus
3. Klicke **Open**

---

### Schritt 4: Library sollte jetzt laden! 🎉

**Was du sehen solltest:**

Links in der Palette sollte ein neuer Abschnitt erscheinen:
```
┌─────────────────────────┐
│ Struktogramme (BW...)   │  ← Deine Custom Library!
├─────────────────────────┤
│ ┌─────┐  Anweisung      │
│ │     │                 │
│ └─────┘                 │
│                         │
│ ◇       Alternative     │
│                         │
│ ⊐       While           │
│                         │
│ ⊐       For             │
│                         │
│ ┌─────┐  Deklaration    │
│ └─────┘                 │
│  ...und mehr...         │
└─────────────────────────┘
```

**Wenn das NICHT erscheint:** Siehe Troubleshooting unten ⬇️

---

### Schritt 5: Shapes testen

#### Test 1: Shape auf Canvas ziehen

1. Klicke auf "Anweisung" in der Palette
2. Halte Maustaste gedrückt
3. Ziehe auf den Canvas
4. Lasse los

**Erwartetes Ergebnis:**
```
┌──────────────────┐
│  text            │  ← Weißes Rechteck mit Text-Placeholder
└──────────────────┘
```

#### Test 2: Text editieren

1. Doppelklick auf das Shape
2. Tippe: `summe = 0`
3. Klicke außerhalb

**Erwartetes Ergebnis:**
```
┌──────────────────┐
│  summe = 0       │  ← Dein Text!
└──────────────────┘
```

#### Test 3: BW-Formen überprüfen

Ziehe folgende Shapes und überprüfe die Struktur:

| Shape | Erwartete Form |
|-------|-----------------|
| Anweisung | Rechteck |
| Alternative | Rechteck mit eingebettetem Dreieck + J/N-Bereiche |
| While | Umgedrehtes L |
| For | Umgedrehtes L |
| Aufruf | Rechteck mit zwei vertikalen Seitenstrichen |

#### Test 4: Kontrollstrukturen

Teste die komplexen Shapes:

**While-Schleife:**
```
┌──────────────────┐
│ Wiederhole...    │  ← Schleifenkopf
│                  │
│  (Körper)        │  ← umgedrehtes L
└──────────────────┘
```

**For-Schleife:**
```
┌──────────────────┐
│ Zähle i...       │  ← Schleifenkopf
│                  │
│  (Körper)        │  ← Körper (weiß)
│                  │
└──────────────────┘
```

---

## ✅ Test-Checkliste

Hake ab, was funktioniert:

### Basis-Tests:
- [ ] Library erscheint in der Palette
- [ ] Alle BW-Operator-Templates sind sichtbar
- [ ] Shape kann auf Canvas gezogen werden
- [ ] Text kann editiert werden
- [ ] Shape kann verschoben werden
- [ ] Shape kann kopiert werden (Strg+C, Strg+V)

### Visuelle Tests:
- [ ] Anweisung ist weiß mit schwarzer Umrandung
- [ ] Alternative zeigt Rechteck + eingebettetes Dreieck + J/N
- [ ] While ist als umgedrehtes L dargestellt
- [ ] For ist als umgedrehtes L dargestellt
- [ ] Aufruf zeigt vertikale Seitenstriche im Rechteck
- [ ] Operator-Text folgt `Operator: ...`-Notation

### Fortgeschrittene Tests:
- [ ] Mehrere Shapes können kombiniert werden
- [ ] Shapes können verbunden werden (mit Pfeilen)
- [ ] Zoom funktioniert (Strg + Mausrad)
- [ ] Export als PNG funktioniert (File → Export as → PNG)
- [ ] Speichern funktioniert (File → Save as)

---

## 🐛 Troubleshooting

### Problem 1: Library erscheint nicht

**Symptom:** Nach "Open Library from URL/Device" passiert nichts

**Mögliche Ursachen:**
1. **XML/JSON-Syntax-Fehler** in `library.xml`
2. **Falsche URL** (Tippfehler)
3. **Browser-Blocker** (CORS Issue)
4. **Draw.io Cache** (alte Version geladen)

**Lösungen:**

Wichtig: `File → Open Library from ...` erwartet eine **Bibliotheksdatei** (`<mxlibrary>`), nicht direkt ein Stencil-Set (`<shapes>`). Verwende deshalb `library.xml`.

```bash
# 1. XML validieren
cd apps/drawio-extension
python3 -c "import xml.etree.ElementTree as ET; ET.parse('library.xml'); print('OK')"

# 2. URL überprüfen
# Öffne die URL direkt im Browser - sollte XML zeigen

# 3. Browser-Console checken (F12)
# Gibt es CORS-Fehler oder andere Meldungen?

# 4. Cache leeren
# Strg+Shift+Del → "Cached Images/Files" → Clear
```

### Problem 2: Shapes sehen nicht BW-konform aus

**Symptom:** Alternative/Schleife/Aufruf sehen wie Flussdiagramm statt Struktogramm aus

**Lösung:**
- Vergleiche mit `struktogramme/Operatorenliste-Struktogramme.md`
- Prüfe die Templates „Wenn ... dann ... sonst“, „While“, „For“, „Aufruf“ in `library.xml`
- Lade die Library neu (File → Close Library, dann erneut öffnen)

### Problem 3: Operator-Text wird nicht korrekt übernommen

**Symptom:** Shape wird angezeigt, aber Operator-Zeilen fehlen oder sind falsch formatiert

**Lösung:**
- Doppelklick auf Shape und Operator-Text direkt eintragen
- Prüfe, dass `whiteSpace=wrap` im Style aktiv ist
- Nutze kurze Zeilen im Kopf (z. B. `Deklaration:`) und Details in Zeile 2

### Problem 4: Library verschwindet nach Reload

**Symptom:** Nach Browser-Reload ist Library weg

**Das ist NORMAL!** Custom Libraries müssen jedes Mal neu geladen werden.

**Lösung für Phase 2-B:**
- Wir werden ein Plugin erstellen, das die Library automatisch lädt
- Bis dahin: Jedes Mal manuell laden

---

## 📸 Screenshots für Dokumentation

Wenn alles funktioniert, mache Screenshots von:

1. **Palette mit allen Shapes:** (für README.md)
2. **Beispiel-Struktogramm:** (ein einfacher Algorithmus gezeichnet)
3. **BW-Formen:** Alternative, While, For, Aufruf nebeneinander

Speichere in: `apps/drawio-extension/docs/screenshots/`

---

## 🔧 Erweiterte Tests (Optional)

### Test mit verschiedenen Browsern:

- [ ] Chrome / Chromium
- [ ] Firefox
- [ ] Safari (Mac)
- [ ] Edge

### Test mit lokalem Draw.io:

```bash
# Draw.io lokal installieren
git clone https://github.com/jgraph/drawio.git
cd drawio/src/main/webapp
python3 -m http.server 8080

# Öffne http://localhost:8080
# Lade library.xml von lokalem Dateisystem
```

---

## 📊 Test-Report Template

Nach dem Test, dokumentiere:

```markdown
## Test-Report: library.xml in Draw.io

**Datum:** 18.02.2026
**Tester:** [Dein Name]
**Browser:** Chrome 120
**Draw.io Version:** https://app.diagrams.net

### Ergebnisse:

| Test | Status | Bemerkungen |
|------|--------|-------------|
| Library lädt | ✅ PASS | |
| BW-Templates sichtbar | ✅ PASS | |
| Drag & Drop | ✅ PASS | |
| Text-Editing | ✅ PASS | |
| BW-Formen korrekt | ✅ PASS | |
| Export PNG | ✅ PASS | |

### Probleme:

- Keine!

### Nächste Schritte:

- Phase 2-B: plugin.js implementieren
- Dokumentation mit Screenshots ergänzen
```

---

## ✅ Erfolgs-Kriterium

**Phase 2-A gilt als erfolgreich getestet, wenn:**

1. ✅ Library lädt ohne Fehler
2. ✅ Alle Kernformen (Alternative/While/For/Aufruf) sind BW-konform
3. ✅ Drag & Drop + Text-Editing funktioniert
4. ✅ Operatortexte folgen der Operatorenliste
5. ✅ Export als PNG/SVG funktioniert

**Wenn alle 5 Punkte ✅ = READY FÜR PHASE 2-B!**

---

## 🚀 Nach erfolgreichem Test

### Committe das Test-Report:

```bash
cd apps/drawio-extension
touch TEST_REPORT_PHASE_2A.md  # Fülle mit deinen Resultaten

git add TEST_REPORT_PHASE_2A.md
git commit -m "test: Phase 2-A library.xml validated against BW notation"
git push origin main
```

### Update Todo:

```
✅ Phase 2-A: library.xml mit BW-Operator-Templates - TESTED & WORKING
```

---

## 📚 Weiterführende Links

- **Draw.io Custom Libraries:** https://www.drawio.com/blog/custom-libraries
- **mxGraph Shapes Reference:** https://github.com/jgraph/mxgraph/tree/master/javascript/examples/grapheditor
- **mxLibrary / Stencil Format:** https://jgraph.github.io/mxgraph/docs/manual.html

---

## 💡 Tipps & Best Practices

### Tipp 1: Library während Entwicklung testen
```
Jede Änderung an library.xml:
1. Speichern
2. In Draw.io: File → Close Library
3. File → Open Library from Device (neu laden)
4. Testen
```

### Tipp 2: Mehrere Versionen parallel
```
library_v1.xml  ← Stable Version
library_v2.xml  ← Neue Features
library.xml     ← Current/Production
```

### Tipp 3: Debugging mit Browser DevTools
```
F12 → Console → Suche nach Fehlern
Netzwerk-Tab → Siehe ob XML korrekt geladen
```

---

**Viel Erfolg beim Testen! 🎉**

Bei Fragen oder Problemen: Siehe Troubleshooting oder frage nach!

<!-- CUSTOM_LICENSE_NOTICE_START -->
## License

This repository is licensed under a custom license.

- Attribution required: Christine Janischek - https://emotionalspirit.de
- Non-commercial use only
- Use only within state school systems
- Any other use requires explicit prior written permission
<!-- CUSTOM_LICENSE_NOTICE_END -->
