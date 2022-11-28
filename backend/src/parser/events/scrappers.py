from .constants import (
    RECENT_EVENTS_BATCH_LIMIT,
    UFC_EVENTS_URL,
)
from src.parser.commons.scrappers import AbstractScrapper


class LatestEventsScrapper(AbstractScrapper):
    url: str = UFC_EVENTS_URL

    def __init__(self, limit: int = RECENT_EVENTS_BATCH_LIMIT):
        super().__init__()
        self.limit = limit

    @property
    def data(self) -> list[dict]:
        events_list = []
        events = self.content.find(id="recent_tab").find_all('tr')[1:(self.limit+1)]
        for event in events:
            tds = event.find_all('td')
            events_list.append({
                'date': tds[0].meta['content'],
                'href': tds[1].a['href'],
                'name': tds[1].span.text
            })
        return events_list
