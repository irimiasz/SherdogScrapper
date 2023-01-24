import datetime

from pydantic import BaseModel


class Fighter(BaseModel):
    name: str
    href: str


class Fight(BaseModel):
    fighters: list[Fighter]


class FightList(BaseModel):
    fights: list[Fight]


class Event(BaseModel):
    name: str
    href: str
    date: datetime.date


class EventList(BaseModel):
    events: list[Event]
