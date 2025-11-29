from typing import Dict, Any
import uuid
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.db.models import Room

class RoomService:
    """Room service using database for persistence."""
    @classmethod
    def create_room(cls) -> str:
        room_id = str(uuid.uuid4())
        db = SessionLocal()
        try:
            new_room = Room(id=room_id, code="")
            db.add(new_room)
            db.commit()
        finally:
            db.close()
        return room_id

    @classmethod
    def room_exists(cls, room_id: str) -> bool:
        db = SessionLocal()
        try:
            room = db.query(Room).filter(Room.id == room_id).first()
            return room is not None
        finally:
            db.close()

    @classmethod
    def get_code(cls, room_id: str) -> str:
        db = SessionLocal()
        try:
            room = db.query(Room).filter(Room.id == room_id).first()
            if not room:
                raise ValueError("Room does not exist.")
            return room.code
        finally:
            db.close()

    @classmethod
    def update_code(cls, room_id: str, code: str) -> None:
        db = SessionLocal()
        try:
            room = db.query(Room).filter(Room.id == room_id).first()
            if not room:
                raise ValueError("Room does not exist.")
            room.code = code
            db.commit()
        finally:
            db.close()

    @classmethod
    def get_all_rooms(cls) -> list[Dict[str, Any]]:
        db = SessionLocal()
        try:
            rooms = db.query(Room).all()
            return [{"id": r.id, "code": r.code[:50] + ("..." if len(r.code) > 50 else "")} for r in rooms]
        finally:
            db.close()

# Module-level function aliases for backward compatibility
create_room = RoomService.create_room
room_exists = RoomService.room_exists
update_code = RoomService.update_code
get_code = RoomService.get_code
get_all_rooms = RoomService.get_all_rooms
