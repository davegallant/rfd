def calculate_score(post):
    """Calculate either topic or post score. If votes cannot be retrieved, the score is 0.

    Arguments:
        post {dict} -- pass in the topic/post object

    Returns:
        int -- score
    """
    score = 0
    try:
        score = int(post.get("votes").get("total_up")) - int(
            post.get("votes").get("total_down")
        )
    except AttributeError:
        pass

    return score
