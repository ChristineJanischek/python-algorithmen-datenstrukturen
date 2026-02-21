from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[4]


def _plugins_file() -> Path:
    return _repo_root() / "data" / "elearning" / "plugins_v1.json"


def _default_plugins() -> list[dict[str, Any]]:
    return [
        {
            "id": "pruefungsmodul",
            "name": "Prüfungsmodul",
            "type": "plugin",
            "version": "0.1.0",
            "enabled": True,
            "status": "active",
            "description": "Erweiterung für Prüfungserstellung, Aufgabenverwaltung und Exporte.",
            "entrypoint": "apps/api/app/modules/pruefungen",
            "capabilities": [
                "pruefung.create",
                "pruefung.update",
                "pruefung.export",
            ],
        },
        {
            "id": "drawio-extension",
            "name": "Draw.io Extension",
            "type": "plugin",
            "version": "0.1.0",
            "enabled": True,
            "status": "active",
            "description": "Erweiterung für Struktogramm-Visualisierung und XML/SVG-Konvertierung.",
            "entrypoint": "apps/drawio-extension",
            "capabilities": [
                "struktogramm.render",
                "struktogramm.validate",
                "struktogramm.convert",
            ],
        },
    ]


class PluginRegistry:
    def __init__(self) -> None:
        self.file_path = _plugins_file()

    def _ensure_file(self) -> None:
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        if self.file_path.exists():
            return
        with self.file_path.open("w", encoding="utf-8") as handle:
            json.dump(_default_plugins(), handle, ensure_ascii=False, indent=2)

    def list_plugins(self) -> list[dict[str, Any]]:
        self._ensure_file()
        with self.file_path.open("r", encoding="utf-8") as handle:
            data = json.load(handle)
        if not isinstance(data, list):
            return []
        return data

    def get_plugin(self, plugin_id: str) -> dict[str, Any] | None:
        for plugin in self.list_plugins():
            if plugin.get("id") == plugin_id:
                return plugin
        return None