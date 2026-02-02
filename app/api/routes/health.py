from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

@router.get("/health")
async def health_check():
    """
    Health check endpoint to verify service status.
    Returns current timestamp and service status.
    """
    return {
        "status": "healthy",
        "service": "video-intelligence-backend",
        "timestamp": datetime.utcnow().isoformat(),
        "version": "1.0.0"
    }

@router.get("/")
async def root():
    """
    Root endpoint with basic service information.
    """
    return {
        "service": "Video Intelligence Backend",
        "version": "1.0.0",
        "docs": "/docs",
        "health": "/health"
    }
