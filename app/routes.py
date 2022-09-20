from uuid import uuid4

from fastapi import APIRouter, Response

from app.game.match import Match
from app.schema import NewMatchSchema
from app.session import session_backend, cookie

router = APIRouter()


@router.get("/new-match", response_model=NewMatchSchema)
def new_match(response: Response):
    session_token = uuid4()
    match = Match()
    session_backend.create(session_token, match)
    cookie.attach_to_response(response, session_token)
    return {'board': match.get_board_as_array()}
