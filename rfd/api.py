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


def get_posts(post, count=5, tail=False, per_page=40):
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
    total_posts = response.json().get('pager').get('total')
    total_pages = response.json().get('pager').get('total_pages')

    if count == 0:
        pages = total_pages
    if count > per_page:
        if count > total_posts:
            count = total_posts
        pages = ceil(count / per_page)
    else:
        if tail:
            pages = total_pages
        else:
            pages = 1

    if tail:
        start_page = ceil((total_posts + 1 - count) / per_page)
        start_post = (total_posts + 1 - count) % per_page
        if start_post == 0:
            start_post = per_page
    else:
        start_page, start_post = 0, 0

    # Go through as many pages as necessary
    for page in range(start_page, pages + 1):
        response = requests.get(
            "https://forums.redflagdeals.com/api/topics/{}/posts?per_page={}&page={}".format(post_id,
                                                                                             get_safe_per_page(
                                                                                                 per_page),
                                                                                             page))

        users = users_to_dict(response.json().get('users'))

        _posts = response.json().get('posts')

        # Determine which post to start with (for --tail)
        if page == start_page and not start_post == 0:
            if tail:
                _posts = _posts[start_post - 1:]
            else:
                _posts = _posts[:start_post]

        for _post in _posts:
            count -= 1
            if count < 0:
                return
            # Sometimes votes is null
            if _post.get('votes') is not None:
                calculated_score = get_vote_score(_post.get('votes').get(
                    'total_up'), _post.get('votes').get('total_down'))
            else:
                calculated_score = 0
            yield{
                'body': strip_html(_post.get('body')),
                'score': calculated_score,
                'user': users[_post.get('author_id')],
            }
