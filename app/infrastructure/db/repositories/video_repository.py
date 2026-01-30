from sqlalchemy.orm import Session
from uuid import UUID

from app.infrastructure.db.models import Video
from app.domain.enums import ProcessingStatus


class VideoRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_video(self, video: Video) -> Video:
        self.db.add(video)
        self.db.commit()
        self.db.refresh(video)
        return video

    def get_video_by_id(self, video_id: UUID) -> Video | None:
        return self.db.query(Video).filter(Video.id == video_id).first()

    def list_videos(self, limit: int = 10, offset: int = 0):
        return (
            self.db.query(Video)
            .order_by(Video.created_at.desc())
            .offset(offset)
            .limit(limit)
            .all()
        )

    def update_status(self, video_id: UUID, status: ProcessingStatus) -> Video | None:
        video = self.get_video_by_id(video_id)
        if not video:
            return None

        video.status = status
        self.db.commit()
        self.db.refresh(video)
        return video
