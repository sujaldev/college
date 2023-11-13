import tomllib
from typing import Union
from pathlib import Path

from utils.web.helpers import *
from utils.web.files import file_factory


class Directory:
    def __init__(self, parent: Union["Directory", None], src_path: str | Path, build_path: str | Path):
        """
        Directory object to recursively build a tree of directories and files to facilitate easy build operations.
        :param parent: Parent directory of the current directory, None if root directory.
        :param src_path: Path of the source tree.
        :param build_path: Path where to build the output tree.
        """
        self.parent = parent
        self.src_path = Path(src_path).resolve()
        self.build_path = Path(build_path).resolve()

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
            return directory_factory(self, path, self.build_path)
        else:
            return file_factory(self, path, self.build_path).build()

    def get_children(self):
        for file in gitignored_listdir(self.src_path):
            file_path = (self.src_path / file).resolve()

            if file_path in self.ignored_files:
                continue

            child = self.process_child(file_path)
            if child is not None:
                self.children.append(child)

    def build(self):
        self.get_children()

    def write(self):
        pass

    def __repr__(self):
        return str(self.src_path.relative_to(SRC_DIR))


class CPracticalDirectory(Directory):
    def process_child(self, path: str | Path):
        pass

    def build(self):
        self.ignored_files = ["CMakeLists.txt"]
        self.get_children()


def directory_factory(parent: Directory, path: str | Path, build_path: str | Path) -> Directory:
    dir_obj = Directory(parent, path, build_path)
    if dir_obj.config.get("dirtype") == "c-practical":
        return CPracticalDirectory(parent, path, build_path)
    return dir_obj
