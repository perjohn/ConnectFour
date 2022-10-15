from fastapi import APIRouter, Depends, Response, status, Request

from app.bot.bot_factory import create_bot
from app.game.match import Match
from app.game.move import Move
from app.game.move_result import MoveResult
from app.game.player import Player
from app.schema import NewMatchSchema

router = APIRouter()


@router.get("/new-match/{player_type}/{bot_type}", response_model=NewMatchSchema)
def new_match(player_type: int, bot_type: int, response: Response, request: Request):
    match = Match()
    if player_type != 1 and player_type != -1:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {'board': match.get_board_as_array()}
    if Player(player_type) == Player.YELLOW:
        bot = create_bot(bot_type, game=match.engine.game)
        match.move(bot.calculate_move(Player.RED))
    request.session['match'] = match.get_board_as_array()
    request.session['bot_type'] = bot_type
    return {'board': match.get_board_as_array()}


@router.get("/move/{player}/{column}", response_model=NewMatchSchema, status_code=status.HTTP_200_OK)
def move(player: int, column: int, response: Response, request: Request):
    match = Match.from_array(request.session['match'])
    move_result = match.move(Move(column=column, player=Player.RED if player == 1 else Player.YELLOW))
    if move_result == MoveResult.ILLEGAL_MOVE:
        response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        return {'board': match.get_board_as_array()}
    request.session['match'] = match.get_board_as_array()
    return {'board': match.get_board_as_array()}
