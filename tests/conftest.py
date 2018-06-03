import json
import pytest


@pytest.fixture
def threads_api_response():
    with open("tests/mock_data/threads_api_response.json") as json_file:
        return json.load(json_file)
