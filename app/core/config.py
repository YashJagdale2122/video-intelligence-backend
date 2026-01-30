from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/video_intelligence"

    class Config:
        env_file = ".env"


settings = Settings()
