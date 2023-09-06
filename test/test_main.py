from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_read_ping():
    response = client.get("/api/ping")
    assert response.status_code == 200
    assert response.json() == {"message": "pong"}


def test_book_index():
    response = client.get("/api/book")
    assert response.status_code == 200


def test_book_find():
    response = client.get("/api/book/1")
    assert response.status_code == 200

