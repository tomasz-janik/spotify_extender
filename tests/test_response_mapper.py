import types
from unittest import TestCase

from spotify_extender.enums.top_type import SpotifyTopType
from spotify_extender.mappers.response_mapper import get_mapper


class TestResponseMapper(TestCase):

    def test_get_mapper(self):
        # given
        # when
        response = get_mapper(SpotifyTopType.ARTISTS)

        # then
        self.assertIsInstance(response, types.FunctionType)
