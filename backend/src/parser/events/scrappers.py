from .constants import (
    RECENT_EVENTS_BATCH_LIMIT,
    UFC_EVENT_URL_PREFIX,
    UFC_EVENTS_URL,
)
from src.parser.commons.scrappers import AbstractScrapper
from src.parser.commons.helpers import chunks
from src.parser.events.helpers import parse_fighter_span_intro_dict


class LatestEventsScrapper(AbstractScrapper):
    url: str = UFC_EVENTS_URL

    def __init__(self, limit: int = RECENT_EVENTS_BATCH_LIMIT):
        super().__init__()
        self.limit = limit

    @property
    def data(self) -> list[dict]:
        events_list = []
        events = self.content.find(id="recent_tab").find_all("tr")[1 : (self.limit + 1)]
        for event in events:
            tds = event.find_all("td")
            events_list.append(
                {
                    "date": tds[0].meta["content"],
                    "href": tds[1].a["href"],
                    "name": tds[1].span.text,
                }
            )
        return events_list


class EventFightsScrapper(AbstractScrapper):
    def __init__(self, event_name: str):
        self.url = f"{UFC_EVENT_URL_PREFIX}/{event_name}"
        super().__init__()

    @property
    def data(self) -> list[list[dict]]:
        main_event_fighters = self.content.find(class_="fight_card").find_all(
            itemprop="name"
        )
        non_main_event_fighters = self.content.find(class_="new_table_holder").find_all(
            "span", itemprop="name"
        )
        fights = chunks(main_event_fighters + non_main_event_fighters, 2)
        return [
            [parse_fighter_span_intro_dict(span) for span in fight] for fight in fights
        ]
