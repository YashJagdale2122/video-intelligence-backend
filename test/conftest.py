from app.core.database import Base, engine


def pytest_sessionstart(session):
    Base.metadata.create_all(bind=engine)
