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
        """WSGI application interface"""
        start_response(self.status, self.headerlist)
        if environ["REQUEST_METHOD"] == "HEAD":
            return []
        else:
            return self.app_iter
