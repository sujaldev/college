import os
from pathlib import Path
from functools import wraps

import igittigitt
from minify_html import minify

__all__ = ["PROJECT_DIR", "SRC_DIR", "gitignored_listdir", "minified"]

PROJECT_DIR = Path(__file__).parent.parent.parent.resolve()
SRC_DIR = PROJECT_DIR / "src/"


def gitignored_listdir(path: str | Path) -> list[str]:
    """
    `os.listdir` but filters out items based on .gitignore
    """
    parser = igittigitt.IgnoreParser()

    # Load project's .gitignore
    parser.parse_rule_file(PROJECT_DIR / ".gitignore")

    # Append additional restrictions that can't be mentioned in the project's .gitignore file
    additional_rules = [".git", ".gitignore"]
    for rule in additional_rules:
        parser.add_rule(rule, PROJECT_DIR)

    return [f for f in os.listdir(path) if not parser.match(f)]


def minified(renderer):
    @wraps(renderer)
    def minified_renderer(self, *args, **kwargs):
        if not self.builder.minify_output:
            return renderer(self, *args, **kwargs)
        return minify(renderer(self, *args, **kwargs), minify_css=True, minify_js=True)

    return minified_renderer
