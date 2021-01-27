"""
    config

    This module acts as a configuration for flask application
"""
import os

import redis


class Config:
    SESSION_TYPE = os.getenv('SESSION_TYPE')
    SESSION_REDIS = redis.from_url(os.getenv('SESSION_REDIS'))
    FLASK_ENV = os.getenv('FLASK_ENV')
    FLASK_DEBUG = os.getenv('FLASK_DEBUG')
    CLIENT_ID = os.getenv('CLIENT_ID')
    CLIENT_SECRET = os.getenv('CLIENT_SECRET')
    REDIRECT_URI = os.getenv('REDIRECT_URI')
    SECRET_KEY = os.getenv('SECRET_KEY')
