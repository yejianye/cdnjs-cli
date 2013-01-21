cdnjs-cli
===============

A command line interface to search/install Javascript/CSS libraries from cdnjs.com.

Installation
-------------

Install directly from github.com

    $ pip install git+git://github.com/yejianye/cdnjs-cli.git

Or clone this repository and run

	$ python setup.py install

Usage
-------------

For example, to install jquery, cd to your static root, and run

    $ cdnjs install jquery

`cdnjs` will create `jquery` directory and install the library into that directory. You could also install a specific version of the library

    $ cdnjs install jquery#1.9.0

To list all supported libraries

    $ cdnjs list

To search a library

    $ cdnjs search keyword

