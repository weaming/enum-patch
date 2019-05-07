# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import os
import re

here = os.path.abspath(os.path.dirname(__file__))


def read_text(fname):
    if os.path.isfile(fname):
        with open(os.path.join(here, fname)) as f:
            return f.read()
    else:
        print("warning: file {} does not exist".format(fname))
        return ""


def get_version(path):
    src = read_text(path)
    pat = re.compile(r"""^version = ['"](.+?)['"]$""", re.MULTILINE)
    result = pat.search(src)
    version = result.group(1)
    return version


long_description = read_text("README.md")

name = "enum-patch"
gh_repo = "https://github.com/weaming/{}".format(name)

setup(
    name=name,  # Required
    version=get_version("enum_patch.py"),  # Required
    # This is a one-line description or tagline of what your project does.
    description="Patch the python3's enum.Enum",  # Required
    long_description=long_description,  # Optional
    long_description_content_type="text/markdown",  # Optional
    py_modules=['enum_patch'],
    url=gh_repo,  # Optional
    author="weaming",  # Optional
    author_email="garden.yuen@gmail.com",  # Optional
    keywords="enum,monkey-patch",  # Optional
    project_urls={
        "Bug Reports": gh_repo,
        "Source": gh_repo
    },  # Optional
)
