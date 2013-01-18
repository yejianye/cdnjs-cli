Fetchr
===============

This is a Javascript/CSS package mangament tool. It allows you to easily grab frequently-used Javascript/CSS libraries to your project. It current supports the following libraries
- jquery
- jquery-ui
- bootstrap
- google-code-prettify

Inspired by `Fetch` plugin for Sublime Text and `Bower` from Twitter.

Installation
-------------

Install directly from github.com

    $ pip install git+git://github.com/yejianye/fetchr.git

Or clone this repository and run

	$ python setup.py install

Usage
-------------

For example, in your website, you create a `static/lib` directory to store all third-party libraries. To install jquery into that directory

    $ cd static/lib
    $ fetchr install jquery

`fetchr` will display the source url where it fetches jquery.js and put it under `static/lib/js/jquery.js`. If you'd like to install a minified version, you should do

    $ fetchr install -m jquery

To list all supported packages

    $ fetchr list
