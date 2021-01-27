"""
    spotify_extender.decorators

    This module is used to define decorators used to handle
    requests to spotify_extender application and both
    Spotify API requests and responses
"""
from functools import wraps
from typing import Callable

from flask import redirect, session, url_for, request
from werkzeug.exceptions import abort


def jsonify_response(function: Callable) -> Callable:
    """Decorator used to automatically get JSON
    response returned by Spotify API call

    :param function: function to decorate
    :return: decorated function
    """

    @wraps(function)
    def decorated_function(*args, **kwargs):
        return function(*args, **kwargs).json()

    return decorated_function


def redirect_logged(function: Callable) -> Callable:
    """Decorator used to automatically redirect
    user to '/start' endpoint if said user is
    already logged

    :param function: function to decorate
    :return: decorated function
    """

    @wraps(function)
    def decorated_function(*args, **kwargs):
        if 'access_token' in session:
            return redirect('/start')
        return function(*args, **kwargs)

    return decorated_function


def success_status_code_required(function: Callable) -> Callable:
    """Decorator used to automatically check
    whether response code of request made to
    Spotify API is successful

    :param function: function to decorate
    :return: decorated function
    """

    @wraps(function)
    def decorated_function(*args, **kwargs):
        response = function(*args, **kwargs)
        if response.status_code != 200:
            abort(response.status_code)
        return response

    return decorated_function


def tokens_required(function: Callable) -> Callable:
    """Decorator used to automatically redirect
    user to '/login' endpoint if said user is not
    already logged

    :param function: function to decorate
    :return: decorated function
    """

    @wraps(function)
    def decorated_function(*args, **kwargs):
        if 'access_token' not in session:
            return redirect(url_for('.login', next=request.url))
        return function(*args, **kwargs)

    return decorated_function
