from fetchr.packages.base import package, SimplePackage

@package
class Bootstrap(SimplePackage):
    version = '2.2.2'

    @property
    def cdn_urls(self):
        return [
            '//netdna.bootstrapcdn.com/twitter-bootstrap/$version/css/bootstrap-combined.min.css',
            '//netdna.bootstrapcdn.com/twitter-bootstrap/$version/js/bootstrap.min.js',
        ]
