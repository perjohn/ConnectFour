from fastapi import APIRouter, Depends, Response, status, Request, Path

from app.bot.bot_factory import create_bot
from app.game.match import Match
from app.game.move import Move
from app.game.move_result import MoveResult
from app.game.player import Player
from app.model import NewMatchModel, MoveResultModel

router = APIRouter()


@router.get("/new-match/{player_type}/{bot_type}", response_model=NewMatchModel)
def new_match(*, player_type: str = Path(regex='(-1|1)'), bot_type: int, request: Request):
    player_type = int(player_type)
    match = Match()
    if Player(player_type) == Player.YELLOW:
        bot = create_bot(bot_type, game=match.engine.game)
        match.move(bot.calculate_move(Player.RED))
    request.session['match'] = match.get_board_as_array()
    request.session['bot_type'] = bot_type
    return {'board': match.get_board_as_array()}


@router.get("/move/{player_type}/{column}", response_model=MoveResultModel, status_code=status.HTTP_200_OK)
def move(*, player_type: str = Path(regex='(-1|1)'), column: int, response: Response, request: Request):
    player_type = int(player_type)
    match = Match.from_array(request.session['match'])
    bot_type = request.session['bot_type']
    move_result = match.move(Move(column=column, player=Player.RED if player_type == 1 else Player.YELLOW))
    if move_result == MoveResult.ILLEGAL_MOVE:
        response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        return MoveResultModel(board=match.get_board_as_array(), moveResult=move_result.value)
    elif move_result == MoveResult.WIN_RED or move_result == MoveResult.WIN_YELLOW:
        request.session['match'] = match.get_board_as_array()
        return MoveResultModel(board=match.get_board_as_array(), moveResult=move_result.value)
    bot = create_bot(bot_type, game=match.engine.game)
    move_result = match.move(bot.calculate_move(Player.YELLOW if Player(player_type) == Player.RED else Player.YELLOW))
    request.session['match'] = match.get_board_as_array()
    return MoveResultModel(board=match.get_board_as_array(), moveResult=move_result.value)
