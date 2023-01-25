import requests

from .constants import MOCKED_HEADER


def get_site_content(url: str):
    return requests.get(url, headers=MOCKED_HEADER).content


def chunks(lst: list, amount: int) -> list[list]:
    for i in range(0, len(lst), amount):
        yield lst[i : i + amount]
