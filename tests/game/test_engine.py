from app.game.engine import Engine
from app.game.game import Game
from app.game.move_result import MoveResult
from app.game.player import Player


def test_move():
    engine = Engine()
    result, game = engine.move(0, Player.RED, Game())
    assert result == MoveResult.OK


def test_illegal_move_row():
    engine = Engine()
    result, game = engine.move(-1, Player.RED, Game())
    assert result == MoveResult.ILLEGAL_MOVE


def test_illegal_move_state():
    engine = Engine()
    result, game = engine.move(0, Player.YELLOW, Game())
    assert result == MoveResult.ILLEGAL_MOVE
