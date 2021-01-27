"""
    spotify_extender.views

    This module sda as a configuration of behaviour of all
    available endpoints in spotify_extender application
"""
from flask import Blueprint, render_template, request, session
from injector import inject
from werkzeug import Response
from werkzeug.utils import redirect

from spotify_extender.decorators.decorators import redirect_logged, tokens_required
from spotify_extender.enums.time_range import TimeRange
from spotify_extender.enums.top_type import TopType
from spotify_extender.services.game_service import GameService
from spotify_extender.services.login_service import LoginService

blueprint: Blueprint = Blueprint('', __name__)


@blueprint.route('/')
@redirect_logged
def index() -> str:
    """Handles '/' (initial) request to application, might redirect
    to '/start' if user is already logged using Spotify API

    :return: server-side rendered template as a String
    """
    return render_template('index.html')


@blueprint.route('/contact')
def contact() -> str:
    """Handles '/contact' request to application

    :return: server-side rendered template as a String
    """
    return render_template('contact.html')


@inject
@blueprint.route('/login')
def login(login_service: LoginService) -> str:
    """Handles '/login' request to application

    :return: server-side rendered template as a String
    """
    return login_service.login()


@inject
@blueprint.route('/callback')
def callback(login_service: LoginService) -> Response:
    """Handles '/callback' request to application.

    Said request is fired after user has successfully
    logged into Spotify account.

    :return: server-side rendered template as a String
    """
    login_service.handle_callback(code=request.args.get('code'))
    return redirect('/start')


@blueprint.route('/start')
@tokens_required
def start() -> str:
    """Handles '/start' request to application, might redirect
    to '/login' if user doesn't have tokens available in session

    :return: server-side rendered template as a String
    """
    return render_template('start.html')


@inject
@blueprint.route('/play')
@tokens_required
def play(game_service: GameService) -> str:
    """Handles '/play' request to application, might redirect
    to '/login' if user doesn't have tokens available in session

    Request url arguments required to successfully handle said
    request are: 'time_range' and 'top_type'

    :return: server-side rendered template as a String
    """
    time_range = TimeRange(request.args['time_range'])
    top_type = TopType(request.args['top_type'])
    game_service.start(time_range, top_type)

    return render_template('play.html')


@inject
@blueprint.route('/round')
@tokens_required
def single_round(game_service: GameService) -> str:
    """Handles '/round' request to application, might redirect
    to '/login' if user doesn't have tokens available in session

    :return: server-side rendered template as a String
    that contain information about a single round
    """
    response = game_service.get_single_round()
    return render_template('round/round.html', response=response, top_type=session['top_type'])


@inject
@blueprint.route('/check', methods=['POST'])
@tokens_required
def check(game_service: GameService) -> str:
    """Handles '/check' request to application, might redirect
    to '/login' if user doesn't have tokens available in session

    :return: server-side rendered template as a String
    that contain information about the results of a single round
    """
    response = game_service.check(request.json)
    return render_template('response/response.html', response=response)
