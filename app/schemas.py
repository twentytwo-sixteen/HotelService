from pydantic import BaseModel
from datetime import date

class RoomCreate(BaseModel):
    description: str
    price: str

class RoomOut(BaseModel):
    id: int
    description: str
    price: int
    created_at: str
    
class BookingCreate(BaseModel):
    room_id: int
    date_start: date
    date_end: date
    
class BookingOut(BaseModel):
    booking_id: int
    date_start: date
    date_end: date
