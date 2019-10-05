"""RFD API."""

try:
    from json.decoder import JSONDecodeError
except ImportError:
    JSONDecodeError = ValueError
import logging
import requests
from .constants import API_BASE_URL
from .format import strip_html, is_valid_url
from .models import Post
from .scores import calculate_score
from .utils import is_int


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


def get_threads(forum_id, limit, page=1):
    """Get threads from rfd api

    Arguments:
        forum_id {int} -- forum id
        limit {[type]} -- limit number of threads returned

    Returns:
        dict -- api response
    """
    try:
        response = requests.get(
            "{}/api/topics?forum_id={}&per_page={}&page={}".format(
                API_BASE_URL, forum_id, get_safe_per_page(limit), page
            )
        )
        if response.status_code == 200:
            return response.json()
        logging.error("Unable to retrieve threads. %s", response.text)
    except JSONDecodeError as err:
        logging.error("Unable to retrieve threads. %s", err)
    return None


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
