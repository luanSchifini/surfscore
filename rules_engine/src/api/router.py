from fastapi import APIRouter
from rules_engine.src.api.endpoints import scores

api_router = APIRouter()

api_router.include_router(scores.api_router, prefix="/scores", tags=["Scores"])
