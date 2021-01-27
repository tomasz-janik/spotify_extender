from unittest import TestCase
from unittest.mock import MagicMock

import requests_mock

from spotify_extender.enums.time_range import SpotifyTimeRange
from spotify_extender.enums.top_type import SpotifyTopType
from spotify_extender.request.request_handler import RequestHandler
from wsgi import app


class TestRequestHandler(TestCase):

    def setUp(self):
        mock = MagicMock()
        self.requestHandler = RequestHandler(mock)

    def test_get_tokens(self):
        with requests_mock.Mocker() as mock:
            with app.app_context():
                # given
                expected_response = r'{"response": "response"}'
                mock.post(url='https://accounts.spotify.com/api/token',
                          text=expected_response)

                # when
                response = self.requestHandler.get_tokens('code')

                # then
                self.assertDictEqual(response, {"response": "response"})

    def test_get_top(self):
        with requests_mock.Mocker() as mock:
            with app.app_context():
                # given
                expected_response = r'{"response": "response"}'
                mock.get(url='https://api.spotify.com/v1/me/top/tracks?time_range=long_term&offset=0&limit=50',
                         text=expected_response)

                # when
                response = self.requestHandler.get_top(SpotifyTimeRange.LONG_TERM,
                                                       SpotifyTopType.TRACKS, 0)

                # then
                self.assertEqual(response.status_code, 200)

    def test_get_top_artists(self):
        with requests_mock.Mocker() as mock:
            with app.app_context():
                # given
                expected_response = r'{"response": "response"}'
                mock.get(url='https://api.spotify.com/v1/me/top/artists?time_range=long_term&offset=0&limit=50',
                         text=expected_response)

                # when
                response = self.requestHandler.get_top(SpotifyTimeRange.LONG_TERM,
                                                       SpotifyTopType.ARTISTS, 0)

                # then
                self.assertEqual(response.status_code, 200)

    def test_get_top_short_term(self):
        with requests_mock.Mocker() as mock:
            with app.app_context():
                # given
                expected_response = r'{"response": "response"}'
                mock.get(url='https://api.spotify.com/v1/me/top/tracks?time_range=short_term&offset=0&limit=50',
                         text=expected_response)

                # when
                response = self.requestHandler.get_top(SpotifyTimeRange.SHORT_TERM,
                                                       SpotifyTopType.TRACKS, 0)

                # then
                self.assertEqual(response.status_code, 200)
