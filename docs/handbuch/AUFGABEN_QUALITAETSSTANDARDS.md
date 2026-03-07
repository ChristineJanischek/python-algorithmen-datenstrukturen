# 🎓 AUFGABEN-QUALITÄTSSTANDARDS (ERWEITERT)

**Version:** 1.0 | **Datum:** 07.03.2026 | **Status:** Aktiv

---

## 🎯 Ziel

Dieses Dokument definiert die **Qualitätsstandards für alle Aufgaben** im E-Learning-System, um:
✅ Konsistente Struktur & Aufbau zu sichern
✅ Inhaltliche Varianz (keine Wiederholungen) zu garantieren  
✅ Automatische Code-Generierung für E-Learning zu ermöglichen
✅ Lehrkraftkompatibilität zu gewährleisten

---

## 1️⃣ STRUKTURSTANDARDS

### 1.1 Aufbau nach Klausur-Muster

**ALLE Aufgaben müssen folgende Struktur einhalten:**

```markdown
## 📝 Aufgabe X: [Titel]

### 📌 Übersicht
- Level, Kategorie, Punkte, Zeitaufwand, Schwierigkeit

### 📝 Problemstellung
- Kurzzusammenfassung
- Detaillierte Anforderungen (nummeriert)

### 📊 Teilaufgabe a) [Titel] (X Punkte)
- Anforderungen
- Struktogramm (falls nötig)
- Python-Code Block
- (optional: Text-Analyse)

### 📊 Teilaufgabe b), c), ...
- (Analog zu a)

### 💡 Hinweise
- Optionale Tipps

### 🧪 Beispiel/Testfall
- Eingabe
- Erwartete Ausgabe
- Erklärung

### ✅ Akzeptanzkriterien
- Checkliste für korrekte Lösung

```

### 1.2 Metadaten (YAML-Frontmatter)

**Alle Aufgaben müssen vollständig dokumentierte YAML-Header haben:**

```yaml
titel: "[Aussagekräftiger Titel]"
level: "L1" | "L2" | "L3"
kategorie: 1  # 1=Verzweigung, 2=Schleifen, 3=Arrays, 4=Sortieralgorithmen, 5=Suchalgorithmen, 6=Analyse
nummer: 1     # Laufend innerhalb Level + Kategorie
autor: "[Name]"
punkte:
  gesamt: 3
themen: ["Thema1", "Thema2"]
lernziele: ["Lernziel 1", "Lernziel 2"]
umfang:
  zeitaufwand_minuten: 5
  schwierigkeitsgrad: "Einfach" | "Mittel" | "Schwer"
```

---

## 2️⃣ INHALTLICHE VARIANZ-STANDARDS

### 2.1 **KEINE Wiederholungen** - Das Varianz-Prinzip

> ⚠️ **KRITISCH:** Jede Aufgabe zu einem Thema muss **inhaltlich unterschiedlich** sein, selbst wenn sie den gleichen Schwierigkeitsgrad haben.

#### Varianz-Dimensionen:

```
1. KONTEXT/SZENARIO:
   ❌ Falsch: 3x "Array durchlaufen und Summe berechnen"
   ✅ Richtig: 
      - Aufgabe 1: "Schätzungen von Läufern summieren"
      - Aufgabe 2: "Temperaturen eines Tages analys"
      - Aufgabe 3: "Rechnungsbeträge in Shop addieren"

2. DATENTYPEN:
   ❌ Falsch: Alle mit int
   ✅ Richtig: int, float, str, mixed

3. KOMPLEXITÄT (innerhalb Level):
   ❌ Falsch: Alle gleich komplex
   ✅ Richtig: Varianz in Voraussetzungen, Eingabegröße, etc.

4. ALGORITHMEN-VARIATION:
   ❌ Falsch: Alle mit while-Schleifen
   ✅ Richtig: while, for, verschachtelt, etc.

5. OUTPUT-FORM:
   ❌ Falsch: Alle mit "print" oder "return"
   ✅ Richtig: Verschiedene Output-Formate (Text, Zahl, Liste, etc.)
```

