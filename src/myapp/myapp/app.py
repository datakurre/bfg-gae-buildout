# -*- coding: utf-8 -*-
"""Very simple application root example"""

import os

from zope.interface import implements

from myapp.interfaces import IApplication
from myapp.utils import SimpleResponse


class Application(object):
    """Application root"""
    implements(IApplication)


root = Application()

here = os.path.dirname(__file__)

favicon_data = open(os.path.join(here, "images/favicon.ico")).read()
favicon_response = SimpleResponse(favicon_data, "image/x-icon")

robots_data = open(os.path.join(here, "robots.txt")).read()
robots_response = SimpleResponse(robots_data, "text/plain")


def get_root(request):
    return root


def favicon(context, request):
    return favicon_response


def robots(context, request):
    return robots_response


def hello_world(context, request):
    return {"title": "Hello from pyramid!"}
