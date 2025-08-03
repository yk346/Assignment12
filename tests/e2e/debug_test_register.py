import requests

def test_debug_register():
    url = "http://127.0.0.1:8000/auth/register"
    payload = {
        "first_name": "Debug",
        "last_name": "Test",
        "email": "debug.test@example.com",
        "username": "debugtest",
        "password": "SecurePass123!123123",
        "confirm_password": "SecurePass123!123123"
    }
    response = requests.post(url, json=payload)
    print("Status Code:", response.status_code)
    print("Response Body:", response.text)

    assert response.status_code == 201, f"Expected 201 but got {response.status_code}"
    data = response.json()
    assert "id" in data
    assert data["username"] == "debugtest"
    assert data["email"] == "debug.test@example.com"
    assert data["first_name"] == "Debug"
    assert data["last_name"] == "Test"
    assert data["is_active"] is True
    assert data["is_verified"] is False
