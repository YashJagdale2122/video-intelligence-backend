from typing import Optional
from pydantic import BaseModel, HttpUrl, Field


class VideoIngestResponse(BaseModel):
    video_id: str
    status: str
    message: str


class VideoStatusResponse(BaseModel):
    video_id: str
    status: str
    metadata: Optional[dict] = None
    nlp_result: Optional[dict] = None
    cv_result: Optional[dict] = None
    risk_analysis: Optional[dict] = None
    errors: Optional[list] = None

class VideoListItem(BaseModel):
    video_id: str
    status: str
    created_at: str


class VideoListResponse(BaseModel):
    items: list[VideoListItem]
    total: int
