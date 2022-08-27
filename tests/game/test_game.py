from app.game.game import Game
from app.game.player import Player


def test_initialize():
    game = Game()
    expected = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]
    assert is_game_equal(game, expected) is True


def test_win_first_column():
    game = Game()
    game.board_state.at[5, 0] = Player.RED.value
    game.board_state.at[4, 0] = Player.RED.value
    game.board_state.at[3, 0] = Player.RED.value
    game.board_state.at[2, 0] = Player.RED.value
    game.board_state.at[5, 1] = Player.YELLOW.value
    game.board_state.at[4, 1] = Player.YELLOW.value
    game.board_state.at[3, 1] = Player.YELLOW.value
    assert game.is_win() is True


def test_win_second_column():
    game = Game()
    game.board_state.at[5, 1] = Player.RED.value
    game.board_state.at[4, 1] = Player.RED.value
    game.board_state.at[3, 1] = Player.RED.value
    game.board_state.at[2, 1] = Player.RED.value
    game.board_state.at[5, 0] = Player.YELLOW.value
    game.board_state.at[4, 0] = Player.YELLOW.value
    game.board_state.at[3, 0] = Player.YELLOW.value
    assert game.is_win() is True


def is_game_equal(game, expected_board) -> bool:
    for row_idx in range(0, 6):
        game_row = game.board_state.iloc[row_idx]
        if game_row.tolist() != expected_board[row_idx]:
            return False
    return True
