from fastapi import APIRouter, Depends

from app.config import Settings, get_settings

router = APIRouter()


@router.get("/health")
async def health(settings: Settings = Depends(get_settings)):
    return {
        "health": "healthy",
        "environment": settings.environment,
        "testing": settings.testing,
    }