### 2.2 Varianz-Tracking-System

**Jede Aufgabe bekommt einen `inhaltliche_variation`-Block:**

```yaml
inhaltliche_variation:
  - "Kontext: Sportindex (Joggen)"
  - "Datentypen: int, str"
  - "Besonderheit: Mixed-Type Array"
  - "Algorithmus: for-Schleife mit Index"
  - "Output: Einzelne Ausgaben, keine Rückgabe"
```

**Vor dem Hochladen automatisch prüfen:**
- Gibt es bereits eine ähnliche Aufgabe mit gleichem Kontext?
- Unterscheiden sich Datentypen/Algorithmen ausreichend?
- Ist die Variation >= 3 Dimensionen?

---

## 3️⃣ PUNKTE & UMFANG-STANDARDS

### 3.1 Bepunktungsmuster (BW-konform)

```
Level L1 (Grundlagen):
├─ 3 Punkte (einfache Aufgabe): 1–5 Min
│  └─ 1–2 Teilaufgaben
├─ 6 Punkte (mittlere Aufgabe): 5–10 Min
│  └─ 2–3 Teilaufgaben
└─ 8 Punkte (umfangreiche Aufgabe): 10–15 Min
   └─ 3–4 Teilaufgaben

Level L2 (Fortgeschritten):
├─ 6 Punkte: 8–12 Min, 2 Teilaufgaben
├─ 7 Punkte: 10–15 Min, 3 Teilaufgaben
└─ 8 Punkte: 12–18 Min, 3–4 Teilaufgaben

Level L3 (Expert):
├─ 8 Punkte: 15–20 Min, 3 Teilaufgaben
└─ 10 Punkte: 20–25 Min, 4–5 Teilaufgaben
```

### 3.2 Gewichtung Struktogramm vs. Code

```
STRUKTURANFORDERUNGEN:

Nur Struktogramm:
├─ Theoretische Aufgaben (Analyse, "Was macht dieser Code?")
└─ Beispiel: "Finde den Fehler im Struktogramm" (3 Punkte)

Struktogramm + Code:
├─ Implementation von Logik
├─ Teilaufgabe a: Struktogramm (2–3 Punkte)
└─ Teilaufgabe b: Python-Code (1–2 Punkte)

Nur Code:
├─ Feine Implementierungsdetails
├─ Code-Optimierung
└─ Debug-Aufgaben
```

### 3.3 Zeitaufwand & Umfang

```
3 Punkte | 5 Min   | 1–2 Zeilen Code | 1 Konzept
6 Punkte | 10 Min  | 5–10 Zeilen Code | 2–3 Konzepte
7 Punkte | 12 Min  | 10–15 Zeilen Code | 3 Konzepte
8 Punkte | 15 Min  | 15–20 Zeilen Code | 3–4 Konzepte
```

**NICHT ÜBERSCHREITEN** - Schüler brauchen Zeit für alle Aufgaben.

---

## 4️⃣ STRUKTOGRAMM-STANDARDS

### 4.1 Unverzichtbar:

✅ **Struktogramm ist ERFORDERLICH, wenn:**
- Kontrollstrukturen (if, while, for) verlangt werden
- Algorithmen implementiert werden (Sortieren, Suchen)
- Logik analysiert wird
- Pseudo-Code gezeigt wird

### 4.2 Nicht nötig:

❌ **Kein Struktogramm bei:**
- Reinen Code-Style/Syntax-Fragen
- Variablenzugriffen
- Output-Formatierung

### 4.3 BW-Standard Einhaltung:

```
✅ IMMER verwenden:
- Operatorenliste aus: struktogramme/Operatorenliste-Struktogramme.md
- Textbasierte Notation (kein Draw.io in Aufgabe, nur wenn Optional)

✅ IMMER PRÜFEN:
- Sind alle Verzweigungen korrekt mit "dann J ... sonst N..." dargestellt?
- Sind Schleifen mit Zähler oder Bedingung gekennzeichnet?
- Ist die Verschachtelung erkennbar?
```

