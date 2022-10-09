from http import HTTPStatus
from uuid import uuid4

from fastapi import APIRouter, Depends, Response, status

from app.game.match import Match
from app.game.move import Move
from app.game.move_result import MoveResult
from app.game.player import Player
from app.schema import NewMatchSchema
from app.session import session_backend, cookie, SessionData, verifier

router = APIRouter()


@router.get("/new-match", response_model=NewMatchSchema)
def new_match(response: Response):
    session_token = uuid4()
    match = Match()
    session_backend.create(session_token, SessionData(match=match.get_board_as_array()))
    cookie.attach_to_response(response, session_token)
    return {'board': match.get_board_as_array()}


@router.get("/move/{player}/{column}", response_model=NewMatchSchema, dependencies=[Depends(cookie)],
            status_code=status.HTTP_200_OK)
def move(player: int, column: int, response: Response, session_data: SessionData = Depends(verifier)):
    match = Match.from_array(session_data.match)
    move_result = match.move(Move(column=column, player=Player.RED if player == 1 else Player.YELLOW))
    if move_result == MoveResult.ILLEGAL_MOVE:
        response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        return {'board': match.get_board_as_array()}
    return {'board': match.get_board_as_array()}
