"""Basic tests that do not require Django."""

import os

import pytest

try:
    import tomllib as toml
except ModuleNotFoundError:  # Python <3.11
    import tomli as toml

pytestmark = pytest.mark.unit


def test_docs_packaging_versions_match():
    """Compare pyproject dev dependencies with docs requirements."""
    parent_path = os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    )
    poetry_path = os.path.join(parent_path, "pyproject.toml")
    with open(poetry_path, "rb") as f:
        poetry_details = toml.load(f)["tool"]["poetry"]["group"]["dev"]["dependencies"]
    with open(f"{parent_path}/docs/requirements.txt", "r", encoding="utf-8") as file:
        requirements = [
            line
            for line in file.read().splitlines()
            if len(line) > 0 and not line.startswith("#")
        ]
    for pkg in requirements:
        package_name = pkg
        if len(pkg.split("==")) == 2:  # noqa: PLR2004
            package_name, version = pkg.split("==")
        else:
            version = "*"
        assert poetry_details[package_name] == version
