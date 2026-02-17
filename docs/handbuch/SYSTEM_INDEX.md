# System Index - Zentrale Dokumentation

**Stand:** 2026-02-06

Dieses Dokument bietet einen Überblick über alle zentralen Systemroutinen, Dokumentationen und Guides im Repository.

---

## 📖 Handbücher & Dokumentation

### Kernhandbücher
| Dokument | Beschreibung | Zielgruppe |
|----------|-------------|-----------|
| [CONTRIBUTOR_ONBOARDING.md](CONTRIBUTOR_ONBOARDING.md) | **PFLICHT:** Schritt-für-Schritt Anleitung für neue Contributor (Git, Setup, Strukturogramme, etc.) | **Alle neuen Contributor** |
| [STRUKTOGRAMM_GUIDE.md](STRUKTOGRAMM_GUIDE.md) | Praktischer Guide zu Struktogrammen nach Baden-Württemberg-Abitur-Standard | Tutoren, Content-Ersteller |
| [ELEARNING_TEMPLATE_GUIDE.md](ELEARNING_TEMPLATE_GUIDE.md) | Anleitung für das E-Learning Content Management System | Administratoren, Content-Manager |
| [ROUTINEN.md](ROUTINEN.md) | Vollständige Übersicht aller System- und Anwendungsroutinen | Entwickler, Administratoren |
| [BACKUP_STRATEGY.md](BACKUP_STRATEGY.md) | Versionierungs- und Backup-Strategien für verlässliche Releases | DevOps, Administratoren |
| [ARCHITECTURE.MD](ARCHITECTURE.MD) | Systemarchitektur und technische Übersicht | Entwickler |
| [DEVELOPMENT.MD](DEVELOPMENT.MD) | Entwicklungs-Richtlinien und Setup | Entwickler |

---

## 🔧 Systemroutinen

### Python-Utilities (src/utils/)

#### **struktogramm_helper.py**
Hilfsfunktionen für die Stroktogramm-Erstellung nach BW-Standard:
- `StruktogrammValidator` - Validierung von Struktogrammen
- `StruktogrammRenderer` - Rendering von Box-, Branch-, Loop-Strukturen
- `StruktogrammBuilder` - Fluent-API zum Erstellen von Struktogrammen
- Patterns: `pattern_array_durchlaufen()`, `pattern_summe_berechnen()`, `pattern_maximum_finden()`, `pattern_lineare_suche()`

**Verwendung:** Content-Erstellung, Aufgabenentwicklung

#### **elearning_manager.py**
Zentrales Content-Management-System für E-Learning-Inhalte:
- `ELearningManager` - Verwaltung von Aufgaben, Informationen und Lösungen
- `create_aufgabe_quick()` - Schnell-API für Aufgabenerstellung
- `create_information_quick()` - Schnell-API für Informationserstellung
- `create_loesung_quick()` - Schnell-API für Lösungserstellung
- Automatische Index-Generierung

**Verwendung:** E-Learning Content Management, Publikation von Lernmaterialien

#### **version_manager.py**
Verwaltung von Versionsinformationen und Release-Metadaten

**Verwendung:** Versionskontrolle, Release-Management

### API-Anwendungen (apps/api/)

#### **main.py**
REST-API für E-Learning-Zugriff:
- `health_check()` - System-Status
- `list_themes()` - Verfügbare Themen
- `list_milestones()` - Meilensteine abrufen
- `get_milestone()` - Meilenstein-Details
- `list_tasks()` - Aufgaben auflisten
- `get_operatorenliste()` - Operatoren-Referenz

#### **data_loader.py**
Daten-Loader für Konfiguration und Inhalte:
- `load_json()` - JSON-Dateien laden
- `load_text()` - Text-Dateien laden

### Tools & Skripte (apps/tools/)

#### **generate_information_docs.py**
Code-Analyser und Dokumentations-Generator:
- `analyze_py()` - Python-Dateien analysieren
- `analyze_text()` - Text-Dateien analysieren
- `make_md_for_file()` - Markdown-Dokumentation generieren

---

## 📦 Verzeichnisstruktur

```
docs/handbuch/                 ← ZENTRALE DOKUMENTATION
├── STRUKTOGRAMM_GUIDE.md      (BW-Standard Guide)     
├── ELEARNING_TEMPLATE_GUIDE.md (Content Management)   
├── ROUTINEN.md                (Diese Übersicht)       
├── BACKUP_STRATEGY.md         (Versionierung)         
├── SYSTEM_INDEX.md            (↑ Sie sind hier)       
└── *.MD                       (weitere Handbücher)    

src/utils/                      ← PYTHON UTILITIES     
├── struktogramm_helper.py                             
├── elearning_manager.py                               
└── version_manager.py                                 

apps/api/                       ← REST-API             
├── main.py                                            
└── data_loader.py                                     

apps/tools/                     ← SKRIPTE & TOOLS      
└── generate_information_docs.py                       

docs/aufgaben/                  ← LERNMATERIALIEN      
docs/loesungen/                                        
docs/information/                                      

struktogramme/                  ← STRUKTOGRAMM-DATEIEN 
└── *.stgr                                             
```

---

## 🚀 Häufige Workflows

### Neue Aufgabe erstellen
```python
from src.utils.elearning_manager import create_aufgabe_quick, Level

aufgabe = create_aufgabe_quick(
    titel="Bubble Sort Implementierung",
    level=Level.L2,
    kategorie=2,
    nummer=1,
    problemstellung="Implementiere einen Bubble-Sort-Algorithmus...",
    autor="Ihr Name"
)
aufgabe.metadata.themen = ["Sortieren", "Arrays"]
manager.save_aufgabe(aufgabe)
```

### Struktogramm validieren
```python
from src.utils.struktogramm_helper import StruktogrammValidator

validator = StruktogrammValidator()
errors = validator.validate_struktogramm(lines)
```

### Index neu generieren
```python
from src.utils.elearning_manager import ELearningManager

manager = ELearningManager()
manager.generate_all_indices()
```

---

## 📋 Kategorien (Nummern)

- **1** = Grundlagen
- **2** = Sortieralgorithmen
- **3** = Suchalgorithmen
- **4** = Vertiefung / Spezial

## 📊 Level-Definition

- **L1** = Grundlagen (Sequenz, einfache Verzweigungen/Schleifen)
- **L2** = Fortgeschritten (Arrays, Such-/Sortieralgorithmen)
- **L3** = Expert (Komplexe Datenstrukturen, Rekursion)

---

## 🔗 Wichtige Links

- **Copilot-Anweisungen**: [.github/copilot-instructions.md](../../.github/copilot-instructions.md)
- **Operatorenliste**: [struktogramme/Operatorenliste-Struktogramme.md](../../struktogramme/Operatorenliste-Struktogramme.md)
- **Repository-Root**: [/]( /)

---

*Diese Datei dient als zentrales Navigationsdokument für alle Systemroutinen und Dokumentationen.*
