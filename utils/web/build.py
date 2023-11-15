import shutil
from pathlib import Path

from utils.web.helpers import *
from utils.web.directories import directory_factory

from jinja2 import Environment, FileSystemLoader, select_autoescape


class Builder:
    def __init__(
            self,
            src_path: str | Path = SRC_DIR,
            build_root: str | Path = PROJECT_DIR / "build/www/",
            minified: bool = True,
    ):
        self.src_path = Path(src_path).resolve()
        self.build_root = Path(build_root).resolve()
        self.minified = minified

        self.jinja_env = Environment(
            loader=FileSystemLoader((PROJECT_DIR / "utils/web/templates/").resolve()),
            autoescape=select_autoescape()
        )

    def build(self):
        # Ensure build_root is clean and exists before building
        shutil.rmtree(self.build_root, ignore_errors=True)
        self.build_root.mkdir(parents=True)

        # Copy static assets
        shutil.copytree(
            PROJECT_DIR / "utils/web/static/",
            self.build_root / "static/",
            dirs_exist_ok=True
        )

        # Setup Jinja Environment Variables
        self.jinja_env.globals["STATIC_PREFIX"] = "/static"

        # Build source
        source_directory = directory_factory(None, self.src_path, self)
        source_directory.build()


if __name__ == "__main__":
    Builder().build()
