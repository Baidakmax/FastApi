from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_root():
    responce = client.get('/')
    assert responce.status_code == 200
    assert responce.json() == {'Hello': 'World'}



