from typing import Dict, Any
from fastapi import WebSocket, WebSocketDisconnect
from collections import defaultdict

class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[str, WebSocket] = {}
        self.room_code: Dict[str, str] = defaultdict(str)

    async def connect(self, room_id: str, websocket: WebSocket):
        await websocket.accept()
        self.active_connections[room_id] = websocket

    def disconnect(self, room_id: str):
        if room_id in self.active_connections:
            del self.active_connections[room_id]

    async def send_message(self, room_id: str, message: str):
        if room_id in self.active_connections:
            websocket = self.active_connections[room_id]
            await websocket.send_text(message)

    async def broadcast(self, room_id: str, message: str):
        for connection in self.active_connections.values():
            await connection.send_text(message)

    def set_code(self, room_id: str, code: str):
        self.room_code[room_id] = code

    def get_code(self, room_id: str) -> str:
        return self.room_code.get(room_id, "")