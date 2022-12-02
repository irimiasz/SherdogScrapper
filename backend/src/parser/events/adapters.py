from datetime import datetime

from src.parser.commons.adapters import (
    AbstractAdapter,
    ScrapperDataSetupMixin,
    SubAdapterDataSetupMixin,
)
from src.parser.commons.constants import SHERDOG_URL_PREFIX

from .models import (
    Event,
    EventList,
)
from .scrappers import LatestEventsScrapper


class EventAdapter(AbstractAdapter, SubAdapterDataSetupMixin):
    model_class = Event

    def to_dict(self):
        return {
            'name': self.data["name"],
            "href": SHERDOG_URL_PREFIX + self.data["href"],
            "date": datetime.strptime(self.data["date"][:10], "%Y-%m-%d").date()
        }


class EventListAdapter(AbstractAdapter, ScrapperDataSetupMixin):
    scrapper_class = LatestEventsScrapper
    model_class = EventList

    def to_dict(self):
        return {
            'events': [
                EventAdapter(data=event).to_dict() for event in self.data
            ]
        }

