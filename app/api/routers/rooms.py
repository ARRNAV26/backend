from fastapi import APIRouter
from typing import List
from pydantic import BaseModel
from app.services.room_service import RoomService

class RoomCreateResponse(BaseModel):
    roomId: str

class RoomInfo(BaseModel):
    id: str
    code: str

router = APIRouter()
room_service = RoomService()

@router.post("", response_model=RoomCreateResponse)
async def create_room() -> RoomCreateResponse:
    room_id = room_service.create_room()
    return RoomCreateResponse(roomId=room_id)

@router.get("", response_model=List[RoomInfo])
async def get_rooms() -> List[RoomInfo]:
    rooms_data = room_service.get_all_rooms()
    return [RoomInfo(id=item["id"], code=item["code"]) for item in rooms_data]
