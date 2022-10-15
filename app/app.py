from fastapi import FastAPI
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware

from app import routes

middleware = [
    Middleware(
        TrustedHostMiddleware,
        allowed_hosts=['*'],
    ),
    Middleware(SessionMiddleware, secret_key='p1ndar0ts')
]

app = FastAPI(middleware=middleware)


def _configure_routes():
    api_version_prefix = '/api/v1'
    app.include_router(routes.router, prefix=api_version_prefix)


_configure_routes()
