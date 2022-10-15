import copy

from app.bot.bot import Bot
from app.bot.random_bot import RandomBot
from app.game.engine import Engine
from app.game.game import Game, NR_OF_COLUMNS
from app.game.move import Move
from app.game.move_result import MoveResult
from app.game.player import Player


class OnePlyBot(Bot):
    TYPE = 1

    def __init__(self, game: Game):
        self.game = game

    def calculate_move(self, player: Player) -> Move:
        engine = Engine()
        for move in range(0, NR_OF_COLUMNS):
            if self.game.space_left_for_player_in_column(move):
                game_copy = copy.deepcopy(self.game)
                engine.game = game_copy
                move_result, _ = engine.move(column=move, player=player)
                if move_result == MoveResult.WIN_RED or move_result == MoveResult.WIN_YELLOW:
                    return Move(move, player)
        # otherwise make a random move
        random_bot = RandomBot(self.game)
        return random_bot.calculate_move(player)
