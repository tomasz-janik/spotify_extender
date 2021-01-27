"""
    spotify_extender.enums.time_range

    This module is used to define Enums used to handle
    parameter time_range connected with time range for
    both spotify_extender application and Spotify API
"""
from enum import Enum


class TimeRange(Enum):
    """
    Enum used to represent time_range parameter in
    spotify_extender application
    """
    ALL_TIME = 'all_time'
    LAST_YEAR = 'last_year'
    LAST_MONTH = 'last_month'


class SpotifyTimeRange(Enum):
    """
    Enum used to represent time_range parameter in
    Spotify API
    """
    LONG_TERM = 'long_term'
    MEDIUM_TERM = 'medium_term'
    SHORT_TERM = 'short_term'
