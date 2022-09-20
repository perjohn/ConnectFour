import pytest
from fastapi.testclient import TestClient

from app.app import app


def test_new_game(test_client):
    response = test_client.get('api/v1/new-match')
    assert response.status_code == 200
    response_json = response.json()
    assert 'board' in response_json
    assert len(response_json['board']) == 6
    assert len(response_json['board'][0]) == 7


@pytest.fixture
def test_client():
    return TestClient(app)
