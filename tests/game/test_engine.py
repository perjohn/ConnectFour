from app.game.engine import Engine
from app.game.game import Game
from app.game.move_result import MoveResult
from app.game.player import Player
from tests.game.test_game import is_game_equal


def test_move():
    engine = Engine()
    result, game = engine.move(0, Player.RED, Game())
    assert result == MoveResult.OK

    expected = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0],
    ]
    assert is_game_equal(game, expected) is True


def test_two_moves():
    engine = Engine()
    result, game = engine.move(0, Player.RED, Game())
    result, game = engine.move(0, Player.YELLOW, game)
    assert result == MoveResult.OK

    expected = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [-1, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0],
    ]
    assert is_game_equal(game, expected) is True


def test_illegal_move_row():
    engine = Engine()
    result, game = engine.move(-1, Player.RED, Game())
    assert result == MoveResult.ILLEGAL_MOVE


def test_illegal_move_state():
    engine = Engine()
    result, game = engine.move(0, Player.YELLOW, Game())
    assert result == MoveResult.ILLEGAL_MOVE


def test_illegal_move_full_column():
    engine = Engine()
    result, game = engine.move(0, Player.RED, Game())
    result, game = engine.move(0, Player.YELLOW, game)
    result, game = engine.move(0, Player.RED, game)
    result, game = engine.move(0, Player.YELLOW, game)
    result, game = engine.move(0, Player.RED, game)
    result, game = engine.move(0, Player.YELLOW, game)
    assert result == MoveResult.OK

    result, game = engine.move(0, Player.RED, game)
    assert result == MoveResult.ILLEGAL_MOVE
