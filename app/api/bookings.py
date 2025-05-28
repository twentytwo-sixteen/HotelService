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
def create_booking(booking: schemas.BookingCreate, db: Session = Depends(get_db)):
    db_booking = crud.bookings.create_booking(db, booking)
    if not db_booking:
        raise HTTPException(status_code=400, detail="Room is already booked for these dates")
    return {"booking_id": db_booking.id}

@router.delete("/delete")
def delete_booking(booking_id: int, db: Session = Depends(get_db)):
    db_booking = crud.bookings.delete_booking(db, booking_id)
    if not db_booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return {"status": "deleted"}

@router.get("/list", response_model=list[schemas.BookingOut])
def list_bookings(room_id: int, db: Session = Depends(get_db)):
    bookings = crud.bookings.list_bookings(db, room_id)
    return [
        {
            "booking_id": booking.id,
            "date_start": booking.date_start,
            "date_end": booking.date_end
        }
        for booking in bookings
    ]