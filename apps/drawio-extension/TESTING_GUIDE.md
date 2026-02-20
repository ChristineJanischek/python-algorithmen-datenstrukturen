# 🧪 Testing Guide - Stencil in Draw.io laden

**Version:** 0.1.0  
**Phase:** 2-A Testing  
**Ziel:** Validieren, dass stencil.xml in Draw.io korrekt geladen wird

---

## 🎯 Was testen wir?

Nach Phase 2-A haben wir `stencil.xml` mit 11 Shapes erstellt. Jetzt überprüfen wir:

- ✅ Stencil kann in Draw.io geladen werden
- ✅ Alle 11 Shapes werden angezeigt
- ✅ Shapes können in Canvas gezogen werden
- ✅ Farben & Formen sind korrekt
- ✅ Text kann editiert werden

---

## 📋 Voraussetzungen

**Du brauchst:**
- ✅ Web-Browser (Chrome, Firefox, Edge)
- ✅ Internet-Verbindung
- ✅ Die Datei `stencil.xml` (bereits vorhanden in `apps/drawio-extension/`)
- ⚠️ **KEIN** npm install nötig für diesen Test!

**Zeit:** ~10-15 Minuten

---

## 🚀 Methode 1: Draw.io Online (EINFACHSTE Methode)

### Schritt 1: Draw.io öffnen

1. Öffne deinen Browser
2. Gehe zu: **https://app.diagrams.net** (oder https://draw.io)
3. Wähle "Create New Diagram"
4. Wähle "Blank Diagram" → OK

Du siehst jetzt einen leeren Canvas mit der Shape-Palette links.

---

### Schritt 2: Stencil-Datei vorbereiten

Die `library.xml` muss für Draw.io als Bibliotheksdatei zugänglich sein:

**Option A: Via GitHub Raw URL** (wenn schon gepusht)
```
https://raw.githubusercontent.com/ChristineJanischek/python-algorithmen-datenstrukturen/main/apps/drawio-extension/library.xml
```

**Option B: Lokale Datei** (später laden)
- Kopiere `library.xml` auf deinen Desktop
- Oder merke dir den Pfad: `apps/drawio-extension/library.xml`

---

### Schritt 3: Custom Stencil Library laden

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

### Schritt 4: Stencil sollte jetzt laden! 🎉

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

#### Test 3: Farben überprüfen

Ziehe folgende Shapes und überprüfe Farben:

| Shape | Erwartete Farbe |
|-------|-----------------|
| Anweisung | Weiß |
| Alternative | Hellgelb |
| Deklaration | Hellblau |
| Einlesen | Hellgrün (mit schrägen Kanten) |
| Ausgabe | Gelb (mit schrägen Kanten) |
| Rückgabe | Hellrot |

#### Test 4: Kontrollstrukturen

Teste die komplexen Shapes:

**While-Schleife:**
```
┌──────────────────┐
│ Wiederhole...    │  ← Kopf (gelb)
├──────────────────┤
│                  │
│  (Körper)        │  ← Körper (weiß)
│                  │
└──────────────────┘
```

**For-Schleife:**
```
┌──────────────────┐
│ Zähle i...       │  ← Kopf (grün)
├──────────────────┤
│                  │
│  (Körper)        │  ← Körper (weiß)
│                  │
└──────────────────┘
```

---

## ✅ Test-Checkliste

Hake ab, was funktioniert:

### Basis-Tests:
- [ ] Stencil erscheint in der Palette
- [ ] Alle 11 Shapes sind sichtbar
- [ ] Shape kann auf Canvas gezogen werden
- [ ] Text kann editiert werden
- [ ] Shape kann verschoben werden
- [ ] Shape kann kopiert werden (Strg+C, Strg+V)

### Visuelle Tests:
- [ ] Anweisung ist weiß mit schwarzer Umrandung
- [ ] Alternative zeigt Raute (◇) Form
- [ ] While hat gelben Kopf + weißen Körper
- [ ] For hat grünen Kopf + weißen Körper
- [ ] Deklaration ist hellblau
- [ ] Einlesen hat schräge Kanten (Trapez)
- [ ] Ausgabe hat schräge Kanten (Trapez)
- [ ] Rückgabe ist hellrot

### Fortgeschrittene Tests:
- [ ] Mehrere Shapes können kombiniert werden
- [ ] Shapes können verbunden werden (mit Pfeilen)
- [ ] Zoom funktioniert (Strg + Mausrad)
- [ ] Export als PNG funktioniert (File → Export as → PNG)
- [ ] Speichern funktioniert (File → Save as)

