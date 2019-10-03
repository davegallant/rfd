from rfd.parsing import parse_threads
from rfd.api import get_threads


def search_threads(threads, pages=10, keyword=None):
    """Match deal title and dealer names with keyword specified."""

    for deal in threads:
        if keyword.lower() in deal.title.lower() or (
            deal.dealer_name and keyword.lower() in deal.dealer_name.lower()
        ):
            yield deal
