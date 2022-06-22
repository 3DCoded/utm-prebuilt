import json

from jinja2 import Environment, FileSystemLoader, Template
from yaml import load

with open('data.json') as file:
    vms = json.load(file)


def render_template(filename, **kwargs):
    with open(f'templates/{filename}') as file:
        template = Environment(loader=FileSystemLoader(
            searchpath='./')).from_string(file.read())
        return template.render(**kwargs)


def build_template(filename, dest, **kwargs):
    with open(f'built/{dest}', 'w') as file:
        file.write(render_template(filename, **kwargs))


build_template('index.html', 'index.html', vms=vms)
