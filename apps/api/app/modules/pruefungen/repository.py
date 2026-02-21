from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[5]


def _file_path() -> Path:
    return _repo_root() / "data" / "elearning" / "pruefungen_v1.json"


class PruefungenRepository:
    def __init__(self) -> None:
        self.file_path = _file_path()

    def load_all(self) -> list[dict[str, Any]]:
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        if not self.file_path.exists():
            self.file_path.write_text("[]", encoding="utf-8")
            return []
        with self.file_path.open("r", encoding="utf-8") as handle:
            data = json.load(handle)
        if not isinstance(data, list):
            return []
        return data

    def save_all(self, pruefungen: list[dict[str, Any]]) -> None:
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        with self.file_path.open("w", encoding="utf-8") as handle:
            json.dump(pruefungen, handle, ensure_ascii=False, indent=2)