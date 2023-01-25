import random
import re

from datetime import datetime

from src.parser.commons.adapters import (
    AbstractAdapter,
    ScrapperDataSetupMixin,
    SubAdapterDataSetupMixin,
)

from .models import Event, EventList, Fight, Fighter, FightList
from .scrappers import (
    EventFightsScrapper,
    LatestEventsScrapper,
)


class EventAdapter(AbstractAdapter, SubAdapterDataSetupMixin):
    model_class = Event

    def to_dict(self):
        return {
            "name": self.data["name"],
            "href": self.data["href"].split("/")[-1],
            "date": datetime.strptime(self.data["date"][:10], "%Y-%m-%d").date(),
        }


class EventListAdapter(AbstractAdapter, ScrapperDataSetupMixin):
    scrapper_class = LatestEventsScrapper
    model_class = EventList

    def to_dict(self):
        return {"events": [EventAdapter(data=event).to_dict() for event in self.data]}


class FighterAdapter(AbstractAdapter, SubAdapterDataSetupMixin):
    model_class = Fighter

    def to_dict(self) -> dict:
        return {
            "name": re.sub(r"(\w)([A-Z])", r"\1 \2", self.data["name"]),
            "href": self.data["href"],
        }


class FightAdapter(AbstractAdapter, SubAdapterDataSetupMixin):
    model_class = Fight

    def to_dict(self) -> dict:
        return {
            "fighters": random.sample(
                [FighterAdapter(data=fighter).to_dict() for fighter in self.data], 2
            )
        }


class FightListAdapter(AbstractAdapter, ScrapperDataSetupMixin):
    scrapper_class = EventFightsScrapper
    model_class = FightList

    def to_dict(self) -> dict:
        from logging import getLogger

        log = getLogger(__name__)
        log.warning(self.data)
        return {"fights": [FightAdapter(data=fight).to_dict() for fight in self.data]}
