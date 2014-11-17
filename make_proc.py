#!/usr/bin/env python
"""
The MIT License (MIT)

Copyright (c) 2014 Sterling Greene 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

"""
import os, sys, copy, shutil
import markdown
import pystache
import yaml
import html.parser

import datetime

if (len(sys.argv) < 2): 
   print("make_proc.py path/to/data.yaml path/to/output.html")
   exit(-1)

# TODO: Expand command line options
projectfile = sys.argv[1]
outputdir = sys.argv[2] + '/'
outputfile = outputdir + 'index.html'

# Prevents escaping of HTML elements in test cases
class Lambdas(object):
    def __init__(self, renderer):
        self.renderer = renderer
    def unescape(self):
        return lambda s: html.parser.HTMLParser().unescape(copy.deepcopy(self.renderer).render(s, self.renderer.context))

def merge_dict_lists(dict1, dict2):
    return list(dict1.items()) + list(dict2.items())

def escape_pystache_include(test_file):
    return "{{>" + test_file + "}}"

def add_internal_props(idx, test):
    # Assign unique identifiers to test cases and format into pystache import format

    inner_props = { 
       '__id': idx+1, 
       '__file': escape_pystache_include(test['file']),
       }
    return dict(merge_dict_lists(test, inner_props))

with open(projectfile) as configuration_data:
    project_data = yaml.load(configuration_data)

    # handle import_from settings:
    common_data = {}
    for import_from in project_data['import_from']: 
        with open(import_from) as common_configuration_data:
            loaded_data = yaml.load(common_configuration_data)
	    # Combine previously import_from data with newly loaded import_from data (last one takes precedence)
            common_data = { key: value for (key, value) in merge_dict_lists(common_data, loaded_data) }

    # Combine import_from and project_data (project data takes priority)
    data = { key: value for (key, value) in merge_dict_lists(common_data, project_data) }
    data['included_tests'] = [ add_internal_props(idx, test) for idx, test in enumerate(data['included_tests'])]
    # timestamp for when we created the document
    data['__generation_timestamp'] = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M')
#    print(yaml.dump(data))

# Converts input mustache files into single markdown formatted file
# Converts markdown formatted file into HTML
with open(data['markdown_template_file']) as md_file, open(data['html_template_file']) as html_file:

    py_renderer = pystache.Renderer(missing_tags='strict', search_dirs=data['search_dirs'])
    body_md = py_renderer.render(md_file.read(), data, Lambdas(py_renderer))

#    print(body_md)

    md_render = markdown.Markdown(extensions=data['markdown_extensions'], output_format="html5" )
    data['__body'] = md_render.convert(body_md)
#    print(data['__body'])

    output = py_renderer.render(html_file.read(), data, Lambdas(py_renderer))
#    print(output)

# Copy supporting files to outputdir
# TODO: Allow this to be configurable
try:
    shutil.rmtree(outputdir+'css')
except OSError as e:
    pass
shutil.copytree('css', outputdir+'css')

lib_dir = outputdir+'lib/'
if not os.path.isdir(lib_dir):
    os.mkdir(lib_dir)

for js_file in data['js_files']:
    shutil.copy(js_file, lib_dir)

with open(outputfile, 'w') as out:
    out.write(output)
    out.close()

