from fastapi import APIRouter

from src.parser.events.adapters import EventListAdapter
from src.parser.events.models import EventList

router = APIRouter(prefix="/events")


@router.get("/latest")
async def latest() -> EventList:
    return EventListAdapter(limit=3).to_dict()
