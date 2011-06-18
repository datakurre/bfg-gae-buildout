# -*- coding: utf-8 -*-
"""A few generic utilities"""


# http://bfg.repoze.org/pastebin/684
class SimpleResponse:
    """Faster than webob.Response"""
    status = "200 OK"

    def __init__(self, body, content_type="text/html"):
        self.app_iter = [body]
        self.headerlist = [("Content-Type", content_type),
                           ("Content-Length", str(len(body)))]