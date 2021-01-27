from unittest import TestCase
from unittest.mock import MagicMock

from spotify_extender.services.login_service import LoginService


class TestLoginService(TestCase):

    def test_login(self):
        # given
        request_handler = MagicMock()
        session_facade = MagicMock()
        mocked_response = MagicMock()
        request_handler.login.return_value = mocked_response

        login_service = LoginService(request_handler, session_facade)

        # when
        response = login_service.login()

        # then
        request_handler.login.assert_called()
        mocked_response.set_cookie.assert_called()
        self.assertEqual(response, mocked_response)

    def test_handle_callback(self):
        # given
        request_handler = MagicMock()
        session_facade = MagicMock()
        request_handler.get_tokens.return_value = '0'

        login_service = LoginService(request_handler, session_facade)

        # when
        login_service.handle_callback('code')

        # then
        request_handler.get_tokens.assert_called_with('code')
        session_facade.save_tokens.assert_called_with('0')
