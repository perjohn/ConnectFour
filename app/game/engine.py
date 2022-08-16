from app.game.game import Game
from app.game.move_result import MoveResult
from app.game.player import Player


class Engine:
    # def __init__(self):
    #     self.game = ConnectFourGame()

    def move(self, row: int, player: Player, game: Game) -> (MoveResult, Game):
        validation_result = self.validate(row, player, game)
        if validation_result != MoveResult.OK:
            return validation_result, game
        game = self.make_move(row, player, game)
        return validation_result, game

    def validate(self, row: int, player: Player, game: Game) -> MoveResult:
        if not -1 < row < 7:
            return MoveResult.ILLEGAL_MOVE
        sum_board_values = game.sum_board_values()
        if player == Player.RED and sum_board_values != 0:
            return MoveResult.ILLEGAL_MOVE
        elif player == Player.YELLOW and sum_board_values != 1:
            return MoveResult.ILLEGAL_MOVE
        return MoveResult.OK

    def make_move(self, row, player, game):
        pass
