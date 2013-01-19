import requests
import os

class Repository(object):
    def __init__(self, owner, repo):
        self.content_api = 'https://api.github.com/repos/%s/%s/contents/' % (owner, repo)

    def list_dir(self, path):
        return requests.get(self.content_api + path).json

    def exists(self, path):
        return requests.get(self.content_api + path).ok

    def download_dir(self, src, dst):
        if not os.path.exists(dst):
            os.mkdir(dst)
        for child in self.list_dir(src):
            if child['type'] == 'file':
                self.download_file(child['path'], os.path.join(dst, child['name']))
            if child['type'] == 'dir':
                self.download_dir(child['path'], os.path.join(dst, child['name']))

    def download_file(self, src, dst):
        src_url = 'http://cdnjs.cloudflare.com/' + src
        print '%s --> %s' % (src_url, dst)
        with open(dst, 'w') as output:
            output.write(requests.get(src_url).content)

