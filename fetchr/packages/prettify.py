from fetchr.packages.base import package, SimplePackage

@package
class Prettify(SimplePackage):
    """Google Code Prettify"""
    @property
    def dev_urls(self):
        return [
            'http://google-code-prettify.googlecode.com/svn/trunk/src/prettify.js',
            'http://google-code-prettify.googlecode.com/svn/trunk/src/prettify.css',
        ]
