def search_threads(threads, keyword=None):
    """Match deal title and dealer names with keyword specified."""

    if keyword is None:
        return

    keyword = str(keyword)

    for deal in threads:
        if keyword.lower() in deal.title.lower() or (
            deal.dealer_name and keyword.lower() in deal.dealer_name.lower()
        ):
            yield deal
