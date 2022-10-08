from uuid import uuid4

from fastapi import APIRouter, Response, Depends

from app.game.match import Match
from app.game.move import Move
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


@router.get("/move/{player}/{column}", response_model=NewMatchSchema, dependencies=[Depends(cookie)])
def move(player: int, column: int, session_data: SessionData = Depends(verifier)):
    match = Match.from_array(session_data.match)
    match.move(Move(column=column, player=Player.RED if player == 1 else Player.YELLOW))
    return {'board': match.get_board_as_array()}
