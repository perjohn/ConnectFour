import pandas as pd
from pandas import Series

from app.game.player import Player

NR_OF_COLUMNS = 7
NR_OF_ROWS = 6


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
        # vertical
        for column_idx in range(0, NR_OF_COLUMNS):
            for row_idx in range(0, 3):
                if abs(sum(self.board_state.iloc[:, column_idx][row_idx:row_idx + 4])) == 4:
                    return True
        # horizontal
        for row_idx in range(0, NR_OF_ROWS):
            for column_idx in range(0, 4):
                if abs(sum(self.board_state.iloc[row_idx, :][column_idx:column_idx + 4])) == 4:
                    return True

        # diagonal down
        for col_idx in range(0, 4):
            for row_idx in range(0, 3):
                diag_sum = 0
                for i in range(0, 4):
                    diag_sum += self.board_state.at[row_idx + i, col_idx + i]
                if abs(diag_sum) == 4:
                    return True

        # diagonal up
        for col_idx in range(0, 4):
            for row_idx in range(5, 2, -1):
                diag_sum = 0
                for i in range(0, 4):
                    diag_sum += self.board_state.at[row_idx - i, col_idx + i]
                if abs(diag_sum) == 4:
                    return True
        return False

    def is_draw(self):
        return 0 not in self.board_state.values

    def space_left_for_player_in_column(self, column: int) -> bool:
        game_column = self.get_column(column)
        zero_indexes = game_column[game_column == 0]
        return not zero_indexes.empty
