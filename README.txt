bfg-gae-buildout
================

Buildouts repoze.bfg app onto Google's App Engine.

This buildout has been inspired by and isn't possible without:

  * http://darrylcousins.blogspot.com/2010/01/repoze-bfg-on-google-app-engine.html
  * http://code.google.com/p/bridal/
  * http://pypi.python.org/pypi/rod.recipe.appengine
  * http://code.google.com/p/appengine-monkey/


Testing the buildout out of the box
-----------------------------------

Build and run the application::

  $ python bootstrap.py
  $ ./bin/buildout
  $ ./bin/wrapper parts/wrapper

Then access the application using a web browser with the following URL::

  http://localhost:8080/


Adding a custom application to the buildout
-------------------------------------------

Replace 'myapp' with your own application at `buildout:eggs`.

Update `src/wrapper/app.py` to launch your application instead of 'myapp'.

Just in case, run `buildout` with `rm .installed.cfg && bin/buildout`.


Deploying your application onto GAE
----------------------------------

Update the name of your Google App Engine application at `src/wrapper/app.yaml`.

To upload application files, run::

  $ ./bin/appcfg update parts/wrapper

For a more detailed documentation follow this url::

  http://code.google.com/appengine/docs/python/tools/uploadinganapp.html


Troubleshooting
---------------

Buildout fails with `Error: Couldn't install: foobar`.
  Double check that you are using Python 2.5
  
Page request gives `ImportError: foobar`.
  Dependencies for `repoze.bfg` may have been updated.
  Try to update `${wrapper:packages}` on `buildout.cfg` with
  missing packages and run buildout again.

Page request gives `SAXReaderNotAvailable: No parsers found`.
  Most probably, used Python has been built without Expat support.