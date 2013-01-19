from fetchr.packages.base import package, SimplePackage

@package
class Amplify(SimplePackage):
    """A set of tools solve problems of request, store, pub/sub""" 
    version = '1.1.0'
    @property
    def cdn_urls(self):
        return ['//cdnjs.cloudflare.com/ajax/libs/amplifyjs/$version/amplify.min.js']
