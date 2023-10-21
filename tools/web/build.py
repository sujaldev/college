import tomllib
from pathlib import Path
from functools import wraps

from minify_html import minify
from jinja2 import Environment, FileSystemLoader, select_autoescape


class Builder:
    def __init__(self, minify_output=False):
        """
        Class to build the website from the `src` directory. It also supports live builds of pages on-demand.

        :param minify_output: If true, the rendered output will be minified.
        """
        self.minify_output = minify_output

        parent_dir = Path(__file__).parent

        with open(parent_dir / "../../src/config.toml", "rb") as file:
            self.config = tomllib.load(file)

        self.env = Environment(
            loader=FileSystemLoader(parent_dir / "templates"),
            autoescape=select_autoescape()
        )

    @staticmethod
    def minified(renderer):
        @wraps(renderer)
        def minified_renderer(self, *args, **kwargs):
            if not self.minify_output:
                return renderer(self, *args, **kwargs)
            return minify(renderer(self, *args, **kwargs), minify_css=True, minify_js=True)

        return minified_renderer

    @minified
    def render_home(self):
        return self.env.get_template("home.jinja").render(directories=self.config["sources"])


print(Builder().render_home())
