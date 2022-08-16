import pandas as pd

from app.game.player import Player


class Game:
    def __init__(self):
        self.board_state: pd.DataFrame = self._initialize_board()

    def move(self, row: int, player: Player):
        pass

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
