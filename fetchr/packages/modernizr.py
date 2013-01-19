from fetchr.packages.base import package, SimplePackage

@package
class Modernizr(SimplePackage):
    version = '2.6.2'
    @property
    def cdn_urls(self):
        return ['//cdnjs.cloudflare.com/ajax/libs/modernizr/$version/modernizr.min.js']

    @property
    def dev_urls(self):
        return ['http://www.modernizr.com/downloads/modernizr-latest.js']
