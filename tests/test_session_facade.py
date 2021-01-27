from unittest import TestCase
from unittest.mock import MagicMock, call

from spotify_extender.enums.time_range import TimeRange
from spotify_extender.enums.top_type import TopType
from spotify_extender.session.session_facade import SessionFacade


class TestSessionFacade(TestCase):

    def test_access_token(self):
        # given
        session_manager = MagicMock()
        session_manager.__getitem__.return_value = '0'

        session_facade = SessionFacade(session_manager)

        # when
        response = session_facade.access_token

        # then
        session_manager.__getitem__.assert_called_with('access_token')
        self.assertEqual(response, '0')

    def test_refresh_token(self):
        # given
        session_manager = MagicMock()
        session_manager.__getitem__.return_value = '0'

        session_facade = SessionFacade(session_manager)

        # when
        response = session_facade.refresh_token

        # then
        session_manager.__getitem__.assert_called_with('refresh_token')
        self.assertEqual(response, '0')

    def test_correct_id_get(self):
        # given
        session_manager = MagicMock()
        session_manager.__getitem__.return_value = '0'

        session_facade = SessionFacade(session_manager)

        # when
        response = session_facade.correct_id

        # then
        session_manager.__getitem__.assert_called_with('correct_id')
        self.assertEqual(response, '0')

    def test_correct_id_set(self):
        # given
        session_manager = MagicMock()

        session_facade = SessionFacade(session_manager)

        # when
        session_facade.correct_id = '0'

        # then
        session_manager.__setitem__.assert_called_with('correct_id', '0')

    def test_init_game(self):
        # given
        session_manager = MagicMock()

        session_facade = SessionFacade(session_manager)

        # when
        session_facade.init_game(TimeRange.ALL_TIME, TopType.TRACKS, ['0', '1'])

        # then
        session_manager.__setitem__.assert_has_calls([
            call('time_range', TimeRange.ALL_TIME),
            call('top_type', TopType.TRACKS)],
            call('TimeRange.ALL_TIME_TopType.TRACKS_statistics', ['0', '1']))

        session_manager.reset_variables.assert_called_with([
            'correct_answer_streak', 'total_correct_answers',
            'total_incorrect_answers', 'total_answers'])

    def test_get_statistics(self):
        # given
        session_manager = MagicMock()
        session_manager.__getitem__.return_value = '0'

        session_facade = SessionFacade(session_manager)

        # when
        response = session_facade.get_statistics()

        # then
        session_manager.__getitem__.assert_has_calls([
            call('time_range'),
            call('top_type'),
            call('0_0_statistics')])
        self.assertEqual(response, '0')

    def test_handle_correct_answer(self):
        # given
        session_manager = MagicMock()

        session_facade = SessionFacade(session_manager)

        # when
        session_facade.handle_correct_answer()

        # then
        session_manager.increment_variables.assert_called_with([
            'total_answers', 'correct_answer_streak',
            'total_correct_answers'])

    def test_handle_incorrect_answer(self):
        # given
        session_manager = MagicMock()

        session_facade = SessionFacade(session_manager)

        # when
        session_facade.handle_incorrect_answer()

        # then
        session_manager.increment_variables.assert_called_with(['total_answers', 'total_incorrect_answers'])
        session_manager.reset_variables.assert_called_with(['correct_answer_streak'])

    def test_save_tokens(self):
        # given
        session_manager = MagicMock()

        session_facade = SessionFacade(session_manager)

        # when
        session_facade.save_tokens({'access_token': 0, 'refresh_token': 1})

        # then
        session_manager.__setitem__.assert_has_calls([
            call('access_token', 0),
            call('refresh_token', 1)
        ])
