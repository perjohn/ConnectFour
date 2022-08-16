import pandas as pd


class Game:
    def __init__(self):
        self.board_state: pd.DataFrame = self._initialize_board()

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
