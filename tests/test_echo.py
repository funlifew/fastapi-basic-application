from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_echo_success():
    response = client.post(
        "/echo",
        json={"message": "Test"}
    )
    
    assert response.status_code == 200
    assert response.json() == {
        'status': 'success',
        'received_message': 'Test'
    }

def test_echo_validation_error():
    response = client.post(
        "/echo",
        json={},
    )
    
    assert response.status_code == 422