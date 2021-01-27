"""
    spotify_extender.request.url_builder

    This module is responsible for building
    urls to Spotify API
"""
from spotify_extender.enums.time_range import SpotifyTimeRange
from spotify_extender.enums.top_type import SpotifyTopType


class UrlBuilder:
    """
    Build urls to Spotify API
    """

    @staticmethod
    def get_top(time_range: SpotifyTimeRange, top_type: SpotifyTopType,
                offset: int, limit: int = 50) -> str:
        """Builds url to Spotify API used to get
        top artists/tracks for authorized user

        :param time_range: SpotifyTimeRange enum value
        representing time range that should be respected
        by Spotify API
        :param top_type: SpotifyTopType enum value
        representing whether to get top tracks or artists
        :param offset: integer representing offset
        :param limit: integer representing how many items
        to return in response
        :return: string representing url used in communication
        with Spotify API
        """
        return f'https://api.spotify.com/v1/me/top/{top_type.value}' \
               f'?time_range={time_range.value}' \
               f'&offset={offset}' \
               f'&limit={limit}'

    @staticmethod
    def get_refresh() -> str:
        """Builds url to Spotify API used to
        refresh tokens

        :return: string representing url used in communication
        with Spotify API
        """
        return 'https://accounts.spotify.com/api/token'

    @staticmethod
    def get_tokens() -> str:
        """Builds url to Spotify API used to
        get access tokens

        :return: string representing url used in communication
        with Spotify API
        """
        return 'https://accounts.spotify.com/api/token'

    @staticmethod
    def get_authorization() -> str:
        """Builds string to Spotify API used to
        authorize user

        :return: string representing url used in communication
        with Spotify API
        """
        return 'https://accounts.spotify.com/authorize'
