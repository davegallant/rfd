import re
from . import API_BASE_URL
from .scores import calculate_score

# pylint: disable=old-style-class
class Thread:
    def __init__(self, title, dealer_name, score, url, total_views):
        self.dealer_name = dealer_name
        self.score = score
        self.title = title
        self.url = url
        self.total_views = total_views

    def __repr__(self):
        return "Thread(%s)" % self.title


def build_web_path(slug):
    return "{}{}".format(API_BASE_URL, slug)


def get_dealer(topic):
    dealer = None
    if topic.get("offer"):
        dealer = topic.get("offer").get("dealer_name")
    return dealer


def parse_threads(threads, limit):
    """Parse topics list api response into digestible list.

    Arguments:
        threads {dict} -- topics response from rfd api
        limit {int} -- limit number of threads returned

    Returns:
        list(dict) -- digestible list of threads
    """
    parsed_threads = []
    if threads is None:
        return []
    for count, topic in enumerate(threads.get("topics"), start=1):
        if count > limit:
            break
        parsed_threads.append(
            Thread(
                title=topic.get("title"),
                dealer_name=get_dealer(topic),
                score=calculate_score(topic),
                url=build_web_path(topic.get("web_path")),
                total_views=topic.get("total_views"),
            )
        )
    return parsed_threads


def sort_threads(threads, sort_by):
    """Sort threads by an attribute"""
    if sort_by is None:
        return threads
    assert sort_by in ["total_views", "score", "title"]
    threads = sorted(threads, key=lambda x: getattr(x, sort_by), reverse=True)
    return threads


def search_threads(threads, regex):
    """Match deal title and dealer names with regex specified."""

    regexp = re.compile(str(regex).lower())

    for deal in threads:

        if regexp.search(deal.title.lower()) or (
            deal.dealer_name and regexp.search(deal.dealer_name.lower())
        ):
            yield deal
