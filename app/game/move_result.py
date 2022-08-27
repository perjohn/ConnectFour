from enum import Enum


class MoveResult(Enum):
    OK = 0
    ILLEGAL_MOVE = 1
    WIN_RED = 2
    WIN_YELLOW = 3
