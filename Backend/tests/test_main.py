
from fastapi.testclient import TestClient
from Backend.main import app

client = TestClient(app)


def test_generate_qr():
    response = client.get("/generate_qr?data=HelloWorld")

    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"
    assert response.content.startswith(b"\x89PNG")


def test_empty_qr_data():
    response = client.get("/generate_qr?data=")

    assert response.status_code == 422
