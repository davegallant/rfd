import re


def search_threads(threads, regex):
    """Match deal title and dealer names with regex specified."""

    regexp = re.compile(str(regex).lower())

    for deal in threads:

        if regexp.search(deal.title.lower()) or (
            deal.dealer_name and regexp.search(deal.dealer_name.lower())
        ):
            yield deal
