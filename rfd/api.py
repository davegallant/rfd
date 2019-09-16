"""RFD API."""

try:
    from json.decoder import JSONDecodeError
except ImportError:
    JSONDecodeError = ValueError
import logging
from math import ceil
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


def users_to_dict(users):
    """Create a dictionary of user ids to usernames."""
    users_dict = {}
    for user in users:
        users_dict[user.get("user_id")] = user.get("username")
    return users_dict


def get_threads(forum_id, limit):
    """Get threads from rfd api

    Arguments:
        forum_id {int} -- forum id
        limit {[type]} -- limit number of threads returned

    Returns:
        dict -- api response
    """
    try:
        response = requests.get(
            "{}/api/topics?forum_id={}&per_page={}".format(
                API_BASE_URL, forum_id, get_safe_per_page(limit)
            )
        )
        if response.status_code == 200:
            return response.json()
        logging.error("Unable to retrieve threads. %s", response.text)
    except JSONDecodeError as err:
        logging.error("Unable to retrieve threads. %s", err)
    return None


def get_posts(post, count=5, per_page=40):
    """Retrieve posts from a thread.

    Args:
        post (str): either post id or full url
        count (int, optional): Description

    Yields:
        list(dict): body, score, and user
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
    total_posts = response.json().get("pager").get("total")
    total_pages = response.json().get("pager").get("total_pages")

    if count == 0:
        pages = total_pages
    if count > per_page:
        if count > total_posts:
            count = total_posts
        pages = ceil(count / per_page)
    else:
        pages = 1

    for page in range(0, pages + 1):
        response = requests.get(
            "{}/api/topics/{}/posts?per_page={}&page={}".format(
                API_BASE_URL, post_id, get_safe_per_page(per_page), page
            )
        )
        users = users_to_dict(response.json().get("users"))

        posts = response.json().get("posts")

        for i in posts:
            count -= 1
            if count < 0:
                return
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
