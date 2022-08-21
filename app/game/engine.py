from pandas import Series

from app.game.game import Game
from app.game.move_result import MoveResult
from app.game.player import Player


class Engine:
    # def __init__(self):
    #     self.game = ConnectFourGame()

    def move(self, column: int, player: Player, game: Game) -> (MoveResult, Game):
        validation_result = self.validate(column, player, game)
        if validation_result != MoveResult.OK:
            return validation_result, game
        game = self.make_move(column, player, game)
        return validation_result, game

    def validate(self, column: int, player: Player, game: Game) -> MoveResult:
        if not -1 < column < 7:
            return MoveResult.ILLEGAL_MOVE
        sum_board_values = game.sum_board_values()
        if player == Player.RED and sum_board_values != 0:
            return MoveResult.ILLEGAL_MOVE
        elif player == Player.YELLOW and sum_board_values != 1:
            return MoveResult.ILLEGAL_MOVE
        if not self._space_left_for_player_in_row(game.get_column(column)):
            return MoveResult.ILLEGAL_MOVE
        return MoveResult.OK

    def make_move(self, column: int, player: Player, game: Game):
        game_column = game.get_column(column)
        row = self._find_row_for_move(game_column)
        game.board_state.at[row, column] = player.value
        return game

    def _space_left_for_player_in_row(self, game_column: Series) -> bool:
        zero_indexes = game_column[game_column == 0]
        return not zero_indexes.empty

    def _find_row_for_move(self, game_column: Series):
        zero_indexes = game_column[game_column == 0]
        return zero_indexes.index[-1]
