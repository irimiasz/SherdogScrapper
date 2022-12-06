import requests

from .constants import MOCKED_HEADER


def get_site_content(url: str):
    return requests.get(url, headers=MOCKED_HEADER).content
