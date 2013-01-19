import requests
import os
import sh
import slimit
import cssmin

minify_js = slimit.minify
minify_css = cssmin.cssmin

def download(url, filename, content_processor=lambda x:x):
    filedir = os.path.dirname(filename)
    sh.mkdir('-p', filedir)
    print '%s --> %s' % (url, filename)
    resp = requests.get(url)
    if resp.ok:
        f = open(filename, 'w')
        f.write(content_processor(resp.content))
        f.close()
    else:
        print 'Error: %s' % resp.status_code
    return resp.ok

def minify_file(input_filename, output_filename, minify_func):
    minified_text = minify_func(open(input_filename).read())
    output = open(output_filename, 'w')
    output.write(minified_text)
    output.close()

