"""This module provides utility functions that are used within rfd"""
try:
    from urllib.parse import urlparse  # python 2
except ImportError:
    from urlparse import urlparse  # python 1
from bs4 import BeautifulSoup


def strip_html(text):
    return BeautifulSoup(text, "html.parser").get_text()


def is_valid_url(url):
    result = urlparse(url)
    return all([result.scheme, result.netloc, result.path])


def is_int(number):
    try:
        int(number)
        return True
    except ValueError:
        return False
