from fastapi import APIRouter, UploadFile, File, Form, HTTPException, Depends, BackgroundTasks

from typing import Optional
from sqlalchemy.orm import Session
from uuid import UUID
import uuid
from app.api.schemas.video import (VideoIngestResponse, VideoStatusResponse, VideoListResponse)
from app.api.dependencies import get_db
from app.services.video_service import VideoService
from app.domain.enums import SourceType


router = APIRouter(prefix="/api/v1/videos", tags=["Videos"])


@router.post("", response_model=VideoIngestResponse)
async def ingest_video(
    background_tasks: BackgroundTasks,
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

    background_tasks.add_task(
        service.process_video_stub,
        video.id
    )

    return VideoIngestResponse(
        video_id=str(video.id),
        status=video.status,
        message="Video accepted for processing"
    )


@router.get("/{video_id}", response_model=VideoStatusResponse)
async def get_video_status(video_id: uuid.UUID, db: Session = Depends(get_db)):

    service = VideoService(db)
    video = service.get_video(video_id)

    if not video:
        raise HTTPException(status_code=404, detail="Video not found")

    return VideoStatusResponse(
        video_id=str(video.id),
        source_type=video.source_type,
        status=video.status,
        storage_path=video.storage_path,
        created_at=video.created_at,
    )


@router.get("", response_model=VideoListResponse)
async def list_videos():
    return VideoListResponse(
        items=[],
        total=0
    )
