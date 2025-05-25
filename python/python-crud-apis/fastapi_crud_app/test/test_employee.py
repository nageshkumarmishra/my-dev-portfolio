from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_employee():
    response = client.post("/employees/", json={"name": "Jane", "department": "IT"})
    assert response.status_code == 201
    assert response.json()["name"] == "Jane"

def test_list_employees():
    response = client.get("/employees/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
