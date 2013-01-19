from fetchr.packages.base import package, SimplePackage

@package
class Prettify(SimplePackage):
    """Syntax highlighter from Google"""
    @property
    def dev_urls(self):
        return [
            'http://google-code-prettify.googlecode.com/svn/trunk/src/prettify.js',
            'http://google-code-prettify.googlecode.com/svn/trunk/src/prettify.css',
        ]
