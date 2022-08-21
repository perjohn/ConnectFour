from app.game.game import Game


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


def is_game_equal(game, expected_board) -> bool:
    for row_idx in range(0, 6):
        game_row = game.board_state.iloc[row_idx]
        if game_row.tolist() != expected_board[row_idx]:
            return False
    return True
