from abc import (
    ABC,
    abstractmethod,
)
from bs4 import BeautifulSoup

from .helpers import get_site_content


class AbstractScrapper(ABC):
    url: str = None

    def __init__(self):
        self.content = BeautifulSoup(get_site_content(self.url), "html.parser")

    @property
    @abstractmethod
    def data(self) -> dict:
        raise NotImplementedError()
