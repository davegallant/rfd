import io  # for python2
from os import path
from setuptools import setup
from version import __version__ as version


here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with io.open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='rfd',
    version=version,
    packages=['rfd'],
    keywords='cli redflagdeals',
    install_requires=[
        'PyYAML>=3.11',
        'beautifulsoup4>=4.6.0',
        'click>=6.7',
        'colorama>=0.3.9',
        'pytest>=3.4.2',
        'requests>=2.18.4'
    ],
    url='https://github.com/davegallant/rfd_cli',
    license='Apache License, Version 2.0',
    author='Dave Gallant',
    author_email='davegallant@gmail.com',
    description='CLI for RedFlagDeals.com',
    long_description=long_description,
    entry_points={
        'console_scripts': [
            'rfd = rfd.rfd_cli:cli',
        ],
    },
)
