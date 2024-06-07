import pytest
from Main import app

def test_root_route():
    with app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 200
