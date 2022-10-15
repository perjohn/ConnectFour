from app.bot.one_ply_bot import OnePlyBot
from app.game.game import Game, NR_OF_COLUMNS
from app.game.player import Player


def test_move_first_column():
    game = Game()
    one_ply_bot = OnePlyBot(game)

    game.board_state.at[5, 0] = Player.RED.value
    game.board_state.at[4, 0] = Player.RED.value
    game.board_state.at[3, 0] = Player.RED.value
    game.board_state.at[5, 1] = Player.YELLOW.value
    game.board_state.at[4, 1] = Player.YELLOW.value
    game.board_state.at[3, 1] = Player.YELLOW.value

    result = one_ply_bot.calculate_move(Player.RED)
    assert result.column == 0


def test_move_second_column():
    game = Game()
    one_ply_bot = OnePlyBot(game)

    game.board_state.at[5, 1] = Player.RED.value
    game.board_state.at[4, 1] = Player.RED.value
    game.board_state.at[3, 1] = Player.RED.value
    game.board_state.at[5, 0] = Player.YELLOW.value
    game.board_state.at[4, 0] = Player.YELLOW.value
    game.board_state.at[3, 0] = Player.YELLOW.value

    result = one_ply_bot.calculate_move(Player.RED)
    assert result.column == 1


def test_move_random():
    game = Game()
    one_ply_bot = OnePlyBot(game)

    game.board_state.at[5, 1] = Player.RED.value
    game.board_state.at[4, 1] = Player.YELLOW.value
    game.board_state.at[3, 1] = Player.RED.value
    game.board_state.at[5, 0] = Player.YELLOW.value
    game.board_state.at[4, 0] = Player.RED.value
    game.board_state.at[3, 0] = Player.YELLOW.value

    result = one_ply_bot.calculate_move(Player.RED)
    assert 0 <= result.column < NR_OF_COLUMNS
