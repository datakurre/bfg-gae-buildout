# -*- coding: utf-8 -*-
"""Common utilities"""

from zope.interface import implements

from pyramid.interfaces import IResponse


class SimpleResponse(object):
    """Faster than webob.Response"""

    implements(IResponse)

    status = "200 OK"

    def __init__(self, body, content_type="text/html"):
        self.app_iter = [body]
        self.headerlist = [("Content-Type", content_type),
                           ("Content-Length", str(len(body)))]

    def __call__(self, environ, start_response):
        return self.app_iter