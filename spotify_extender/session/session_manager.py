"""
    spotify_extender.session.session_Manager

    This module represents login service available
    in spotify_extender application
"""
from flask import session


class SessionManager:
    """
    Handles information about user's session
    """

    def __getitem__(self, key):
        return session[key]

    def __setitem__(self, key, value):
        session[key] = value

    @staticmethod
    def reset_variables(variables: list) -> None:
        """Resets (sets to 0) all variables passed
        as parameters

        :param variables: string representing variables names
        """
        for variable in variables:
            session[variable] = 0

    @staticmethod
    def increment_variables(variables: list) -> None:
        """Increments (by one) all variables passed
        as parameters

        :param variables: string representing variables names
        """
        for variable in variables:
            session[variable] += 1
