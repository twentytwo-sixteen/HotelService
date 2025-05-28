from sqlalchemy.orm import Session
from .. import models, schemas

def create_room(db: Session, room: schemas.RoomCreate):
    db_room = models.Room(**room.dict())
    db.add(db_room)
    db.commit()
    db.refresh(db_room)
    return db_room

def delete_room(db: Session, room_id: int):
    db_room = db.get(models.Room, room_id)
    if db_room:
        db.delete(db_room)
        db.commit()
    return db_room

def list_rooms(db: Session, sort_by: str = "created_at", order: str = "asc"):
    query = db.query(models.Room)
    if sort_by == "price":
        sort_field = models.Room.price
    else:
        sort_field = models.Room.created_at
    if order == "desc":
        sort_field = sort_field.desc()
    return query.order_by(sort_field).all()
