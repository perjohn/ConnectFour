from app.bot.bot import Bot
from app.bot.one_ply_bot import OnePlyBot
from app.bot.random_bot import RandomBot
from app.bot.test_bot import TestBot
from app.game.game import Game


def create_bot(bot_type: int, game: Game) -> Bot:
    if bot_type == RandomBot.TYPE:
        return RandomBot(game)
    elif bot_type == OnePlyBot.TYPE:
        return OnePlyBot(game)
    elif bot_type == TestBot.TYPE:
        return TestBot(game)
    raise RuntimeError(f'Unexpected bot type {bot_type}')