---

## 5️⃣ BEISPIELE & TESTFÄLLE-STANDARDS

### 5.1 Muss enthalten:

```
🧪 MINDESTENS ein Testfall mit:
├─ Klare Eingabe (Input)
├─ Erwartete Ausgabe (Output)
└─ Kurze Erklärung

💡 OPTIONAL: 2-3 weitere Testfälle für Edge Cases
```

### 5.2 Testfall-Qualität:

```
❌ FALSCH:
Eingabe: 5
Ausgabe: 5

✅ RICHTIG:
Eingabe:
```
5
3
2
-1
```
Ausgabe:
```
5
8
10
```
Erklärung: Programm summiert Eingaben bis zur Eingabe von -1
```

---

## 6️⃣ AUFGABEN-VERSIONEN MANAGEMENT

### 6.1 Versionsschema

```
Aufgabe Format: L{level}_{kategorie}_{nummer}_{version}

Beispiel:
├─ L1_3_001_v1.md (Erste Version)
├─ L1_3_001_v2.md (Überarbeitete Version - differenter Kontext)
└─ L1_3_002_v1.md (Nächste Aufgabe in Kategorie)

NICHT SO:
❌ L1_3_001_a.md
❌ L1_3_001_alt.md
❌ L1_3_001_neu.md
```

### 6.2 Varianz-Index System

**Für systematisches Tracking:**

```yaml
varianz_index: 1  # 0=erste Variante, 1=zweite, etc.
inhaltliche_variation:
  - "Kontext: Aktiendaten"
  - "Datentypen: float, list"
  - "Algorithmus: for-Schleife mit Bedingung"
```

---

## 7️⃣ PYTHON-CODE-STANDARDS

### 7.1 Anforderungen:

✅ **ALLE Codes müssen:**
```python
# 1. Type Hints haben
def funktion(parameter: List[int]) -> int:
    pass

# 2. Docstring (Google-Style)
"""
Kurze Beschreibung.
    
Args:
    parameter: Beschreibung
    
Returns:
    Beschreibung des Rückgabewertes
"""

# 3. Aussagekräftige Variablennamen (deutsch OK)
summe = 0
fuer_index in range(10):
    summe += zahlen[index]

# 4. Kommentare bei komplexer Logik
# Tausch nur wenn links > rechts
if zahlen[i] > zahlen[i+1]:
    zahlen[i], zahlen[i+1] = zahlen[i+1], zahlen[i]
```

### 7.2 Was NICHT erlaubt:

```python
❌ sorted(arr)  # Schüler sollen selbst sortieren!
❌ import numpy  # Keine Extended Libraries für Grundaufgaben
❌ arr[::-1]    # Zu "magisch" für Anfänger
```

---

## 8️⃣ ANALYSE-AUFGABEN-STANDARDS

### 8.1 Struktur Fehleranalyse:

```
**a) Vermuter Zweck (3 Punkte):**
"Was soll dieser Algorithmus tun?"
→ Offene Frage, 2-4 Sätze

**b) Fehleridentifikation (3 Punkte):**
"Nenne den logischen Fehler"
→ Konkrete Fehlerposition angeben

**c) Korrekturvorschlag (2 Punkte):**
"Wie würde die korrekte Zeile lauten?"
→ BW-konforme Notation
```

### 8.2 Qualitätskriterien:

```
✅ Der Fehler muss:
- Pädagogisch wertvoll sein (häufiger Anfängerfehler)
- Nicht trivial erkennbar sein
- Logische Konsequenzen haben (nicht nur Syntaxfehler)
```

---

## 9️⃣ INTEGRATION MIT E-LEARNING-SYSTEM

### 9.1 Automatische Generierung:

```python
# Das System generiert automatisch aus Template:
├─ E-Learning-ID
├─ Komponenten-Referenzen
├─ Varianz-Hashes
├─ Validation-Status
└─ Einbettungs-Codes
```

