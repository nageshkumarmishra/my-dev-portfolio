import pytest
from app import create_app, db

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_add_employee(client):
    response = client.post("/employees/", json={"name": "Alice", "department": "HR"})
    assert response.status_code == 201
    assert response.get_json()["name"] == "Alice"

def test_get_employees(client):
    client.post("/employees/", json={"name": "Bob", "department": "Finance"})
    response = client.get("/employees/")
    assert response.status_code == 200
    assert len(response.get_json()) >= 1