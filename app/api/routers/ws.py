from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from typing import List, Dict
from app.services.room_service import RoomService
import json

router = APIRouter()

# In-memory storage for rooms and their WebSocket connections
rooms: Dict[str, List[WebSocket]] = {}

async def send_code_init(websocket: WebSocket, room_id: str) -> None:
    """Send current room code to newly connected client."""
    try:
        code = RoomService.get_code(room_id)
        message = {"type": "init", "code": code}
    except ValueError:
        message = {"type": "init", "code": ""}
    await websocket.send_text(json.dumps(message))

async def handle_update_message(room_id: str, code: str, sender: WebSocket) -> None:
    """Update code in database and broadcast to other clients."""
    RoomService.update_code(room_id, code)
    updated_message = json.dumps({"type": "update_code", "code": code})

    for connection in rooms[room_id]:
        if connection != sender:
            await connection.send_text(updated_message)

def add_connection(room_id: str, websocket: WebSocket) -> None:
    """Add WebSocket connection to room."""
    if room_id not in rooms:
        rooms[room_id] = []
    rooms[room_id].append(websocket)

def remove_connection(room_id: str, websocket: WebSocket) -> None:
    """Remove WebSocket connection from room."""
    if room_id in rooms:
        rooms[room_id].remove(websocket)
        if not rooms[room_id]:
            del rooms[room_id]

@router.websocket("/{room_id}")
async def websocket_endpoint(websocket: WebSocket, room_id: str) -> None:
    await websocket.accept()

    add_connection(room_id, websocket)
    await send_code_init(websocket, room_id)

    try:
        while True:
            data = await websocket.receive_text()
            try:
                payload = json.loads(data)
                if payload.get("type") == "update_code":
                    await handle_update_message(room_id, payload["code"], websocket)
            except json.JSONDecodeError:
                continue
    except WebSocketDisconnect:
        remove_connection(room_id, websocket)
