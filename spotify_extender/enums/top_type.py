"""
    spotify_extender.enums.top_type

    This module is used to define Enums used to handle
    parameter top_type connected with time range for
    both spotify_extender application and Spotify API
"""
from enum import Enum


class TopType(Enum):
    """
    Enum used to represent top_type parameter in
    spotify_extender application
    """
    TRACKS = 'track'
    ARTISTS = 'artist'


class SpotifyTopType(Enum):
    """
    Enum used to represent top_type parameter in
    Spotify API
    """
    TRACKS = 'tracks'
    ARTISTS = 'artists'
