bfg-gae-buildout
================

Buildouts pyramid app onto Google App Engine.

This buildout has been inspired by:

* http://darrylcousins.blogspot.com/2010/01/repoze-bfg-on-google-app-engine.html
* http://code.google.com/p/bridal/
* http://pypi.python.org/pypi/rod.recipe.appengine
* http://code.google.com/p/appengine-monkey/


Requirements
------------

Python 2.5 compiled with expat support. Virtualenv may not work with GAE.


Testing the buildout out of the box
-----------------------------------

Build and run the application::

  $ python bootstrap.py
  $ ./bin/buildout
  $ ./bin/wrapper parts/wrapper

Then access the application using a web browser with the following URL::

  http://localhost:8080/


Using the buildout with your application
----------------------------------------

At first, take a look at *myapp* example. Besides minimal WSGI-wrapper at ``run.py``, it has completely no idea, that it would be run on GAE.

Replace *myapp* with your own application package at ``buildout:eggs`` and ``setup.py.install_requires``. These steps are required for ``rod.recipe.appengine`` to be able to find our requirement packages.

Update ``src/wrapper/app.py`` to launch your application instead of *myapp*. This step is required for our wrapper to launch our app as as WSGI-application.

Take care that setuptools will find our application files. This is usually done by setuptools' SVN, Mercurial, etc... integration, but you may also define included files explicitly in your package's ``MANIFEST.in``.

Just in case, run ``buildout`` with ``rm .installed.cfg && bin/buildout``. It seems, ``rod.recipe.appengine`` doesn't support buildout's update very well.


Deploying your application onto GAE
-----------------------------------

Update the name of your Google App Engine application at ``src/wrapper/app.yaml``. This step is required for GAE-script to know, which onto which GAE-instance to deploy.

To upload application files, run::

  $ ./bin/appcfg update parts/wrapper

For a more detailed documentation follow this url::

  http://code.google.com/appengine/docs/python/tools/uploadinganapp.html


Troubleshooting
---------------

Buildout fails with ``Error: Couldn't install: foobar``.
  Double check that you are using Python 2.5
  
Page request gives ``ImportError: ...``.
  Dependencies for ``pyramid`` may have been updated.
  Try to update ``${wrapper:packages}`` on ``buildout.cfg`` with
  missing packages and run buildout again.

Page request gives ``SAXReaderNotAvailable: No parsers found``.
  Most probably, used Python has been built without Expat support.