# A very simple script to render markdown files (simple enough that most code here was available in the documentation of
# these projects, I've just glued it together).

import os
import sys
import argparse
from pathlib import Path

import mistune
import frontmatter
from minify_html import minify
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_lexer_by_name
from jinja2 import Environment, FileSystemLoader, select_autoescape

# --- Command line ---
parser = argparse.ArgumentParser(prog="ipu-md", description="Render markdown/code files as html.")
parser.add_argument("template", help="Absolute path to the jinja2 template file.")
args = parser.parse_args()

# --- Setup ---
env = Environment(
    loader=FileSystemLoader(Path(args.template).resolve().parent),
    autoescape=select_autoescape()
)
template = env.get_template("template.jinja2")


class HighlightRenderer(mistune.HTMLRenderer):
    def block_code(self, code, info=None):
        if info:
            info = info.lstrip("{").rstrip("}")
            lexer = get_lexer_by_name(info, stripall=True)
            formatter = HtmlFormatter(style="default")
            return highlight(code, lexer, formatter)
        return '<pre><code>' + mistune.escape(code) + '</code></pre>'


render_markdown = mistune.create_markdown(
    renderer=HighlightRenderer(escape=False),
    plugins=['strikethrough', 'footnotes', 'table', 'speedup', 'task_lists', 'url']
)

# --- Read ---
source = sys.stdin.read()

# --- Parse frontmatter ---
metadata, content = frontmatter.parse(source)
filename = Path(os.environ.get("SCRIPT_FILENAME", "/Document")).resolve().name
metadata["title"] = metadata.get("title", filename)

# --- Render markdown ---
content = render_markdown(content)

# --- Render Jinja template ---
html = template.render(content=content, **metadata)

# --- Post-processing ---
print(minify(html, minify_css=True, minify_js=True))
