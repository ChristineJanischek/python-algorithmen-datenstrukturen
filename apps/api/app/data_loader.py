from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[3]


def _data_dir() -> Path:
    return _repo_root() / "data" / "elearning"


def load_json(name: str) -> List[Dict[str, Any]]:
    path = _data_dir() / name
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def load_text(relative_path: str) -> str:
    path = _repo_root() / relative_path
    return path.read_text(encoding="utf-8")
