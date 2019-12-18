from .constants import API_BASE_URL
from .scores import calculate_score
from .models import Thread


def build_web_path(slug):
    return "{}{}".format(API_BASE_URL, slug)


def parse_threads(threads, limit):
    """parse topics list api response into digestible list.

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
                dealer_name=topic["offer"].get("dealer_name"),
                score=calculate_score(topic),
                url=build_web_path(topic.get("web_path")),
                total_views=topic.get("total_views"),
            )
        )
    return parsed_threads
