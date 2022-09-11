import uvicorn

from app import config
from app.config import Environment

if __name__ == "__main__":
    auto_reload = config.environment() == Environment.LOCAL.value
    uvicorn.run('app.app:app', host=config.app_host(), port=config.app_port(), reload=auto_reload, lifespan='on')
