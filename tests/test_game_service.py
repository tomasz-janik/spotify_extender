from unittest import TestCase
from unittest.mock import MagicMock

from spotify_extender.converters.converters import Parameters
from spotify_extender.enums.time_range import TimeRange, SpotifyTimeRange
from spotify_extender.enums.top_type import TopType, SpotifyTopType
from spotify_extender.services.game_service import GameService


class TestGameService(TestCase):

    def test_start(self):
        # given
        parameter_converter = MagicMock()
        parameter_converter.convert.return_value = Parameters(SpotifyTimeRange.LONG_TERM, SpotifyTopType.TRACKS)

        request_handler = MagicMock()
        request_handler.get_all_top.return_value = ['1', '2']

        session_facade = MagicMock()

        game_service = GameService(request_handler, parameter_converter, session_facade)

        # when
        game_service.start(TimeRange.LAST_MONTH, TopType.ARTISTS)

        # then
        parameter_converter.convert.assert_called_with(TimeRange.LAST_MONTH, TopType.ARTISTS)
        request_handler.get_all_top.assert_called_with(SpotifyTimeRange.LONG_TERM, SpotifyTopType.TRACKS)
        session_facade.init_game.assert_called_with('last_month', 'artist',
                                                    [{'index': 0, 'value': '1'}, {'index': 1, 'value': '2'}])

    def test_get_single_round(self):
        # given
        parameter_converter = MagicMock()
        request_handler = MagicMock()
        session_facade = MagicMock()

        session_facade.get_statistics.return_value = [{'index': 0, 'value': {'id': 0}},
                                                      {'index': 1, 'value': {'id': 1}}]

        game_service = GameService(request_handler, parameter_converter, session_facade)

        # when
        response = game_service.get_single_round()

        # then
        session_facade.get_statistics.assert_called()
        session_facade.__setitem__.assert_called_with('correct_id', 0)
        self.assertCountEqual(response, [{'id': 0}, {'id': 1}])

    def test_check_with_correct_answer(self):
        # given
        parameter_converter = MagicMock()
        request_handler = MagicMock()
        session_facade = MagicMock()

        session_facade.correct_id = '0'

        game_service = GameService(request_handler, parameter_converter, session_facade)

        # when
        response = game_service.check('0')

        # then
        session_facade.handle_correct_answer.assert_called()
        self.assertDictEqual(response, {'success': True})

    def test_check_with_incorrect_answer(self):
        # given
        parameter_converter = MagicMock()
        request_handler = MagicMock()
        session_facade = MagicMock()

        session_facade.correct_id = '0'

        game_service = GameService(request_handler, parameter_converter, session_facade)

        # when
        response = game_service.check('1')

        # then
        session_facade.handle_incorrect_answer.assert_called()
        self.assertDictEqual(response, {'success': False})
