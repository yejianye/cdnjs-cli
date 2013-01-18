#!/usr/bin/env python
import requests
import os
import sys
import sh
from argh import arg, dispatch_commands
from argh.decorators import named

jquery_version = '1.9.0'
packages = {}
def package(cls):
    packages[cls.__name__.lower().replace('_', '-')] = cls
    return cls

def download(url, filename):
    filedir = os.path.dirname(filename)
    sh.mkdir('-p', filedir)
    print '%s --> %s' % (url, filename)
    resp = requests.get(url)
    if resp.ok:
        f = open(filename, 'w')
        f.write(resp.content)
        f.close()
    else:
        print 'Error: %s' % resp.status_code
    return resp.ok

@package
class JQuery:
    version = '1.9.0'
    def snippet(self):
        print "<script src='//ajax.googleapis.com/ajax/libs/jquery/%s/jquery.min.js'></script>" % self.version

    def prod(self):
        download('http://code.jquery.com/jquery-%s.min.js' % self.version, 'js/jquery.min.js')

    def dev(self):
        download('http://code.jquery.com/jquery-%s.js' % self.version, 'js/jquery.js')

@package
class JQuery_UI:
    version = '1.9.2'
    def snippet(self):
        print "<script src='//ajax.googleapis.com/ajax/libs/jqueryui/%s/jquery-ui.min.js'></script>" % self.version
        print "<link rel='stylesheet' href='//ajax.googleapis.com/ajax/libs/jqueryui/%s/themes/base/jquery-ui.css' charset='utf-8'>" % self.version

    def prod(self):
        download('http://ajax.googleapis.com/ajax/libs/jqueryui/%s/jquery-ui.min.js' % self.version, 'js/jquery-ui.min.js')
        self.download_css()

    def dev(self):
        download('http://code.jquery.com/ui/%s/jquery-ui.js' % self.version, 'js/jquery-ui.js')
        self.download_css()

    def download_css(self):
        download('http://ajax.googleapis.com/ajax/libs/jqueryui/%s/themes/base/jquery-ui.css' % self.version, 'css/jquery-ui.css')

def check_package(package):
    if package not in packages.keys():
        print "Unknown package:", package
        sys.exit(1)

@named('list')
def list_packages():
    """ list all packages """
    print '\n'.join(packages.keys())

@named('install')
@arg('--min', '-m', default=False, help='Fetch production/minified version.')
@arg('package', help='Package name')
def install_package(args):
    """ install package """
    check_package(args.package)
    pkg = packages[args.package]()
    if args.min:
        pkg.prod() 
    else:
        pkg.dev()

@named('cdn')
@arg('package', help='Package name')
def cdn_snippet(args):
    """ show embedded html snippets for using package via CDN """
    check_package(args.package)
    pkg = packages[args.package]()
    pkg.snippet() 

def main():
    dispatch_commands([list_packages, install_package, cdn_snippet])

if __name__ == '__main__':
    main()
