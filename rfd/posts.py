# pylint: disable=old-style-class
import os
from colorama import Fore, Style
from .scores import get_vote_color

class Post:
    def __init__(self, body, score, user):
        self.body = body
        self.score = score
        self.user = user

def get_terminal_width():
    _, columns = os.popen("stty size", "r").read().split()
    return int(columns)

def generate_posts_output(posts):
    output = ""
    output += ("-" * get_terminal_width())
    for post in posts:
        output += (
            " -"
            + get_vote_color(post.score)
            + Fore.RESET
            + post.body
            + Fore.YELLOW
            + " ({})".format(post.user)
        )
        output += (Style.RESET_ALL)
        output += "\n"
        output += ("-" * get_terminal_width())
        output += "\n"
    return output
