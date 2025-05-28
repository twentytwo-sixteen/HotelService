from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud
from ..db import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.post("/create")
def create_room(room: schemas.RoomCreate, db: Session = Depends(get_db)):
    db_room = crud.rooms.create_rooms(db, room)
    return {"room_id": db_room.id}

@router.delete("/delete")
def delete_room(room_id: int, db: Session = Depends(get_db)):
    db_room = crud.rooms.delete_room(db, room_id)
    if not db_room:
        raise HTTPException(status_code=404, detail="Room not found")
    
@router.get("/list", response_model=list[schemas.RoomOut])
def list_rooms(sort_by: str = "created_at", order: str = "asc", db: Session = Depends(get_db)):
    return crud.rooms.list_rooms(db, sort_by, order)