# Struktogramm Render Pipeline (CLI + Core)

## Ziel

Die Render Pipeline ermöglicht einen einheitlichen, automatisierbaren Workflow für:

- Extraktion von `struktogramm`-Blöcken aus Markdown
- Validierung nach BW-Operatornotation
- SVG-Generierung für E-Learning-Inhalte
- maschinenlesbare Reports für CI, API und Admin-Prozesse

## Architektur

### Schichtenmodell

1. **Core (`src/utils/struktogramm_pipeline.py`)**
   - `StruktogrammPipeline`
   - `BwNotationValidator`
   - `BwSvgRenderer`
   - `DrawioStencilRegistry`

2. **CLI Adapter (`apps/tools/struktogramm_cli.py`)**
   - Kommandos `render` und `render-and-validate`
   - Ausgabeformat für Lehrkräfte/Entwicklung

3. **Datenfluss**
   - Markdown-Datei → Block-Extraktion → Validierung → SVG-Dateien → JSON-Report

### Warum diese Trennung

- Keine Redundanz: Fachlogik liegt zentral in `src/utils`
- Hohe Wiederverwendbarkeit: API, CLI und spätere E-Learning-Worker nutzen dieselbe Pipeline
- Wartbarkeit: CLI enthält keine Rendering-/Parsing-Logik

## Kommandos

### Rendern

```bash
cd apps/tools
python struktogramm_cli.py render <datei.md> [--output-dir ...] [--prefix ...] [--strict] [--report ...]
```

### Rendern + Validieren

```bash
cd apps/tools
python struktogramm_cli.py render-and-validate <datei.md> [--output-dir ...] [--prefix ...] [--strict] [--report ...]
```

## Sicherheits- und Betriebsregeln

- Pfad-Sicherheit: Alle Lese-/Schreibpfade müssen innerhalb des Repositorys liegen.
- Unsichere Pfade führen zu `PipelineSecurityError` und Exit-Code `2`.
- Ausgabeordner wird kontrolliert erzeugt (`struktogramme/generated/svg/cli` als Default).
- Optionaler Report ist JSON und eignet sich für automatisierte Auswertung.
- Draw.io-Stencil (`apps/drawio-extension/stencil.xml`) wird auf Existenz und XML-Struktur geprüft.

## Automatisierung (Bürokratie/Admin)

### Standard-Workflow für Inhalte

1. Markdown-Aufgabe/Musterlösung pflegen
2. Pipeline laufen lassen (`render-and-validate`)
3. JSON-Report archivieren (Nachweis)
4. SVGs in Zieldatei einbetten

### CI-Idee

- Pipeline auf geänderten `docs/**/*.md`
- Abbruch bei `--strict`-Fehlern
- Report als Artefakt speichern

## JSON-Report

Beispielstruktur:

```json
{
  "source_file": "...",
  "output_dir": "...",
  "stencil_file": "...",
  "stencil_ok": true,
  "block_count": 2,
  "artifacts": [
    {
      "block_index": 1,
      "output_file": ".../datei_block_01.svg",
      "issues": [
        {"line": 88, "message": "...", "severity": "error"}
      ],
      "rendered": true
    }
  ]
}
```

## Erweiterungspunkte

- Austauschbarer Renderer (z. B. MXGraph/Draw.io-Export)
- Zusätzliche Validierungsprofile (Prüfung, Unterricht, CI)
- API-Endpunkt in `apps/api` als Wrapper um `StruktogrammPipeline`
- Auto-Einbettung der erzeugten SVGs in Markdown

## Ordnung und Verantwortlichkeiten

- Core-Logik: `src/utils/`
- Ausführbare Tools: `apps/tools/`
- Draw.io-Artefakte: `apps/drawio-extension/`
- Fachdokumentation: `docs/handbuch/`

Diese Ordnung ist verbindlich, damit Sicherheit, Wartbarkeit und Effizienz langfristig erhalten bleiben.
