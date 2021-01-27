"""
    spotify_extender.dependencies

    This module acts as a configuration of dependency injector container
    used in spotify_extender
"""
from injector import singleton, Binder

from spotify_extender.configuration.configuration import time_range_mapping, top_type_mapping
from spotify_extender.converters.converters import ParametersConverter
from spotify_extender.request.request_handler import RequestHandlerProxy
from spotify_extender.session.session_manager import SessionManager


def configure(binder: Binder) -> None:
    """Configures the  container used for dependency injection process

    :param binder: injector Binder used to bind interfaces to implementations.
    :return: None
    """
    binder.bind(SessionManager, to=SessionManager, scope=singleton)
    binder.bind(RequestHandlerProxy, to=RequestHandlerProxy, scope=singleton)
    binder.bind(ParametersConverter, to=provide_parameters_converter(), scope=singleton)


def provide_parameters_converter() -> ParametersConverter:
    """Creates and configures ParameterConverter object

    :return: configured ParameterConverter initialized object
    """
    parameters_converter = ParametersConverter(time_range_mapping(), top_type_mapping())
    return parameters_converter
