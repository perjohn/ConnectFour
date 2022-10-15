from http import HTTPStatus
from typing import List

import pytest
from fastapi.testclient import TestClient

from app.app import app


def test_new_game(test_client):
    response = test_client.get('api/v1/new-match/1/0')
    assert response.status_code == HTTPStatus.OK
    response_json = response.json()
    assert 'board' in response_json
    assert len(response_json['board']) == 6
    assert len(response_json['board'][0]) == 7
    assert board_sum(response_json['board']) == 0


def test_new_game_yellow(test_client):
    response = test_client.get('api/v1/new-match/-1/0')
    assert response.status_code == HTTPStatus.OK
    response_json = response.json()
    assert 'board' in response_json
    assert len(response_json['board']) == 6
    assert len(response_json['board'][0]) == 7
    assert board_sum(response_json['board']) == 1


def test_new_game_illegal_player(test_client):
    response = test_client.get('api/v1/new-match/0/0')
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_move(test_client):
    response = test_client.get('api/v1/new-match/1/0')
    assert response.status_code == HTTPStatus.OK

    response = test_client.get('api/v1/move/1/3')
    assert response.status_code == HTTPStatus.OK
    response_json = response.json()
    assert 'board' in response_json
    board = response_json['board']
    assert len(board) == 6
    assert len(board[0]) == 7
    assert board[5][3] == 1


def test_two_moves(test_client):
    response = test_client.get('api/v1/new-match/1/0')
    assert response.status_code == HTTPStatus.OK

    response = test_client.get('api/v1/move/1/3')
    assert response.status_code == HTTPStatus.OK

    response = test_client.get('api/v1/move/-1/3')
    assert response.status_code == HTTPStatus.OK

    response_json = response.json()
    assert 'board' in response_json
    board = response_json['board']
    assert board[4][3] == -1


def test_illegal_move(test_client):
    response = test_client.get('api/v1/new-match/1/0')
    assert response.status_code == HTTPStatus.OK

    response = test_client.get('api/v1/move/1/8')
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


def board_sum(board_array: List[List[int]]) -> int:
    return sum(sum(board_array, []))


@pytest.fixture
def test_client():
    return TestClient(app)
