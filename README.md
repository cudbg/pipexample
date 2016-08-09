# What is this

Example repository structure for writing a python package that can be uploaded to pip.

Note

* module files are defined under `pipexample/`
* `pipexample/__init__.py` loads the functions in `pipexample/pipexample.py` so it's available in the module

        import pipexample
        pipexample.Foo

  otherwise you would need to write

        import pipexample
        import pipexample.pipexample # to load the file
        pipexample.pipexample.Foo
* read setup.py to see how scripts and data files are included

How to install

    # create a virtual environment first

    python setup.py install

    # run it
    runexample.py 1


How to upload to pip

* http://peterdowns.com/posts/first-time-with-pypi.html

