import os
import glob
from functools import wraps
from fetchr.utils import download, minify_js, minify_css

_packages = {}

def resolve_deps(func):
    @wraps(func)
    def wrapped(self, *args, **kwargs):
        [getattr(pkg, func.__name__)(*args, **kwargs) for pkg in self.dep_pkgs]
        return func(self, *args, **kwargs)
    return wrapped

class SimplePackage(object):
    css_dir = 'css'
    js_dir = 'js'
    version = '1.0'
    deps = []

    def __init__(self):
        self.dep_pkgs = [get_instance(name) for name in self.deps]

    @property
    def cdn_urls(self):
        return []

    @property
    def dev_urls(self):
        return []

    @property
    def min_urls(self):
        return self.cdn_urls

    @resolve_deps
    def snippet(self):
        if not self.cdn_urls:
            raise NotImplementedError
        for url in self.cdn_urls:
            url = self.version_url(url)
            if url.endswith('.js'):
                print "<script src='%s'></script>" % url
            elif url.endswith('.css'):
                print "<link rel='stylesheet' href='%s'>" % url

    @resolve_deps
    def dev(self):
        if self.dev_urls:
            self.get(self.dev_urls, self.download_one)
        elif self.cdn_urls:
            print "WARNING: Development version not found, will download minified version instead."
            self.get(self.cdn_urls, self.download_one)

    @resolve_deps
    def minified(self):
        if self.min_urls:
            self.get(self.min_urls, self.download_one)
        else:
            self.get(self.dev_urls, self.minify_one)

    def version_url(self, url):
        return url.replace('$version', self.version)

    def get(self, urls, one_func):
        for url in urls:
            url = self.version_url(url)
            if url.startswith('//'):
                url = 'http:' + url
            filename = url.rsplit('/', 1)[-1]
            one_func(url, filename)
    
    def download_one(self, url, filename):
        if url.endswith('.js'):
            download(url, os.path.join(self.js_dir, filename))
        elif url.endswith('.css'):
            download(url, os.path.join(self.css_dir, filename))

    def minify_one(self, url, filename):
        filename, ext = filename.rsplit('.', 1)  
        filename = '%s.min.%s' % (filename, ext)
        if url.endswith('.js'):
            download(url, os.path.join(self.js_dir, filename), minify_js)
        elif url.endswith('.css'):
            download(url, os.path.join(self.css_dir, filename), minify_css)

def has_package(package):
    return package in _packages.keys()

def list_packages():
    return dict((name, cls.__doc__) for name, cls in _packages.iteritems())

def get_instance(name):
    return _packages[name]()

def package(cls):
    _packages[cls.__name__.lower().replace('_', '-')] = cls
    return cls

def discover_packages():
    package_dir = os.path.dirname(__file__)
    base_path = 'fetchr.packages'
    exclude_list = ['__init__', 'base', 'utils']
    for pyfile in glob.glob(os.path.join(package_dir, '*.py')):
        module_name = os.path.basename(pyfile).rsplit('.', 1)[0]
        if module_name not in exclude_list:
            __import__('%s.%s' % (base_path, module_name))
