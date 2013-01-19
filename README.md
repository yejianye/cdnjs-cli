Fetchr
===============

This is a Javascript/CSS package mangament tool. It allows you to easily grab frequently-used Javascript/CSS libraries to your project. It current supports the following libraries
- amplify
- backbone
- bootstrap
- jquery
- jquery-ui
- modernizr
- prettify
- underscore

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

To search a package

    $ fetchr search keyword

Add new packages
---------------

Add support to a new package for `Fetchr` is easy. Just add a new file under fetchr/packages. In most cases, you could subclass `SimplePackage` and set the following properties

- `version`: Library's version
- `dev_urls`: Urls for development version of the library
- `min_urls`: Urls for minified version of the library
- `cdn_urls`: Urls for CDN hosting the library

It's not required to set all of them and `Fetchr` is smart enough to derive the rest from what you've set. For example, if only `dev_urls` is set, when users request a minified version, `Fetchr` will download the development and generate minified Javascript/CSS files of the library. If only `cdn_urls` is set, `min_urls` will default to `cdn_urls` and when development version is requested, it will show a warning and download the minified version instead.

