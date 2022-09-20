import pandas as pd
from pydantic import BaseModel


class MatchSchemaBaseModel(BaseModel):
    class Config:
        arbitrary_types_allowed = True


class NewMatchSchema(MatchSchemaBaseModel):
    board: list[list[int]]
