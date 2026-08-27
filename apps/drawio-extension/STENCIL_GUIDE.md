# Struktogramm Stencil System - Technische Dokumetation

**Version:** 0.1.0  
**Created:** 18.02.2026  
**File:** `stencil.xml`

---

## 📋 Überblick

Das Struktogramm **Stencil System** ist die Brücke zwischen deinen strukturalen Definitionen und Draw.io.

Ein **Stencil** ist eine XML-Datei, die für mxGraph (die Engine von Draw.io) definiert:
1. **Welche Shapes zeichnbar sind** (Rechteck, Raute, etc.)
2. **Ihre visuellen Eigenschaften** (Farbe, Größe, Formen)
3. **Wie sie in der Palette angezeigt werden** (Kategorien, Icons)

---

## 🎨 **Die 4 BW-Standard Formen**

### 1. **Anweisung** (Rechteck)
```
┌─────────────────┐
│   variable = w  │
└─────────────────┘
```
- **XML-Name:** `<shape name="Anweisung">`
- **Bedeutung:** Einfache Verarbeitung, Zuweisungen
- **Größe Default:** 120x60 Pixel
- **Farbe:** Weiß (#ffffff)
- **Umrandung:** Schwarz 2px

**Verwendung:**
```
Zuweisung: summe = 0
Ausgabe: cout << x
Funktionsaufruf: print(text)
```

---

### 2. **Alternative** (Raute + Rechtecke)
```
      wenn bedingung
          ◊
         / \
        J   N
       /     \
      □       □
```
- **XML-Name:** `<shape name="Alternative">`
- **Bedeutung:** Verzweigung (if-then-else)
- **Größe Default:** 120x80 Pixel
- **Farbe:** Gelb (#ffffcc) - signalisiert Entscheidung
- **Label:** `J` (Ja) und `N` (Nein) für die zwei Äste

**Verwendung:**
```
wenn a > b, dann
    ...
, sonst
    ...
```

---

### 3. **While-Schleife** (Umgedrehtes L)
```
┌──────────────────┐
│ Wiederhole solange │
│    i < 10        │
├──────────────────┤
│                  │
│  Körper der      │
│  Schleife        │
│                  │
└──────┬───────────┘
       └──> (zurück zum Kopf)
```
- **XML-Name:** `<shape name="While">`
- **Bedeutung:** Wiederholung mit Bedingungsprüfung oben
- **Größe Default:** 120x100 Pixel
- **Farbe:** Hellgelb (#ffffcc) - Bedingung
- **Struktur:** 2 Teile (Kopf + Körper)

**Verwendung:**
```
Wiederhole solange summe < 100
    summe = summe + 1
    index = index + 1
```

---

### 4. **For-Schleife** (Variant mit Zähler)
```
┌──────────────────────┐
│ Zähle i von 1 bis 10 │
├──────────────────────┤
│                      │
│  Körper der          │
│  Schleife            │
│                      │
└──────┬───────────────┘
       └──> (i = i + 1)
```
- **XML-Name:** `<shape name="For">`
- **Bedeutung:** Zählschleife mit festem Start/Ende
- **Größe Default:** 140x100 Pixel
- **Farbe:** Hellgrün (#ccffcc) - unterscheidet sich von While
- **Struktur:** 2 Teile (Kopf mit Zähler + Körper)

**Verwendung:**
```
Zähle i von 1 bis länge(array)
    element = array[i]
    summe = summe + element
```

---

## 🏷️ **Die 7 Instruction Types**

Alle 7 sind **Spezialisierungen der "Anweisung"** (Rechteck), unterscheiden sich aber durch:
- **Farb-Coding** - schnell visuell erkennbar
- **Form-Variationen** - schräge Kanten für I/O
- **Icons/Symbole** - (später in Phase 2-B)

### Farb-Schema:

| Typ | Farbe | Hex | Bedeutung |
|-----|-------|-----|-----------|
| **Deklaration** | Hellblau | #e8f4f8 | Neue Variable |
| **Initialisierung** | Blau | #dceefb | Deklaration + Wert |
| **Einlesen** | Grün | #d4edda | Input von außen |
| **Zuweisung** | Weiß | #ffffff | Normale Zuweisung |
| **Ausgabe** | Gelb | #fff3cd | Output nach außen |
| **Rückgabe** | Rot | #f5d4d4 | Return-Statement |
| **FunktionsAufruf** | Lila | #e8d5e8 | Aufruf einer Funktion |

---

## 📊 **XML-Struktur erklärt**

### Basis-Aufbau:

```xml
<shape name="Anweisung" description="Einfache Anweisung">
  <description>
    Erklärender Text für Entwickler
  </description>
  
  <connections>
    <!-- Definiert Verbindungspunkte -->
    <constraint name="perimeter" type="perimeter"/>
  </connections>
  
  <background w="120" h="60">
    <!-- VISUELLER AUFBAU: Formen & Pfade -->
    <path data="M 0 0 L 120 0 L 120 60 L 0 60 Z" 
          stroke="#000000" 
          strokewidth="2" 
          fill="#ffffff"/>
  </background>
  
  <foreground w="120" h="60">
    <!-- TEXT & LABELS -->
    <text x="60" y="30" ...>
      <mxCell style="..."/>
    </text>
  </foreground>
</shape>
```

### Element-Erklärung:

| Element | Bedeutung |
|---------|-----------|
| `<shape>` | Definition eines neuen Shapes |
| `name` | Eindeutige ID (wird in Draw.io angezeigt) |
| `description` | Kurzbeschreibung |
| `<background>` | Wie wird die Form gezeichnet |
| `<path>` | SVG-Pfad (M=Move, L=Line, Z=Close) |
| `stroke` | Umriss-Farbe (#000000 = schwarz) |
| `strokewidth` | Dicke der Linie (2px) |
| `fill` | Füll-Farbe (#ffffff = weiß) |
| `<foreground>` | Text/Labels die oben zeichnen |

---

## 🔄 **SVG-Pfade verstehen**

Beispiel: Rechteck zeichnen

```
<path data="M 0 0 L 120 0 L 120 60 L 0 60 Z" />
```

**Kommandos:**
- `M 0 0` = **M**ove to (0, 0) - Startpunkt
- `L 120 0` = **L**ine to (120, 0) - Linie oben
- `L 120 60` = Linie rechts
- `L 0 60` = Linie unten  
- `Z` = Close path (automatisch zurück zum Start)

**Resultat:**
```
(0,0) ├─(120,0)
  ├─────┤
  │     │
(0,60)─┤(120,60)
```

---

## 🎨 **Farb-Kodierung - Best Practice**

Die Farben sind **nicht zufällig**:

- **Blautöne** (#e8f4f8, #dceefb) = Datenstrukturen (Deklaration)
- **Grün** (#d4edda) = Input (kommt von außen)
- **Weiß** (#ffffff) = Standard/Neutral
- **Gelb** (#fff3cd) = Output/Warnung  
- **Rot** (#f5d4d4) = Rückkehr/Ende
- **Lila** (#e8d5e8) = Spezial (Funktionsaufruf)

das ist **Color Coding nach Semantik** - sehr professionell!

---

## 🔧 **Wie Draw.io diese Stencils nutzt**

### Workflow:

```
1. User lädt Extension in Draw.io
        ↓
2. Extension lädt stencil.xml
        ↓
3. Draw.io parsed die <shape> Elemente
        ↓
4. Palette zeigt alle Formen
        ↓
5. User zieht Shape in Canvas
        ↓
6. Draw.io zeichnet es via <background> + <foreground>
        ↓
7. User kann Text editieren (wird in <foreground> <text> angezeigt)
```

---

## 📝 **Anpassungen & Erweiterungen**

### Shape-Größe ändern:

```xml
<!-- Default: 120x60 -->
<shape name="Anweisung" ...>
  <background w="200" h="80">  <!-- ← Neue Größe -->
    ...
  </background>
</shape>
```

### Neue Farbe:

```xml
<!-- von white (#ffffff) zu lightblue (#e3f2fd) -->
<path data="..." fill="#e3f2fd" />
```

### Neuer Instruction Type:

```xml
<shape name="Assertion" description="Debug-Assertion">
  <background w="120" h="60">
    <path data="M 0 0 L 120 0 L 120 60 L 0 60 Z" 
          stroke="#000000" 
          strokewidth="2" 
          fill="#ff9999"/>  <!-- Dunkelrot für Fehler -->
  </background>
</shape>
```

---

## ✅ **Phase 2-A Checkliste**

- [x] stencil.xml mit 4 BW-Formen
- [x] 7 Instruction Types mit Farb-Kodierung
- [x] Start/Ende Helper Shapes
- [x] Detaillierte Dokumentation (diese Datei)
- [ ] Plugin.js implementiert (Phase 2-B)
- [ ] In Draw.io getestet (Phase 2-C)

---

## 📚 **Nächste Schritte**

### Phase 2-B (Morgen):
1. plugin.js schreiben (lädt stencil.xml)
2. Palette loader implementieren
3. Event handlers für Shape-Erstellung

### Phase 2-C (Später):
1. In lokaler Draw.io testen
2. Shape-Rendering debuggen
3. Interaktion testen

---

## 🔗 **Referenzen**

- **mxGraph Stencils:** https://github.com/jgraph/drawio/tree/master/src/main/webapp/stencils
- **SVG Paths:** https://www.w3.org/TR/SVG/paths.html
- **Draw.io Plugin Docs:** https://desk.draw.io/support/solutions/articles/16000042544-

---

**Erstellt:** 18.02.2026  
**Status:** ✅ Phase 2-A COMPLETE

<!-- CUSTOM_LICENSE_NOTICE_START -->
## License

This repository is licensed under a custom license.

- Attribution required: Christine Janischek - https://emotionalspirit.de
- Non-commercial use only
- Use only within state school systems
- Any other use requires explicit prior written permission
<!-- CUSTOM_LICENSE_NOTICE_END -->
