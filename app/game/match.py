import pandas as pd

from app.game.engine import Engine
from app.game.game import NR_OF_ROWS, NR_OF_COLUMNS
from app.game.move import Move
from app.game.move_result import MoveResult


class Match:

    def __init__(self):
        self.engine = Engine()
        self.moves: list[Move] = []

    def move(self, move: Move) -> MoveResult:
        self.moves.append(move)
        move_result, _ = self.engine.move(move.column, move.player)
        return move_result

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
    def _has_valid_board_content(board_array: list[list[int]]) -> False:
        if Match._has_incorrect_entries(board_array):
            return False
        if Match._has_incorrect_empty_cell_under_filled_one(board_array):
            return False
        if Match._has_incorrect_move_order(board_array):
            return False
        return True

    @staticmethod
    def _has_incorrect_entries(board_array: list[list[int]]) -> False:
        for row in board_array:
            for cell in row:
                if -1 <= cell <= 1:
                    continue
                return True
        return False

    @staticmethod
    def _has_incorrect_empty_cell_under_filled_one(board_array: list[list[int]]) -> False:
        for column_idx in range(0, NR_OF_COLUMNS):
            found_filled_cell = False
            for row_idx in range(0, NR_OF_ROWS):
                if board_array[row_idx][column_idx] != 0:
                    found_filled_cell = True
                if board_array[row_idx][column_idx] == 0 and found_filled_cell:
                    return True
        return False

    @staticmethod
    def _has_incorrect_move_order(board_array: list[list[int]]) -> False:
        total = 0
        for row in board_array:
            for cell in row:
                total += cell
        return not 0 <= total <= 1
