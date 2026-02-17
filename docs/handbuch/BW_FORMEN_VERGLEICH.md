# BW-Standard Struktogramm-Formen: Vergleich

## Übersicht der korrekten Baden-Württemberg Abitur-Formen

Dieses Dokument zeigt die **korrekten SVG-Implementierungen** der BW-Standard Struktogramm-Formen nach der Operatorenliste.

---

## 1. Anweisung (Einfache Rechteck-Form)

### ✅ KORREKT (BW-Standard):

```
┌──────────────────────────────────┐
│ Bezeichnung:                     │  ← Label in Zeile 1 (klein, grau)
│ variable = wert                  │  ← Formulierung (normal)
└──────────────────────────────────┘
```

**SVG-Code:**
```xml
<rect x="50" y="80" width="600" height="50" class="box"/>
<text x="60" y="98" class="text label">Anweisung:</text>
<text x="60" y="115" class="text">variable = wert</text>
```

**Bezeichnungen:**
- `Deklaration:` für `variable |als datentyp|`
- `Initialisierung:` für `variable = wert`
- `Zuweisung:` für `x = ...`
- `Einlesen:` für Eingabe von Variablen
- `Ausgabe:` für Textausgabe
- `Rückgabe:` für Return-Statements

**Beispiele:**
- `Deklaration: alter |als Ganzzahl|`
- `Zuweisung: summe = summe + zahl`
- `Einlesen: name |als Text|`
- `Ausgabe: Hallo Welt`

---

## 2. Alternative (Briefumschlag-Form)

### ✅ KORREKT (BW-Standard):

**Beschreibung:** Rechteckige Gesamtform mit eingebettetem gleichschenkligem Dreieck (Hypotenuse oben, Spitze nach unten). Das Dreieck enthält die Bedingung. Darunter zwei Bereiche: Ecke links unten mit "J" (Ja-Zweig), Ecke rechts unten mit "N" (Nein/Sonst-Zweig).

```
┌─────────────────────────────────┐
│╲                               ╱│
│ ╲         Bedingung           ╱ │  ← Gleichschenkliges Dreieck
│  ╲                           ╱  │     (Hypotenuse oben)
│   ╲                         ╱   │
│    ╲_______________________╱    │     (Spitze unten)
│        │                │        │
│   J    │                │   N    │  ← J/N in Ecken unten
│        │                │        │
│  Dann  │                │  Sonst │
│        │                │        │
└────────┴────────────────┴────────┘
```

**SVG-Code:**
```xml
<!-- Äußeres Rechteck (Gesamtform) -->
<rect x="50" y="130" width="600" height="120" class="box"/>

<!-- Eingebettetes Dreieck (Hypotenuse oben, Spitze unten) -->
<polygon points="50,130 650,130 350,170" fill="#fff" stroke="#000" stroke-width="2"/>

<!-- Bedingung im Dreieck -->
<text x="350" y="150" class="text" text-anchor="middle">bedingung</text>

<!-- Vertikale Trennlinie (Mitte) -->
<line x1="350" y1="170" x2="350" y2="250" stroke="#000" stroke-width="2"/>

<!-- J in Ecke links unten -->
<text x="60" y="185" class="text bold">J</text>

<!-- N in Ecke rechts unten -->
<text x="360" y="185" class="text bold">N</text>
```

**Form:** Rechteck mit eingebettetem Dreieck (Spitze nach unten), zwei Felder darunter

**Beispiele:**
- `alter < 18` → J: Jugendlicher | N: Erwachsener
- `zahl % 2 = 0` → J: Gerade | N: Ungerade

---

## 3. Schleife (Umgedrehtes L, gespiegelt)

### ✅ KORREKT (BW-Standard - While):

```
┌──────────────────────────────────┐
│ Wiederhole solange bedingung     │  ← Kopf
├──────────────────────────────────┤
│ │ Anweisung 1                    │  ← Körper eingerückt
│ │ Anweisung 2                    │
│ │ Anweisung 3                    │
└─┴────────────────────────────────┘
  ↑
  Vertikale Linie links
```

