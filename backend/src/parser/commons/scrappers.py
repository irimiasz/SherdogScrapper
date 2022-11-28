import requests
from abc import (
    ABC,
    abstractmethod,
)
from bs4 import BeautifulSoup


class BaseSherdogScrapper(ABC):
    url: str = None

    @property
    def _html_content(self):
        return requests.get(self.url).content

    @property
    def content(self) -> BeautifulSoup:
        return BeautifulSoup(self._html_content, "html.parser")

    @abstractmethod
    def parse(self) -> dict:
        raise NotImplementedError()
