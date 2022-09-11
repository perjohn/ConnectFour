import random

from app.bot.bot import Bot
from app.game.game import Game
from app.game.player import Player


class RandomBot(Bot):
    def __init__(self, game: Game):
        self.game = game

    def calculate_move(self, player: Player) -> int:
        result = 0
        legal_move = False
        while not legal_move:
            column = random.randint(0, 6)
            if self.game.space_left_for_player_in_column(column):
                result = column
                legal_move = True
        return result
