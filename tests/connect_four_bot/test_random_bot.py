from app.connect_four_bot.random_bot import RandomBot
from app.game.game import Game
from app.game.player import Player


def test_random_move_empty():
    game = Game()
    random_bot = RandomBot(game)

    result = random_bot.calculate_move()
    assert 0 <= result <= 6


def test_random_move_first_column_filled():
    game = Game()
    random_bot = RandomBot(game)

    game.board_state.at[5, 0] = Player.RED.value
    game.board_state.at[4, 0] = Player.YELLOW.value
    game.board_state.at[3, 0] = Player.RED.value
    game.board_state.at[2, 0] = Player.YELLOW.value
    game.board_state.at[1, 0] = Player.RED.value
    game.board_state.at[0, 0] = Player.YELLOW.value

    result = random_bot.calculate_move()
    assert 1 <= result <= 6
