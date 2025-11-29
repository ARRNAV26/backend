# backend/app/api/__init__.py

from fastapi import APIRouter

router = APIRouter()

from .routers import rooms, autocomplete, ws

router.include_router(rooms.router, prefix="/rooms", tags=["rooms"])
router.include_router(autocomplete.router, prefix="/autocomplete", tags=["autocomplete"])
router.include_router(ws.router, prefix="/ws", tags=["websocket"])