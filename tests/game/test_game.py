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


def test_win_red_first_column():
    game = Game()
    game.board_state.at[5, 0] = Player.RED.value
    game.board_state.at[4, 0] = Player.RED.value
    game.board_state.at[3, 0] = Player.RED.value
    game.board_state.at[2, 0] = Player.RED.value
    game.board_state.at[5, 1] = Player.YELLOW.value
    game.board_state.at[4, 1] = Player.YELLOW.value
    game.board_state.at[3, 1] = Player.YELLOW.value
    assert game.is_win() is True


def test_win_red_from_last_row():
    game = Game()
    game.board_state.at[5, 5] = Player.YELLOW.value
    game.board_state.at[4, 5] = Player.RED.value
    game.board_state.at[3, 5] = Player.RED.value
    game.board_state.at[2, 5] = Player.RED.value
    game.board_state.at[1, 5] = Player.RED.value
    game.board_state.at[5, 1] = Player.YELLOW.value
    game.board_state.at[4, 1] = Player.YELLOW.value
    assert game.is_win() is True


def test_win_red_lowest_row():
    game = Game()
    game.board_state.at[5, 0] = Player.RED.value
    game.board_state.at[5, 1] = Player.RED.value
    game.board_state.at[5, 2] = Player.RED.value
    game.board_state.at[5, 3] = Player.RED.value
    game.board_state.at[4, 0] = Player.YELLOW.value
    game.board_state.at[4, 1] = Player.YELLOW.value
    game.board_state.at[4, 1] = Player.YELLOW.value
    assert game.is_win() is True


def test_win_red_lowest_row_to_the_right():
    game = Game()
    game.board_state.at[5, 2] = Player.RED.value
    game.board_state.at[5, 3] = Player.RED.value
    game.board_state.at[5, 4] = Player.RED.value
    game.board_state.at[5, 5] = Player.RED.value
    game.board_state.at[4, 2] = Player.YELLOW.value
    game.board_state.at[4, 3] = Player.YELLOW.value
    game.board_state.at[4, 4] = Player.YELLOW.value
    assert game.is_win() is True


def test_win_yellow():
    game = Game()
    game.board_state.at[5, 0] = Player.RED.value
    game.board_state.at[4, 0] = Player.RED.value
    game.board_state.at[3, 0] = Player.RED.value
    game.board_state.at[2, 2] = Player.RED.value
    game.board_state.at[5, 6] = Player.YELLOW.value
    game.board_state.at[4, 6] = Player.YELLOW.value
    game.board_state.at[3, 6] = Player.YELLOW.value
    game.board_state.at[2, 6] = Player.YELLOW.value
    assert game.is_win() is True


def is_game_equal(game, expected_board) -> bool:
    for row_idx in range(0, 6):
        game_row = game.board_state.iloc[row_idx]
        if game_row.tolist() != expected_board[row_idx]:
            return False
    return True
