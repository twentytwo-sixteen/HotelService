from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from .. import models, schemas

def has_overlap(db: Session, booking: schemas.BookingCreate)-> bool:
    sql = text("""
        SELECT 1 FROM bookings
        WHERE room_id = :room_id
          AND date_start < :date_end
          AND date_end > :date_start
        LIMIT 1 
        """)
    result = db.execute(sql,{
        "room_id": booking.room_id,
        "date_start": booking.date_start,
        "date_end": booking.date_end
    }).first()
    return result is not None

def create_booking(db: Session, booking: schemas.BookingCreate):
    if has_overlap(db, booking):
        return None

    db_booking = models.Booking(**booking.dict())
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking

def delete_booking(db: Session, booking_id: int):
    db_booking = db.get(models.Booking, booking_id)
    if db_booking:
        db.delete(db_booking)
        db.commit()
    return db_booking

def list_bookings(db: Session, room_id: int):
    return db.query(models.Booking).filter_by(room_id=room_id).order_by(models.Booking.date_start).all()
