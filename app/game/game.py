import pandas as pd
from pandas import Series

from app.game.player import Player

NR_OF_COLUMNS = 7


class Game:
    def __init__(self):
        self.board_state: pd.DataFrame = self._initialize_board()

    def move(self, column: int, player: Player):
        game_column = self.get_column(column)
        row = self.find_row_for_move(game_column)
        self.board_state.at[row, column] = player.value

    @staticmethod
    def _initialize_board() -> pd.DataFrame:
        return pd.DataFrame(
            [
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
            ]
        )

    def sum_board_values(self) -> int:
        return self.board_state.values.sum()

    def get_column(self, index: int):
        return self.board_state.iloc[:, index]

    @staticmethod
    def find_row_for_move(game_column: Series):
        zero_indexes = game_column[game_column == 0]
        return zero_indexes.index[-1]

    def is_win(self) -> bool:
        for column_idx in range(0, NR_OF_COLUMNS):
            for row_idx in range(0, 4):
                if abs(sum(self.board_state.iloc[:, column_idx][2:6])) == 4:
                    return True
        return False