**SVG-Code:**
```xml
<!-- Schleifenkopf -->
<rect x="50" y="180" width="600" height="40" class="box"/>
<text x="60" y="205" class="text">Wiederhole solange zahl != -1</text>

<!-- Vertikale Linie links (L-Form) -->
<line x1="50" y1="220" x2="50" y2="370" stroke="#000" stroke-width="2"/>

<!-- Körper (eingerückt um 20px) -->
<rect x="70" y="220" width="580" height="50" class="box"/>
<text x="80" y="245" class="text">summe = summe + zahl</text>

<!-- Abschlusslinie -->
<line x1="50" y1="370" x2="650" y2="370" stroke="#000" stroke-width="2"/>
```

### ✅ KORREKT (BW-Standard - For):

```
┌──────────────────────────────────┐
│ Zähle i von 0 bis n, Schrittweite 1  │  ← Kopf
├──────────────────────────────────┤
│ │ Anweisung 1                    │
│ │ Anweisung 2                    │
└─┴────────────────────────────────┘
```

**Form:** Umgedrehtes L (gespiegelt horizontal)
- Vertikale Linie links
- Kopf oben horizontal
- Körper eingerückt (rechts der vertikalen Linie)

**Beispiele:**
- `Wiederhole solange i < 10` (While)
- `Zähle i von 0 bis n-1, Schrittweite 1` (For)

---

## 4. Funktionsaufruf (Rechteck mit vertikalen Strichen)

### ✅ KORREKT (BW-Standard):

```
│┌────────────────────────────────┐│
││ Aufruf: funktionsname(param)   ││  ← Vertikale Striche außen
│└────────────────────────────────┘│
```

**SVG-Code:**
```xml
<!-- Hauptrechteck -->
<rect x="50" y="100" width="600" height="50" class="box"/>

<!-- Vertikale Striche links -->
<line x1="60" y1="100" x2="60" y2="150" stroke="#000" stroke-width="2"/>

<!-- Vertikale Striche rechts -->
<line x1="640" y1="100" x2="640" y2="150" stroke="#000" stroke-width="2"/>

<!-- Text -->
<text x="325" y="130" class="text" text-anchor="middle">Aufruf: sortiere(array)</text>
```

**Form:** Normales Rechteck + vertikale Linien links und rechts

**Beispiele:**
- `Aufruf: berechne_summe(zahlen)`
- `Aufruf: sortiere(array, n)`

---

## Komplexes Beispiel: Bubble Sort

Kombiniert alle Formen:

```
┌────────────────────────────────────────┐
│ Deklaration: temp |als Ganzzahl|       │  ← Anweisung
└────────────────────────────────────────┘
┌────────────────────────────────────────┐
│ Zähle i von 0 bis n-1, Schrittweite 1  │  ← Äußere For-Schleife (L)
├────────────────────────────────────────┤
│ │┌───────────────────────────────────┐│
│ ││ Zähle j von 0 bis n-i-1, ...      ││  ← Innere For-Schleife (L)
│ │├───────────────────────────────────┤│
│ ││ │      ╱─────────────────╲        ││
│ ││ │     ╱  zahlen[j] >      ╲       ││  ← Alternative (Briefumschlag)
│ ││ │    ╱   zahlen[j+1]?      ╲      ││
│ ││ │   ╱_______________________╲     ││
│ ││ │  │    J    │      N        │    ││
│ ││ │  │Tauschen │   (nichts)    │    ││
│ ││ │  └─────────┴───────────────┘    ││
│ │└─┴─────────────────────────────────┘│
└─┴─────────────────────────────────────┘
```

**Siehe:** [L2_6_Aufgabe6_Bubble_Sort.svg](../../struktogramme/generated/svg/L2_6_Aufgabe6_Bubble_Sort.svg)

---

## Vergleich ALT (falsch) vs. NEU (korrekt)

### ❌ ALTE VERSION (Nicht BW-konform):

| Element | Alte Form | Problem |
|---------|-----------|---------|
| Anweisung | Einfaches Rechteck | Keine Label-Zeile |
| Alternative | Diamant (Raute) ◇ | Falsche Form (soll Briefumschlag sein) |
| Schleife | Abgerundetes Rechteck | Keine L-Form, keine Einrückung |
| Funktionsaufruf | Normales Rechteck | Keine vertikalen Striche |

### ✅ NEUE VERSION (BW-konform):

