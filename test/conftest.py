import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.database import Base
from app.core.config import settings
# Add project root to PYTHONPATH

def pytest_sessionstart(session):
    """
    Create database tables at the start of the test session.
    This ensures a clean schema for CI and local test runs.
    """
    engine = create_engine(settings.DATABASE_URL)
    Base.metadata.create_all(bind=engine)
