#!/usr/bin/env python
import sys
from cdnjs import base
from argh import arg, dispatch_commands
from argh.decorators import named

def check_lib(lib, version=None):
    if not base.has_lib(lib, version):
        if version:
            print "%s %s not found " % (lib, version)
        else:
            print "%s not found " % lib
        sys.exit(1)

def filter_libs(cond):
    libs = base.list_libs()
    return [name for name in libs if cond(name)]

@named('list')
def list_libs():
    """ list all libraries """
    print '\n'.join(filter_libs(lambda name:True))

@named('search')
@arg('keyword', help='Keyword to search the library')
def search_libs(args):
    """ search libraries via a keyword """
    result = filter_libs(lambda name: (args.keyword in name))
    if not result:
        print 'libs not found.'
    else:
        print '\n'.join(result)

@named('install')
@arg('library', help='Library name')
def install_lib(args):
    """ install library """
    lib_ver = args.library.split('#')
    check_lib(*lib_ver)
    base.download_lib(*lib_ver)

@named('cdn')
@arg('library', help='Library name')
def cdn_snippet(args):
    """ show embedded html snippets for using library via CDN """
    lib_ver = args.library.split('#')
    check_lib(*lib_ver)
    base.cdn_snippet(*lib_ver)

def main():
    dispatch_commands([list_libs, search_libs, install_lib, cdn_snippet])

if __name__ == '__main__':
    main()
