from app.game.player import Player


class Move:

    def __init__(self, column: int, player: Player):
        self.column: int = column
        self.player: Player = player
