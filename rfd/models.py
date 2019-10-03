# pylint: disable=old-style-class
class Thread:
    def __init__(self, title, dealer_name, score, url):
        self.dealer_name = dealer_name
        self.score = score
        self.title = title
        self.url = url

    def __repr__(self):
        return "Thread(%s)" % self.title


class Post:
    def __init__(self, body, score, user):
        self.body = body
        self.score = score
        self.user = user
