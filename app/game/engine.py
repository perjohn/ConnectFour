from pandas import Series

from app.game.game import Game
from app.game.move_result import MoveResult
from app.game.player import Player


class Engine:
    def __init__(self):
        self.game = Game()

    def move(self, column: int, player: Player) -> (MoveResult, Game):
        move_result = self.validate(column, player)
        if move_result != MoveResult.OK:
            return move_result, self.game
        self.make_move(column, player)
        if self.is_win():
            move_result = MoveResult.WIN_RED if player == Player.RED else MoveResult.WIN_YELLOW
        return move_result, self.game

    def validate(self, column: int, player: Player) -> MoveResult:
        if not -1 < column < 7:
            return MoveResult.ILLEGAL_MOVE
        sum_board_values = self.game.sum_board_values()
        if player == Player.RED and sum_board_values != 0:
            return MoveResult.ILLEGAL_MOVE
        elif player == Player.YELLOW and sum_board_values != 1:
            return MoveResult.ILLEGAL_MOVE
        if not self.game.space_left_for_player_in_column(column):
            return MoveResult.ILLEGAL_MOVE
        return MoveResult.OK

    def is_win(self) -> bool:
        return self.game.is_win()

    def make_move(self, column: int, player: Player):
        self.game.move(column, player)
