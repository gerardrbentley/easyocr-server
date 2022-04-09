from fastapi import APIRouter, Depends

from app.config import get_settings, Settings


router = APIRouter()


@router.get("/health")
async def health(settings: Settings = Depends(get_settings)):
    return {
        "health": "healthy",
        "environment": settings.environment,
        "testing": settings.testing
    }