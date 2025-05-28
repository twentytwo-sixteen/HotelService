from fastapi import FastAPI
from .api import rooms, bookings

app = FastAPI()
app.include_router(rooms.router, prefix="/rooms")
app.include_router(bookings.router, prefix="/bookings")

