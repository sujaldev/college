import os
from pathlib import Path

import igittigitt

__all__ = ["PROJECT_DIR", "SRC_DIR", "gitignored_listdir"]

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
