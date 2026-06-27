from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_home_returns_welcome_message():
    # Validates that the home endpoint returns the expected welcome message.
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "API Testing Demo with FastAPI"}


def test_health_check_returns_ok():
    # Validates that the health endpoint reports the API as available.
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_get_users_returns_list():
    # Validates that the users endpoint returns a non-empty list.
    response = client.get("/users")
    body = response.json()

    assert response.status_code == 200
    assert isinstance(body, list)
    assert len(body) >= 1


def test_get_user_by_id_success():
    # Validates that an existing user can be retrieved by id.
    response = client.get("/users/1")
    body = response.json()

    assert response.status_code == 200
    assert body["id"] == 1


def test_get_user_by_id_not_found():
    # Validates that a clear 404 response is returned for a missing user.
    response = client.get("/users/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "User with id 999 was not found."


def test_create_user_success():
    # Validates that a valid user payload creates a new resource.
    payload = {"name": "Carla Brown", "email": "carla@example.com"}

    response = client.post("/users", json=payload)
    body = response.json()

    assert response.status_code == 201
    assert "id" in body
    assert body["name"] == payload["name"]
    assert body["email"] == payload["email"]


def test_create_user_invalid_payload():
    # Validates that empty values are rejected by request validation.
    payload = {"name": "", "email": ""}

    response = client.post("/users", json=payload)

    assert response.status_code == 422
