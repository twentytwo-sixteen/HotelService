def test_create_booking(client):
    room = client.post("/rooms", json={"description": "Booking Room", "price": 200}).json()
    response = client.post("/bookings", json={
        "room_id": room["id"],
        "date_start": "2025-06-01",
        "date_end": "2025-06-05"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["room_id"] == room["id"]

def test_booking_overlap(client):
    room = client.post("/rooms", json={"description": "Overlap Room", "price": 300}).json()
    client.post("/bookings", json={
        "room_id": room["id"],
        "date_start": "2025-06-10",
        "date_end": "2025-06-15"
    })
    response = client.post("/bookings", json={
        "room_id": room["id"],
        "date_start": "2025-06-12",
        "date_end": "2025-06-18"
    })
    assert response.status_code == 400
