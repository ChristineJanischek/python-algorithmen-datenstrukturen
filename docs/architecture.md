# Architektur des Lernagenten

## Überblick

Der Lernagent ist als Konsolenanwendung implementiert.
Er folgt einer klaren Trennung der Verantwortlichkeiten.

```
Nutzereingabe
     │
     ▼
┌─────────────┐
│  main.py    │  Ein- und Ausgabe (Konsole)
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  agent.py   │  Agentensteuerung (orchestriert alle Komponenten)
└──────┬──────┘
       │
   ┌───┴───────────────────┐
   │                       │
   ▼                       ▼
┌──────────┐        ┌────────────┐
│ context  │        │   safety   │  Sicherheitsprüfungen
│ feedback │        │ input_check│  (Ein- und Ausgabe)
│ hint_lvl │        │output_check│
└──────────┘        └────────────┘
learning/                    
   │
   ▼
┌─────────────┐
│system_prompt│  Prompt-Erzeugung
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  providers  │  LLM-Provider-Schnittstelle
│ mock_prov.  │  (MockProvider im MVP)
└─────────────┘
```

## Verantwortlichkeiten

| Modul | Datei | Aufgabe |
|-------|-------|---------|
| Ein-/Ausgabe | `main.py` | Konsoleninteraktion |
| Agentensteuerung | `agent.py` | Orchestrierung aller Komponenten |
| Lernkontext | `learning/context.py` | Verwaltung des Lernzustands |
| Feedback | `learning/feedback.py` | Strukturierte Antworten |
| Hilfestufen | `learning/hint_levels.py` | Auswahl der Unterstützungstiefe |
| Prompt-Erzeugung | `prompts/system_prompt.py` | Systemprompt generieren |
| Provider-Schnittstelle | `providers/__init__.py` | Austauschbare LLM-Schnittstelle |
| MockProvider | `providers/mock_provider.py` | Testbarer Provider ohne API |
| Lerninhalte | `content/loader.py` | JSON-Module laden |
| Eingabeprüfung | `safety/input_check.py` | Nutzereingaben prüfen |
| Ausgabeprüfung | `safety/output_check.py` | Agentenantworten prüfen |

## Datenmodelle

Alle Datenmodelle sind in `models.py` definiert:

- **`LearningContext`**: Fachgebiet, Thema, Niveau, Lernziel, Eingabe, Hilfestufe
- **`Message`**: Rolle (System/User/Assistant) + Inhalt
- **`AgentResponse`**: Text, Antworttyp, Hilfestufe, optionale nächste Aktion
- **`HintLevel`**: ORIENTIERUNG (1), HINWEIS (2), ERKLAERUNG (3)
- **`LearningModule`**: Vollständiges Lernmodul mit allen Metadaten

## Provider-Schnittstelle

Der Provider ist über ein `Protocol` austauschbar:

```python
class LLMProvider(Protocol):
    def generate(self, messages: list[Message]) -> str: ...
```

Im MVP ist nur der `MockProvider` implementiert.
Ein externer Provider (z.B. OpenAI-kompatibel) kann hinzugefügt werden,
ohne dass sich die übrige Architektur ändert.

## Erweiterungspunkte

Die folgenden Erweiterungen sind vorbereitet, aber noch nicht implementiert:

- Adaptive Hilfestufen-Auswahl (→ `hint_levels.py`)
- Fehlerklassifikation (→ Aufgabe 03)
- Externe LLM-Provider (→ `providers/`)
- Lernstandsverfolgung (→ erst nach DSGVO-Prüfung)
- Web-API (→ z.B. FastAPI, später)
- MindLink-Integration (→ langfristige Vision)

## Designentscheidungen

Siehe `docs/decisions.md`.

<!-- CUSTOM_LICENSE_NOTICE_START -->
## License

This repository is licensed under a custom license.

- Attribution required: Christine Janischek - https://emotionalspirit.de
- Non-commercial use only
- Use only within state school systems
- Any other use requires explicit prior written permission
<!-- CUSTOM_LICENSE_NOTICE_END -->
