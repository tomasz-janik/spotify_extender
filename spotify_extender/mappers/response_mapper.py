"""
    spotify_extender.mappers

    This module is used to configure mappers used to map
    only the specific values from responses of Spotify API
"""
from typing import Callable

from spotify_extender.configuration import configuration
from spotify_extender.enums.top_type import SpotifyTopType

response_mapping = configuration.response_mapping()


def get_mapper(response_type: SpotifyTopType) -> Callable:
    """Returns mapping function used to map specific
    SpotifyTopType

    :param response_type: SpotifyTopType Enum value representing
    top_type parameter
    :return: callable that maps items returned in result of
    Spotify API call with specified SpotifyTopType
    """
    return response_mapping[response_type]
