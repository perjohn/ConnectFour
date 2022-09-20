from app.game.engine import Engine
from app.game.move import Move


class Match:
    engine = Engine()
    moves: list[Move] = []

    def move(self, move: Move):
        pass

    def get_board_as_array(self):
        return self.engine.game.board_state.values.tolist()
