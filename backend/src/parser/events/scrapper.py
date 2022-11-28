from .constants import UFC_EVENTS_URL
from ..commons.scrappers import BaseSherdogScrapper


class LatestEventsScrapper(BaseSherdogScrapper):
    url: str = UFC_EVENTS_URL

    def parse(self):
        return self.content
