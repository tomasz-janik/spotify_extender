from unittest import TestCase
from unittest.mock import MagicMock

from werkzeug.exceptions import HTTPException

from spotify_extender.decorators.decorators import jsonify_response, success_status_code_required
from wsgi import app


class TestDecorators(TestCase):

    def test_jsonify_response(self):
        # given
        mock = MagicMock()
        response_mock = MagicMock()
        mock.json = response_mock

        @jsonify_response
        def func():
            return mock

        # when
        func()

        # then
        response_mock.assert_called_once()

    def test_redirect_logged_when_access_token(self):
        with app.test_client() as application:
            # given
            with application.session_transaction() as session:
                session['access_token'] = 'value'

            # when
            response = application.get('/')

            # then
            self.assertEqual(response.status_code, 302)

    def test_redirect_logged_when_no_access_token(self):
        with app.test_client() as application:
            # given

            # when
            response = application.get('/')

            # then
            self.assertEqual(response.status_code, 200)

    def test_success_status_code_required_when_successful(self):
        # given
        mock = MagicMock()
        mock.status_code = 200

        @success_status_code_required
        def func():
            return mock

        # when
        response = func()

        # then
        self.assertEqual(response, mock)

    def test_success_status_code_required_when_unsuccessful(self):
        # given
        mock = MagicMock()
        mock.status_code = 400

        @success_status_code_required
        def func():
            return mock

        # when & then
        with self.assertRaises(HTTPException):
            func()

    def test_tokens_required_when_token(self):
        with app.test_client() as application:
            # given
            with application.session_transaction() as session:
                session['access_token'] = 'value'

            # when
            response = application.get('/start')

            # then
            self.assertEqual(response.status_code, 200)

    def test_tokens_required_when_no_token(self):
        with app.test_client() as application:
            # given

            # when
            response = application.get('/start')

            # then
            self.assertEqual(response.status_code, 302)
