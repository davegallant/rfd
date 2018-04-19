import io  # for python2
from os import path
from setuptools import setup
try:  # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:  # for pip <= 9.0.3
    from pip.req import parse_requirements
from version import __version__ as version

WORKING_DIR = path.abspath(path.dirname(__file__))

# Get long description from reStructuredTExt
with io.open(path.join(WORKING_DIR, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

# read requirements.txt and load into list
REQUIREMENTS_TXT = parse_requirements(
    path.join(WORKING_DIR, "requirements.txt"), session='my_session')
REQUIREMENTS = [str(r.req) for r in REQUIREMENTS_TXT]

setup(
    author='Dave Gallant',
    author_email='davegallant@gmail.com',
    description='CLI for RedFlagDeals.com',
    entry_points={
        'console_scripts': [
            'rfd = rfd.rfd_cli:cli',
        ],
    },
    install_requires=REQUIREMENTS,
    keywords='cli redflagdeals',
    license='Apache License, Version 2.0',
    long_description=long_description,
    name='rfd',
    packages=['rfd'],
    url='https://github.com/davegallant/rfd_cli',
    version=version,
)
