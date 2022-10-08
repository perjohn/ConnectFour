import pandas as pd

from app.game.engine import Engine
from app.game.move import Move


class Match:

    def __init__(self):
        self.engine = Engine()
        self.moves: list[Move] = []

    def move(self, move: Move):
        self.moves.append(move)
        self.engine.move(move.column, move.player)

    def get_board_as_array(self) -> list[list[int]]:
        return self.engine.game.board_state.values.tolist()

    @staticmethod
    def from_array(board_array: list[list[int]]):
        if len(board_array) != 6:
            raise ValueError('Board should be 6 rows and 7 columns')
        if len(board_array[0]) != 7:
            raise ValueError('Board should be 6 rows and 7 columns')
        if not Match._has_valid_board_content(board_array):
            raise ValueError('Board can only contain 1, 0 or -1')
        result = Match()
        result.engine.game.board_state = pd.DataFrame(board_array)
        return result

    @staticmethod
    def _has_valid_board_content(board_array: list[list[int]]):
        for row in board_array:
            for cell in row:
                if -1 <= cell <= 1:
                    continue
                return False
        return True
