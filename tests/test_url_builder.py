from unittest import TestCase

from spotify_extender.enums.time_range import SpotifyTimeRange
from spotify_extender.enums.top_type import SpotifyTopType
from spotify_extender.request.url_builder import UrlBuilder


class TestUrlBuilder(TestCase):

    def test_get_top_long_term(self):
        # given

        # when
        url = UrlBuilder.get_top(SpotifyTimeRange.LONG_TERM, SpotifyTopType.TRACKS, 0)
        # then
        self.assertEqual(url, 'https://api.spotify.com/v1/me/top/tracks?time_range=long_term&offset=0&limit=50')

    def test_get_top_medium_term(self):
        # given

        # when
        url = UrlBuilder.get_top(SpotifyTimeRange.MEDIUM_TERM, SpotifyTopType.TRACKS, 0)
        # then
        self.assertEqual(url, 'https://api.spotify.com/v1/me/top/tracks?time_range=medium_term&offset=0&limit=50')

    def test_get_top_short_term(self):
        # given

        # when
        url = UrlBuilder.get_top(SpotifyTimeRange.SHORT_TERM, SpotifyTopType.TRACKS, 0)
        # then
        self.assertEqual(url, 'https://api.spotify.com/v1/me/top/tracks?time_range=short_term&offset=0&limit=50')

    def test_get_top_artists(self):
        # given

        # when
        url = UrlBuilder.get_top(SpotifyTimeRange.SHORT_TERM, SpotifyTopType.ARTISTS, 0)
        # then
        self.assertEqual(url, 'https://api.spotify.com/v1/me/top/artists?time_range=short_term&offset=0&limit=50')

    def test_get_refresh(self):
        # given

        # when
        url = UrlBuilder.get_refresh()
        # then
        self.assertEqual(url, 'https://accounts.spotify.com/api/token')

    def test_get_tokens(self):
        # given

        # when
        url = UrlBuilder.get_tokens()
        # then
        self.assertEqual(url, 'https://accounts.spotify.com/api/token')

    def test_get_authorization(self):
        # given

        # when
        url = UrlBuilder.get_authorization()
        # then
        self.assertEqual(url, 'https://accounts.spotify.com/authorize')
