from unittest import TestCase

from flask import current_app

import config
from spotify_extender.request.request_factory import RequestFactory
from wsgi import app


class TestRequestFactory(TestCase):

    def setUp(self):
        self.request_factory = RequestFactory()

    def test_build_authorization_header(self):
        # given
        token = 'token'

        # when
        response = self.request_factory.build_authorization_header(token)

        # then
        self.assertDictEqual(response, {'Authorization': f'Bearer {token}'})

    def test_build_content_type_header(self):
        # given

        # when
        response = self.request_factory.build_content_type_header()

        # then
        self.assertDictEqual(response, {'Content-Type': 'application/x-www-form-urlencoded'})

    def test_build_refresh_payload(self):
        # given
        token = 'token'

        # when
        response = self.request_factory.build_refresh_payload(token)

        # then
        self.assertDictEqual(response, {
            'grant_type': 'refresh_token',
            'refresh_token': token
        })

    def test_build_tokens_request(self):
        with app.app_context():
            # given
            code = 'code'

            # when
            response = self.request_factory.build_tokens_request(code)

            # then
            self.assertDictEqual(response, {
                'grant_type': 'authorization_code',
                'code': code,
                'redirect_uri': current_app.config.get('REDIRECT_URI'),
            })

    def test_build_authorization_request(self):
        with app.app_context():
            # given
            state = 'state'

            # when
            response = self.request_factory.build_authorization_request(state)

            # then
            self.assertDictEqual(response, {
                'client_id': current_app.config.get('CLIENT_ID'),
                'response_type': 'code',
                'redirect_uri': current_app.config.get('REDIRECT_URI'),
                'state': state,
                'scope': 'user-read-private user-read-email user-top-read',
                'show_dialog': 'true'
            })

    def test_build_auth(self):
        with app.app_context():
            # given
            token = 'token'

            # when
            response = self.request_factory.build_auth()

            # then
            self.assertEqual(response, (config.Config.CLIENT_ID, config.Config.CLIENT_SECRET))
