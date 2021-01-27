"""
    spotify_extender.session.session_Manager

    This module represents login service available
    in spotify_extender application
"""
from injector import inject

from spotify_extender.enums.time_range import TimeRange
from spotify_extender.enums.top_type import TopType
from spotify_extender.session.session_manager import SessionManager


class SessionFacade:
    """
    Facade used to make handling session
    information easier and more manageable
    """

    @inject
    def __init__(self, session_manager: SessionManager):
        self.session_manager = session_manager

    def __setitem__(self, key, value):
        self.session_manager[key] = value

    @property
    def access_token(self) -> str:
        """Returns access token from session

        :return: string representing access token
        """
        return self.session_manager['access_token']

    @property
    def refresh_token(self) -> str:
        """Returns refresh token from session

        :return: string representing refresh token
        """
        return self.session_manager['refresh_token']

    @property
    def correct_id(self) -> str:
        """Returns correct id of artist or track connected
         with single round played by user

        :return: string representing correct id
        of artist or track
        """
        return self.session_manager['correct_id']

    @correct_id.setter
    def correct_id(self, value: str) -> None:
        """Sets correct id of artist or track connected
         with single round played by user

        :param value: string representing correct id
        of artist or track
        """
        self.session_manager['correct_id'] = value

    def init_game(self, time_range: TimeRange, top_type: TopType, statistics: list) -> None:
        """Initialize the user guessing game by
        clearing session information and saving
        new ones

        :param time_range: TimeRange enum value representing
        time range parameter
        :param top_type: TopType enum value representing
        top type parameter
        :param statistics: list containing all top tracks/artists
        """
        self.session_manager['time_range'] = time_range
        self.session_manager['top_type'] = top_type
        self.session_manager[f'{time_range}_{top_type}_statistics'] = statistics
        self.session_manager.reset_variables(['correct_answer_streak', 'total_correct_answers',
                                              'total_incorrect_answers', 'total_answers'])

    def get_statistics(self) -> list:
        """Returns statistics for current time range
        and top type connected with game played by user

        :return: list containing all top tracks/artists
        """
        time_range = self.session_manager['time_range']
        top_type = self.session_manager['top_type']
        statistics = self.session_manager[f'{time_range}_{top_type}_statistics']

        return statistics

    def handle_correct_answer(self) -> None:
        """Handles user correct guess answer by
        incrementing chosen variables
        """
        self.session_manager.increment_variables(['total_answers', 'correct_answer_streak',
                                                  'total_correct_answers'])

    def handle_incorrect_answer(self) -> None:
        """Handles user incorrect guess answer by
        incrementing chosen variables
        """
        self.session_manager.increment_variables(['total_answers', 'total_incorrect_answers'])
        self.session_manager.reset_variables(['correct_answer_streak'])

    def save_tokens(self, response) -> None:
        """Saves user's tokens to session

        :param response: response from Spotify API containing
        user's tokens
        """
        self.session_manager['access_token'] = response.get('access_token')
        self.session_manager['refresh_token'] = response.get('refresh_token')
