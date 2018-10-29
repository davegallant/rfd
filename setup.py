import io  # for python2
from os import path
from setuptools import setup, find_packages
from rfd.__version__ import version

WORKING_DIR = path.abspath(path.dirname(__file__))

# Get long description from README.md
with io.open(path.join(WORKING_DIR, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


setup(
    author="Dave Gallant",
    description="CLI for RedFlagDeals.com",
    entry_points={"console_scripts": ["rfd = rfd.rfd_cli:cli"]},
    install_requires=[
        "beautifulsoup4>=4.6.0",
        "click>=7.0",
        "colorama>=0.3.9",
        "requests>=2.18.0",
    ],
    keywords="cli redflagdeals",
    license="Apache License, Version 2.0",
    long_description=long_description,
    long_description_content_type="text/markdown",
    name="rfd",
    packages=find_packages(),
    url="https://github.com/davegallant/rfd_cli",
    version=version,
)
