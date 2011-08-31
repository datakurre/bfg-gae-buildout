# Monkeypatches to enable pyramid within GAE
import os; os.mkdir = None  # GAE has no os.mkdir
import pkg_resources  # Fixes "pkg_resources" is not defined error on SDK
if hasattr(os, "__loader__"):
    pkg_resources.register_loader_type(
        type(os.__loader__), pkg_resources.DefaultProvider)

from google.appengine.ext.webapp.util import run_wsgi_app

# Replace this with your own app
from myapp import run

if __name__ == "__main__":
    settings = {
        "reload_templates": True,
        "debug_authorization": False,
        "debug_notfound": True,
    }
    run_wsgi_app(run.wsgi_app())
