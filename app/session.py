from typing import Dict
from uuid import UUID

from fastapi import HTTPException
from fastapi_sessions.backends.implementations import InMemoryBackend
from fastapi_sessions.frontends.implementations import CookieParameters, SessionCookie
from fastapi_sessions.session_verifier import SessionVerifier
from pydantic import BaseModel

from app.game.match import Match


class SessionData(BaseModel):
    match: list[list[int]]


class InMemorySessionStore:
    def __init__(self) -> None:
        self.data: Dict[UUID, SessionData] = {}

    def create(self, session_id: UUID, session_data: SessionData):
        if self.data.get(session_id):
            raise RuntimeError("create can't overwrite an existing session")

        self.data[session_id] = session_data.copy(deep=True)

    async def read(self, session_id: UUID):
        session_data = self.data.get(session_id)
        if not session_data:
            return

        return session_data.copy(deep=True)


cookie_params = CookieParameters()

# Uses UUID
cookie = SessionCookie(
    cookie_name="connect-four-cookie",
    identifier="general_verifier",
    auto_error=True,
    secret_key="DONOTUSE",
    cookie_params=cookie_params,
)
session_backend = InMemorySessionStore()


class BasicVerifier(SessionVerifier[UUID, SessionData]):
    def __init__(
            self,
            *,
            identifier: str,
            auto_error: bool,
            backend: InMemoryBackend[UUID, SessionData],
            auth_http_exception: HTTPException,
    ):
        self._identifier = identifier
        self._auto_error = auto_error
        self._backend = backend
        self._auth_http_exception = auth_http_exception

    @property
    def identifier(self):
        return self._identifier

    @property
    def backend(self):
        return self._backend

    @property
    def auto_error(self):
        return self._auto_error

    @property
    def auth_http_exception(self):
        return self._auth_http_exception

    def verify_session(self, model: SessionData) -> bool:
        """If the session exists, it is valid"""
        return True


verifier = BasicVerifier(
    identifier="general_verifier",
    auto_error=True,
    backend=session_backend,
    auth_http_exception=HTTPException(status_code=403, detail="invalid session"),
)