### 9.2 Validierungs-Checkliste:

```
Vor dem Speichern prüfen:
☐ YAML-Header vollständig?
☐ Alle Themen definiert?
☐ Lernziele aktiv formuliert?
☐ Punkte = Summe Teilaufgaben?
☐ Inhaltliche Varianz >= 3 Dimensionen?
☐ Keine ähnliche Aufgabe bereits vorhanden?
☐ Struktogramme BW-konform?
☐ Code-Beispiele ausführbar?
☐ Testfälle plausibel?
```

---

## 🔟 RESSOURCEN-SYSTEM

### 10.1 Resource-Directory-Struktur

```
resources/
├── python_samples/          # Python-Dateisammlung (Idea-Feed)
│   ├── algorithmen/
│   │   ├── sortieren/
│   │   ├── suchen/
│   │   └── ...
│   └── datenstrukturen/
├── aufgaben_ideen/          # Aufgabenkonzepte (vor Formalisierung)
│   └── {Lehrkraft}_YYYY_MM_DD/
├── varianz_tracker.json     # Tracking: Aufgaben + Varianz
└── validation_reports/      # Validierungsergebnisse
```

### 10.2 Idea-Feed-Integration

```
Workflow:
1. Lehrkraft lädt .py-Dateien hoch → resources/python_samples/
2. System indiziert automatisch (Funktionen, Variablen, Themen)
3. Varianz-Tracker prüft: "Kann hier eine neue Aufgabe entstehen?"
4. Copilot nutzt als Kontext für Aufgabengenerierung
```

---

## 1️⃣1️⃣ GUI-UPLOAD-KOMPONENTEN SPEZIFIKATION

### 11.1 Zukünftige Lehrkraft-GUI:

```
📦 Upload-Komponente:
│
├─ Datei-Auswahl (Aufgabe/Lösung/Projekt/Resource)
├─ Metadaten-Formular:
│  ├─ Titel
│  ├─ Level / Kategorie
│  ├─ Punkte
│  ├─ Themen (Multi-Select)
│  ├─ Lernziele
│  └─ Inhaltliche Besonderheiten
├─ Varianz-Check-Engine:
│  └─ "Diese Aufgabe ist zu ähnlich zu [Aufgabe XYZ]"
├─ Preview-Renderer:
│  └─ Struktogramme + Markdown live
└─ Publish-Button:
   └─ → Validierung → E-Learning-Indizierung
```

### 11.2 API-Struktur (vorbereitet):

```python
# Zukünftige API-Endpoints:

POST /api/v1/resources/upload
├─ file: Multipart
├─ metadata: JSON
└─ type: "aufgabe" | "loesung" | "projekt"

GET /api/v1/aufgaben/varianz-check?title=...&level=L1&kategorie=3
└─ Response: Ähnliche Aufgaben + Varianz-Score

POST /api/v1/aufgaben/validate
├─ file: Markdown
└─ Response: Validierungsbericht

GET /api/v1/aufgaben/index
└─ Response: Alle Aufgaben mit Metadaten + Varianz-Info
```

---

## 🎯 IMPLEMENTIERUNGS-ROADMAP

### Phase 1: JETZT (März 2026)
- ✅ Template etablieren
- ✅ Qualitätsstandards dokumentieren
- ✅ Varianz-Tracking-System vorbereiten
- ✅ Validierungs-Tools erstellen

### Phase 2: BALD (April 2026)
- Resource-Directory aufbauen
- Python Indexer implementieren
- Automatic Varianz-Check Engine
- Copilot-Integration erweitern

### Phase 3: SPÄTER (Mai+ 2026)
- GUI-Upload-Komponente bauen
- API-Endpoints implementieren
- Lehrkraft-Dashboard entwickeln

---

## 📞 Fragen & Rückmeldungen

Kontakt: [E-Mail Lehrkraft]

**Viel Erfolg beim Aufgabenerstellen! 🚀**
