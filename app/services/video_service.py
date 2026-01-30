from uuid import uuid4
from uuid import UUID
from sqlalchemy.orm import Session

from app.infrastructure.db.repositories.video_repository import VideoRepository
from app.infrastructure.db.models import Video
from app.domain.enums import ProcessingStatus, SourceType


class VideoService:
    def __init__(self, db: Session):
        self.repo = VideoRepository(db)

    def ingest_video(
        self,
        source_type: SourceType,
        source_url: str | None,
        storage_path: str
    ) -> Video:
        video = Video(
            source_type=source_type,
            source_url=source_url,
            storage_path=storage_path,
            status=ProcessingStatus.UPLOADED
        )

        return self.repo.create_video(video)

    def get_video(self, video_id: UUID):
       return self.repo.get_video_by_id(video_id)
