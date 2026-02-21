from __future__ import annotations

from fastapi import APIRouter

from ...modules.plugins.router import router as plugins_router
from ...modules.pruefungen.router import router as pruefungen_router

v1_router = APIRouter()
v1_router.include_router(pruefungen_router, prefix="/pruefungen", tags=["pruefungen"])
v1_router.include_router(plugins_router, prefix="/plugins", tags=["plugins"])