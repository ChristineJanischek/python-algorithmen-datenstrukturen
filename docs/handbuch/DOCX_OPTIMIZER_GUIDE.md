# DOCX Markdown Optimizer - Dokumentation

## 📋 Überblick

Das **DOCX Markdown Optimizer** System optimiert Markdown-Dokumente für den Export nach DOCX-Format (Microsoft Word). Es wurde entwickelt, um speziell die Anforderungen von Klassenarbeits- und Prüfungsdokumenten zu adressieren.

**Status:** Produktionsreif | **Version:** 1.0 | **Letzte Aktualisierung:** 2026-03-03

---

## 🎯 Hauptmerkmale

### 1. **Struktogramm-Optimierung**
- Fügt DOCX-Metadaten-Kommentare zu SVG-Struktogrammen hinzu
- Stellt sicher, dass SVG-Dateien bei DOCX-Export korrekt eingebettet werden
- Verbessert die Kopierbarkeit von Struktogrammen (STRG+C)

### 2. **Code-Block-Styling**
- Definiert Farbschema für Python-Code-Blöcke
- Hintergrund: `#F2F2F2` (Hellgrau) für hohen Kontrast
- Text: `#111111` (Dunkelgrau) für Lesbarkeit
- Rahmen: `#C8C8C8` (Mittleres Grau) für Definition

### 3. **Footer-Versionierung**
- Verschiebt Versionsinformationen aus dem Dokumentbody in die Fußzeile
- Hält Dokumente sauberer und professioneller
- Ermöglicht einfache Versionsverwaltung

### 4. **Erweiterbar durch Design**
- Plugin-Architektur mit `BaseOptimizer` Klasse
- Einfach neue Optimizer hinzufügen
- Zentrale `DocxMetadata` Konfiguration

---

## 🏗️ Architektur

```
src/utils/docx_markdown_optimizer.py
├── DocxMetadata (Zentrale Konfiguration)
├── OptimizationResult (Ergebnisformat)
├── BaseOptimizer (Abstrakte Basis)
│   ├── StruktogrammOptimizer
│   ├── CodeBlockOptimizer
│   └── FooterVersionOptimizer
├── DocxOptimizer (Hauptklasse)
└── optimize_pruefungen_directory() (Convenience-Funktion)

scripts/optimize_docx.py
└── CLI-Interface zum Optimizer

config/docx_config.json
└── Zentrale Konfigurationsdatei
```

---

## 💻 Verwendung

### Standard-Verwendung: Alle Prüfungsdokumente optimieren

```bash
python scripts/optimize_docx.py
```

### Mit ausführlicher Ausgabe

```bash
python scripts/optimize_docx.py --verbose
```

### Spezifisches Verzeichnis optimieren

```bash
python scripts/optimize_docx.py --dir docs/aufgaben
```

### Mit Konfigurationsdatei

```bash
python scripts/optimize_docx.py --config config/docx_config.json
```

### Dry-Run (keine Änderungen durchführen)

```bash
python scripts/optimize_docx.py --dry-run --verbose
```

---

## 🐍 Python API

### Einfache Verwendung

```python
from src.utils.docx_markdown_optimizer import optimize_pruefungen_directory

# Alle Prüfungsdokumente optimieren
result = optimize_pruefungen_directory(verbose=True)

print(f"Optimiert: {result['summary']['files_optimized']} Dateien")
print(f"Änderungen: {result['summary']['total_optimizations']}")
```

### Erweiterte Verwendung

```python
from src.utils.docx_markdown_optimizer import DocxOptimizer, DocxMetadata
from pathlib import Path

# Konfiguration anpassen
metadata = DocxMetadata(
    code_bg_color="#F5F5F5",  # Leicht andere Farbe
    verbose=True
)

# Optimizer erstellen
optimizer = DocxOptimizer(metadata)

# Einzelne Datei optimieren
result = optimizer.optimize_file(Path("dokument.md"))
print(f"✅ {result.changes_count} Änderungen")

# Ganzes Verzeichnis optimieren
results = optimizer.optimize_directory(Path("docs"))
for result in results:
    if result.changes_count > 0:
        print(f"📝 {result.file_path}: {result.changes_count} Änderungen")
```

### Mit benutzerdefiniertem Optimizer

```python
from src.utils.docx_markdown_optimizer import (
    DocxOptimizer,
    DocxMetadata,
    BaseOptimizer
)
from typing import Tuple

class MyCustomOptimizer(BaseOptimizer):
    """Eigener Optimizer für spezifische Anforderungen."""
    
    def optimize(self, content: str) -> Tuple[str, int]:
        """Implementiere deine Logik."""
        # ... optimierungen ...
        return optimized_content, changes_count

# Verwende in Pipeline
metadata = DocxMetadata()
optimizer = DocxOptimizer(metadata)
optimizer.optimizers.append(MyCustomOptimizer(metadata))
```

---

