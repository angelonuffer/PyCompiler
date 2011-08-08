PyCompiler 0.0.1
================

Simple way to build a compiler in python.
The methods are converted in assembly instructions.


Usage
-----

To make a static executable::

    >>> from pycompiler import compile, Executable
    >>> executable = Executable()
    >>> executable.write("foo")
    >>> compile(code, ".test.out")

Then a executable was created::

    $ ./test.out
    foo


Installing
----------

Install using latest version::

    $ git clone git@github.com:angelonuffer/PyCompiler.git
    # python setup.py install

*NOTE: the second command needs be runned with root user, you can use the sudo application for this
