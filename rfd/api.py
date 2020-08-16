"""RFD API."""

try:
    from json.decoder import JSONDecodeError
except ImportError:
    JSONDecodeError = ValueError
import logging
import requests
from . import API_BASE_URL
from .posts import Post
from .scores import calculate_score
from .utils import is_int, strip_html, is_valid_url


def extract_post_id(url):
    return url.split("/")[3].split("-")[-1]


def get_safe_per_page(limit):
    """Ensure that per page limit is between 5-40"""
    if limit < 5:
        return 5
    if limit > 40:
        return 40
    return limit


def create_user_map(users):
    """Create a map of user ids to usernames."""
    m = dict()
    for user in users:
        m[user.get("user_id")] = user.get("username")
    return m


def get_threads(forum_id, pages):
    """Get threads from rfd api

    Arguments:
        forum_id {int} -- forum id
        pages {int} -- the number of pages of threads to collect

    Returns:
        dict -- api response
    """
    threads = []
    try:
        for page in range(1, pages + 1):
            response = requests.get(
                "{}/api/topics?forum_id={}&per_page=40&page={}".format(
                    API_BASE_URL, forum_id, page
                )
            )
            if response.status_code != 200:
                raise Exception("When collecting threads, received a status code: %s" % response.status_code)
            threads += response.json().get("topics")
    except JSONDecodeError as err:
        logging.error("Unable to decode threads. %s", err)
    return threads


def get_posts(post):
    """Retrieve posts from a thread.

    Args:
        post (str): either full url or postid

    Yields:
        list(Post): Posts
    """
    if is_valid_url(post):
        post_id = extract_post_id(post)
    elif is_int(post):
        post_id = post
    else:
        raise ValueError()

    response = requests.get(
        "{}/api/topics/{}/posts?per_page=40&page=1".format(API_BASE_URL, post_id)
    )

    total_pages = response.json().get("pager").get("total_pages")

    for page in range(0, total_pages + 1):
        response = requests.get(
            "{}/api/topics/{}/posts?per_page={}&page={}".format(
                API_BASE_URL, post_id, 40, page
            )
        )
        users = create_user_map(response.json().get("users"))

        posts = response.json().get("posts")

        for i in posts:
            # Sometimes votes is null
            if i.get("votes") is not None:
                calculated_score = calculate_score(i)
            else:
                calculated_score = 0
            yield Post(
                body=strip_html(i.get("body")),
                score=calculated_score,
                user=users[i.get("author_id")],
            )
