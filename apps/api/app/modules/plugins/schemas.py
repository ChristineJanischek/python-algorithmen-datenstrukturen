from __future__ import annotations

from pydantic import BaseModel


class PluginResponse(BaseModel):
    id: str
    name: str
    type: str
    version: str
    enabled: bool
    status: str
    description: str
    entrypoint: str
    capabilities: list[str]
