from app.game.game import Game
from app.game.move_result import MoveResult
from app.game.player import Player


class Engine:
    # def __init__(self):
    #     self.game = ConnectFourGame()

    def move(self, row: int, player: Player, game: Game) -> (MoveResult, Game):
        if not -1 < row < 7:
            return MoveResult.ILLEGAL_MOVE, game
        sum_board_values = game.sum_board_values()
        if player == Player.RED and sum_board_values != 0:
            return MoveResult.ILLEGAL_MOVE, game
        elif player == Player.YELLOW and sum_board_values != 1:
            return MoveResult.ILLEGAL_MOVE, game

    def validate(self, row: int, player: Player, game: Game) -> MoveResult:
        if not -1 < row < 7:
            return MoveResult.ILLEGAL_MOVE
        sum_board_values = game.sum_board_values()
        if player == Player.RED and sum_board_values != 0:
            return MoveResult.ILLEGAL_MOVE
        elif player == Player.YELLOW and sum_board_values != 1:
            return MoveResult.ILLEGAL_MOVE
        return MoveResult.OK
