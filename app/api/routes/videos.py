from fastapi import APIRouter, UploadFile, File, Form, HTTPException, Depends
from typing import Optional
from sqlalchemy.orm import Session

from app.api.schemas.video import (VideoIngestResponse, VideoStatusResponse, VideoListResponse)
from app.api.dependencies import get_db
from app.services.video_service import VideoService
from app.domain.enums import SourceType

router = APIRouter(prefix="/api/v1/videos", tags=["Videos"])


@router.post("", response_model=VideoIngestResponse)
async def ingest_video(
    file: UploadFile | None = File(None),
    video_url: str | None = Form(None),
    db : Session = Depends(get_db)
):
    if not file and not video_url:
        raise HTTPException(
            status_code=400,
            detail="File or Video_URL is required"
        )

    if file and video_url:
        raise HTTPException(
            status_code=400,
            detail="Provide only one input"
        )

    service = VideoService(db)

    if file:
        video = service.ingest_video(
            source_type = SourceType.UPLOAD,
            source_url = None,
            storage_path = f"/tmp/{file.filename}"
        )
    else:
        video = service.ingest_video(
            source_type = SourceType.URL,
            source_url = video_url,
            storage_path = "remote"
        )

    return VideoIngestResponse(
        video_id=str(video.id),
        status=video.status,
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