## ⚙️ Konfiguration

### Via Config-Datei (`config/docx_config.json`)

```json
{
  "code_bg_color": "#F2F2F2",
  "code_text_color": "#111111",
  "code_border_color": "#C8C8C8",
  "embed_struktogramme": true,
  "add_alttext": true,
  "version_footer": true,
  "verbose": false
}
```

### Programmatisch

```python
from src.utils.docx_markdown_optimizer import DocxMetadata

config = {
    "code_bg_color": "#F2F2F2",
    "code_text_color": "#111111",
    "embed_struktogramme": True,
    "verbose": True
}

metadata = DocxMetadata.from_dict(config)
```

---

## 📊 Ausgabeformat

Der Optimizer erzeugt folgende DOCX-Metadaten-Kommentare im Markdown:

### Beispiel: Optimiertes Struktogramm

**Input:**
```markdown
![Mein Struktogramm](https://example.com/diagram.svg)
```

**Output:**
```markdown
![Mein Struktogramm](https://example.com/diagram.svg)
<!-- DOCX-ALT-TEXT: Mein Struktogramm -->
<!-- DOCX-EMBED-SVG: https://example.com/diagram.svg -->
<!-- DOCX-EMBEDDING-HINT: Dieses Struktogramm wird bei DOCX-Export als eingebettete Grafik dargestellt... -->
```

### Beispiel: Code-Block-Styling

**Input:**
```markdown
```python
def beispiel():
    pass
```python
```

**Output:**
```markdown
<!-- DOCX-CODE-STYLING: bg=#F2F2F2, text=#111111, border=#C8C8C8 -->
...
```python
def beispiel():
    pass
```python
```

---

## 🔌 Integration mit anderen Tools

### Mit Pandoc für DOCX-Export

```bash
# Markdown to DOCX (Metadaten werden berücksichtigt)
pandoc input.md -t docx -o output.docx
```

### Mit CI/CD Pipeline

```yaml
# GitHub Actions Beispiel
- name: Optimiere DOCX-Markdown
  run: python scripts/optimize_docx.py --verbose
```

---

## 🧪 Testing

```python
# Test einzelner Component
from src.utils.docx_markdown_optimizer import StruktogrammOptimizer, DocxMetadata

optimizer = StruktogrammOptimizer(DocxMetadata())
content = "![Test](https://example.com/image.svg)"
optimized, count = optimizer.optimize(content)

assert count == 1
assert "DOCX-EMBED-SVG" in optimized
```

---

## 📈 Extensibility

### Neue Optimizer hinzufügen

1. Erbe von `BaseOptimizer`:
```python
class MyOptimizer(BaseOptimizer):
    def optimize(self, content: str) -> Tuple[str, int]:
        # Implementierung
        return optimized_content, changes_count
```

2. Registriere in `DocxOptimizer`:
```python
optimizer = DocxOptimizer(metadata)
optimizer.optimizers.append(MyOptimizer(metadata))
```

### Neue Optimizer-Modi

```python
# Extend MetaData
@dataclass
class MyDocxMetadata(DocxMetadata):
    custom_option: str = "value"
```

---

## 🐛 Troubleshooting

### Problem: Änderungen werden nicht angewendet

**Lösung:** Überprüfe, ob das Dokument bereits optimiert ist:
```bash
grep -l "DOCX-" dokument.md
```

### Problem: Falsche Farben

**Lösung:** Passe die Farben in `config/docx_config.json` an:
```json
{
  "code_bg_color": "#EEEEEE",
  "code_text_color": "#000000"
}
```

---

## 📝 Best Practices

1. **Dry-Run vor Änderungen:** `python scripts/optimize_docx.py --dry-run -v`
2. **Git-Commit vor Massenänderungen:** Dokumentiere Zweck der Optimierung
3. **Test auf einem Dokument:** Vor kompletten Verzeichnis-Durchlauf
4. **Logische Gruppierung:** Optimiere thematisch zusammenhängende Dokumente zusammen

---

## 🤝 Contributing

Neue Optimizer-Ideen? Erstelle einen neuen Optimizer:

```python
# In src/utils/docx_markdown_optimizer.py
class NewFeatureOptimizer(BaseOptimizer):
    """Beschreibe dein Feature."""
    
    def optimize(self, content: str) -> Tuple[str, int]:
        """Implementiere die Logik."""
        pass
```

Dann registriere ihn und teste:
```python
optimizer.optimizers.append(NewFeatureOptimizer(metadata))
```

---

## 📄 Lizenz

MIT License - Siehe LICENSE für Details

---

## 📚 Weitere Ressourcen

- [DOCX-Standard Referenz](https://en.wikipedia.org/wiki/Office_Open_XML)
- [Pandoc Dokumentation](https://pandoc.org/)
- [Repository README](../../README.md)

---

**Fragen?** Erstelle ein Issue im Repository oder kontaktiere den Maintainer.
