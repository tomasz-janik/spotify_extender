"""
    spotify_extender.converters

    This module is used to perform conversion between
    elements used in spotify_extender application and Spotify API
"""
from collections import namedtuple

from spotify_extender.enums.time_range import TimeRange, SpotifyTimeRange
from spotify_extender.enums.top_type import TopType, SpotifyTopType

Parameters = namedtuple('Parameters', 'time_range top_type')


class ParametersConverter:
    """
    Converter between time_range and top_type parameters
    """

    def __init__(self, time_range_mapping: dict, top_type_mapping: dict):
        self.time_range_mapping = time_range_mapping
        self.top_type_mapping = top_type_mapping

    def convert(self, time_range: TimeRange, top_type: TopType) -> Parameters:
        """Converts both time_range and top_type from spotify_extender
        format to Spotify API format

        :param time_range: TimeRange Enum value representing time_range parameter
        :param top_type: TopType Enum value representing top_type parameter
        :return: namedtuple of both time_range and top_type parameters in
        Spotify API representation
        """
        return Parameters(self.convert_time_range(time_range),
                          self.convert_top_type(top_type))

    def convert_time_range(self, time_range: TimeRange) -> SpotifyTimeRange:
        """Converts time_range parameter between spotify_extender
        and Spotify API format

        :param time_range: TimeRange Enum value representing time_range parameter
        :return: SpotifyTimeRange Enum value representing time_range parameter
        in Spotify API representation
        """
        return self.time_range_mapping[time_range]

    def convert_top_type(self, top_type: TopType) -> SpotifyTopType:
        """Converts top_type parameter between spotify_extender
        and Spotify API format

        :param top_type: TopType Enum value representing time_range parameter
        :return: SpotifyTopType Enum value representing time_range parameter
        in Spotify API representation
        """
        return self.top_type_mapping[top_type]
