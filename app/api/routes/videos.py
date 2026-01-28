from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from typing import Optional

from app.api.schemas.video import (
    VideoIngestResponse,
    VideoStatusResponse,
    VideoListResponse
)

router = APIRouter(prefix="/api/v1/videos", tags=["Videos"])


@router.post("", response_model=VideoIngestResponse)
async def ingest_video(
    file: Optional[UploadFile] = File(None),
    video_url: Optional[str] = Form(None),
    title: Optional[str] = Form(None)
):
    if not file and not video_url:
        raise HTTPException(
            status_code=400,
            detail="Either file or video_url must be provided"
        )

    if file and video_url:
        raise HTTPException(
            status_code=400,
            detail="Provide only one of file or video_url"
        )

    return VideoIngestResponse(
        video_id="placeholder-id",
        status="UPLOADED",
        message="Video accepted for processing"
    )


@router.get("/{video_id}", response_model=VideoStatusResponse)
async def get_video_status(video_id: str):
    return VideoStatusResponse(
        video_id=video_id,
        status="PROCESSING"
    )


@router.get("", response_model=VideoListResponse)
async def list_videos():
    return VideoListResponse(
        items=[],
        total=0
    )
