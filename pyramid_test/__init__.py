"""Initializer."""

from pyramid.config import Configurator
from pyramid_test.models import comment  # noqa
from pyramid_test.models import post  # noqa


def main(global_config, **settings):
    """Return a Pyramid WSGI application."""
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.include('.models')
    config.include('.routes')
    config.scan()
    return config.make_wsgi_app()
