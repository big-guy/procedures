#!/usr/bin/env python

import os, sys, copy
import markdown
import pystache
import json
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

with open(projectfile) as json_data:
    project_data = json.load(json_data)

    common_data = {}
    for common_settings in project_data['common_settings']: 
        with open(common_settings) as common_json_data:
            loaded_data = json.load(common_json_data)
            common_data = {key: value for (key, value) in (list(common_data.items()) + list(loaded_data.items()))}

    data = {key: value for (key, value) in (list(common_data.items()) + list(project_data.items()))}
    data['generation_timestamp'] = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M')
#    print(json.dumps(data))

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

