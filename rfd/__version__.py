# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from os.path import dirname, abspath, join


def load_version():
    with open(join(dirname(abspath(__file__)), "VERSION")) as handle:
        return handle.read()


version = load_version()
