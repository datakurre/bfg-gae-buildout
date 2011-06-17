import pyramid_zcml

from pyramid.configuration import Configurator
from myapp.models import get_root

def wsgi_app(**settings):
  config = Configurator(root_factory=get_root, settings=settings)
  config.include(pyramid_zcml)
  config.load_zcml('configure.zcml')
  return config.make_wsgi_app()