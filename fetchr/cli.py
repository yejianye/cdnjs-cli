#!/usr/bin/env python
import sys
from fetchr.packages import base 
from argh import arg, dispatch_commands
from argh.decorators import named

def check_package(package):
    base.discover_packages()
    if not base.has_package(package):
        print "Unknown package:", package
        sys.exit(1)

@named('list')
def list_packages():
    """ list all packages """
    base.discover_packages()
    packages = base.list_packages()
    for name, desc in packages.iteritems():
        if desc:
            print '%s - %s' % (name, desc)
        else:
            print name

@named('install')
@arg('--min', '-m', default=False, help='Generate production/minified version.')
@arg('package', help='Package name')
def install_package(args):
    """ install package """
    check_package(args.package)
    pkg = base.get_instance(args.package)
    if args.min:
        pkg.minified() 
    else:
        pkg.dev()

@named('cdn')
@arg('package', help='Package name')
def cdn_snippet(args):
    """ show embedded html snippets for using package via CDN """
    check_package(args.package)
    pkg = base.get_instance(args.package)
    try:
        pkg.snippet() 
    except NotImplementedError:
        print "Sorry, there's no CDN hosting the library."

def main():
    dispatch_commands([list_packages, install_package, cdn_snippet])

if __name__ == '__main__':
    main()
