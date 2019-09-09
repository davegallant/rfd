from rfd.api import build_web_path, extract_post_id, parse_threads


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

    assert len(parse_threads(threads_api_response, 10)) == len(
        [
            {
                "score": 0,
                "title": "[Sponsored] 3 Months Free, Cable 75M, Unlimited Internet $34.99/30 "
                "Days, Free Installation/Modem Rental",
                "url": "https://forums.redflagdeals.com/carrytel-sponsored-3-months-free-cable-75m-unlimited-internet-34-99-30-days-free-installation-modem-rental-2197859/",
            },
            {
                "score": 92,
                "title": "WyzeCam 1080p HD Wireless Smart Home Camera v2 $37.49",
                "url": "https://forums.redflagdeals.com/amazon-ca-wyzecam-1080p-hd-wireless-smart-home-camera-v2-37-49-2191108/",
            },
            {
                "score": 8,
                "title": "Jabra Elite 65T $169.99",
                "url": "https://forums.redflagdeals.com/best-buy-jabra-elite-65t-169-99-2197916/",
            },
            {
                "score": 1,
                "title": "Glad Cling Wrap Plastic Wrap, 300 Metre Roll - best price $9.47",
                "url": "https://forums.redflagdeals.com/amazon-ca-glad-cling-wrap-plastic-wrap-300-metre-roll-best-price-9-47-2198211/",
            },
            {
                "score": 17,
                "title": "Firman 3300 inverter generator $599",
                "url": "https://forums.redflagdeals.com/costco-firman-3300-inverter-generator-599-2195171/",
            },
            {
                "score": 3,
                "title": "HOT - KitchenAid Stand Mixer - $199",
                "url": "https://forums.redflagdeals.com/walmart-hot-kitchenaid-stand-mixer-199-2198199/",
            },
            {
                "score": -1,
                "title": "Seagate Expansion 4TB Portable External Hard Drive USB 3.0 "
                "(STEA4000400) $119.92",
                "url": "https://forums.redflagdeals.com/amazon-ca-seagate-expansion-4tb-portable-external-hard-drive-usb-3-0-stea4000400-119-92-2198164/",
            },
            {
                "score": 0,
                "title": "WORKSHOP Wet Dry Vacs Ash Vacuum Cleaner WS0500ASH, 5-Gallon Ash "
                "Vac 65% Off, Now: $48.54",
                "url": "https://forums.redflagdeals.com/workshop-wet-dry-vacs-ash-vacuum-cleaner-ws0500ash-5-gallon-ash-vac-65-off-now-48-54-2198212/",
            },
            {
                "score": 4,
                "title": "NBA 2K18 (Nintendo Switch) -$19.99 or $16.99 PM",
                "url": "https://forums.redflagdeals.com/the-source-nba-2k18-nintendo-switch-19-99-16-99-pm-2198191/",
            },
            {
                "score": 5,
                "title": "CROCS.CA 40%OFF Select style - at checkout",
                "url": "https://forums.redflagdeals.com/crocs-crocs-ca-40-off-select-style-checkout-2198145/",
            },
        ]
    )

    assert len(parse_threads(None, 10)) == 0
