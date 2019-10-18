import io  # for python2
from os import path
from setuptools import setup, find_packages
from rfd.__version__ import version


def load_requirements(file_name):
    """ Reads and returns requirements """
    with io.open(path.join(WORKING_DIR, file_name)) as handle:
        raw_reqs = handle.read().strip().split("\n")
        reqs = [req for req in raw_reqs]
        return reqs


WORKING_DIR = path.abspath(path.dirname(__file__))
REQUIREMENTS = load_requirements("requirements.txt")
TEST_REQUIREMENTS = load_requirements("requirements_dev.txt")

# Get long description from README.md
with io.open(path.join(WORKING_DIR, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    author="Dave Gallant",
    description="CLI for RedFlagDeals.com",
    entry_points={"console_scripts": ["rfd = rfd.__main__:cli"]},
    include_package_data=True,
    install_requires=REQUIREMENTS,
    keywords="cli redflagdeals",
    license="Apache License, Version 2.0",
    long_description=long_description,
    long_description_content_type="text/markdown",
    name="rfd",
    packages=find_packages(),
    url="https://github.com/davegallant/rfd",
    version=version,
)
