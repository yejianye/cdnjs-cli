from fetchr.packages.base import package, SimplePackage

@package
class JQuery(SimplePackage):
    """JQuery"""
    version = '1.9.0'

    @property
    def cdn_urls(self):
        return ['//ajax.googleapis.com/ajax/libs/jquery/$version/jquery.min.js']

    @property
    def dev_urls(self):
        return ['//ajax.googleapis.com/ajax/libs/jquery/$version/jquery.js']

@package
class JQuery_UI(SimplePackage):
    """JQuery UI"""
    version = '1.9.2'
    deps = ['jquery']

    @property
    def cdn_urls(self):
        return [
            '//ajax.googleapis.com/ajax/libs/jqueryui/$version/jquery-ui.min.js',
            '//ajax.googleapis.com/ajax/libs/jqueryui/$version/themes/base/jquery-ui.css',
        ]

    @property
    def dev_urls(self):
        return [
            '//ajax.googleapis.com/ajax/libs/jqueryui/$version/jquery-ui.js',
            '//ajax.googleapis.com/ajax/libs/jqueryui/$version/themes/base/jquery-ui.css',
        ]
