from app.bot.bot import Bot
from app.game.game import Game
from app.game.move import Move
from app.game.player import Player


class TestBot(Bot):
    TYPE = 99

    def __init__(self, game: Game):
        self.game = game

    def calculate_move(self, player: Player) -> Move:
        return Move(3, player)
