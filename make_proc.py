#!/usr/bin/env python

import os, sys
import markdown
import pystache
import json

import time
import datetime

if (len(sys.argv) < 2): 
   exit(-1)

projectfile = sys.argv[1]

with open(projectfile) as json_data:
    project_data = json.load(json_data)
    if 'common_settings' in project_data: 
        with open(project_data['common_settings']) as common_json_data:
            common_data = json.load(common_json_data)
    else:
        common_data = {}

    data = {key: value for (key, value) in (list(project_data.items()) + list(common_data.items()))}
    data['generation_timestamp'] = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M')
    print(json.dumps(data))

with open(data['body_template_file']) as body_file, open(data['html_template_file']) as html_file:

    body_md = pystache.render(body_file.read(), data)

    md_render = markdown.Markdown(extensions=data['markdown_extensions'], output_format="html5" )
    data['__body'] = md_render.convert(body_md)
    # print(body_md)

    output = pystache.render(html_file.read(), data)

with open(sys.argv[2], 'w') as outfile:
    outfile.write(output)
    outfile.close()

