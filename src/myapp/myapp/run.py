# -*- coding: utf-8 -*-
"""WSGI application wrapper"""

import pyramid_zcml

from pyramid.config import Configurator
from myapp.app import get_root


def wsgi_app(**settings):
    config = Configurator(root_factory=get_root, settings=settings, autocommit=True)
    config.include(pyramid_zcml)
    config.load_zcml("configure.zcml")
    return config.make_wsgi_app()