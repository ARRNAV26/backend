import os
from typing import Any
from typing_extensions import TypedDict

class Settings(TypedDict):
    database_url: str
    websocket_url: str

def get_settings() -> Settings:
    return {
        "database_url": os.getenv("DATABASE_URL", "sqlite:///./test.db"),
        "websocket_url": os.getenv("WEBSOCKET_URL", "ws://localhost:8000/ws")
    }

settings = get_settings()