---

## 🐛 Troubleshooting

### Problem 1: Stencil erscheint nicht

**Symptom:** Nach "Open Library from URL/Device" passiert nichts

**Mögliche Ursachen:**
1. **XML-Syntax-Fehler** in stencil.xml
2. **Falsche URL** (Tippfehler)
3. **Browser-Blocker** (CORS Issue)
4. **Draw.io Cache** (alte Version geladen)

**Lösungen:**

Wichtig: `File → Open Library from ...` erwartet eine **Bibliotheksdatei** (`<mxlibrary>`), nicht direkt ein Stencil-Set (`<shapes>`). Verwende deshalb `library.xml`.

```bash
# 1. XML validieren
cd apps/drawio-extension
xmllint stencil.xml  # Sollte keine Fehler zeigen

# 2. URL überprüfen
# Öffne die URL direkt im Browser - sollte XML zeigen

# 3. Browser-Console checken (F12)
# Gibt es CORS-Fehler oder andere Meldungen?

# 4. Cache leeren
# Strg+Shift+Del → "Cached Images/Files" → Clear
```

### Problem 2: Shapes sehen falsch aus

**Symptom:** Farben sind anders, Formen sind kaputt

**Lösung:**
- Überprüfe `<path data="...">` in stencil.xml
- Vergleiche mit STENCIL_GUIDE.md
- Teste mit einem einfacheren Shape (nur Rechteck)

### Problem 3: Text wird nicht angezeigt

**Symptom:** Shape zeichnet, aber kein Text-Placeholder

**Lösung:**
- Überprüfe `<foreground>` in stencil.xml
- Stelle sicher, dass `<text>` Element korrekt ist
- Teste mit Rechtsklick → "Edit Style" → setze "text=1"

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
3. **Farbcodierung:** (alle 7 Instruction Types nebeneinander)

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
# Lade stencil.xml von lokalem Dateisystem
```

---

## 📊 Test-Report Template

Nach dem Test, dokumentiere:

```markdown
## Test-Report: stencil.xml in Draw.io

**Datum:** 18.02.2026
**Tester:** [Dein Name]
**Browser:** Chrome 120
**Draw.io Version:** https://app.diagrams.net

### Ergebnisse:

| Test | Status | Bemerkungen |
|------|--------|-------------|
| Stencil lädt | ✅ PASS | |
| 11 Shapes sichtbar | ✅ PASS | |
| Drag & Drop | ✅ PASS | |
| Text-Editing | ✅ PASS | |
| Farb-Kodierung | ✅ PASS | |
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

1. ✅ Stencil lädt ohne Fehler
2. ✅ Mindestens 8 von 11 Shapes funktionieren
3. ✅ Drag & Drop + Text-Editing funktioniert
4. ✅ Farben sind wie erwartet
5. ✅ Export als PNG/SVG funktioniert

**Wenn alle 5 Punkte ✅ = READY FÜR PHASE 2-B!**

---

## 🚀 Nach erfolgreichem Test

### Committe das Test-Report:

```bash
cd apps/drawio-extension
touch TEST_REPORT_PHASE_2A.md  # Fülle mit deinen Resultaten

git add TEST_REPORT_PHASE_2A.md
git commit -m "test: Phase 2-A stencil.xml validated in Draw.io"
git push origin main
```

### Update Todo:

```
✅ Phase 2-A: stencil.xml mit 4 BW-Formen - TESTED & WORKING
```

---

## 📚 Weiterführende Links

- **Draw.io Custom Libraries:** https://www.drawio.com/blog/custom-libraries
- **mxGraph Shapes Reference:** https://github.com/jgraph/mxgraph/tree/master/javascript/examples/grapheditor
- **Stencil XML Format:** https://jgraph.github.io/mxgraph/docs/manual.html

---

## 💡 Tipps & Best Practices

### Tipp 1: Stencil während Entwicklung testen
```
Jede Änderung an stencil.xml:
1. Speichern
2. In Draw.io: File → Close Library
3. File → Open Library from Device (neu laden)
4. Testen
```

### Tipp 2: Mehrere Versionen parallel
```
stencil_v1.xml  ← Stable Version
stencil_v2.xml  ← Neue Features
stencil.xml     ← Current/Production
```

### Tipp 3: Debugging mit Browser DevTools
```
F12 → Console → Suche nach Fehlern
Netzwerk-Tab → Siehe ob XML korrekt geladen
```

---

**Viel Erfolg beim Testen! 🎉**

Bei Fragen oder Problemen: Siehe Troubleshooting oder frage nach!
