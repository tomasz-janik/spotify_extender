"""
    spotify_extender.services.login_service

    This module represents login service available
    in spotify_extender application
"""
import secrets
import string

import flask
import requests
from injector import inject

from spotify_extender.request.request_handler import RequestHandlerFacade
from spotify_extender.session.session_facade import SessionFacade


class LoginService:
    """
    Service for logging and handling
    callback from Spotify API
    """

    @inject
    def __init__(self, request_handler: RequestHandlerFacade, session_facade: SessionFacade):
        self.request_handler = request_handler
        self.session_facade = session_facade

    def login(self) -> flask.Response:
        """Handles login request to spotify_extender
        application and generates login request to
        Spotify API

        :return: response redirecting login request
        to Spotify API
        """
        state: str = self.__generate_state()
        response: flask.Response = self.request_handler.login(state)
        response.set_cookie('spotify_auth_state', state)

        return response

    def handle_callback(self, code) -> None:
        """Handles callback that is send to
        spotify_extender application when user
        has successfully authorized into Spotify API

        :param code: string returned by Spotify while
        callback application to authorize user
        """
        response: requests.models.Response = self.request_handler.get_tokens(code)
        self.session_facade.save_tokens(response)

    @staticmethod
    def __generate_state() -> str:
        """Generates state string used as protection from
        cross-site request forgery.

        :return: string representing state
        """
        return ''.join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(16))
