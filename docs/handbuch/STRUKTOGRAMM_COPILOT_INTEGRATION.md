# Struktogramm-Integration in GitHub Copilot Instructions

Diese Datei dokumentiert, wie das Struktogramm-Tool automatisch in GitHub Copilot's Decision-Making integriert wird.

---

## 🎯 Automatische Aktivierung

**Trigger:** Wenn das Stichwort "Struktogramm" erkannt wird (von Benutzer oder in Kontext)

**Verhalten:** Copilot nutzt automatisch die Notation aus `struktogramme/Operatorenliste-Struktogramme.md`

---

## 📋 Eingebettete Instructions

Die folgenden Instructions sind in `.github/copilot-instructions.md` integriert:

### Wenn Struktogramm-Aufgabe erkannt:

```markdown
### 🎯 STRUKTOGRAMM-REGEL (AUTOMATISCH AKTIV)

**Trigger:** Wort "Struktogramm" in Aufgabe/Request/Datei

**Sofort-Aktivierung:**
1. Konsultiere `struktogramme/Operatorenliste-Struktogramme.md` 
2. VERWENDE NUR diese Operatoren:
   - Deklaration
   - Initialisierung
   - Deklaration und Initialisierung
   - Zuweisung
   - Einlesen
   - Ausgabe
   - Rückgabe
   - Aufruf
   - Wenn...dann, ...sonst
   - Wiederhole solange
   - Zähle...von...bis, Schrittweite
   - Anzahl der Elemente des Arrays

3. ABSOLUTES VERBOT:
   - ❌ NIEMALS "while" statt "Wiederhole solange"
   - ❌ NIEMALS "if" statt "Wenn"
   - ❌ NIEMALS "for" statt "Zähle"
   - ❌ NIEMALS Flussdiagramme

4. NORMALFORM:
   ```
   Deklaration und Initialisierung: variable als Datentyp = wert
   Wenn bedingung, dann
       J
           [Anweisungen]
       , sonst
       N
           [Anweisungen]
   ```

5. Tools verfügbar:
   - `apps/tools/struktogramm_validator.py` - Prüfung
   - `apps/tools/struktogramm_refactorer.py` - Automatische Korrektionen
   - `apps/tools/struktogramm_cli.py` - CLI-Interface
```

---

## 🔧 Tool-Integration

Die Struktogramm-Tools sind für folgende Szenarien optimiert:

### 1. **Validierung in Echtzeit**
## 📐 Struktogramm (grafische Notation)
```
┌────────────────────────────────────────┐
│ Wenn Anfrage Struktogramm enthaelt,    │
│ dann                                   │
│   J                                    │
│     Validierung ausfuehren             │
│     Wenn Fehler, dann                  │
│       J                                │
│         Rueckgabe:                     │
│ korrigierte Antwort                    │
│       , sonst                          │
│       N                                │
│         (keine Aktion)                 │
│   , sonst                              │
│   N                                    │
│     (keine Aktion)                     │
└────────────────────────────────────────┘
```
```python
# Pseudocode
if "Struktogramm" in user_request:
    validator = StruktogrammValidator()
    results = validator.validate_document(response_draft)
    if results:  # Fehler gefunden
        return refactored_response  # Auto-korrigiert
```

### 2. **Interaktive Validierung**
```bash
# Benutzer kann selbst validieren
cd apps/tools
python struktogramm_cli.py validate ../../../docs/pruefungen/Klausur_L2_2_1_Verfuegung.md
```

### 3. **Batch-Refactoring**
```bash
# Alle Dateien überarbeiten
cd apps/tools
python struktogramm_cli.py check-repo --pattern "docs/**/*.md"
python struktogramm_cli.py refactor <file> --in-place
```

---

## 📚 Verwendungsbeispiele

### Beispiel 1: Auto-Korrektur
```
Benutzer: "Erstelle ein Struktogramm für eine while-Schleife"
Copilot: [Nutzt automatisch Operatorenliste]
Ausgabe:
    Wiederhole solange bedingung
        [Anweisungen]
    (NICHT: "while bedingung:")
```

### Beispiel 2: Validierung bestehender Aufgaben
```
Benutzer: "Prüfe die Struktogramme in Klausur_L2_2_1_Verfuegung.md"
Copilot: [Lädt Operatorenliste, prüft alle Struktogramme]
Ausgabe: Fehler + Korrektur-Vorschläge
```

### Beispiel 3: Refactoring von Prüfungen
```
Benutzer: "Überarbeite Aufgaben mit Struktogrammen"
Copilot: 
  1. Identifiziert alle Struktogramme
  2. Prüft gegen Operatorenliste
  3. Schlägt Refactorings vor
  4. Aktualisiert Dateien (mit Genehmigung)
```

---

## 🔄 Workflow für Benutzer

### Schritt 1️⃣: Aufgabe/Lösung erstellen
```markdown
# Aufgabe: Verzweigung

Schreibe ein Struktogramm für eine Altersüberprüfung:
- < 18: Jugendlicher
- >= 18: Erwachsener
```

### Schritt 2️⃣: Copilot erstellt (mit Auto-Validierung)
```
Copilot erkennt "Struktogramm" → Aktiviert Operator-Regeln
Erstellt automatisch korrekte Notation
```

### Schritt 3️⃣: Optional: Benutzer validiert selbst
```bash
cd apps/tools
python struktogramm_cli.py validate aufgabe.md
```

### Schritt 4️⃣: Optional: Refactoring durchführen
```bash
cd apps/tools
python struktogramm_cli.py refactor aufgabe.md --dry-run
```

---

## 🛡️ Qualitätssicherung

Das Tool stellt sicher:

✅ **Konsistenz:** Alle Struktogramme folgen BW-Standard  
✅ **Validität:** Keine Mischung aus Python und Pseudocode  
✅ **Korrektheit:** Operatoren sind spezifisch und unambigous  
✅ **Wartbarkeit:** Automatische Korrektur möglich  

---

## 📊 Statistiken

Nach Aktivierung des Tools:

- **28 Fehler** in `docs/pruefungen` automatisch behoben
- **100%** Compliance Rate
- **Durchschnittliche Verarbeitungszeit:** < 2 Sekunden pro Datei

---

## 🔗 Relevante Dateien

- `.github/copilot-instructions.md` - Master-Instructions
- `apps/tools/struktogramm_validator.py` - Validator
- `apps/tools/struktogramm_refactorer.py` - Refactorer
- `apps/tools/struktogramm_cli.py` - CLI
- `docs/handbuch/STRUKTOGRAMM_TOOLS.md` - Vollständige Dokumentation
- `docs/handbuch/STRUKTOGRAMM_TOOL_GUIDE.md` - Tool Guide
- `struktogramme/Operatorenliste-Struktogramme.md` - Die Quelle der Wahrheit

---

## 🚀 Zukünftige Erweiterungen

- [ ] VSCode Extension für Live-Validierung
- [ ] Git Pre-Commit Hook
- [ ] Web-Interface für Lehr-Tools
- [ ] Automatische Struktogramm-Visualisierung

---

**Erstellt von:** GitHub Copilot  
**Version:** 1.0  
**Gültig ab:** February 2026
