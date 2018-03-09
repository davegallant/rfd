"""RFD API."""

from math import ceil
import requests
from bs4 import BeautifulSoup

try:
    from urllib.parse import urlparse  # python 3
except ImportError:
    from urlparse import urlparse  # python 2


def build_web_path(slug):
    return "https://forums.redflagdeals.com{}".format(slug)


def extract_post_id(url):
    return url.split('/')[3].split('-')[-1]


def is_int(number):
    try:
        int(number)
        return True
    except ValueError:
        return False


def get_vote_score(up_vote, down_vote):
    return up_vote - down_vote


def get_safe_per_page(limit):
    if limit < 5:
        return 5
    elif limit > 40:
        return 40
    return limit


def users_to_dict(users):
    users_dict = {}
    for user in users:
        users_dict[user.get('user_id')] = user.get('username')
    return users_dict


def strip_html(text):
    return BeautifulSoup(text, "html.parser").get_text()


def is_valid_url(url):
    result = urlparse(url)
    return all([result.scheme, result.netloc, result.path])


def get_threads(forum_id, limit):
    threads = []
    response = requests.get(
        "https://forums.redflagdeals.com/api/topics?forum_id={}&per_page={}".format(forum_id, get_safe_per_page(limit)))
    for topic in response.json().get('topics'):
        threads.append({
            'title': topic.get('title'),
            'score': get_vote_score(topic.get('votes').get('total_up'), topic.get('votes').get('total_down')),
            'url': build_web_path(topic.get('web_path')),
        })
    return threads[:limit]


def get_posts(post, count=5, tail=False):
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
        "https://forums.redflagdeals.com/api/topics/{}/posts?per_page=40&page=1".format(post_id))
    total_pages = response.json().get('pager').get('total_pages')

    if count == 0:
        pages = total_pages
    if count > 40:
        pages = ceil(count / 40)
    else:
        pages = 1

    if pages > total_pages:
        pages = total_pages

    # Go through as many pages as necessary
    for page in range(pages):
        page = page + 1  # page 0 causes issues
        response = requests.get(
            "https://forums.redflagdeals.com/api/topics/{}/posts?per_page={}&page={}".format(post_id,
                                                                                             get_safe_per_page(
                                                                                                 count),
                                                                                             page))

        users = users_to_dict(response.json().get('users'))
        for _post in response.json().get('posts'):
            # Sometimes votes is null
            if _post.get('votes') is not None:
                calculated_score = get_vote_score(_post.get('votes').get('total_up'), _post.get('votes').get('total_down'))
            else:
                calculated_score = 0
            yield{
                'body': strip_html(_post.get('body')),
                'score': calculated_score,
                'user': users[_post.get('author_id')],
            }
