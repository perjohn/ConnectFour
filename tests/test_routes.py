from http import HTTPStatus
from typing import List

import pytest
from fastapi.testclient import TestClient

from app.app import app
from app.game.move_result import MoveResult


def test_new_game(test_client):
    response = test_client.get('api/v1/new-match/1/0')
    assert response.status_code == HTTPStatus.OK
    response_json = response.json()
    assert 'board' in response_json
    assert len(response_json['board']) == 6
    assert len(response_json['board'][0]) == 7
    assert board_sum(response_json['board']) == 0


def test_new_game_yellow(test_client):
    response = test_client.get('api/v1/new-match/-1/99')
    assert response.status_code == HTTPStatus.OK
    response_json = response.json()
    assert 'board' in response_json
    board = response_json['board']
    assert len(board) == 6
    assert len(board[0]) == 7
    assert board_sum(board) == 1
    assert board[5][3] == 1


def test_new_game_illegal_player(test_client):
    response = test_client.get('api/v1/new-match/0/0')
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


def test_move(test_client):
    response = test_client.get('api/v1/new-match/1/99')
    assert response.status_code == HTTPStatus.OK

    response = test_client.get('api/v1/move/1/3')

    assert response.status_code == HTTPStatus.OK
    response_json = response.json()
    assert 'board' in response_json
    board = response_json['board']
    assert len(board) == 6
    assert len(board[0]) == 7
    assert board_sum(board) == 0
    assert board[5][3] == 1
    assert board[4][3] == -1
    assert 'moveResult' in response_json
    move_result = MoveResult(response_json['moveResult'])
    assert move_result == MoveResult.OK


def test_two_moves(test_client):
    response = test_client.get('api/v1/new-match/1/99')
    assert response.status_code == HTTPStatus.OK

    response = test_client.get('api/v1/move/1/3')
    assert response.status_code == HTTPStatus.OK

    response = test_client.get('api/v1/move/1/3')
    assert response.status_code == HTTPStatus.OK

    response_json = response.json()
    assert 'board' in response_json
    board = response_json['board']
    assert board[5][3] == 1
    assert board[4][3] == -1
    assert board[3][3] == 1
    assert board[2][3] == -1


def test_win_red(test_client):
    response = test_client.get('api/v1/new-match/1/99')
    assert response.status_code == HTTPStatus.OK

    test_client.get('api/v1/move/1/2')
    test_client.get('api/v1/move/1/2')
    test_client.get('api/v1/move/1/2')
    response = test_client.get('api/v1/move/1/2')
    assert response.status_code == HTTPStatus.OK

    response_json = response.json()
    assert 'board' in response_json
    assert 'moveResult' in response_json
    move_result = MoveResult(response_json['moveResult'])
    assert move_result == MoveResult.WIN_RED


def test_win_yellow(test_client):
    response = test_client.get('api/v1/new-match/1/99')
    assert response.status_code == HTTPStatus.OK

    test_client.get('api/v1/move/1/1')
    test_client.get('api/v1/move/1/4')
    test_client.get('api/v1/move/1/5')
    response = test_client.get('api/v1/move/1/6')
    assert response.status_code == HTTPStatus.OK

    response_json = response.json()
    assert 'board' in response_json
    assert 'moveResult' in response_json
    move_result = MoveResult(response_json['moveResult'])
    assert move_result == MoveResult.WIN_YELLOW


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
