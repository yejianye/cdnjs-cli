import github
repo = github.Repository(owner='cdnjs', repo='cdnjs')

def has_lib(lib, version=None):
    if version:
        return repo.exists('ajax/libs/%s/%s' % (lib, version))
    else:
        return repo.exists('ajax/libs/' + lib)

def list_libs():
    return [x['name'] for x in repo.list_dir('ajax/libs')]

def download_lib(lib, version=None):
    if not version:
        version = get_latest_version(lib)
    repo.download_dir('ajax/libs/%s/%s' % (lib, version), lib)

def cdn_snippet(lib, version=None):
    if not version:
        version = get_latest_version(lib)
    files = [
        '//cdnjs.cloudflare.com/' + f['path'] 
        for f in repo.list_dir('ajax/libs/%s/%s' % (lib, version)) 
        if f['type'] == 'file']
    for file in files:
        if file.endswith('min.js'):
            print "<script src='%s'></script>" % file
        elif file.endswith('.css'):
            print "<link rel='stylesheet' href='%s'>" % file

def get_latest_version(lib):
    versions = sorted([f['name'] for f in repo.list_dir('ajax/libs/%s' % lib) if f['type'] == 'dir'])
    return versions[-1]
