from fastapi import APIRouter

from src.parser.events.scrapper import LatestEventsScrapper


router = APIRouter(prefix="/events")


@router.get("/latest")
async def latest():
    return {"response_code": 200}
