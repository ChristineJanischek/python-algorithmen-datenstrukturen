# Codespace Setup ToDos

## Automatisch eingerichtet

Beim Erstellen eines Codespace werden folgende Voraussetzungen automatisch gesetzt:

- VS Code Erweiterungen:
  - `ms-azuretools.vscode-docker`
  - `ms-python.python`
  - `ms-toolsai.jupyter`
  - `dbaeumer.vscode-eslint`
  - `esbenp.prettier-vscode`
  - `ritwickdey.LiveServer`
- Systemfeatures:
  - Node.js (LTS)
  - Docker CLI (`docker-outside-of-docker` Feature)
- Python-Abhängigkeiten für API:
  - Installation aus `apps/api/requirements.txt`
  - `pip-audit`
- Node-Abhängigkeiten:
  - `apps/web` (`npm ci` bzw. `npm install`)
  - `apps/drawio-extension` (`npm ci` bzw. `npm install`)
- Globales Hilfstool:
  - `live-server`

Quelle: `.devcontainer/devcontainer.json` + `.devcontainer/post-create.sh`

## Offene ToDos (manuell/organisatorisch)

- Docker-Daemon-Verfügbarkeit in der Umgebung prüfen:
  - `docker version`
  - Falls nicht verfügbar: Codespace mit Docker-Support neu erstellen
- Erste Qualitätsprüfung nach Setup ausführen:
  - `python3 apps/tools/check_docs_dod.py`
  - `cd apps/api && python -m unittest discover -s tests -p "test_*.py"`
  - `cd apps/web && npm run test && npm run build`
- Optional: Sicherheitsprüfung lokal ausführen:
  - `cd apps/api && pip-audit -r requirements.txt --progress-spinner off --ignore-vuln CVE-2025-54121 --ignore-vuln CVE-2025-62727`
  - `cd apps/web && npm audit --audit-level=high`

## Definition of Done für neue Dev-Umgebungen

Eine neue Dev-Umgebung gilt als betriebsbereit, wenn:

1. `postCreateCommand` ohne Fehler durchläuft.
2. Die oben genannten Qualitätsprüfungen erfolgreich sind.
3. `docker` CLI verfügbar ist.
