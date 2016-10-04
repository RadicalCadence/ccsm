#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.compat import Directive

class conceptdemo(nodes.General, nodes.Element): pass

def visit_conceptdemo_node(self, node):

    regex = re.compile(r"(\w+)\.js")

    container_attrs = {
        'class': 'concept-demo',
        'ids': [regex.search(node['scriptsource']).group(0)[:-3]]
    }
    self.body.append(self.starttag(node, "div", **container_attrs))
    self.body.append('</div>')

    script_attrs = {
        'src': node['scriptsource']
    }
    self.body.append(self.starttag(node, "script", **script_attrs))
    self.body.append('</script>')

def depart_conceptdemo_node(self, node):
    pass

class ConceptDemo(Directive):
    has_content = True
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False

    def run(self):
        return [conceptdemo(scriptsource=self.arguments[0])]

def setup(app):
    app.add_node(conceptdemo, html=(visit_conceptdemo_node, depart_conceptdemo_node))
    app.add_directive("conceptdemo", ConceptDemo)
