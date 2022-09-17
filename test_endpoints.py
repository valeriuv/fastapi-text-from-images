from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)   # r = requests

def test_get_home():
    response = client.get("/") # requests.get("") equivalent # python requests package
    assert response.status_code == 200
    assert "text/html" in response.headers['content-type']


def test_post_home():
    response = client.post("/") # requests.post("") equivalent # python requests package
    assert response.status_code == 200
    assert "application/json" in response.headers['content-type']
    assert response.json() == {"hello": "world"}