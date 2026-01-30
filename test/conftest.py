from sqlalchemy import create_engine
from app.core.database import Base
from app.core.config import settings


def pytest_sessionstart(session):
    """
    Create database tables at the start of the test session.
    Ensures schema exists for SQLite-based test runs (CI).
    """
    engine = create_engine(settings.DATABASE_URL)
    Base.metadata.create_all(bind=engine)
