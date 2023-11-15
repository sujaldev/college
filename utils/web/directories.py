import tomllib
from typing import Union
from pathlib import Path

from utils.web.helpers import *
from utils.web.files import file_factory


class Directory:
    def __init__(self, parent: Union["Directory", None], src_path: str | Path, builder):
        """
        Directory object to recursively build a tree of directories and files to facilitate easy build operations.
        :param parent: Parent directory of the current directory, None if root directory.
        :param src_path: Path of the source tree.
        :param builder: Builder object provides build options such as build_root and whether to minify output or not.
        """
        self.parent = parent
        self.src_path = Path(src_path).resolve()
        self.builder = builder

        self.config = self.parse_config()
        self.ignored_files = [(Path(self.src_path) / f).resolve() for f in self.config.get("ignore", [])]

        self.children = []

    def parse_config(self):
        config_path = self.src_path / "config.toml"
        if config_path.exists() and config_path.is_file():
            with open(config_path, "rb") as file:
                return tomllib.load(file)
        return {}

    def process_child(self, path: str | Path):
        if path.is_dir():
            return directory_factory(self, path, self.builder)
        else:
            # return file_factory(self, path, self.build_root).build()
            pass

    def get_children(self):
        for file in gitignored_listdir(self.src_path):
            file_path = (self.src_path / file).resolve()

            if file_path in self.ignored_files:
                continue

            child = self.process_child(file_path)
            if child is not None:
                self.children.append(child)

    def inject_blobs(self):
        # Injects blobs as child files that create symlinks to the "real blobs" when written to the build dir.
        pass

    def build(self):
        self.get_children()
        self.inject_blobs()
        self.write()
        for child in self.children:
            child.build()

    @property
    def build_path(self) -> Path:
        return (self.builder.build_root / self.src_path.relative_to(SRC_DIR)).resolve()

    @minified
    def render_template(self):
        template = self.builder.jinja_env.get_template("listing.jinja")
        return template.render(files={
            child.build_path.name: child.build_path.name for child in self.children
        })

    def write(self):
        self.build_path.mkdir(parents=True, exist_ok=True)
        with open(self.build_path / "index.html", "w") as file:
            file.write(self.render_template())

    def __repr__(self):
        return str(self.src_path.relative_to(SRC_DIR))


class CPracticalDirectory(Directory):
    def process_child(self, path: str | Path):
        pass

    def build(self):
        self.ignored_files = ["CMakeLists.txt"]
        super().get_children()


def directory_factory(parent: Union[Directory | None], path: str | Path, builder) -> Directory:
    dir_obj = Directory(parent, path, builder)

    if dir_obj.config.get("dirtype") == "c-practical":
        return CPracticalDirectory(parent, path, builder)

    return dir_obj
