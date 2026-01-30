import uuid
from sqlalchemy import Column, String, Float, Text, Enum, ForeignKey, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.domain.enums import ProcessingStatus,SourceType
from app.core.db_types import JSONType

class Video(Base):
    __tablename__ = "videos"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    source_type = Column(Enum(SourceType), nullable=False)
    source_url = Column(Text, nullable=True)
    storage_path = Column(Text, nullable=False)

    duration = Column(Float, nullable=True)
    resolution = Column(String, nullable=True)
    size_mb = Column(Float, nullable=True)

    status = Column(Enum(ProcessingStatus), nullable=False)

    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True),server_default=func.now(), onupdate=func.now())

    ai_result = relationship("AIResult", back_populates="video", uselist=False)


class AIResult(Base):
    __tablename__ = "ai_results"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    video_id = Column(UUID(as_uuid=True), ForeignKey("videos.id"), nullable=False)

    nlp_result = Column(JSONType, nullable=True)
    cv_result = Column(JSONType, nullable=True)
    risk_result = Column(JSONType, nullable=True)
    errors = Column(JSONType, nullable=True)

    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True),server_default=func.now(), onupdate=func.now())

    video = relationship("Video", back_populates="ai_result")
