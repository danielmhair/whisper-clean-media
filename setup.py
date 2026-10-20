import os
from os.path import abspath

import setuptools
import toml


def get_package_readme():
    cwd = os.getcwd()
    path = abspath(f"{cwd}/README.md")

    with open(path, "r", encoding="utf-8") as fh:
        return fh.read()


def get_package_version():
    cwd = os.getcwd()
    path = abspath(f"{cwd}/pyproject.toml")
    toml_obj = toml.load(path)
    version = toml_obj["tool"]["poetry"]["version"]
    return version


def setup_package(model_name, repo_url):
    setuptools.setup(
        name=model_name,
        version=get_package_version(),
        author="Daniel Hair",
        author_email="danielmhair@gmail.com",
        description=model_name,
        long_description=get_package_readme(),
        long_description_content_type="text/markdown",
        url=repo_url,
        project_urls={},
        packages=[model_name],
        install_requires=[""],
    )


model_name: str = "clean_media"
repo_url = "https://github.com/danielmhair/whisper-clean-media.git"

setup_package(model_name, repo_url)
