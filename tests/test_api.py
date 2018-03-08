from rfd.api import build_web_path, extract_post_id


def test_build_web_path():
    assert build_web_path("/test") == "https://forums.redflagdeals.com/test"


def test_extract_post_id():
    assert extract_post_id("https://forums.redflagdeals.com/targeted-bob-2173603/120") == '2173603'
    assert extract_post_id("http://forums.redflagdeals.com/targeted-2173604/120") == '2173604'
