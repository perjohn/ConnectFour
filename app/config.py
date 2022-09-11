import os

from enum import Enum


def environment():
    return os.getenv('ENVIRONMENT')


def app_host():
    return os.getenv('APP_HOST', '0.0.0.0')


def app_port():
    return int(os.getenv('APP_PORT', 8000))


class Environment(Enum):
    LOCAL = 'local'
    DEVELOPMENT = "development"
    STAGING = "staging"
    PRODUCTION = "production"
