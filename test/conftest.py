from app.core.database import Base, engine


def pytest_sessionstart(session):
    """
    Create database tables on the SAME engine used by the application.
    This is critical for SQLite and CI environments.
    """
    Base.metadata.create_all(bind=engine)
