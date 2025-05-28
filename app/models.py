from sqlalchemy import Column, Integer, String, Date, ForeignKey, DateTime, func, Numeric
from .db  import Base
from sqlalchemy import Index

class Room(Base):
    __tablename__ = "rooms"
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    
class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True, index=True)
    room_id = Column(Integer, ForeignKey("rooms.id", ondelete="CASCADE"), nullable=False)
    date_start = Column(Date, nullable=False)
    date_end = Column(Date, nullable=False)
    
    __table_args__ = (
        Index("idx_room_date_range", "room_id", "date_start", "date_end"),
    )
    