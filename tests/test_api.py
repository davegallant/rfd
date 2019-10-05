from rfd.api import extract_post_id
from rfd.parsing import build_web_path, parse_threads


def test_build_web_path():
    assert build_web_path("/test") == "https://forums.redflagdeals.com/test"


def test_extract_post_id():
    assert (
        extract_post_id("https://forums.redflagdeals.com/targeted-bob-2173603/120")
        == "2173603"
    )
    assert (
        extract_post_id("http://forums.redflagdeals.com/targeted-2173604/120")
        == "2173604"
    )


def test_parse_threads(threads_api_response):

    limit = 10
    threads = parse_threads(threads_api_response, limit)
    assert len(threads) == limit


def test_parse_threads_empty():

    assert parse_threads(None, 10) == []
