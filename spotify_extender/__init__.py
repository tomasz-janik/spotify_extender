"""
spotify_extender

This module handles spotify_extender app initialization and configuration.

"""
import flask
from flask import Flask
from flask_injector import FlaskInjector
from flask_session import Session

import config
from spotify_extender.dependencies import configure


def create_app() -> flask.app.Flask:
    """Creates and configures flask application.

    Acts as a application factory.

    :return: configured flask application
    """
    app = Flask(__name__, static_url_path='', static_folder='web/static',
                template_folder='web/templates')
    app.config.from_object(config.Config)
    Session(app)

    with app.app_context():
        from . import views  # pylint: disable-all
        app.register_blueprint(views.blueprint)

    FlaskInjector(app=app, modules=[configure])
    return app
