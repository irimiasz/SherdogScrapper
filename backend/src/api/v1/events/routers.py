from fastapi import (
    APIRouter,
    Query,
)

from src.parser.events.adapters import EventListAdapter
from src.parser.events.models import EventList

router = APIRouter(prefix="/events")


@router.get("/latest")
async def latest(limit: int = Query(default=10, gt=0, lt=20)) -> EventList:
    return EventListAdapter(limit=limit).to_dict()
