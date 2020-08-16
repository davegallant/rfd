import re
from colorama import Fore, Style
from . import API_BASE_URL
from .scores import calculate_score, get_vote_color

# pylint: disable=old-style-class
class Thread:
    def __init__(self, title, dealer_name, score, url, views):
        self.dealer_name = dealer_name
        self.score = score
        self.title = title
        self.url = url
        self.views = views

    def __repr__(self):
        return "Thread(%s)" % self.title


def build_web_path(slug):
    return "{}{}".format(API_BASE_URL, slug)


def get_dealer(topic):
    dealer = None
    if topic.get("offer"):
        dealer = topic.get("offer").get("dealer_name")
    return dealer


def parse_threads(threads):
    """Parse topics list api response into digestible list.

    Arguments:
        threads {dict} -- topics response from rfd api

    Returns:
        list(dict) -- digestible list of threads
    """
    parsed_threads = []
    if threads is None:
        return []
    for topic in threads:
        parsed_threads.append(
            Thread(
                title=topic.get("title"),
                dealer_name=get_dealer(topic),
                score=calculate_score(topic),
                url=build_web_path(topic.get("web_path")),
                views=topic.get("total_views"),
            )
        )
    return parsed_threads


def sort_threads(threads, sort_by):
    """Sort threads by an attribute"""
    if sort_by is None:
        return threads
    assert sort_by in ["views", "score", "title"]
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


def generate_thread_output(threads):
    for count, thread in enumerate(threads, 1):
        output = ""
        dealer = thread.dealer_name
        if dealer and dealer is not None:
            dealer = "[" + dealer + "] "
        else:
            dealer = ""
        output += (
            " "
            + str(count)
            + "."
            + get_vote_color(thread.score)
            + Fore.RESET
            + "%s%s" % (dealer, thread.title)
            + Fore.LIGHTYELLOW_EX
            + " (%d views)" % thread.views
            + Fore.RESET
        )
        output += Fore.BLUE + " {}".format(thread.url)
        output += Style.RESET_ALL
        output += "\n\n"
        yield output
