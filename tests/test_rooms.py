def test_create_room(client):
    response = client.post("/rooms", json={"description": "Test room", "price": 100})
    assert response.status_code == 200
    data = response.json()
    assert data["description"] == "Test room"
    assert data["price"] == 100

def test_get_rooms(client):
    response = client.get("/rooms")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_delete_room(client):
    create_response = client.post("/rooms", json={"description": "To delete", "price": 50})
    room_id = create_response.json()["id"]
    del_response = client.delete(f"/rooms/{room_id}")
    assert del_response.status_code == 200