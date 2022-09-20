from fastapi import FastAPI

from app import routes

app = FastAPI()


def _configure_routes():
    api_version_prefix = '/api/v1'
    app.include_router(routes.router, prefix=api_version_prefix)


_configure_routes()
