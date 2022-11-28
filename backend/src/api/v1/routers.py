from fastapi import APIRouter

from .events import routers as event_routers


api_v1_router = APIRouter(prefix="/api/v1")

api_v1_router.include_router(event_routers.router)
