import pytest
from api_library import create_booking, get_booking, update_booking, delete_booking
from config import AUTH_TOKEN

# Test cases
def test_create_booking():
    response = create_booking()
    assert response.status_code == 200
    assert "bookingid" in response.json()

def test_get_booking():
    booking_id = create_booking().json()["bookingid"]
    response = get_booking(booking_id)
    assert response.status_code == 200
    assert response.json()["firstname"] == BOOKING_DATA["firstname"]

def test_update_booking():
    booking_id = create_booking().json()["bookingid"]
    new_data = {"firstname": "Updated", "lastname": "Name"}
    response = update_booking(booking_id, new_data)
    assert response.status_code == 200
    assert response.json()["firstname"] == new_data["firstname"]

def test_delete_booking():
    booking_id = create_booking().json()["bookingid"]
    response = delete_booking(booking_id)
    assert response.status_code == 201
    assert response.json()["id"] == booking_id