| Element | Neue Form | BW-Standard |
|---------|-----------|-------------|
| Anweisung | Rechteck mit "Label:" + Text | ✅ |
| Alternative | Briefumschlag (Dreieck + 2 Seiten) | ✅ |
| Schleife | Umgedrehtes L (vertikale Linie + Einrückung) | ✅ |
| Funktionsaufruf | Rechteck mit ││ Strichen ││ | ✅ |

---

## Verwendung im Repository

**Alle generierten SVGs** verwenden jetzt die korrekten BW-Formen:

```bash
# Einzelne Konvertierung
python3 struktogramme/converter/struktogramm_xml_renderer.py input.xml output.svg

# Batch-Konvertierung
for xml in struktogramme/xml_definitions/L2_sortieren/*.xml; do
    python3 struktogramme/converter/struktogramm_xml_renderer.py "$xml" \
        "struktogramme/generated/svg/$(basename "$xml" .xml).svg"
done
```

**Pre-commit Hook:** Automatische Generierung bei `git commit`

**Siehe auch:**
- [Operatorenliste-Struktogramme.md](../../struktogramme/Operatorenliste-Struktogramme.md) - Vollständige BW-Standards
- [STRUKTOGRAMM_GUIDE.md](STRUKTOGRAMM_GUIDE.md) - Praktischer Guide
- [STRUKTOGRAMM_XML_GUIDE.md](STRUKTOGRAMM_XML_GUIDE.md) - XML-Format Dokumentation

---

## Technische Details

### SVG-Konfiguration (BW-Standard):

```python
@dataclass
class SVGConfig:
    WIDTH: int = 700
    HEIGHT: int = 1200
    BOX_WIDTH: int = 600
    BOX_HEIGHT: int = 50
    MARGIN_TOP: int = 80
    MARGIN_LEFT: int = 50
    FONT_SIZE: int = 13
    LINE_SPACING: int = 18
    STROKE_WIDTH: int = 2
    
    # Spezielle Höhen
    DECISION_TRIANGLE_HEIGHT: int = 40  # Briefumschlag-Dreieck
    DECISION_BODY_HEIGHT: int = 80       # Zweig-Körper
    LOOP_HEADER: int = 40                # Schleifenkopf
    
    INDENT: int = 20  # Einrückung für Schleifenkörper (L-Form)
```

### Renderer-Methoden:

```python
class BWStruktogrammRenderer:
    def _render_anweisung(element, typ, x, width)
        # Rechteck mit "Bezeichnung:" + Text
        
    def _render_alternative(element, x, width)
        # Briefumschlag: <polygon> für Dreieck + 2 Seiten
        
    def _render_while_schleife(element, x, width)
        # Umgedrehtes L: Vertikale Linie + eingerückter Körper
        
    def _render_for_schleife(element, x, width)
        # Umgedrehtes L: "Zähle ... von ... bis ..."
        
    def _render_funktionsaufruf(element, x, width)
        # Rechteck + <line> links und rechts
```

---

## Qualitätskontrolle

**Checklist für BW-Konformität:**

- [x] Anweisungen haben Label + Doppelpunkt in Zeile 1
- [x] Alternative verwendet Polygon (Dreieck/Briefumschlag)
- [x] Schleifen haben vertikale Linie links (L-Form)
- [x] Schleifenkörper ist eingerückt (20px)
- [x] Funktionsaufrufe haben vertikale Striche ││
- [x] Alle Formulierungen entsprechen Operatorenliste
- [x] Verschachtelte Strukturen korrekt dargestellt

**Getestet mit:**
- ✅ 9 Exam-Aufgaben (L2_1 bis L2_6)
- ✅ Einfache Verzweigungen
- ✅ While-Schleifen
- ✅ For-Schleifen
- ✅ Verschachtelte Schleifen (Bubble Sort)
- ✅ Komplexe Kombinationen

---

**Status:** ✅ VOLLSTÄNDIG IMPLEMENTIERT (Stand: 05.02.2026)

**Renderer:** `struktogramme/converter/struktogramm_xml_renderer.py` (460 Zeilen)

**Migration:** 9/9 Exam-Aufgaben erfolgreich mit BW-Formen generiert

---

*Letzte Aktualisierung: 05.02.2026*
*Version: 2.0 (BW-konform)*
