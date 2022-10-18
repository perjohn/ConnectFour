from pydantic import BaseModel


class MatchBaseModel(BaseModel):
    class Config:
        arbitrary_types_allowed = True


class NewMatchModel(MatchBaseModel):
    board: list[list[int]]


class MoveResultModel(NewMatchModel):
    moveResult: int
