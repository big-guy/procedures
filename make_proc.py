#!/usr/bin/env python

import os, sys, copy
import markdown
import pystache
import yaml
import html.parser

import datetime

if (len(sys.argv) < 2): 
   exit(-1)

projectfile = sys.argv[1]
outputfile = sys.argv[2]

class Lambdas(object):
    def __init__(self, renderer):
        self.renderer = renderer
    def unescape(self):
        return lambda s: html.parser.HTMLParser().unescape(copy.deepcopy(self.renderer).render(s, self.renderer.context))

with open(projectfile) as configuration_data:
    project_data = yaml.load(configuration_data)

    common_data = {}
    for import_from in project_data['import_from']: 
        with open(import_from) as common_configuration_data:
            loaded_data = yaml.load(common_configuration_data)
            common_data = {key: value for (key, value) in (list(common_data.items()) + list(loaded_data.items()))}

    data = {key: value for (key, value) in (list(common_data.items()) + list(project_data.items()))}

    tests = [ {'id': idx+1, 'file': "{{>" + test + "}}" } for idx, test in enumerate(data['included_tests'])]
    data['included_tests'] = tests
    data['generation_timestamp'] = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M')

md_render = markdown.Markdown(extensions=data['markdown_extensions'], output_format="html5" )
py_renderer = pystache.Renderer(missing_tags='strict', search_dirs=data['search_dirs'])

with open(data['markdown_template_file']) as md_file, open(data['html_template_file']) as html_file:

    body_md = py_renderer.render(md_file.read(), data, Lambdas(py_renderer))

#    print(body_md)

    data['__body'] = md_render.convert(body_md)
#    print(data['__body'])

    output = py_renderer.render(html_file.read(), data, Lambdas(py_renderer))
#    print(output)

with open(outputfile, 'w') as out:
    out.write(output)
    out.close()

