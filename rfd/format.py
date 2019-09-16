"""Formatting utils"""

try:
    from urllib.parse import urlparse  # python 3
except ImportError:
    from urlparse import urlparse  # python 2
from bs4 import BeautifulSoup


def strip_html(text):
    return BeautifulSoup(text, "html.parser").get_text()


def is_valid_url(url):
    result = urlparse(url)
    return all([result.scheme, result.netloc, result.path])
