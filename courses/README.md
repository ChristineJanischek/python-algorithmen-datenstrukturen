# Lernmodule

Dieses Verzeichnis enthält wiederverwendbare Lernmodule im JSON-Format.

## Struktur

```
courses/
├── schemas/
│   └── learning-module.schema.json   # JSON-Schema für Lernmodule
└── examples/
    └── python-lists/
        ├── module.json               # Lernmodul (maschinenlesbar)
        ├── introduction.md           # Einführung (menschenlesbar)
        └── exercise.md               # Aufgabe (menschenlesbar)
```

## Eigene Module erstellen

1. Kopiere `examples/python-lists/module.json` als Vorlage.
2. Vergib eine eindeutige `id` (z.B. `inf-python-schleifen-001`).
3. Fülle alle Pflichtfelder aus (siehe Schema).
4. Validiere das Modul gegen das Schema.
5. Erstelle passende `introduction.md` und `exercise.md`.

## JSON-Schema

Das Schema `schemas/learning-module.schema.json` beschreibt alle Pflichtfelder.
Es kann mit Tools wie `jsonschema` (Python) oder einem Online-Validator geprüft werden.

```bash
pip install jsonschema
python -c "
import json, jsonschema
schema = json.load(open('courses/schemas/learning-module.schema.json'))
modul = json.load(open('courses/examples/python-lists/module.json'))
jsonschema.validate(modul, schema)
print('Modul ist gültig.')
"
```

<!-- CUSTOM_LICENSE_NOTICE_START -->
## License

This repository is licensed under a custom license.

- Attribution required: Christine Janischek - https://emotionalspirit.de
- Non-commercial use only
- Use only within state school systems
- Any other use requires explicit prior written permission
<!-- CUSTOM_LICENSE_NOTICE_END -->
