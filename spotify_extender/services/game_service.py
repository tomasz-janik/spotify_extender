"""
    spotify_extender.services.game_service

    This module represents game service available
    in spotify_extender application
"""
import random
from injector import inject

from spotify_extender.converters.converters import ParametersConverter, Parameters
from spotify_extender.enums.time_range import TimeRange
from spotify_extender.enums.top_type import TopType
from spotify_extender.request.request_handler import RequestHandlerFacade
from spotify_extender.session.session_facade import SessionFacade


class GameService:
    """
    Service for gaming(guessing) process available in
    spotify_extender application
    """

    @inject
    def __init__(self, request_handler: RequestHandlerFacade,
                 parameter_converter: ParametersConverter,
                 session_facade: SessionFacade):
        self.request_handler = request_handler
        self.parameter_converter = parameter_converter
        self.session_facade = session_facade

    def start(self, time_range: TimeRange, top_type: TopType) -> None:
        """Initializes the game by handling session and
        requesting top tracks/artists for authorized user

        :param time_range: TimeRange enum value representing
        time range parameter
        :param top_type: TopType enum value representing
        top type parameter
        """
        parameters: Parameters = self.parameter_converter.convert(time_range, top_type)
        response: list = \
            self.request_handler.get_all_top(parameters.time_range, parameters.top_type)
        statistics: list = \
            [{'index': index, 'value': value} for index, value in enumerate(response)]

        self.session_facade.init_game(time_range.value, top_type.value, statistics)

    def get_single_round(self) -> list:
        """Returns single round in game that is
        presented to user and saves correct id
        in session

        :return: list of artists/tracks the user has
        to pick from
        """
        statistics: list = self.session_facade.get_statistics()
        random_statistics: list = random.sample(statistics, 2)
        self.session_facade['correct_id'] = \
            min(random_statistics, key=lambda statistic: statistic['index'])['value']['id']

        return [statistic['value'] for statistic in random_statistics]  # pylint: disable=E1136

    def check(self, answer_id: str) -> dict:
        """Checks the user answer for single round
        and saves information to session about guess
        results

        :param answer_id: string representing the id of
        artist/track the user choose
        :return: dictionary containing information about
        round results
        """
        result: bool = self.__check_answer_id(answer_id)
        if result:
            self.session_facade.handle_correct_answer()
        else:
            self.session_facade.handle_incorrect_answer()

        return {'success': result}

    def __check_answer_id(self, answer_id: str) -> bool:
        """Check if answer made by user is correct

        :param answer_id: string representing the id of
        artist/track the user choose
        :return: True if user answer is correct, otherwise False
        """
        return answer_id == self.session_facade.correct_id
