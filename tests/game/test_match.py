import pytest

from app.game.match import Match
from app.game.move import Move
from app.game.player import Player


def test_move():
    match = Match()
    result = match.move(Move(3, Player.RED))
    assert result.OK


def test_illegal_move():
    match = Match()
    result = match.move(Move(3, Player.YELLOW))
    assert result.ILLEGAL_MOVE


def test_get_board_as_array():
    match = Match()
    result = match.get_board_as_array()
    assert result
    assert len(result) == 6
    assert len(result[0]) == 7


def test_match_from_array():
    board_array = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, -1, 0, 0]
    ]
    match = Match.from_array(board_array)
    assert match


def test_match_from_array_incorrect_rows():
    board_array = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]
    with pytest.raises(ValueError):
        Match.from_array(board_array)


def test_match_from_array_incorrect_columns():
    board_array = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ]
    with pytest.raises(ValueError):
        Match.from_array(board_array)


def test_match_from_array_incorrect_entry():
    board_array = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, -1, 0, 0]
    ]
    with pytest.raises(ValueError):
        Match.from_array(board_array)


def test_match_from_array_incorrect_board():
    board_array = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, -1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0]
    ]
    with pytest.raises(ValueError):
        Match.from_array(board_array)


def test_match_from_array_incorrect_move_order():
    board_array = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0]
    ]
    with pytest.raises(ValueError):
        Match.from_array(board_array)
