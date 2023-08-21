import requests
from config import BASE_URL, AUTH_TOKEN, BOOKING_DATA

def create_booking():
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {AUTH_TOKEN}"
    }
    response = requests.post(f"{BASE_URL}/booking", json=BOOKING_DATA, headers=headers)
    return response

def get_booking(booking_id):
    response = requests.get(f"{BASE_URL}/booking/{booking_id}")
    return response

def update_booking(booking_id, new_data):
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {AUTH_TOKEN}"
    }
    response = requests.put(f"{BASE_URL}/booking/{booking_id}", json=new_data, headers=headers)
    return response

def delete_booking(booking_id):
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {AUTH_TOKEN}"
    }
    response = requests.delete(f"{BASE_URL}/booking/{booking_id}", headers=headers)
    return response
