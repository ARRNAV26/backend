from pydantic import BaseModel
from typing import List, Optional

class RoomCreate(BaseModel):
    room_id: str

class RoomUpdate(BaseModel):
    code: str
    users: List[str]

class RoomResponse(BaseModel):
    room_id: str
    code: Optional[str] = None
    users: List[str] = []