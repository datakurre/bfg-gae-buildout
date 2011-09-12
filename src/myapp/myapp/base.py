from zope.interface import implements

from repoze.bfg.interfaces import IResponse


class SimpleResponse(object):
    """Faster than webob.Response"""
    # http://bfg.repoze.org/pastebin/684

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


import os
here = os.path.dirname(__file__)
icon = open(os.path.join(here, "images/favicon.ico")).read()
icon_response = SimpleResponse(icon, "image/x-icon")


def favicon(context, request):
    return icon_response


def robots(context, request):
    return SimpleResponse("")
