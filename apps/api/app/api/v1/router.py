from __future__ import annotations

from fastapi import APIRouter

from ...modules.pruefungen.router import router as pruefungen_router

v1_router = APIRouter()
v1_router.include_router(pruefungen_router, prefix="/pruefungen", tags=["pruefungen"])