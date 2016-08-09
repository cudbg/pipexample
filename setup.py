#!/usr/bin/env python2.7
try:
    from setuptools import setup, find_packages
except ImportError:
    import ez_setup
    ez_setup.use_setuptools()
from setuptools import setup, find_packages

setup(name="pipexample",
      version="0.0.1",
      description="",
      license="MIT",
      author="Eugene Wu",
      author_email="",
      url="http://github.com/cudbg/pipexample",
      packages = find_packages(),
      include_package_data = True,

      # ensures that pipexample is defined as a module
      package_dir = {'pipexample' : 'pipexample'},

      # ensures that pipexample/*.txt is included in the package
      package_data={
        'pipexample':['*.txt']
      },

      # ensures that runexample.py can be run from the command line as a program
      scripts = [
        'bin/runexample.py'
      ],
      install_requires = [
        'click'
      ],
      keywords= "")
