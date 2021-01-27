"""
    spotify_extender.configuration

    This module acts as a provider for all configurable dependencies
    used in spotify_extender
"""
from spotify_extender.enums.time_range import TimeRange, SpotifyTimeRange
from spotify_extender.enums.top_type import TopType, SpotifyTopType


def time_range_mapping() -> dict:
    """Provides configuration for time_range element mapping

    :return: dictionary containing mapping from time_range used
    in spotify_extender application and the one defined in Spotify API
    """
    return {
        TimeRange.ALL_TIME: SpotifyTimeRange.LONG_TERM,
        TimeRange.LAST_YEAR: SpotifyTimeRange.MEDIUM_TERM,
        TimeRange.LAST_MONTH: SpotifyTimeRange.SHORT_TERM
    }


def top_type_mapping() -> dict:
    """Provides configuration for top_type element mapping

    :return: dictionary containing mapping from top_type used
    in spotify_extender application and the one defined in Spotify API
    """
    return {
        TopType.TRACKS: SpotifyTopType.TRACKS,
        TopType.ARTISTS: SpotifyTopType.ARTISTS,
    }


def response_mapping() -> dict:
    """Provides configuration for function used to map
    elements returned as response for Spotify API call

    :return: dictionary containing mapping between Spotify
    API call type and callable used to map response returned
    by said call
    """
    return {
        SpotifyTopType.ARTISTS: __artists_response_mapping,
        SpotifyTopType.TRACKS: __tracks_response_mapping
    }


def __artists_response_mapping(item: dict) -> dict:
    """Provides configuration for mapping of top artists

    :param item: dictionary returned by Spotify API call
    for top artists
    :return: dictionary containing information used by
    spotify_extender
    """
    return {
        'id': item['id'],
        'name': item['name'],
        'image_url': item['images'][1]['url'],
        'followers': item['followers']['total']
    }


def __tracks_response_mapping(item: dict) -> dict:
    """Provides configuration for mapping of top tracks

    :param item: dictionary returned by Spotify API call
    for top tracks
    :return: dictionary containing information used by
    spotify_extender
    """
    return {
        'id': item['id'],
        'name': item['name'],
        'image_url': item['album']['images'][1]['url'],
        'artists': [artist['name'] for artist in item['artists']]
    }
