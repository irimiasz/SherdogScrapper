import requests
from abc import (
    ABC,
    abstractmethod,
)
from bs4 import BeautifulSoup

from .constants import MOCKED_HEADER


class AbstractScrapper(ABC):
    url: str = None

    @property
    def _html_content(self):
        return requests.get(self.url, headers=MOCKED_HEADER).content

    @property
    def content(self) -> BeautifulSoup:
        return BeautifulSoup(self._html_content, "html.parser")

    @property
    @abstractmethod
    def data(self) -> dict:
        raise NotImplementedError()
