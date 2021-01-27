from unittest import TestCase
from unittest.mock import MagicMock

from spotify_extender.converters.converters import ParametersConverter, Parameters
from spotify_extender.enums.time_range import TimeRange, SpotifyTimeRange
from spotify_extender.enums.top_type import TopType, SpotifyTopType


class TestParametersConverter(TestCase):

    def setUp(self):
        # given
        time_range_mapping = MagicMock()
        time_range_mapping.__getitem__.side_effect = \
            {TimeRange.ALL_TIME: SpotifyTimeRange.LONG_TERM}.__getitem__
        top_type_mapping = MagicMock()
        top_type_mapping.__getitem__.side_effect = \
            {TopType.TRACKS: SpotifyTopType.TRACKS}.__getitem__
        self.parameters_converter = ParametersConverter(time_range_mapping, top_type_mapping)

    def test_convert(self):
        # when
        parameters = self.parameters_converter.convert(TimeRange.ALL_TIME, TopType.TRACKS)

        # then
        self.assertIsInstance(parameters, Parameters)
        self.assertEqual(parameters, Parameters(SpotifyTimeRange.LONG_TERM, SpotifyTopType.TRACKS))

    def test_convert_time_range(self):
        # when
        time_range = self.parameters_converter.convert_time_range(TimeRange.ALL_TIME)

        # then
        self.assertIsInstance(time_range, SpotifyTimeRange)
        self.assertEqual(time_range, SpotifyTimeRange.LONG_TERM)

    def test_convert_top_type(self):
        # when
        top_type = self.parameters_converter.convert_top_type(TopType.TRACKS)

        # then
        self.assertIsInstance(top_type, SpotifyTopType)
        self.assertEqual(top_type, SpotifyTopType.TRACKS)
